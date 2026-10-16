# Ikhtibar: Testing AI Systems Before Deployment. Required, Recommended, or Merely Described?

**A comparative evidence review, with a gap analysis for UAE public sector deployment**

Prepared for Huda Mueen. Version 2.0 (phase 2), 12 October 2026. All retrieval dates are 2026-10-12 unless a row says otherwise. This file is generated from the data files by `python -m ikhtibar.build_docs`; do not edit it by hand.

**This is research analysis, not legal advice.** It has not been peer reviewed. It was produced with AI research subagents and independent AI verification passes (Appendix A). Statements about what a document says trace to a row in `data/evidence_table.csv`. Statements that are interpretation appear in paragraphs marked **Interpretation**. A dagger (†) after a row identifier means the row is excluded from every headline count: it could not be verified (source blocked, passage not located, or source not read), or it rests on a portal summary or a secondary report only.

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

1. **Most testing content in the evidence base is not binding.** Of 246 headline test provisions, 73 (30%) are mandatory or conditional, 154 (63%) are voluntary or guidance, and 19 (8%) are ambiguous. Phase 1 reported 73 / 142 / 19 of 234. The two sets differ because phase 2 removed rows that could not be verified without a workaround (all Canada test rows and most EU Act rows beyond the first part of the text) and added UAE rows. The binding rows now come from: EU AI Act (as amended 2026) (26), Abu Dhabi DoH (health sector) (11), China (GenAI, algorithm, labelling, GB/T 45654) (10), DIFC and ADGM (Reg 10, Framework, DP guidance) (8), Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies) (7), UAE federal (Charter, Strategy, Guidelines, Ethics, Cyber policy, PDPL) (4), US OMB M-25-21 (3), South Korea AI Basic Act (3), UK (Playbook, ATRS, DSIT, AISI) (1).
2. **Where testing is binding, the text mostly requires that it happens and is documented, not how.** The EU Act requires testing of high risk systems against metrics and thresholds the provider defines (`EU-AI-Act-016`, `EU-AI-Act-018`). OMB M-25-21 requires pre deployment testing plans for high impact AI (`US-OMB-003`). The Abu Dhabi DoH Standard requires validation against "established performance benchmarks" and does not name them (`UAE-AbuDhabi-DoH-003`).
3. **Independent testing is binding in a few places and mostly for health or certified processing.** The Dubai Health Authority AI in Healthcare Policy requires independent third party validation and independent audits of AI functionality (`UAE-Dubai-025`, `UAE-Dubai-026`). DIFC Regulation 10 makes certification a precondition for commercial high risk processing, and the Commissioner has published an accreditation and certification framework (`UAE-DIFC-ADGM-004`, `UAE-DIFC-ADGM-018`). The DoH Standard provides for DoH audits (`UAE-AbuDhabi-DoH-013`). Independent evaluation of frontier models appears only in voluntary instruments (`UK-024`).
4. **Binding red teaming is narrow.** There are 24 headline red teaming and dangerous capability rows and 3 of them are mandatory or conditional: `EU-AI-Act-063`, `EU-AI-Act-068`, `EU-AI-Act-071`. In the verified rows these are EU duties for general purpose models with systemic risk (model evaluation including adversarial testing) and the AI Office power to evaluate such models. Binding red teaming rows that are not yet verified, and so excluded: `EU-AI-Act-P3-20`†, `UAE-Federal-P3-04`†.
5. **Human oversight is specified as design, not as something to test.** Headline rows with human oversight validation as primary test type: 1 (`UAE-DIFC-ADGM-015` (guidance)). Oversight design duties appear as enabling provisions (`EU-AI-Act-026`, `UAE-Federal-008`).
6. **In the UAE and Gulf sources retrieved, binding testing text is sector or zone specific.** The strongest are the Abu Dhabi DoH Responsible AI Standard (`UAE-AbuDhabi-DoH-003` to `UAE-AbuDhabi-DoH-013`), the Dubai Health Authority policy (`UAE-Dubai-025` to `UAE-Dubai-029`) and DIFC Regulation 10. Federal documents retrieved are principles and guidelines with testing language but without a stated binding force (`UAE-Federal-009`, `UAE-Federal-018`, `UAE-Federal-021`). The federal personal data law excludes government data and government entities from its scope (`UAE-Federal-034`), so its impact assessment and security testing duties (`UAE-Federal-005`, `UAE-Federal-007`) may not reach a government deployer. The Dubai Information Security Regulation is mandatory for Dubai government entities and requires security testing and sign off, but it is not specific to AI (`UAE-Dubai-033` to `UAE-Dubai-035`).
7. **Verification.** Phase 2 checked 389 rows against sources by independent subagents using only the standard fetch tool: 13 errors among 293 verifiable rows (4.4%, 95% interval 2.6% to 7.4%). Phase 1 reported 1 error in 32 verifiable rows (3.1%). The fresh random sample alone had 0 errors in 44 verifiable rows. About 38.6% of verifiable rows had some imprecision (MINOR or ERROR). 52 checked rows were blocked and 44 were readable but could not be located; these are excluded. See Appendix A.
8. **Access method.** Phase 1 verdicts that rested on a browser style user agent or other workaround are provisional. 49 such rows were re verified in phase 2 using only the standard fetch tool (Section 2.3).

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

