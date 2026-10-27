# Ikhtibar: limitations audit and remediation plan (phase 4)

Written on 28 October 2026 from a read of the repository at the end of phase 3 (522 evidence rows, 63 tests passing). This file is hand written. It lists what stops the work from being a submittable research paper, what will be done about each item, and what only the author can do. Status values are updated as work lands.

Reviewer standard assumed: a reader who asks (1) is every claim traceable, (2) can every number be reproduced, (3) against what is the method compared, (4) how complete is the evidence, (5) who other than the author checked it, and (6) what is not claimed.

## A. Gaps found

| ID | Gap | Why it matters | Evidence in repository | Severity |
|---|---|---|---|---|
| G1 | No baselines. The binding status coding, the test type coding and the checklist tool were never compared with anything simpler. | A reviewer cannot tell whether the coding adds anything beyond reading the word "shall", or whether the tool beats a trivial rule. | No baseline code or results in `src/` or `data/`. | High |
| G2 | All coding was done by AI subagents of one model family. Only normative force was double coded. Binding status and test type have one coder. No human gold labels. | Reliability is unmeasured for the two fields that drive the headline split. | Report Section 10, item 6. `data/coding/` holds normative force only. | High |
| G3 | Verification error rate is high and imprecise. Fresh sample: 3 of 23 readable rows (13.0%, 95% interval 4.5% to 32.1%). All verifiers are AI. | The interval is too wide to support a stated accuracy of the table. | Report Appendix A. | High |
| G4 | Completeness is unknown. No estimate of how many relevant instruments were missed. | "Most testing text is not binding" is only as good as the sampling frame. | Report Section 6.3 lists absences but no recall estimate. | High |
| G5 | Headline counts are not tested for sensitivity. | A change in one family, one coding rule or the excluded rows might change the headline. | Only one scenario (all excluded rows counted) is reported. | Medium |
| G6 | Unit of analysis is the extracted provision. Counts depend on document length. | Long guidance documents inflate the non binding share. | Report Section 5.4 warns but does not correct. | Medium |
| G7 | The checklist tool has unit tests but no independent evaluation and no comparison. | A tool paper needs a specification test written without sight of the code. | `tests/test_engine.py` was written by the engine's author. | Medium |
| G8 | 32 rows rest on sources that rejected the fetch tool (Canada 24, ISO, SDAIA, NCA). | Canada contributes no headline rows. | `docs/DOWNLOAD_LIST.md`. | Medium |
| G9 | Six UAE sources could not be re-read on 16 October (moved or too large). | UAE is the application focus. | Report Section 11, item 2. | Medium |
| G10 | Status items were last checked on 16 October. The DoH Responsible AI Standard revision fell due in October. | Time sensitive claims go stale. | `docs/TIME_SENSITIVE.md`. | Medium |
| G11 | No manuscript, related work section, bibliography or paper style limitations and ethics statements. | Not submittable. | No `paper/` directory. | High |
| G12 | No data sheet, no frozen release, no archive identifier. | Reproducibility and citation. | No `CITATION.cff`, no release tag. | Medium |
| G13 | No expert review (domain or legal). | Interpretation and Section 8 are the author's judgement. | Report Section 11. | High, author action |
| G14 | Licences proposed, not applied. | A paper needs an explicit data licence. | `docs/LICENSING.md`. | Low, author action |
| G15 | Arabic originals read for part of the UAE sources only. | Arabic text governs in some cases. | `language_read` column. | Medium |

## B. Plan

Work is done in small commits straight to main, with the full test suite, `check_content` and `scan_secrets` passing before each push.

