"""Tests for the phase 4 evidence: baselines, tool evaluation, coding agreement, robustness, completeness, verification.

Each result file under data/ must agree with what the code recomputes from the committed inputs, so a changed table
cannot leave stale numbers behind. Cheap parts only: the cross validated models are not rerun here.
"""
import json, unittest
from tests.helpers import ROOT, rows


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


class BaselineTests(unittest.TestCase):
    def setUp(self):
        try:
            from ikhtibar import baselines
        except ImportError:
            self.skipTest("scikit-learn is not installed (requirements-baselines.txt)")
        self.b = baselines
        self.res = load("data/baselines/results.json")

    def test_results_match_current_table(self):
        self.assertEqual(self.res["meta"]["input_sha256"], self.b.input_hash(self.b.load_rows()),
                         "the table changed after data/baselines/results.json was written; rerun python -m ikhtibar.baselines")

    def test_majority_baseline_equals_largest_class_share(self):
        rs = self.b.load_rows()
        n = len(rs)
        top = max(sum(r["binding_status"] == s for r in rs) for s in self.b.BINDING)
        self.assertAlmostEqual(self.res["binding5"]["cv"]["majority"]["accuracy"], 100 * top / n, delta=1.5)
        self.assertEqual(self.res["meta"]["n_rows"], n)

    def test_a_learned_text_model_does_not_beat_the_document_prior_on_binding(self):
        cv = self.res["binding5"]["cv"]
        self.assertGreater(cv["framework"]["accuracy"], cv["tfidf_lr"]["accuracy"])
        self.assertGreater(cv["framework"]["accuracy"], cv["majority"]["accuracy"])

    def test_pinned_versions_recorded(self):
        self.assertTrue(self.res["meta"]["sklearn"])
        self.assertEqual(self.res["meta"]["seed"], 20261028)


class ToolEvaluationTests(unittest.TestCase):
    def test_engine_matches_preregistered_scenarios_except_the_documented_divergence(self):
        from ikhtibar import evaluate_tool
        res, misses = evaluate_tool.evaluate_prereg()
        self.assertEqual(res["scenarios_specified"], 82)
        self.assertEqual({m["scenario"] for m in misses}, {"S43"}, "a new scenario disagrees with the preregistered expectation")
        self.assertEqual(res["engine"]["wrongly_excluded"], 0)
        self.assertEqual(res["engine"]["wrongly_applied"], 0)

    def test_engine_never_crashes_on_the_invalid_inputs(self):
        from ikhtibar import evaluate_tool
        res, _ = evaluate_tool.evaluate_prereg()
        self.assertEqual([x["scenario"] for x in res["invalid_inputs"] if x["engine"] == "crashed"], [])

    def test_naive_baselines_are_worse_than_the_engine(self):
        res = load("data/evaluation/results.json")
        e = res["engine"]["accuracy"]
        for name in ("closed_two_valued", "open_two_valued", "always_applies"):
            self.assertLess(res["baselines"][name]["accuracy"], e, name)
        self.assertGreater(res["baselines"]["closed_two_valued"]["wrongly_excluded"], 0)

    def test_stored_results_are_current(self):
        from ikhtibar import evaluate_tool
        res, _ = evaluate_tool.evaluate_prereg()
        stored = load("data/evaluation/results.json")
        self.assertEqual(res["engine"], stored["engine"])

    def test_no_sign_flips_when_an_answer_is_added(self):
        self.assertEqual(load("data/evaluation/simulation.json")["applies_to_not_apply_flips"], 0)


class CodingAgreementTests(unittest.TestCase):
    def test_kappa_and_alpha_against_hand_computed_cases(self):
        from ikhtibar import coding_agreement as ca
        po, k = ca.cohen(["a", "a", "b", "b"], ["a", "a", "b", "b"])
        self.assertEqual((po, k), (1.0, 1.0))
        po, k = ca.cohen(["a", "a", "b", "b"], ["a", "b", "a", "b"])
        self.assertAlmostEqual(k, 0.0)
        self.assertEqual(ca.kripp_alpha_nominal([["a", "b", "a"], ["a", "b", "a"], ["a", "b", "a"]]), 1.0)
        self.assertLess(ca.kripp_alpha_nominal([["a", "a", "b", "b"], ["a", "b", "a", "b"]]), 0.2)

    def test_agreement_file_is_for_the_sampled_rows_and_consistent(self):
        ag = load("data/coding/phase4/agreement.json")
        self.assertEqual(ag["n"], 120)
        for f in ("binding5", "binding3", "test_type"):
            pairs = ag["fields"][f]["pairs"]
            self.assertEqual(len(pairs), 3)
            for p in pairs.values():
                lo, hi = p["kappa_ci95"]
                self.assertLessEqual(lo, p["kappa"] + 0.02)
                self.assertGreaterEqual(hi, p["kappa"] - 0.02)

    def test_original_codes_in_agreement_file_match_current_table(self):
        import csv
        by = {r["row_id"]: r for r in rows()}
        ids = [r["row_id"] for r in csv.DictReader(open(ROOT / "data/coding/phase4/coding_input.csv", encoding="utf-8"))]
        orig = {i: by[i]["binding_status"] for i in ids}
        from ikhtibar import coding_agreement as ca
        c2 = {r["row_id"]: r["binding_status"].strip() for r in ca.read(ROOT / "data/coding/phase4/coder2.csv")}
        agree = sum(orig[i] == c2[i] for i in ids)
        stored = load("data/coding/phase4/agreement.json")["fields"]["binding5"]["pairs"]["original|coder2"]["agreement_pct"]
        self.assertEqual(round(100 * agree / len(ids), 1), stored)

    def test_coder_input_does_not_leak_the_original_codes(self):
        header = (ROOT / "data/coding/phase4/coding_input.csv").read_text(encoding="utf-8").splitlines()[0].split(",")
        for leak in ("binding_status", "primary_test_type", "verification_status"):
            self.assertNotIn(leak, header)


