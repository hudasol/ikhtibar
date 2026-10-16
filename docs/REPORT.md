# Ikhtibar: Testing AI Systems Before Deployment. Required, Recommended, or Merely Described?

**A comparative evidence review, with a gap analysis for UAE public sector deployment**

Prepared for Huda Mueen. Version 3.0 (phase 3), 16 October 2026. Rows carry their own retrieval and check dates: phase 1 and 2 rows were retrieved on 11 or 12 October 2026, and phase 3 checks and new rows are dated 16 October 2026. This file is generated from the data files by `python -m ikhtibar.build_docs`; do not edit it by hand.

**This is research analysis, not legal advice.** It has not been peer reviewed. It was produced with AI research subagents and independent AI verification passes in three phases (Appendix A); phase 3 re-checked every row that phase 2 had left open, re-checked the status of time sensitive items, added new rows, and ran a fresh independent verification sample. Statements about what a document says trace to a row in `data/evidence_table.csv`. Statements that are interpretation appear in paragraphs marked **Interpretation**. A dagger (†) after a row identifier means the row is excluded from every headline count: it could not be verified (source blocked, passage not located, or source not read), or it rests on a portal summary or a secondary report only.

---

## 0. How to read this report

- **Row IDs.** Every factual claim cites row IDs such as `EU-AI-Act-018` or `UAE-AbuDhabi-DoH-003`. Each row holds the clause or page, a paraphrase, a binding status, who tests, the source URL, the retrieval date and a verification status.
- **Documented versus interpreted.** Where the text separates what a document states from what the analyst makes of it, the first is labelled **Source says** and the second **Interpretation**.
- **Counts are counts of extracted provisions.** A long guidance document yields many rows; a short statute yields few. Section 5.4 explains why raw counts must not be read as league tables.
- **Headline counts exclude unverified rows.** 94 of 522 rows are excluded (unverified, unverifiable, or resting on a portal summary or secondary report only). If the 65 excluded test rows were counted, the split would be 93 mandatory or conditional (30%), 180 voluntary or guidance (58%) and 38 ambiguous (12%) of 311.
- **Absence is not evidence of absence.** "Not found in the public sources searched" means exactly that. It does not mean a UAE or Gulf requirement does not exist.
- **No claim about what the UAE requires is made unless a retrieved source says so.** Where a source's own binding force is unclear, the row is coded ambiguous.

---

## 1. Headline findings

1. **Most testing content in the evidence base is not binding.** Of 246 headline test provisions, 73 (30%) are mandatory or conditional, 154 (63%) are voluntary or guidance, and 19 (8%) are ambiguous. The binding rows come from: EU AI Act (as amended 2026), Art 50 code, Reg 2026/1755 (26), Abu Dhabi DoH (health sector: Standard and Protocol) (11), China (GenAI, algorithm, labelling, GB/T 45654, TC260 guide) (10), DIFC and ADGM (Reg 10, Framework, 2026 draft amendments, DP guidance) (8), Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies) (7), UAE federal (Charter, Strategy, Guidelines, Ethics, CSC AI security policy, PDPL) (4), US OMB M-25-21 and M-26-04 (3), South Korea AI Basic Act and Enforcement Decree (3), UK (Playbook, ATRS, DSIT, AISI) (1). Phase 2 had removed most EU Act rows because the fetch tool truncated EUR-Lex; phase 3 read the consolidated Act through the EU Publications Office and restored them, which is the main reason the binding share rose. Canada's Directive is still unreadable by the fetch tool and none of its rows is counted.
2. **Where testing is binding, the text mostly requires that it happens and is documented, not how.** The EU Act requires testing of high risk systems against metrics and thresholds the provider defines (`EU-AI-Act-016`, `EU-AI-Act-018`). OMB M-25-21 requires pre deployment testing plans for high impact AI (`US-OMB-003`). The Abu Dhabi DoH Standard requires validation against "established performance benchmarks" and does not name them (`UAE-AbuDhabi-DoH-003`). The first harmonised standard cited under the EU Act, on 14 October 2026, is the quality management standard EN 18286 (`EU-Standards-P3-20`†), not a testing method standard.
3. **Independent testing is binding in a few places.** Under the EU Act a notified body assesses biometric high risk systems where harmonised standards were not fully applied, and is an option otherwise (`EU-AI-Act-040`), while most Annex III systems follow internal control (`EU-AI-Act-041`), and the AI Office may evaluate general purpose models with systemic risk and require access to them (`EU-AI-Act-071`, `EU-AI-Act-P3-20`†). In the UAE sources, the Dubai Health Authority AI in Healthcare Policy requires independent third party validation and audits (`UAE-Dubai-025`, `UAE-Dubai-026`), DIFC Regulation 10 makes certification a precondition for commercial high risk processing (`UAE-DIFC-ADGM-004`, `UAE-DIFC-ADGM-018`), and the DoH Standard provides for DoH audits (`UAE-AbuDhabi-DoH-013`). Independent pre release evaluation of frontier models by the UK AI Security Institute remains voluntary (`UK-024`).
4. **Binding red teaming is narrow.** There are 24 headline red teaming and dangerous capability rows and 3 of them are mandatory or conditional: `EU-AI-Act-063`, `EU-AI-Act-068`, `EU-AI-Act-071`. Binding red teaming rows that are not counted (unverified or awaiting check): `EU-AI-Act-P3-20`†, `UAE-Federal-P3-04`†.
5. **Human oversight is specified as design, not as something to test.** Headline rows with human oversight validation as primary test type: 1 (`UAE-DIFC-ADGM-015` (guidance)). Oversight design duties appear as enabling provisions (`EU-AI-Act-026`, `UAE-Federal-008`).
6. **In the UAE, one cross sector instrument binding government entities was found, and it is about AI security.** The UAE National Cyber Security Policy for AI, version 1.1 (Cyber Security Council), states in "shall" form that entities test and validate AI systems, develop and test them securely, and test them regularly, and it names federal ministries and authorities, emirate government entities and critical infrastructure entities as addressees (`UAE-Federal-P3-01`†, `UAE-Federal-P3-03`†, `UAE-Federal-P3-04`†, `UAE-Federal-P3-08`†). Its wording that systems be rigorously tested *before deployment* is in the implementation guidance, phrased "should" (`UAE-Federal-P3-02`†). Phase 2 had only the portal summary and coded this policy ambiguous. Other binding UAE testing text remains sector or zone specific: Abu Dhabi health (`UAE-AbuDhabi-DoH-003` to `UAE-AbuDhabi-DoH-013`), Dubai health (`UAE-Dubai-025` to `UAE-Dubai-029`), DIFC Regulation 10, and Dubai government information security, which is not AI specific (`UAE-Dubai-033` to `UAE-Dubai-035`). The federal personal data law excludes government entities (`UAE-Federal-034`). No Abu Dhabi government wide AI policy was found in public sources.
7. **Required, recommended and described.** Among the non binding test rows, two independent coders separated text with obligation wording, recommendations and descriptions of practice (Section 5.5). Of 173 such headline rows, 120 recommend a test, 36 only describe testing practice, 8 use obligation wording in a document that is not binding or whose force is unclear, and 9 were disputed between the coders (agreement 95.4%, Cohen's kappa 0.9).
8. **Verification.** In phase 3, separate verifier subagents checked a fresh random sample of 30 rows (seed 20261016) and all 56 new rows. In the fresh sample, 0 of 0 verifiable rows had an error (None%, 95% interval 0.0% to 0.0%); among new rows, 0 of 0 (None%). The research agents' own re-check of the 175 rows phase 2 had left open found 1 errors as they graded them; applying the rubric strictly (a wrong status, date or version, or an overstated paraphrase is an error) gives 15 errors in 142 verifiable rows (10.6%). Phase 2 reported 13 errors in 293 (4.4%). All errors found were corrected. See Appendix A.
9. **What changed since 12 October 2026.** The amended EU application dates are now confirmed in operative text (Article 113, third paragraph, point (c)(i) and (ii)); the first harmonised standard was cited on 14 October 2026; Japan's Digital Agency guideline on generative AI in government (DS-920 v2.0, in force 1 September 2026) asks ministries to test inputs and outputs before release (`Japan-P3-01`†); Singapore announced an AI tester accreditation programme; the DIFC consulted on adding a pre-use safety verification test to Regulation 10 (`UAE-DIFC-ADGM-P3-01`†, not enacted). Section 7 lists every status item.

---

## 2. Method

The full protocol is in `docs/PROTOCOL.md`.

### 2.1 Inclusion, coding and statuses

- **Inclusion.** Primary documents from governments, national institutes and standards bodies, retrieved and read, containing at least one provision on testing, evaluation, assessment, validation, conformity, red teaming, audit or verification of an AI system before or at deployment. Secondary sources (law firm notes, news) were used only to locate primary sources.
- **Binding status.** Five values. **Mandatory**: legally binding on the stated actor, with the testing or assessment duty in operative text. **Conditional**: binding only if a trigger applies (risk classification, impact level, compute threshold, scope, commercial use). **Voluntary**: a formal scheme or standard an organisation may adopt. **Guidance**: a recommendation or description of practice. **Ambiguous**: the document's own language conflicts, or its status could not be settled.
- **Row types.** Each row is a `test` (a provision calling for, or describing as practice, an evaluation that produces evidence), an `enabler` (documentation, logging, registration or disclosure that supports tests) or `context` (dates, scope, penalties, status). Of 522 rows, 311 are test rows, 122 are enablers and 89 are context. Headline tables use test rows that are not unverified (246 rows; 65 excluded).
- **Coding.** Test type, secondary type and stage were assigned by AI coding subagents from the taxonomy in Section 4. This coding is judgemental. One test type (content safety) emerged during coding. In phase 2 one coding error was found and corrected (`UAE-Dubai-036`, a vehicle inspection, moved from content safety to conformity).
- **Translation.** Official English versions were preferred. The row column `language_read` records, per row, whether an original or a translation was read, and whether a translation was official, unofficial or produced by the fetch tool.

### 2.2 Phase 2 verification design

1. **Access rule.** Only the standard fetch and search tools were used. If a site rejected a fetch it was retried once and then stopped. No user agent change, cache, mirror, archive, translation proxy or third party copy was used. Such rows are marked `UNVERIFIED_BLOCKED` with the exact document to download in `docs/DOWNLOAD_LIST.md`. A permission timeout is recorded separately (`block_type` = `permission_timeout`) because it is not a site block; the URL can be approved and retried.
2. **Coverage.** All rows cited in the phase 1 report prose, brief and checklist were checked again; a fresh seeded random sample (seed 20261012) of 64 other rows was checked by different subagents; targeted rows, the provisional rows, all new UAE rows and all DIFC rows were checked. Rows from sample types are separated in Appendix A.
3. **Not rechecked.** 0 rows were not in any phase 2 sample. They keep their phase 1 status and are included in headline counts; they are flagged `NOT_RECHECKED` in the table.
4. **Verdict handling.** MINOR means a small imprecision. A date only MINOR (for example a retrieval date) is reported as PASS in the adjusted column; the raw verdict is retained. Errors were corrected in the table through `data/patches.json`, each patch with a source and reason.
5. **Rule for report prose.** The report is generated. Any cited row that is unverified gets a dagger. A test fails the build if a row cited in this report does not exist.

### 2.3 Phase 1 provisional rows

Phase 1 verification used a browser style user agent for some downloads, and a research subagent used one for the JTC 21 feed and used the Publications Office copy when EUR-Lex challenged it. Those verdicts were treated as provisional. The affected sets were: the Phase 1 verification sample A (20 rows from EU, Canada, Singapore, Saudi NCA and DIFC sources), the JTC 21 rows, one UK parliament row, rows whose source host was digitaldubai.ae, and Saudi OCR rows. 49 rows carry the `phase1_provisional` flag. They were re verified with the standard tools only. Result: 17 PASS, 10 MINOR, 4 ERROR, 12 blocked and 6 unverifiable (31 verifiable).

| Final status | Rows | Row identifiers |
|---|---|---|
| VERIFIED | 25 | `China-013`, `EU-AI-Act-028`, `EU-AI-Act-032`, `EU-AI-Act-034`, `EU-AI-Act-038`, `EU-AI-Act-044`, `EU-AI-Act-068`, `EU-Standards-002`, `EU-Standards-003`, `EU-Standards-004`, `EU-Standards-006`, `EU-Standards-008`, `ISO-IEC-009`, `ISO-IEC-015`, `ISO-IEC-017`, `Saudi-019`, `Saudi-020`, `Saudi-021`, `Saudi-023`, `Singapore-014`, `UAE-AbuDhabi-DoH-008`, `UAE-DIFC-ADGM-002`, `UAE-DIFC-ADGM-008`, `UAE-Dubai-006`, `US-NIST-005` |
| VERIFIED_CORRECTED | 18 | `EU-AI-Act-031`, `EU-Standards-005`, `Japan-016`, `Saudi-008`, `Saudi-018`, `Saudi-022`, `Singapore-002`, `Singapore-033`, `UAE-Dubai-001`, `UAE-Dubai-002`, `UAE-Dubai-003`, `UAE-Dubai-004`, `UAE-Dubai-005`, `UAE-Dubai-007`, `UAE-Dubai-008`, `UAE-Dubai-009`, `UK-009`, `UK-032` |
| UNVERIFIED_BLOCKED | 6 | `Canada-002`†, `Canada-008`†, `Canada-009`†, `Canada-014`†, `Canada-020`†, `Canada-021`† |

### 2.4 Phase 3 design (16 October 2026)

1. **Re-check of open rows.** Every row that phase 2 left blocked, unreadable, unread, withdrawn or not rechecked (175 rows) went to one of six family research agents, which checked it against the primary source and proposed corrections. A seventh agent searched UAE federal, Abu Dhabi and Dubai sources for instruments missing from the table. Each agent also re-checked the status of time sensitive items in its families (Section 7).
2. **Access.** The phase 2 access rule was kept: only the standard fetch and search tools, one retry after a site block, no user agent change, cache, mirror or third party copy. Two clarifications. First, the fetch tool can now read long documents in segments; that is the standard tool, so rows that phase 2 lost to truncation were retried. Second, when the fetch tool fetched a PDF it could not render, it saved the file, and agents extracted text from that saved file locally, or rendered image-only pages and read them. No second download took place. These rows carry `access_path` = `standard_fetch_saved_pdf_local_text` or `standard_fetch_saved_pdf_page_image`, listed in `data/verification/phase3/access_relabel.csv`. Phase 1 treated OCR as provisional; phase 3 discloses the method row by row instead, and the reader can exclude these rows. EU texts were read on the EU Publications Office endpoint because EUR-Lex returned empty pages (`access_path` = `alt_official_endpoint`).
3. **Re-grading.** The research agents graded 14 findings as MINOR that the rubric classes as errors (a wrong binding status, a wrong date or document version, a paraphrase that overstated scope or turned "must" into "should", an unsupported actor). The lead analyst re-graded them to ERROR; the agents' grades are kept in `data/verification/phase3/verdict_reclass.csv`, and both figures are reported.
4. **Corrections.** Proposed corrections were read and applied through `data/verification/phase3/patches_p3_agents.json`; lead analyst corrections are in `patches_p3_manual.json`. Four UAE rows based on a portal summary were marked `SUPERSEDED` because the full policy was read and coded in new rows; they are excluded from counts so the policy is not counted twice.
5. **New rows.** 56 rows were added. Their identifiers contain `P3`. They were coded by the agent that found them, which is a proposal, and then checked by separate verifiers.
6. **Final independent check.** After corrections, four verifier subagents that had not taken part in the research, and that were told not to open any working file, checked a fresh random sample of 30 rows (seed 20261016, drawn from rows with a readable source) and all new rows. Errors they found were corrected. Rows still awaiting a check are excluded from counts (`NEW_UNCHECKED`).
7. **Normative force coding.** Two coders independently classified non binding test rows as obligation wording, recommendation or description (Section 5.5, `data/coding/`).

---

## 3. Evidence base

| Family | Rows | Headline test rows | Primary text read | Catalogue only | Unofficial or machine translation | Unverified or unverifiable |
|---|---|---|---|---|---|---|
| EU AI Act (as amended 2026), Art 50 code, Reg 2026/1755 | 78 | 28 | 78 | 0 | 0 | 4 |
| EU GPAI Code of Practice | 13 | 7 | 13 | 0 | 0 | 4 |
| EU harmonised standards (JTC 21, EN 18286 citation) | 9 | 1 | 9 | 0 | 0 | 1 |
| ISO/IEC (catalogue level) | 19 | 12 | 0 | 19 | 0 | 1 |
| NIST (AI RMF, Playbook, 600-1, 800-2 draft) | 46 | 36 | 46 | 0 | 0 | 0 |
| US OMB M-25-21 and M-26-04 | 9 | 3 | 9 | 0 | 0 | 2 |
| UK (Playbook, ATRS, DSIT, AISI) | 36 | 19 | 36 | 0 | 0 | 3 |
| Canada Directive on Automated Decision-Making | 24 | 0 | 24 | 0 | 0 | 24 |
| Singapore (AI Verify, Starter Kit, frameworks) | 38 | 31 | 38 | 0 | 0 | 2 |
| Japan (Act, plan, guidelines, Digital Agency DS-920, AISI) | 28 | 13 | 28 | 0 | 0 | 4 |
| South Korea AI Basic Act and Enforcement Decree | 19 | 5 | 16 | 0 | 3 | 2 |
| China (GenAI, algorithm, labelling, GB/T 45654, TC260 guide) | 33 | 15 | 13 | 1 | 18 | 3 |
| UAE federal (Charter, Strategy, Guidelines, Ethics, CSC AI security policy, PDPL) | 42 | 15 | 39 | 3 | 0 | 12 |
| DIFC and ADGM (Reg 10, Framework, 2026 draft amendments, DP guidance) | 29 | 13 | 29 | 0 | 0 | 4 |
| Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies) | 40 | 20 | 39 | 0 | 0 | 1 |
| Abu Dhabi DoH (health sector: Standard and Protocol) | 18 | 13 | 18 | 0 | 0 | 4 |
| Abu Dhabi AI and Advanced Technology Council law | 2 | 0 | 2 | 0 | 0 | 0 |
| Saudi Arabia (SDAIA, NCA draft, SFDA) | 39 | 15 | 38 | 0 | 0 | 23 |
| **Total** | **522** | **246** | **475** | **23** | **21** | **94** |