---

## 3. Evidence base

| Family | Rows | Headline test rows | Primary text read | Catalogue only | Unofficial or machine translation | Unverified or unverifiable |
|---|---|---|---|---|---|---|
| EU AI Act (as amended 2026) | 78 | 28 | 78 | 0 | 0 | 4 |
| EU GPAI Code of Practice | 13 | 7 | 13 | 0 | 0 | 4 |
| EU harmonised standards (JTC 21) | 9 | 1 | 9 | 0 | 0 | 1 |
| ISO/IEC (catalogue level) | 19 | 12 | 0 | 19 | 0 | 1 |
| NIST (AI RMF, Playbook, 600-1, 800-2 draft) | 46 | 36 | 46 | 0 | 0 | 0 |
| US OMB M-25-21 | 9 | 3 | 9 | 0 | 0 | 2 |
| UK (Playbook, ATRS, DSIT, AISI) | 36 | 19 | 36 | 0 | 0 | 3 |
| Canada Directive on Automated Decision-Making | 24 | 0 | 24 | 0 | 0 | 24 |
| Singapore (AI Verify, Starter Kit, frameworks) | 38 | 31 | 38 | 0 | 0 | 2 |
| Japan (Act, plan, guidelines, AISI) | 28 | 13 | 28 | 0 | 0 | 4 |
| South Korea AI Basic Act | 19 | 5 | 16 | 0 | 3 | 2 |
| China (GenAI, algorithm, labelling, GB/T 45654) | 33 | 15 | 13 | 1 | 18 | 3 |
| UAE federal (Charter, Strategy, Guidelines, Ethics, Cyber policy, PDPL) | 42 | 15 | 39 | 3 | 0 | 12 |
| DIFC and ADGM (Reg 10, Framework, DP guidance) | 29 | 13 | 29 | 0 | 0 | 4 |
| Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies) | 40 | 20 | 39 | 0 | 0 | 1 |
| Abu Dhabi DoH (health sector) | 18 | 13 | 18 | 0 | 0 | 4 |
| Abu Dhabi AI and Advanced Technology Council law | 2 | 0 | 2 | 0 | 0 | 0 |
| Saudi Arabia (SDAIA, NCA draft) | 39 | 15 | 38 | 0 | 0 | 23 |
| **Total** | **522** | **246** | **475** | **23** | **21** | **94** |

**Source says (about access).** Some sources could not be read. Rows are unverified when the issuing site rejected the standard fetch tool (Canada Treasury Board Secretariat, parts of SDAIA and NCA), when a permission timeout stopped a fetch, when the fetch tool truncated a very long document (the EUR-Lex consolidated Act is readable only to about Article 38), or when a passage could not be located. Block types among the unverified rows: none: 61, site_rejected: 32, truncated_or_unreadable: 1.

