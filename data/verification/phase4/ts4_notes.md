# ts4 notes (retrieval date 2026-10-28)

Research, not legal advice. Free tools only. Web content was read only through WebFetch and WebSearch.

## Read this first: coverage is partial

- The shared WebSearch budget (200 per turn, all agents) was already used up. Seven of my searches ran (all for Task B, listed below); 4 further searches (DoH, DIFC, NIST, TBS) were refused for budget.
- WebFetch refused most URLs with URL_NOT_ON_ALLOWLIST (a tool side restriction, not a site block). The tool said not to repeat those fetches, and I did not. No workaround was used.
- Result: of 181 items in `data/time_sensitive.csv`, 22 are confirmed, 5 are not_found (not re-seen), 154 are blocked (not re-verified; earlier value carried). `blocked` in ts4_status.csv for these rows means "not re-read on 2026-10-28", with the reason in conflict_or_note. Nothing in them should be read as a changed or confirmed value.
- No item was found to have changed. That is not evidence of stability for the 154 unread items.

## Task A: answers to the eight points

1. DoH Responsible AI Standard V1 (revision due Oct 2026): NOT DETERMINED. The V1 PDF, the policies listings (EN, AR) and the Protocol PDF were all refused by the tool. Only the 2018 policy file (Policy/AI/0.9, 30 Apr 2018) loaded. No evidence of a V2 either way.
2. DIFC Regulation 10 amendments: a DIFCA Consultation Paper (June 2026; cover "No. 3", body "No. 2 of 2026"; deadline 18 July 2026) proposes updating Reg 10 and adding a new Reg 11. No enactment seen, but the DIFC legal database and enactment news pages were refused, so enacted versus still consultation is NOT determined.
3. EU AI Act: NOT RE-CHECKED. Every EUR-Lex, Cellar and Commission URL was refused. Application dates, corrigenda (the German corrigendum of 29.9.2026), harmonised standards after 14 Oct 2026 (Decision 2026/2274 listed EN 18286:2026) and further amending acts remain as recorded on 2026-10-16.
4. Saudi: NCA AICG-1:2026 English PDF cover still reads "Draft of AI Cybersecurity Guidelines"; the NCA Arabic consultation page lists it as closed (page stamp 20/08/2026); NCA EN news item dated 05/07/2026 gave feedback deadline 5 Aug 2026; no final version seen; NCA regulatory documents page 1 shows no AI document. SDAIA: dgp.sdaia.gov.sa English PDF is AI Ethics Principles Version 1.0, September 2023 (no draft/final label); sdaia.gov.sa files (2025 principles PDF, GenAI Guidelines, AI Adoption Framework) returned "Request Rejected" (twice each for the first two, twice for the third); National AI Risk Management Framework not reachable. No final SDAIA or NCA AI instrument was found.
5. Korea enforcement decree: NOT DETERMINED. KLRI English still shows Presidential Decree No. 36053 of 21 Jan 2026 (Art. 24(1) exponent still garbled). law.go.kr was refused, so the later Decree No. 36580 (18 Aug 2026) seen on 16 Oct was not re-checked.
6. Canada Directive on Automated Decision-Making: BLOCKED (tbs-sct.canada.ca returned URL_NOT_ON_ALLOWLIST). Current version not known from this run.
7. NIST: AI 800-2 page (nist.gov/node/1905466) still says initial public draft, released 2026-01-30, page updated 2026-02-10, comments to 2026-03-31; no final seen. The page text uses the acronym CAISI; the CAISI program page itself was refused, so the naming question (CAISI versus "CAISSI" seen on 16 Oct) is NOT re-checked. OMB index still lists M-25-21 and shows no AI memo after M-26-04 (11 Dec 2025).
8. UAE federal, new instruments since 16 Oct: none seen on the u.ae AI resources page (updated on 25 Sep 2026), ai.gov.ae publications (newest items 2023) or the charter page (updated on 03 Jul 2026). Coverage is thin (u.ae policy index, Cabinet and WAM news were not reachable).

Other re-confirmed items: AISI blog posts (12 Oct and later), UK AI Playbook (10 Feb 2025), AI Verify framework (29 May 2025), China Order No. 21, ISO/IEC 23894 (60.60, 2023-02), ISO/IEC 42006 (60.60, 2025-07).

