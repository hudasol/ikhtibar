# Phase 3 notes: g1_canada_us_iso (retrieved 2026-10-16)

## Searches run (WebSearch, 2026-10-16)
- "Directive on Automated Decision-Making" site:canada.ca OR site:publications.gc.ca OR site:open.canada.ca
- publications.gc.ca "Directive on Automated Decision-Making" Treasury Board
- Treasury Board Directive on Automated Decision-Making amendment 2026 review canada.ca
- "Directive on Automated Decision-Making" fourth review 2026
- NIST AI 800-2 "Practices for Automated Benchmark Evaluations" final 2026
- site:nist.gov "AI 800-2" OR "AI 800-3" OR "Cyber AI Profile" 2026
- OMB memorandum rescinds M-25-21 2026 AI use agencies
- NIST CAISI renamed "Super Intelligence" CAISSI; "Center for Advancing Innovation and Standards for Super Intelligence"

Search results were used only to find sources. They are not evidence.

## Sources fetched (WebFetch) and outcome
| Source | Outcome |
|---|---|
| tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592 | Rejected ("The requested URL was rejected...", support ID 9025196602307507123). Retried once and rejected again. |
| tbs-sct.gc.ca/...id=32592 | Returns a 301 redirect to the same blocked host |
| canada.ca "Amendments to the Directive on Automated Decision-Making" | Read. Page dated 2024-10-08. It covers only the 2023 amendments and links to the TBS page; it does not reproduce the Directive text, so it cannot serve as an alternative official copy. |
| NIST AI 100-1, AI 600-1, AI 800-2 ipd PDFs (nvlpubs) | WebFetch could not render them but saved the full PDFs it fetched. Text was extracted locally from those saved files with PyMuPDF, and printed page footers were checked. |
| OMB M-25-21, M-26-04, M-26-10 PDFs (whitehouse.gov) | Same method as the NIST PDFs (OCR text layer). |
| OMB memoranda index (whitehouse.gov) | Read |
| AIRC Playbook landing page and playbook.json | Read. The JSON was read at offsets 200000 and 300000. No timeout this time. |
| nist.gov/caisi | Read 3 times. The title is now "Center for Advancing Innovation and Standards for Super Intelligence (CAISSI)". |
| nist.gov/itl/ai-risk-management-framework | Read |
| nist.gov/node/1905466 (AI 800-2 news) | Read |
| csrc.nist.gov/pubs/ir/8596/iprd | Read |
| nccoe.nist.gov/node/2581 | 403 on the first try and on the retry |
| iso.org catalogue pages (42001, 77304, 42005, 42006, 84127, 79016, 77607, 79804, 80655, 84110, 27090) | All returned 403 on the first try and on the retry |

## Searched for and NOT found
- No official Government of Canada copy of the Directive text on any host other than the blocked TBS site.
- No official primary source on a 2025 or 2026 amendment, or a 4th or 5th review, of the Directive. Only GCcollab wiki and news items turned up, and these are secondary.
- No revised AI RMF (1.1 or 2.0) text or draft. NIST only says that AI RMF 1.0 "is being revised".
- No final version of NIST AI 800-2.
- No official notice explaining the CAISI to CAISSI rename.
- No OMB memo that rescinds M-25-21.
- No ISO catalogue data. All ISO pages were blocked, so no ISO rows were added. TR 24027 and TS 12791 are not in the table and remain candidates.

## Conflicts
- The NIST CAISI page title (CAISSI, "SI" systems) conflicts with search results and news, which still use "Center for AI Standards and Innovation". The primary page was recorded as it reads on 2026-10-16.
- US-NIST-037 was UNVERIFIABLE_OTHER in phase 2. It is now resolved as PASS.

## Documents the user must download by hand
1. Treasury Board of Canada Secretariat, *Directive on Automated Decision-Making* (current version; record the "Date modified"), https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592. The site rejects the fetch tool. This is needed for all 24 Canada rows and for the version and review-status checks.
2. The ISO catalogue pages, opened in a browser (free abstract and status only, no purchase) for:
   - ISO/IEC 42001
   - ISO/IEC 23894 (/standard/77304.html)
   - ISO/IEC 42005
   - ISO/IEC 42006
   - ISO/IEC TS 42119-2 (/standard/84127.html)
   - ISO/IEC TR 29119-11 or its successor
   - ISO/IEC TR 24027
   - ISO/IEC 24029-2 (/standard/79804.html)
   - ISO/IEC 25059 (/standard/80655.html)
   - ISO/IEC TS 12791
   - ISO/IEC 27090

   iso.org returns 403 to the fetch tool. For each page, record the stage code and date, the publication date and any revision. Catalogue IDs 79016, 77607 and 84110 are unconfirmed guesses.
3. Optional: the NCCoE Cyber AI Profile project page, https://www.nccoe.nist.gov/node/2581, which returned 403.
