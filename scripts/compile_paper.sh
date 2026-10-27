#!/bin/sh
# Compile the paper outside the repository tree (the content check rejects PDFs inside it).
# Usage: scripts/compile_paper.sh [output directory]   (default: a new temporary directory)
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd)
OUT=${1:-$(mktemp -d)}
PYTHONPATH="$ROOT/src" python "$ROOT/scripts/build_paper.py"
cp "$ROOT/paper/main.tex" "$ROOT/paper/refs.bib" "$OUT/"
cd "$OUT"
pdflatex -interaction=nonstopmode main > /dev/null
bibtex main > /dev/null
pdflatex -interaction=nonstopmode main > /dev/null
pdflatex -interaction=nonstopmode main > /dev/null
echo "$OUT/main.pdf"
