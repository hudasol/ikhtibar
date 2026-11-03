"""Tests for the UAE Arabic check (data/uae_arabic)."""
import csv, json, unittest
from tests.helpers import ROOT

D = ROOT / "data" / "uae_arabic"


class UaeArabicTests(unittest.TestCase):
    def test_every_input_row_has_a_reader_row(self):
        inp = set()
        for g in ("doh_other", "difc_adgm", "dubai", "federal"):
            inp |= {r["row_id"] for r in csv.DictReader(open(D / "inputs" / f"{g}.csv", encoding="utf-8"))}
        raw = set()
        for g in ("doh_other", "difc_adgm", "dubai", "federal"):
            raw |= {r["row_id"] for r in csv.DictReader(open(D / "raw" / f"{g}.csv", encoding="utf-8"))}
        self.assertEqual(inp, raw)

    def test_unread_rows_are_not_counted_as_absent(self):
        st = json.loads((D / "stats.json").read_text(encoding="utf-8"))
        self.assertEqual(st["meta"]["arabic_not_found"] + st["meta"]["arabic_found"] + st["meta"]["not_checked"], st["meta"]["rows_returned"])
        if st["meta"]["read_with_status"] == 0:
            self.assertIsNone(st["binding_status_differs"]["pct"])

    def test_only_test_rows_in_inputs(self):
        table = {r["row_id"]: r for r in csv.DictReader(open(ROOT / "data" / "evidence_table.csv", encoding="utf-8"))}
        for g in ("doh_other", "difc_adgm", "dubai", "federal"):
            for r in csv.DictReader(open(D / "inputs" / f"{g}.csv", encoding="utf-8")):
                self.assertEqual(table[r["row_id"]]["row_type"], "test")


if __name__ == "__main__":
    unittest.main()