| Family | Rows | Blocked | Readable but passage not located | Source not read or withdrawn |
|---|---|---|---|---|
| EU AI Act (as amended 2026) | 4 | 0 | 0 | 0 |
| EU GPAI Code of Practice | 4 | 0 | 0 | 0 |
| EU harmonised standards (JTC 21) | 1 | 0 | 0 | 0 |
| ISO/IEC (catalogue level) | 1 | 1 | 0 | 0 |
| US OMB M-25-21 | 2 | 0 | 0 | 0 |
| UK (Playbook, ATRS, DSIT, AISI) | 3 | 0 | 0 | 0 |
| Canada Directive on Automated Decision-Making | 24 | 24 | 0 | 0 |
| Singapore (AI Verify, Starter Kit, frameworks) | 2 | 0 | 0 | 0 |
| Japan (Act, plan, guidelines, AISI) | 4 | 0 | 0 | 0 |
| South Korea AI Basic Act | 2 | 0 | 0 | 0 |
| China (GenAI, algorithm, labelling, GB/T 45654) | 3 | 0 | 1 | 0 |
| UAE federal (Charter, Strategy, Guidelines, Ethics, Cyber policy, PDPL) | 12 | 0 | 0 | 0 |
| DIFC and ADGM (Reg 10, Framework, DP guidance) | 4 | 0 | 0 | 0 |
| Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies) | 1 | 0 | 0 | 0 |
| Abu Dhabi DoH (health sector) | 4 | 0 | 0 | 0 |
| Saudi Arabia (SDAIA, NCA draft) | 23 | 7 | 0 | 0 |

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
| EU AI Act (as amended 2026) | 28 | 0 | 26 | 2 | 0 | 0 | 26 of 28 | 3 |
| EU GPAI Code of Practice | 7 | 0 | 0 | 7 | 0 | 0 | 0 of 7 | 2 |
| EU harmonised standards (JTC 21) | 1 | 0 | 0 | 1 | 0 | 0 | 0 of 1 | 0 |
| ISO/IEC (catalogue level) | 12 | 0 | 0 | 1 | 11 | 0 | 0 of 12 | 0 |
| NIST (AI RMF, Playbook, 600-1, 800-2 draft) | 36 | 0 | 0 | 1 | 35 | 0 | 0 of 36 | 0 |
| US OMB M-25-21 | 3 | 0 | 3 | 0 | 0 | 0 | 3 of 3 | 0 |
| UK (Playbook, ATRS, DSIT, AISI) | 19 | 0 | 1 | 5 | 9 | 4 | 1 of 19 | 3 |
| Canada Directive on Automated Decision-Making | 0 | 0 | 0 | 0 | 0 | 0 | 0 of 0 | 12 |
| Singapore (AI Verify, Starter Kit, frameworks) | 31 | 0 | 0 | 12 | 18 | 1 | 0 of 31 | 2 |
| Japan (Act, plan, guidelines, AISI) | 13 | 0 | 0 | 0 | 13 | 0 | 0 of 13 | 2 |
| South Korea AI Basic Act | 5 | 0 | 3 | 2 | 0 | 0 | 3 of 5 | 1 |
| China (GenAI, algorithm, labelling, GB/T 45654) | 15 | 5 | 5 | 5 | 0 | 0 | 10 of 15 | 2 |
| UAE federal (Charter, Strategy, Guidelines, Ethics, Cyber policy, PDPL) | 15 | 1 | 3 | 0 | 10 | 1 | 4 of 15 | 9 |
| DIFC and ADGM (Reg 10, Framework, DP guidance) | 13 | 0 | 8 | 0 | 4 | 1 | 8 of 13 | 3 |
| Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies) | 20 | 5 | 2 | 1 | 11 | 1 | 7 of 20 | 0 |
| Abu Dhabi DoH (health sector) | 13 | 8 | 3 | 0 | 0 | 2 | 11 of 13 | 4 |
| Saudi Arabia (SDAIA, NCA draft) | 15 | 0 | 0 | 0 | 6 | 9 | 0 of 15 | 22 |
| **All** | **246** | **19** | **54** | **37** | **117** | **19** | **73 of 246** | **65** |

**Source says (selected, verified rows).**

- **EU AI Act.** High risk systems must be tested to find the most appropriate risk management measures and to ensure consistent performance (`EU-AI-Act-016`), at appropriate points in development and in any event before placing on the market, against pre defined metrics and probabilistic thresholds (`EU-AI-Act-018`). Accuracy, robustness and cybersecurity are required (`EU-AI-Act-028`, `EU-AI-Act-029`, `EU-AI-Act-030`). Testing procedures may include real world testing (`EU-AI-Act-017`). Public bodies deploying certain Annex III systems must assess fundamental rights impact before first use (`EU-AI-Act-036`). The Act reaches providers established outside the Union (`EU-AI-Act-009`). The Commission announced that the 2026 amendment entered into force on 27 July 2026 and moved Annex III obligations to 2 December 2027 (`EU-AI-Act-005`). The conformity assessment routes, general purpose model rows, real world testing procedure, post market monitoring and the operative application dates sit beyond the part of the Official Journal text the fetch tool returned and are unverified (see Section 7).
- **EU Code of Practice and standards.** The Code of Practice is a voluntary route to demonstrate compliance for general purpose models; its rows could not be verified in phase 2 because the document host blocked the standard fetch (rows marked †). Standards rows from the JTC 21 feed show draft or enquiry stages (`EU-Standards-002`, `EU-Standards-005`).
- **Canada.** No Canadian row is in the headline counts. The Treasury Board site rejected the standard fetch, so 24 of the 24 Canada rows are unverified. The Directive text and the rows from phase 1 remain in the table for reference and are marked †.
- **United States.** NIST AI RMF 1.0, its Generative AI Profile and the AI 800-2 draft are not binding (all but one NIST headline row are guidance). OMB M-25-21 is binding on federal agencies for high impact AI: pre deployment testing plans (`US-OMB-003`), a documented impact assessment (`US-OMB-004`) and ongoing testing (`US-OMB-006`).
- **United Kingdom.** No statutory pre deployment testing duty was found in the primary texts read. The AI Playbook is guidance and uses "must" in places (`UK-004`, ambiguous). The Algorithmic Transparency Recording Standard is mandatory for in scope central government bodies (`UK-014`, `UK-015`) but asks for evaluation to be described rather than performed (`UK-018`). AI Security Institute pre and post deployment evaluation is coded voluntary (`UK-024`); the Seoul frontier commitments are voluntary (`UK-029` to `UK-031`).
- **Singapore.** The AI Verify Testing Framework and related tools are voluntary; the Starter Kit for testing LLM applications and the generative and agentic frameworks are guidance. Singapore contributes the most detailed non binding testing guidance in the table.
- **Japan.** The AI Promotion Act and guidelines contain no testing mandate in the rows read; testing appears as guidance, for example red teaming before release (`Japan-020`) from the Japan AI Safety Institute.
- **South Korea.** The AI Basic Act imposes safety duties above a compute threshold set by decree (`Korea-005`) and duties on high impact AI (`Korea-007`); verification, certification and fundamental rights impact assessment are voluntary ("should endeavor") (`Korea-003`, `Korea-008`). The decree rows rest on secondary sources and are unverified (`Korea-013` to `Korea-016`).
- **China.** Generative AI providers must sample check annotation quality (`China-003`) and periodically review algorithms (`China-009`); labelling is mandatory (`China-017`). GB/T 45654-2025 supplies concrete test banks but is a voluntary type standard (`China-024`, `China-025`).
- **ISO/IEC.** Entries are catalogue level only (`ISO-IEC-009`, `ISO-IEC-015`); clause content was not read.
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

