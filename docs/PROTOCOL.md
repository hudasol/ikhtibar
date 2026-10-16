# Research Protocol

**Question:** Across governments and national institutes, what pre deployment testing of AI systems is REQUIRED, versus RECOMMENDED, versus merely DESCRIBED, and where are the gaps that matter for deploying AI in UAE government settings?

Not legal advice. Analysis only.

## 1. Inclusion criteria

A source is included if it is:
- A primary document (statute, regulation, directive, official standard page or catalogue entry, official guidance, official framework text) from a government, national institute, or standards body in scope; AND
- Retrieved and read in this session (URL + retrieval date logged); AND
- Containing at least one provision that concerns testing, evaluation, assessment, validation, conformity, red teaming, audit, or verification of an AI system before or at deployment.

Secondary sources (law-firm summaries, news) are used only to locate primary sources, and are never cited as evidence for a clause. Where only a secondary source is available, the row is marked `unverified`.

Frameworks in scope (minimum): NIST AI RMF + Playbook/GenAI Profile; UK AI Security Institute and UK guidance; EU AI Act (high risk conformity assessment, GPAI obligations, harmonised standards work); Singapore AI Verify; Canada Directive on Automated Decision-Making; Japan; South Korea; China generative AI rules; ISO/IEC 42001, 23894, 42006 and testing-related standards; UAE national AI strategy/charter; Dubai AI policies; Abu Dhabi government AI policy; Saudi SDAIA principles.

## 2. Search strategy

1. Start from the issuing body's own site (eur-lex.europa.eu, nist.gov, gov.uk, tbs-sct.canada.ca, imda.gov.sg, iso.org, sdaia.gov.sa, u.ae, etc.).
2. Use web search to locate the current consolidated or official version; confirm status (in force / draft / repealed / amended) from the issuing body, not from memory.
3. Fetch the full text where free; for paywalled standards, use only the publicly visible catalogue abstract/scope and mark clause-level rows `unverified` or omit them. List such documents for the user to download.
4. Record for every row: framework, clause/page, paraphrase, binding status, what is tested, who tests, URL, retrieval date.
5. Time-sensitive items (EU AI Act application dates and any amendments, Korea AI Basic Act implementing decrees, Japan legislation, UAE policy updates) are checked against current primary sources.

## 3. How "required" is determined

Binding status values:
- **mandatory**: legally binding on the stated actor, with testing/assessment obligation stated in operative text.
- **conditional**: binding only if a trigger applies (e.g. high risk classification, impact level, threshold of compute, sector).
- **voluntary**: formal scheme or standard that an organisation may adopt; testing steps exist but adoption is optional (including certifiable management-system standards).
- **guidance**: a recommendation that is not binding, framework or description of practice.

Rules: operative text outranks recitals and preambles; "should" in guidance that is not binding is `guidance`; a policy binding only on government bodies is `mandatory` for those bodies and the row records the actor. Where status is ambiguous, the row is marked `ambiguous` with an explanatory note rather than forced into a category. Interpretation is kept in a separate column from paraphrase.

## 4. Translation handling

- Prefer official English versions. Where only non-English originals exist (e.g. Chinese, Korean, Japanese, Arabic), use the official translation if one exists; otherwise machine translation with explicit flag `translation: machine` and lower confidence; no clause numbers asserted beyond what the original text visibly shows.
- Arabic UAE/Saudi documents: read in Arabic where possible, flag when only English summaries were available.
- Direct quotes are limited to short attributed phrases (<15 words), never from translations presented as official.

## 5. Verification

After the table is merged, a separate subagent that has not seen the working notes re-checks a random sample of at least 25 rows against the original URLs (clause exists, paraphrase faithful, status correct, date correct). Error rate is reported; errors are corrected in the table.

## 6. Even-handedness and limits

No advocacy for or against any regulation. Conflicts between sources are flagged in a dedicated column. Gap analysis for the UAE is framed as analytical (what retrieved sources do and do not state), not as claims about UAE requirements beyond retrieved text.

## 7. Phase 2 addendum (12 October 2026)

