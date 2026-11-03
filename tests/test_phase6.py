import json, unittest
from pathlib import Path
from ikhtibar import split6, confirm6

ROOT = Path(__file__).resolve().parents[1]


class Phase6(unittest.TestCase):
    def test_split_is_reproducible_and_disjoint(self):
        stored = json.loads((ROOT / "data/phase6/split.json").read_text())["assignment"]
        docs = {r["framework"] for r in split6.headline()}
        self.assertEqual(set(stored), docs)
        design = {d for d, h in stored.items() if h == "design"}
        conf = {d for d, h in stored.items() if h.startswith("confirmation")}
        self.assertFalse(design & conf)

    def test_new_documents_only_in_confirmation(self):
        stored = json.loads((ROOT / "data/phase6/split.json").read_text())["assignment"]
        for r in split6.headline():
            if stored[r["framework"]] == "design":
                self.assertNotEqual(r["sample_type"], "new_row_phase5")

    def test_results_rows_match_table(self):
        for s in ("design", "confirmation", "old", "new", "all"):
            res = json.loads((ROOT / f"data/phase6/results_{s}.json").read_text())
            self.assertEqual(res["n_rows"], len(confirm6.pick(s)), s)

    def test_stored_confirmation_result_decisions_present(self):
        res = json.loads((ROOT / "data/phase6/results_confirmation.json").read_text())
        for k in ("C1_documents_are_pure", "C2_concordance_excess", "C3_minority_of_documents_binding",
                  "C4_minority_of_documents_weighted", "C5_process_only_gap_direction"):
            self.assertIn(k, res["decisions"])


if __name__ == "__main__":
    unittest.main()
