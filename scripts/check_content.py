#!/usr/bin/env python3
"""Fail if the repository holds paywalled or copyrighted material that should not be committed.

Checks (thresholds are constants below so they can be argued with):
  1. No document binaries (pdf, epub, docx, xlsx, pptx, zip, mobi) outside an explicit allow list.
  2. No file larger than MAX_FILE_BYTES.
  3. No long quotations: a quoted span of QUOTE_WORDS words or more in markdown, and no CSV cell with more than
     CELL_WORDS words in the paraphrase and note columns (paraphrase should be short).
  4. No standards body copyright notices in text files (a sign that standard text was pasted in).
  5. No long verbatim overlaps between two different text files is not testable offline; reviewers should spot check.
Exit status 1 on any failure.
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BINARY_EXT = {".pdf", ".epub", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".zip", ".mobi", ".djvu"}
MAX_FILE_BYTES = 2_000_000
QUOTE_WORDS = 20          # protocol: short attributed quotes only (under 15 words); 20 gives a margin for detection
CELL_WORDS = 120
CELL_COLS = {"requirement_paraphrase", "interpretation_note", "verification_note"}
NOTICE_RE = re.compile(r"(©|\(c\)|copyright)\s*(iso|iec|ieee|cen|bsi|astm|ansi)\b|all rights reserved", re.I)
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".pytest_cache"}
ALLOW_FILE = ROOT / ".contentcheck-allow"

def allowed():
    if not ALLOW_FILE.exists():
        return set()
    return {l.split("#")[0].strip() for l in ALLOW_FILE.read_text(encoding="utf-8").splitlines() if l.split("#")[0].strip()}

def files():
    for p in ROOT.rglob("*"):
        if p.is_file() and not (set(p.relative_to(ROOT).parts) & SKIP_DIRS):
            yield p

def words(s):
    return len(s.split())

def quoted_spans(text):
    """Pair quotation marks in order on each line (straight pairs, then curly pairs)."""
    for line in text.splitlines():
        pos = [i for i, ch in enumerate(line) if ch == '"']
        if len(pos) % 2 == 0:
            for a, b in zip(pos[0::2], pos[1::2]):
                yield line[a + 1:b]
        for m in re.finditer("\u201c([^\u201d]*)\u201d", line):
            yield m.group(1)

def main():
    allow = allowed()
    bad = []
    for p in files():
        rel = p.relative_to(ROOT).as_posix()
        if rel in allow:
            continue
        if p.suffix.lower() in BINARY_EXT:
            bad.append(f"{rel}: document binary committed (paywalled or copyrighted PDFs and office files are not allowed)")
            continue
        if p.stat().st_size > MAX_FILE_BYTES:
            bad.append(f"{rel}: larger than {MAX_FILE_BYTES} bytes")
            continue
        if p.suffix.lower() not in {".md", ".txt", ".csv", ".yaml", ".yml", ".json", ".py"}:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if NOTICE_RE.search(text) and rel not in {"scripts/check_content.py"} and not rel.startswith("tests/"):
            bad.append(f"{rel}: contains a copyright or all rights reserved notice (is standard text pasted in?)")
        if p.suffix.lower() == ".md":
            for q in quoted_spans(text):
                if words(q) >= QUOTE_WORDS:
                    bad.append(f"{rel}: quoted span of {words(q)} words: {q[:60]}...")
        if p.suffix.lower() == ".csv":
            with open(p, encoding="utf-8", newline="") as f:
                for i, r in enumerate(csv.DictReader(f), 2):
                    for c in CELL_COLS & set(r):
                        if words(r[c] or "") > CELL_WORDS:
                            bad.append(f"{rel} line {i} column {c}: {words(r[c])} words")
                        for q in quoted_spans(r[c] or ""):
                            if words(q) >= QUOTE_WORDS:
                                bad.append(f"{rel} line {i} column {c}: quoted span of {words(q)} words")
    if bad:
        print("content check FAILED:")
        for b in bad: print("  -", b)
        return 1
    print("content check passed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
