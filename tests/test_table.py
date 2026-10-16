import re, unittest
from tests.helpers import ROOT, rows

BINDING = {"mandatory", "conditional", "voluntary", "guidance", "ambiguous"}
STATUS = {"VERIFIED", "VERIFIED_CORRECTED", "VERIFIED_NOTE_ONLY", "NOT_RECHECKED", "UNVERIFIED_BLOCKED", "UNVERIFIABLE_OTHER",
          "UNVERIFIED_SOURCE_NOT_READ", "ERROR_WITHDRAWN", "NEW_UNCHECKED", "SUPERSEDED"}
UNRELIABLE = {"UNVERIFIED_BLOCKED", "UNVERIFIABLE_OTHER", "UNVERIFIED_SOURCE_NOT_READ", "ERROR_WITHDRAWN", "NEW_UNCHECKED"}
TYPES = set("PERF ROB FAIR SEC RED CSAFE PRIV TRANS OVER RISK DATA CONF REAL MON GATE".split())


class TableTests(unittest.TestCase):
    def setUp(self):
        self.rows = rows()

    def test_unique_ids(self):
        ids = [r["row_id"] for r in self.rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_vocabularies(self):
        for r in self.rows:
            self.assertIn(r["binding_status"], BINDING, r["row_id"])
            self.assertIn(r["verification_status"], STATUS, r["row_id"])
            self.assertIn(r["row_type"], {"test", "enabler", "context"}, r["row_id"])
            if r["row_type"] == "test":
                self.assertIn(r["primary_test_type"], TYPES, r["row_id"])

    def test_unreliable_rows_are_excluded_and_explained(self):
        for r in self.rows:
            if r["verification_status"] in UNRELIABLE:
                self.assertEqual(r["headline_include"], "no", r["row_id"])
            elif r["verification_status"] == "SUPERSEDED":
                # replaced in counts by rows read from a fuller version of the same source
                self.assertEqual(r["headline_include"], "no", r["row_id"])
                self.assertIn("supersed", (r["interpretation_note"] + r["verification_note"]).lower(), r["row_id"])
            elif r["headline_include"] == "no":
                # excluded although checked: rests on a summary or secondary report only
                self.assertTrue(r["evidence_grade"].startswith("unverified") or r["evidence_grade"] == "catalogue-level only", r["row_id"])
        for r in self.rows:
            if r["verification_status"] == "UNVERIFIED_BLOCKED":
                self.assertTrue(r["document_to_download"].strip(), f"{r['row_id']} lacks a document to download")
                self.assertTrue(r["block_type"].strip(), r["row_id"])

    def test_review_dates(self):
        for r in self.rows:
            self.assertRegex(r["retrieved_on"], r"^\d{4}-\d\d-\d\d$", r["row_id"])
            self.assertRegex(r["next_review_by"], r"^\d{4}-\d\d-\d\d$", r["row_id"])
            self.assertGreater(r["next_review_by"], r["retrieved_on"], r["row_id"])

    def test_sources_present(self):
        for r in self.rows:
            self.assertTrue(r["source_url"].startswith("http"), r["row_id"])

    def test_named_earlier_unverifiable_rows_are_resolved_or_marked(self):
        by = {r["row_id"]: r for r in self.rows}
        for i in ["Canada-002", "Canada-009", "Canada-014", "EU-AI-Act-034", "EU-AI-Act-044", "EU-AI-Act-068", "Saudi-008", "Singapore-014", "UK-009"]:
            self.assertNotEqual(by[i]["verification_status"], "NOT_RECHECKED", i)

    def test_withdrawn_row_not_counted(self):
        for r in self.rows:
            if r["verification_status"] == "ERROR_WITHDRAWN":
                self.assertEqual(r["headline_include"], "no")

    def test_no_long_quotes_cells(self):
        for r in self.rows:
            for c in ("requirement_paraphrase", "interpretation_note", "verification_note"):
                self.assertLessEqual(len(r[c].split()), 120, f"{r['row_id']} {c}")

    def test_repo_text_style(self):
        """Repo facing text: no em dash, no university affiliation."""
        banned = ["—", "stirling"]
        for p in list(ROOT.glob("*.md")) + list((ROOT / "docs").glob("*.md")) + list((ROOT / "docs_src").glob("*.md")) \
                + list((ROOT / "examples").glob("*.md")) + list((ROOT / "templates").rglob("*.md")):
            text = p.read_text(encoding="utf-8").lower()
            for b in banned:
                self.assertNotIn(b, text, f"{p.name} contains {b!r}")
        self.assertNotIn("stirling", (ROOT / "data" / "evidence_table.csv").read_text(encoding="utf-8").lower())

    def test_no_email_address_in_repo_text(self):
        pat = re.compile(r"[A-Za-z0-9._%+-]+@gmail\.com")
        for p in list(ROOT.glob("*.md")) + list((ROOT / "docs").glob("*.md")):
            self.assertIsNone(pat.search(p.read_text(encoding="utf-8")), p.name)

    def test_no_purchase_wording(self):
        for p in [ROOT / "docs" / "READING_LIST.md", ROOT / "docs" / "REPORT.md", ROOT / "README.md"]:
            t = p.read_text(encoding="utf-8").lower()
            for w in ("to buy", "paywalled", "purchase a", "purchase the", "subscribe", "paid api"):
                self.assertNotIn(w, t, f"{p.name}: {w}")


if __name__ == "__main__":
    unittest.main()