### 5.5 Source conflicts and status volatility

Conflicts are recorded in the `conflict_flag` column of the table. In summary:

- **EU timeline.** Commentary from before July 2026 shows 2 August 2026 for Annex III high risk requirements; the Commission pages read show 2 December 2027 (`EU-AI-Act-004`, `EU-AI-Act-005`). The operative Article 113 text was not seen (Section 7).
- **EU standards status.** The Commission standardisation page treats prEN 18286 as a draft entering enquiry, while the JTC 21 data feed lists EN 18286:2026 as published (`EU-Standards-002`).
- **NIST.** NIST states that AI RMF 1.0 is being revised and AI 800-2 is an initial public draft.
- **UK.** The AI Playbook uses "must" in guidance (`UK-004`).
- **Korea.** Two secondary sources disagree on the grace period and thresholds (`Korea-016`).
- **DIFC.** The consolidated cover says in force 1 September 2023; the official page says enacted on that date; DIFC news announced the amendment on 7 September 2023 (`UAE-DIFC-ADGM-001`).
- **DHA.** The policy header carries inconsistent issue and effective dates, and its stated revision date of 1 July 2026 has passed, so a newer version may exist (`UAE-Dubai-025`, `UAE-Dubai-027`).
- **Dubai ethics guidelines.** The suspension of the external audit guideline appears in both the English v1.11 PDF and the Arabic edition (`UAE-Dubai-018`); a changelog date in the extraction was garbled.
- **Saudi.** The SDAIA Ethics Principles read are version 1.0 of September 2023 on the portal host; a 2025 edition and a draft label could not be read (Section 7).

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
| UAE National Cyber Security Policy for AI (portal summary and Arabic wording) | UAE federal | Comprehensive testing and validation for reliability; secure development and testing. The full PDF was blocked; the portal text does not state binding force. | ambiguous | `UAE-Federal-014`† to `UAE-Federal-017`† |
| Federal Decree Law No. 45 of 2021 (PDPL) | UAE federal, personal data | Impact assessment before high risk processing; testing of security measures; right to human review of automated decisions; Article 2 excludes government data and government entities. | conditional / mandatory | `UAE-Federal-005` to `UAE-Federal-008`, `UAE-Federal-032` to `UAE-Federal-034` |
| Abu Dhabi Law No. 3 of 2024 (AI and Advanced Technology Council) | Abu Dhabi | The Council sets conditions and standards for AI investment and research; relevant entities must implement the Council's decisions. No testing content. | ambiguous / mandatory | `UAE-AbuDhabi-Other-001`, `UAE-AbuDhabi-Other-002` |
| DoH Abu Dhabi Policy on Use of AI in the Healthcare Sector (version 0.9, April 2018) | Abu Dhabi health sector | "Expects" in one place and "must comply" in another. | ambiguous | `UAE-AbuDhabi-DoH-001`, `UAE-AbuDhabi-DoH-002` |
| DoH Abu Dhabi Responsible AI Standard V1 (October 2025) | Abu Dhabi health sector | Mandatory validation against benchmarks, testing across diverse data, safety testing and failure mode analysis, code review and vulnerability scanning, representativeness audits, risk assessment, documented evidence, internal and DoH audits. Conditional: conformity assessment for high risk systems, no deployment at very high residual risk. | mandatory / conditional | `UAE-AbuDhabi-DoH-003` to `UAE-AbuDhabi-DoH-014` |
| DHA Artificial Intelligence in the Healthcare Policy (HISHD/PP-09) | Dubai health sector | Independent third party validation, independent audits of AI functionality, certification from recognised bodies, performance monitoring against training results, auditable validation statements. | mandatory | `UAE-Dubai-025` to `UAE-Dubai-030` |
| Dubai AI Ethics Guidelines (English and Arabic editions), Ethics Toolkit and Self Assessment Tool | Dubai | Bias testing, discrimination impact assessment, quality checks as stringent as for a human, external audit for critical decisions (marked suspended in the versions read because no mechanism existed). The Executive Council reportedly advised all public entities to use the toolkit. | guidance / voluntary / ambiguous | `UAE-Dubai-001` to `UAE-Dubai-006`, `UAE-Dubai-011` to `UAE-Dubai-024` |
| Dubai AI Integration Matrix Framework (Dubai Digital Authority) | Dubai government | Quality assurance protocols, ethical compliance validation, pilots. | guidance / ambiguous | `UAE-Dubai-007` to `UAE-Dubai-009`, `UAE-Dubai-031`, `UAE-Dubai-032` |
| Dubai Information Security Regulation v2.0 (DESC) | Dubai government entities | Security testing during development, technical reviews and vulnerability tests, security sign off. Mandatory but not AI specific. | mandatory | `UAE-Dubai-033` to `UAE-Dubai-035` |
| Dubai Law No. 9 of 2023 (autonomous vehicles) | Dubai | Technical inspection as a condition of licence; RTA approval for updates to the driving system. | conditional | `UAE-Dubai-036`, `UAE-Dubai-037` |
| Dubai Department of Finance and Dubai Culture AI policies | Dubai entities | Commitments to risk assessment, monitoring and internal audit of their own AI. | ambiguous | `UAE-Dubai-038` to `UAE-Dubai-040` |
| DIFC Data Protection Regulations, Consolidated Version No. 2, Regulation 10 | DIFC | High risk processing by autonomous or semi autonomous systems for commercial purposes needs audit and certification; an Autonomous Systems Officer; accountability and bias mitigation. | conditional | `UAE-DIFC-ADGM-001` to `UAE-DIFC-ADGM-005`, `UAE-DIFC-ADGM-016` |
| DIFC Commissioner guidance, Accreditation and Certification Framework and FAQs | DIFC | Certification application to an accredited certification body; criteria for those bodies; assessment of governance, risk choice, bias and transparency. Each Framework page says it is informational and may be incomplete. | conditional / voluntary / guidance | `UAE-DIFC-ADGM-017` to `UAE-DIFC-ADGM-025` |
| ADGM data protection and FSRA guidance | ADGM | Impact assessment before high risk processing; automated decision guidance; digital investment management guidance on testing. | conditional / guidance | `UAE-DIFC-ADGM-006` to `UAE-DIFC-ADGM-015` |
| SDAIA AI Ethics Principles (version 1.0, September 2023, portal host) | Saudi Arabia | Robustness testing, fairness metrics, privacy leakage testing, user acceptance testing, third party due diligence, conformity assessment for high risk systems. Scope says it applies to all AI stakeholders; the compliance mechanism is optional registration. | ambiguous | `Saudi-001` to `Saudi-010` |
| SDAIA Generative AI Guidelines, AI Adoption Framework, National AI Risk Management Framework | Saudi Arabia | Blocked or secondary only; rows are unverified. | guidance | `Saudi-011`† to `Saudi-017`† |
| NCA AI Cybersecurity Guidelines (draft, AICG-1:2026) | Saudi Arabia | AI penetration testing, red teaming, validating human override. Draft; consultation closed 5 August 2026; binding force not stated. Rows rest on a document read through OCR and are unverified. | guidance | `Saudi-018` to `Saudi-023` |