- **Access rule.** Only the standard fetch and search tools. A blocked fetch is retried once, then stopped. No user agent changes, caches, mirrors, web archives, translation proxies or third party copies. A blocked row is marked unverified and the exact document to download is listed. A permission timeout is recorded as such.
- **Official alternates.** A different host of the same publisher may be used only if it is a documented official endpoint, and the access path is recorded.
- **Verification.** All rows cited in the report prose, brief and checklist are verified or marked unverified. A fresh seeded random sample is drawn separately from the cited rows, and verifiers differ from earlier verifiers. Sample types are reported separately. Wilson intervals are used for error rates.
- **Headline counts.** Unverified and unverifiable rows are excluded from headline counts and shown in a sensitivity figure.
- **UAE and Arabic.** Each source records whether an original or a translation was read, and English renderings produced by the fetch tool are marked as machine renderings. No claim about what the UAE requires is made unless a retrieved source says so.
- **Review dates.** Each row has retrieved_on, last_checked_on and next_review_by. The staleness script reads these offline.

## 8. Phase 3 addendum (16 October 2026)

Phase 3 re-runs the original brief over the existing evidence base rather than starting again, so that verified work is kept and every change is traceable.

- **Scope of re-checking.** Every row that phase 2 left as `UNVERIFIED_BLOCKED`, `UNVERIFIABLE_OTHER`, `UNVERIFIED_SOURCE_NOT_READ`, `NOT_RECHECKED`, `ERROR_WITHDRAWN` or `VERIFIED_NOTE_ONLY` (175 rows) is assigned to a research subagent for its family and checked against the primary source.
- **Access rule.** Unchanged from section 7. One clarification: the standard fetch tool now reads long documents in segments (a character offset). Reading on through a long official document with that option is the standard tool, not a workaround, so rows that phase 2 marked unreadable because of truncation are retried. Rows that phase 2 marked `permission_timeout` were a tool environment failure, not a site block, and are retried once. Site rejections are retried once and then stopped.
- **Status re-check.** Time sensitive items (EU AI Act dates after Regulation (EU) 2026/1744, GPAI Code of Practice, harmonised standards, Korea and Japan implementing texts, China standards, NIST and UK institute outputs, ISO/IEC testing standards, Saudi drafts, UAE instruments) are re-checked against primary sources on 16 October 2026.
- **Discovery.** In-scope instruments missing from the table are searched for, with priority on the Abu Dhabi government AI policy named in the brief, other UAE federal and emirate instruments, and ISO/IEC testing standards. New rows get identifiers of the form `<family>-P3-<nn>` so their phase is visible.
- **How "required" is determined.** Unchanged (section 3). For the comparison in the report a provision counts as *required pre-deployment testing* only if all four hold: (a) it is in operative text, (b) the text binds the stated actor, (c) it names an evaluation, test, assessment or audit activity, not only documentation, and (d) the activity is due before deployment, placing on the market, putting into service or production use. A trigger makes it *conditional*. A provision that only describes practice (an institute report, a case study, a methodology guide with no recommendation) is coded `guidance` with row type `context` and is reported as "described".
- **Translation.** Unchanged (section 4). Where the fetch tool renders a non-English page in English, the row records this as a machine rendering and no clause number is asserted that was not visible in the original structure.
- **Verification.** Round 3 results override earlier rounds row by row. After phase 3 corrections are applied, a separate subagent that did not take part in the research checks (a) every new phase 3 row and (b) a fresh random sample of at least 25 existing rows drawn with seed 20261016 from rows with a readable source. Error rate = ERROR verdicts divided by verifiable rows (PASS, MINOR, ERROR), reported with a Wilson 95% interval, before and after correction. MINOR is reported separately.
- **Files.** Inputs, rules and raw results for phase 3 are in `data/verification/phase3/`.
- **Additions made during phase 3.** (a) Two coder subagents independently classified non binding test rows by normative force (obligation wording, recommendation, description) from the row paraphrases; agreement and Cohen's kappa are reported and disagreements stay marked disputed (`data/coding/`). (b) The lead analyst re-graded verifier MINOR verdicts to ERROR where the verdict rubric requires it, keeping the original grades (`verdict_reclass.csv`). (c) A row whose source could not be re-read in a later round keeps its earlier verified status with a note, rather than being dropped. (d) A separate reviewer checked the report prose against the cited rows (`data/verification/phase3/final/prose_review.md`), and its findings were applied.
