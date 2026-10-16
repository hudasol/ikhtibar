# Phase 3 notes: g7_uae (UAE discovery and status checks)

Retrieval date for everything below: 2026-10-16. Only WebSearch and WebFetch were used for web access. Four PDFs came back from WebFetch as binary the tool could not decode: the CSC AI policy v1.1, the DoH Responsible AI Standard, the DoH Responsible AI Risk Management Protocol and the DIFC DP Regulations, Consultation Paper and Annex A. WebFetch saved each file locally. Their text was extracted from those saved copies with pypdf, in an isolated scratch folder. No second download was made. Search results were used only to find primary sources and are not cited as evidence.

Outputs: `p3new_g7_uae.csv` (16 new rows), `p3ts_g7_uae.csv` (18 status items).

## Searches run (all 2026-10-16)

| # | Query | Use |
|---|---|---|
| 1 | Abu Dhabi Government AI policy Department of Government Enablement government entities (extended) | Only the Digital Strategy 2025-2027 came up; no policy text |
| 2 | Dubai AI Security Policy DESC government entities requirements | Secondary coverage only |
| 3 | UAE federal law artificial intelligence 2026 decree-law (extended) | No federal AI law; led to AI and Data Authority and CBUAE note |
| 4 | dge.gov.ae artificial intelligence policy OR standard OR guideline government entities Abu Dhabi responsible AI (extended) | No DGE AI policy |
| 5 | سياسة الذكاء الاصطناعي حكومة أبوظبي دائرة التمكين الحكومي الجهات الحكومية | Only DGE programmes and news; no policy |
| 6 | "Abu Dhabi" "AI policy" government entities ADDA OR "Digital Authority" responsible AI policy document pdf (extended) | Nothing found |
| 7 | Dubai AI policy government entities launched Dubai AI Week 2025 Digital Dubai policy document (extended) | Found the Apr 2025 "AI Policy for Government Entities" (news only) |
| 8 | "AI Policy for Government Entities" Dubai pdf digitaldubai.ae (extended) | No PDF |
| 9 | سياسة الذكاء الاصطناعي للجهات الحكومية في دبي دبي الرقمية وثيقة | News only |
| 10 | "Dubai AI Security Policy" pdf desc.gov.ae (extended) | No PDF; DESC releases documents by e-mail request |
| 11 | Central Bank UAE guidance artificial intelligence machine learning licensed financial institutions 2026 | CBUAE Guidance Note 23 Feb 2026 located |
| 12 | centralbank.ae "Guidance Note" artificial intelligence machine learning consumer protection pdf rulebook | Same |
| 13 | rulebook.centralbank.ae guidance note consumer protection responsible adoption ... | Same |
| 14 | u.ae UAE National Strategy for Artificial Intelligence 2031 page updated (allowed_domains u.ae) | Strategy page located |
| 15 | "Artificial Intelligence and Data Authority" UAE Cabinet established decree 2026 | 14 Jun 2026 authority; no instrument |
| 16 | مرسوم بقانون اتحادي الذكاء الاصطناعي 2026 الإمارات قانون تنظيم الذكاء الاصطناعي | No AI decree-law |
| 17 | DIFC Data Protection Regulations amendment 2025 OR 2026 consolidated version Regulation 10 autonomous systems | Located 2023 and 2025 items |
| 18 | DIFC enacts amended Data Protection Regulations 2026 Regulation 10 safety Autonomous Systems Officer Regulation 11 | Consultation (Jun 2026) located; no enactment found |
| 19 | Abu Dhabi "AI" "government entities" policy OR framework OR standard governance testing 2026 site:dge.gov.ae OR site:mediaoffice.abudhabi | Nothing new |
| 20 | Artificial Intelligence and Advanced Technology Council Abu Dhabi AIATC policy regulation AI governance framework 2025 2026 | No AIATC instruments; reconstitution resolution (news) |
| 21 | Dubai generative AI guidelines government employees Dubai Digital Authority OR "Dubai Government" generative AI policy usage | MBRSG survey report only |
| 22 | dlp.dubai.gov.ae artificial intelligence Executive Council Resolution 2025 OR 2026 Dubai law AI regulation | Nothing |
| 23 | قرار المجلس التنفيذي دبي الذكاء الاصطناعي 2025 2026 تنظيم استخدام الذكاء الاصطناعي الجهات الحكومية | Nothing |
| 24 | ADGM FSRA artificial intelligence guidance OR consultation paper 2025 2026 AI model risk testing | Nothing from FSRA; led to the DFSA letter |
| 25 | UAE Cyber Security Council AI guidance 2026 generative AI security guideline OR "AI Security" csc.gov.ae | No new CSC AI guidance |
| 26 | DFSA "Dear SEO" letter artificial intelligence risk management June 2026 dfsa.ae | DFSA letter of 4 Jun 2026 located |
| 27 | UAE government AI procurement guidelines federal entities 2025 OR 2026 ... agentic AI government framework | Agentic AI guide (news); MoF AI procurement workshop |
| 28 | "AI Procurement Guidelines" UAE government pdf | No PDF |