**Source says (about access).** Rows stay unverified where the issuing site rejected the standard fetch tool on 16 October 2026 as well: the Treasury Board of Canada Secretariat (all Canada rows), iso.org catalogue pages, sdaia.gov.sa, and, for leads not yet in the table, the Saudi laws portal, the UAE central bank rulebook, the DFSA, ai.gov.ae and the UK bills site. Two files exceeded the fetch tool's size limit (China's AI Safety Governance Framework 2.0 and the UAE National AI Strategy PDF at its new address). The phase 2 problem of EUR-Lex truncation is resolved. Block types among excluded rows: none: 61, site_rejected: 32, truncated_or_unreadable: 1.

| Family | Rows | Blocked | Readable but passage not located | Source not read or withdrawn | Other (superseded, portal or secondary only, awaiting check) |
|---|---|---|---|---|---|
| EU AI Act (as amended 2026), Art 50 code, Reg 2026/1755 | 4 | 0 | 0 | 0 | 4 |
| EU GPAI Code of Practice | 4 | 0 | 0 | 0 | 4 |
| EU harmonised standards (JTC 21, EN 18286 citation) | 1 | 0 | 0 | 0 | 1 |
| ISO/IEC (catalogue level) | 1 | 1 | 0 | 0 | 0 |
| US OMB M-25-21 and M-26-04 | 2 | 0 | 0 | 0 | 2 |
| UK (Playbook, ATRS, DSIT, AISI) | 3 | 0 | 0 | 0 | 3 |
| Canada Directive on Automated Decision-Making | 24 | 24 | 0 | 0 | 0 |
| Singapore (AI Verify, Starter Kit, frameworks) | 2 | 0 | 0 | 0 | 2 |
| Japan (Act, plan, guidelines, Digital Agency DS-920, AISI) | 4 | 0 | 0 | 0 | 4 |
| South Korea AI Basic Act and Enforcement Decree | 2 | 0 | 0 | 0 | 2 |
| China (GenAI, algorithm, labelling, GB/T 45654, TC260 guide) | 3 | 0 | 1 | 0 | 2 |
| UAE federal (Charter, Strategy, Guidelines, Ethics, CSC AI security policy, PDPL) | 12 | 0 | 0 | 0 | 12 |
| DIFC and ADGM (Reg 10, Framework, 2026 draft amendments, DP guidance) | 4 | 0 | 0 | 0 | 4 |
| Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies) | 1 | 0 | 0 | 0 | 1 |
| Abu Dhabi DoH (health sector: Standard and Protocol) | 4 | 0 | 0 | 0 | 4 |
| Saudi Arabia (SDAIA, NCA draft, SFDA) | 23 | 7 | 0 | 0 | 16 |

---

## 4. Taxonomy of test types

The taxonomy was built bottom up. The first extraction pass produced a free text "what is tested" label for every row. These were grouped into fourteen families and a fifteenth was added when three rows (China's GB/T 45654 output safety and refusal rate tests) fitted none. Three further candidate categories were raised and not adopted (evaluation tooling, assurance ecosystem, reporting of test results); they appear under boundary cases.

| Code | Test type | Definition | Examples |
|---|---|---|---|
| PERF | Performance and validity evaluation | Measuring whether the system does its task, with what accuracy, on what data, and whether the test itself is valid. | `EU-AI-Act-016`, `UAE-AbuDhabi-DoH-003`, `US-OMB-003`, `US-NIST-009`, `Singapore-005` |
| ROB | Robustness, reliability and fault testing | Behaviour under perturbed inputs, outliers, faults, repeated runs; fail safe behaviour. | `EU-AI-Act-029`, `UAE-AbuDhabi-DoH-005`, `UAE-Federal-023`, `ISO-IEC-009` |
| FAIR | Fairness, bias and representativeness testing | Unequal performance across groups; representativeness of data and test sets. | `UAE-AbuDhabi-DoH-008`, `UAE-Dubai-001`, `UAE-Federal-018`, `Singapore-019` |
| SEC | Security and adversarial resilience testing | Security assessment, code review, vulnerability scanning, penetration testing, AI specific attacks. | `UAE-AbuDhabi-DoH-007`, `EU-AI-Act-030`, `UAE-Federal-007` |
| RED | Red teaming and dangerous capability evaluation | Adversarial probing for misuse; evaluation of dangerous capabilities; systemic risk model evaluation. | `UK-024`, `UK-031`, `Japan-020`, `US-NIST-028`, `Singapore-007`, `ISO-IEC-015` |
| CSAFE | Content safety evaluation | Harmful output rates, refusal and over refusal against question banks. | `China-024`, `China-025` |
| PRIV | Privacy and data protection assessment or testing | Privacy leakage and re identification testing; data protection impact assessment. | `UAE-Federal-005`, `UAE-DIFC-ADGM-006`, `US-NIST-033` |
| TRANS | Transparency, explainability, labelling and reproducibility | Explainability tests; checks that labels and disclosures work; reproducibility. | `China-017`, `Singapore-021`, `Singapore-022` |
| OVER | Human oversight and operational control validation | Testing that override, human review and escalation work. | `UAE-DIFC-ADGM-015` (test); enablers: `EU-AI-Act-026`, `UAE-Federal-008` |
| RISK | Risk, impact and compliance assessment | Structured assessment of risks, impacts on rights or groups, legal compliance. | `EU-AI-Act-014`, `UAE-AbuDhabi-DoH-009`, `UAE-DIFC-ADGM-020` |
| DATA | Data and training corpus quality validation | Data relevance, accuracy, lawfulness, provenance, quality. | `EU-AI-Act-020`, `China-002` |
| CONF | Conformity assessment, independent review, audit, certification, filing | Assessment against a standard by provider or third party; certification; security assessment and filing with a regulator. | `EU-AI-Act-032`, `China-005`, `UAE-Dubai-025`, `UAE-DIFC-ADGM-018`, `UAE-AbuDhabi-DoH-010` |
| REAL | Real world, sandbox and pilot testing | Controlled live trials, regulatory sandboxes, pilots. | `EU-AI-Act-017`, `EU-AI-Act-055`, `UAE-Dubai-009`, `Singapore-033` |
| MON | Post deployment monitoring and re assessment | Performance and outcome monitoring, incident handling, re testing triggers. | `US-OMB-006`, `UAE-Dubai-028`, `UAE-Federal-011` |
| GATE | Acceptance criteria and release decision | Pre set thresholds, go or no go decisions, approval authority by risk level. | `EU-AI-Act-018`, `UAE-AbuDhabi-DoH-011`, `UAE-Federal-009`, `Singapore-009` |

**Boundary cases.**

- *Enablers take the code of the test they support.* A documentation duty about validation results is coded PERF with row type `enabler`.
- *Evaluation tooling* (for example UK Inspect, NIST AI 800-2 draft) is coded under the test it supports.
- *Assurance ecosystem* rows (accreditation of third party assurers) are coded CONF as enablers.
- *Reporting of test results* is coded TRANS as an enabler.
- *Risk assessment versus testing.* Impact assessments are not tests of behaviour; they are included because many frameworks treat them as the trigger and scope setter for testing.
- *RED versus PERF and CSAFE.* Misuse probing is RED; harmful output and refusal rates against fixed banks are CSAFE; ordinary accuracy is PERF.

---

## 5. Comparative analysis

### 5.1 By framework: required versus recommended

| Family | Headline test rows | M | C | V | G | A | Binding where triggered (M+C) | Test rows excluded as unverified |
|---|---|---|---|---|---|---|---|---|
| EU AI Act (as amended 2026), Art 50 code, Reg 2026/1755 | 28 | 0 | 26 | 2 | 0 | 0 | 26 of 28 | 3 |
| EU GPAI Code of Practice | 7 | 0 | 0 | 7 | 0 | 0 | 0 of 7 | 2 |
| EU harmonised standards (JTC 21, EN 18286 citation) | 1 | 0 | 0 | 1 | 0 | 0 | 0 of 1 | 0 |
| ISO/IEC (catalogue level) | 12 | 0 | 0 | 1 | 11 | 0 | 0 of 12 | 0 |
| NIST (AI RMF, Playbook, 600-1, 800-2 draft) | 36 | 0 | 0 | 1 | 35 | 0 | 0 of 36 | 0 |
| US OMB M-25-21 and M-26-04 | 3 | 0 | 3 | 0 | 0 | 0 | 3 of 3 | 0 |
| UK (Playbook, ATRS, DSIT, AISI) | 19 | 0 | 1 | 5 | 9 | 4 | 1 of 19 | 3 |
| Canada Directive on Automated Decision-Making | 0 | 0 | 0 | 0 | 0 | 0 | 0 of 0 | 12 |
| Singapore (AI Verify, Starter Kit, frameworks) | 31 | 0 | 0 | 12 | 18 | 1 | 0 of 31 | 2 |
| Japan (Act, plan, guidelines, Digital Agency DS-920, AISI) | 13 | 0 | 0 | 0 | 13 | 0 | 0 of 13 | 2 |
| South Korea AI Basic Act and Enforcement Decree | 5 | 0 | 3 | 2 | 0 | 0 | 3 of 5 | 1 |
| China (GenAI, algorithm, labelling, GB/T 45654, TC260 guide) | 15 | 5 | 5 | 5 | 0 | 0 | 10 of 15 | 2 |
| UAE federal (Charter, Strategy, Guidelines, Ethics, CSC AI security policy, PDPL) | 15 | 1 | 3 | 0 | 10 | 1 | 4 of 15 | 9 |
| DIFC and ADGM (Reg 10, Framework, 2026 draft amendments, DP guidance) | 13 | 0 | 8 | 0 | 4 | 1 | 8 of 13 | 3 |
| Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies) | 20 | 5 | 2 | 1 | 11 | 1 | 7 of 20 | 0 |
| Abu Dhabi DoH (health sector: Standard and Protocol) | 13 | 8 | 3 | 0 | 0 | 2 | 11 of 13 | 4 |
| Saudi Arabia (SDAIA, NCA draft, SFDA) | 15 | 0 | 0 | 0 | 6 | 9 | 0 of 15 | 22 |
| **All** | **246** | **19** | **54** | **37** | **117** | **19** | **73 of 246** | **65** |

**Source says (selected, verified rows).**

