"""Statistics for the phase 4 fresh independent verification sample.

Sample: 120 rows drawn at random (seed 20261028) from rows with a completed check and a readable source (see
scripts/p4_draw_samples.py). Verifiers saw only the row and the rules. First round: data/verification/phase4/v4res_*.csv.
Retry round for rows the first round could not read: v4retryres_*.csv. A retry result replaces a first round
result only when the retry could read the source.
Lead re-grading against the rubric (strict): data/verification/phase4/verdict_reclass.csv.
Output: data/verification/phase4/stats_p4.json. Run: python -m ikhtibar.verify4
"""
import csv, glob, json, collections
from pathlib import Path
from .completeness import wilson

ROOT = Path(__file__).resolve().parents[2]
P4 = ROOT / "data" / "verification" / "phase4"
READ = ("PASS", "MINOR", "ERROR")


def rd(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def load_results():
    first = {}
    for f in sorted(glob.glob(str(P4 / "v4res_*.csv"))):
        for r in rd(f):
            first[r["row_id"]] = r
    final = dict(first)
    retry_used = set()
    for f in sorted(glob.glob(str(P4 / "v4retryres_*.csv"))) + sorted(glob.glob(str(P4 / "v4retry2res_*.csv"))):
        for r in rd(f):
            if r["verdict"] in READ and final[r["row_id"]]["verdict"] not in READ:
                final[r["row_id"]] = r
                retry_used.add(r["row_id"])
    return first, final, retry_used


def row_verdicts():
    """Strict verdict per sampled row (does not read the evidence table, so the table builder can use it)."""
    sample = json.loads((P4 / "sample_p4.json").read_text(encoding="utf-8"))
    _, final, _ = load_results()
    reclass = {r["row_id"]: r for r in rd(P4 / "verdict_reclass.csv")}
    out = {}
    for i in sample["sample"]:
        v = final[i]["verdict"]
        if i in reclass and reclass[i]["agent_verdict"] == v:
            v = reclass[i]["lead_verdict"]
        out[i] = v
    return out


def classify_block(r):
    t = " ".join([r.get("failed_checks", ""), r.get("what_source_says", "")]).lower()
    if "allowlist" in t:
        return "session_allowlist"
    if "request rejected" in t or "403" in t or "rejected" in t:
        return "site_rejected"
    if r["verdict"] == "UNVERIFIABLE_OTHER":
        return "unreadable_passage_or_binary"
    return "other"


def compute():
    sample = json.loads((P4 / "sample_p4.json").read_text(encoding="utf-8"))
    ids = sample["sample"]
    table = {r["row_id"]: r for r in rd(ROOT / "data" / "evidence_table.csv")}
    first, final, retry_used = load_results()
    assert set(ids) == set(final), "results do not cover the sample"
    reclass = {r["row_id"]: r for r in rd(P4 / "verdict_reclass.csv")}
    strict = {}
    for i in ids:
        v = final[i]["verdict"]
        if i in reclass and reclass[i]["agent_verdict"] == v:
            v = reclass[i]["lead_verdict"]
        strict[i] = v
    graded = collections.Counter(final[i]["verdict"] for i in ids)
    st = collections.Counter(strict.values())
    readable = [i for i in ids if final[i]["verdict"] in READ]
    n_read = len(readable)
    err_g = sum(final[i]["verdict"] == "ERROR" for i in readable)
    err_s = sum(strict[i] == "ERROR" for i in readable)
    minor_s = sum(strict[i] == "MINOR" for i in readable)
    blocked = [i for i in ids if final[i]["verdict"] not in READ]
    by_reason = collections.Counter(classify_block(final[i]) for i in blocked)
    fam = collections.defaultdict(lambda: {"sampled": 0, "readable": 0, "errors_strict": 0})
    for i in ids:
        f = table[i]["family"]
        fam[f]["sampled"] += 1
        if i in readable:
            fam[f]["readable"] += 1
            fam[f]["errors_strict"] += strict[i] == "ERROR"
    out = {
        "seed": sample["seed"], "population_size": sample["population_size"], "sampled": len(ids),
        "retry_resolved": len(retry_used),
        "verdicts_as_graded": dict(graded), "verdicts_strict": dict(st),
        "readable": n_read, "readable_pct_of_sample": round(100 * n_read / len(ids), 1),
        "errors_as_graded": err_g, "error_rate_as_graded_pct": round(100 * err_g / n_read, 1),
        "error_rate_as_graded_ci95": wilson(err_g, n_read),
        "errors_strict": err_s, "error_rate_strict_pct": round(100 * err_s / n_read, 1),
        "error_rate_strict_ci95": wilson(err_s, n_read),
        "any_fault_strict": err_s + minor_s, "any_fault_strict_pct": round(100 * (err_s + minor_s) / n_read, 1),
        "any_fault_strict_ci95": wilson(err_s + minor_s, n_read),
        "unreadable": len(blocked), "unreadable_by_reason": dict(by_reason),
        "unreadable_by_family": dict(collections.Counter(table[i]["family"] for i in blocked)),
        "by_family": {k: v for k, v in sorted(fam.items())},
        "error_rows_strict": sorted(i for i in readable if strict[i] == "ERROR"),
        "error_types_among_faults": dict(collections.Counter(
            final[i]["error_type"] for i in readable if strict[i] in ("MINOR", "ERROR"))),
    }
    # if every unreadable row had the same fault rate as the readable ones is the neutral assumption;
    # bounds: none of them faulty, or all of them faulty
    out["bounds_all_sampled_strict_error_pct"] = {
        "none_of_unreadable_in_error": round(100 * err_s / len(ids), 1),
        "all_of_unreadable_in_error": round(100 * (err_s + len(blocked)) / len(ids), 1)}
    # pooled with the phase 3 fresh sample (3 of 23 under the strict rubric)
    k, n = err_s + 3, n_read + 23
    out["pooled_with_phase3_fresh_sample"] = {"errors": k, "readable": n, "pct": round(100 * k / n, 1), "ci95": wilson(k, n)}
    out["row_verdicts"] = {i: {"as_graded": final[i]["verdict"], "strict": strict[i]} for i in ids}
    return out


def main():
    out = compute()
    (P4 / "stats_p4.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print({k: v for k, v in out.items() if k not in ("row_verdicts", "by_family", "unreadable_by_family")})


if __name__ == "__main__":
    main()
