<p align="center"><img src="assets/banner.svg" alt="Ikhtibar" width="100%"></p>

# Ikhtibar 🌸

A comparative evidence base on testing AI systems before deployment, with a gap analysis for UAE government deployment and a small self assessment tool. The question: across governments and institutes, what is required, what is recommended, and what is merely described?

**Research, not legal advice.** Nothing here states what the UAE or any other jurisdiction requires unless a cited source that was retrieved and read says so. A qualified lawyer must review anything before it is relied on for compliance. This README is generated from the data files by `python -m ikhtibar.build_docs`.

## Status 🌷

Version 4.0 (phase 4), 28 October 2026. Phase 4 added baselines, a tool evaluation, blind second codings, a robustness analysis, a fresh verification sample, a completeness pilot and a conference paper draft (see `docs/EVALUATION.md`; judgement calls in `docs/DECISIONS.md`). Counts are computed from the current table, which includes the 25 phase 4 corrections. 522 evidence rows (311 test provisions), 56 of them added in phase 3. Phase 3 re-checked the 175 rows phase 2 had left open and ran a fresh independent check: in a seeded random sample of 30 rows, 3 of 23 verifiable rows had an error under a strict rubric (13.0%, 95% interval 4.5% to 32.1%), all corrected. 38 rows are excluded from the headline counts (unverified, unverifiable, superseded, or resting on a summary or secondary report only). Of 290 headline test provisions, 81 (28%) are mandatory or conditional, 174 (60%) are voluntary or guidance and 35 (12%) are ambiguous.

## What is documented

Documented means a retrieved source says it, and the row records where.

- Each evidence row holds a paraphrase, a clause or page locator, a binding status, who tests, the source address, the retrieval date, the language read, and a verification status with a note. Quotations are short and attributed.
- Verification outcomes per row, the raw verification files, the rules the verifiers followed, and every correction with its reason (`data/patches.json`; phase 3 in `data/verification/phase3/`).
- Time sensitive items checked against primary sources, with locator, retrieval date, access path and any conflict (`data/time_sensitive.csv`).
- Every UAE search and fetch, and every source, with whether an original or a translation was read and whether an English rendering was produced by the fetch tool (`data/uae_search_log.csv`, `data/uae_sources.csv`).

## What is interpreted

Interpreted means the analyst's judgement. It is labelled as such in the report.

- The binding status coding (mandatory, conditional, voluntary, guidance, ambiguous) and the test type taxonomy.
- The normative force coding of non binding rows (obligation wording, recommendation, description), double coded in `data/coding/`.
- The lead analyst's re-grading of verifier verdicts against the rubric (`data/verification/phase3/verdict_reclass.csv`).
- The gap analysis in Section 8 of `docs/REPORT.md`. It describes gaps in the documents retrieved, not in UAE law.
- The assurance checklist and its applicability rules. They are proposals.
- The test evidence templates in `templates/test_evidence/`. They are labelled proposals.
- The hypothetical worked example `examples/MADOUN_EXAMPLE.md`, based on a synthetic prototype that is not deployed and is not used or endorsed by any authority.

## What is still open

- 32 rows rest on sources that rejected the standard fetch tool, mainly Canada's Directive on Automated Decision-Making, and 1 are readable but could not be located. They are not worked around. The documents to download by hand are in `docs/DOWNLOAD_LIST.md` and Appendix B of the report.
- Seven sampled UAE and ISO rows could not be re-read on 16 October because their sources moved or exceeded the fetch limit; on 28 October five of the six moved UAE sources were read again, and UAE-Dubai-008 is still too large for the fetch tool.
- About 22% of the phase 4 fresh verification sample (26 of 120 rows, after two retry rounds) could not be read in the working session, so its error rate describes readable rows only (`docs/EVALUATION.md`).
- The scope of the UAE National Cyber Security Policy for AI for emirate government entities was read differently by two verifiers; check it by hand.
- The DoH Responsible AI Standard revision falls due in October 2026; the DIFC Regulation 10 amendments are consulted on but not enacted; the Saudi instruments are not final. See `docs/TIME_SENSITIVE.md`.
- Some phase 3 rows were read from PDFs saved by the fetch tool and extracted locally; this is recorded per row in `access_path`.
- Arabic originals were obtained for only part of the UAE sources (`docs/UAE_COVERAGE.md`).
- Licences are proposed, not applied (`docs/LICENSING.md`).

## Quick start

Requires Python 3.10 or later and PyYAML for the build scripts. The command line tool and tests need only the Python standard library once `data/checklist.json` exists, which it does in this repository.

```
python -m pip install -r requirements.txt
export PYTHONPATH=src
python -m ikhtibar.cli --list-questions
python -m ikhtibar.cli --system-type predictive_ml --audience internal --decision-impact significant_support
python -m ikhtibar.cli --answers examples/madoun_answers.json --format markdown
python -m ikhtibar.staleness --max-age-days 180
python -m unittest discover -s tests
python scripts/check_content.py
python scripts/scan_secrets.py
python -m ikhtibar.build_all
```

The tool returns, for each checklist item, APPLIES, DOES_NOT_APPLY or UNKNOWN, with source traces and what would settle each UNKNOWN. A missing answer never makes an item apply or not apply. Staleness checks are offline: the script flags rows past `next_review_by` and never fetches anything; a blocked site stays blocked.

## Repository map

| Path | Contents |
|---|---|
| `docs/REPORT.md`, `docs/EXECUTIVE_BRIEF.md` | Generated report and brief |
| `docs/DOWNLOAD_LIST.md` | Documents to download by hand |
| `docs/UAE_COVERAGE.md`, `docs/TIME_SENSITIVE.md` | Phase 2 records |
| `docs/EVALUATION.md`, `docs/DECISIONS.md`, `docs/GAP_ANALYSIS.md` | Phase 4 evaluation (generated), decision log, limitations and plan |
| `paper/` | Conference paper draft, generated from the result files (`scripts/build_paper.py`, `scripts/compile_paper.sh`) |
| `data/baselines/`, `data/evaluation/`, `data/robustness.json`, `data/completeness/`, `data/coding/phase4/` | Phase 4 result files and inputs |
| `docs/LICENSING.md` | Licence proposal and library licence record |
| `data/evidence_table.csv` | The evidence table |
| `data/checklist.yaml`, `data/answers_schema.yaml` | Checklist and questions |
| `data/verification/` | Raw verification results |
| `src/ikhtibar/` | Build scripts, engine, command line tool |
| `templates/test_evidence/` | Evidence templates by test type |
| `scripts/` | Content check (long quotations and document binaries) and secrets scan |
| `tests/` | Unit tests |

## Licences

Proposal only, to be confirmed by the author: documents and data under CC BY 4.0, code under the MIT licence. Reasons and the licence record for libraries and data are in `docs/LICENSING.md`. Source documents remain the property of their publishers; this repository stores paraphrases and short attributed quotations, and a check fails the build on long quotations or document binaries.

## Author

Huda Mueen. Analysis prepared with AI research assistance under her direction.