- **EU AI Act.** High risk systems must be tested to find the most appropriate risk management measures and to ensure consistent performance (`EU-AI-Act-016`), at appropriate points in development and in any event before placing on the market, against pre defined metrics and probabilistic thresholds (`EU-AI-Act-018`). Accuracy, robustness and cybersecurity are required (`EU-AI-Act-028`, `EU-AI-Act-029`, `EU-AI-Act-030`). Testing procedures may include real world testing (`EU-AI-Act-017`, `EU-AI-Act-055`). Public bodies deploying certain Annex III systems must assess fundamental rights impact before first use (`EU-AI-Act-036`). Conformity assessment is by internal control for most Annex III systems and may involve a notified body for biometrics (`EU-AI-Act-040`, `EU-AI-Act-041`). Providers of general purpose models with systemic risk must evaluate their models, including adversarial testing (`EU-AI-Act-068`), and the AI Office may evaluate models and require access (`EU-AI-Act-071`, `EU-AI-Act-P3-20`†). The amended dates are confirmed in operative text: Chapter III Sections 1 to 3 apply from 2 December 2027 for Annex III systems and 2 August 2028 for Annex I systems (`EU-AI-Act-001`, `EU-AI-Act-002`).
- **EU codes and standards.** The General Purpose AI Code of Practice describes itself as a voluntary tool for showing compliance with binding duties, adherence to which is not conclusive evidence of compliance (`EU-GPAI-CoP-001`); the Commission's adequacy opinion is recorded in Section 7. The Code asks signatories to give external evaluators access and to file a model report before market placement (`EU-GPAI-CoP-P3-20`†, `EU-GPAI-CoP-P3-23`†). A separate code under Article 50 asks for pre market testing of content marking and detection (`EU-AI-Act-P3-22`†). The only harmonised standard cited in the Official Journal so far is EN 18286 on quality management (`EU-Standards-P3-20`†); risk management, trustworthiness, cybersecurity and conformity assessment standards are still drafts.
- **Canada.** No Canadian row is in the headline counts. The Treasury Board site rejected the standard fetch again in phase 3, and no official copy was found on another Government of Canada host, so 24 of the 24 Canada rows are unverified. The Directive text and the phase 1 rows remain in the table for reference and are marked †.
- **United States.** NIST AI RMF 1.0, its Generative AI Profile and the AI 800-2 draft are not binding (NIST says the RMF is being revised; no revision was released). OMB M-25-21 binds federal agencies for high impact AI: pre deployment testing (`US-OMB-003`), an impact assessment (`US-OMB-004`) and ongoing monitoring (`US-OMB-006`). OMB M-26-04 (December 2025) requires agencies buying large language models to request model, system and data cards with evaluation information (`US-OMB-P3-01`†) and lets them ask for bias evaluation and red teaming results (`US-OMB-P3-02`†).
- **United Kingdom.** No statutory pre deployment testing duty was found, and no government AI bill was announced in the May 2026 King's Speech. The AI Playbook is guidance and uses "must" in places (`UK-004`, `UK-011`). The Algorithmic Transparency Recording Standard is mandatory for in scope central government bodies (`UK-014`, `UK-015`) and asks for evaluation to be recorded rather than performed (`UK-018`, `UK-019`). AI Security Institute pre deployment evaluation is voluntary (`UK-024`).
- **Singapore.** AI Verify, the Starter Kit for testing LLM applications and the generative and agentic frameworks are voluntary or guidance; no public instrument was found that makes them binding on public agencies. The agentic framework describes Singapore government agencies testing agents before rollout (`Singapore-035`, `Singapore-P3-01`†). An AI tester accreditation programme and a starter kit for testing agentic systems were announced in 2026 (Section 7; the kit's text was not read).
- **Japan.** The AI Promotion Act and the business guidelines contain no testing mandate. The Digital Agency guideline on generative AI in government (DS-920 v2.0, marked normative, in force 1 September 2026) asks ministries to create test scenarios and test inputs and outputs before release (`Japan-P3-01`†); the English translation says "should" while the Japanese uses a declarative form, which the row flags. The Japan AI Safety Institute's red teaming guide is guidance (`Japan-020`).
- **South Korea.** The AI Basic Act imposes safety duties above a compute threshold set by decree (`Korea-005`, `Korea-013`) and duties on high impact AI (`Korea-007`, `Korea-014`); impact assessment may be done by the operator or a third party (`Korea-P3-01`†). The decree was read in the reference English translation. MSIT announced a grace period of at least one year for fines (`Korea-016`).
- **China.** Generative AI providers must sample check annotation quality (`China-003`) and review algorithms (`China-009`); labelling is mandatory (`China-017`) and the labelling standard GB 45438 is listed as mandatory (`China-031`, catalogue level). GB/T 45654-2025 supplies concrete test banks but is a recommended standard (`China-024`, `China-025`). A September 2026 TC260 practice guide describes verification and validation testing and deployment checks (`China-P3-01`†, `China-P3-02`†).
- **ISO/IEC.** Entries are catalogue level only (`ISO-IEC-009`, `ISO-IEC-015`); iso.org rejected the fetch tool in phase 3, so no status was re-checked.
- **UAE and Gulf.** See Section 6.

**Interpretation.** Binding (mandatory or conditional) test rows are concentrated in a few families. The frameworks with the most detailed testing guidance (NIST, Singapore, Japan, ISO) are not binding. The binding regimes are more compact and leave method to the regulated party. The headline split is also sensitive to what could be verified: removing blocked sources removed two regimes (Canada and most of the EU conformity chapter) that phase 1 counted as binding.

### 5.2 By test type

| Code | Test type | Headline test rows | M | C | V | G | A | Families with M or C rows |
|---|---|---|---|---|---|---|---|---|
| PERF | Performance and validity | 54 | 2 | 4 | 3 | 42 | 3 | EU-AI-Act, UAE-AbuDhabi-DoH, US-OMB |
| ROB | Robustness and reliability | 16 | 1 | 1 | 2 | 9 | 3 | EU-AI-Act, UAE-AbuDhabi-DoH |
| FAIR | Fairness and representativeness | 16 | 1 | 2 | 2 | 10 | 1 | UAE-AbuDhabi-DoH, UAE-DIFC-ADGM |
| SEC | Security and adversarial resilience | 13 | 2 | 1 | 3 | 6 | 1 | EU-AI-Act, UAE-AbuDhabi-DoH, UAE-Federal |
| RED | Red teaming and dangerous capability evaluation | 24 | 0 | 3 | 7 | 14 | 0 | EU-AI-Act |
| CSAFE | Content safety evaluation | 2 | 0 | 0 | 2 | 0 | 0 | none |
| PRIV | Privacy and data protection assessment | 10 | 0 | 5 | 0 | 4 | 1 | UAE-DIFC-ADGM, UAE-Federal, UK |
| TRANS | Transparency, explainability and reproducibility | 4 | 1 | 0 | 2 | 1 | 0 | China |
| OVER | Human oversight validation | 1 | 0 | 0 | 0 | 1 | 0 | none |
| RISK | Risk, impact and compliance assessment | 32 | 3 | 11 | 6 | 8 | 4 | China, EU-AI-Act, Korea, UAE-AbuDhabi-DoH, UAE-DIFC-ADGM, US-OMB |
| DATA | Data quality validation | 5 | 2 | 1 | 2 | 0 | 0 | China, EU-AI-Act |
| CONF | Conformity assessment, independent review, certification | 33 | 5 | 16 | 2 | 5 | 5 | China, EU-AI-Act, UAE-AbuDhabi-DoH, UAE-DIFC-ADGM, UAE-Dubai |
| REAL | Real world, sandbox and pilot testing | 6 | 0 | 1 | 2 | 3 | 0 | EU-AI-Act |
| MON | Post deployment monitoring and re assessment | 15 | 2 | 4 | 1 | 8 | 0 | China, EU-AI-Act, UAE-Dubai, UAE-Federal, US-OMB |
| GATE | Acceptance criteria and release decision | 15 | 0 | 5 | 3 | 6 | 1 | EU-AI-Act, UAE-AbuDhabi-DoH, UAE-DIFC-ADGM, UAE-Dubai |

**Interpretation.**

- *Performance, risk assessment and conformity or review* tend to carry the most binding rows, because binding regimes commonly require "test it, assess the risk, and document the review".
- *Red teaming (RED)* has 3 binding headline rows of 24.
- *Human oversight validation (OVER)* has 1 headline test row(s): `UAE-DIFC-ADGM-015` (guidance). None of the retrieved provisions requires evidence that oversight works under realistic conditions.
- *Content safety (CSAFE)* has 2 headline rows, all from the Chinese standard.
- *Real world and sandbox testing (REAL)* has 6 headline rows.
- Test types with no headline row at all: none.

### 5.3 Coverage matrix

Cell notation: letter = highest unambiguous binding status among headline test rows in that cell (M mandatory, C conditional, V voluntary, G guidance); number = count of test rows; `+aN` = N additional ambiguous rows; `.` = no test row; `A` alone = only ambiguous rows.

| Family | PERF | ROB | FAIR | SEC | RED | CSAFE | PRIV | TRANS | OVER | RISK | DATA | CONF | REAL | MON | GATE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EU-AI-Act | C3 | C1 | . | C1 | C3 | . | . | . | . | C5 | C1 | C7 | C3 | C2 | C2 |
| EU-GPAI-CoP | V1 | . | . | V1 | V3 | . | . | . | . | V1 | . | . | . | . | V1 |
| EU-Standards | V1 | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| ISO-IEC | G6 | V4 | . | . | G1 | . | . | . | . | G1 | . | . | . | . | . |
| US-NIST | G16 | G2 | G2 | G2 | V7 | . | G1 | G1 | . | . | . | G2 | . | G1 | G2 |
| US-OMB | C1 | . | . | . | . | . | . | . | . | C1 | . | . | . | C1 | . |
| UK | G5+a2 | . | G1 | G2+a1 | V3 | . | C1 | . | . | V2 | . | G2+a1 | . | G2 | V1 |
| Singapore | V11+a1 | V2 | V2 | V1 | V2 | . | . | V2 | . | V2 | . | V1 | G2 | V3 | V3 |
| Japan | G3 | G1 | . | . | G4 | . | . | . | . | G4 | . | . | . | G1 | . |
| Korea | . | . | . | . | . | . | . | . | . | C4 | . | V1 | . | . | . |
| China | . | . | . | V1 | . | V2 | . | M1 | . | M1 | M4 | C5 | . | M1 | . |
| UAE-Federal | G1 | G1 | G3 | M2 | . | . | C3 | . | . | A1 | . | G1 | . | C2 | G1 |
| UAE-DIFC-ADGM | G1 | . | C2 | . | . | . | C4 | . | G1 | C1 | . | C3+a1 | . | . | C1 |
| UAE-Dubai | G3 | . | G4 | . | . | . | . | . | . | V3+a1 | . | M6 | G1 | M2 | C1 |
| UAE-AbuDhabi-DoH | M2 | M2+a1 | M1 | M1 | . | . | . | . | . | M3 | . | M3+a1 | . | . | C1 |
| Saudi | . | G3+a2 | A1 | G2 | G1 | . | A1 | . | . | G3+a2 | . | A2 | . | . | G2+a1 |

**Interpretation.** Read the matrix by columns as well as rows. The matrix records provisions extracted; a blank cell may be addressed by text outside the testing passages read. Raw counts reflect extraction effort and document length.

### 5.4 What "required" means: five distinctions

1. **Who is bound.** OMB M-25-21 binds US federal agencies (`US-OMB-001`); the EU Act binds providers and deployers, including some outside the Union (`EU-AI-Act-009`); the DoH Standard binds DoH licensed healthcare entities; the DHA policy binds DHA regulated healthcare; DIFC Regulation 10 binds deployers and operators in DIFC. A "mandatory" row therefore means something different in each.
2. **What triggers the duty.** EU duties depend on classification as high risk (`EU-AI-Act-011`); OMB's on "high impact" use (`US-OMB-002`); Korea's on a compute threshold or high impact classification (`Korea-005`, `Korea-006`); DIFC's on high risk processing for commercial purposes (`UAE-DIFC-ADGM-004`). Most binding rows in the table are conditional on a trigger.
3. **Method versus outcome.** The Act requires testing against provider defined metrics (`EU-AI-Act-018`); the DoH Standard requires validation against benchmarks without naming them (`UAE-AbuDhabi-DoH-003`). **Interpretation:** binding regimes mostly standardise that a test is done and documented, leaving what counts as a pass to the regulated party, to standards or to later guidance.
4. **Who tests.** Most binding testing is by the provider or deployer. Independent assessment is binding on narrower routes: DHA third party validation and audits (`UAE-Dubai-025`, `UAE-Dubai-026`), DIFC accredited certification bodies (`UAE-DIFC-ADGM-018`, `UAE-DIFC-ADGM-022`), DoH audits (`UAE-AbuDhabi-DoH-013`). The status of the DIFC accreditation criteria is voluntary for a body that chooses to apply (`UAE-DIFC-ADGM-022`).
5. **Binding standards versus binding principles.** Several frameworks bind an obligation while pointing to non binding standards for method (`EU-AI-Act-037` is unverified; `EU-Standards-002` shows the relevant standards at draft or enquiry stages).

**Interpretation.** A statement such as "country X requires testing" is incomplete until it says: for whom, under what trigger, by whom, against what, and with what evidence.

### 5.5 Required, recommended or merely described

The binding status separates what is required (mandatory or conditional) from the rest. To separate the rest, two coder subagents independently classified each non binding test row by the force of its own wording: obligation wording (must or shall in a document that is not binding, or whose force is unclear), recommendation, or description of practice with no advice to act (codebook: `data/coding/CODEBOOK_normative_force.md`). They coded 216 rows from the paraphrases, agreed on 95.4% and reached a Cohen's kappa of 0.9. Disagreements are left as disputed rather than resolved by the analyst. The table counts headline rows only (0 non binding headline rows added after the coding are not coded).

| Family | Required (mandatory or conditional) | Obligation wording, not binding | Recommended | Described only | Disputed |
|---|---|---|---|---|---|
| EU AI Act (as amended 2026), Art 50 code, Reg 2026/1755 | 26 | 0 | 0 | 2 | 0 |
| EU GPAI Code of Practice | 0 | 0 | 7 | 0 | 0 |
| EU harmonised standards (JTC 21, EN 18286 citation) | 0 | 0 | 0 | 1 | 0 |
| ISO/IEC (catalogue level) | 0 | 0 | 0 | 12 | 0 |
| NIST (AI RMF, Playbook, 600-1, 800-2 draft) | 0 | 0 | 31 | 4 | 1 |
| UK (Playbook, ATRS, DSIT, AISI) | 1 | 2 | 12 | 4 | 0 |
| Singapore (AI Verify, Starter Kit, frameworks) | 0 | 0 | 27 | 3 | 1 |
| Japan (Act, plan, guidelines, Digital Agency DS-920, AISI) | 0 | 0 | 5 | 2 | 6 |
| South Korea AI Basic Act and Enforcement Decree | 3 | 0 | 2 | 0 | 0 |
| China (GenAI, algorithm, labelling, GB/T 45654, TC260 guide) | 10 | 0 | 5 | 0 | 0 |
| UAE federal (Charter, Strategy, Guidelines, Ethics, CSC AI security policy, PDPL) | 4 | 0 | 8 | 3 | 0 |
| DIFC and ADGM (Reg 10, Framework, 2026 draft amendments, DP guidance) | 8 | 2 | 2 | 0 | 1 |
| Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies) | 7 | 1 | 10 | 2 | 0 |
| Abu Dhabi DoH (health sector: Standard and Protocol) | 11 | 1 | 1 | 0 | 0 |
| Saudi Arabia (SDAIA, NCA draft, SFDA) | 0 | 2 | 10 | 3 | 0 |

**Interpretation.** Most non binding testing text recommends rather than describes. A small group uses obligation wording inside documents that do not say they bind anyone, or whose force is unclear: `UK-007`, `UK-011`, `UAE-Dubai-008`, `UAE-AbuDhabi-DoH-002`, `Saudi-001`, `Saudi-002`, `UAE-DIFC-ADGM-009`, `UAE-DIFC-ADGM-012`. For a UAE reader these rows matter most, because a document's "must" can be read as a requirement by an implementing team even when its legal force is unclear. Disputed rows: `US-NIST-020`, `Singapore-001`, `Japan-012`, `Japan-013`, `Japan-015`, `Japan-016`, `Japan-018`, `Japan-019`, `UAE-DIFC-ADGM-005`. The coders read paraphrases, not sources, and both are AI models of the same family, so the high agreement may overstate how reliable the classification is.

### 5.6 Source conflicts and status volatility

Conflicts are recorded in the `conflict_flag` column of the table. In summary:

- **EU timeline.** Commentary from before July 2026 shows 2 August 2026 for Annex III high risk requirements; the amended Article 113 sets 2 December 2027 (`EU-AI-Act-001`), as the Commission pages also say (`EU-AI-Act-005`). Resolved in phase 3 from operative text.
- **EU standards status.** On 12 October 2026 the JTC 21 feed listed EN 18286 as published with no Official Journal reference (`EU-Standards-002`); the reference was published on 14 October 2026 (`EU-Standards-P3-20`†). A Commission press release still calls the Article 50 guidelines a draft while the guidelines page shows them adopted (Section 7).
- **NIST.** NIST states that AI RMF 1.0 is being revised and AI 800-2 is an initial public draft. The NIST page for the Center for AI Standards and Innovation now carries a different name and refers to "SI" systems; no official notice of the change was found (`US-NIST-046`).
- **UK.** The AI Playbook uses "must" in guidance (`UK-004`, `UK-011`).
- **Singapore.** The Model AI Governance Framework for Generative AI cover says published 30 May 2024; the file name and PDF date say 19 June 2024 (`Singapore-028`).
- **Korea.** The reference English text of the decree renders the compute threshold exponent illegibly; MSIT English releases state 10^26 operations (`Korea-013`). A newer decree number appeared in August 2026 whose content could not be read (Section 7).
- **Japan.** The English translation of DS-920 uses "should" where the Japanese original is declarative (`Japan-P3-01`†).
- **UAE National Cyber Security Policy for AI.** The portal calls domain 4 "Operational Safety"; the PDF calls it "Operational Security" (`UAE-Federal-014`†).
- **DoH Standard and Protocol.** The Responsible AI Standard sends high risk systems to conformity assessment (`UAE-AbuDhabi-DoH-010`); the companion Risk Management Protocol says a system that stays high risk after controls must be avoided, and its own decision point routes only very high risk systems that way (`UAE-AbuDhabi-DoH-P3-03`†). The two documents also give different dates (June and July 2025) for the DoH AI Policy they cite, which was not found.
- **DIFC.** The consolidated cover says in force 1 September 2023; the official page says enacted on that date (`UAE-DIFC-ADGM-001`). A June 2026 consultation proposes renumbering Regulation 10.3.2 and changing the Autonomous Systems Officer role (`UAE-DIFC-ADGM-003`, `UAE-DIFC-ADGM-P3-04`†).
- **DHA.** The policy header carries inconsistent issue and effective dates, and its stated revision date of 1 July 2026 has passed, so a newer version may exist (`UAE-Dubai-025`, `UAE-Dubai-027`).
- **Dubai ethics guidelines.** The suspension of the external audit guideline appears in both the English v1.11 PDF and the Arabic edition (`UAE-Dubai-018`).
- **Saudi.** The NCA document's cover and Arabic pages say "Guidelines"; only the PDF file name says "Controls". The document states it is not mandatory (`Saudi-018`). The SDAIA Ethics Principles read are the first edition of September 2023; "2.0" appears only in secondary sources.

---

## 6. UAE and Gulf: what the retrieved sources say

This section reports what the sources retrieved say. It does not describe the whole of UAE or Gulf regulation. Section 6.2 lists what was searched, and `docs/UAE_COVERAGE.md` lists every source and search.

### 6.1 Instruments retrieved

| Instrument (as read) | Issuer and scope | Testing related content | Status as coded | Rows |
|---|---|---|---|---|
| UAE Charter for the Development and Use of AI | UAE federal | A safety principle; no test, assessment or audit method. | ambiguous | `UAE-Federal-001` |
| UAE National Strategy for AI 2031 | UAE federal | Pilots proposed to test governance frameworks; a planned UAI Seal with no criteria. | guidance | `UAE-Federal-002`, `UAE-Federal-003`, `UAE-Federal-030`, `UAE-Federal-031` |
| UAE Cabinet announcement, 23 April 2026 | UAE federal | Phased move of half of federal sectors and services to agentic AI, each phase tied to performance and impact assessments; no method. | ambiguous | `UAE-Federal-004` |
| UAE AI Adoption Guideline in Government Services (English and Arabic text) | UAE federal | Model evaluated against acceptance criteria before deployment; monitoring of deployed use cases; documentation of testing results; pilot gates. The text read does not state that it binds entities. | guidance | `UAE-Federal-009` to `UAE-Federal-013` |
| UAE AI Ethics Principles and Guidelines (December 2022) and Self Assessment Tool | UAE federal | Bias testing, discrimination impact assessment, quality checks, external audit for critical decisions, fallback testing, vulnerability assessment, privacy impact assessment. Phrased "should" or "could". | guidance / voluntary | `UAE-Federal-018` to `UAE-Federal-027` |
| UAE AI Guide (National Program for AI) | UAE federal | Test algorithms before field deployment; check representativeness; federal RegLab sandbox licences. | guidance | `UAE-Federal-028`, `UAE-Federal-029` |
| UAE National Cyber Security Policy for AI, version 1.1, November 2025 (Cyber Security Council, full PDF read in phase 3) | Federal ministries and authorities, emirate government entities, non government critical infrastructure entities | Policy statements in "shall" form: testing and validation of AI systems, secure development and testing, regular testing, risk assessment, supply chain assessment. Implementation guidance ("should"): rigorous testing before deployment, testing of changes and patches. Compliance monitored through the UAE Information Assurance Standard. | mandatory for the named entities (statements); guidance (implementation guidance) | `UAE-Federal-P3-01`† to `UAE-Federal-P3-08`† (portal summary rows `UAE-Federal-014`† to `UAE-Federal-017`† superseded) |
| Federal Decree Law No. 45 of 2021 (PDPL) | UAE federal, personal data | Impact assessment before high risk processing; testing of security measures; right to human review of automated decisions; Article 2 excludes government data and government entities. | conditional / mandatory | `UAE-Federal-005` to `UAE-Federal-008`, `UAE-Federal-032` to `UAE-Federal-034` |
| Abu Dhabi Law No. 3 of 2024 (AI and Advanced Technology Council) | Abu Dhabi | The Council sets conditions and standards for AI investment and research; relevant entities must implement the Council's decisions. No testing content. | ambiguous / mandatory | `UAE-AbuDhabi-Other-001`, `UAE-AbuDhabi-Other-002` |
| DoH Abu Dhabi Policy on Use of AI in the Healthcare Sector (version 0.9, April 2018) | Abu Dhabi health sector | "Expects" in one place and "must comply" in another. | ambiguous | `UAE-AbuDhabi-DoH-001`, `UAE-AbuDhabi-DoH-002` |
| DoH Abu Dhabi Responsible AI Risk Management Protocol V1 (October 2025) | Abu Dhabi health sector | Controls tested by simulation or pilot before implementation; risk rating; avoid high residual risk; reassessment and DoH review. Section headed "Recommended Protocol". | ambiguous | `UAE-AbuDhabi-DoH-P3-01`† to `UAE-AbuDhabi-DoH-P3-04`† |
| DoH Abu Dhabi Responsible AI Standard V1 (October 2025) | Abu Dhabi health sector | Mandatory validation against benchmarks, testing across diverse data, safety testing and failure mode analysis, code review and vulnerability scanning, representativeness audits, risk assessment, documented evidence, internal and DoH audits. Conditional: conformity assessment for high risk systems, no deployment at very high residual risk. | mandatory / conditional | `UAE-AbuDhabi-DoH-003` to `UAE-AbuDhabi-DoH-014` |
| DHA Artificial Intelligence in the Healthcare Policy (HISHD/PP-09) | Dubai health sector | Independent third party validation, independent audits of AI functionality, certification from recognised bodies, performance monitoring against training results, auditable validation statements. | mandatory | `UAE-Dubai-025` to `UAE-Dubai-030` |
| Dubai AI Ethics Guidelines (English and Arabic editions), Ethics Toolkit and Self Assessment Tool | Dubai | Bias testing, discrimination impact assessment, quality checks as stringent as for a human, external audit for critical decisions (marked suspended in the versions read because no mechanism existed). The Executive Council reportedly advised all public entities to use the toolkit. | guidance / voluntary / ambiguous | `UAE-Dubai-001` to `UAE-Dubai-006`, `UAE-Dubai-011` to `UAE-Dubai-024` |
| Dubai AI Integration Matrix Framework (Dubai Digital Authority) | Dubai government | Quality assurance protocols, ethical compliance validation, pilots. | guidance / ambiguous | `UAE-Dubai-007` to `UAE-Dubai-009`, `UAE-Dubai-031`, `UAE-Dubai-032` |
| Dubai Information Security Regulation v2.0 (DESC) | Dubai government entities | Security testing during development, technical reviews and vulnerability tests, security sign off. Mandatory but not AI specific. | mandatory | `UAE-Dubai-033` to `UAE-Dubai-035` |
| Dubai Law No. 9 of 2023 (autonomous vehicles) | Dubai | Technical inspection as a condition of licence; RTA approval for updates to the driving system. | conditional | `UAE-Dubai-036`, `UAE-Dubai-037` |
| Dubai Department of Finance and Dubai Culture AI policies | Dubai entities | Commitments to risk assessment, monitoring and internal audit of their own AI. | ambiguous | `UAE-Dubai-038` to `UAE-Dubai-040` |
| DIFC Data Protection Regulations, Consolidated Version No. 2, Regulation 10 | DIFC | High risk processing by autonomous or semi autonomous systems for commercial purposes needs audit and certification; an Autonomous Systems Officer; accountability and bias mitigation. | conditional | `UAE-DIFC-ADGM-001` to `UAE-DIFC-ADGM-005`, `UAE-DIFC-ADGM-016` |
| DIFC Commissioner guidance, Accreditation and Certification Framework and FAQs | DIFC | Certification application to an accredited certification body; criteria for those bodies; assessment of governance, risk choice, bias and transparency. Each Framework page says it is informational and may be incomplete. | conditional / voluntary / guidance | `UAE-DIFC-ADGM-017` to `UAE-DIFC-ADGM-025` |
| DIFC consultation on amending Regulation 10 (June 2026, not enacted) | DIFC | Would add a duty that a system be tested for safety verification before commercial use, a safety principle, a Commissioner power to require an impact assessment or audit, and a certification regulation. | ambiguous (proposal) | `UAE-DIFC-ADGM-P3-01`† to `UAE-DIFC-ADGM-P3-04`† |
| ADGM data protection and FSRA guidance | ADGM | Impact assessment before high risk processing; automated decision guidance; digital investment management guidance on testing. | conditional / guidance | `UAE-DIFC-ADGM-006` to `UAE-DIFC-ADGM-015` |
| SDAIA AI Ethics Principles (version 1.0, September 2023, portal host) | Saudi Arabia | Robustness testing, fairness metrics, privacy leakage testing, user acceptance testing, third party due diligence, conformity assessment for high risk systems. Scope says it applies to all AI stakeholders; the compliance mechanism is optional registration. | ambiguous | `Saudi-001` to `Saudi-010` |
| SDAIA Generative AI Guidelines, AI Adoption Framework, National AI Risk Management Framework | Saudi Arabia | sdaia.gov.sa still rejects the fetch tool; rows are unverified. | guidance | `Saudi-011`† to `Saudi-017`† |
| SDAIA AI service provider accreditation and AI ethics self assessment (Arabic service pages) | Saudi Arabia | A questionnaire reviewed by a committee leading to a label; a self assessment tool. | ambiguous | `Saudi-P3-15`†, `Saudi-P3-16`† |
| SFDA guidance on AI based medical devices (MDS-G010, 2022) | Saudi medical devices | Pre market verification and validation, clinical validation, independent review, reference datasets and subgroup analysis, local validation, post market monitoring, change control. Clarifies requirements set in another document that was not read. | ambiguous | `Saudi-P3-07`† to `Saudi-P3-14`† |
| NCA AI Cybersecurity Guidelines (draft, AICG-1:2026) | Saudi Arabia | AI penetration testing, red teaming, guardrail testing before production, validating human override. Draft; the document states it is not mandatory. Read in phase 3 from page images of the PDF the fetch tool saved. | guidance | `Saudi-018` to `Saudi-023`, `Saudi-P3-01`† to `Saudi-P3-06`† |

**Source says (selected details).**

- **DoH Standard.** It applies to DoH and licensed healthcare entities developing, procuring or deploying AI; it states a revision date of October 2026 (Section 7). DoH states it will conduct periodic audits (`UAE-AbuDhabi-DoH-013`).
- **DHA policy.** Independent third party validation and independent audits of AI functionality are mandatory for healthcare AI in Dubai (`UAE-Dubai-025`, `UAE-Dubai-026`). The policy shows conflicting effective dates and a revision date that has passed.
- **DIFC Regulation 10.** Commercial high risk processing needs certification under the Commissioner's framework (`UAE-DIFC-ADGM-004`, `UAE-DIFC-ADGM-018`). The Framework carries a notice that it is informational only and that its implementation timeline is at the Commissioner's discretion; this conflicts with wording that certification is required (conflict flag on `UAE-DIFC-ADGM-018`).
- **National Cyber Security Policy for AI.** The scope section names ministries and federal authorities and non government critical infrastructure entities, and covers emirate government entities through the emirate lead where an emirate programme exists (`UAE-Federal-P3-08`†). The policy statements use "shall" and the implementation guidance "should" (`UAE-Federal-P3-01`†, `UAE-Federal-P3-02`†). *Interpretation:* under the protocol's four part test, the "shall" statements are binding testing duties for those entities, but the statement on testing and validation does not itself fix when testing happens; the before deployment wording is in guidance. Its subject is security; it does not address accuracy, fairness or fitness for purpose.
- **PDPL.** The retrieved articles address personal data processing, do not set accuracy, robustness or fairness testing for AI as such, and exclude government data and government entities (`UAE-Federal-034`).

### 6.2 What was searched, where

Federal, Abu Dhabi and Dubai sources were searched with English and Arabic queries using the search and fetch tools only. 230 searches and fetches are logged and 122 sources are listed (51 Arabic queries; 44 searches ended in not found).

| Zone | Searches and fetches logged | English / Arabic queries | Found | Not found | Blocked | Locator only | Sources listed | English read | Arabic wording obtained | of which English rendering by fetch tool | Not read |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UAE federal | 77 | 54 / 23 | 49 | 17 | 11 | 0 | 34 | 16 | 8 | 5 | 10 |
| Abu Dhabi | 59 | 45 / 14 | 34 | 14 | 3 | 8 | 27 | 20 | 4 | 4 | 3 |
| Dubai | 94 | 80 / 14 | 75 | 13 | 6 | 0 | 61 | 40 | 5 | 4 | 16 |

**Arabic handling.** For 17 sources Arabic original wording was obtained. For 13 of them the fetch tool returned an English summary or paraphrase containing some Arabic quotations; those English renderings are machine produced and are not official translations. Official English editions of bilingual documents were read in English and the Arabic edition was not always checked. Per source, the column `language_read` in `data/uae_sources.csv` says what was read, `reading_class` classifies it and `machine_summary_of_arabic` flags machine renderings.

### 6.3 Searched for and not found in the public sources searched

