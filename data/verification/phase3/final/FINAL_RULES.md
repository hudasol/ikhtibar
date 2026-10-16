# Final independent verification, phase 3 (16 October 2026)

You are an independent verifier. You did not take part in the research. Your job is to find faults.

1. Read `ROOT\data\verification\phase3\RULES_P3.md` for the ACCESS RULE, vocabularies and verdict definitions, and follow them. ROOT = `C:\Users\karee\Downloads\projects\khtibaar multi\ikhtibaar`.
2. Independence: read ONLY that rules file, this file, and your own input file in `ROOT\data\verification\phase3\final\inputs\`. Do NOT open any other file under ROOT (no notes, results, patches, evidence table or report). Work from the primary sources.
3. For each row, open `source_url` (or the official document it points to) and check: (a) the passage exists at the stated locator, (b) the paraphrase is faithful and not overstated or understated (including "must" versus "should"), (c) binding_status is right under the protocol definitions in RULES_P3.md, (d) who tests and what is tested are supported, (e) document version and dates in `framework` and `clause_or_page` are right.
4. Grade strictly: a wrong binding status, a wrong date or version, a paraphrase that overstates or changes the scope or modality, or an unsupported actor is ERROR, not MINOR. MINOR is only for imprecision that leaves meaning intact (page slightly off, citation incomplete, wording slightly loose).
5. Long PDFs: read with the WebFetch offset. If WebFetch saves a PDF it cannot render, you may extract text locally from THAT saved file (record access_path `standard_fetch_saved_pdf_local_text`, or `standard_fetch_saved_pdf_page_image` if you rendered page images). Never fetch by any other route.
6. Catalogue-level rows (paywalled standards): check only against the free catalogue/abstract page; a claim beyond what the abstract says is an ERROR.
7. Output: write `ROOT\data\verification\phase3\final\fv3_<n>.csv` (n = your batch number) with columns `row_id,verdict,failed_checks,what_source_says,suggested_fix,locator_seen,access_log,evidence_url,text_basis,language_read,access_path`, one line per input row, using Python's csv module (`py -3`). For every MINOR or ERROR also write `ROOT\data\verification\phase3\final\fv3patch_<n>.csv` with columns `row_id,field,new_value,reason` (allowed fields as in RULES_P3.md; full new value).
8. Final message: counts per verdict and one line per non-PASS row with the fix.
