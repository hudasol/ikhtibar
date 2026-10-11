import tempfile, unittest
from pathlib import Path
import check_content, scan_secrets


class ContentCheckTests(unittest.TestCase):
    def run_in(self, files):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name, data in files.items():
                p = root / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))
            old = (check_content.ROOT, check_content.ALLOW_FILE)
            check_content.ROOT, check_content.ALLOW_FILE = root, root / ".contentcheck-allow"
            try:
                return check_content.main()
            finally:
                check_content.ROOT, check_content.ALLOW_FILE = old

    def test_repository_passes(self):
        self.assertEqual(check_content.main(), 0)

    def test_pdf_is_rejected(self):
        self.assertEqual(self.run_in({"a/standard.pdf": b"%PDF-1.4"}), 1)

    def test_long_quotation_is_rejected(self):
        quote = " ".join(["word"] * 25)
        self.assertEqual(self.run_in({"x.md": f'The text says "{quote}" here.'}), 1)

    def test_short_quotation_is_accepted(self):
        self.assertEqual(self.run_in({"x.md": 'The text says "established performance benchmarks" here.'}), 0)

    def test_copyright_notice_is_rejected(self):
        self.assertEqual(self.run_in({"x.txt": "Copyright ISO 2023. All rights reserved."}), 1)

    def test_long_csv_cell_is_rejected(self):
        cell = " ".join(["w"] * 130)
        self.assertEqual(self.run_in({"t.csv": f"requirement_paraphrase,x\n{cell},1\n"}), 1)


class SecretsScanTests(unittest.TestCase):
    def test_repository_passes(self):
        self.assertEqual(scan_secrets.main(), 0)

    def test_detects_planted_secrets(self):
        fake_aws = "AKIA" + "ABCDEFGHIJKLMNOP"
        fake_key = "-----BEGIN " + "RSA PRIVATE KEY-----"
        fake_gh = "ghp_" + "a" * 36
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "a.txt").write_text(f"{fake_aws}\n{fake_key}\n{fake_gh}\n", encoding="utf-8")
            old = scan_secrets.ROOT
            scan_secrets.ROOT = root
            try:
                self.assertEqual(scan_secrets.main(), 1)
            finally:
                scan_secrets.ROOT = old


if __name__ == "__main__":
    unittest.main()