## Fetches and outcomes (all 2026-10-16)

| URL | Outcome |
|---|---|
| https://www.desc.gov.ae/regulations/standards-policies/ | OK. 6 documents, none on AI, each by e-mail request |
| https://www.dge.gov.ae/en/laws-resolutions-circulars | OK. 5 documents (DGE law, HR law and bylaws, BCMS policy, employee code of conduct 2026); none on AI |
| https://www.digitaldubai.ae/standards-and-policies | OK. Only AI item is the AI Ethics Principles & Guidelines (already in table) |
| digitaldubai.ae news item on the State of AI Report and the AI policy | OK. Names the "AI Policy for Government Entities"; no link to its text |
| https://www.desc.gov.ae/dubai-electronic-security-center-launches-the-dubai-ai-security-policy/ | OK. No link, scope, binding status or testing content |
| CSC National Cyber Security Policy for AI v1.1 PDF (csc.gov.ae) | OK (binary returned; text extracted from it). Was blocked in phase 2; now read in full, 55 pp. Rows UAE-Federal-P3-01 to 08 |
| https://www.centralbank.ae/media/mykn5fue/...-en.pdf (press release) | HTTP 404, retried, 404 again. Stopped |
| https://docs.modulos.ai/frameworks/uae-consumer-ai | Secondary, used only to locate the rulebook URL |
| https://rulebook.centralbank.ae/en/entiresection/6958 | HTTP 403, retried, 403 again. Blocked |
| u.ae Charter page (EN) | OK. Updated On 03 Jul 2026; content unchanged |
| uaelegislation.gov.ae Charter policy page | HTTP 403 twice. Blocked |
| https://ai.gov.ae/ | HTTP 403 twice. Blocked |
| u.ae AI resources page | OK. Updated On 23 Sep 2026; resource list recorded |
| assets.u.ae National AI Strategy PDF (new address) | Failed: over the tool's 10 MB limit (not a site block) |
| u.ae "AI in government policies" page | OK. Updated On 06 Oct 2026; no AI law listed |
| u.ae UAE Strategy for AI page | OK. Updated On 30 Dec 2024; no revision |
| mediaoffice.ae 14-06-2026 AI and Data Authority release | OK. No legal instrument cited |
| https://www.doh.gov.ae/en/resources/policies | OK (phase 2 failure now resolved). Only the 2018 AI policy is listed |
| https://www.doh.gov.ae/ar/resources/policies | OK. Arabic title of the 2018 policy recorded |
| https://www.doh.gov.ae/en/resources/standards | OK, but the list renders empty (script-populated) |
| https://www.doh.gov.ae/en/resources/standards-rss-feed | OK. No AI items among the entries |
| DoH Responsible AI Standard V1 PDF | OK (binary returned; text extracted). Still V1 |
| DoH Responsible AI Risk Management Protocol PDF (8BD7C5DE...ashx) | OK (binary returned; text extracted). Rows UAE-AbuDhabi-DoH-P3-01 to 04 |
| https://www.difc.com/business/laws-and-regulations/legal-database | OK, read with offset 0 and 100000. June 2026 consultation listed; no 2026 enactment notice |
| DIFC DP Regulations consolidated PDF | OK (binary returned; text extracted). Still Version No. 2 |
| DIFC consultation-paper.pdf (June 2026) | OK (binary returned; text extracted) |
| DIFC annex-a---proposed-changes.pdf | OK (binary returned; text extracted). Rows UAE-DIFC-ADGM-P3-01 to 04 |
| https://www.dge.gov.ae/en/news/adg-digital-strategy-update-2025 | OK. 30 Sep 2025 page. Responsible-AI wording and Chief Data and AI Officers, but no testing, evaluation or assurance requirement, so no row |
| https://uaemodel.egsep.ae/agentic_ai_guide_website.html | HTTP 403, retried, 403 again. Blocked |
| https://www.aiatc.ae/ and https://aiatc.ae/ | DNS failure (ENOTFOUND). The domain does not resolve |
| https://tdra.gov.ae/ | OK. No AI governance documents |
| https://tdra.gov.ae/ar/About/regulations-and-ruling | OK. No AI or digital-government titles |
| assets.u.ae Generative AI guide (100 Practical Applications, Apr 2023) | OK (binary returned; text extracted). Only advice to users on checking output accuracy; no system testing, so excluded |
| digitaldubai.ae Dubai State of AI Report PDF | Failed: over the 10 MB limit |
| https://www.dfsa.ae/your-resources/publications-reports/seo-letters-1 | HTTP 403 twice. Blocked |
| u.ae Agentic AI for Government Services page | OK. Last updated 30 Sep 2026; no testing or assessment requirement |
| https://mof.gov.ae/?p=25743 | HTTP 410 Gone. Page removed, not blocked |
| u.ae National Cyber Security Policy for AI page (EN) | OK. Updated On 02 Jul 2026; points to the v1.1 PDF |

