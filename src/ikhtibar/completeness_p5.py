"""Completeness, second reference list (task 3b and 3c, phase 5).

The list (data/completeness/reference_list_p5.csv) was built blind to the table by six agents, one per area, under
the same search and fetch tools as the table. Matching to the table (data/completeness/matches_p5.csv) was done by
three further agents that saw only titles, issuers and addresses. Both lists used the same tools, so they are not
independent samples of the literature and no capture recapture estimate is made. Recall here is against what the
list builders found, which is a lower bound on the true gap.
Outputs: data/completeness/recall_p5.json (recall by jurisdiction group, strict = exact and lenient = exact or
partial, Wilson 95% intervals). Run: python -m ikhtibar.completeness_p5
"""
import csv, json, collections
from pathlib import Path
from .completeness import wilson

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "data" / "completeness"

GROUPS = {"EU": "EU", "UK": "UK", "US federal": "US and Canada", "US": "US and Canada", "Canada": "US and Canada"}


def group(j):
    j0 = j.strip()
    for k, v in GROUPS.items():
        if j0.startswith(k):
            return v
    low = j0.lower()
    if any(x in low for x in ("uae", "saudi", "emirates", "abu dhabi", "dubai", "gulf", "qatar", "bahrain", "oman", "kuwait", "difc", "adgm")):
        return "UAE and Gulf"
    if any(x in low for x in ("international", "global", "oecd", "un ", "multilateral", "iso", "g7", "council of europe")):
        return "International"
    if any(x in low for x in ("china", "japan", "korea", "singapore", "hong kong", "taiwan", "malaysia", "vietnam", "thailand", "india", "asia", "australia", "indonesia")):
        return "Asia Pacific"
    return "Other"


def block(items, hit):
    n = len(items)
    k = sum(1 for r in items if hit(r))
    return {"n": n, "hits": k, "pct": round(100 * k / n, 1) if n else None, "wilson_ci95": wilson(k, n)}


def compute():
    ref = [r for r in csv.DictReader(open(D / "reference_list_p5.csv", encoding="utf-8")) if not r["duplicate_of"]]
    mat = {r["ref_id"]: r for r in csv.DictReader(open(D / "matches_p5.csv", encoding="utf-8"))}
    for r in ref:
        r["match"] = mat[r["ref_id"]]["match"]
        r["group"] = group(r["jurisdiction"])
    strict = lambda r: r["match"] == "exact"
    lenient = lambda r: r["match"] in ("exact", "partial")
    yes = [r for r in ref if r["has_testing_provision"] == "yes"]
    unc = [r for r in ref if r["has_testing_provision"] not in ("yes", "no")]
    out = {
        "instruments": len(ref), "has_testing_yes": len(yes), "has_testing_no": sum(1 for r in ref if r["has_testing_provision"] == "no"),
        "unclear": len(unc),
        "access": dict(collections.Counter(r["access_status"] for r in ref)),
        "match_counts_all": dict(collections.Counter(r["match"] for r in ref)),
        "confirmed_positive_strict": block(yes, strict), "confirmed_positive_lenient": block(yes, lenient),
        "all_instruments_strict": block(ref, strict),
        "by_group": {}, "missed_confirmed": [],
        "method_note": ("Second reference list built by six agents blind to the table, under the same search tools as the table; "
                        "matching by agents that saw titles and addresses only, so some matches rest on catalogue knowledge; "
                        "the table at matching time already contained the 19 phase 5 US rows. Not independent of the table builders' "
                        "tools, so no capture recapture estimate."),
    }
    for g in sorted({r["group"] for r in ref}):
        ys = [r for r in yes if r["group"] == g]
        out["by_group"][g] = {"confirmed_positive_strict": block(ys, strict), "confirmed_positive_lenient": block(ys, lenient),
                              "all_strict": block([r for r in ref if r["group"] == g], strict)}
    for r in yes:
        if not strict(r):
            out["missed_confirmed"].append({"ref_id": r["ref_id"], "group": r["group"], "match": r["match"], "title": r["title"],
                                            "access_status": r["access_status"]})
    return out


def main():
    out = compute()
    (D / "recall_p5.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("instruments", "has_testing_yes", "confirmed_positive_strict", "confirmed_positive_lenient")}, indent=1))
    for g, v in out["by_group"].items():
        print(g, v["confirmed_positive_strict"], v["confirmed_positive_lenient"]["pct"])


if __name__ == "__main__":
    main()