## Task B: moved sources

| Row | Verdict | Note |
|---|---|---|
| UAE-Federal-009 | MINOR | Moved to u.ae asset address; page locator approx. pp.78-79 not 76-77 |
| UAE-Federal-012 | MINOR | Locators and "has defined" wording adjusted |
| UAE-Federal-021 | PASS | Old u.ae URL resolves again; same text at assets.u.ae |
| UAE-Federal-027 | MINOR | "during this time" qualifier missing |
| UAE-Federal-031 | PASS | Old u.ae URL resolves again |
| UAE-Dubai-008 | UNVERIFIED_BLOCKED | 21.9 MB PDF: SERVER_ERROR then refused repeat |

Official addresses found:
- AI Adoption Guideline in Government Services: https://assets.u.ae/api/public/content/efd38f961c104415a22db5e177a73e02?v=57989b9e (listed on https://u.ae/en/about-the-uae/digital-uae/digital-technology/artificial-intelligence/ai-resources and https://ai.gov.ae/publications/). The ai.gov.ae publications page text shows no link targets, and shows no Arabic edition for the guideline.
- AI Ethics: https://u.ae/-/media/AI-publications/MOCAI-AI-Ethics-EN-1.pdf (works again); also https://assets.u.ae/api/public/content/893c940c21c4403ea8df7faad66a889e?v=b2f9c1a1 (listed as "AI Ethics Guide").
- Self assessment: https://ai.gov.ae/aiethics-self-assessment/ (works again).
- National AI Strategy 2031 PDF: https://u.ae/-/media/AI-publications/UAE-National-Strategy-for-Artificial-Intelligence-2031.pdf (works again); u.ae also lists https://assets.u.ae/api/public/content/deed2bf9d68244ab8119c27f2c52813f?v=87559d49 (not allowlisted, not read).
- Dubai AI Integration Matrix: publication page https://www.digitaldubai.ae/knowledge-hub/publications/ai-integration-matrix-framework-for-government-organizations; PDF address unchanged.

Caveat: all reads of PDFs went through the fetch tool's summarising step, not raw text; page numbers are tool reported and approximate. No PDF was saved locally, so no local text extraction was done.

## Searches run

1. "UAE AI Adoption Guideline in Government Services pdf"
2. "Dubai AI Integration Matrix Framework for Government Organizations Dubai Digital Authority"
3. "UAE National Strategy for Artificial Intelligence 2031 pdf u.ae"
4. "UAE AI Ethics Principles and Guidelines pdf ai.gov.ae"
5. "ai.gov.ae AI Adoption Guideline in Government Services AI-Report-EN-V7 pdf"
6. "u.ae AI adoption guideline government services ..." (domains u.ae, ai.gov.ae, government.ae, uaelegislation.gov.ae)
7. "digitaldubai.ae AI Integration Matrix Framework pdf publications" (domains digitaldubai.ae, dubai.ae, mediaoffice.ae)

Refused for budget (not run): DoH Responsible AI Standard version 2; DIFC Regulation 10 amendments 2026; NIST AI 800-2 final or draft; Treasury Board Directive on Automated Decision-Making current version.

## Sources fetched, with outcome

Read: ai.gov.ae self assessment page; u.ae strategy PDF; u.ae AI ethics PDF; assets.u.ae AI Adoption Guideline; assets.u.ae AI Ethics Guide; ai.gov.ae/publications; u.ae AI resources page; u.ae charter page; digitaldubai.ae publication page and news item; mediaoffice.ae Dubai release; DIFC consultation paper; NCA EN and AR consultation pages, EN news item, regulatory documents page; NCA English draft PDF (upload 9ae38ab1); dgp.sdaia.gov.sa English ethics PDF; DoH 2018 policy file; nist.gov/node/1905466; OMB memoranda index; ISO pages 23894 and 42006; KLRI decree page; AISI blog index and two posts; UK AI Playbook page; AIVF what-is-AI-Verify and resources pages; CAC Order 21 page.

Blocked with "Request Rejected" (retried once, then stopped): moj.gov.ae AI Adoption Guideline mirror; sdaia.gov.sa ai-principles.pdf; sdaia.gov.sa GenAIGuidelinesForGovernmentENCompressed.pdf; sdaia.gov.sa AIAdoptionFramework.pdf.

