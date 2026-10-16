# Prose review: REPORT.md (sections 1, 5.1, 5.6, 6.1, 7, 8, 11) and EXECUTIVE_BRIEF.md

Reviewer: sceptical prose check (suggested wordings longer than a short phrase are shown in italics; they are the reviewer's text, not source quotations) against `data/evidence_table.csv` and `data/time_sensitive.csv`, 16 October 2026. Research review, not legal advice. No repository file was edited. Severity: **high** = factually wrong or unsupported; **medium** = overstatement, wrong or contradictory supporting row, or missing Interpretation label; **low** = wording.

## Findings

### High

1. **Brief, "Items to confirm" (all three of the first bullets).** Excerpts: "confirmed at recital level only; the operative Article 113 text is still to be read"; "Whether it has been revised is open (listing pages unreadable)"; "amendments after Version No. 2 are unchecked".
   - Problem: these are phase 2 statements. The report itself says the dates are confirmed in operative text (Section 1 item 9, Section 7), and time_sensitive.csv lines 78 and 79 (phase 3) confirm Art 113(c)(i) and (ii). The DoH policies listing is now readable (time_sensitive line 166, status changed). The DIFC amendments were checked: a consultation exists and nothing has been enacted (line 172; `UAE-DIFC-ADGM-P3-01` to `P3-04`). So the brief contradicts the report on all three items.
   - Rows: `EU-AI-Act-001`, `EU-AI-Act-002`, time_sensitive lines 6, 7, 78, 79, 166, 172.
   - Fix: regenerate the brief's "Items to confirm" from the phase 3 items. EU: dates confirmed in operative text. DoH: still V1, revision due this month, and the listing shows only the 2018 policy. DIFC: June 2026 consultation, not enacted as of 16 October.

2. **Section 7, opening sentence and table.** Excerpts: "Status counts: ... confirmed: 87" and "DoH Responsible AI Standard | 2026-10-12 | 11 | blocked 2, confirmed 7, open 2".
   - Problem: time_sensitive.csv holds 20 DoH items dated 12 October (16 confirmed): the 9 clause-level checks on lines 26 to 34 are missing from the table. The table's items add up to 172, not 181, and its confirmed counts add up to 78, not 87. The headline counts and the table do not agree.
   - Rows: time_sensitive lines 15 to 34.
   - Fix: make the DoH row read 20 items (blocked 2, confirmed 16, open 2), or drop those 9 items from the headline counts and say so.

3. **Section 5.1, Interpretation paragraph.** Excerpt: "removing blocked sources removed two regimes (Canada and most of the EU conformity chapter)".
   - Problem: this is stale. Section 1 item 1 says phase 3 restored the EU rows. The conformity rows `EU-AI-Act-040` and `EU-AI-Act-041` are in the headline counts, coded conditional, and the EU family has 27 binding rows in the 5.1 table.
   - Rows: `EU-AI-Act-040`, `EU-AI-Act-041`.
   - Fix: *removing blocked sources removes Canada (12 test rows) from the binding count; the EU rows removed in phase 2 were restored in phase 3.*

### Medium

4. **Section 1 item 4 and the brief.** Excerpt: "Binding red teaming is narrow ... 4 of them are mandatory or conditional".
   - Problem: only `EU-AI-Act-068` requires adversarial testing. `EU-AI-Act-063` (Art 51) is a classification rule for systemic risk, and `EU-AI-Act-071` and `EU-AI-Act-P3-20` are AI Office evaluation and access powers. They carry the RED code, but calling them "binding red teaming" overstates them. The brief drops even the "dangerous capability" qualifier ("4 of 26 verified red teaming rows").
   - Rows: `EU-AI-Act-063`, `EU-AI-Act-068`, `EU-AI-Act-071`, `EU-AI-Act-P3-20`.
   - Fix: *1 provision binds providers to adversarial testing (`EU-AI-Act-068`); 3 more are related binding rules: classification by evaluated capability, and AI Office evaluation and access powers.*

5. **Section 1 item 3 and the brief.** Excerpt: "Independent testing is binding in a few places ... DIFC Regulation 10 makes certification a precondition".
   - Problem: DIFC certification criteria are reviews of documents and evidence, "not technical performance testing" (`UAE-DIFC-ADGM-020`). The Framework is marked informational (`UAE-DIFC-ADGM-018`, conflict flag). The only accredited certification body listed is for internal systems only (`UAE-DIFC-ADGM-022`, `UAE-DIFC-ADGM-025`). Calling this "independent testing" overstates it.
   - Rows: `UAE-DIFC-ADGM-004`, `UAE-DIFC-ADGM-018`, `UAE-DIFC-ADGM-020`, `UAE-DIFC-ADGM-022`, `UAE-DIFC-ADGM-025`.
   - Fix: *DIFC Regulation 10 makes independent certification (document and governance review) a precondition ...; whether external certification is operational is not stated.*

6. **Section 1 item 6 and the brief.** Excerpts: "one cross sector instrument binding government entities was found" and "one cross government instrument binds entities to test AI".
   - Problem: the binding status is stated as fact. Section 6.1 labels the same point *Interpretation* ("under the protocol's four part test"). The policy names no legal instrument and no penalty clause was seen (`UAE-Federal-P3-08` interpretation_note, `UAE-Federal-P3-01`).
   - Rows: `UAE-Federal-P3-01`, `UAE-Federal-P3-08`.
   - Fix: *one cross sector instrument was found that uses 'shall' for government entities (coded mandatory; the document does not name its legal basis).* Alternatively, mark the sentence **Interpretation**.

7. **Section 6.1, "Source says", National Cyber Security Policy bullet.** Excerpt: "covers emirate government entities through the emirate lead where an emirate programme exists".
   - Problem: this presents one of the two disputed readings as what the source says. It contradicts Section 1, Section 11 item 1 and the conflict flag on `UAE-Federal-P3-08`. The rows themselves also embed opposite readings. `UAE-Federal-P3-01` (note) says entities are covered by the Emirate Lead where a programme exists and directly otherwise. `UAE-Federal-P3-02` to `P3-07` (who_tests) say "covered only where no Emirate CIIP Program exists".
   - Rows: `UAE-Federal-P3-01`, `UAE-Federal-P3-02`, `UAE-Federal-P3-08`.
   - Fix: add "verifiers read s1.2 differently (Section 11)" to the bullet. Make who_tests in P3-02 to P3-07 neutral until a human reads s1.2.

8. **Section 8, G8.** Excerpt: "the cyber security policy requires regular security testing and the testing of changes".
   - Problem: `UAE-Federal-P3-07` is coded guidance. Its note says that testing changes before deployment is "should" guidance, and only patch testing (statement 2.2.3) is mandatory, with no timing.
   - Rows: `UAE-Federal-P3-04`, `UAE-Federal-P3-07`.
   - Fix: "requires regular security testing and the testing of patches; testing changes before deployment is guidance."

9. **Section 5.1, China bullet.** Excerpt: "Generative AI providers must sample check annotation quality (`China-003`) and review algorithms (`China-009`)".
   - Problem: `China-009` comes from the 2022 Provisions on Algorithmic Recommendation, not the generative AI measures, so the actor and instrument are wrong.
   - Rows: `China-003`, `China-009`.
   - Fix: "Generative AI providers must sample check annotation quality (`China-003`); algorithmic recommendation providers must periodically review algorithms (`China-009`)."

10. **Brief, UAE bullet.** Excerpt: "No binding federal text ... requires testing accuracy or fairness ... that remains ... zone specific (DIFC)".
    - Problem: this implies DIFC binds accuracy or fairness testing. The DIFC rows require certification against governance and evidence criteria (`UAE-DIFC-ADGM-020`) and bias mitigation measures (`UAE-DIFC-ADGM-021`), not accuracy testing. The pre-use safety verification test is only proposed (`UAE-DIFC-ADGM-P3-01`). No row is cited.
    - Rows: `UAE-DIFC-ADGM-004`, `UAE-DIFC-ADGM-020`, `UAE-DIFC-ADGM-021`, `UAE-DIFC-ADGM-P3-01`.
    - Fix: "...remains sector specific (Abu Dhabi and Dubai health); DIFC requires certification for commercial high risk processing" and cite the rows.

11. **Section 1 item 2, brief, G3.** Excerpt: "validation against \"established performance benchmarks\"".
    - Problem: the phrase is given in quotation marks as source wording. The row paraphrase says "established", but the clause check in time_sensitive line 26 records "recognised performance benchmarks". The verbatim wording is not settled.
    - Rows: `UAE-AbuDhabi-DoH-003`, time_sensitive line 26.
    - Fix: check clause 3.1.3.1.1 by hand. Until then, remove the quotation marks: "against performance benchmarks it does not name".

12. **Section 5.1 EU bullet and Section 1 item 9.** Excerpt: "The amended dates are confirmed in operative text (`EU-AI-Act-001`, `EU-AI-Act-002`)".
    - Problem: the interpretation_note of `EU-AI-Act-002`, and of `EU-AI-Act-005` (cited in 5.6), still says that the operative Articles 111 and 113 "was beyond what the fetch tool returned, so the article level locators are unconfirmed". The cited row contradicts the sentence. The claim itself is supported by time_sensitive lines 78 and 79.
    - Rows: `EU-AI-Act-002`, `EU-AI-Act-005`.
    - Fix: update both notes to the phase 3 finding, or cite time_sensitive lines 78 and 79.

13. **Section 5.1, Korea bullet.** Excerpt: "duties on high impact AI (`Korea-007`, `Korea-014`)".
    - Problem: `Korea-014` interpretation_note reads "UNVERIFIED: secondary source only", but the row is VERIFIED_CORRECTED and in the headline counts. The row is internally inconsistent, so the citation is unreliable.
    - Rows: `Korea-014`.
    - Fix: correct the note to match the verification status, or dagger the row.

14. **Section 5.6, Saudi bullet.** Excerpt: "cover and Arabic pages say \"Guidelines\"; only the PDF file name says \"Controls\"".
    - Problem: the Arabic PDF was not located (time_sensitive line 151), so "only" is not established. `Saudi-019` (note) still says "the file name and Arabic cover use 'Controls' (AICC-1:2026)", which contradicts the report.
    - Rows: `Saudi-018`, `Saudi-019`, `Saudi-020`.
    - Fix: *The English cover and Arabic web pages say Guidelines; the English file name says Controls; the Arabic PDF cover was not seen.* Update the `Saudi-019` and `Saudi-020` notes.

15. **Section 1 items 2 and 5 (headings).** Excerpts: "the text mostly requires that it happens and is documented, not how" and "Human oversight is specified as design, not as something to test".
    - Problem: these are analyst generalisations drawn from a few rows (3 examples; 1 oversight row) and presented as findings without an **Interpretation** label. Under the report's own convention they need one.
    - Rows: `EU-AI-Act-016`, `EU-AI-Act-018`, `US-OMB-003`, `UAE-AbuDhabi-DoH-003`, `EU-AI-Act-026`, `UAE-DIFC-ADGM-015`.
    - Fix: prefix each with "Interpretation:" and keep the row-based sentences as "Source says".

16. **Section 5.1, Interpretation.** Excerpt: "The frameworks with the most detailed testing guidance (NIST, Singapore, Japan, ISO) are not binding."
    - Problem: Japan has 2 mandatory test rows in the same table (DS-920, `Japan-P3-01`). ISO entries are catalogue level only and no ISO text was read (`ISO-IEC-009`, `ISO-IEC-015`), so ISO cannot be called the "most detailed".
    - Rows: `Japan-P3-01`, `ISO-IEC-009`, `ISO-IEC-015`.
    - Fix: *...(NIST, Singapore, Japan's AISI guides) are not binding; Japan's DS-920 is the exception for ministries; ISO texts were not read.*

### Low

17. **Section 8, G5.** Excerpt: "which the research agent coded as red teaming".
    - Problem: `UAE-Federal-P3-04` has primary type SEC. RED is only a secondary code, and red teaming appears only in "should" guidance. As written, a reader could infer binding UAE red teaming, which Section 1 item 4 implicitly excludes.
    - Rows: `UAE-Federal-P3-04`.
    - Fix: "coded security testing, with red teaming as a secondary code; red teaming is named only in the implementation guidance."

18. **Section 6.1, Dubai Ethics row.** Excerpt: "`UAE-Dubai-011` to `UAE-Dubai-024`".
    - Problem: the range includes `UAE-Dubai-023`, which has headline_include = no (a newsroom report), with no dagger.
    - Rows: `UAE-Dubai-023`.
    - Fix: split the range and show `UAE-Dubai-023`†.

19. **Section 1 item 7 and the brief.** Excerpt: "Of 209 such headline rows ... (agreement 95.4%, Cohen's kappa 0.9)".
    - Problem: the agreement figure and kappa are computed on n = 216 (`data/coding/normative_force_stats.json`). On the 209 headline rows, 10 disputes give 95.2% agreement.
    - Rows: none (stats file).
    - Fix: state n = 216 for agreement, or recompute on the 209 rows.

20. **Section 5.1, US bullet, and G6.** Excerpt: "request model, system and data cards with evaluation information".
    - Problem: the row says the cards "often include" benchmark scores. The duty is to request the cards, not evaluation information as such.
    - Rows: `US-OMB-P3-01`.
    - Fix: "request model, system and data cards (which often include evaluation results)."

21. **Section 1 item 5.** Excerpt: "Oversight design duties appear as enabling provisions (`EU-AI-Act-026`, `UAE-Federal-008`)".
    - Problem: `UAE-Federal-008` is a data subject's right to object and to human review, not a design duty.
    - Rows: `UAE-Federal-008`.
    - Fix: "...design duties (`EU-AI-Act-026`) and a right to human review (`UAE-Federal-008`)."

22. **Section 7, EU paragraph.** Excerpt: "Article 111(2) gives public authority deployers of legacy systems until 2 August 2030".
    - Problem: the source covers providers and deployers of systems intended for use by public authorities (time_sensitive line 82).
    - Rows: time_sensitive line 82.
    - Fix: reword to match the source.

23. **Brief wording.** Excerpts: "test provisions that are not marked unverified"; "critical infrastructure entities"; "the largest general purpose models".
    - Problem: the exclusions also cover superseded and secondary-only rows. The policy covers *non government* critical infrastructure entities (`UAE-Federal-P3-08`). Art 92 concerns systemic-risk models, not "the largest" (`EU-AI-Act-071`).
    - Fix: "not excluded"; "non government critical infrastructure entities"; "general purpose models with systemic risk".

24. **Template artefacts.**
    - Section 1 item 5: "1 (`UAE-DIFC-ADGM-015` (guidance))" has nested parentheses.
    - G9: "1 oversight validation test row(s)".
    - A.1: "1 errors in 142".
    - Fix: correct the template strings.

25. **Section 8, G1 and G4, and the 6.1 table.** Rows cited as support could not be re-read on 16 October: p3_final_verdict UNVERIFIED_BLOCKED, with the phase 2 status kept. This is disclosed only in Section 11 item 2.
    - Rows: `UAE-Federal-009`, `UAE-Federal-012`, `UAE-Federal-021`, `UAE-Federal-027`, `UAE-Federal-031`, `UAE-Dubai-008`.
    - Fix: add a short marker (for example "not re-read 16 Oct") where these rows are cited.

26. **Section 7, status counts.** Excerpt: "open: 15".
    - Problem: most phase 2 "open" and "blocked" items (EU Omnibus 7 open, DoH listing blocked) were resolved by phase 3 items. The headline counts still report them, so a reader sees 15 open items.
    - Fix: report the effective status, applying phase 3 where it supersedes, or add an "of which superseded" column.

27. **Section 6.1, DoH Protocol row.** Excerpt: "avoid high residual risk".
    - Problem: this states one side of the Protocol's internal inconsistency. DP1 sends only *very high* risk to "avoid".
    - Rows: `UAE-AbuDhabi-DoH-P3-03`.
    - Fix: "avoid very high (Step 6 text says high) residual risk".

## Claims checked and found supported (row IDs)

`EU-AI-Act-001`, `EU-AI-Act-016`, `EU-AI-Act-017`, `EU-AI-Act-018`, `EU-AI-Act-026`, `EU-AI-Act-028`, `EU-AI-Act-029`, `EU-AI-Act-030`, `EU-AI-Act-036`, `EU-AI-Act-040`, `EU-AI-Act-041`, `EU-AI-Act-055`, `EU-AI-Act-068`, `EU-AI-Act-071`, `EU-AI-Act-P3-20`, `EU-AI-Act-P3-22`, `EU-GPAI-CoP-001`, `EU-GPAI-CoP-P3-20`, `EU-GPAI-CoP-P3-23`, `EU-Standards-002`, `EU-Standards-P3-20`, `US-OMB-003`, `US-OMB-004`, `US-OMB-006`, `US-OMB-P3-02`, `US-NIST-026`, `US-NIST-028`, `US-NIST-046`, `UK-004`, `UK-011`, `UK-014`, `UK-015`, `UK-018`, `UK-019`, `UK-024`, `Singapore-007`, `Singapore-009`, `Singapore-028`, `Singapore-035`, `Singapore-P3-01`, `Japan-020`, `Japan-P3-01`, `Korea-005`, `Korea-007`, `Korea-013`, `Korea-016`, `Korea-P3-01`, `China-003`, `China-017`, `China-024`, `China-025`, `China-031`, `China-P3-01`, `China-P3-02`, `ISO-IEC-009`, `ISO-IEC-015`, `UAE-Federal-001` to `UAE-Federal-013`, `UAE-Federal-014`† (superseded, correctly daggered), `UAE-Federal-018` to `UAE-Federal-034`, `UAE-Federal-P3-01` to `UAE-Federal-P3-06`, `UAE-Federal-P3-08` (scope dispute as stated in Section 1), `UAE-AbuDhabi-Other-001`, `UAE-AbuDhabi-Other-002`, `UAE-AbuDhabi-DoH-001`, `UAE-AbuDhabi-DoH-002`, `UAE-AbuDhabi-DoH-004` to `UAE-AbuDhabi-DoH-014`, `UAE-AbuDhabi-DoH-P3-01`, `UAE-AbuDhabi-DoH-P3-02`, `UAE-AbuDhabi-DoH-P3-04`, `UAE-DIFC-ADGM-001` to `UAE-DIFC-ADGM-017`, `UAE-DIFC-ADGM-019`, `UAE-DIFC-ADGM-023`, `UAE-DIFC-ADGM-024`, `UAE-DIFC-ADGM-P3-01` to `UAE-DIFC-ADGM-P3-04`, `UAE-Dubai-001` to `UAE-Dubai-022`, `UAE-Dubai-024` to `UAE-Dubai-040`, `Saudi-001` to `Saudi-010`, `Saudi-011`† to `Saudi-017`† (correctly daggered), `Saudi-018`, `Saudi-021` to `Saudi-023`, `Saudi-P3-01` to `Saudi-P3-16`.

Number checks that pass:
- The 5.1 table columns sum to 290 / 26 / 55 / 42 / 131 / 36 / 81 / 21 and match `evidence_table.csv`.
- Section 0 matches the table: 522 rows, 38 excluded, and 311 rows splitting 93 / 180 / 38 if excluded test rows were counted.
- The Section 1 family split of 81 binding rows matches the table.
- The 209 non binding rows break down as 140 + 40 + 19 + 10.
- The Appendix A.1 rows sum correctly, and the Wilson intervals for 3/23 and 15/142 recompute.
- Section 1 item 8, Appendix A and the brief agree on all verification figures.
- Section 7 facts match time_sensitive.csv: EU dates and corrigendum, EN 18286 citation, GPAI Code opinion of 1 August 2025, Art 50 code, Implementing Regulation 2026/1755, Korea decree 36580, DS-920, the five AI TAP firms, DoH V1, DIFC consultation closing 18 July 2026, SPA "guidance reference".
- The DoH June and July 2025 policy date conflict in 5.6 is supported by time_sensitive line 167.
