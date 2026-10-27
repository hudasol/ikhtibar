# Rules for phase 4 verifier subagents (read fully before doing anything)

Context: an evidence table on pre deployment testing of AI systems (what governments and institutes require, recommend or merely describe). You are an independent verifier drawing a fresh check of a random sample. Research, not legal advice. Retrieval date to record: 2026-10-28. Everything must be free: never suggest buying a standard, subscription or paid API.

You see only your input CSV. Do NOT open any other file in the repository (not the report, not the evidence table, not earlier verification notes). Independence matters. Write only the two output files named in your task.

## ACCESS RULE (strict)
1. For web content use ONLY the WebFetch and WebSearch tools. No curl, wget, Python requests, headless browser, or any other route to web pages.
2. WebFetch accepts an offset. Reading on through a long document with offset is allowed: if truncated, continue until you reach the passage. Ask for the exact passage and its locator.
3. If a site blocks a fetch (403/429/406, "Request Rejected", bot challenge, empty response), retry once. If still blocked, STOP for that source: no user agent changes, caches, archives, mirrors, translation proxies or third party copies, and no search snippets as evidence. Record the URL and the exact error text.
4. A different official host of the SAME publisher (for example publications.europa.eu for EUR-Lex) may be used; label access_path alt_official_endpoint.
5. If WebFetch returns a binary PDF it saved to disk, you may extract text from that saved file locally (pdftotext or pypdf); label access_path standard_fetch_saved_pdf_local_text.
6. Secondary sources may help locate a primary source but are never evidence.
7. Paraphrase. Any quote under 15 words and attributed. Never invent clause numbers, pages, dates or quotations. If no locator was seen, write "locator not seen".

## What to check for each row
(a) the clause or page exists at the stated locator and says what the paraphrase says; (b) the paraphrase does not overstate or understate (a "should" turned into "must" is an ERROR); (c) the binding_status is correct under this protocol: mandatory = legally binding on the stated actor in operative text; conditional = binding only if a trigger applies; voluntary = a formal scheme or standard an organisation may adopt; guidance = non binding recommendation or description of practice; ambiguous = the document's own language conflicts or status cannot be settled. Operative text outranks recitals; "should" in non binding guidance is guidance; a policy binding only on government bodies is mandatory for those bodies. (d) who_tests and what_is_tested are supported; (e) the version, date and source address are right.

## Verdicts
- PASS: all checks hold.
- MINOR: a small imprecision that does not change meaning (locator slightly off, citation incomplete, retrieval date).
- ERROR: a check clearly fails: clause absent or elsewhere with different meaning; paraphrase unfaithful or overstated; wrong binding status; unsupported actor or test; wrong version or date. Apply this strictly: do not grade a substantive fault as MINOR.
- UNVERIFIED_BLOCKED: blocked under rule 3.
- UNVERIFIABLE_OTHER: readable but the passage could not be located or read; say exactly why.
Be sceptical. Your job is to find faults. Check clause numbers yourself.

## Outputs (new files; use Python's csv module)
1. data/verification/phase4/v4res_<n>.csv with columns: row_id, verdict, error_type (one of: none, locator, overstated, understated, wrong_status, wrong_actor, wrong_date_or_version, unsupported_test, other), failed_checks, what_source_says, suggested_fix, locator_seen, evidence_url, text_basis, language_read, access_path.
2. data/verification/phase4/v4patch_<n>.csv for MINOR and ERROR rows: row_id, field, new_value, reason. Allowed fields: framework, clause_or_page, requirement_paraphrase, binding_status, what_is_tested, who_tests, source_url, interpretation_note, language_read.
Final message: short. Counts per verdict, and a bullet for every non PASS row with the proposed fix.