- A UAE federal law or Cabinet resolution on AI. The federal AI and Data Authority approved in June 2026 was found only as an announcement, with no legal instrument cited.
- A UAE federal technical standard for functional, fairness or accuracy testing of AI in government. The cyber security policy for AI covers security testing only.
- An Abu Dhabi government wide AI policy or standard for government entities (Department of Government Enablement, Abu Dhabi Digital Authority, AI and Advanced Technology Council). The Council's website did not resolve.
- The text of the Dubai AI Policy for Government Entities (April 2025) and of the Dubai Electronic Security Center AI Security Policy. Both are referred to publicly; neither text is published (the Center says its documents are available by e-mail request).
- The DoH AI Policy of 2025 that the DoH Standard and Protocol both cite; the DoH policies listing, now readable, shows only the 2018 policy.
- UAE PDPL Executive Regulations.
- An external audit mechanism replacing the suspended Dubai guideline.
- Leads that could not be read: the Central Bank of the UAE guidance note on AI and machine learning for licensed financial institutions (February 2026; rulebook site rejected the fetch), a DFSA letter on AI risk management (June 2026; rejected), an agentic AI guide for government entities (rejected), and the UAE Information Assurance Standard appendix that the cyber security policy uses for compliance monitoring (no public copy found).

The full list of queries that ended in not found or blocked is in `docs/UAE_COVERAGE.md`.

---

## 7. Time sensitive items

Each item records the locator, the retrieval date and any source conflict. The full table, with the access path for each item, is in `docs/TIME_SENSITIVE.md` and `data/time_sensitive.csv`. Status counts: blocked: 27, changed: 27, confirmed: 87, confirmed_draft: 1, confirmed_exists: 2, corrected: 2, not_found: 13, not_found_in_sources_searched: 2, open: 15, secondary_only: 5.

| Topic | Item | Status | Retrieved on |
|---|---|---|---|
| EU Omnibus | Act identity and title | confirmed | 2026-10-12 |
| EU Omnibus | Signature date | confirmed | 2026-10-12 |
| EU Omnibus | OJ publication date | confirmed | 2026-10-12 |
| EU Omnibus | Entry into force | confirmed | 2026-10-12 |
| EU Omnibus | Art 113 Annex III high-risk application (Chapter III Sections 1 to 3) | open | 2026-10-12 |
| EU Omnibus | Art 113 Annex I high-risk application | open | 2026-10-12 |
| EU Omnibus | Art 57(1) national sandboxes | confirmed | 2026-10-12 |
| EU Omnibus | Art 111(2) public-authority backstop | open | 2026-10-12 |
| EU Omnibus | Art 111(3)/(4) legacy GPAI | open | 2026-10-12 |
| EU Omnibus | Art 50(2) marking, systems placed before 2 Aug 2026 | open | 2026-10-12 |
| EU Omnibus | Art 5(1)(ba),(bb),(1a),(1b) new prohibitions | open | 2026-10-12 |
| EU Omnibus | Commission fining powers over GPAI (Art 101) | open | 2026-10-12 |
| EU Omnibus | Later corrigendum or further amendment | confirmed | 2026-10-12 |
| DoH Responsible AI Standard | RAI Standard reference no. | confirmed | 2026-10-12 |
| DoH Responsible AI Standard | RAI Standard publication/effective date | confirmed | 2026-10-12 |
| DoH Responsible AI Standard | RAI Standard revision due | confirmed | 2026-10-12 |
| DoH Responsible AI Standard | RAI Standard owner | confirmed | 2026-10-12 |
| DoH Responsible AI Standard | RAI Standard current status (revised/replaced/withdrawn?) | blocked | 2026-10-12 |
| DoH Responsible AI Standard | DoH policies listing, Arabic | blocked | 2026-10-12 |
| DoH Responsible AI Standard | V2 / addendum / circular for RAI Standard | open | 2026-10-12 |
| DoH Responsible AI Standard | AI Policy Standard (June 2025) referenced by Standard | confirmed | 2026-10-12 |
| DoH Responsible AI Standard | AI Risk Management (July 2025) referenced by Standard | confirmed | 2026-10-12 |
| DoH Responsible AI Standard | 2018 Policy on Use of AI: title/ref/version/date | confirmed | 2026-10-12 |
| DoH Responsible AI Standard | 2018 policy current vs superseded | open | 2026-10-12 |
| DIFC Regulation 10 | DP Regulations current consolidated version | confirmed | 2026-10-12 |
| DIFC Regulation 10 | DP Regulations in-force date | confirmed | 2026-10-12 |
| DIFC Regulation 10 | Amendments after Version No. 2 | open | 2026-10-12 |
| DIFC Regulation 10 | Reg 10 exists: autonomous and semi-autonomous systems | confirmed | 2026-10-12 |
| DIFC Regulation 10 | Commissioner audit or certification requirement for High Risk Processing | confirmed_exists | 2026-10-12 |
| DIFC Regulation 10 | Autonomous Systems Officer guidance | confirmed_exists | 2026-10-12 |
| DIFC Regulation 10 | 2025 to 2026 amendments to DP Law or Regulations touching AI | open | 2026-10-12 |
| Saudi drafts | 1a SDAIA AI Ethics Principles current edition | blocked | 2026-10-12 |
| Saudi drafts | 1b SDAIA AI Ethics Principles earlier edition (dgp.sdaia.gov.sa) | corrected | 2026-10-12 |
| Saudi drafts | 1c SDAIA AI Ethics Principles Arabic edition | open | 2026-10-12 |
| Saudi drafts | 1d Secondary note: Ethics Principles 2.0 | open | 2026-10-12 |
| Saudi drafts | 2a NCA AI Cybersecurity Guidelines status | confirmed_draft | 2026-10-12 |
| Saudi drafts | 2b NCA doc code and title: Guidelines vs Controls | open | 2026-10-12 |
| Saudi drafts | 2c NCA mandatory vs advisory | open | 2026-10-12 |
| Saudi drafts | 2d NCA Arabic PDF | blocked | 2026-10-12 |
| Saudi drafts | 3 SDAIA National AI Risk Management Framework | corrected | 2026-10-12 |
| Saudi drafts | 4a SDAIA Generative AI Guidelines for Government | blocked | 2026-10-12 |
| Saudi drafts | 4b SDAIA AI Adoption Framework | blocked | 2026-10-12 |
| Saudi drafts | 5a Other SDAIA instruments on AI testing or assurance | blocked | 2026-10-12 |
| Saudi drafts | 5b NCA other AI testing/assurance instrument | not_found_in_sources_searched | 2026-10-12 |
| Saudi drafts | 5c Saudi statutes via laws.boe.gov.sa (AI-specific) | not_found_in_sources_searched | 2026-10-12 |
| Canada | Directive on Automated Decision-Making: current version / last amendment date | blocked | 2026-10-16 |
| Canada | Any 2026 amendment or review of the Directive | blocked | 2026-10-16 |
| US-NIST | AI RMF revision (1.1 / 2.0) | confirmed | 2026-10-16 |
| US-NIST | New AI RMF profile: Trustworthy AI in Critical Infrastructure | changed | 2026-10-16 |
| US-NIST | Cyber AI Profile (NIST IR 8596) | changed | 2026-10-16 |
| US-NIST | NIST AI 800-2 status | confirmed | 2026-10-16 |
| US-NIST | CAISI name / program page | changed | 2026-10-16 |
| US-OMB | M-25-21 still current | confirmed | 2026-10-16 |
| ISO-IEC | ISO/IEC 42001 | blocked | 2026-10-16 |
| ISO-IEC | ISO/IEC 23894 | blocked | 2026-10-16 |
| ISO-IEC | ISO/IEC 42005 | blocked | 2026-10-16 |
| ISO-IEC | ISO/IEC 42006 | blocked | 2026-10-16 |
| ISO-IEC | ISO/IEC TS 42119-2 | blocked | 2026-10-16 |
| ISO-IEC | ISO/IEC TR 29119-11 (or successor) | blocked | 2026-10-16 |
| ISO-IEC | ISO/IEC TR 24027 | blocked | 2026-10-16 |
| ISO-IEC | ISO/IEC 24029-2 | blocked | 2026-10-16 |
| ISO-IEC | ISO/IEC 25059 | blocked | 2026-10-16 |
| ISO-IEC | ISO/IEC TS 12791 | blocked | 2026-10-16 |
| ISO-IEC | ISO/IEC 27090 (row ISO-IEC-019) | blocked | 2026-10-16 |
| Reg 2026/1744 status | Signature date | confirmed | 2026-10-16 |
| Reg 2026/1744 status | OJ publication date | confirmed | 2026-10-16 |
| Reg 2026/1744 status | Entry into force | confirmed | 2026-10-16 |
| AI Act application dates | Chapter III Sections 1-3, Annex III systems | confirmed | 2026-10-16 |
| AI Act application dates | Chapter III Sections 1-3, Annex I systems | confirmed | 2026-10-16 |
| AI Act application dates | Entry into force / general date of base act | confirmed | 2026-10-16 |
| AI Act application dates | New prohibitions and Arts 102-110 | confirmed | 2026-10-16 |
| Transitional rules | Art 111(2) legacy high-risk systems | confirmed | 2026-10-16 |
| Transitional rules | Art 111(3) legacy GPAI models | confirmed | 2026-10-16 |
| Transitional rules | Art 111(4) legacy generative systems | confirmed | 2026-10-16 |
| Transitional rules | Art 111(1) Annex X large-scale IT systems | confirmed | 2026-10-16 |
| Sandboxes | Art 57(1) national sandbox deadline | confirmed | 2026-10-16 |
| Transparency | Art 50(2) marking timing | confirmed | 2026-10-16 |
| Conformity assessment | Sectoral notified bodies designation deadline | confirmed | 2026-10-16 |
| Later acts | Corrigendum after 24 July 2026 | changed | 2026-10-16 |
| Later acts | Further amendment of Reg 2024/1689 after 24 July 2026 | not_found | 2026-10-16 |
| harmonised_standards | EN 18286:2026 (AI QMS) OJ citation | changed | 2026-10-16 |
| harmonised_standards | Other AI Act harmonised standards cited in OJ | confirmed | 2026-10-16 |
| harmonised_standards | prEN 18228 AI risk management | confirmed | 2026-10-16 |
| harmonised_standards | prEN 18229-1 to -5 AI trustworthiness framework | confirmed | 2026-10-16 |
| harmonised_standards | prEN 18282 cybersecurity for AI systems | confirmed | 2026-10-16 |
| harmonised_standards | prEN 18285 AI conformity assessment framework | confirmed | 2026-10-16 |
| harmonised_standards | EC standardisation page status | changed | 2026-10-16 |
| gpai_code | GPAI Code of Practice version | confirmed | 2026-10-16 |
| gpai_code | Commission/AI Board adequacy assessment | confirmed | 2026-10-16 |
| gpai_code | Signatories / partial signature | changed | 2026-10-16 |
| guidelines | Art 6 high-risk classification guidelines | changed | 2026-10-16 |
| guidelines | GPAI guidelines (scope of obligations) | confirmed | 2026-10-16 |
| guidelines | Serious incident guidance (Art 73) and template | not_found | 2026-10-16 |
| guidelines | Art 50 transparency guidelines | changed | 2026-10-16 |
| guidelines | Art 50 Code of Practice on Transparency of AI-generated Content | changed | 2026-10-16 |
| guidelines | Post-market monitoring template (Art 72(3)) | confirmed | 2026-10-16 |
| implementing_acts | Implementing Regulation on GPAI evaluations and proceedings | changed | 2026-10-16 |
| common_specifications | Art 41 common specifications | not_found | 2026-10-16 |
| eu_ai_act_text | Consolidated text version | confirmed | 2026-10-16 |
| UK statutory testing duty | Government AI bill / statutory AI testing duty | confirmed | 2026-10-16 |
| UK statutory testing duty | Private members' AI bills in Parliament | blocked | 2026-10-16 |
| UK AISI | AISI remit | confirmed | 2026-10-16 |
| UK AISI | Pre-deployment testing agreements | confirmed | 2026-10-16 |
| UK AISI | Published pre-deployment evaluation reports | confirmed | 2026-10-16 |
| UK ATRS | Mandatory status and scope | confirmed | 2026-10-16 |
| UK AI Playbook | Current version | confirmed | 2026-10-16 |
| Singapore AI Verify | AI Verify Testing Framework version | confirmed | 2026-10-16 |
| Singapore MGF Agentic AI | Latest version and date | confirmed | 2026-10-16 |
| Singapore IMDA testing guidance | Starter Kit for Testing Agentic Systems for Safety and Reliability | changed | 2026-10-16 |
| Singapore IMDA testing guidance | Starter Kit for Testing LLM-Based Applications current version | confirmed | 2026-10-16 |
| Singapore AI assurance | AI Tester Accreditation Programme (AI TAP) | changed | 2026-10-16 |
| Singapore AI assurance | Global AI Assurance Pilot / Sandbox outputs | confirmed | 2026-10-16 |
| Singapore public agencies | Whether testing guidance is binding on public agencies | not_found | 2026-10-16 |
| Singapore MGF GenAI | Publication date | changed | 2026-10-16 |
| Korea | AI Framework Act entry into force | confirmed | 2026-10-16 |
| Korea | Act No. 21311 delayed provisions | confirmed | 2026-10-16 |
| Korea | Enforcement Decree number and date | confirmed | 2026-10-16 |
| Korea | Enforcement Decree current version | changed | 2026-10-16 |
| Korea | Decree partial amendment (MSIT legislative notice) | changed | 2026-10-16 |
| Korea | Compute threshold for Art. 32 safety duties | confirmed | 2026-10-16 |
| Korea | Grace period for fines and investigations | confirmed | 2026-10-16 |
| Korea | MSIT guidelines/notices on high-impact AI safety and reliability measures | not_found | 2026-10-16 |
| Korea | AI Basic Act Improvement Working Group | changed | 2026-10-16 |
| Japan | AI Promotion Act implementation | confirmed | 2026-10-16 |
| Japan | Current AI Basic Plan | confirmed | 2026-10-16 |
| Japan | Government guideline on generative AI procurement and use | changed | 2026-10-16 |
| Japan | Guideline for Ensuring Appropriateness (AI Act Art. 13) | confirmed | 2026-10-16 |
| China | GB/T 45654-2025 status | confirmed | 2026-10-16 |
| China | GB 45438-2025 status | confirmed | 2026-10-16 |
| China | Anthropomorphic AI Interactive Services Measures | confirmed | 2026-10-16 |
| China | Digital Virtual Human Information Services Measures | changed | 2026-10-16 |
| China | Cybersecurity Law amendment (AI article) | confirmed | 2026-10-16 |
| China | New generative AI national standards 2025-2026 | changed | 2026-10-16 |
| China | Mandatory standard on AI agent application security (planned) | secondary_only | 2026-10-16 |
| China | TC260 practice guide on AI application security (general) | changed | 2026-10-16 |
| China | TC260 AI Safety Governance Framework 2.0 | confirmed | 2026-10-16 |
| China | TC260 Sep 2026 notice on agentic system development security practice guide (draft) | changed | 2026-10-16 |
| SDAIA AI Ethics Principles | current edition | confirmed | 2026-10-16 |
| SDAIA AI Ethics Principles | 2.0 edition | secondary_only | 2026-10-16 |
| NCA AI cybersecurity document | status (draft vs final) | confirmed | 2026-10-16 |
| NCA AI cybersecurity document | title (Guidelines vs Controls) and code | changed | 2026-10-16 |
| NCA AI cybersecurity document | mandatory vs advisory | confirmed | 2026-10-16 |
| SDAIA National AI Risk Management Framework | primary publication and testing content | blocked | 2026-10-16 |
| SDAIA Generative AI Guidelines for Government | existence and testing content | blocked | 2026-10-16 |
| Saudi AI testing/assurance instruments | SDAIA AI service provider accreditation | confirmed | 2026-10-16 |
| Saudi AI testing/assurance instruments | SDAIA AI ethics self-assessment tool | confirmed | 2026-10-16 |
| Saudi AI testing/assurance instruments | SFDA AI/ML medical devices guidance | confirmed | 2026-10-16 |
| Saudi AI testing/assurance instruments | SASO AI technical regulation | not_found | 2026-10-16 |
| Saudi AI statutes | AI-specific statute on laws.boe.gov.sa | not_found | 2026-10-16 |
| GCC | Qatar - QCB Artificial Intelligence Guideline | blocked | 2026-10-16 |
| GCC | Qatar - NCSA Guidelines for Secure Adoption and Usage of AI | blocked | 2026-10-16 |
| GCC | Bahrain - National Policy for the Use of AI (iGA, 27 Jul 2025) | confirmed | 2026-10-16 |
| GCC | Oman - MTCIT Public Policy for Safe and Ethical Use of AI Systems | secondary_only | 2026-10-16 |
| GCC | Kuwait - CITRA AI instrument | not_found | 2026-10-16 |
| DoH Responsible AI Standard | Current version and status | confirmed | 2026-10-16 |
| DoH Responsible AI Standard | DoH policies listing (EN and AR) | changed | 2026-10-16 |
| DoH Responsible AI Standard | 2025 DoH AI Policy referenced by Standard and Protocol | not_found | 2026-10-16 |
| DoH Responsible AI Standard | Responsible AI Risk Management Protocol (companion document) | confirmed | 2026-10-16 |
| DoH Responsible AI Standard | Conflict: treatment of high-risk AI systems | changed | 2026-10-16 |
| DoH Responsible AI Standard | Arabic title of the Responsible AI Standard | not_found | 2026-10-16 |
| DIFC Regulation 10 | DP Regulations current consolidated version | confirmed | 2026-10-16 |
| DIFC Regulation 10 | Amendments after Version No. 2 touching Regulation 10 | changed | 2026-10-16 |
| DIFC Regulation 10 | 2025 amendment to DIFC Data Protection Law | secondary_only | 2026-10-16 |
| UAE federal instruments | UAE Charter for the Development and Use of AI (2024) updated? | confirmed | 2026-10-16 |
| UAE federal instruments | National Strategy for AI 2031 updated? | confirmed | 2026-10-16 |
| UAE federal instruments | New federal AI legislation (2025-2026) | not_found | 2026-10-16 |
| UAE federal instruments | National Cyber Security Policy for AI: version and binding status (rows UAE-Federal-014 to 017) | changed | 2026-10-16 |
| UAE federal instruments | CBUAE Guidance Note on AI/ML for licensed financial institutions (Feb 2026) | blocked | 2026-10-16 |
| UAE federal instruments | Agentic AI government framework date (row UAE-Federal-004) | secondary_only | 2026-10-16 |
| Dubai instruments | Dubai AI Policy for Government Entities (Apr 2025) text | not_found | 2026-10-16 |
| Dubai instruments | Dubai AI Security Policy (DESC, Sep 2024) text | not_found | 2026-10-16 |
| DIFC-ADGM instruments | DFSA letter on AI risk management (4 Jun 2026) | blocked | 2026-10-16 |