Failed: digitaldubai.ae AI Integration Matrix PDF (SERVER_ERROR, then repeat refused; 21.9 MB).

Refused as URL_NOT_ON_ALLOWLIST (one attempt each, not repeated): all EUR-Lex, Cellar, Commission, JTC21 URLs; DoH RAI Standard PDF, policies listings (EN, AR), Protocol PDF; DIFC Regulation PDF, legal database, enactment news; nist.gov AI RMF page, CAISI page; csrc.nist.gov; tbs-sct.canada.ca; iso.org 42001 and others listed in the status file; SDAIA executive summary; SPA items; dgp.sdaia accreditation and ethics assessment pages; SFDA; uqn.gov.sa; gov.uk King's Speech and ATRS hub; IMDA MGF Agentic PDF; AIVF assurance page and factsheet; playbooks.aip.gov.sg; law.go.kr; MSIT 1238; cao.go.jp plan page; CAC draft notice; openstd; tc260; CSC PDF; u.ae strategy page; Agentic AI page; mediaoffice AI authority release; Digital Dubai State of AI news; DESC; DFSA; CBUAE rulebook; NCA upload cbf45381 and Arabic PDF.

Not attempted: Japan law translation page, CAC items other than Order 21 and the draft notice, GCC pages for Qatar, Oman and Kuwait, SASO, UK bills page, laws.boe.gov.sa, SDAIA bias PDF, openstd items other than GB/T 45654, the Arabic dgp.sdaia.gov.sa ethics PDF, DIFC Regulation 10 pages.

## Searched for and not found

- Any DoH Responsible AI Standard V2 or revised text: not searched (budget), not seen.
- Any final NCA AI cybersecurity guideline: not seen on pages read.
- Any new federal AI instrument since 16 Oct 2026: not seen on pages read.
- An Arabic edition of the AI Adoption Guideline on ai.gov.ae publications: none listed.
- The ethical validation workflow of UAE-Dubai-008 in the press release: not described there.

## Documents to download by hand

1. Digital Dubai, AI Integration Matrix Framework for Government Organizations (21.9 MB). https://www.digitaldubai.ae/docs/default-source/publications/the-ai-integration-matrix-framework-1.pdf?sfvrsn=820a85b0_2 . To check Ch. 10.2 and 10.3 (printed p.87) for UAE-Dubai-008, and front matter version and date.
2. DoH Responsible AI Standard V1 and the DoH policies/standards listing. https://www.doh.gov.ae/-/media/Feature/Resources/Standards/2025/Responsible-AI-Standard-V1.ashx and https://www.doh.gov.ae/en/resources/policies . To check the control table (revision due Oct 2026) and whether a new version exists.
3. DIFC legal database entry for the Data Protection Regulations. https://www.difc.com/business/laws-and-regulations/legal-database . To see whether the June 2026 amendments were enacted.
4. EUR-Lex Regulation (EU) 2026/1744 page and consolidated 2024/1689. https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng . For corrigenda or amending acts after 16 Oct 2026; also the OJ L series after 14 Oct 2026 for harmonised standard citations.
5. Treasury Board Directive on Automated Decision-Making. https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592 . For current version and amendment date.
6. Korea enforcement decree on the Korean law portal. https://www.law.go.kr/LSW/lsInfoP.do?lsNm=인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 시행령 . For the current decree number.
7. NIST CAISI page. https://www.nist.gov/caisi . For naming.
8. SDAIA 2025 AI Ethics Principles, GenAI Guidelines for Government, AI Adoption Framework and National AI Risk Management Framework (sdaia.gov.sa files listed in the status file). Returned Request Rejected.
9. NCA AICG-1:2026 English PDF page 8. To re-find the "not mandatory" sentence recorded on 16 Oct but not re-seen on 28 Oct; also the Arabic PDF cover.
10. AI Adoption Guideline in Government Services, page check of Execution and Initiation stages (approx. pp.74-79) in the u.ae PDF, to settle exact printed page numbers.
11. IMDA Model Governance Framework for Agentic AI PDF cover, and LLM Starter Kit PDF cover (binary returned), to settle versions and dates.