class RobustnessTests(unittest.TestCase):
    def test_stored_robustness_is_current(self):
        from ikhtibar import robustness
        self.assertEqual(robustness.compute(), load("data/robustness.json"))

    def test_claim_survives_every_scenario(self):
        c = load("data/robustness.json")["claim_binding_is_minority"]
        self.assertTrue(c["survives_every_scenario"], c)

    def test_extreme_bounds_are_ordered(self):
        r = load("data/robustness.json")
        self.assertLessEqual(r["extreme_bounds"]["least_favourable_to_binding_pct"], r["base"]["binding_pct"])
        self.assertGreaterEqual(r["extreme_bounds"]["most_favourable_to_binding_pct"], r["base"]["binding_pct"])


class CompletenessTests(unittest.TestCase):
    def test_stored_recall_is_current(self):
        from ikhtibar import completeness
        self.assertEqual(completeness.compute(), load("data/completeness/recall.json"))

    def test_wilson_interval_known_value(self):
        from ikhtibar.completeness import wilson
        lo, hi = wilson(13, 19)
        self.assertAlmostEqual(lo, 46.0, delta=0.2)
        self.assertAlmostEqual(hi, 84.6, delta=0.2)

    def test_lower_bound_not_above_confirmed_recall_claim_for_a_pilot(self):
        r = load("data/completeness/recall.json")
        self.assertLessEqual(r["recall_lower_bound_pct"], r["recall_if_no_unresolved_miss_pct"])


class VerificationTests(unittest.TestCase):
    def test_stats_are_consistent(self):
        s = load("data/verification/phase4/stats_p4.json")
        self.assertEqual(s["sampled"], 120)
        self.assertEqual(s["readable"] + s["unreadable"], s["sampled"])
        self.assertLessEqual(s["errors_as_graded"], s["errors_strict"])
        self.assertLessEqual(s["errors_strict"], s["any_fault_strict"])

    def test_stored_stats_are_current(self):
        from ikhtibar import verify4
        stored = load("data/verification/phase4/stats_p4.json")
        res = verify4.compute() if hasattr(verify4, "compute") else None
        if res is None:
            self.skipTest("verify4 has no compute()")
        for k in ("sampled", "readable", "errors_strict", "any_fault_strict", "errors_as_graded"):
            self.assertEqual(res[k], stored[k], k)

    def test_sample_is_reproducible_and_inside_the_population(self):
        sample = load("data/verification/phase4/sample_p4.json")["sample"]
        ids = {r["row_id"] for r in rows()}
        self.assertEqual(len(sample), len(set(sample)))
        self.assertTrue(set(sample) <= ids)

    def test_strict_error_rows_carry_the_flag_in_the_table(self):
        from ikhtibar.verify4 import row_verdicts
        v = row_verdicts()
        by = {r["row_id"]: r for r in rows()}
        for rid, verdict in v.items():
            self.assertEqual(by[rid]["p4_verdict"], verdict, rid)
            self.assertTrue(by[rid]["p4_sample"].startswith("fresh_random"), rid)

    def test_accepted_patches_are_applied(self):
        patches = load("data/verification/phase4/patches_p4.json")
        by = {r["row_id"]: r for r in rows()}
        last = {}
        for p in patches:
            if p.get("op") == "set":
                last[(p["row_id"], p["field"])] = p["value"]
        self.assertGreater(len(last), 0)
        for (rid, field), value in last.items():
            self.assertEqual(by[rid][field], value, (rid, field))


class PaperTests(unittest.TestCase):
    def test_paper_source_is_current(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("build_paper", ROOT / "scripts" / "build_paper.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        tex, bib, n = mod.render()
        self.assertEqual(tex, (ROOT / "paper" / "main.tex").read_text(encoding="utf-8"),
                         "paper/main.tex is older than the results; run python scripts/build_paper.py")
        self.assertEqual(bib, (ROOT / "paper" / "refs.bib").read_text(encoding="utf-8"))
        self.assertGreater(n, 20)

    def test_every_cited_work_was_read(self):
        import csv, re
        listed = {r["key"]: r for r in csv.DictReader(open(ROOT / "data/paper/refs_candidates.csv", encoding="utf-8"))}
        text = (ROOT / "paper" / "main.tex").read_text(encoding="utf-8")
        for m in re.finditer(r"\\cite[a-z]*\{([^}]+)\}", text):
            for k in m.group(1).split(","):
                self.assertIn(k.strip(), listed)
                self.assertIn(listed[k.strip()]["read_level"], {"abstract_page", "landing_page_only", "full_text"})

    def test_house_style(self):
        for rel in ("paper/main.tmpl.tex", "docs_src/EVALUATION.tmpl.md", "docs/DECISIONS.md", "docs/EVALUATION.md"):
            t = (ROOT / rel).read_text(encoding="utf-8")
            self.assertNotIn("\u2014", t, rel + " has an em dash")
            self.assertNotIn("claude", t.lower(), rel + " mentions the assistant")


if __name__ == "__main__":
    unittest.main()
