import csv, json, re, unittest
from collections import Counter
from tests.helpers import ROOT, rows, stats
from ikhtibar import stats as stats_mod, build_docs

SPLIT = {"mandatory": "M", "conditional": "M", "voluntary": "V", "guidance": "V", "ambiguous": "A"}


class StatsTests(unittest.TestCase):
    def test_counts_recomputed_from_table_match_stats_json(self):
        rs = rows()
        t = [r for r in rs if r["row_type"] == "test"]
        h = [r for r in t if r["headline_include"] == "yes"]
        s = stats()
        self.assertEqual(s["total_rows"], len(rs))
        self.assertEqual(s["test_rows_all"], len(t))
        self.assertEqual(s["test_rows_headline"], len(h))
        c = Counter(r["binding_status"] for r in h)
        for k in ("mandatory", "conditional", "voluntary", "guidance", "ambiguous"):
            self.assertEqual(s["binding_headline"].get(k, 0), c[k], k)
        self.assertEqual(sum(s["binding_headline"].values()), len(h))

    def test_stats_json_is_current(self):
        fresh = stats_mod.compute()
        self.assertEqual(json.loads(json.dumps(fresh, sort_keys=True)), json.loads(json.dumps(stats(), sort_keys=True)),
                         "data/stats.json is stale: run python -m ikhtibar.build_all")

    def test_wilson_interval(self):
        lo, hi = stats_mod.wilson(1, 32)
        self.assertAlmostEqual(lo, 0.6, places=1)   # percent, as reported in phase 1
        self.assertAlmostEqual(hi, 15.7, places=1)

    def test_verification_tallies_exclude_unverified_from_denominator(self):
        v = stats()["verification"]["all_checked_this_round"]
        self.assertEqual(v["verifiable"], v["PASS"] + v["MINOR"] + v["ERROR"])
        self.assertEqual(v["n_checked_rows"], v["verifiable"] + v["UNVERIFIED_BLOCKED"] + v["UNVERIFIABLE_OTHER"])

    def test_no_canada_or_unverified_row_in_headline(self):
        for r in rows():
            if r["headline_include"] == "yes":
                self.assertNotIn(r["verification_status"], {"UNVERIFIED_BLOCKED", "UNVERIFIABLE_OTHER"})


class DocsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = build_docs.render_all(write_support=False)

    def test_generated_files_are_up_to_date(self):
        for rel, text in self.out.items():
            self.assertEqual((ROOT / rel).read_text(encoding="utf-8"), text, f"{rel} is stale: run python -m ikhtibar.build_all")

    def test_every_cited_row_exists_and_is_checked(self):
        by = {r["row_id"]: r for r in rows()}
        ids = set()
        for rel in ("docs/REPORT.md", "docs/EXECUTIVE_BRIEF.md", "README.md"):
            ids |= set(re.findall(r"`([A-Za-z][A-Za-z0-9-]*-\d{3})`", self.out[rel]))
        self.assertTrue(ids)
        for i in ids:
            self.assertIn(i, by)
            self.assertNotEqual(by[i]["verification_status"], "NOT_RECHECKED", f"{i} cited but not verified in phase 2")

    def test_excluded_rows_always_carry_dagger(self):
        by = {r["row_id"]: r for r in rows()}
        for rel in ("docs/REPORT.md", "docs/EXECUTIVE_BRIEF.md"):
            for m in re.finditer(r"`([A-Za-z][A-Za-z0-9-]*-\d{3})`(†?)", self.out[rel]):
                excluded = by[m.group(1)]["headline_include"] != "yes"
                self.assertEqual(bool(m.group(2)), excluded, f"{rel}: {m.group(1)}")

    def test_headline_numbers_in_report_match_stats(self):
        s = stats()
        b = s["binding_headline"]
        n = s["test_rows_headline"]
        mc = b["mandatory"] + b["conditional"]
        self.assertIn(f"Of {n} headline test provisions, {mc} (", self.out["docs/REPORT.md"])

    def test_report_has_no_unfilled_placeholders(self):
        for rel, text in self.out.items():
            self.assertNotRegex(text, r"\{\{[^}]+\}\}", rel)

    def test_time_sensitive_dates_in_report_are_in_data(self):
        ts = (ROOT / "data" / "time_sensitive.csv").read_text(encoding="utf-8")
        for needle in ("27 July 2026", "24 July 2026", "8 July 2026", "2 December 2027", "2 August 2028", "2 August 2027",
                       "DoH/ST/DDGO/RAI/V1/2025", "1 September 2023", "14 July 2026"):
            self.assertIn(needle, ts, needle)
            self.assertIn(needle, self.out["docs/REPORT.md"] + self.out["docs/TIME_SENSITIVE.md"], needle)

    def test_report_claims_on_red_and_oversight_follow_data(self):
        by = rows()
        red = [r for r in by if r["row_type"] == "test" and r["headline_include"] == "yes" and r["primary_test_type"] == "RED"]
        binding = [r for r in red if r["binding_status"] in ("mandatory", "conditional")]
        # every binding headline red teaming row is named in the headline finding
        for r in binding:
            self.assertIn(r["row_id"], self.out["docs/REPORT.md"].split("## 2. Method")[0])
        self.assertTrue(all(r["family"].startswith("EU") for r in binding), [r["row_id"] for r in binding])


if __name__ == "__main__":
    unittest.main()
