<p align="center"><img src="assets/banner.svg" alt="Ikhtibar" width="100%"></p>

# Ikhtibar 🌸

A comparative evidence base on testing AI systems before deployment, with a gap analysis for UAE government deployment and a small self assessment tool. The question: across governments and institutes, what is required, what is recommended, and what is merely described?

**Research, not legal advice.** Nothing here states what the UAE or any other jurisdiction requires unless a cited source that was retrieved and read says so. A qualified lawyer must review anything before it is relied on for compliance. This README is generated from the data files by `python -m ikhtibar.build_docs`.

## Status 🌷

Version 2.0 (phase 2), 12 October 2026. {{n_rows}} evidence rows ({{n_test_all}} test provisions). Verification by independent AI subagents using only the standard fetch tool: {{ver_all_n}} rows checked in phase 2 with {{ver_all_err}} errors among {{ver_all_verifiable}} verifiable rows ({{ver_all_rate}}%, 95% interval {{ver_all_lo}}% to {{ver_all_hi}}%). {{n_unreliable_rows}} rows are excluded from the headline counts (unverified, unverifiable, or resting on a summary or secondary report only). Of {{n_test_head}} headline test provisions, {{head_mc}} ({{head_mc_pct}}) are mandatory or conditional and {{head_vg}} ({{head_vg_pct}}) are voluntary or guidance.

## What is documented

Documented means a retrieved source says it, and the row records where.

- Each evidence row holds a paraphrase, a clause or page locator, a binding status, who tests, the source address, the retrieval date, the language read, and a verification status with a note. Quotations are short and attributed.
- Verification outcomes per row, the raw verification files, the rules the verifiers followed, and every correction with its reason (`data/patches.json`).
- Time sensitive items checked against primary sources, with locator, retrieval date, access path and any conflict (`data/time_sensitive.csv`).
- Every UAE search and fetch, and every source, with whether an original or a translation was read and whether an English rendering was produced by the fetch tool (`data/uae_search_log.csv`, `data/uae_sources.csv`).

## What is interpreted

Interpreted means the analyst's judgement. It is labelled as such in the report.

- The binding status coding (mandatory, conditional, voluntary, guidance, ambiguous) and the test type taxonomy.
- The gap analysis in Section 8 of `docs/REPORT.md`. It describes gaps in the documents retrieved, not in UAE law.
- The assurance checklist and its applicability rules. They are proposals.
- The test evidence templates in `templates/test_evidence/`. They are labelled proposals.
- The hypothetical worked example `examples/MADOUN_EXAMPLE.md`, based on a synthetic prototype that is not deployed and is not used or endorsed by any authority.

## What is still open

- {{n_blocked}} rows rest on sources that rejected the standard fetch tool or timed out, and {{n_unverifiable_other}} are readable but could not be located. They are not worked around. The exact documents to download by hand are in `docs/DOWNLOAD_LIST.md`.
- EU Omnibus operative dates (Article 113 and others) are confirmed at recital level only. DoH Responsible AI Standard revision status is unknown. DIFC amendments after Version No. 2 are unchecked. The Saudi instruments cannot be called final. See `docs/TIME_SENSITIVE.md`.
- {{n_not_rechecked}} rows were not re checked in phase 2.
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

Huda Mueen. Analysis prepared with Claude AI research assistance under her direction.
