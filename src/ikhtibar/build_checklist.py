"""Mirror data/checklist.yaml and data/answers_schema.yaml to JSON (used by the stdlib only CLI).
Fails if a row id does not exist or a condition is malformed. Run: python -m ikhtibar.build_checklist
"""
import json, sys
from pathlib import Path
import yaml
from . import engine

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "data"

def check_cond(c, schema, where):
    (op, arg), = c.items()
    if op in ("all", "any"):
        for x in arg: check_cond(x, schema, where)
    elif op == "not":
        check_cond(arg, schema, where)
    elif op == "always":
        pass
    elif op == "tri":
        key, tv, fv = arg
        allowed = set(schema["questions"][key]["values"])
        for v in list(tv) + list(fv):
            if v not in allowed: raise SystemExit(f"{where}: value {v} not allowed for {key}")
    else:
        key, vals = arg
        if key not in schema["questions"]:
            raise SystemExit(f"{where}: unknown question {key}")
        allowed = set(schema["questions"][key]["values"])
        for v in (vals if isinstance(vals, list) else [vals]):
            if v not in allowed:
                raise SystemExit(f"{where}: value {v} not allowed for {key}")

def main():
    cl = yaml.safe_load(open(D / "checklist.yaml", encoding="utf-8"))
    sc = yaml.safe_load(open(D / "answers_schema.yaml", encoding="utf-8"))
    rows = engine.load_rows()
    for it in cl["items"]:
        for r in it["rows"]:
            if r not in rows:
                raise SystemExit(f"{it['id']}: row {r} not in evidence table")
        check_cond(it["applies_when"], sc, it["id"])
        for k in it.get("to_settle", []):
            if k not in sc["questions"]: raise SystemExit(f"{it['id']}: to_settle {k}")
    for k, rule in {**cl["row_binding"]["by_family"], **cl["row_binding"]["by_row"]}.items():
        check_cond(rule["applies_when"], sc, k)
    for k in cl["row_binding"]["by_row"]:
        if k not in rows: raise SystemExit(f"row_binding row {k} missing")
    (D / "checklist.json").write_text(json.dumps(cl, indent=1, ensure_ascii=False), encoding="utf-8")
    (D / "answers_schema.json").write_text(json.dumps(sc, indent=1, ensure_ascii=False), encoding="utf-8")
    print("checklist.json and answers_schema.json written;", len(cl["items"]), "items")

if __name__ == "__main__":
    main()
