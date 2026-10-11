"""Three valued applicability engine for the Ikhtibar checklist.

Principles
- An answer that is missing or "unknown" never makes a condition true or false: the result is UNKNOWN.
- Applicability is the maintainer's proposal. Whether a source binds an entity is reported separately and is
  YES only when the answers settle that the entity is the stated actor. Nothing here is legal advice.
- Standard library only (the checklist is read from the JSON mirror of data/checklist.yaml).
"""
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

TRUE, FALSE, UNKNOWN = "TRUE", "FALSE", "UNKNOWN"
APPLIES, NOT_APPLY = "APPLIES", "DOES_NOT_APPLY"

def load_checklist(path=None):
    return json.loads(Path(path or DATA / "checklist.json").read_text(encoding="utf-8"))

def load_schema(path=None):
    return json.loads(Path(path or DATA / "answers_schema.json").read_text(encoding="utf-8"))

def load_rows(path=None):
    with open(path or DATA / "evidence_table.csv", encoding="utf-8", newline="") as f:
        return {r["row_id"]: r for r in csv.DictReader(f)}

class AnswerError(ValueError):
    pass

def validate_answers(answers, schema):
    """Return a cleaned dict. Raises AnswerError on a key or value that is not in the schema."""
    qs = schema["questions"]
    out = {}
    for k, v in answers.items():
        if k not in qs:
            raise AnswerError(f"unknown question '{k}'. Valid: {', '.join(sorted(qs))}")
        q = qs[k]
        if v is None or v == "unknown":
            continue
        allowed = set(q["values"])
        if q["type"] == "multi":
            vals = v if isinstance(v, list) else [x.strip() for x in str(v).split(",") if x.strip()]
            if "unknown" in vals:
                continue
            bad = [x for x in vals if x not in allowed]
            if bad:
                raise AnswerError(f"invalid value(s) {bad} for '{k}'. Valid: {', '.join(sorted(allowed))}")
            out[k] = sorted(set(vals))
        else:
            if v not in allowed:
                raise AnswerError(f"invalid value '{v}' for '{k}'. Valid: {', '.join(sorted(allowed))}")
            out[k] = v
    return out

def _not(t):
    return {TRUE: FALSE, FALSE: TRUE, UNKNOWN: UNKNOWN}[t]

def evaluate(cond, a):
    """Kleene three valued evaluation of a condition against answers `a` (already validated)."""
    if not isinstance(cond, dict) or len(cond) != 1:
        raise ValueError(f"bad condition: {cond!r}")
    (op, arg), = cond.items()
    if op == "always":
        return TRUE if arg else FALSE
    if op == "eq":
        key, val = arg
        if key not in a:
            return UNKNOWN
        return TRUE if a[key] == val else FALSE
    if op == "in":
        key, vals = arg
        if key not in a:
            return UNKNOWN
        return TRUE if a[key] in vals else FALSE
    if op == "tri":
        # known value that is neither listed as true nor as false leaves the item UNKNOWN
        key, tvals, fvals = arg
        if key not in a:
            return UNKNOWN
        if a[key] in tvals: return TRUE
        if a[key] in fvals: return FALSE
        return UNKNOWN
    if op == "contains":
        key, val = arg
        if key not in a:
            return UNKNOWN
        return TRUE if val in a[key] else FALSE
    if op == "any_contains":
        key, vals = arg
        if key not in a:
            return UNKNOWN
        return TRUE if any(v in a[key] for v in vals) else FALSE
    if op == "not":
        return _not(evaluate(arg, a))
    if op in ("all", "any"):
        res = [evaluate(c, a) for c in arg]
        if op == "all":
            if FALSE in res: return FALSE
            if UNKNOWN in res: return UNKNOWN
            return TRUE
        if TRUE in res: return TRUE
        if UNKNOWN in res: return UNKNOWN
        return FALSE
    raise ValueError(f"unknown operator {op}")

def _row_binding(row, rb, a):
    st = row["binding_status"]
    if st in ("guidance", "voluntary"):
        return "NO", "source is not binding (" + st + ")"
    if st == "ambiguous":
        return "UNKNOWN", "binding status of the source is ambiguous"
    rule = rb["by_row"].get(row["row_id"]) or rb["by_family"].get(row["family"])
    if not rule:
        return "UNKNOWN", f"{st} in the source, but no applicability rule is encoded; read the row to see the actor and trigger"
    r = evaluate(rule["applies_when"], a)
    if r == FALSE:
        return "NO", f"stated actor is {rule['actor']}; your answers say otherwise"
    if r == UNKNOWN:
        return "UNKNOWN", f"stated actor is {rule['actor']}; your answers do not settle whether you are in scope"
    if st == "conditional" or rule.get("still_conditional"):
        return "UNKNOWN", f"stated actor is {rule['actor']} and your answers match, but a trigger or scope question in the source is not settled by the answers"
    return "YES", f"stated actor is {rule['actor']} and your answers match"

def run(answers, checklist=None, schema=None, rows=None):
    checklist = checklist or load_checklist()
    schema = schema or load_schema()
    rows = rows or load_rows()
    a = validate_answers(answers, schema)
    results = []
    for it in checklist["items"]:
        t = evaluate(it["applies_when"], a)
        state = {TRUE: APPLIES, FALSE: NOT_APPLY, UNKNOWN: UNKNOWN}[t]
        srcs = []
        for rid in it["rows"]:
            row = rows[rid]
            binds, why = _row_binding(row, checklist["row_binding"], a)
            srcs.append({"row_id": rid, "framework": row["framework"], "clause": row["clause_or_page"],
                         "source_binding_status": row["binding_status"], "verification_status": row["verification_status"],
                         "binds_you": binds, "binds_you_reason": why, "source_url": row["source_url"]})
        settle = []
        if state == UNKNOWN:
            settle = [k for k in it.get("to_settle", []) if k not in a]
        results.append({"id": it["id"], "phase": it["phase"], "text": it["text"], "state": state,
                        "why": it["why"], "close_by": it.get("close_by", ""), "to_settle": settle, "templates": it.get("templates", []), "sources": srcs})
    notes = []
    if "hosting" in a:
        notes.append("hosting was recorded but no retrieved source sets a requirement keyed to where a system runs, so it settles no item.")
    summary = {s: sum(1 for r in results if r["state"] == s) for s in (APPLIES, NOT_APPLY, UNKNOWN)}
    return {"answers_used": a, "summary": summary, "items": results, "notes": notes,
            "disclaimer": "Research aid built from retrieved sources. Not legal advice. Applicability rules are proposals. UNKNOWN means the answers do not settle it."}
