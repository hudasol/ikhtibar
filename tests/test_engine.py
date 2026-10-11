import json, unittest
from tests.helpers import ROOT
from ikhtibar import engine
from ikhtibar.engine import TRUE, FALSE, UNKNOWN, evaluate, run, validate_answers, AnswerError, load_schema


def states(res):
    return {i["id"]: i["state"] for i in res["items"]}


class KleeneTests(unittest.TestCase):
    def test_missing_answer_is_unknown_not_false(self):
        self.assertEqual(evaluate({"eq": ["audience", "public_facing"]}, {}), UNKNOWN)

    def test_eq_true_and_false(self):
        self.assertEqual(evaluate({"eq": ["audience", "internal"]}, {"audience": "internal"}), TRUE)
        self.assertEqual(evaluate({"eq": ["audience", "internal"]}, {"audience": "public_facing"}), FALSE)

    def test_not_and_all_any(self):
        a = {"audience": "internal"}
        self.assertEqual(evaluate({"not": {"eq": ["audience", "internal"]}}, a), FALSE)
        self.assertEqual(evaluate({"all": [{"eq": ["audience", "internal"]}, {"eq": ["system_type", "agentic"]}]}, a), UNKNOWN)
        self.assertEqual(evaluate({"all": [{"eq": ["audience", "public_facing"]}, {"eq": ["system_type", "agentic"]}]}, a), FALSE)
        self.assertEqual(evaluate({"any": [{"eq": ["audience", "internal"]}, {"eq": ["system_type", "agentic"]}]}, a), TRUE)
        self.assertEqual(evaluate({"any": [{"eq": ["audience", "public_facing"]}, {"eq": ["system_type", "agentic"]}]}, a), UNKNOWN)


class RunTests(unittest.TestCase):
    def test_empty_answers_never_exclude_and_never_settle_conditional_items(self):
        res = run({})
        st = states(res)
        self.assertNotIn("DOES_NOT_APPLY", st.values())
        cl = engine.load_checklist()
        for it in cl["items"]:
            if it["applies_when"] != {"always": True}:
                self.assertEqual(st[it["id"]], "UNKNOWN", it["id"])
        self.assertTrue(all(i["to_settle"] for i in res["items"] if i["state"] == "UNKNOWN"))

    def test_unknown_string_equals_missing(self):
        self.assertEqual(states(run({"audience": "unknown"})), states(run({})))

    def test_rules_based_system_drops_learned_model_items(self):
        st = states(run({"system_type": "rules_based"}))
        self.assertEqual(st["C1"], "DOES_NOT_APPLY")
        self.assertEqual(st["D3"], "DOES_NOT_APPLY")

    def test_genai_triggers_red_teaming_item(self):
        self.assertEqual(states(run({"system_type": "genai_llm"}))["D7"], "APPLIES")
        self.assertEqual(states(run({"system_type": "predictive_ml"}))["D7"], "DOES_NOT_APPLY")

    def test_entity_zone_settles_jurisdiction_items(self):
        st = states(run({"entity_zone": "health_dubai"}))
        self.assertEqual(st["H2"], "APPLIES")
        self.assertEqual(st["H1"], "DOES_NOT_APPLY")

    def test_hosting_settles_nothing(self):
        base = states(run({}))
        for v in load_schema()["questions"]["hosting"]["values"]:
            self.assertEqual(states(run({"hosting": v})), base, v)
        self.assertTrue(run({"hosting": next(iter(load_schema()["questions"]["hosting"]["values"]))})["notes"])

    def test_binding_is_not_yes_without_entity_zone(self):
        res = run({"system_type": "predictive_ml"})
        for it in res["items"]:
            for s in it["sources"]:
                self.assertNotEqual(s["binds_you"], "YES", s["row_id"])

    def test_guidance_rows_never_bind(self):
        res = run({"entity_zone": "dubai_gov"})
        for it in res["items"]:
            for s in it["sources"]:
                if s["source_binding_status"] in ("guidance", "voluntary"):
                    self.assertEqual(s["binds_you"], "NO", s["row_id"])

    def test_every_source_has_trace_fields(self):
        for it in run({})["items"]:
            for s in it["sources"]:
                for k in ("row_id", "framework", "clause", "source_url", "verification_status", "binds_you"):
                    self.assertTrue(s[k] != "" , (it["id"], s["row_id"], k))

    def test_invalid_answers_raise(self):
        with self.assertRaises(AnswerError):
            validate_answers({"audience": "everyone"}, load_schema())
        with self.assertRaises(AnswerError):
            validate_answers({"nonsense": "x"}, load_schema())

    def test_multi_value_question(self):
        out = validate_answers({"data_types": "personal,health"}, load_schema())
        self.assertEqual(out["data_types"], ["health", "personal"])

    def test_madoun_golden_summary(self):
        ans = json.loads((ROOT / "examples" / "madoun_answers.json").read_text(encoding="utf-8"))
        res = run(ans)
        st = states(res)
        self.assertEqual(st["D7"], "DOES_NOT_APPLY")
        self.assertEqual(st["D8"], "DOES_NOT_APPLY")
        for h in ("H1", "H2", "H3", "H4", "H5", "H6", "A3", "D6"):
            self.assertEqual(st[h], "UNKNOWN", h)
        self.assertEqual(sum(res["summary"].values()), len(res["items"]))


if __name__ == "__main__":
    unittest.main()
