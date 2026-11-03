"""Tests for the extraction recall evidence (data/extraction_recall)."""
import json, unittest
from tests.helpers import ROOT

D = ROOT / "data" / "extraction_recall"


class ExtractionRecallTests(unittest.TestCase):
    def setUp(self):
        from ikhtibar import extraction_recall as e
        self.e = e

    def test_wilson_bounds(self):
        lo, hi = self.e.wilson(0, 10)
        self.assertEqual(lo, 0.0)
        lo, hi = self.e.wilson(10, 10)
        self.assertAlmostEqual(hi, 100.0, places=6)

    def test_sample_is_seeded_and_recorded(self):
        s = json.loads((D / "sample.json").read_text(encoding="utf-8"))
        self.assertEqual(s["seed"], self.e.SEED)
        self.assertEqual(len(s["documents"]), self.e.N_DOCS)

    def test_stats_consistent_with_matches(self):
        import csv
        st = json.loads((D / "stats.json").read_text(encoding="utf-8"))
        rows = list(csv.DictReader(open(D / "matches.csv", encoding="utf-8")))
        hits = sum(r["matched"] in ("yes", "partial") for r in rows)
        self.assertEqual(st["recall"]["hits"], hits)
        self.assertEqual(st["recall"]["n"], len(rows))

    def test_missed_candidates_are_not_in_headline_table(self):
        import csv
        miss = list(csv.DictReader(open(D / "missed_candidates.csv", encoding="utf-8")))
        table_ids = {r["row_id"] for r in csv.DictReader(open(ROOT / "data" / "evidence_table.csv", encoding="utf-8"))}
        for r in miss:
            self.assertNotIn(r.get("indep_id"), table_ids)


if __name__ == "__main__":
    unittest.main()
