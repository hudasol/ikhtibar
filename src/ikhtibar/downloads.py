"""Build docs/DOWNLOAD_LIST.md: documents the maintainer must open by hand, from rows that could not be verified."""
import csv, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def main():
    rows = list(csv.DictReader(open(ROOT / "data/evidence_table.csv", encoding="utf-8", newline="")))
    un = [r for r in rows if r["verification_status"] in ("UNVERIFIED_BLOCKED", "UNVERIFIABLE_OTHER", "ERROR_WITHDRAWN", "UNVERIFIED_SOURCE_NOT_READ")]
    by = collections.defaultdict(list)
    for r in un:
        by[(r["family"], r["source_url"].split("#")[0], r["verification_status"], r["block_type"])].append(r)
    L = ["# Documents to download and check by hand", "",
         "These rows could not be verified this round, either because the publisher's site rejected the fetch tool (no workaround was used), the tool truncated the document, or the source was never read in full. "
         "Open each document in a normal browser, check the row, then update `data/patches.json` and re run `python -m ikhtibar.build_all`. Free documents only; where a standard is paywalled the row stays catalogue level and nothing needs buying.", "",
         f"Rows listed: **{len(un)}** in **{len(by)}** source groups.", "",
         "| Family | Document URL | Status | Block type | Rows | What to check |", "|---|---|---|---|---|---|"]
    for (fam, url, st, bt), rs in sorted(by.items()):
        ids = ", ".join(f"`{r['row_id']}`" for r in sorted(rs, key=lambda x: x["row_id"]))
        hint = (rs[0]["document_to_download"] or "locator, paraphrase, status, who tests").replace("|", "/").replace("\n", " ")[:220]
        L.append(f"| {fam} | {url} | {st} | {bt or '-'} | {ids} | {hint} |")
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs/DOWNLOAD_LIST.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("download list:", len(un), "rows,", len(by), "groups")

if __name__ == "__main__":
    main()
