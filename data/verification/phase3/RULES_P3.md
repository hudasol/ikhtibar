# Rules for every phase 3 subagent (read fully before doing anything)

Context: an AI governance evidence review on pre-deployment testing of AI systems: what governments and institutes REQUIRE, RECOMMEND or merely DESCRIBE, with a UAE government gap analysis. Research, not legal advice. Retrieval date to record: **2026-10-16**. Repository root: `C:\Users\karee\Downloads\projects\khtibaar multi\ikhtibaar` (call it ROOT). Protocol: `ROOT\docs\PROTOCOL.md` sections 3, 4, 7 and 8. Everything must be free: never suggest buying a standard, subscription or paid API.

## ACCESS RULE (strict)
1. For web content use ONLY the WebFetch and WebSearch tools. Do NOT use curl, wget, Python requests, PowerShell Invoke-WebRequest, a browser tool, or any other route.
2. WebFetch accepts an `offset` (character position). Reading on through a long official document with `offset` IS allowed and expected: if a document is truncated, continue with the offset the tool gives until you reach the passage. Ask the tool for the exact passage and its locator (article, section, clause, page).
3. If a site blocks a fetch (403/429/406, "Request Rejected", bot challenge, empty response, robots disallow), retry the same URL ONCE. If still blocked, STOP for that source: no user agent changes, caches, web archives, mirrors, translation proxies or third-party copies, and no search snippets as evidence. Record the URL, the exact error text and the exact document the user should download by hand.
4. A different, documented official host of the SAME publisher (for example publications.europa.eu for EUR-Lex, or the same ministry's PDF on its own domain) may be used; label access_path `alt_official_endpoint` and name the host that blocked.
5. Secondary sources (law firms, news, blogs, newsletters, consultancies, Wikipedia) may help LOCATE a primary source but are NEVER evidence for a clause, date or status. If only a secondary source exists, say so and mark the item unverified.
6. Paraphrase. Any quote must be under 15 words and attributed. Never invent clause numbers, page numbers, dates, document codes or quotations. If you did not see a locator, write "locator not seen".
7. Do not read other working files beyond those your task names (independence matters). Do NOT edit any existing file in ROOT. Write only the output files your task names, as NEW files under `ROOT\data\verification\phase3\`. Use Python's csv module via a script you write to the scratchpad or via the Write tool; Python is `py -3`.
8. Never include credentials, cookies or personal data.

## Binding status vocabulary (protocol section 3)
mandatory (operative text binding on the stated actor) · conditional (binding only if a trigger applies) · voluntary (formal scheme/standard an organisation may adopt, incl. certifiable standards) · guidance (recommendation or description of practice) · ambiguous (document's own language conflicts or status unsettled; explain). Operative text outranks recitals and preambles. "Should" in non-binding guidance is guidance. A policy binding only on government bodies is mandatory for those bodies; record the actor.

## Test type codes (primary_test_type)
PERF performance/validity · ROB robustness/reliability · FAIR fairness/bias · SEC security/adversarial · RED red teaming/dangerous capability · CSAFE content safety (harmful output/refusal rates) · PRIV privacy/data protection assessment · TRANS transparency/explainability/labelling/reporting · OVER human oversight validation · RISK risk/impact/compliance assessment · DATA data quality validation · CONF conformity/independent audit/certification/filing · REAL real-world/sandbox/pilot testing · MON post-deployment monitoring · GATE acceptance criteria/release decision · NONE (context rows).
row_type: test (calls for or describes an evaluation producing evidence) · enabler (documentation, logging, registration, disclosure supporting tests) · context (dates, scope, penalties, status).
test_stage: pre-deployment · at-deployment · post-deployment · lifecycle · n/a.

## Verdict vocabulary (verification tasks)
- PASS: clause exists at the stated locator, paraphrase faithful, binding_status correct, who/what tested supported, version/date right.
- MINOR: small imprecision that does not change meaning (locator slightly off, wording slightly strong, citation incomplete).
- ERROR: a check clearly fails (clause absent or elsewhere with different meaning, paraphrase unfaithful or overstated, wrong status, unsupported who/what, wrong version or date).
- UNVERIFIED_BLOCKED: blocked under rule 3. Give the exact document to download.
- UNVERIFIABLE_OTHER: readable but the passage could not be located or read even with offset (image-only, garbled). Say exactly why.
Be sceptical: your job is to find faults. Check clause numbers yourself. A row whose source is a secondary report should be re-pointed to a primary source if one exists (propose the new URL and locator in a patch) or stay unverified.

## Output files (all NEW, under ROOT\data\verification\phase3\, <g> = your group name)
1. `p3res_<g>.csv` — one row per input row: `row_id,verdict,failed_checks,what_source_says,suggested_fix,locator_seen,access_log,evidence_url,text_basis,language_read,access_path`. access_path is `standard_fetch`, `standard_fetch_offset`, `alt_official_endpoint` or `none`. text_basis says what text you read (e.g. "consolidated text 2026-07-27", "OJ amending act", "official English translation", "fetch-tool English rendering of Korean original").
2. `p3patch_<g>.csv` — proposed corrections for MINOR/ERROR rows: `row_id,field,new_value,reason`. Allowed fields: framework, clause_or_page, requirement_paraphrase, binding_status, what_is_tested, who_tests, source_url, interpretation_note, conflict_flag, language_read, row_type, primary_test_type, test_stage. Give the full new value, not a diff.
3. If your task asks for status checks: `p3ts_<g>.csv` with columns `topic,item,our_value,primary_value_seen,locator_seen,source_url,access_path,status,retrieved_on,conflict_or_note`; status is one of confirmed / changed / not_found / blocked / secondary_only.
4. If your task asks for new rows: `p3new_<g>.csv` with columns `row_id,family,framework,clause_or_page,requirement_paraphrase,binding_status,what_is_tested,who_tests,source_url,retrieval_date,interpretation_note,conflict_flag,row_type,primary_test_type,secondary_test_types,test_stage,evidence_grade,language_read`. row_id = `<family>-P3-<two digits>`. evidence_grade is `primary text read`, `catalogue-level only` (paywalled standard: scope/abstract page only) or `read via unofficial/machine translation`. Only add a row if you read the primary text yourself.
5. `p3notes_<g>.md` — short: searches run (query, date), sources fetched with outcome, what was searched for and NOT found, conflicts between sources, documents the user must download by hand (exact title, URL, why).

Final message: short. Counts per verdict, list of every non-PASS row with the proposed fix, new rows added, status changes found, and the download list.
