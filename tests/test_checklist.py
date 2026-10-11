import json, unittest
from tests.helpers import ROOT, by_id
from ikhtibar import engine

try:
    import yaml
except ImportError:  # the mirror is checked only when PyYAML is present
    yaml = None


class ChecklistTests(unittest.TestCase):
    def setUp(self):
        self.cl = engine.load_checklist()
        self.rows = by_id()

    def test_every_row_exists_and_not_withdrawn(self):
        for it in self.cl["items"]:
            self.assertTrue(it["rows"], it["id"])
            for r in it["rows"]:
                self.assertIn(r, self.rows, f"{it['id']} cites {r}")
                self.assertNotEqual(self.rows[r]["verification_status"], "ERROR_WITHDRAWN", r)

    def test_each_item_has_at_least_one_headline_row(self):
        for it in self.cl["items"]:
            self.assertTrue(any(self.rows[r]["headline_include"] == "yes" for r in it["rows"]), it["id"])

    def test_templates_exist(self):
        for it in self.cl["items"]:
            for t in it.get("templates", []):
                self.assertTrue((ROOT / "templates" / "test_evidence" / f"{t}.md").exists(), f"{it['id']} {t}")

    def test_templates_are_labelled_proposals(self):
        for p in (ROOT / "templates" / "test_evidence").glob("*.md"):
            self.assertIn("PROPOSAL", p.read_text(encoding="utf-8").upper(), p.name)

    def test_unknown_resolution_text_present(self):
        for it in self.cl["items"]:
            if it["applies_when"] != {"always": True}:
                self.assertTrue(it.get("to_settle"), it["id"])

    @unittest.skipIf(yaml is None, "PyYAML not installed")
    def test_json_mirror_matches_yaml(self):
        y = yaml.safe_load((ROOT / "data" / "checklist.yaml").read_text(encoding="utf-8"))
        ids_y = [i["id"] for i in y["items"]]
        ids_j = [i["id"] for i in self.cl["items"]]
        self.assertEqual(ids_y, ids_j)
        for a, b in zip(y["items"], self.cl["items"]):
            self.assertEqual(a["rows"], b["rows"], a["id"])
            self.assertEqual(a["applies_when"], b["applies_when"], a["id"])
        s = yaml.safe_load((ROOT / "data" / "answers_schema.yaml").read_text(encoding="utf-8"))
        self.assertEqual(s["questions"].keys(), engine.load_schema()["questions"].keys())

    def test_conditions_use_valid_answer_values(self):
        schema = engine.load_schema()["questions"]

        def walk(c):
            if not isinstance(c, dict):
                return
            for op, arg in c.items():
                if op in ("eq", "in", "tri", "contains", "any_contains"):
                    q = arg[0]
                    self.assertIn(q, schema)
                    vals = arg[1] if isinstance(arg[1], list) else [arg[1]]
                    for v in vals:
                        self.assertIn(v, schema[q]["values"], f"{q}={v}")
                elif op in ("all", "any"):
                    for x in arg:
                        walk(x)
                elif op == "not":
                    walk(arg)
        for it in self.cl["items"]:
            walk(it["applies_when"])


if __name__ == "__main__":
    unittest.main()
