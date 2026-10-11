import io, json, unittest
from contextlib import redirect_stdout, redirect_stderr
from tests.helpers import ROOT
from ikhtibar import cli


def call(argv):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        try:
            code = cli.main(argv)
        except SystemExit as e:
            code = e.code
    return code, out.getvalue(), err.getvalue()


class CliTests(unittest.TestCase):
    def test_json_output_is_valid(self):
        code, out, _ = call(["--system-type", "agentic", "--format", "json"])
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertIn("items", data)
        self.assertIn("disclaimer", data)

    def test_invalid_value_exit_2(self):
        code, _, err = call(["--audience", "martians"])
        self.assertEqual(code, 2)

    def test_list_questions(self):
        code, out, _ = call(["--list-questions"])
        self.assertEqual(code, 0)
        self.assertIn("system_type", out)

    def test_answers_file(self):
        code, out, _ = call(["--answers", str(ROOT / "examples" / "madoun_answers.json"), "--format", "text"])
        self.assertEqual(code, 0)
        self.assertIn("UNKNOWN", out)

    def test_no_arguments_returns_unknowns(self):
        code, out, _ = call(["--format", "json"])
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertGreater(data["summary"]["UNKNOWN"], 0)
        self.assertEqual(data["summary"]["DOES_NOT_APPLY"], 0)


if __name__ == "__main__":
    unittest.main()
