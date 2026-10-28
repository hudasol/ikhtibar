# Literature search 2: notes

Topic codes in new_2.csv are letters, not the numbers used in refs_candidates.csv: A = testing, evaluation and assurance practice and standards; B = language model assisted extraction, screening and coding; C = preregistration, reproducibility, documentation, coverage estimation; D = Gulf and Arabic coverage.

## Searches run (WebSearch, standard mode)
1. BetterBench benchmark quality; construct validity in LLM benchmarks; evaluation science for generative AI; third party audit ecosystem and audit effectiveness.
2. LLM data extraction in systematic reviews (Gartlehner); datasheets for datasets; preregistration revolution; AI governance in the Gulf (UAE, Saudi).
3. LLM abstract and title screening accuracy; joint position statement on AI in evidence synthesis; NIST TEVV; EU AI Act harmonised standards and conformity; AI assurance literature; Saudi AI ethics in Arabic scholarship; ML reproducibility checklist; model cards.
4. ISO/IEC 42001 critiques (only vendor pages found); EU standardisation (Veale and others); TRIPOD-LLM; sampling frame and corpus coverage (nothing scholarly); LLM annotation validation; Arabic LLM evaluation gaps; conformity assessment.
5. Preregistration in ML and NLP; gaps in safety evaluation; LLM assisted extraction 2025; UAE AI regulation scholarship; AI ethics guidelines landscape; ISO/IEC TS 42119 and 29119; leakage and reproducibility; abstract screening diagnostic accuracy; multilingual AI gap.
6. ISO 42001 comparisons; recall estimation and stopping rules in technology assisted review.

## Not verified or caveats
- Venue or year not shown in the fetched text, so inferred: gartlehner2025opportunities (journal inferred from URL; title uncertain), nosek2018preregistration (journal and year from DOI in search results), lewis2025mapping (year from arXiv number), hofman2023preregistration and peppin2025multilingual (no venue stated), gebru2021datasheets (CACM version not confirmed), vanmiltenburg2021preregistering (NAACL 2021 from the ACL Anthology listing in search results). Confirm each against the publisher record before the bibliography is final.
- gartlehner2025swar: full author list was not in the fetched text; only the lead author was named via the protocol reference. Preprint.
- gallifant2024tripodllm: read as the medRxiv preprint page; a note on that page says a Nature Medicine version exists, which was not opened.
- nist2025tevv: an outline for public comment, not peer reviewed; date inferred.
- nosek2018: fetched copy is a hosted PDF; a related PNAS reply by the same authors to Ledgerwood (PMC6233068) was also read but is not listed.
- reuel2024betterbench, bean2025measuring and others fetched as HTML: the tool read the first 100,000 characters of pages up to about 130,000; the tail (mostly appendices) was not read. Marked full_text.
- A full-text check of the claims "venue NeurIPS 2024/2025" for BetterBench and Bean rests on proceedings pages in search results, not on a page I opened.

## Fetched but excluded
- birhane2024broken, mokander2023auditing, mokander2021conformity, albous2025gcc: already in refs_candidates.csv.
- Cheng, Mayya and Sedoc (LLM annotation across management tasks, fetched at arXiv 2412.14461): the content returned did not match the title I expected, so identity is uncertain.
- Dennstaedt et al. (screening, Systematic Reviews 2024) and Kapoor and Narayanan (leakage, Patterns 2023): fetch hit a browser check or a URL outside the session allowlist; skipped, no workaround used.
- Laux, Wachter and Mittelstadt (three pathways, EU AI Act standardisation): redirect target was not allowed; not read.
- Medical abstract screening diagnostic accuracy study (medRxiv 2024.10.01.24314702): authors not shown in fetched text; not listed.
- PubMed page for TRIPOD-LLM: returned a browser check; the PMC preprint was used instead.
- Goodman 2023 (LSE Law Review, standards under the draft Act), Golpayegani et al. 2022 (ISO/IEC 42001 vs AI Act vs ALTAI), MITRE AI Assurance Landscape 2025 (grey report), Molnar (EU and UAE AI regulation, journal and year not stated), Jobin et al. 2019: read at abstract or landing level but dropped to keep the list at 20; Goodman and Golpayegani are good reserves for topic A.
- ISO/IEC TS 42119-2:2025: ISO catalogue page only (landing page); it is a standard, not scholarship, and no peer reviewed commentary on TS 42119 or on ISO/IEC 29119 for AI was found. Scholarly critique of ISO/IEC 42001 was likewise not found beyond item above.

## Gaps
- Topic C, sampling frame coverage: nothing found beyond technology assisted review stopping rules; no source on estimating coverage of a frame of policy documents.
- Topic D: no study of AI testing requirements in UAE or Saudi documents, consistent with the paper's stated limit.
