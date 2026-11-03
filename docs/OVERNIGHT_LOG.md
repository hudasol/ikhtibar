# Overnight log, phase 5 (3 November 2026)

Frozen reference for the compiled paper: commit fa3e410 (local tag `v4.0-paper-frozen`; remote branch `frozen/v4.0-paper`). The remote refused to accept the tag push through the session proxy (HTTP 403 on tag refs), so a branch at the same commit was created through the repository connector. The branch must not be advanced.

## Orientation
- Tests (93), content check and secrets scan passed before any change.
- Preregistration committed first: `docs/PREREG_PHASE5.md` (commit 456dc34).

## Task 2 extraction recall
- Sample drawn with seed 20261103: 14 documents from 8 family groups (`data/extraction_recall/sample.json`).
- First round of fourteen independent readers: only 3 of 14 could open their address, because the fetch tool accepts only addresses that have appeared in search results. Eleven were refused, were stopped after one retry as the access rule requires, and were relaunched after the addresses had been surfaced by a standard search.
- Model identity was recorded for every run in `data/model_identity_log.csv`.
