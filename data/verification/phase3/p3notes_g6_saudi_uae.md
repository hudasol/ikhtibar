# Phase 3 notes: g6_saudi_uae (retrieved 2026-10-16)

## Searches run (all 2026-10-16, WebSearch)
- NCA "AI Cybersecurity" controls OR guidelines final 2026 site:nca.gov.sa
- Arabic: "irshadat / dawabit al-amn al-sibrani lil-dhaka al-istina'i" nca.gov.sa
- "Generative AI Guidelines" SDAIA pdf (dgp.sdaia.gov.sa / ndmo / spa.gov.sa)
- SDAIA "AI Adoption Framework" pdf
- SDAIA "AI Ethics Principles" version 2.0
- SDAIA National AI Risk Management Framework 2026 (English and Arabic)
- sdaia.gov.sa National AI Risk Management Framework pdf (domain-restricted)
- istitlaa SDAIA responsible AI policy 2026 (Arabic)
- laws.boe.gov.sa nizam al-dhaka al-istina'i; ICAIRE basic statute
- SFDA AI/ML medical devices MDS-G010 (general and domain-restricted to sfda.gov.sa)
- SASO AI technical regulation / conformity assessment
- Qatar QCB AI guideline; Qatar NCSA/MCIT AI guidelines; Oman MTCIT AI policy (English and Arabic); Kuwait CITRA AI; Bahrain AI policy

## Sources fetched and outcome
| Source | Outcome |
|---|---|
| sdaia.gov.sa GenerativeAIPublicEN.pdf | Request Rejected, retried once, stopped |
| sdaia.gov.sa AIAdoptionFramework.pdf | Request Rejected, retried once, stopped |
| sdaia.gov.sa GenAIGuidelinesForGovernmentENCompressed.pdf | Request Rejected, retried once, stopped |
| sdaia.gov.sa ResearchLibrary/ExecutiveSummaryEn.pdf (National AI RMF) | Request Rejected, retried once, stopped |
| sdaia.gov.sa ResearchLibrary/AIMarketGovernanceTools.pdf | Request Rejected, retried once, stopped |
| sdaia.gov.sa Documents/ai-principles.pdf ("2025 AI Ethics Principles") | Request Rejected, retried once, stopped |
| dgp.sdaia.gov.sa home, Knowledge Center | Read. Lists PDPL instruments and two AI services. Does not list the GenAI, Adoption or RMF documents |
| dgp.sdaia.gov.sa AI service provider accreditation; AI Ethics Assessment | Read (Arabic) |
| dgp.sdaia.gov.sa ai-principles-AR.pdf | Read. Cover: first edition, September 2023 |
| cdn.nca.gov.sa AI_Cybersecurity_Controls_EN.pdf (both UUIDs, identical file) | Fetched. Body text is in images, so the returned PDF was rendered locally and read page by page (pp. 1, 8, 16-23) |
| nca.gov.sa news page (EN and AR); public-consultations listing (EN and AR); regulatory-documents p. 1 | Read. guidelines-list URL returned 404 |
| spa.gov.sa N2633725 (AR), N2633781 (EN) | Headline only: no body and no date |
| uqn.gov.sa 4001603, 4001598 | Read: Royal Decree M/77 and the ICAIRE Basic Statute |
| laws.boe.gov.sa search | ECONNREFUSED twice, stopped |
| sfda.gov.sa MDS-G010ML.pdf | Fetched. Text layer read locally |
| sfda.gov.sa /en/regulations/87661 | 404 |
| digitaldubai.ae ai-ethics.pdf | Fetched. Text layer read locally |
| qcb.gov.qa QCB_Artificial_Intelligence_Guideline.pdf | TLS error "unable to verify the first certificate", twice, stopped |
| ncsa.gov.qa AI-Guide-en-V6.pdf | Landing page containing only "Ncsa", twice, stopped |
| iga.gov.bh article on the national AI policy | Read |

Method note: WebFetch could not decode the binary PDFs. The fetch tool saved each file, and I extracted text from that file locally with pdftotext. For the image-only NCA pages I rendered each page and read it visually. No other access route was used.

## Searched for and NOT found
- A final (non-draft) NCA AI cybersecurity document.
- An Arabic PDF of the NCA draft. This means the phase 2 claim that the Arabic cover says "Controls (AICC-1:2026)" could not be re-checked.
- An official SDAIA "AI Ethics Principles 2.0".
- Any readable primary text of the National AI RMF, the GenAI guidelines (public and government) or the AI Adoption Framework on a host other than sdaia.gov.sa.
- A SASO AI technical regulation.
- An AI statute on laws.boe.gov.sa. The site was blocked. The only AI statute seen on the official gazette is the ICAIRE basic statute, which has no testing provisions.
- The official texts of the Oman MTCIT policy and of any Kuwait CITRA AI instrument.

## Conflicts
- **NCA title:** The English cover and every official Arabic web page say "Guidelines" (AICG-1:2026). "Controls" appears only in the PDF file name. Phase 2's "AICC" Arabic-cover claim remains unconfirmed.
- **SDAIA Ethics Principles edition:** The official Arabic cover says first edition, September 2023. Secondary sources call a September/October 2023 release "2.0".
- **National AI RMF date:** A search listing gives the sdaia.gov.sa summary title as "April 2026". Phase 2 noted that SPA reported a July 2026 launch. Not resolved from primary text.
- **UAE-Dubai-017:** Phase 2 could not confirm the qualifier "to the extent permitted by technology". It is present (Security principle, printed p. 9).

## Documents the user must download by hand
1. SDAIA, *Generative Artificial Intelligence for Public Guidelines* (2025), https://sdaia.gov.sa/en/SDAIA/about/Files/GenerativeAIPublicEN.pdf. Needed for Saudi-011 to Saudi-013. The site rejects the fetch tool.
2. SDAIA, *Artificial Intelligence Adoption Framework* (2025), https://sdaia.gov.sa/en/SDAIA/about/Files/AIAdoptionFramework.pdf. Needed for Saudi-014 to Saudi-016 (pp. 22-23, 38-39). Same reason.
3. SDAIA, *National AI Risk Management Framework*, English executive summary (April 2026), https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/ExecutiveSummaryEn.pdf, plus the Arabic full text from the same site. Needed for Saudi-017 and for what the framework says about testing. Same reason.
4. SDAIA, *Generative AI Guidelines for Government* (2025), https://sdaia.gov.sa/en/SDAIA/about/Files/GenAIGuidelinesForGovernmentENCompressed.pdf. Not yet in the table. Same reason.
5. SDAIA, *AI Ethics Principles* (2025 file), https://sdaia.gov.sa/en/SDAIA/about/Documents/ai-principles.pdf. Needed to settle whether a newer edition replaces v1.0. Same reason.
6. NCA, Arabic PDF of the draft AI Cybersecurity Guidelines. No URL was found. It may be available through Istitlaa or from NCA directly. Needed to check the Guidelines-vs-Controls naming.
7. Qatar Central Bank, *Artificial Intelligence Guideline* (2024), https://www.qcb.gov.qa/Services/Financial%20Technology/QCB_Artificial_Intelligence_Guideline.pdf. Fails with a TLS certificate error.
8. Qatar NCSA, *Guidelines for Secure Adoption and Usage of AI* (2024), https://www.ncsa.gov.qa/sites/default/files/2024-02/AI-Guide-en-V6.pdf. Returns an empty landing page.
9. Saudi laws: a search of laws.boe.gov.sa for "الذكاء الاصطناعي". The connection was refused.
