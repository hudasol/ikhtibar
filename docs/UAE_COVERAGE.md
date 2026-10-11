# UAE and Gulf coverage record

Generated from `data/uae_search_log.csv` and `data/uae_sources.csv`. Research, not legal advice. Retrieval date 2026-10-12.

This file records exactly what was searched and where, and, per source, whether an original or a translation was read. It supports Section 6.2 of the report. No claim about what the UAE requires is made from a source that was not retrieved and read.

## How reading was classified

- **english_original**: the English text of the official publication was read.
- **arabic_original**: Arabic wording was obtained, in whole or in part. Where the fetch tool answered in English about an Arabic page, the English rendering is the tool's, not an official translation, and the column "English rendering by fetch tool" says yes. Such renderings are treated as machine produced.
- **not_read**: the document was located but not read, or the fetch failed.

## Summary

| Zone | Searches and fetches logged | English / Arabic queries | Found | Not found | Blocked | Locator only | Sources listed | English read | Arabic wording obtained | of which English rendering by fetch tool | Not read |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UAE federal | 77 | 54 / 23 | 49 | 17 | 11 | 0 | 34 | 16 | 8 | 5 | 10 |
| Abu Dhabi | 59 | 45 / 14 | 34 | 14 | 3 | 8 | 27 | 20 | 4 | 4 | 3 |
| Dubai | 94 | 80 / 14 | 75 | 13 | 6 | 0 | 61 | 40 | 5 | 4 | 16 |

## Sources

