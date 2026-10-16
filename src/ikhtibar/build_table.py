"""Build data/evidence_table.csv from raw inputs, verification results and patches.

Everything downstream (counts, matrix, report tables, checklist trace) is computed from the
output of this script. Run:  python -m ikhtibar.build_table
"""
import csv, glob, json, os, re, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "data"
TODAY = "2026-10-12"      # phase 2 check date (rounds 1 and 2)
P3_DATE = "2026-10-16"    # phase 3 check date (rounds 3 and 4)
P3 = D / "verification" / "phase3"

OUT_COLS = [
    "row_id", "family", "framework", "clause_or_page", "requirement_paraphrase", "binding_status",
    "what_is_tested", "who_tests", "source_url", "retrieved_on", "last_checked_on", "next_review_by",
    "interpretation_note", "conflict_flag", "row_type", "primary_test_type", "secondary_test_types",
    "test_stage", "coding_note", "evidence_grade", "language_read",
    "verification_status", "verdict_raw", "verdict_adjusted", "verification_round", "sample_type",
    "text_basis", "block_type", "access_path", "document_to_download", "verification_note",
    "phase1_provisional", "headline_include",
    "verdict_p2_adjusted", "p3_sample", "p3_recheck_verdict", "p3_final_verdict",
]

def read(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def load_policy():
    return json.load(open(D / "review_policy.json", encoding="utf-8"))

def next_review(row, policy):
    base = row["last_checked_on"] or row["retrieved_on"]
    fam = row["family"]
    days = policy["default_days"].get(row["binding_status"], policy["default_days"]["other"])
    for fam_prefix, d in policy["family_days"].items():
        if fam.startswith(fam_prefix):
            days = min(days, d)
    return (dt.date.fromisoformat(base) + dt.timedelta(days=days)).isoformat()

def classify_block(log):
    l = (log or "").lower()
    if "provenance_required" in l or "permission request" in l:
        return "permission_timeout"
    if "request rejected" in l or "403" in l or "requested url was rejected" in l:
        return "site_rejected"
    if "client_error" in l or "error while fetching" in l:
        return "fetch_error"
    return "other"

def adjust(v):
    """Date-only MINOR flags (retrieval date earlier than the check date) are not faults."""
    if v["verdict"] == "MINOR":
        fc = (v.get("failed_checks") or "").strip().lower()
        if fc == "date":
            return "PASS"
    return v["verdict"]

def main():
    policy = load_policy()
    phase1 = read(D / "inputs/evidence_table_phase1.csv")
    new = read(D / "inputs/new_uae_rows.csv")
    sets = json.load(open(D / "verification/sample_sets.json"))
    prov = set(sets["provisional"]) | set(sets["jtc"]) | set(sets["ukparl"])

    # verification results; round 2 (rres_*) overrides round 1 (vres_*) per row
    ver = {}
    for f in sorted(glob.glob(str(D / "verification/vres_*.csv"))):
        for r in read(f):
            r["_round"] = 1; r["_file"] = os.path.basename(f); ver[r["row_id"]] = r
    for f in sorted(glob.glob(str(D / "verification/rres_*.csv"))):
        for r in read(f):
            r["_round"] = 2; r["_file"] = os.path.basename(f)
            ver[r["row_id"]] = r
    ver2 = dict(ver)
    # phase 3: round 3 = research re-check (p3res_*), round 4 = final independent check (final/fv3_*)
    ver3, ver4 = {}, {}
    for f in sorted(glob.glob(str(P3 / "p3res_*.csv"))):
        for r in read(f):
            r["_round"] = 3; r["_file"] = os.path.basename(f); ver3[r["row_id"]] = r; ver[r["row_id"]] = r
    for f in sorted(glob.glob(str(P3 / "final" / "fv3_*.csv"))):
        for r in read(f):
            r["_round"] = 4; r["_file"] = os.path.basename(f); ver4[r["row_id"]] = r; ver[r["row_id"]] = r
    fresh3 = set()
    if (P3 / "final" / "sample_p3.json").exists():
        fresh3 = set(json.load(open(P3 / "final" / "sample_p3.json"))["fresh_random_seed_20261016"])

    rows = {}
    order = []
    for r in phase1:
        x = {c: r.get(c, "") for c in OUT_COLS}
        x["retrieved_on"] = r["retrieval_date"]
        x["sample_type"] = ""
        reason = ""
        if r["row_id"] in prov:
            reason = "yes: phase 1 verification or reading used a route not allowed by the access rule (browser style user agent, API, direct download or OCR)"
        elif "digitaldubai.ae" in r["source_url"] or r["row_id"] in {f"Saudi-{n:03d}" for n in range(18, 24)}:
            reason = "yes: phase 1 content was obtained by direct download or OCR, not by the standard fetch tool"
        x["phase1_provisional"] = reason
        x["language_read"] = ""
        rows[r["row_id"]] = x; order.append(r["row_id"])
    # new UAE rows with coding from round-2 verifiers
    for r in new:
        x = {c: r.get(c, "") for c in OUT_COLS}
        x["retrieved_on"] = r["retrieval_date"]
        v = ver.get(r["row_id"], {})
        for c in ["row_type", "primary_test_type", "secondary_test_types", "test_stage", "evidence_grade", "language_read"]:
            x[c] = v.get(c, "")
        x["conflict_flag"] = r.get("conflict_flag", "") or ""
        x["coding_note"] = "coded by independent verifier (proposal), not by the discovery agent"
        x["sample_type"] = "new_row_phase2"
        rows[r["row_id"]] = x; order.append(r["row_id"])
    # new phase 3 rows, proposed by research agents and checked by the final independent verifier
    for f in sorted(glob.glob(str(P3 / "p3new_*.csv"))):
        for r in read(f):
            x = {c: r.get(c, "") for c in OUT_COLS}
            x["retrieved_on"] = r["retrieval_date"]
            x["coding_note"] = "coded by phase 3 research agent (proposal)"
            x["sample_type"] = "new_row_phase3"
            x["phase1_provisional"] = ""
            rows[r["row_id"]] = x; order.append(r["row_id"])

    # apply patches
    fails = []
    patches = json.load(open(D / "patches.json", encoding="utf-8"))
    applied = {}
    for p in patches:
        rid = p["row_id"]
        if rid not in rows:
            fails.append((rid, "missing row")); continue
        if p["field"] == "verification_override":
            rows[rid].setdefault("_override", p["value"]); rows[rid]["_override"] = p["value"]
            applied.setdefault(rid, []).append(p["reason"]); continue
        f = p["field"]
        if p["op"] == "set":
            rows[rid][f] = p["value"]
        elif p["op"] == "append":
            rows[rid][f] = (rows[rid][f] + " " + p["value"]).strip()
        else:
            if p["old"] not in rows[rid][f]:
                fails.append((rid, f"replace target not found in {f}: {p['old'][:50]}")); continue
            rows[rid][f] = rows[rid][f].replace(p["old"], p["new"], 1)
        applied.setdefault(rid, []).append(f"{p['field']}: {p['reason']}".strip(": "))

    # verification fields
    for rid, x in rows.items():
        v = ver.get(rid)
        v2 = ver2.get(rid)
        x["verdict_p2_adjusted"] = adjust(v2) if v2 else ""
        x["p3_recheck_verdict"] = adjust(ver3[rid]) if rid in ver3 else ""
        x["p3_final_verdict"] = adjust(ver4[rid]) if rid in ver4 else ""
        x["p3_sample"] = ("fresh_random_seed_20261016" if rid in fresh3 else
                          "new_row_phase3" if x["sample_type"] == "new_row_phase3" else
                          "phase3_recheck" if rid in ver3 else "")
        if x["sample_type"] not in ("new_row_phase2", "new_row_phase3"):
            if rid in sets["fresh"]: x["sample_type"] = "fresh_random_seed_20261012"
            elif rid in sets["cited"]: x["sample_type"] = "cited_in_prose"
            elif rid in sets["must"]: x["sample_type"] = "targeted"
            elif v: x["sample_type"] = "targeted"
            else: x["sample_type"] = "not_rechecked"
            if rid in sets["cited"] and rid in sets["fresh"]: x["sample_type"] = "cited_in_prose"
        if v is None and x["sample_type"] == "new_row_phase3":
            x["verification_status"] = "NEW_UNCHECKED"
            x["verification_round"] = ""
        elif v is None:
            x["verification_status"] = ("UNVERIFIED_SOURCE_NOT_READ"
                                        if x["evidence_grade"].startswith("unverified") else "NOT_RECHECKED")
            x["verification_round"] = ""
            x["last_checked_on"] = ""
        else:
            raw = v["verdict"]; adj = adjust(v)
            x["verdict_raw"] = raw; x["verdict_adjusted"] = adj
            x["verification_round"] = str(v["_round"])
            x["text_basis"] = v.get("text_basis", "")
            if x["language_read"] == "" and v.get("language_read"):
                x["language_read"] = v["language_read"]
            if raw in ("PASS", "MINOR", "ERROR"):
                x["last_checked_on"] = P3_DATE if v["_round"] >= 3 else TODAY
                if raw == "PASS" or adj == "PASS":
                    x["verification_status"] = "VERIFIED"
                else:
                    x["verification_status"] = "VERIFIED_CORRECTED" if rid in applied else "VERIFIED_NOTE_ONLY"
                x["access_path"] = v.get("access_path") or "standard_fetch"
                x["block_type"] = ""; x["document_to_download"] = ""
                x["verification_note"] = (v.get("failed_checks") or "").strip()
                if raw in ("MINOR", "ERROR") and adj != "PASS" and rid not in applied:
                    x["verification_note"] += " | verifier fix (not applied): " + (v.get("suggested_fix") or "")[:400]
            elif raw == "UNVERIFIED_BLOCKED":
                x["verification_status"] = "UNVERIFIED_BLOCKED"
                x["block_type"] = classify_block(v.get("access_log"))
                x["access_path"] = "none"
                x["document_to_download"] = (v.get("suggested_fix") or "")[:500]
                x["verification_note"] = (v.get("access_log") or "")[:300]
            else:
                x["verification_status"] = "UNVERIFIABLE_OTHER"
                x["block_type"] = "truncated_or_unreadable"
                x["access_path"] = "none"
                x["document_to_download"] = (v.get("suggested_fix") or "")[:500]
                x["verification_note"] = (v.get("what_source_says") or "")[:300]
        if x.get("_override"):
            x["verification_status"] = x.pop("_override")
        if x["verification_status"] == "ERROR_WITHDRAWN":
            x["document_to_download"] = "IMDA Model AI Governance Framework for Agentic AI v1.5 PDF (download by hand and re-check s.2.3.x case study)"
        x.pop("_override", None)
        if rid in applied:
            x["verification_note"] = (x["verification_note"] + " | applied: " + "; ".join(applied[rid]))[:900]

    # headline inclusion: only rows with a readable, checked or phase-1-read source, not withdrawn
    for rid, x in rows.items():
        inc = x["verification_status"] in ("VERIFIED", "VERIFIED_CORRECTED", "VERIFIED_NOTE_ONLY", "NOT_RECHECKED")
        if x["evidence_grade"].startswith("unverified"):
            inc = False
        if x["evidence_grade"] == "catalogue-level only" and x["sample_type"] == "new_row_phase2":
            inc = False  # portal summary pages only
        x["headline_include"] = "yes" if inc else "no"
        x["next_review_by"] = next_review(x, policy)

    out = D / "evidence_table.csv"
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for rid in order:
            w.writerow(rows[rid])
    print("wrote", out, len(order), "rows; patch failures:", len(fails))
    for x in fails: print("  PATCH FAIL", x)
    return fails

if __name__ == "__main__":
    main()
