"""Compute every number quoted in the report, brief and README from data/evidence_table.csv.

Run: python -m ikhtibar.stats   (writes data/stats.json)
"""
import csv, json, math, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "data"
C = collections.Counter
BS = ["mandatory", "conditional", "voluntary", "guidance", "ambiguous"]

def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    den = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (round(100 * (c - h) / den, 1), round(100 * (c + h) / den, 1))

def load(path=None):
    with open(path or D / "evidence_table.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def verdict_tally(rows):
    c = C(r["verdict_adjusted"] for r in rows if r["verdict_adjusted"])
    verifiable = c["PASS"] + c["MINOR"] + c["ERROR"]
    k = c["ERROR"]
    return {"n_checked_rows": sum(c.values()), "PASS": c["PASS"], "MINOR": c["MINOR"], "ERROR": k,
            "UNVERIFIED_BLOCKED": c["UNVERIFIED_BLOCKED"], "UNVERIFIABLE_OTHER": c["UNVERIFIABLE_OTHER"],
            "verifiable": verifiable, "error_rate_pct": round(100 * k / verifiable, 1) if verifiable else None,
            "error_ci95_pct": wilson(k, verifiable),
            "any_fault_rate_pct": round(100 * (k + c["MINOR"]) / verifiable, 1) if verifiable else None}

def compute(rows=None):
    rows = rows or load()
    S = {}
    S["total_rows"] = len(rows)
    S["row_type"] = dict(C(r["row_type"] for r in rows))
    S["verification_status"] = dict(C(r["verification_status"] for r in rows))
    inc = [r for r in rows if r["headline_include"] == "yes"]
    tests_all = [r for r in rows if r["row_type"] == "test"]
    tests = [r for r in inc if r["row_type"] == "test"]
    S["test_rows_all"] = len(tests_all)
    S["test_rows_headline"] = len(tests)
    S["test_rows_excluded"] = len(tests_all) - len(tests)
    S["binding_headline"] = {b: sum(1 for r in tests if r["binding_status"] == b) for b in BS}
    S["binding_all_tests"] = {b: sum(1 for r in tests_all if r["binding_status"] == b) for b in BS}
    S["excluded_test_rows_by_status"] = dict(C(r["verification_status"] for r in tests_all if r["headline_include"] != "yes"))
    S["excluded_test_rows_by_family"] = dict(C(r["family"] for r in tests_all if r["headline_include"] != "yes"))
    # binding split among headline test rows, by family
    fam = {}
    for f in sorted({r["family"] for r in rows}):
        fr = [r for r in tests if r["family"] == f]
        fam[f] = {"rows": sum(1 for r in rows if r["family"] == f), "test_headline": len(fr),
                  **{b: sum(1 for r in fr if r["binding_status"] == b) for b in BS}}
    S["by_family"] = fam
    # verification
    cited = [r for r in rows if r["sample_type"] == "cited_in_prose"]
    fresh = [r for r in rows if r["sample_type"].startswith("fresh_random")]
    new = [r for r in rows if r["sample_type"] == "new_row_phase2"]
    targeted = [r for r in rows if r["sample_type"] == "targeted"]
    prov = [r for r in rows if r["phase1_provisional"].startswith("yes")]
    S["verification"] = {
        "cited_rows": {"n": len(cited), **verdict_tally(cited),
                       "no_check_source_unread": sum(1 for r in cited if r["verification_status"] == "UNVERIFIED_SOURCE_NOT_READ")},
        "fresh_random_sample": {"n": len(fresh), **verdict_tally(fresh)},
        "new_uae_rows": {"n": len(new), **verdict_tally(new)},
        "targeted_other": {"n": len(targeted), **verdict_tally(targeted)},
        "all_checked_this_round": verdict_tally([r for r in rows if r["verdict_adjusted"]]),
        "all_checked_excluding_new_rows": verdict_tally([r for r in rows if r["verdict_adjusted"] and r["sample_type"] != "new_row_phase2"]),
        "phase1_provisional_rows": {"n": len(prov), **verdict_tally(prov),
                                    "ids_by_final_status": {k: sorted(r["row_id"] for r in prov if r["verification_status"] == k)
                                                           for k in sorted({r["verification_status"] for r in prov})}},
        "phase1_sample_reported": {"n": 40, "PASS": 18, "MINOR": 13, "ERROR": 1, "UNVERIFIABLE": 8,
                                   "error_rate_pct": round(100 * 1 / 32, 1), "error_ci95_pct": wilson(1, 32),
                                   "caveat": "Phase 1 verdicts that relied on a browser style user agent are provisional."},
    }
    S["verification"]["raw_verdict_counts_all"] = dict(C(r["verdict_raw"] for r in rows if r["verdict_raw"]))
    S["verification"]["date_only_minor_reclassified"] = sum(1 for r in rows if r["verdict_raw"] == "MINOR" and r["verdict_adjusted"] == "PASS")
    S["unverified_by_family"] = dict(C(r["family"] for r in rows if r["verification_status"].startswith("UNVERIFI")))
    S["block_types"] = dict(C(r["block_type"] for r in rows if r["block_type"]))
    S["language_read"] = dict(C(r["language_read"] for r in rows if r["language_read"]))
    S["evidence_grade"] = dict(C(r["evidence_grade"] for r in rows))
    return S

def main():
    S = compute()
    (D / "stats.json").write_text(json.dumps(S, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: S[k] for k in ["total_rows", "test_rows_all", "test_rows_headline", "binding_headline", "verification_status"]}, indent=1))
    print(json.dumps(S["verification"], indent=1)[:3500])

if __name__ == "__main__":
    main()