**Source says (selected details).**

- **DoH Standard.** It applies to DoH and licensed healthcare entities developing, procuring or deploying AI; it states a revision date of October 2026 (Section 7). DoH states it will conduct periodic audits (`UAE-AbuDhabi-DoH-013`).
- **DHA policy.** Independent third party validation and independent audits of AI functionality are mandatory for healthcare AI in Dubai (`UAE-Dubai-025`, `UAE-Dubai-026`). The policy shows conflicting effective dates and a revision date that has passed.
- **DIFC Regulation 10.** Commercial high risk processing needs certification under the Commissioner's framework (`UAE-DIFC-ADGM-004`, `UAE-DIFC-ADGM-018`). The Framework carries a notice that it is informational only and that its implementation timeline is at the Commissioner's discretion; this conflicts with wording that certification is required (conflict flag on `UAE-DIFC-ADGM-018`).
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

- A UAE federal binding rule or technical standard for testing AI systems in government.
- UAE PDPL Executive Regulations.
- A TDRA specific AI guideline with testing content.
- A Dubai government wide mandatory AI testing or certification instrument other than the Information Security Regulation (not AI specific) and the DHA policy (health only). The Universal Blueprint for AI was found only in summaries.
- An external audit mechanism replacing the suspended Dubai guideline.
- An Abu Dhabi government wide AI policy or standard with testing content (the Council law was found; it has none).
- The DoH "AI Policy Standard" and "AI Risk Management" documents that the Standard cites; DoH listing pages could not be opened.
- ADGM AI specific guidance beyond data protection and the FSRA digital investment note.
- Federal leads found only in secondary sources and therefore not evidence: reports of a National AI Test and Validation Lab, a Federal Authority for AI and Data, a guide on leading generative AI applications and an agentic AI guide. They are listed in `docs/UAE_COVERAGE.md` as leads.

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

