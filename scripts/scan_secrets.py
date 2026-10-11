#!/usr/bin/env python3
"""Small secrets scan with no dependencies: working tree and (if present) git history.

It complements, not replaces, a maintained scanner. Use detect-secrets (Apache-2.0) or gitleaks (MIT) as well; see README.
Exit status 1 if anything matches.
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "private key block": r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----",
    "AWS access key id": r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b",
    "GitHub token": r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}\b|\bgithub_pat_[A-Za-z0-9_]{40,}\b",
    "Slack token": r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b",
    "Google API key": r"\bAIza[0-9A-Za-z_\-]{35}\b",
    "OpenAI or Anthropic style key": r"\bsk-(?:ant-)?[A-Za-z0-9_\-]{32,}\b",
    "JWT": r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\b",
    "generic secret assignment": r"(?i)\b(?:api[_-]?key|secret|passwd|password|token)\b\s*[:=]\s*['\"][^'\"\s]{12,}['\"]",
    "bearer header": r"(?i)authorization\s*[:=]\s*['\"]?bearer\s+[A-Za-z0-9_\-\.]{20,}",
}
SKIP = {".git", "__pycache__", ".pytest_cache"}
SELF = {"scripts/scan_secrets.py", "tests/test_scripts.py"}
SKIP_SUFFIX = {".pyc"}

def scan_text(name, text, hits):
    for label, pat in PATTERNS.items():
        for m in re.finditer(pat, text):
            line = text.count("\n", 0, m.start()) + 1
            hits.append(f"{name}:{line}: {label}")

def main():
    hits = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or set(p.relative_to(ROOT).parts) & SKIP or p.suffix in SKIP_SUFFIX:
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel in SELF:
            continue
        try:
            scan_text(rel, p.read_text(encoding="utf-8", errors="ignore"), hits)
        except OSError:
            pass
    if (ROOT / ".git").exists():
        try:
            log = subprocess.run(["git", "-C", str(ROOT), "log", "-p", "--all", "--no-color"], capture_output=True, text=True, timeout=120).stdout
            scan_text("git-history", log, hits)
        except Exception as e:  # git missing or no commits
            print("note: git history not scanned:", e)
    if hits:
        print("secrets scan FAILED:")
        for h in sorted(set(hits)): print("  -", h)
        return 1
    print("secrets scan passed (working tree and git history)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
