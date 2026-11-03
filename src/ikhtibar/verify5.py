"""Statistics for the phase 5 fresh independent checks (task 3d).

Two groups, each checked by fresh verifiers who saw only the row and the rules (RULES_P5.md):
  existing: a seeded sample of rows already in the table (scripts/p5_draw_sample.py, seed 20261103)
  new:      the rows added in phase 5 from newly read instruments and the US candidate rows
Readable means the verifier could open the source and reach a verdict PASS, MINOR or ERROR. Blocked rows are reported
separately and are not counted as correct. An error is an ERROR verdict as graded by the verifier under the rules.
Pooled rates add to the frozen phase 3 and 4 fresh samples (data/phase5/frozen_v4/data_verification_phase4_stats_p4.json).
Output: data/verification/phase5/stats_p5.json. Run: python -m ikhtibar.verify5
"""
import csv, glob, json, collections
from pathlib import Path
from .completeness import wilson

ROOT = Path(__file__).resolve().parents[2]
P5 = ROOT / "data" / "verification" / "phase5"
READ = ("PASS", "MINOR", "ERROR")


def rd(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def load(prefix):
    out = {}
    for f in sorted(glob.glob(str(P5 / "raw" / f"{prefix}_res_*.csv"))):
        for r in rd(f):
            out[r["row_id"]] = r
    return out


def block_type(r):
    t = " ".join([r.get("failed_checks", ""), r.get("what_source_says", "")]).lower()
    if "allowlist" in t:
        return "session_allowlist"
    if "robots" in t:
        return "robots_disallowed"
    if "reject" in t or "403" in t or "site_block" in t:
        return "site_rejected"
    return "other"


def summarise(res, table):
    n = len(res)
    readable = [r for r in res.values() if r["verdict"] in READ]
    c = collections.Counter(r["verdict"] for r in res.values())
    errs = [r["row_id"] for r in readable if r["verdict"] == "ERROR"]
    faults = [r["row_id"] for r in readable if r["verdict"] in ("MINOR", "ERROR")]
    blocked = collections.Counter(block_type(r) for r in res.values() if r["verdict"] not in READ)
    fam = collections.defaultdict(lambda: {"sampled": 0, "readable": 0, "errors": 0})
    for k, r in res.items():
        f = table.get(k, {}).get("family", "")
        fam[f]["sampled"] += 1
        fam[f]["readable"] += r["verdict"] in READ
        fam[f]["errors"] += r["verdict"] == "ERROR"
    return {"n": n, "readable": len(readable), "readable_pct": round(100 * len(readable) / n, 1) if n else None,
            "verdicts": dict(c), "errors": len(errs), "error_rate_pct": round(100 * len(errs) / len(readable), 1) if readable else None,
            "error_rate_ci95": wilson(len(errs), len(readable)), "any_fault": len(faults),
            "any_fault_pct": round(100 * len(faults) / len(readable), 1) if readable else None,
            "any_fault_ci95": wilson(len(faults), len(readable)), "error_rows": errs, "blocked_by_type": dict(blocked),
            "by_family": {k: v for k, v in sorted(fam.items())},
            "bounds_error_pct": {"none_of_unreadable_in_error": round(100 * len(errs) / n, 1) if n else None,
                                 "all_of_unreadable_in_error": round(100 * (len(errs) + n - len(readable)) / n, 1) if n else None}}


def pooled(blocks, label):
    k = sum(b[0] for b in blocks)
    n = sum(b[1] for b in blocks)
    return {"label": label, "errors": k, "readable": n, "pct": round(100 * k / n, 1) if n else None, "ci95": wilson(k, n)}


def compute():
    table = {r["row_id"]: r for r in rd(ROOT / "data" / "evidence_table.csv")}
    ex, nw = load("p5v"), load("p5n")
    us = {r["row_id"]: r for r in rd(P5 / "p5res_us.csv")}
    out = {"seed": 20261103, "existing_sample": summarise(ex, table), "new_rows": summarise(nw, table),
           "us_candidate_rows": summarise(us, table)}
    frozen = json.loads((ROOT / "data" / "phase5" / "frozen_v4" / "data_verification_phase4_stats_p4.json").read_text(encoding="utf-8"))
    p = frozen["pooled_with_phase3_fresh_sample"]
    base = (p["errors"], p["readable"])
    e = out["existing_sample"]
    n_all = [out["new_rows"], out["us_candidate_rows"]]
    out["pooled"] = {
        "frozen_phase3_and_4": pooled([base], "fresh samples of phases 3 and 4 (frozen)"),
        "plus_phase5_existing_sample": pooled([base, (e["errors"], e["readable"])], "plus the phase 5 sample of existing rows"),
        "plus_phase5_existing_and_new_rows": pooled([base, (e["errors"], e["readable"])] + [(x["errors"], x["readable"]) for x in n_all],
                                                    "plus the phase 5 new rows and US candidate rows"),
        "new_rows_only": pooled([(x["errors"], x["readable"]) for x in n_all], "phase 5 new rows and US candidate rows only"),
    }
    out["note"] = ("Verifiers could read only a small share of the existing sample because the session allowed fetches only to addresses "
                   "seen in search results and the search budget was used up; blocked rows are not counted as correct.")
    return out


def main():
    out = compute()
    (P5 / "stats_p5.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    for k in ("existing_sample", "new_rows", "us_candidate_rows"):
        v = out[k]
        print(k, v["n"], "readable", v["readable"], "errors", v["errors"], v["verdicts"], v["blocked_by_type"])
    print(json.dumps(out["pooled"], indent=1))


if __name__ == "__main__":
    main()
