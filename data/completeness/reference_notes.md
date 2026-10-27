# Reference list notes (independent completeness check)

Date of work: 28 October 2026. The list holds 82 rows, not the 120 to 200 targeted. It is incomplete and should be read as a partial reference list.

## Why the target was missed
1. The WebSearch budget (200 per turn, shared by all agents) was exhausted after 16 searches of mine. 6 further searches (EU harmonised standards, GPAI code, MDR, EASA, EBA/EIOPA/ESMA, CRA/PLD) returned "budget used up" and were not run. No other search route was used.
2. WebFetch only accepted URLs that had appeared in search results or in pages already read. Most other official URLs I tried were rejected by the tool allowlist (not by the sites). Those rows are marked access_status blocked with a note saying so. They are tool restrictions, not site blocks, except SDAIA.
3. sdaia.gov.sa returned "Request Rejected" on every document. Each was tried twice (Adoption Framework, GenAI for Government, GenAI for Public, Deepfakes, AI Market Regulation Tools, AI Bias Guide, regulations index) and then dropped. The AI Ethics Principles were readable on the issuer's dgp.sdaia.gov.sa host.

## Searches run (16)
1. EU AI Act Regulation 2024/1689 conformity assessment Article 43 high-risk
2. NIST AI RMF 1.0 TEVV
3. OECD.AI policy observatory AI policy instruments testing evaluation database
4. IAPP global AI law and policy tracker jurisdictions
5. UAE AI Charter / AI ethics guidelines Dubai self-assessment Smart Dubai
6. SDAIA AI Ethics Principles Saudi Arabia AI adoption framework generative AI guidelines
7. IMDA Singapore Model AI Governance Framework agentic AI AI Verify
8. Japan AI Promotion Act AI Guidelines for Business METI MIC AISI
9. Korea AI Basic Act high-impact AI risk assessment enforcement decree MSIT
10. China generative AI interim measures security assessment TC260
11. SDAIA AI Adoption Framework (allowed_domains sdaia.gov.sa)
12. AI Ethics Principles and Controls generative AI guidelines (sdaia.gov.sa, dgp.sdaia.gov.sa)
13. AI Office UAE AI ethics principles guidelines charter (ai.gov.ae, u.ae, uaelegislation.gov.ae)
14. Model AI Governance Framework Singapore testing AI Verify (imda, pdpc, mas, aiverifyfoundation)
15. NIST AI 600-1 generative AI profile (nist.gov, airc, doi, nvlpubs)
16. OMB M-25-21 pre-deployment testing (whitehouse.gov, federalregister.gov, congress.gov)
Fewer than the 20 required, and no Arabic queries were run.

## Aggregators and indexes actually read
- IAPP Global AI Governance jurisdiction overviews, plus the EU, US, UK, Canada, Singapore, Japan, China, UAE country articles (mostly paywalled or thin; they named few instruments).
- aigl.blog copy of the IAPP Global AI Law and Policy Tracker (third party copy, May 2025 snapshot). Futurium description page of the IAPP tracker (no instrument list).
- regulations.ai: NIST AI RMF page, UAE overview page, Saudi AI Adoption Framework page, Dubai AI Certification Framework, Dubai sandbox, UAE financial guidelines pages.
- OECD.AI: one initiative entry (Dubai AI principles) and the About the Observatory PDF. The OECD dashboards pages were rejected by the tool allowlist.
- u.ae AI resources page and ai.gov.ae publications page (UAE official portals).
- AI Verify Foundation resources page.
- White House OMB memoranda index page.
- Digital Policy Alert entry for Japan AI Guidelines for Business v1.1.
- SESEC (EU-China standards project) Annex II on AI security standards in China; MoFo China AI page (law firm, used only to locate).
- hsfkramer Saudi tracker (law firm, used only to locate).
Not read: Stanford AI Index, International AI Safety Report or AISI network pages, CEN CENELEC JTC 21, ISO catalogue (rejected), canada.ca (rejected), MSIT, CAC and TC260 official sites, uaelegislation.gov.ae beyond two policy pages. Fewer than six of the suggested aggregators were read in full depth.

## Reading standard
- has_testing_provision yes only where I read the provision myself in a fetch result. Locators come from the fetch tool's summary of the page, so paragraph and slide numbers (for example OMB M-25-21 section numbering) may be imprecise and should be checked against the PDFs.
- Rows known only from a secondary page (regulations.ai, law firm, white paper, trade.gov) are marked unclear even where the secondary says there is a testing provision.
- Several rows (UK, Canada, ISO) come from my own recall and were not found through any aggregator. Their discovered_via says so, and they were not readable. Titles and dates for them are unverified.
- artificialintelligenceact.eu is not an official source. It was used only for the Article 9 wording, flagged in the AI Act row.

## Not found or not covered
- CEN CENELEC JTC 21 deliverables (prEN on QMS, risk, conformity, accuracy, robustness, cybersecurity), the Commission GPAI guidelines, and ISO/IEC 42006, 29119-11, TS 4213, 24029, 5338, 25059: not found or not fetchable.
- EU sector instruments (MDR/IVDR and MDCG 2019-11, EASA AI roadmap and concept papers, EBA/EIOPA/ESMA, Machinery Regulation, CRA, Product Liability): not searched.
- US sector instruments (FDA PCCP and AI device guidance, FAA, NHTSA, DoD Directive 3000.09 and RAI toolkit, SR 11-7): not searched.
- UK sector instruments (MHRA, FCA, PRA SS1/23, CAA, MoD JSP 936, ICO AI guidance, AISI publications): only MHRA tried, rejected.
- Canada (AIDA, voluntary code, Directive on ADM, Health Canada MLMD guidance): Directive tried, rejected.
- Japan sector instruments, Korea KCC/FSC guidance, China sector standards beyond those listed, Saudi sector rules (SAMA, NCA, SFDA), UAE sector rules (DHA, DoH Abu Dhabi AI policy, CBUAE, TDRA, RTA autonomous vehicle rules, DIFC Regulation 10, ADGM): not found or not searched.