Phase 3 items (16 October 2026) are appended to the phase 2 items; where a phase 3 item updates a phase 2 item, the phase 3 status applies.

**EU Act after Regulation (EU) 2026/1744.** *Source says:* signed 8 July 2026, published in the Official Journal on 24 July 2026, in force 27 July 2026 (Article 4 of the amending act). In the amended Article 113, third paragraph, point (c)(i) sets 2 December 2027 for Annex III high risk systems and point (c)(ii) sets 2 August 2028 for Annex I systems; point (a) sets 2 December 2026 for the new prohibitions and point (d) applies Articles 102 to 110 from 27 July 2026. The amended Article 111(2) gives public authority deployers of legacy systems until 2 August 2030; a new Article 111(4) gives generative systems already on the market until 2 December 2026 for marking. A corrigendum of 29 September 2026 changes one word in the German version only. The consolidated text read is dated 27 July 2026 and lists only this amendment. *Interpretation:* the phase 2 caveat that the dates were confirmed only at recital level is resolved.

**EU codes, guidelines and standards.** *Source says:* Commission Implementing Decision (EU) 2026/2274 of 12 October 2026, published 14 October 2026, cites EN 18286:2026 (quality management); no other AI Act harmonised standard is cited, and the risk management, trustworthiness, cybersecurity and conformity assessment drafts are at enquiry or earlier stages. The General Purpose AI Code of Practice is still the July 2025 version; the Commission's opinion of 1 August 2025 found it adequate. The Article 50 guidelines were adopted and a code of practice on transparency of AI generated content was finalised in June 2026. Implementing Regulation (EU) 2026/1755 sets arrangements for AI Office model evaluations. The Article 6 classification guidelines are still a draft. Final serious incident guidance and any common specifications were not found.

**United States, United Kingdom, Singapore.** *Source says:* NIST has not released a revised AI RMF; AI 800-2 remains an initial public draft; OMB M-25-21 is current and M-26-04 adds procurement transparency for large language models. No UK government AI bill was announced; the AI Security Institute describes itself as a research body without regulatory powers; the AI Playbook is still the February 2025 edition; ATRS remains mandatory for in scope bodies. Singapore's agentic AI framework is at version 1.5 (May 2026, updated June 2026); IMDA lists a starter kit for testing agentic systems (October 2026, text not read) and an AI tester accreditation programme with five accredited firms listed.

**Japan, Korea, China.** *Source says:* Japan's Digital Agency guideline DS-920 v2.0 replaced the May 2025 edition and applies from 1 September 2026; the second AI Basic Plan (July 2026) is current. Korea's AI Basic Act and decree are in force; the national law site now shows a newer decree number (August 2026, an amendment made through another law) whose content could not be read, and no final MSIT guideline on high impact or safety measures was found. In China, GB/T 45654-2025 is a recommended standard in force since 1 November 2025; no new mandatory AI national standard was found in the official catalogue; the anthropomorphic AI measures are in force from 15 July 2026.

**DoH Responsible AI Standard.** *Source says:* still V1 (October 2025) with a stated revision date of October 2026; the DoH policies listing, blocked in phase 2, is now readable and lists only the 2018 AI policy. A companion Risk Management Protocol V1 was read (Section 6.1). *Interpretation:* the revision date falls this month; check again before relying on V1.

**DIFC Regulation 10.** *Source says:* Consolidated Version No. 2 (in force 1 September 2023) is still the in force text. A consultation paper proposed amendments; comments closed 18 July 2026 and no enactment notice was seen on 16 October 2026.

**Saudi instruments.** *Source says:* the NCA AI cybersecurity document remains a draft, titled guidelines, and states it is not mandatory. The SDAIA Ethics Principles official Arabic cover reads first edition, September 2023. The National AI Risk Management Framework, the generative AI guidelines and the adoption framework are on sdaia.gov.sa, which rejects the fetch tool; an official news headline describes the framework as a guidance reference. *Interpretation:* none of the Saudi instruments read is binding on its face.

---

## 8. Gap analysis for UAE government deployment

**Framing.** These are gaps in the evidence base retrieved, measured against what other frameworks in this table contain. They are not claims about what the UAE does or does not require. A UAE government entity may be subject to internal, sectoral or non public instruments that were not found.

**G1. A federal binding duty exists for AI security testing, not for testing whether a system works well or fairly.**
*Source says:* the National Cyber Security Policy for AI binds federal ministries and authorities and emirate government entities to test and validate AI systems, develop and test them securely, test them regularly, and assess risks and suppliers (`UAE-Federal-P3-01`†, `UAE-Federal-P3-03`† to `UAE-Federal-P3-06`†); its before deployment wording is guidance (`UAE-Federal-P3-02`†). The Adoption Guideline in Government Services describes evaluation against acceptance criteria and monitoring (`UAE-Federal-009`, `UAE-Federal-011`), and the Ethics Guidelines suggest bias testing and external audit for critical decisions (`UAE-Federal-018`, `UAE-Federal-021`), in "should" language. The Charter states a safety principle (`UAE-Federal-001`). Comparators that bind government bodies on performance testing are OMB M-25-21 (`US-OMB-003`, `US-OMB-004`), Japan's DS-920 for generative AI (`Japan-P3-01`†) and, for health, the DoH Standard (`UAE-AbuDhabi-DoH-003`).
*Interpretation:* a federal entity has a security testing duty but, in the texts read, no binding requirement to test accuracy, robustness for the task, or fairness before deployment. Whether the Adoption Guideline binds a particular entity is not stated in the text read. The policy refers compliance to the UAE Information Assurance Standard appendix, which was not found, so how the testing duty is checked in practice is not known from public sources.

**G2. Beyond security, binding testing text is sector, zone or data specific.**
*Source says:* mandatory text covers Abu Dhabi health (`UAE-AbuDhabi-DoH-003` to `UAE-AbuDhabi-DoH-013`), Dubai health (`UAE-Dubai-025`, `UAE-Dubai-026`), commercial high risk processing in DIFC (`UAE-DIFC-ADGM-004`), personal data (`UAE-Federal-005`, `UAE-Federal-007`), information security in Dubai government (`UAE-Dubai-034`) and AI security across government (`UAE-Federal-P3-01`†).
*Interpretation:* for non health public sector uses such as eligibility, licensing, customs or inspection, the retrieved sources contain no AI specific binding duty to test performance or fairness. A cross sector baseline for those properties, if one exists, was not found; the Dubai AI Policy for Government Entities may contain one, but its text is not published.

**G3. Benchmarks and thresholds are not defined.**
*Source says:* the DoH Standard requires validation against "established performance benchmarks" (`UAE-AbuDhabi-DoH-003`); the federal Ethics Guidelines say a fallback plan should include thresholds for acceptable results (`UAE-Federal-023`). The EU Act leaves metrics to the provider (`EU-AI-Act-018`); Singapore's Starter Kit and NIST describe how to set acceptance criteria (`Singapore-009`, `US-NIST-026`).
*Interpretation:* the gap is shared with other binding regimes. A procuring entity would need to define pass criteria itself.

**G4. Independent assurance is contingent.**
*Source says:* Dubai's external audit guideline is marked suspended in the versions read (`UAE-Dubai-005`, `UAE-Dubai-018`); the federal Ethics Guidelines suggest external audit (`UAE-Federal-021`); the Strategy plans a seal without criteria (`UAE-Federal-003`); the Dubai AI Seal classifies businesses rather than testing systems (`UAE-Dubai-010`). Binding independent assurance exists for Dubai health (`UAE-Dubai-025`) and for DIFC certification (`UAE-DIFC-ADGM-018`).
*Interpretation:* independent testing capacity outside those two is an open question, in most jurisdictions here and not only in the UAE.

**G5. Generative, agentic and frontier style evaluation.**
*Source says:* the cyber security policy requires regular security testing of AI systems (`UAE-Federal-P3-04`†), which the research agent coded as red teaming; no UAE row retrieved covers capability evaluation or misuse testing of generative or agentic systems specifically. Comparators: binding model evaluation for EU general purpose models with systemic risk (`EU-AI-Act-068`); guidance in `US-NIST-028`, `Japan-020`, `Singapore-007`, `UK-024`; Singapore's case studies of government agencies testing agents before rollout (`Singapore-035`, `Singapore-P3-01`†); the Saudi NCA draft on guardrail testing before production (`Saudi-P3-03`†).
*Interpretation:* the Cabinet announcement of a move toward agentic AI in federal services (`UAE-Federal-004`) contrasts with the absence of retrieved test guidance for agentic systems. An agentic AI guide for government entities was reported but could not be read (Section 6.3).

**G6. Vendor and black box systems.**
*Source says:* OMB requires alternative test methods when internals are inaccessible (`US-OMB-003`) and, for large language models, asks agencies to obtain model and system cards with evaluation information when buying (`US-OMB-P3-01`†). The UAE cyber security policy requires supply chain risk assessment (`UAE-Federal-P3-06`†). The DoH Standard requires secure code review and vulnerability scanning for proprietary and third party software (`UAE-AbuDhabi-DoH-007`).
*Interpretation:* no UAE procurement stage requirement was retrieved for obtaining a vendor's evaluation evidence on performance or bias.

**G7. Language and local context performance.**
*Source says:* no extracted test row requires language specific performance testing, such as Arabic dialects or bilingual use. Adjacent: dataset diversity (`UAE-AbuDhabi-DoH-008`), generalisation for under represented groups (`UAE-Dubai-002`), representativeness of training data (`UAE-Federal-028`).
*Interpretation:* an absence in this table, not a claim that no source addresses it. For a bilingual public service it is a natural item for a test plan (checklist C2, D1).

**G8. Post deployment monitoring outside health.**
*Source says:* binding monitoring appears in OMB (`US-OMB-006`), the DoH Standard (`UAE-AbuDhabi-DoH-005`) and the DHA policy (`UAE-Dubai-028`). Federal guidance mentions monitoring (`UAE-Federal-011`), and the cyber security policy requires regular security testing and the testing of changes (`UAE-Federal-P3-04`†, `UAE-Federal-P3-07`†). Federal law retrieved contains a periodic review of an impact assessment only (`UAE-Federal-006`).
*Interpretation:* outside security, an incident or drift reporting duty for non health government AI was not found.

**G9. Human oversight is required in places but its validation is not.**
*Source says:* the table has 1 oversight validation test row(s): `UAE-DIFC-ADGM-015` (guidance). Federal law gives a right to human review (`UAE-Federal-008`); the EU Act specifies oversight design (`EU-AI-Act-026`).
*Interpretation:* none of the frameworks read requires evidence that oversight works under realistic load or automation bias.

**G10. The data protection law may not reach government deployers.**
*Source says:* Federal Decree Law 45 of 2021 does not apply to government data or government entities that control or process personal data (`UAE-Federal-034`).
*Interpretation:* the impact assessment and security testing duties in that law (`UAE-Federal-005`, `UAE-Federal-007`) cannot be assumed to apply to a federal entity. The checklist treats them as conditional on entity type.

**G11. Gaps in the evidence itself.** Still blocked or unread: Canada's Directive, ISO catalogue pages, most SDAIA documents, the Dubai AI Policy for Government Entities and the DESC AI Security Policy (not published), the UAE Information Assurance Standard appendix, the CBUAE AI guidance note, the Korean decree's current version, and Arabic originals of several UAE documents. See Appendix B.

