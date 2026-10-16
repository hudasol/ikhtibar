"""Turn reviewed phase 3 patch proposals (p3patch_*.csv) into data/verification/phase3/patches_p3_agents.json.

Each proposal was read by the lead analyst before acceptance. Proposals listed in REJECT are not applied
and the reason is recorded in the output file. Run: python scripts/p3_accept_patches.py
"""
import csv, glob, json, os

P3 = os.path.join(os.path.dirname(__file__), "..", "data", "verification", "phase3")
ALLOWED = {"framework", "clause_or_page", "requirement_paraphrase", "binding_status", "what_is_tested", "who_tests",
           "source_url", "interpretation_note", "conflict_flag", "language_read", "row_type", "primary_test_type",
           "test_stage"}
REJECT = {}  # (row_id, field) -> reason


def main():
    out, rejected = [], []
    for f in sorted(glob.glob(os.path.join(P3, "p3patch_*.csv"))):
        src = os.path.basename(f)[:-4]
        with open(f, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                key = (r["row_id"], r["field"])
                if r["field"] not in ALLOWED:
                    rejected.append({**r, "source": src, "why": "field not allowed"}); continue
                if key in REJECT:
                    rejected.append({**r, "source": src, "why": REJECT[key]}); continue
                out.append({"row_id": r["row_id"], "field": r["field"], "op": "set", "value": r["new_value"],
                            "source": src, "reason": r["reason"]})
    with open(os.path.join(P3, "patches_p3_agents.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    with open(os.path.join(P3, "rejected_p3_patches.json"), "w", encoding="utf-8") as fh:
        json.dump(rejected, fh, indent=1, ensure_ascii=False)
    print("accepted", len(out), "rejected", len(rejected))


if __name__ == "__main__":
    main()
