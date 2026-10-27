"""Completeness benchmark: recall of the evidence table against an independently built reference list.

The reference list (data/completeness/reference_list.csv) was built by a separate agent that did not see the table.
The match of each reference to the table (data/completeness/matches.csv) was made afterwards by hand and is
reviewable. Only instruments whose primary text the reference builder read and found to contain a testing
provision (has_testing_provision == yes) are confirmed positives. Unclear instruments are unresolved.
Output: data/completeness/recall.json. Run: python -m ikhtibar.completeness
"""
import csv, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "data" / "completeness"


def wilson(k, n, z=1.96):
    if n == 0:
        return [None, None]
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(100 * max(0, c - h), 1), round(100 * min(1, c + h), 1)]


def compute():
    ref = {r["ref_id"]: r for r in csv.DictReader(open(D / "reference_list.csv", encoding="utf-8"))}
    mat = {r["ref_id"]: r for r in csv.DictReader(open(D / "matches.csv", encoding="utf-8"))}
    inframe = {k: v for k, v in ref.items() if mat[k]["match"] != "out_of_frame"}
    got = lambda k: mat[k]["match"] in ("exact", "successor")
    yes = [k for k, v in inframe.items() if v["has_testing_provision"] == "yes"]
    unc = [k for k, v in inframe.items() if v["has_testing_provision"] not in ("yes", "no")]
    yes_hit = [k for k in yes if got(k)]
    unc_hit = [k for k in unc if got(k)]
    unc_miss = [k for k in unc if not got(k)]
    out = {
        "reference_candidates": len(ref), "out_of_frame": len(ref) - len(inframe),
        "confirmed_positive": len(yes), "confirmed_positive_in_table": len(yes_hit),
        "recall_confirmed_pct": round(100 * len(yes_hit) / len(yes), 1), "recall_confirmed_ci95": wilson(len(yes_hit), len(yes)),
        "missed_confirmed": [{"ref_id": k, "jurisdiction": ref[k]["jurisdiction"], "title": ref[k]["title"]} for k in yes if not got(k)],
        "unresolved": len(unc), "unresolved_in_table": len(unc_hit), "unresolved_not_in_table": len(unc_miss),
        "unresolved_not_in_table_by_jurisdiction": {},
        "recall_lower_bound_pct": round(100 * (len(yes_hit) + len(unc_hit)) / (len(yes) + len(unc)), 1),
        "recall_if_no_unresolved_miss_pct": round(100 * (len(yes_hit) + len(unc_hit)) / (len(yes) + len(unc_hit)), 1),
        "access": {a: sum(1 for v in inframe.values() if v["access_status"] == a) for a in ("read", "partly_read", "blocked")},
        "method_note": "Reference list built blind to the table by a separate agent under the same tool limits; matching by hand afterwards. A pilot, not a population estimate."}
    for k in unc_miss:
        j = ref[k]["jurisdiction"]
        out["unresolved_not_in_table_by_jurisdiction"][j] = out["unresolved_not_in_table_by_jurisdiction"].get(j, 0) + 1
    return out


def main():
    out = compute()
    (D / "recall.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