---

## 9. Proposed assurance checklist

**This is a proposal assembled from the sources, not a UAE requirement.** 29 items. Each cites the rows that motivate it. The last column shows whether any cited reliable row binds the item, and for which sources. Rows with a dagger are shown but excluded from the trace. The checklist is also a tool: `python -m ikhtibar.cli` takes answers about a system and returns, for each item, APPLIES, DOES_NOT_APPLY or UNKNOWN, with source traces and what would settle each UNKNOWN. The machine readable version is `data/checklist.yaml`; the table below is generated from it.

| # | Check | Applies when (proposal) | Motivating rows | Binding trace |
|---|---|---|---|---|
| **A** | **Scope and risk** |  |  |  |
| A1 | Classify the use case by impact or risk tier before build or procurement, and record the reasoning. | always | `Canada-005`†, `US-OMB-002`, `EU-AI-Act-011`, `Korea-006`, `UAE-AbuDhabi-DoH-009`, `Singapore-008`, `UAE-Dubai-021` | binding in some cited sources: EU-AI-Act (C), Korea (C), UAE-AbuDhabi-DoH (M), US-OMB (C) |
| A2 | Run a documented risk and impact assessment that names affected groups (including vulnerable groups) and the harms considered. | always | `EU-AI-Act-014`, `EU-AI-Act-019`, `Canada-015`†, `US-OMB-004`, `UAE-AbuDhabi-DoH-009`, `Saudi-014`†, `UAE-Dubai-013` | binding in some cited sources: EU-AI-Act (C), UAE-AbuDhabi-DoH (M), US-OMB (C) |
| A3 | Involve legal and data protection review from concept stage; run a data protection impact assessment where personal data is processed at risk. | data_types includes any of {personal, sensitive_personal, biometric, health, financial} | `Canada-018`†, `UAE-Federal-005`, `UAE-Federal-032`, `UAE-DIFC-ADGM-006`, `UAE-DIFC-ADGM-008`, `UAE-DIFC-ADGM-012`, `UAE-Federal-026` | binding in some cited sources: UAE-DIFC-ADGM (C), UAE-Federal (C) |
| **B** | **Define what good enough means** |  |  |  |
| B1 | Fix metrics and acceptance thresholds before testing, scaled to stakes, including whether pass criteria are absolute or comparative. | always | `EU-AI-Act-018`, `Singapore-009`, `Singapore-010`, `US-NIST-026`, `Saudi-004`, `EU-GPAI-CoP-008`, `UAE-AbuDhabi-DoH-003`, `UAE-Federal-009` | binding in some cited sources: EU-AI-Act (C), UAE-AbuDhabi-DoH (M) |
| B2 | Record why the chosen metrics and benchmarks are valid for the deployment context, and the limits of what the tests cannot show. | always | `US-NIST-006`, `US-NIST-035`, `US-NIST-037`, `US-NIST-041`, `US-NIST-043` | not binding in the reliable cited rows (guidance) |
| **C** | **Data** |  |  |  |
| C1 | Validate training, validation and test data for quality, provenance, lawfulness and representativeness. | system_type in {predictive_ml, genai_llm, agentic, computer_vision} | `Canada-011`†, `EU-AI-Act-020`, `China-002`, `UAE-AbuDhabi-DoH-008`, `UAE-Federal-028` | binding in some cited sources: China (M), EU-AI-Act (C), UAE-AbuDhabi-DoH (M) |
| C2 | Check that test data reflects the local deployment setting (population, language, geography) and under represented groups. | audience in {public_facing} | `EU-AI-Act-022`, `UAE-Dubai-002`, `UAE-AbuDhabi-DoH-008`, `UAE-Dubai-012` | binding in some cited sources: EU-AI-Act (C), UAE-AbuDhabi-DoH (M) |
| **D** | **System testing before release** |  |  |  |
| D1 | Test accuracy and task performance on diverse datasets in deployment like conditions. | always | `EU-AI-Act-016`, `Canada-007`†, `UAE-AbuDhabi-DoH-004`, `US-OMB-003`, `US-NIST-009`, `Singapore-005` | binding in some cited sources: EU-AI-Act (C), UAE-AbuDhabi-DoH (M), US-OMB (C) |
| D2 | Test for bias and unequal performance across subgroups. | {"all": [{"tri": ["decision_impact", ["significant_support", "automated_significant", "critical"], ["none"]]}, {"in": ["system_type", ["predictive_ml", "genai_llm", "agentic", "computer_vision"]]}]} | `Canada-007`†, `EU-AI-Act-020`, `UAE-AbuDhabi-DoH-008`, `UAE-Dubai-001`, `Singapore-019`, `US-NIST-034`, `Saudi-004`, `UAE-Federal-018`, `UAE-Dubai-011` | binding in some cited sources: EU-AI-Act (C), UAE-AbuDhabi-DoH (M) |
| D3 | Test robustness: perturbed inputs, outliers and extreme cases, and run to run stability. | system_type in {predictive_ml, genai_llm, agentic, computer_vision} | `EU-AI-Act-029`, `UAE-AbuDhabi-DoH-005`, `Saudi-003`, `Singapore-006`, `Singapore-017`, `ISO-IEC-009`, `UAE-Federal-023` | binding in some cited sources: EU-AI-Act (C), UAE-AbuDhabi-DoH (M) |
| D4 | Analyse failure modes and confirm fail safe or graceful degradation behaviour. | always | `UAE-AbuDhabi-DoH-005`, `US-NIST-023`, `US-NIST-011`, `EU-AI-Act-029`, `UAE-Federal-023` | binding in some cited sources: EU-AI-Act (C), UAE-AbuDhabi-DoH (M) |
| D5 | Run security testing: secure code review, vulnerability scanning, penetration testing, and AI specific attacks (prompt injection, poisoning, evasion). | always | `UAE-AbuDhabi-DoH-007`, `EU-AI-Act-030`, `Canada-017`†, `Saudi-019`, `Saudi-021`, `Singapore-025`, `UAE-Federal-007`, `UAE-Federal-025`, `UAE-Dubai-034` | binding in some cited sources: EU-AI-Act (C), UAE-AbuDhabi-DoH (M), UAE-Dubai (M), UAE-Federal (M) |
| D6 | Test for privacy leakage and re identification risk. | data_types includes any of {personal, sensitive_personal, biometric, health, financial} | `US-NIST-033`, `Saudi-005`, `Singapore-012` | not binding in the reliable cited rows (guidance) |
| D7 | For generative or agentic systems, run structured red teaming and harmful output and refusal tests, and test whole workflow and tool use behaviour. | system_type in {genai_llm, agentic} | `Singapore-007`, `Singapore-016`, `US-NIST-024`, `US-NIST-028`, `Japan-020`, `Japan-021`, `Saudi-020`, `EU-GPAI-CoP-003`, `Singapore-032`, `Singapore-033`, `China-024`, `China-025` | not binding in the reliable cited rows (voluntary) |
| D8 | For vendor or black box systems, secure contractual access for testing and verify vendor performance claims independently, using alternative methods where internals are closed. | acquisition in {vendor_product, mixed} | `US-OMB-003`, `Canada-022`†, `Singapore-023`, `Saudi-007` | binding in some cited sources: US-OMB (C) |
| **E** | **Oversight and independent review** |  |  |  |
| E1 | Design human oversight and test that override and review actually work, with trained reviewers. | decision_impact in {significant_support, automated_significant, critical} | `EU-AI-Act-026`, `Canada-019`†, `Canada-016`†, `Saudi-020`, `UAE-Federal-008`, `UAE-DIFC-ADGM-015` | binding in some cited sources: EU-AI-Act (C), UAE-Federal (M) |
| E2 | Obtain independent review scaled to impact level (qualified expert reviewers, independent assessors, or notified body style assessment). | decision_impact in {automated_significant, critical} | `Canada-013`†, `Canada-014`†, `US-OMB-004`, `US-NIST-007`, `EU-AI-Act-045`, `Singapore-026`, `EU-GPAI-CoP-007`, `UAE-Federal-021`, `UAE-Dubai-016` | binding in some cited sources: EU-AI-Act (C), US-OMB (C) |
| **F** | **Release decision and evidence** |  |  |  |
| F1 | Make a documented go or no go decision at an authority level matched to the impact tier, with a rule for unacceptable residual risk. | always | `Canada-020`†, `UAE-AbuDhabi-DoH-011`, `EU-AI-Act-015`, `US-NIST-017`, `Saudi-006`, `Singapore-026`, `UAE-Federal-009`, `UAE-Dubai-021` | binding in some cited sources: EU-AI-Act (C), UAE-AbuDhabi-DoH (C) |
| F2 | Keep reproducible evidence: test data versions, protocols, results and logs. | always | `EU-AI-Act-023`, `Canada-023`†, `UAE-AbuDhabi-DoH-006`, `US-NIST-044`, `Singapore-022`, `UAE-Federal-010` | binding in some cited sources: EU-AI-Act (C), UAE-AbuDhabi-DoH (M) |
| F3 | Publish or disclose a summary of tested performance and fairness results as appropriate to the audience. | audience in {public_facing} | `Canada-024`†, `Canada-021`†, `UK-018`, `EU-AI-Act-025`, `Singapore-029` | binding in some cited sources: EU-AI-Act (C) |
| **G** | **After deployment** |  |  |  |
| G1 | Monitor performance, drift, outcomes, complaints and human overrides on a schedule. | always | `Canada-008`†, `Canada-010`†, `EU-AI-Act-060`, `US-OMB-006`, `UAE-AbuDhabi-DoH-005`, `UK-003`, `Singapore-034`, `UAE-Federal-011`, `UAE-Dubai-014`, `UAE-Dubai-028`, `UAE-DIFC-ADGM-010` | binding in some cited sources: EU-AI-Act (C), UAE-AbuDhabi-DoH (M), UAE-Dubai (M), US-OMB (C) |
| G2 | Define re testing triggers: model or data change, vendor update, scope change. | always | `Singapore-014`, `UK-011`, `EU-AI-Act-043`, `Canada-006`†, `Singapore-018` | binding in some cited sources: EU-AI-Act (C) |
| G3 | Set incident escalation, suspension and rollback procedures. | always | `EU-AI-Act-061`, `EU-AI-Act-034`, `UK-012`, `Canada-010`† | binding in some cited sources: EU-AI-Act (C) |
| **H** | **Jurisdiction specific checks (apply only when the entity zone is stated)** |  |  |  |
| H1 | Healthcare entity licensed by Abu Dhabi Department of Health: check each applicable clause of the DoH Responsible AI Standard V1 (validation, safety testing, security review, representativeness audits, risk assessment, conformity assessment for high risk). | entity_zone = health_abu_dhabi | `UAE-AbuDhabi-DoH-003`, `UAE-AbuDhabi-DoH-004`, `UAE-AbuDhabi-DoH-005`, `UAE-AbuDhabi-DoH-006`, `UAE-AbuDhabi-DoH-007`, `UAE-AbuDhabi-DoH-008`, `UAE-AbuDhabi-DoH-009`, `UAE-AbuDhabi-DoH-010`, `UAE-AbuDhabi-DoH-011`, `UAE-AbuDhabi-DoH-012`, `UAE-AbuDhabi-DoH-013` | binding in some cited sources: UAE-AbuDhabi-DoH (M) |
| H2 | Healthcare entity regulated by Dubai Health Authority: check the DHA AI in Healthcare Policy (independent third party validation, certification, auditable validation statements, regular independent audits). | entity_zone = health_dubai | `UAE-Dubai-025`, `UAE-Dubai-026`, `UAE-Dubai-027`, `UAE-Dubai-028`, `UAE-Dubai-029`, `UAE-Dubai-030` | binding in some cited sources: UAE-Dubai (M) |
| H3 | Determine whether the federal personal data law applies to the entity and the data (Article 2 excludes government data and government entities controlling or processing personal data), then, if it does, check the impact assessment and security testing duties. | data_types includes any of {personal, sensitive_personal, biometric, health, financial} | `UAE-Federal-034`, `UAE-Federal-032`, `UAE-Federal-033`, `UAE-Federal-005`, `UAE-Federal-007` | binding in some cited sources: UAE-Federal (M) |
| H4 | DIFC or ADGM entity: check the DIFC Data Protection Regulations Regulation 10, the Commissioner's Accreditation and Certification Framework, and the ADGM data protection and FSRA guidance that applies. | entity_zone in {difc, adgm} | `UAE-DIFC-ADGM-001`, `UAE-DIFC-ADGM-003`, `UAE-DIFC-ADGM-004`, `UAE-DIFC-ADGM-016`, `UAE-DIFC-ADGM-018`, `UAE-DIFC-ADGM-020`, `UAE-DIFC-ADGM-009`, `UAE-DIFC-ADGM-010`, `UAE-DIFC-ADGM-012`, `UAE-DIFC-ADGM-013`, `UAE-DIFC-ADGM-014` | binding in some cited sources: UAE-DIFC-ADGM (C) |
| H5 | Dubai government entity: check the Dubai AI Ethics Guidelines and self assessment tool, the AI Integration Matrix Framework, and the DESC Information Security Regulation controls on testing and sign off. | entity_zone = dubai_gov | `UAE-Dubai-011`, `UAE-Dubai-015`, `UAE-Dubai-020`, `UAE-Dubai-021`, `UAE-Dubai-022`, `UAE-Dubai-031`, `UAE-Dubai-033`, `UAE-Dubai-034`, `UAE-Dubai-035` | binding in some cited sources: UAE-Dubai (M) |
| H6 | Abu Dhabi government entity (not health) or UAE federal entity: look for entity specific or council instructions; none with AI testing content were found in the public sources searched. | entity_zone in {abu_dhabi_gov, federal_gov} | `UAE-AbuDhabi-Other-001`, `UAE-AbuDhabi-Other-002`, `UAE-Federal-009`, `UAE-Federal-018`, `UAE-Federal-021` | binding in some cited sources: UAE-AbuDhabi-Other (M) |

**How to use it.** Scale depth to the impact tier assigned in A1. Items D7 and D8 apply only to generative or agentic systems and to purchased systems. The checklist concerns testing and assurance; it omits procurement law, data sharing agreements and sector regulation. Test evidence templates (labelled proposals) are in `templates/test_evidence/`.

**Worked example.** `examples/MADOUN_EXAMPLE.md` applies the tool to a hypothetical customs clearance decision support system based on the author's synthetic prototype Madoun. It is not deployed, and it is not used or endorsed by any authority. With the answers given, 16 items apply, 2 do not apply and 11 are UNKNOWN; the file lists what would close each.

---

## 10. Limitations

