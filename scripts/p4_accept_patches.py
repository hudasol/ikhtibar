"""Turn reviewed phase 4 patch proposals into data/verification/phase4/patches_p4.json.

Sources: v4patch_*.csv (first round verifiers), v4retrypatch_*.csv and v4retry2patch_*.csv (retry rounds) and uae_moved_patch.csv (UAE sources
re-read at their current address). Each proposal was read by the lead analyst. REJECT lists proposals not applied;
OVERRIDE lists proposals applied with a different value (the reason is recorded). Run: python scripts/p4_accept_patches.py
"""
import csv, glob, json, os

P4 = os.path.join(os.path.dirname(__file__), "..", "data", "verification", "phase4")
ALLOWED = {"framework", "clause_or_page", "requirement_paraphrase", "binding_status", "what_is_tested", "who_tests",
           "source_url", "interpretation_note", "conflict_flag", "language_read"}
REJECT = {}
OVERRIDE = {
    ("Korea-002", "binding_status"): (
        "conditional",
        "Verifier proposed mandatory (Art. 12(2): the institute shall carry out the listed projects). Art. 12(1) makes operating "
        "the institute discretionary (the Minister may operate it), so the duty applies only if the trigger occurs, which the "
        "protocol codes conditional. Lead analyst judgement."),
}


def main():
    out, rejected = [], []
    files = (sorted(glob.glob(os.path.join(P4, "v4patch_*.csv"))) + sorted(glob.glob(os.path.join(P4, "v4retrypatch_*.csv")))
             + sorted(glob.glob(os.path.join(P4, "v4retry2patch_*.csv")))
             + [os.path.join(P4, "uae_moved_patch.csv")])
    for f in files:
        src = os.path.basename(f)[:-4]
        with open(f, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                key = (r["row_id"], r["field"])
                if r["field"] not in ALLOWED:
                    rejected.append({**r, "source": src, "why": "field not allowed"}); continue
                if key in REJECT:
                    rejected.append({**r, "source": src, "why": REJECT[key]}); continue
                value, reason = r["new_value"], r["reason"]
                if key in OVERRIDE:
                    value, reason = OVERRIDE[key]
                out.append({"row_id": r["row_id"], "field": r["field"], "op": "set", "value": value,
                            "source": src, "reason": reason})
    with open(os.path.join(P4, "patches_p4.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    with open(os.path.join(P4, "rejected_p4_patches.json"), "w", encoding="utf-8") as fh:
        json.dump(rejected, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print("accepted", len(out), "rejected", len(rejected))


if __name__ == "__main__":
    main()