## Searched for and not found

- **Abu Dhabi government AI policy or standard for government entities (DGE or ADDA).** None was found on dge.gov.ae (laws and policies page, digital strategy pages) or through English and Arabic searches. The Digital Strategy 2025-2027 pages read contain no testing, evaluation, validation or assurance requirement. ADDA's functions are now within DGE. The AIATC website does not resolve, and no AIATC instrument was found.
- **Dubai "AI Policy for Government Entities" (April 2025).** The policy exists according to Digital Dubai's own news item, but its text is not published on digitaldubai.ae.
- **Dubai AI Security Policy (DESC, September 2024).** Not published. DESC documents are available only by e-mail request.
- **Dubai generative AI policy for government, and any Dubai Executive Council resolution on AI for 2025-2026.** Neither was found.
- **Federal AI law or Cabinet resolution for 2025-2026.** None was found. The AI and Data Authority was approved on 14 Jun 2026 with no instrument cited. uaelegislation.gov.ae was blocked, so it could not be searched directly.
- **New CSC AI guidance after v1.1.** None was found.
- **TDRA AI guidance.** None was found.
- **Ministry of AI / AI Office procurement or deployment guidelines.** None was found. The MoF page on the AI procurement workshop is gone (HTTP 410), and ai.gov.ae is blocked.
- **The 2025 DoH "AI Policy" cited by the Responsible AI Standard and the Protocol.** It is not on the DoH listing. The two documents give different dates for it (June vs July 2025).
- **Arabic version or title of the DoH Responsible AI Standard.** Not found.
- **DIFC enactment of the June 2026 Regulation 10 amendments.** No enactment notice was found on the legal database.

## Conflicts between sources and with existing rows

