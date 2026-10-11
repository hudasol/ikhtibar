import datetime as dt, unittest
from ikhtibar import staleness


def row(i, retrieved, due, last=""):
    return {"row_id": i, "family": "X", "retrieved_on": retrieved, "last_checked_on": last, "next_review_by": due, "verification_status": "VERIFIED"}


class StalenessTests(unittest.TestCase):
    def test_age_threshold(self):
        rs = [row("A", "2026-01-01", "2027-01-01"), row("B", "2026-09-01", "2027-09-01")]
        out = staleness.find_stale(rs, dt.date(2026, 10, 12), max_age_days=180)
        self.assertEqual([x["row_id"] for x in out], ["A"])

    def test_past_review_date(self):
        rs = [row("A", "2026-01-01", "2026-06-01"), row("B", "2026-01-01", "2026-12-01")]
        out = staleness.find_stale(rs, dt.date(2026, 10, 12))
        self.assertEqual([x["row_id"] for x in out], ["A"])
        self.assertIn("next_review_by", out[0]["reason"])

    def test_last_checked_overrides_retrieved(self):
        rs = [row("A", "2025-01-01", "2027-01-01", last="2026-10-01")]
        self.assertEqual(staleness.find_stale(rs, dt.date(2026, 10, 12), max_age_days=30), [])

    def test_family_filter(self):
        r1, r2 = row("A", "2026-01-01", "2026-02-01"), row("B", "2026-01-01", "2026-02-01")
        r2["family"] = "Saudi"
        out = staleness.find_stale([r1, r2], dt.date(2026, 10, 12), family="Saudi")
        self.assertEqual([x["row_id"] for x in out], ["B"])

    def test_script_makes_no_network_calls(self):
        import inspect
        src = inspect.getsource(staleness)
        for bad in ("urllib", "requests", "http.client", "socket"):
            self.assertNotIn("import " + bad, src)


if __name__ == "__main__":
    unittest.main()
