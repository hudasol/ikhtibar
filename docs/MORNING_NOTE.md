# Morning note (3 November 2026)

Plain words. Everything is committed and pushed to `main`. Tests (100), the content check and the secrets scan pass. The version 4.0 results are frozen at commit fa3e410 and kept beside the new ones.

## Numbers that changed
- Table: 290 headline test rows became 355. Binding share 27.9% (81 rows) became 24.8% (88 rows). Mandatory 26 became 30, ambiguous 35 became 36.
- On the 52 new rows from the second reference list the binding share is only 7.7%.
- Error rate of the new rows in fresh checks: 7.7% (6 of 78). Pooled with the earlier fresh samples: 7.4%.
- Completeness against the second reference list: 23.1% (the first pilot gave 68.4%).
- Extraction recall: 38.3%. This means the table holds the main provisions of a document, not all of them.

## What replicated and what did not
Replicated (6 hits of 12 predictions): binding provisions are still a minority on documents the table had not seen; sector regulators are more binding than national frameworks; the process only gap stays positive; the document prior does as well as the majority rate on unseen documents; unseen families are below 25% binding; missed provisions are less often binding; the error rate on new rows is inside the predicted range.
Did not replicate (5 misses): the binding share on new documents was lower than predicted; the wording rule did better than predicted; completeness and extraction recall were lower than predicted; precision was 100% on too few rows to be informative. The paper says so in the new section.
Not tested: UAE Arabic agreement.

## What failed or was blocked
- The Arabic check of UAE rows and the time sensitive rereads: the search budget was used up. Scripts and inputs are ready. The question whether the National Cyber Security Policy for AI covers emirate level bodies is still open.
- Fresh checks of existing rows: only 3 of 30 could be read, so they add nothing.
- The tag push to GitHub was refused by the proxy; the frozen version is on the branch `frozen/v4.0-paper`.
- The compiled paper is 17 pages. IEEE conference papers are normally 6 to 8, so it must be cut or moved to a journal template.

## Your first three actions
1. Label the 100 rows in `data/coding/phase4/human_gold_template.csv` (instructions beside it), then run the agreement script.
2. Download the blocked documents in `docs/DOWNLOAD_LIST.md`, and run the Arabic check when you have a session with search budget.
3. Decide on the venue and a reviewer for the UAE rows; the paper must not go out as legal analysis.

## Traces of the assistant that I could not remove
- Model identity: you asked for exact model identity and also for no vendor name anywhere. I kept the log and wrote "language model version 5.5 (mid size tier)", with the identifier field reading "identifier withheld" (decision D21). Say if you want the exact identifier added back.
- Published history: `main` and the frozen branch are clean (all commits under your name and address, no trailers or session links). The closed pull request reference `refs/pull/1/head` on GitHub still holds 3 early commits authored as the assistant, with attribution trailers. They are not on `main`. Removing them would mean rewriting published history or recreating the repository, which I did not do.
- Source content: a few table rows quote company and product names that appear inside regulators' own texts (a signatory list, a coding assistant named in a source). That is source content, not attribution, and was left.
- File contents: local paths with the workspace user name, the vendor name in the run metadata and one code constant were replaced in a new commit.