**EU Omnibus (Regulation (EU) 2026/1744).** *Source says:* identity, signature date 8 July 2026, Official Journal date 24 July 2026 and entry into force 27 July 2026 are confirmed from EUR-Lex metadata and the Official Journal headers; the Article 57(1) sandbox date of 2 August 2027 is confirmed; no corrigendum or further amendment was found in metadata. The Annex III date (2 December 2027) and the Annex I date (2 August 2028) are confirmed only at recital 40 and agree with Commission pages; the operative Article 113 text was not seen because the fetch tool returned the Official Journal only to about page 29 of 41. The Article 111(2) date, Articles 111(3) and (4), Article 50(2), Article 5 application dates and Article 101 are not confirmed. *Interpretation:* the headline EU dates are probably right but are not confirmed from operative text; rows `EU-AI-Act-001` to `EU-AI-Act-003`, `EU-AI-Act-006`, `EU-AI-Act-007` and `EU-AI-Act-008` stay unverified.

**DoH Responsible AI Standard.** *Source says:* reference DoH/ST/DDGO/RAI/V1/2025, publication and effective date October 2025, revision date October 2026 with a one year revision period, owner the Data and Digital Governance Office. The PDF still resolves at the recorded address and shows V1. Whether a revision, addendum or replacement exists is open because the DoH listing pages could not be opened (permission timeout, not a site block). The two documents the Standard cites (AI Policy Standard, June 2025; AI Risk Management, July 2025) exist as references only and were not located. The 2018 policy is version 0.9, dated 30 April 2018; its current status is open.

**DIFC Regulation 10.** *Source says:* the official consolidated Regulations, Version No. 2, show "In force on 1 September 2023". The Commissioner has issued Regulation 10 materials: an Accreditation and Certification Framework, guidance and FAQs. Regulation 10.3.3 makes certification a precondition for commercial high risk processing. This replaces the first round finding that no such scheme was found. Open: whether amendments after Version No. 2 exist (the legal database was not read), and Framework sections 2.2 to 4, which were read only partly. Conflict: the Framework's informational notice versus its wording that certification is required.

**Saudi drafts.** *Source says:* the SDAIA AI Ethics Principles read on the portal host are version 1.0 of September 2023 with no draft label; the 2025 edition and the page that calls it a draft were blocked by the site. The NCA AI Cybersecurity document is a draft (AICG-1:2026); the consultation was open from 5 July and closed after 5 August 2026; no final issue was seen. The National AI Risk Management Framework was launched on 14 July 2026 according to the Saudi Press Agency; the framework document itself was not read, and an earlier "April 2026" date is not supported. The Adoption Framework and Generative AI guidelines are blocked. *Interpretation:* none of the Saudi instruments can be called final from the retrieved evidence.

---

## 8. Gap analysis for UAE government deployment

**Framing.** These are gaps in the evidence base retrieved, measured against what other frameworks in this table contain. They are not claims about what the UAE does or does not require. A UAE government entity may be subject to internal, sectoral or non public instruments that were not found.

**G1. No federal binding test method in the instruments retrieved.**
*Source says:* the Charter states a safety principle (`UAE-Federal-001`). The Adoption Guideline in Government Services describes evaluation against acceptance criteria and monitoring (`UAE-Federal-009`, `UAE-Federal-011`) and the Ethics Guidelines suggest bias testing and external audit for critical decisions (`UAE-Federal-018`, `UAE-Federal-021`), in "should" language. The Cabinet release ties adoption phases to performance and impact assessments without a method (`UAE-Federal-004`). Comparators that bind government bodies are OMB M-25-21 (`US-OMB-003`, `US-OMB-004`) and the DoH Standard for health (`UAE-AbuDhabi-DoH-003`).
*Interpretation:* an entity in a federal setting would find guidance on acceptance criteria and testing but not a shared binding procedure. Whether the Adoption Guideline binds a particular entity is not stated in the text read; the entity's governance office would need to say.

**G2. Binding testing text is sector, zone or data specific.**
*Source says:* mandatory text covers Abu Dhabi health (`UAE-AbuDhabi-DoH-003` to `UAE-AbuDhabi-DoH-013`), Dubai health (`UAE-Dubai-025`, `UAE-Dubai-026`), commercial high risk processing in DIFC (`UAE-DIFC-ADGM-004`), personal data (`UAE-Federal-005`, `UAE-Federal-007`) and security testing in Dubai government (`UAE-Dubai-034`).
*Interpretation:* for non health public sector uses such as eligibility, licensing, customs or inspection, the retrieved sources contain no AI specific binding equivalent. A cross sector baseline, if one exists, was not found.

**G3. Benchmarks and thresholds are not defined.**
*Source says:* the DoH Standard requires validation against "established performance benchmarks" (`UAE-AbuDhabi-DoH-003`); the federal Ethics Guidelines say a fallback plan should include thresholds for acceptable results (`UAE-Federal-023`). The EU Act leaves metrics to the provider (`EU-AI-Act-018`); Singapore's Starter Kit and NIST describe how to set acceptance criteria (`Singapore-009`, `US-NIST-026`).
*Interpretation:* the gap is shared with other binding regimes. A procuring entity would need to define pass criteria itself.

