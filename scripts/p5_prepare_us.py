"""Prepare the phase 5 US rows (task 3a): rename ids P4 -> P5, set the retrieval date, convert the verifier
patch tables to the patch format. Inputs: data/completeness/us_docs_candidate_rows.csv and
data/verification/phase5/raw/us*_res.csv, us*_patch.csv. Outputs: p5new_us.csv, p5res_us.csv, patches_p5_us.json."""
import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
P5 = ROOT / "data" / "verification" / "phase5"
NEW = ["row_id", "family", "framework", "clause_or_page", "requirement_paraphrase", "binding_status", "what_is_tested",
       "who_tests", "source_url", "retrieval_date", "interpretation_note", "conflict_flag", "row_type",
       "primary_test_type", "secondary_test_types", "test_stage", "evidence_grade", "language_read"]


def rd(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def rid(x):
    return x.replace("-P4-", "-P5-")


def main():
    cand = rd(ROOT / "data" / "completeness" / "us_docs_candidate_rows.csv")
    out = []
    for r in cand:
        x = {c: "" for c in NEW}
        x.update({k: r[k] for k in r if k in NEW})
        x["row_id"] = rid(r["row_id"])
        x["retrieval_date"] = "2026-11-03"
        x["evidence_grade"] = "primary text read"
        x["language_read"] = "English"
        out.append(x)
    with open(P5 / "p5new_us.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=NEW, lineterminator="\n"); w.writeheader(); w.writerows(out)
    res = []
    for n in (1, 2):
        for r in rd(P5 / "raw" / f"us{n}_res.csv"):
            r["row_id"] = rid(r["row_id"]); res.append(r)
    cols = list(res[0].keys())
    with open(P5 / "p5res_us.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n"); w.writeheader(); w.writerows(res)
    patches = []
    for n in (1, 2):
        for r in rd(P5 / "raw" / f"us{n}_patch.csv"):
            patches.append({"row_id": rid(r["row_id"]), "field": r["field"], "op": "set", "value": r["new_value"],
                            "source": f"p5_us{n}", "reason": r["reason"]})
    (P5 / "patches_p5_us.json").write_text(json.dumps(patches, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(len(out), "rows;", len(res), "verdicts;", len(patches), "patches")


if __name__ == "__main__":
    main()