1. **Language.** UAE and Saudi documents were mostly read in English. Arabic originals were read for some (Section 6.2, `language_read`); fetch tool renderings of Arabic, Chinese, Japanese and Korean text are machine renderings and are flagged. The Korean decree was read in a reference translation that renders one number illegibly.
2. **Documents unavailable or not read.** Canada's Directive, ISO catalogue pages and SDAIA documents rejected the fetch tool on two dates; two files exceeded the size limit; several UAE instruments are referred to publicly but not published. See Appendix B and `docs/DOWNLOAD_LIST.md`.
3. **Second hand reading.** The fetch tool often returns extracted text or summaries. In phase 3 some PDFs were read from the file the tool saved, by local text extraction or by reading rendered page images (49 rows; `access_path`). This is disclosed per row; a reader who wants only text returned by the tool itself can exclude those rows.
4. **Ambiguity in "required".** Status coding applies the protocol. 19 headline test rows are ambiguous. Section 5.5 adds a second, interpretive layer for non binding rows, coded from paraphrases. A "shall" in a policy is coded mandatory for the named entities even where no penalty or enforcement mechanism was seen.
5. **Row counts are not weights.** Counts reflect extraction and document length.
6. **Coding subjectivity.** Test type and stage were coded by AI subagents and not double coded; new phase 3 rows were coded by the agent that found them. Normative force was double coded, but both coders are models of the same family.
7. **Verification limits.** Verification checks rows against sources; it does not check the report narrative. All verifiers are AI subagents; none is a human expert. The research agents tended to grade substantive faults as MINOR; the lead analyst re-graded 14 of them, which is itself a judgement. Error rates are estimates with wide intervals.
8. **Access method disclosure.** Phase 1 used a browser style user agent for some downloads; those verdicts were re verified in phase 2 (Section 2.3). Phase 3 used the EU Publications Office endpoint for EU texts and local reading of files saved by the fetch tool, both recorded per row.
9. **Time.** Status statements are as of 16 October 2026 for items checked in phase 3 and 12 October 2026 otherwise. The DoH Standard revision falls due this month. The `next_review_by` column and a script flag stale rows.
10. **Scope.** The study covers testing provisions, not the whole of AI regulation, and not enforcement. Non public instruments that may bind UAE entities could not be seen. Nothing here is legal advice.

---

## 11. What to double check before relying on this

1. **The UAE cyber security policy rows.** Read sections 1.2, 2 and 3.4 of the National Cyber Security Policy for AI v1.1 yourself and confirm the addressees and the "shall" wording (`UAE-Federal-P3-01`† to `UAE-Federal-P3-08`†). This is the finding most likely to be quoted, and it rests on text extracted from a saved PDF.
2. **Unverified rows.** Download the blocked documents in `docs/DOWNLOAD_LIST.md`, starting with Canada's Directive.
3. **DoH Standard.** Check the DoH site for a revision (the document states October 2026) and for the 2025 DoH AI Policy.
4. **DIFC.** Check whether the June 2026 amendments to Regulation 10 have been enacted.
5. **Korea.** Confirm the compute threshold exponent in the Korean original and what the August 2026 decree changed.
6. **The NIST page name.** The NIST institute page now shows a different centre name (`US-NIST-046`); confirm on nist.gov before quoting it.
7. **Status calls.** Review the ambiguous rows and the disputed normative force rows; they are judgement calls.
8. **Framing of Section 8.** Do not present the gap analysis as a statement of UAE law or policy.
9. **Legal review.** Have a qualified lawyer review anything you plan to rely on for compliance.

---

## Appendix A. Verification

### A.1 Phase 3 (16 October 2026)

| Sample | Rows checked | PASS | MINOR | ERROR | Blocked | Unverifiable | Verifiable | Error rate (Wilson 95%) |
|---|---|---|---|---|---|---|---|---|
| Phase 3 re-check of 175 open rows, as graded by research agents | 175 | 99 | 42 | 1 | 32 | 1 | 142 | 0.7% (0.1 to 3.9) |
| Same rows, re-graded by the lead analyst against the rubric | 175 | 99 | 28 | 15 | 32 | 1 | 142 | 10.6% (6.5 to 16.7) |
| **Fresh random sample (seed 20261016), independent verifiers** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | None% (0.0 to 0.0) |
| New phase 3 rows, independent verifiers | 0 | 0 | 0 | 0 | 0 | 0 | 0 | None% (0.0 to 0.0) |
| **All rows checked by phase 3 independent verifiers** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | None% (0.0 to 0.0) |

**Headline figure.** The fresh random sample is the figure to quote: 0 errors in 0 verifiable rows (None%, Wilson 95% interval 0.0% to 0.0%), with 0 further rows having minor imprecision and 0 blocked. It was drawn from the corrected table, so it estimates the error rate of the table as published. New phase 3 rows: 0 errors in 0 verifiable (None%). Every error found was corrected through `data/verification/phase3/final/` patches before this report was generated.

**The re-check of open rows.** The 175 rows phase 2 had left open are not a random sample: they are the rows that were hardest to read. As graded by the research agents they show 1 errors in 142 verifiable rows (0.7%); re-graded against the rubric, 15 (10.6%, interval 6.5% to 16.7%). The re-graded figure is the honest one; the gap shows that agent graders under-call errors, which is a reason to read every verification figure here as a lower bound.

### A.2 Phase 2 (12 October 2026)

**Design.** Phase 1 checked a seeded random sample of 40 rows plus 5 targeted rows (seed 20261011) and reported 1 error in 32 verifiable rows (3.1%; interval 0.6% to 15.7%). Phase 2 re checked on the standard fetch tool only. Samples are reported separately because they were drawn differently: the cited row sample is not random (it is every row cited in the phase 1 prose and checklist), the fresh sample is a seeded random draw of rows not otherwise checked, targeted rows were chosen for doubt, and the new UAE rows were checked as a full set.

| Sample | Rows checked | PASS | MINOR | ERROR | Blocked | Unverifiable | Verifiable | Error rate (Wilson 95%) |
|---|---|---|---|---|---|---|---|---|
| Rows cited in report prose, brief and checklist (phase 1 citations) | 243 | 106 | 51 | 11 | 46 | 29 | 168 | 6.5% (3.7 to 11.3) |
| Fresh seeded random sample (seed 20261012) | 64 | 30 | 14 | 0 | 6 | 14 | 44 | 0.0% (0.0 to 8.0) |
| Targeted rows | 7 | 4 | 2 | 0 | 0 | 1 | 6 | 0.0% (0.0 to 39.0) |
| New UAE rows added in phase 2 | 75 | 40 | 33 | 2 | 0 | 0 | 75 | 2.7% (0.7 to 9.2) |
| **All rows checked in phase 2** | 389 | 180 | 100 | 13 | 52 | 44 | 293 | 4.4% (2.6 to 7.4) |
| All rows checked, excluding new UAE rows | 314 | 140 | 67 | 11 | 52 | 44 | 218 | 5.0% (2.8 to 8.8) |
| Phase 1 provisional rows (re verified) | 49 | 17 | 10 | 4 | 12 | 6 | 31 | 12.9% (5.1 to 28.9) |

**Coverage of cited rows.** The report prose, brief and checklist cite 268 distinct rows. Of these, 214 were verified in phase 2, 54 are excluded from counts and carry a dagger wherever they appear, and 0 were not rechecked. A test fails if any cited row is neither verified nor marked unverified.

**Combined figure.** Over all 389 rows checked in phase 2, 180 passed, 100 had minor imprecision and 13 had errors; 52 were blocked and 44 unverifiable. The error rate among the 293 verifiable rows is 4.4% (95% interval 2.6% to 7.4%). The cited row sample, which is not random and is weighted to the rows the report relies on, shows 11 errors in 168 verifiable rows (6.5%). The fresh random sample shows 0 errors in 44 (0.0%, interval 0.0% to 8.0%). The new UAE rows show 2 errors in 75 (2.7%).

**Interpretation.** The combined rate is higher than the phase 1 figure. Plausible contributors, which were not tested separately, are that the cited sample is concentrated on the rows the report relies on and that UAE rows read through tool summaries carry version and date errors. The intervals overlap, so the two figures are not clearly different. Errors were corrected through `data/patches.json`. Treat paraphrases and page references as accurate in substance, and check page numbers before quoting. Excluding unverifiable rows could hide errors in those sources; the rate says nothing about them.

**The eight earlier unverifiable rows and UK-009.**

| Row | Final status | Block type | In headline counts | What resolves it |
|---|---|---|---|---|
| `Canada-002`† | UNVERIFIED_BLOCKED | site_rejected | no | Not verified. Download by hand: Treasury Board of Canada Secretariat, 'Directive on Automated Decision-Making' (current version; note the Da |
| `Canada-009`† | UNVERIFIED_BLOCKED | site_rejected | no | Not verified. Download by hand: Treasury Board of Canada Secretariat, 'Directive on Automated Decision-Making' (current version; note the Da |
| `Canada-014`† | UNVERIFIED_BLOCKED | site_rejected | no | Not verified. Download by hand: Treasury Board of Canada Secretariat, 'Directive on Automated Decision-Making' (current version; note the Da |
| `EU-AI-Act-034` | VERIFIED | none | yes |  |
| `EU-AI-Act-044` | VERIFIED | none | yes |  |
| `EU-AI-Act-068` | VERIFIED | none | yes |  |
| `Saudi-008` | VERIFIED_CORRECTED | none | yes | paraphrase misattributes report publishing to the AI System Assessor; internal or external assessor not supported / applied: interpretation_ |
| `Singapore-014` | VERIFIED | none | yes |  |
| `UK-009` | VERIFIED_CORRECTED | none | yes | locator; paraphrase nuance / applied: clause_or_page: Exact heading of the DPIA passage.; requirement_paraphrase: Reflect the Playbook's unc |

Resolved: `EU-AI-Act-034`, `EU-AI-Act-044`, `EU-AI-Act-068`, `Saudi-008`, `Singapore-014`, `UK-009`. Still unverified and excluded: `Canada-002`†, `Canada-009`†, `Canada-014`†.

**Rows excluded from headline counts, by family.**

| Family | Rows | Blocked | Readable but passage not located | Source not read or withdrawn | Other (superseded, portal or secondary only, awaiting check) |
|---|---|---|---|---|---|
| EU AI Act (as amended 2026), Art 50 code, Reg 2026/1755 | 4 | 0 | 0 | 0 | 4 |
| EU GPAI Code of Practice | 4 | 0 | 0 | 0 | 4 |
| EU harmonised standards (JTC 21, EN 18286 citation) | 1 | 0 | 0 | 0 | 1 |
| ISO/IEC (catalogue level) | 1 | 1 | 0 | 0 | 0 |
| US OMB M-25-21 and M-26-04 | 2 | 0 | 0 | 0 | 2 |
| UK (Playbook, ATRS, DSIT, AISI) | 3 | 0 | 0 | 0 | 3 |
| Canada Directive on Automated Decision-Making | 24 | 24 | 0 | 0 | 0 |
| Singapore (AI Verify, Starter Kit, frameworks) | 2 | 0 | 0 | 0 | 2 |
| Japan (Act, plan, guidelines, Digital Agency DS-920, AISI) | 4 | 0 | 0 | 0 | 4 |
| South Korea AI Basic Act and Enforcement Decree | 2 | 0 | 0 | 0 | 2 |
| China (GenAI, algorithm, labelling, GB/T 45654, TC260 guide) | 3 | 0 | 1 | 0 | 2 |
| UAE federal (Charter, Strategy, Guidelines, Ethics, CSC AI security policy, PDPL) | 12 | 0 | 0 | 0 | 12 |
| DIFC and ADGM (Reg 10, Framework, 2026 draft amendments, DP guidance) | 4 | 0 | 0 | 0 | 4 |
| Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies) | 1 | 0 | 0 | 0 | 1 |
| Abu Dhabi DoH (health sector: Standard and Protocol) | 4 | 0 | 0 | 0 | 4 |
| Saudi Arabia (SDAIA, NCA draft, SFDA) | 23 | 7 | 0 | 0 | 16 |

---

## Appendix B. Free resources to download and read

All documents below are free. The complete, row linked list is `docs/DOWNLOAD_LIST.md`; phase 3 agents' lists are in `data/verification/phase3/p3notes_*.md`. In summary:

- **Canada:** the Directive on Automated Decision-Making, https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592 (save the page as PDF and note "Date modified"). All 24 Canada rows depend on it.
- **ISO/IEC:** the free catalogue pages on iso.org for ISO/IEC 42001, 23894, 42005, 42006, TS 42119-2, TR 29119-11, TR 24027, 24029-2, 25059, TS 12791 and 27090 (abstract and status only; nothing needs buying).
- **Saudi Arabia (sdaia.gov.sa):** Generative AI Guidelines for the Public, AI Adoption Framework, National AI Risk Management Framework executive summary and full text, Generative AI Guidelines for Government, AI Ethics Principles 2025 file; the NCA draft in Arabic; laws.boe.gov.sa search for AI.
- **UAE:** the Central Bank guidance note on AI and machine learning (February 2026); the DFSA letter on AI risk management (June 2026); the agentic AI guide for government entities; the National AI Strategy 2031 PDF (over the size limit); the UAE Information Assurance Standard appendix E.2, if obtainable.
- **Korea and China:** the Korean original of the current Enforcement Decree (law.go.kr); China's AI Safety Governance Framework 2.0 PDF (over the size limit); GB 45438-2025 from the national standards portal.
- **Singapore and UK:** IMDA Starter Kit for Testing Agentic Systems (October 2026); IMDA press release of 14 October 2026; bills.parliament.uk for AI private members' bills.

---

## Appendix C. Files

| File | Contents |
|---|---|
| `README.md` | What is documented, interpreted and open |
| `docs/REPORT.md` | This report (generated) |
| `docs/EXECUTIVE_BRIEF.md` | Two page brief (generated) |
| `docs/READING_LIST.md` | Short reading list |
| `docs/PROTOCOL.md` | Research protocol |
| `docs/DOWNLOAD_LIST.md` | Documents to download by hand, per unverified row |
| `docs/UAE_COVERAGE.md` | Per source and per search record for the UAE work |
| `docs/TIME_SENSITIVE.md` | Time sensitive items with locators |
| `docs/LICENSING.md` | Licence proposal and library and data licence record |
| `data/evidence_table.csv` | 522 rows with verification status and review dates |
| `data/checklist.yaml`, `data/answers_schema.yaml` | The checklist and the questions the tool asks |
| `data/time_sensitive.csv`, `data/uae_search_log.csv`, `data/uae_sources.csv` | Status items (phases 2 and 3) and phase 2 UAE search records |
| `data/verification/phase3/` | Phase 3 rules, inputs, agent results, notes, patches, re-grades, access labels and the final independent check (`final/`) |
| `data/coding/` | Normative force codebook, both coders' files, merged codes and agreement |
| `data/verification/` | Raw verification results and rules |
| `src/ikhtibar/` | Build scripts, engine, command line tool, staleness script |
| `templates/test_evidence/` | Evidence templates per test type (proposals) |
| `examples/MADOUN_EXAMPLE.md` | Hypothetical worked example |
| `docs/coverage_matrix.csv`, `docs/summary_by_family.csv`, `docs/summary_by_test_type.csv`, `docs/assurance_checklist.csv` | Generated tables |

## Appendix D. Libraries and data licences

The code uses PyYAML (MIT licence) and the Python standard library. Tests use `unittest` and optionally `pytest` (MIT). The secrets scan uses a local script, and `detect-secrets` (Apache 2.0) was run as an extra check. No dataset other than the cited public sources is used; the table holds paraphrases and short attributed quotes only. See `docs/LICENSING.md`.