| Zone | Title | Issuer | Language read (as recorded) | Class | English rendering by fetch tool | Blocked | URL |
|---|---|---|---|---|---|---|---|
| UAE federal | The UAE Charter for the Development and Use of Artificial Intelligence (u.ae policy page) | UAE Government portal u.ae (charter issued by AI O | English (official portal) | english_original | no | no | https://u.ae/en/about-the-uae/strategies-initiatives-and-awards/policies/Ai/The-UAE-Charter-for-the-Development-and-Use-of-Artificial-Intelligence |
| UAE federal | ميثاق التطوير والاستخدام المسؤول للذكاء الاصطناعي (u.ae Arabic page) | UAE Government portal u.ae | Arabic original (fetch tool returned English summary containing Arabic | arabic_original | yes | no | https://u.ae/ar/about-the-uae/strategies-initiatives-and-awards/policies/Ai/The-UAE-Charter-for-the-Development-and-Use-of-Artificial-Intelligence |
| UAE federal | The UAE Charter for the Development & Use of Artificial Intelligence (PDF) | AI Office (ai.gov.ae); issuer not named in text | English (official) | english_original | no | no | https://ai.gov.ae/wp-content/uploads/2024/07/UAEAI-Methaq-EN2-3.pdf |
| UAE federal | Charter policy page on UAE Legislation portal | Ministry of Cabinet Affairs platform; lead entity  | English (official portal summary) | english_original | no | no | https://uaelegislation.gov.ae/en/policy/details/the-uae-charter-for-the-development-and-use-of-artificial-intelligence |
| UAE federal | AI Office website home | Office of the Minister of State for AI, Digital Ec | English (official) | english_original | no | no | https://ai.gov.ae |
| UAE federal | National Policy for the Promotion of Smart Health Services and AI in the UAE Health Sector | Ministry of Health and Prevention | English (official portal) | english_original | no | no | https://uaelegislation.gov.ae/en/policy/details/national-policy-for-the-promotion-of-smart-health-services-and-artificial-intelligence-in-the-uae-health-sector |
| UAE federal | AI Adoption Guideline in Government Services (English; copy hosted on Ministry of Justice  | Ministry of Cabinet Affairs, Prime Minister's Offi | English (official) | english_original | no | no | https://www.moj.gov.ae/assets/b170a9de/ai-report-en-v7-638538011662280996.aspx |
| UAE federal | AI Adoption Guideline in Government Services (Arabic) | Ministry of Cabinet Affairs / UAE Government | Arabic original (extraction garbled; only short sentences obtained) | arabic_original | yes | no | https://government.ae/-/media/AI-publications/AI-Adoption-Guideline-in-Government-Services--Ar.pdf |
| UAE federal | AI Adoption Guideline in Government Services (Arabic, ai.gov.ae host) | AI Office / Ministry of Cabinet Affairs | Arabic original | arabic_original | no | no | https://ai.gov.ae/wp-content/uploads/2023/03/AI-Report-AR-V7.pdf |
| UAE federal | UAE Position on AI Policy (International Stance) | UAE Government (published at ai.gov.ae); issuer no | English (official) | english_original | no | no | https://www.uaelegislation.gov.ae/en/policy/download/uae-s-international-stance-on-artificial-intelligence-policy |
| UAE federal | Agentic AI for Government Services | UAE Government portal u.ae | Mixed: tool quoted Arabic wording; English summary returned | arabic_original | yes | no | https://u.ae/about-the-uae/digital-uae/digital-technology/Agentic-AI-for-Government-Services |
| UAE federal | Agentic AI practical guide for government entities | National Committee for Agentic AI / egsep.ae | not read | not_read | no | yes | https://uaemodel.egsep.ae/agentic_ai_guide_website.html |
| UAE federal | UAE Cabinet announcement: agentic AI framework for 50% of government within two years | UAE Cabinet | not read | not_read | no | yes | https://uaecabinet.ae/ar/news/under-directives-of-uae-president-and-in-world-first-mohammed-bin-rashid-reveals-new-uae-government-framework-to-deploy-agentic-ai-across-50-of-government-sectors-operations-within-two-years |
| UAE federal | Federal Decree by Law No. 45 of 2021 Concerning the Protection of Personal Data (English) | President of the UAE (Federal Decree-Law); portal  | English version published on official portal (Arabic prevalence not ch | arabic_original | no | no | https://uaelegislation.gov.ae/en/legislations/1972/download |
| UAE federal | المرسوم بقانون اتحادي رقم 45 لسنة 2021 في شأن حماية البيانات الشخصية (Arabic) | President of the UAE | Arabic original (opening sentences of Arts 18(1) and 21(1) only) | arabic_original | no | no | https://uaelegislation.gov.ae/ar/legislations/1972/download |
| UAE federal | Data protection laws (u.ae) | UAE Government portal u.ae | English (official) | english_original | no | no | https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws |
| UAE federal | The National Cyber Security Policy for Artificial Intelligence (u.ae page) | Cyber Security Council (page hosted on u.ae) | English (official portal summary) | english_original | no | no | https://u.ae/en/about-the-uae/strategies-initiatives-and-awards/policies/cyber-activities/The-National-Cyber-Security-Policy-for-Artificial-Intelligence |
| UAE federal | السياسة الوطنية للأمن السيبراني للذكاء الاصطناعي (u.ae Arabic page) | Cyber Security Council | Arabic (portal text; tool returned Arabic quotations; authoring-origin | arabic_original | yes | no | https://u.ae/ar/about-the-uae/strategies-initiatives-and-awards/policies/cyber-activities/The-National-Cyber-Security-Policy-for-Artificial-Intelligence |
| UAE federal | National Cyber Security Policy for Artificial Intelligence v1.1 (full PDF) | UAE Cyber Security Council | not read | not_read | no | yes | https://csc.gov.ae/documents/38662/1042755/National+Cyber+Security+Policy+for+Artificial+Intelligence_v1.1.pdf/aeca22fd-f413-f1ac-a01f-14446e62f982?t=1771617654295 |
| UAE federal | Cyber Security Council home | UAE Cyber Security Council | not read | not_read | no | yes | https://csc.gov.ae |
| UAE federal | UAE National Strategy for Artificial Intelligence 2031 | Office of the Minister of State for AI (AI Office) | English (official) | english_original | no | no | https://u.ae/-/media/AI-publications/UAE-National-Strategy-for-Artificial-Intelligence-2031.pdf |
| UAE federal | Cabinet Resolution No. 13 of 2021 on fees for MOIAT services | UAE Cabinet | Arabic original (OCR garbled) | arabic_original | yes | no | https://uaelegislation.gov.ae/ar/legislations/2001/download |
| UAE federal | AI policies index (u.ae) | UAE Government portal u.ae | English (official) | english_original | no | no | https://u.ae/en/about-the-uae/strategies-initiatives-and-awards/policies/Ai |
| UAE federal | UAE Council for Artificial Intelligence and Blockchain page | AI Office / Council | English (official) | english_original | no | no | https://ai.gov.ae/?p=10623 |
| UAE federal | Digital procurement policy | Ministry of Finance | English (official) | english_original | no | no | https://u.ae/en/about-the-uae/strategies-initiatives-and-awards/policies/economy/digital-procurement-policy |
| UAE federal | AI Ethics Self-Assessment Tool page | AI Office (Minister of State for AI, Digital Econo | English (official) | english_original | no | no | https://ai.gov.ae/aiethics-self-assessment/ |
| UAE federal | AI Guide (National Program for Artificial Intelligence) | Minister of State for AI Office | English (official) | english_original | no | no | https://assets.u.ae/api/public/content/129f71cdf3454d9cba0e6f876a158a83?v=770e53d4 |
| UAE federal | AI Ethics: Principles & Guidelines | UAE AI and Blockchain Council (owner per licensing | English (official) | english_original | no | no | https://u.ae/-/media/AI-publications/MOCAI-AI-Ethics-EN-1.pdf |
| UAE federal | WAM report: Federal Authority for AI and Data established | WAM (news agency) | not read (tool returned site metadata only) | not_read | no | yes | https://www.wam.ae/ar/article/c0pyzva-محمد-بن-راشد-يعتمد-إنشاء-الهيئة-الاتحادية-للذكاء |
| UAE federal | WAM report: National AI Test and Validation Lab | WAM (news agency) | not read (tool returned site metadata only) | not_read | no | yes | https://www.wam.ae/ar/article/3c0fmdz1-الأمن-السيبراني-وسيسكو-وأوبن-إنوفيشن-إيه-يطلقون |
| UAE federal | WAM report: AI Office launches Guide to Leading Generative AI Applications | WAM (news agency) | not read (tool returned site metadata only) | not_read | no | yes | https://www.wam.ae/en/article/c0551ke-office-launches-guide-leading-generative |
| UAE federal | TDRA home | Telecommunications and Digital Government Regulato | not read | not_read | no | yes | https://tdra.gov.ae |
| UAE federal | MOIAT home | Ministry of Industry and Advanced Technology | not read | not_read | no | yes | https://www.moiat.gov.ae |
| UAE federal | PDPL legislation detail page (related items) | UAE Legislation portal | not read | not_read | no | yes | https://uaelegislation.gov.ae/en/legislations/1972 |
| Abu Dhabi | Supplementary Guidance - Digital Investment Management (Guidelines on Digital Investment M | FSRA, ADGM | English official | english_original | no | no | https://assets.adgm.com/download/assets/Supplementary+Guidance+-+Digital+Investment+Management+VER02.061125.pdf/f2ae6f36606c11ef946bcecc50de2f68 |
| Abu Dhabi | Guidance on the DPR 2021 Part 4: DPIAs | Office of Data Protection, ADGM | English official | english_original | no | no | https://assets.adgm.com/download/assets/ADGM+DPR+2021+Guidance+Part+4.pdf/63de087e595611ef8e065eb4feb71eb0 |
| Abu Dhabi | Guidance on the DPR 2021 Part 2: Data Subjects' Rights | Office of Data Protection, ADGM | English official | english_original | no | no | https://assets.adgm.com/download/assets/ADGM+DPR+2021+Guidance+Part+2.pdf/4dfcd0f4595511ef8933e27828504259 |
| Abu Dhabi | Data subject rights: Automated individual decision-making, including profiling (brochure) | ADGM (issuer not named in extracted text; referenc | English official | english_original | no | no | https://assets.adgm.com/download/assets/ADGM+Data+Subject+Rights+Automated+individual+decision-making+Brochure.pdf/698e462858a511ef9face27828504259 |
| Abu Dhabi | ADGM Data Protection Regulations 2021 Update (slide deck) | ADGM ODP | English official | english_original | no | no | https://assets.adgm.com/download/assets/ADGM+Data+Protection+Regulations+2021+Updated.pdf/146aa34858b011efb99a36e29b0f3a63 |
| Abu Dhabi | ADGM Office of Data Protection Guidance (index) | ADGM | English official | english_original | no | no | https://www.adgm.com/operating-in-adgm/office-of-data-protection/guidance |
| Abu Dhabi | ADGM data protection page | ADGM | none | not_read | no | yes | https://www.adgm.com/data-protection |
| Abu Dhabi | A Brief on Data and AI | ADGM Academy (republished from Asia School of Busi | English official | english_original | no | no | https://academy.adgm.com/publications/a-brief-on-data-and-ai |
| Abu Dhabi | Official Gazette Issue 1 (53rd year) incl. Law No. 3 of 2024 establishing the AI and Advan | Government of Abu Dhabi (Official Gazette) | Arabic original (tool extracted Arabic passages, with letter-form arte | arabic_original | yes | no | https://www.abudhabi.gov.ae/-/media/sites/adgov/gazettes/2024/ar/1st-arabic-2024.ashx |
| Abu Dhabi | Law establishing AI and Advanced Technology Council (press page) | Abu Dhabi Media Office | Arabic original (tool answered in Arabic, paraphrasing) | arabic_original | yes | no | https://www.mediaoffice.abudhabi/ar/government-affairs/in-his-capacity-as-ruler-of-abu-dhabi-uae-president-issues-law-establishing-artificial-intelligence-and-advanced-technology-council/ |
| Abu Dhabi | Law No. (14) of 2023 on establishing the Department of Government Enablement | Abu Dhabi Government (DGE site copy) | Arabic original; article content returned as English summary | arabic_original | yes | no | https://www.dge.gov.ae/-/media/sites/dge/legislations-and-polices-and-guides/law-14.ashx |
| Abu Dhabi | Abu Dhabi Government Digital Strategy 2025-2027 accelerates AI-native government journey | DGE | English official | english_original | no | no | https://www.dge.gov.ae/en/news/adg-digital-strategy-update-2025 |
| Abu Dhabi | Arabic version of the Digital Strategy 2025-2027 release | Abu Dhabi Media Office reporting DGE | Arabic original (3 Arabic passages obtained; rest via tool summary) | arabic_original | yes | no | https://www.mediaoffice.abudhabi/ar/technology/abu-dhabi-government-digital-strategy-2025-2027-accelerates-ai-native-government-journey/ |
| Abu Dhabi | Digital Strategy 2025-2027 (English) | Abu Dhabi Media Office reporting DGE | English official | english_original | no | no | https://www.mediaoffice.abudhabi/en/technology/abu-dhabi-government-digital-strategy-2025-2027-accelerates-ai-native-government-journey/ |
| Abu Dhabi | Abu Dhabi to be the world's first fully AI-native government across all digital services b | DGE | English official | english_original | no | no | https://www.dge.gov.ae/en/news/adg-digital-strategy |
| Abu Dhabi | Who we are | DGE | English official | english_original | no | no | https://www.dge.gov.ae/en/about-dge/who-we-are |
| Abu Dhabi | Laws, resolutions, circulars | DGE | English official | english_original | no | no | https://www.dge.gov.ae/en/laws-resolutions-circulars |
| Abu Dhabi | WAM Arabic article on Digital Strategy | WAM | none | not_read | no | yes | https://www.wam.ae/ar/article/bhsv456-... |
| Abu Dhabi | ADJD AI initiatives (WAM) | WAM | none | not_read | no | yes | https://www.wam.ae/en/article/c0memm3-abu-dhabi-judicial-department-reviews-initiatives |
| Abu Dhabi | ITC launches AViTOMS (Autonomous Vehicles Integrated Testing, Operations and Management Sy | Integrated Transport Centre, Abu Dhabi (DMT affili | English official | english_original | no | no | https://admobility.gov.ae/en/news/avitoms |
| Abu Dhabi | DMT regulatory framework for autonomous maritime innovation (press release) | Abu Dhabi Media Office reporting DMT/SASC | English official | english_original | no | no | https://www.mediaoffice.abudhabi/en/transport/under-supervision-of-smart-and-autonomous-systems-council-department-of-municipalities-and-transport-issues-regulatory-framework-to-advance-autonomous-maritime-innovation-in-abu-dhabi/ |
| Abu Dhabi | Smart Customs Classification System (GITEX) | General Administration of Customs, Abu Dhabi | English official | english_original | no | no | https://www.adcustoms.gov.ae/en/Media-Centre/News/Abu-Dhabi-Launches-Smart-Customs-Classification-System-Powered-by-Artificial-Intelligence-at-GITEX |
| Abu Dhabi | Building the road to trustworthy GenAI and LLMs | TII | English official | english_original | no | no | https://www.tii.ae/insights/building-road-trustworthy-genai-and-llms |
| Abu Dhabi | Policy on Use of Artificial Intelligence (AI) in the Healthcare Sector of the Emirate of A | DoH Abu Dhabi | English official | english_original | no | no | https://www.doh.gov.ae/-/media/E9C1470A575146B18015DEBE57E47F8D.ashx |
| Abu Dhabi | Responsible Artificial Intelligence (AI) Standard | DoH Abu Dhabi (owner DDGO) | English official | english_original | no | no | https://www.doh.gov.ae/-/media/B84FF5DD027846699C51F36C439A580F.ashx |
| Abu Dhabi | Responsible AI Risk Management Protocol | DoH Abu Dhabi (owner DDGO) | English official | english_original | no | no | https://www.doh.gov.ae/-/media/8BD7C5DEC5974781B4C11BA00964B6F7.ashx |
| Abu Dhabi | Radiology and Medical Imaging Standard | DoH Abu Dhabi | English official | english_original | no | no | https://doh.gov.ae/-/media/1D754BE9B16E4008BAE7BECF01EE6F11.ashx |
| Dubai | AI System Ethics Self-Assessment Tool | Digital Dubai Office / Dubai Digital Authority | English official | english_original | no | no | https://www.digitaldubai.ae/self-assessment |
| Dubai | AI System Ethics Self-Assessment Tool (Arabic) | Dubai Digital Authority | not read | not_read | no | yes | https://www.digitaldubai.ae/ar/self-assessment |
| Dubai | AI Self-Assessment Tool Has Been Used on 18 AI Use Cases | Smart Dubai (hosted by Dubai Digital Authority) | English official | english_original | no | no | https://www.digitaldubai.ae/newsroom/news/ai-self-assessment-tool-has-been-used-on-18-ai-use-cases |
| Dubai | Artificial Intelligence Principles & Ethics (legacy initiative page) | Smart Dubai | not read | not_read | no | no | https://smartdubai.ae/initiatives/ai-principles-ethics |
| Dubai | Artificial Intelligence Principles & Ethics | Dubai Digital Authority | not read | not_read | no | no | https://www.digitaldubai.ae/initiatives/ai-principles-ethics |
| Dubai | Artificial Intelligence Ethics Guidelines (initiative page) | Dubai Digital Authority | not read | not_read | no | no | https://www.digitaldubai.ae/initiatives/ai-ethics |
| Dubai | Principles of Artificial Intelligence (initiative page) | Dubai Digital Authority | not read | not_read | no | no | https://www.digitaldubai.ae/initiatives/ai-principles |
| Dubai | Ai Ethics (consultation page) | Smart Dubai / Digital Dubai | English official | english_original | no | no | https://www.digitaldubai.ae/ai-ethics |
| Dubai | Ai Ethics Principles & Guidelines (publication page) | Dubai Digital Authority | English official (landing page) | english_original | no | no | https://www.digitaldubai.ae/knowledge-hub/publications/ai-ethics-principles-guidelines |
| Dubai | Dubai AI Ethics Guidelines, Arabic edition (إرشادات أخلاقيات الذكاء الاصطناعي) | Smart Dubai Office | Arabic original | arabic_original | no | no | https://www.digitaldubai.ae/docs/default-source/publications/ai-ethics.pdf?sfvrsn=2c29f04c_2 |
| Dubai | Smart Dubai AI Ethics Principles & Guidelines (English) | Smart Dubai Office with Falcon and Associates | English official | english_original | no | no | https://www.digitaldubai.ae/docs/default-source/ai-principles-resources/ai-ethics.pdf |
| Dubai | AI Ethics Principles & Guidelines (digital-regulations copy) | Smart Dubai Office | English official | english_original | no | no | https://www.digitaldubai.ae/docs/default-source/digital-regulations/data/standards/ai-ethics-principles-guidelines.pdf?sfvrsn=6da24c61_2 |
| Dubai | Ethical AI Toolkit: Request For Information | Smart Dubai (hosted by Dubai Digital Authority) | English official | english_original | no | no | https://www.digitaldubai.ae/knowledge-hub/ethical-ai-toolkit-request-for-information |
| Dubai | Standards And Policies | Dubai Digital Authority | English official | english_original | no | no | https://www.digitaldubai.ae/standards-and-policies |
| Dubai | Publications (Knowledge Hub) | Dubai Digital Authority | English official | english_original | no | no | https://www.digitaldubai.ae/knowledge-hub/publications |
| Dubai | AI Integration Matrix Framework for Government Organizations (publication page) | Dubai Digital Authority | English official | english_original | no | no | https://www.digitaldubai.ae/knowledge-hub/publications/ai-integration-matrix-framework-for-government-organizations |
| Dubai | AI Integration Matrix Framework for Government Organizations: A Strategic Whitepaper and F | Dubai Digital Authority | English official | english_original | no | no | https://www.digitaldubai.ae/docs/default-source/publications/the-ai-integration-matrix-framework-1.pdf?sfvrsn=820a85b0_2 |
| Dubai | Dubai's State of AI Report | Digital Dubai and Dubai Future Foundation | English official | english_original | no | no | https://www.digitaldubai.ae/docs/default-source/publications/dubai-state-of-ai-report.pdf?sfvrsn=a486e23f_5 |
| Dubai | Dubai Strengthens Its Digital Leadership with the Launch of the Updated Dubai Data Manual | Dubai Data and Statistics Establishment (Digital D | English official | english_original | no | no | https://www.digitaldubai.ae/newsroom/news/dubai-strengthens-its-digital-leadership-with-the-launch-of-the-updated-dubai-data-manual |
| Dubai | Information Security Regulation (ISR) v2.0 | Dubai Electronic Security Center (DESC) | English official | english_original | no | no | https://www.digitaldubai.ae/docs/default-source/digital-regulations/cyber/law/information-security-regulation-(isr).pdf?sfvrsn=aa398252_2 |
| Dubai | Dubai Universal Blueprint for Artificial Intelligence (summary page) | UAE Government Portal (u.ae), powered by TDRA | English official | english_original | no | no | https://u.ae/en/about-the-uae/strategies-initiatives-and-awards/strategies-plans-and-visions/government-services-and-digital-transformation/dubai-universal-blueprint-for-ai |
| Dubai | Dubai Universal Blueprint for Artificial Intelligence (summary page, alt path) | UAE Government Portal (u.ae), powered by TDRA | English official | english_original | no | no | https://u.ae/en/about-the-uae/strategies-initiatives-and-awards/strategies-plans-and-visions/Ai/dubai-universal-blueprint-for-ai |
| Dubai | Hamdan bin Mohammed launches Dubai Universal Blueprint for Artificial Intelligence | Protocol Department, Dubai | English official | english_original | no | no | https://www.protocol.dubai.ae/en/media-listing/news-events/hamdan-bin-mohammed-launches-dubai-universal-blueprint-for-artificial-intelligence/ |
| Dubai | Digital Dubai launches AI Integration Matrix Framework to accelerate AI adoption across go | Government of Dubai Media Office / Digital Dubai | English official | english_original | no | no | https://mediaoffice.ae/en/news/2026/april/28-04/digital-dubai-launches-ai-integration-matrix-framework-to-accelerate-ai-adoption-across-government |
| Dubai | دبي الرقمية تطلق وثيقة إطار تكامل الذكاء الاصطناعي في الجهات الحكومية | Government of Dubai Media Office / Digital Dubai | Arabic original (title only quoted; body summarised in English by tool | arabic_original | yes | no | https://mediaoffice.ae/ar/news/2026/april/28-04/digital-dubai-launches-ai-integration-matrix-framework-to-accelerate-ai-adoption-across-government |
| Dubai | Hamdan bin Mohammed reviews first edition of Dubai State of AI Report and witnesses launch | Protocol Department, Dubai | English official | english_original | no | no | https://www.protocol.dubai.ae/en/media-listing/news-events/hamdan-bin-mohammed-reviews-first-edition-of-dubai-state-of-ai-report-and-witnesses-launch-of-ai-policy-at-dubai-ai-week/ |
| Dubai | Hamdan bin Mohammed reviews first edition of Dubai State of AI Report | Government of Dubai Media Office | English official | english_original | no | no | https://mediaoffice.ae/en/news/2025/april/22-04/hamdan-bin-mohammed-reviews-first-edition-of-dubai-state-of-ai-report |
| Dubai | Hamdan bin Mohammed approves new AI initiatives to fast-track Dubai's digital transformati | Government of Dubai Media Office | English official | english_original | no | no | https://mediaoffice.ae/en/news/2025/october/19-10/hamdan-bin-mohammed |
| Dubai | Dubai Finance Calls on Government Entities to Contract AI-Certified Suppliers | Government of Dubai Media Office (reporting Dubai  | English official | english_original | no | no | https://www.mediaoffice.ae/en/news/2025/october/19-10/dubai-finance-calls-on-government-entities-to-contract-ai-certified-suppliers |
| Dubai | «مالية دبي» تدعو الجهات الحكومية للتعاقد مع الموردين الحاصلين على شهادة اعتماد الذكاء الاص | Government of Dubai Media Office (reporting Dubai  | Arabic original (key words دعت and اشتراط quoted by tool) | arabic_original | yes | no | https://www.mediaoffice.ae/ar/news/2025/october/19-10/dubai-finance-calls-on-government-entities-to-contract-ai-certified-suppliers |
| Dubai | 'Dubai AI Seal' Sets Industry Standard for Trusted AI, with Strong Global Response | Government of Dubai Media Office (Dubai Centre for | English official | english_original | no | no | https://www.mediaoffice.ae/en/news/2025/may/15-05/dubai-ai-seal-sets-industry-standard-for-trusted-ai |
| Dubai | Dubai AI Seal | Dubai Centre for Artificial Intelligence (Dubai Fu | English official | english_original | no | no | https://dub.ai/en/ai-seal/ |
| Dubai | شهادة اعتماد الذكاء الاصطناعي (Dubai AI Seal, Arabic) | Dubai Centre for AI (Dubai Future Foundation) | Arabic original (some phrases quoted by tool) | arabic_original | yes | no | https://dub.ai/ar/ai-seal-arabic/ |
| Dubai | WAM: Dubai Centre for AI launches AI Seal | WAM | not read | not_read | no | yes | https://www.wam.ae/article/bhs9w8p-dubai-centre-for-artificial-intelligence-launches |
| Dubai | WAM: Dubai AI security policy launched | WAM | not read | not_read | no | yes | https://www.wam.ae/article/b55eq2m-dubai-security-policy-launched |
| Dubai | WAM Arabic: Dubai annual plan to accelerate AI adoption | WAM | not read | not_read | no | yes | https://www.wam.ae/ar/article/32t0bns7-حمدان-بن-محمد-يطلق-خطة-دبي-السنوية-لتسريع-تبني |
| Dubai | Dubai Electronic Security Center launches the Dubai AI Security Policy | DESC | English official | english_original | no | no | https://www.desc.gov.ae/dubai-electronic-security-center-launches-the-dubai-ai-security-policy/ |
| Dubai | Standards & Policies | DESC | English official | english_original | no | no | https://www.desc.gov.ae/regulations/standards-policies/ |
| Dubai | ISR portal (DESC) | DESC | not read | not_read | no | yes | https://isr.desc.gov.ae |
| Dubai | Dubai Cyber Security Strategy 2023 | Digital Dubai / DESC | English official | english_original | no | no | https://www.desc.gov.ae/wp-content/uploads/2023/pdfs/dcss_EN_2023.pdf |
| Dubai | Artificial Intelligence in the Healthcare (Policy), HISHD/PP-09 | Dubai Health Authority | English official | english_original | no | no | https://www.dha.gov.ae/uploads/082022/Artificial%20Intelligence%20Policy20228457.pdf |
| Dubai | External Circular: Policy for Use of AI in the Healthcare in the Emirate of Dubai (CIR-202 | Dubai Health Authority | English official | english_original | no | no | https://services.dha.gov.ae/sheryan/wps/portal/home/circular-details?circularRefNo=CIR-2021-00000141&isPublicCircular=1&fromHome=true |
| Dubai | Law No. (24) of 2023 Establishing the Dubai Data and Statistics Establishment | Ruler of Dubai | English official translation | english_original | no | no | https://dlp.dubai.gov.ae/Legislation%20Reference/2023/Law%20No.%20(24)%20of%202023%20for%20Dubai%20Data.html |
| Dubai | Law No. (26) of 2015 Regulating Data Dissemination and Exchange in the Emirate of Dubai | Ruler of Dubai | English official translation | english_original | no | no | https://dlp.dubai.gov.ae/Legislation%20Reference/2015/Law%20No.%20(26)%20of%202015.html |
| Dubai | Law No. (9) of 2023 Regulating the Operation of Autonomous Vehicles in the Emirate of Duba | Ruler of Dubai | English official translation | english_original | no | no | https://dlp.dubai.gov.ae/Legislation%20Reference/2023/Law%20No.%20(9)%20of%202023%20Regulating%20the%20Operation%20of%20Autonomous%20Vehicles.html |
| Dubai | Executive Council Resolution No. (34) of 2021 Forming the Committee Supervising the Dubai  | Chairman of the Executive Council | English official translation | english_original | no | no | https://dlp.dubai.gov.ae/Legislation%20Reference/2021/Executive%20Council%20Resolution%20No.%20(34)%20of%202021%20Forming%20the%20Committee%20Supervising.html |
| Dubai | RTA Update 5-year Artificial Intelligence Strategy | Roads and Transport Authority, Dubai | English official | english_original | no | no | https://www.rta.ae/wps/portal/rta/ae/home/news-and-media/all-news/NewsDetails/rta-update-5-year-artificial-intelligence-strategy |
| Dubai | DEWA Adopts Smart Dubai's Ethical AI Toolkit on AI Projects | Dubai Electricity and Water Authority | English official | english_original | no | no | https://www.dewa.gov.ae/en/about-us/media-publications/latest-news/2020/11/dewa-adopts-smart-dubais-ethical-ai-toolkit |
| Dubai | Artificial Intelligence Management System Policy | Dubai Culture and Arts Authority | English official | english_original | no | no | https://dubaiculture.ae/-/media/DC/About-Us/_ISO-42001-AI-policy.pdf |
| Dubai | سياسة الذكاء الاصطناعي (AI Policy), Dubai Department of Finance | Dubai Department of Finance | Arabic original (key bullets' Arabic wording obtained via tool) | arabic_original | yes | no | https://www.dof.gov.ae/ar-sa/profile/Pages/AI-Policy.aspx |
| Dubai | Mohammed bin Rashid approves establishing 'AI' and Data Authority | Government of Dubai Media Office | English official | english_original | no | no | https://mediaoffice.ae/en/news/2026/june/14-06/mohammed-bin-rashid-approves-establishing-artificial-intelligence-and-data-authority |
| Dubai | Dubai Police Awarded ISO Certification for Artificial Intelligence Management System | Government of Dubai Media Office | English official | english_original | no | no | https://www.mediaoffice.ae/en/news/2025/may/15-05/dubai-police-awarded-iso-certification-for-artificial-intelligence-management-system |
| Dubai | Dubai Centre for AI to establish dedicated taskforces within 30 government entities | Dubai Future Foundation | English official | english_original | no | no | https://www.dubaifuture.ae/latest-news/dubai-centre-for-ai-to-establish-dedicated-taskforces-within-30-government-entities/ |
| Dubai | Dubai Customs harnesses AI to strengthen customs readiness and support the future of trade | Dubai Customs | English official | english_original | no | no | https://www.dubaicustoms.gov.ae/en/mobile/Pages/newsdetails.aspx?itemid=2183 |
| Dubai | Regulation 10 (DIFC Commissioner of Data Protection) | DIFC | not opened | not_read | no | no | https://www.difc.com/business/registrars-and-commissioners/commissioner-of-data-protection/regulation-10 |
| Dubai | Public Regulation 10 on Personal Data Processed Through Autonomous and Semi-autonomous Sys | DIFC | not opened | not_read | no | no | https://assets.difc.com/v1/media/edge/images/dubaiintern0078-difcexperie96c5-production-3253/media/project/difcexperiences/difc/difcwebsite/documents/registrars-and-commissioners/guidance-and-handbooks/lawful-processing/dp_regulation_10.pdf |
| Dubai | DIFC Regulation 10 Accreditation and Certification Framework | DIFC | not opened | not_read | no | no | https://assets.difc.com/v1/media/edge/images/dubaiintern0078-difcexperie96c5-production-3253/media/project/difcexperiences/difc/difcwebsite/documents/registrars-and-commissioners/regulation-10/difc-reg-10-accreditation-and-certification-framework.pdf |
| Dubai | FAQs: Regulation 10 | DIFC | not opened | not_read | no | no | https://assets.difc.com/v1/media/edge/images/dubaiintern0078-difcexperie96c5-production-3253/media/project/difcexperiences/difc/difcwebsite/documents/data-protection-pages/guidance-and-handbooks/lawful-processing/dp-regulation-10-faqs.pdf |
| Dubai | DIFC Regulation 10 Advisory Committee Charter | DIFC | not opened | not_read | no | no | https://assets.difc.com/v1/media/edge/images/dubaiintern0078-difcexperie96c5-production-3253/media/project/difcexperiences/difc/difcwebsite/documents/registrars-and-commissioners/regulation-10/difc-regulation-10-committee-charter.pdf |
| Dubai | DIFC Data Protection Regulations, Consolidated Version No. 2 | DIFC | not opened | not_read | no | no | https://assets.difc.com/v1/media/edge/images/dubaiintern0078-difcexperie96c5-production-3253/media/project/difcexperiences/difc/difcwebsite/documents/laws--regulations/data-protection-regulation.pdf |
| Dubai | The National Cyber Security Policy for Artificial Intelligence | UAE Government Portal (federal) | not opened | not_read | no | no | https://u.ae/ar/about-the-uae/strategies-initiatives-and-awards/policies/cyber-activities/The-National-Cyber-Security-Policy-for-Artificial-Intelligence |

## Searches that ended in not found or blocked

| Zone | Query or target | Language | Tool | Outcome |
|---|---|---|---|---|
| UAE federal | (fetch) Agentic AI practical guide uaemodel.egsep.ae | en | WebFetch | blocked |
| UAE federal | (fetch) UAE Cabinet Agentic AI framework news (Arabic) | ar | WebFetch | blocked |
| UAE federal | اللائحة التنفيذية قانون حماية البيانات الشخصية المرسوم بقانون اتحادي رقم 45 لسنة 2021 | ar | WebSearch | not_found |
| UAE federal | UAE Data Office PDPL executive regulations issued 2026 data protection impact assessment automated processing | en | WebSearch | not_found |
| UAE federal | uaelegislation.gov.ae executive regulation personal data protection law Cabinet resolution issued | en | WebSearch | not_found |
| UAE federal | (fetch) uaelegislation.gov.ae/en/legislations/1972 (related legislation list) | en | WebFetch | blocked |
| UAE federal | قرار مجلس الوزراء الذكاء الاصطناعي اختبار تقييم الأنظمة الحكومية الإمارات 2026 | ar | WebSearch | not_found |
| UAE federal | (fetch) WAM Arabic article on Federal Authority for AI and Data (raw and percent-encoded URL) | ar | WebFetch | blocked |
| UAE federal | TDRA artificial intelligence guideline OR policy OR framework tdra.gov.ae testing evaluation | en | WebSearch | not_found |
| UAE federal | tdra.gov.ae "artificial intelligence" policy OR guidelines OR framework Telecommunications and Digital Governm | en | WebSearch | not_found |
| UAE federal | الهيئة العامة لتنظيم قطاع الاتصالات والحكومة الرقمية دليل الذكاء الاصطناعي سياسة حكومية tdra.gov.ae | ar | WebSearch | not_found |
| UAE federal | TDRA UAE government AI standards OR guideline digital government policy testing quality assurance | en | WebSearch | not_found |
| UAE federal | (fetch) tdra.gov.ae home (two attempts) | en | WebFetch | blocked |
| UAE federal | (fetch) CSC full policy PDF v1.1 (two attempts) | en | WebFetch | blocked |
| UAE federal | (fetch) WAM English /a/c01kgfl and WAM Arabic 3c0fmdz1 (National AI Test and Validation Lab) | en/ar | WebFetch | blocked |
| UAE federal | (fetch) tradearabia + middleeastainews on the Lab | en | WebFetch | blocked |
| UAE federal | (fetch) csc.gov.ae home (two attempts) | en | WebFetch | blocked |
| UAE federal | ai.gov.ae wp-content uploads 2026 Leading Generative AI Applications pdf | en | WebSearch | not_found |
| UAE federal | دليل تطبيقات الذكاء الاصطناعي التوليدي الرائدة مكتب الذكاء الاصطناعي | ar | WebSearch | not_found |
| UAE federal | (fetch) WAM English article c0551ke on Leading GenAI guide | en | WebFetch | blocked |
| UAE federal | (fetch) ai.gov.ae/generative-ai-guide/ (guessed URL) | en | WebFetch | not_found |
| UAE federal | MOIAT OR ESMA UAE standard artificial intelligence conformity assessment UAE.S ISO/IEC 42001 adoption | en | WebSearch | not_found |
| UAE federal | وزارة الصناعة والتكنولوجيا المتقدمة مواصفة قياسية الذكاء الاصطناعي تقييم المطابقة | ar | WebSearch | not_found |
| UAE federal | UAE.S standard artificial intelligence MOIAT Emirates standardization technical committee AI national standard | en | WebSearch | not_found |
| UAE federal | (fetch) moiat.gov.ae home | en | WebFetch | blocked |
| UAE federal | UAE federal government AI procurement guideline OR AI procurement Ministry of Finance | en | WebSearch | not_found |
| UAE federal | مبادئ وإرشادات أخلاقيات الذكاء الاصطناعي الإمارات مجلس الإمارات للذكاء الاصطناعي والبلوكتشين | ar | WebSearch | not_found |
| UAE federal | الهيئة الاتحادية للموارد البشرية الحكومية سياسة استخدام الذكاء الاصطناعي في الجهات الاتحادية | ar | WebSearch | not_found |
| Abu Dhabi | Abu Dhabi Department of Government Enablement AI policy testing evaluation assurance | en | WebSearch | not_found |
| Abu Dhabi | ADGM Office of Data Protection guidance artificial intelligence | en | WebSearch | not_found |
| Abu Dhabi | دائرة التمكين الحكومي أبوظبي سياسة الذكاء الاصطناعي اختبار تقييم | ar | WebSearch | not_found |
| Abu Dhabi | ADGM data protection page fetch (adgm.com/data-protection) | en | WebFetch | blocked |
| Abu Dhabi | WAM Arabic Digital Strategy article | ar | WebFetch | blocked |
| Abu Dhabi | TII Falcon safety evaluation red teaming | en | WebSearch | not_found |
| Abu Dhabi | Abu Dhabi Government Data Management Policy / Information Security Standards / AI ethics | en | WebSearch | not_found |
| Abu Dhabi | سياسة إدارة البيانات حكومة أبوظبي الذكاء الاصطناعي دليل أخلاقيات | ar | WebSearch | not_found |
| Abu Dhabi | WAM ADJD AI initiatives | en | WebFetch | blocked |
| Abu Dhabi | TII AI safety framework responsible AI policy | en | WebSearch | not_found |
| Abu Dhabi | معهد الابتكار التكنولوجي سلامة الذكاء الاصطناعي تقييم نماذج فالكون | ar | WebSearch | not_found |
| Abu Dhabi | سوق أبوظبي العالمي مكتب حماية البيانات إرشادات الذكاء الاصطناعي | ar | WebSearch | not_found |
| Abu Dhabi | ADJD AI judicial platform governance | en | WebSearch | not_found |
| Abu Dhabi | TAMM AI assurance testing evaluation | en | WebSearch | not_found |
| Abu Dhabi | المكتب التنفيذي أبوظبي الذكاء الاصطناعي سياسة اختبار تقييم أنظمة | ar | WebSearch | not_found |
| Abu Dhabi | Abu Dhabi Government AI Policy / Responsible AI guidelines (DGE, abudhabi.ae) | en | WebSearch | not_found |
| Abu Dhabi | ADJD AI judicial platform phase one oversight | en | WebSearch | not_found |
| Dubai | دبي الذكاء الاصطناعي مبادئ وإرشادات أخلاقيات الذكاء الاصطناعي التقييم الذاتي | ar | WebSearch | not_found |
| Dubai | سياسة أمن الذكاء الاصطناعي دبي مركز دبي للأمن الإلكتروني | ar | WebSearch | not_found |
| Dubai | Dubai AI Security Policy DESC requirements testing red teaming AI systems government entities | en | WebSearch | not_found |
| Dubai | Dubai Municipality artificial intelligence policy governance document | en | WebSearch | not_found |
| Dubai | Dubai Executive Council resolution artificial intelligence government entities 2025 2026 AI governance mandato | en | WebSearch | not_found |
| Dubai | Dubai legislation law regulating artificial intelligence Emirate of Dubai decree 2025 2026 AI law | en | WebSearch | not_found |
| Dubai | Dubai AI Act OR AI law Dubai Ruler issues law artificial intelligence | en | WebSearch | not_found |
| Dubai | DHA Artificial Intelligence in the Healthcare policy HISHD/PP-09 updated version 2025 2026 | en | WebSearch | not_found |
| Dubai | Dubai Universal Blueprint for AI document pdf dub.ai blueprint full text | en | WebSearch | not_found |
| Dubai | FETCH https://www.digitaldubai.ae/ar/self-assessment (Arabic) | ar | WebFetch | blocked |
| Dubai | FETCH https://smartdubai.ae/initiatives/ai-principles-ethics | en | WebFetch | not_found |
| Dubai | FETCH https://www.digitaldubai.ae/initiatives/ai-principles-ethics | en | WebFetch | not_found |
| Dubai | FETCH https://www.digitaldubai.ae/initiatives/ai-ethics | en | WebFetch | not_found |
| Dubai | FETCH https://www.digitaldubai.ae/initiatives/ai-principles | en | WebFetch | not_found |
| Dubai | FETCH https://www.wam.ae/article/bhs9w8p-dubai-centre-for-artificial-intelligence-launches | en | WebFetch | blocked |
| Dubai | FETCH https://www.wam.ae/en/article/bhs9w8p-dubai-centre-for-artificial-intelligence-launches | en | WebFetch | blocked |
| Dubai | FETCH https://www.wam.ae/article/b55eq2m-dubai-security-policy-launched | en | WebFetch | blocked |
| Dubai | FETCH https://www.wam.ae/ar/article/32t0bns7-حمدان-بن-محمد-يطلق-خطة-دبي-السنوية-لتسريع-تبني | ar | WebFetch | blocked |
| Dubai | FETCH https://isr.desc.gov.ae | en | WebFetch | blocked |

## Leads found only in secondary sources (not evidence)

Reports of a National AI Test and Validation Lab (Cyber Security Council), a Federal Authority for AI and Data (June 2026), a guide on leading generative AI applications (May 2026) and a National Committee for Agentic AI guide were found in news or law firm material only. No primary text was retrieved. They are listed so they can be searched for by hand; they are not used anywhere in the counts.
