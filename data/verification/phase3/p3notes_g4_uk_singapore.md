# Phase 3 notes: g4_uk_singapore (retrieved 2026-10-16)

## Method
- Web access was by WebFetch and WebSearch only. For PDFs, WebFetch returned the binary and saved it locally. I extracted the text layer locally with PyMuPDF, then checked printed page numbers against the PDF pages. I read the MGF GenAI cover, which is image-only, from a rendered image.
- I read the long GOV.UK AI Playbook HTML (about 260k characters) in full, using offsets 0, 80000, 88000, 100000 and 200000.
- The permission timeouts from phase 2 (AISI About, Inspect, MGF GenAI, Cataloguing LLM Evaluations) were tool problems. All of these fetched without error on retry.

## Searches run (2026-10-16)
- "UK artificial intelligence bill introduced Parliament 2026 frontier AI legislation". Results were mostly secondary, so I used them only to find the King's Speech.
- "King's Speech 2026 background briefing notes gov.uk artificial intelligence" (gov.uk only).
- "AI Security Institute pre-deployment evaluation report published 2026" (aisi.gov.uk and gov.uk only).
- "AI Playbook for the UK Government" updated 2026 new version.
- AI Verify Testing Framework latest version 2026.
- AI Verify Foundation AI Tester Accreditation Programme / Global AI Assurance Sandbox.
- IMDA MGF Agentic AI v1.5 press release (imda.gov.sg, aiverifyfoundation.sg and mddi.gov.sg only).
- Global AI Assurance Pilot main report.
- Singapore government agencies IM8 / LLM testing requirement / GovTech (two queries).
- IMDA starter kit for testing agentic AI 2026 (three queries).

## Sources fetched and outcome
- GOV.UK AI Playbook HTML and publication page: OK. Still the 10 Feb 2025 edition, with no update shown.
- ATRS scope policy (17 Dec 2024), ATRS guidance (updated 8 May 2025) and ATRS hub: OK.
- DSIT Introduction to AI assurance (12 Feb 2024): OK.
- AISI approach to evaluations (9 Feb 2024), aisi.gov.uk/about, research-agenda, blog index, and the Mythos, Microsoft, GPT-6 Astra and 12 Oct 2026 best-practice posts: all OK.
- inspect.aisi.org.uk: OK.
- King's Speech 2026 (gov.uk): OK.
- bills.parliament.uk search: HTTP 403 on both attempts, so I stopped (blocked).
- IMDA LLM Starter Kit PDF (v1.0, Jan 2026): OK.
- MGF GenAI PDF (aiverifyfoundation.sg): OK. The cover reads "Published 30 May 2024".
- MGF Agentic AI v1.5 PDF (imda.gov.sg): OK. This is v1.5, 20 May 2026, updated 5 June 2026. It was readable this time.
- Cataloguing LLM Evaluations PDF (Oct 2023 draft): OK.
- AIVF pages (what-is-ai-verify, resources, home, tester-accreditation, ai-assurance), the AI TAP factsheet PDF (19 May 2026) and the AI Verify Testing Framework PDF (file.go.gov.sg): all OK.
- IMDA press release list: OK. However, the press release of 14 Oct 2026 ("New Initiatives to Strengthen AI Safety and Resilience") returned only its title and date, with an empty body, on 2 fetches.
- The IMDA AI page (anchor for the agentic starter kit) had no document link in the fetched text, on 2 fetches.
- My guessed PDF URL for the agentic starter kit returned 404.
- GovTech Responsible AI Playbook Litmus page: OK (updated 29 Jul 2026). The first path I tried returned 404; I then used the correct path from search.

## Findings worth flagging
- Singapore-035 was withdrawn in error. Page 40 of MGF Agentic v1.5 has the Google x Singapore Government case study inside s.2.3.2. Reinstate it with the patch. The source says extraneous personal details appeared "in a significant number of cases", which is stronger than the row's wording.
- The rows on MGF Agentic AI (Singapore-031 to 034) cite v1.0 pages. In v1.5 the pages are:
  - Executive Summary: pp.3-4
  - s.2.3.2: pp.38-40
  - s.2.3.3: pp.42-45
  - These rows are outside this group, but they need re-pointing.
- MGF GenAI date: the cover says 30 May 2024. "19 June 2024" is the file name and PDF build date. I coded this as MINOR because the content is unaffected.
- The AI Playbook uses must-language for SDO standards compliance and for Secure by Design before deployment (UK-011, UK-007).

## Searched for and NOT found
- No UK government AI bill and no statutory AI testing duty. None is in the King's Speech of 13 May 2026.
- No published AISI pre-deployment access agreement text, such as an MOU.
- No new edition of the AI Playbook.
- No 2026 revision of the AI Verify Testing Framework.
- No public instrument, such as IM8 or a Government Instruction Manual, that makes the IMDA Starter Kit, AI Verify or the MGFs binding on Singapore public agencies.
- No primary text of the new agentic starter kit.

## Conflicts between sources
- MGF GenAI: the cover date (30 May 2024) differs from the file name date (19 June 2024).
- MGF Agentic: the IMDA press release page shows "last updated 21 May 2026", while the PDF cover says "Updated 5 June 2026". The PDF metadata creation date is 17 Jul 2026.
- AI TAP: the factsheet (19 May 2026) says the programme is "expected to be available in 3Q26". The AIVF accreditation page already lists 5 accredited firms (AIDX, Knovel, PwC, Resaro, Vulcan) and still says it is expected 3Q 2026.

## Documents the user must download by hand
1. **IMDA, "Starter Kit for Testing Agentic Systems for Safety and Reliability"** (October 2026).
   - Where: the AIVF Resources page (https://aiverifyfoundation.sg/resources/, item 1) links to https://www.imda.gov.sg/about-imda/emerging-technologies-and-research/artificial-intelligence#911f57f5-cbed-4db0-8cea-8f427d184b83.
   - Why: it is a new pre-deployment testing guideline for agents, but its link is rendered dynamically and the PDF was not reachable by fetch.
   - What to record: version, date, status (voluntary or not) and the step and metric sections.
2. **IMDA press release "Singapore Introduces New Initiatives to Strengthen AI Safety and Resilience" (14 Oct 2026)**.
   - Where: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/new-initiatives-to-strengthen-ai-safety-and-resilience
   - Why: the body was empty when fetched. Save it as a PDF.
3. **UK Parliament bills search for AI-related bills in the 2026-27 session**.
   - Where: https://bills.parliament.uk/
   - Why: it returned HTTP 403. Check for any AI or superintelligence private members' bill and its stage.
4. Optional: **AIVF "Global AI Assurance Pilot 2025 Main Report"**.
   - Where: https://aiverifyfoundation.sg/ai-assurance/2025-main-report/
   - Why: I did not read it in full.