| Step | Closes | Work | Output |
|---|---|---|---|
| P1 | G1, G2 | Baselines for binding status and test type: majority class, document level prior, modal verb rule, TF-IDF with logistic regression, evaluated with stratified cross validation and with leave one family out, bootstrap intervals, error analysis. Second blind AI coder on a seeded sample, with Cohen's kappa. A 100 row gold template for a human coder. | `src/ikhtibar/baselines.py`, `data/baselines/`, generated report section |
| P2 | G7 | Preregistered evaluation of the tool: predictions written from the specification alone and committed before any run; 40 or more scenarios; comparison with two naive baselines; a simulation over synthetic deployment profiles that measures how many answers settle the checklist. | `data/evaluation/`, `docs/EVALUATION.md` |
| P3 | G3 | A larger fresh independent verification sample (seeded), then a pooled estimate with intervals by error type. | `data/verification/phase4/`, updated Appendix A |
| P4 | G4 | Completeness benchmark: an independent reference list of instruments built by search before looking at the table, with recall, and a capture recapture estimate. | `data/completeness/`, report section |
| P5 | G5, G6 | Robustness: leave one family out, best and worst cases for excluded rows, ambiguous treatment, and a document level analysis that removes the length effect. | generated report section |
| P6 | G9, G10, G15 | Re-attempt moved UAE sources by searching for their current address; re-check status items (DoH, DIFC, Saudi, EU) as of 28 October. | updated rows and `TIME_SENSITIVE.md` |
| P7 | G11, G12 | Manuscript in LaTeX with bibliography of sources actually read, data sheet, `CITATION.cff`, reproducibility statement, limitations, ethics and threats to validity. | `paper/` |
| P8 | all | Adversarial self review, regenerate, run all checks, push. | `docs/HANDOFF.md` |

## C. What only the author can do

1. Download the blocked documents (Canada Directive, ISO catalogue pages, SDAIA files) so the 32 unverified rows can be checked. Steps are in `docs/DOWNLOAD_LIST.md`.
2. Label the 100 row gold template (about one hour) so that a human, not a model, is the reference for binding status.
3. Arrange a domain or legal reviewer for Section 8 and the UAE rows.
4. Choose licences and add the files.
5. Choose the venue and its template, and approve authorship and acknowledgements.

## E. Status at the end of the first phase 4 session (28 October 2026)

| ID | Status | What was done, and what is left |
|---|---|---|
| G1 | Closed | Baselines for binding status and test type with cross validation and leave one family out (`docs/EVALUATION.md`, section 1). Findings: binding status is mostly document level; the best test type baseline is a keyword rule. |
| G2 | Partly closed | Two blind AI second codings of 120 rows (kappa 0.91 between blind coders, about 0.65 with the original). Both coders are models, so a human second coding is still needed (100 row template ready). |
| G3 | Partly closed | Fresh sample of 120 rows, 73 readable: strict error rate 6.8% (3.0% to 15.1%); pooled with the phase 3 sample 8 of 96. Verifiers are AI. 39% of the sample could not be read because of a session domain restriction. A retry with a fresh search budget is scheduled. |
| G4 | Partly closed | Pilot recall 68.4% on 19 confirmed candidates (46.0% to 84.6%), with 58 unresolved. All confirmed misses are United States federal documents. A capture recapture estimate was not attempted: the two lists were built under the same search tools, so they are not independent, and the method has been questioned for searches of this kind. Widening the reference list needs web access. |
| G5 | Closed | Robustness analysis. The statement that binding is a minority survives every scenario tried (most favourable 44.1%). |
| G6 | Closed for the headline | Document level and family level weighting and a cluster bootstrap are reported. |
| G7 | Closed | 94 preregistered scenarios, four naive baselines, 3000 profile simulation. Two defects found and fixed; one documented conservative divergence (D3). |
| G8 | Open, author action | 32 rows still blocked. |
| G9 | Mostly closed | Five of six moved UAE sources were reread on 28 October (UAE-Federal-009, 012, 021, 027, 031); UAE-Dubai-008 is still blocked by file size and has a date conflict recorded. |
| G10 | Open | Of 181 status items only 22 were reread on 28 October and none changed; 154 could not be fetched in the session and 5 were not found. A retry is scheduled. The DoH revision, DIFC Regulation 10 enactment, EU, Korea decree and Canada versions are not determined. |
| G11 | Draft done | `paper/` holds a generated draft (nine pages). Related work is thin for Gulf governance and public sector assurance, and most works were read at abstract level. |
| G12 | Partly closed | Data sheet and citation file added. No frozen release or archive identifier yet; to be made once the author has chosen licences and venue. |
| G13 | Open, author action | No domain or legal review. |
| G14 | Open, author action | Licences not applied. |
| G15 | Open | Arabic originals still partial. |

## D. What is not claimed

No claim is made about what the UAE or any other jurisdiction requires beyond what a retrieved source states. Baselines measure how predictable the coding is from text. They do not establish that the coding is correct. The tool is a proposal that structures questions. It is not a compliance determination.
