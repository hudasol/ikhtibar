# Overnight log, phase 5 (3 November 2026)

Frozen reference for the compiled paper: commit fa3e410 (local tag `v4.0-paper-frozen`; remote branch `frozen/v4.0-paper`). The remote refused to accept the tag push through the session proxy (HTTP 403 on tag refs), so a branch at the same commit was created through the repository connector. The branch must not be advanced.

## Orientation
- Tests (93), content check and secrets scan passed before any change. At the end: 100 tests, content check and secrets scan pass.
- Preregistration committed first: `docs/PREREG_PHASE5.md` (commit 456dc34).

## Task 2 extraction recall
- Sample drawn with seed 20261103: 14 documents from 8 family groups (`data/extraction_recall/sample.json`).
- First round of fourteen independent readers: only 3 of 14 could open their address, because the fetch tool accepts only addresses that have appeared in search results. Eleven were refused, were stopped after one retry as the access rule requires, and were relaunched after the addresses had been surfaced by a standard search.
- Model identity was recorded for every run in `data/model_identity_log.csv`.

## Task 1 preregistration
- Twelve predictions with ranges and a scoring plan were committed before any new row (`docs/PREREG_PHASE5.md`).

## Task 2 extraction recall
- After retries, 12 of 14 sampled documents were readable, 3 of them in full text. Recall 38.3% (row interval 33.6% to 43.2%; document bootstrap 25.8% to 56.1%), below the predicted 55% to 85%. Precision 100% on 11 rows from 3 documents (predicted 75% to 95%; too few to judge). Missed provisions are less often binding than matched ones (4.2% against 10.1%): hit.
- A second agent re-matched 30% of provisions with 79.5% agreement.

## Task 3 out of sample replication
- 19 United States rows verified and added; second reference list of 189 instruments; 78 rows added from newly read documents; fresh verification of every new row (6 strict errors, 7.7%); blind recoding of 97 new rows.
- Binding share: 27.9% frozen (290 rows), 24.8% extended (355 rows), 7.7% on the 52 rows from the second list (below the predicted 15% to 40%: miss). The process only gap stays positive (17.2 points on the extended table, 16.5 on the few binding new rows).
- Document prior on unseen documents equals the majority rate (78.8%) and the wording rule scores 75.0% (predicted 45% to 65%: miss), because almost every new row is non binding.
- Baselines rerun on the extended table (355 rows, seed 20261028); frozen results are kept in `data/phase5/frozen_v4/`.
- Completeness recall on the second list is 23.1% strict (predicted 30% to 65%: miss).

## Task 4 UAE Arabic check
- Blocked: the search budget was used up before any original could be located. No row compared. Prediction 8 not tested. Script and tests ready.

## Task 5 time sensitive rereads
- Blocked for the same reason. Items stay "not determined".

## Task 6 paper
- New section "Extension, out of sample replication and further checks", with the frozen and extended comparison table and the predictions table; abstract, contributions, limitations and conclusion updated. Every new number is read from a committed result file. The compiled paper has 17 pages in the article class used here; an IEEE conference paper is normally limited to 6 to 8 pages, so the paper needs cutting or a journal template before submission.

## Task 7 review and handover
- Gap analysis section F, handoff, human gold instructions and the morning note were updated. Decisions D11 to D22 are in `docs/DECISIONS.md`.