**G4. Independent assurance is contingent.**
*Source says:* Dubai's external audit guideline is marked suspended in the versions read (`UAE-Dubai-005`, `UAE-Dubai-018`); the federal Ethics Guidelines suggest external audit (`UAE-Federal-021`); the Strategy plans a seal without criteria (`UAE-Federal-003`); the Dubai AI Seal classifies businesses rather than testing systems (`UAE-Dubai-010`). Binding independent assurance exists for Dubai health (`UAE-Dubai-025`) and for DIFC certification (`UAE-DIFC-ADGM-018`).
*Interpretation:* independent testing capacity outside those two is an open question, in most jurisdictions here and not only in the UAE.

**G5. Generative, agentic and frontier style evaluation.**
*Source says:* no UAE row retrieved covers red teaming or capability evaluation. A draft Saudi guideline recommends it (rows † unverified). Comparators: `US-NIST-028`, `Japan-020`, `Singapore-007`, `UK-024`.
*Interpretation:* the Cabinet announcement of a move toward agentic AI in federal services (`UAE-Federal-004`) contrasts with the absence of retrieved test guidance for agentic systems.

**G6. Vendor and black box systems.**
*Source says:* OMB requires alternative test methods when internals are inaccessible (`US-OMB-003`). The DoH Standard requires secure code review and vulnerability scanning for proprietary and third party software (`UAE-AbuDhabi-DoH-007`).
*Interpretation:* no general procurement stage testing requirement for AI was retrieved for UAE government buyers.

**G7. Language and local context performance.**
*Source says:* no extracted test row requires language specific performance testing, such as Arabic dialects or bilingual use. Adjacent: dataset diversity (`UAE-AbuDhabi-DoH-008`), generalisation for under represented groups (`UAE-Dubai-002`), representativeness of training data (`UAE-Federal-028`).
*Interpretation:* an absence in this table, not a claim that no source addresses it. For a bilingual public service it is a natural item for a test plan (checklist C2, D1).

**G8. Post deployment monitoring outside health.**
*Source says:* binding monitoring appears in OMB (`US-OMB-006`), the DoH Standard (`UAE-AbuDhabi-DoH-005`) and the DHA policy (`UAE-Dubai-028`). Federal guidance mentions monitoring (`UAE-Federal-011`). Federal law retrieved contains a periodic review of an impact assessment only (`UAE-Federal-006`).
*Interpretation:* an incident or drift reporting duty for non health government AI was not found.

**G9. Human oversight is required in places but its validation is not.**
*Source says:* the table has 1 oversight validation test row(s): `UAE-DIFC-ADGM-015` (guidance). Federal law gives a right to human review (`UAE-Federal-008`); the EU Act specifies oversight design (`EU-AI-Act-026`).
*Interpretation:* none of the frameworks read requires evidence that oversight works under realistic load or automation bias.

**G10. The data protection law may not reach government deployers.**
*Source says:* Federal Decree Law 45 of 2021 does not apply to government data or government entities that control or process personal data (`UAE-Federal-034`).
*Interpretation:* the impact assessment and security testing duties in that law (`UAE-Federal-005`, `UAE-Federal-007`) cannot be assumed to apply to a federal entity. The checklist treats them as conditional on entity type.

**G11. Gaps in the evidence itself.** Blocked or unread: Canada's Directive and tools, much of SDAIA and NCA, the National Cyber Security Policy for AI PDF, the EU Official Journal pages 30 to 41, ISO clause text, the Korean decree, DoH listing pages, and Arabic originals of several documents. See Appendix B.

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

1. **Language.** UAE and Saudi documents were mostly read in English. Arabic wording was obtained for some documents (Section 6.2); machine renderings are flagged. Chinese original rows rest on the original or on unofficial translation as the `language_read` column states.
2. **Documents unavailable or not read.** See Appendix B and `docs/DOWNLOAD_LIST.md`.
3. **Second hand reading.** The fetch tool often returns extracted text or summaries. Clause text is partly second hand; verification is the main check.
4. **Ambiguity in "required".** Status coding is an application of the protocol. 19 headline test rows are ambiguous.
5. **Row counts are not weights.** Counts reflect extraction and document length.
6. **Coding subjectivity.** Test type coding was done by AI subagents and not double coded.
7. **Verification limits.** Verification checks rows against sources; it does not check the report narrative. 0 rows were not rechecked in phase 2. The error rate is an estimate with a wide interval.
8. **Access method disclosure.** Phase 1 verification used a browser style user agent for some downloads and a research subagent used one for a data feed. The phase 1 verdicts that depended on this were treated as provisional and re verified (Section 2.3). They are listed above by final status.
9. **Time.** Status statements are as of 2026-10-12. Drafts and revisions may already be out of date. A column `next_review_by` and a script flag stale rows.
10. **Scope.** The study covers testing provisions, not the whole of AI regulation, and not enforcement. Nothing here is legal advice.

---

## 11. What to double check before relying on this