1. **UAE-Federal-014 to 017 (CSC AI policy).** These rows are coded ambiguous because their addressees were not seen. The v1.1 PDF states the scope (federal ministries and authorities, non-government CII entities, emirate government entities) and uses "shall" in its policy statements. It also says compliance is monitored through UAE IA Standard Appendix E.2 and the National Cyber Index. Domain 4 is headed "Operational Security" in the PDF but "Operational Safety" on the portal. Status changed: the policy statements should be recoded as mandatory for those entities.
2. **UAE-AbuDhabi-DoH-010 (Standard cl. 3.3.1.2.2.2, conformity assessment for high-risk systems).** Protocol Step 6 says high-risk systems that remain high risk despite controls must be avoided. The Protocol's own DP1 routes only very-high-risk systems to Step 6. This conflicts with the row and is internally inconsistent.
3. **DIFC Regulation 10.** The June 2026 draft would insert a pre-commercial-use "tested for safety verification" condition as new 10.3.2(b). That would renumber the provision now cited in UAE-DIFC-ADGM-003, rewrite the ASO limb (UAE-DIFC-ADGM-004 and -016) and renumber 10.3.4-10.3.5. It is not in force. The Consultation Paper cover says "No. 3" while para 1 says "No. 2 of 2026".
4. **DoH reference dates.** The Standard cites an "AI Policy Standard" of June 2025. The Protocol cites a "DoH AI Policy" of July 2025.
5. **UAE-Federal-004 (agentic AI).** Only secondary sources date the framework reveal to 15 May 2026, against the row's 23 Apr 2026 Cabinet meeting. Unverified, and no change proposed.

## Documents the user must download by hand (blocked or unreadable)

1. **CBUAE, "Guidance Note on the Consumer Protection and Responsible Adoption and Use of Artificial Intelligence and Machine Learning by Licensed Financial Institutions in the U.A.E." (23 Feb 2026).** https://rulebook.centralbank.ae/en/entiresection/6958 returned HTTP 403 twice, and the press-release PDF returned 404. Needed to verify bias-testing and model-validation expectations for a possible UAE-Federal row.
2. **DFSA, "DFSA regulatory expectations on artificial intelligence risk management in the DIFC" (SEO letter, 4 Jun 2026).** Listed at https://www.dfsa.ae/your-resources/publications-reports/seo-letters-1, which returned HTTP 403 twice. Needed for a possible UAE-DIFC-ADGM row on testing and validation.
3. **National Committee for Agentic AI, practical guide for government entities on designing agentic-AI service experiences.** https://uaemodel.egsep.ae/agentic_ai_guide_website.html returned HTTP 403 twice.
4. **UAE Charter policy details page.** https://uaelegislation.gov.ae/en/policy/details/the-uae-charter-for-the-development-and-use-of-artificial-intelligence returned HTTP 403 twice. Needed to confirm the issue date and lead entity.
5. **ai.gov.ae home and publications.** https://ai.gov.ae/ returned HTTP 403 twice. Check for any 2025-2026 AI Office guide on testing or procurement.
6. **UAE National Strategy for AI PDF at its new address.** https://assets.u.ae/api/public/content/deed2bf9d68244ab8119c27f2c52813f?v=87559d49 is over the tool's 10 MB limit. Check whether it differs from the 2018/2019 edition.
7. **Dubai State of AI Report.** https://www.digitaldubai.ae/docs/default-source/publications/dubai-state-of-ai-report.pdf?sfvrsn=a486e23f_5 is over the 10 MB limit. It describes the Dubai AI Policy for Government Entities.
8. **Dubai AI Security Policy (DESC) and Dubai AI Policy for Government Entities (Digital Dubai).** Neither is published. The DESC policy is available by e-mail request only (DESC standards page). These are not free downloads, so they are noted for completeness only.
9. **UAE Information Assurance Standard, Appendix E.2 "National Artificial Intelligence Security Policy".** Referenced in CSC policy s4. A public copy was not located.