1. **Unverified rows.** Download the blocked documents listed in `docs/DOWNLOAD_LIST.md` and check the rows; the named earlier unverifiable rows are in Appendix A.
2. **EU dates.** Read the Official Journal text of Regulation (EU) 2026/1744 pages 30 to 41 and the consolidated Articles 111 and 113.
3. **DoH Standard.** Check the DoH listing for a revision (the document states October 2026).
4. **DIFC.** Check the legal database for amendments after Version No. 2, and the remaining Framework sections.
5. **Saudi.** Check whether SDAIA and NCA documents have moved from draft to final.
6. **Status calls.** Review the ambiguous rows; they are judgement calls.
7. **Framing of Section 8.** Do not present the gap analysis as a statement of UAE law or policy.
8. **Legal review.** Have a qualified lawyer review anything you plan to rely on for compliance.

---

## Appendix A. Verification

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

**Coverage of cited rows.** The report prose, brief and checklist cite 234 distinct rows. Of these, 211 were verified in phase 2, 23 are excluded from counts and carry a dagger wherever they appear, and 0 were not rechecked. A test fails if any cited row is neither verified nor marked unverified.

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

| Family | Rows | Blocked | Readable but passage not located | Source not read or withdrawn |
|---|---|---|---|---|
| EU AI Act (as amended 2026) | 4 | 0 | 0 | 0 |
| EU GPAI Code of Practice | 4 | 0 | 0 | 0 |
| EU harmonised standards (JTC 21) | 1 | 0 | 0 | 0 |
| ISO/IEC (catalogue level) | 1 | 1 | 0 | 0 |
| US OMB M-25-21 | 2 | 0 | 0 | 0 |
| UK (Playbook, ATRS, DSIT, AISI) | 3 | 0 | 0 | 0 |
| Canada Directive on Automated Decision-Making | 24 | 24 | 0 | 0 |
| Singapore (AI Verify, Starter Kit, frameworks) | 2 | 0 | 0 | 0 |
| Japan (Act, plan, guidelines, AISI) | 4 | 0 | 0 | 0 |
| South Korea AI Basic Act | 2 | 0 | 0 | 0 |
| China (GenAI, algorithm, labelling, GB/T 45654) | 3 | 0 | 1 | 0 |
| UAE federal (Charter, Strategy, Guidelines, Ethics, Cyber policy, PDPL) | 12 | 0 | 0 | 0 |
| DIFC and ADGM (Reg 10, Framework, DP guidance) | 4 | 0 | 0 | 0 |
| Dubai (Ethics, Matrix, DHA, ISR, AV law, entity policies) | 1 | 0 | 0 | 0 |
| Abu Dhabi DoH (health sector) | 4 | 0 | 0 | 0 |
| Saudi Arabia (SDAIA, NCA draft) | 23 | 7 | 0 | 0 |

---

## Appendix B. Free resources to download and read

All documents below are free. The complete, row linked list of documents to download by hand is `docs/DOWNLOAD_LIST.md`. In summary:

- **Canada:** the Directive on Automated Decision Making, the Algorithmic Impact Assessment tool page and peer review guide (Treasury Board Secretariat).
- **EU:** Regulation (EU) 2026/1744, Official Journal L of 24 July 2026, pages 30 to 41; the consolidated Articles 111 and 113; the General Purpose AI Code of Practice safety chapter.
- **Saudi Arabia:** the SDAIA AI Ethics Principles 2025 PDF and the AI Ethics page, the Generative AI Guidelines and the AI Adoption Framework (SDAIA); the NCA AI Cybersecurity Guidelines draft and Arabic PDF.
- **UAE:** the National Cyber Security Policy for AI PDF (Cyber Security Council); DoH policies listing pages in English and Arabic; Arabic originals of the Charter, the PDPL and the Adoption Guideline.
- **Standards:** ISO/IEC catalogue entries and public summaries are free to read on the ISO site; full texts of standards may require payment and are not required for this work. Where a clause could not be read, the row says so.
- **NIST:** the AI RMF Playbook pages that the fetch tool could not read.

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
| `data/time_sensitive.csv`, `data/uae_search_log.csv`, `data/uae_sources.csv` | Phase 2 records |
| `data/verification/` | Raw verification results and rules |
| `src/ikhtibar/` | Build scripts, engine, command line tool, staleness script |
| `templates/test_evidence/` | Evidence templates per test type (proposals) |
| `examples/MADOUN_EXAMPLE.md` | Hypothetical worked example |
| `docs/coverage_matrix.csv`, `docs/summary_by_family.csv`, `docs/summary_by_test_type.csv`, `docs/assurance_checklist.csv` | Generated tables |

## Appendix D. Libraries and data licences

The code uses PyYAML (MIT licence) and the Python standard library. Tests use `unittest` and optionally `pytest` (MIT). The secrets scan uses a local script, and `detect-secrets` (Apache 2.0) was run as an extra check. No dataset other than the cited public sources is used; the table holds paraphrases and short attributed quotes only. See `docs/LICENSING.md`.
