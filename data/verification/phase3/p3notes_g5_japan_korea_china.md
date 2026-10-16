# Phase 3 notes: g5_japan_korea_china (retrieved 2026-10-16)

## Method
- Only WebFetch and WebSearch were used. For PDFs, WebFetch returned binary content and saved the file. Text was then extracted locally from that saved file with pypdf. No other retrieval route was used. Recorded as `standard_fetch`.
- Other files read: RULES_P3.md, PROTOCOL.md, the input CSV, and the Japan/Korea/China rows of `data/evidence_table.csv` (read for Task C, to avoid duplicates).

## Searches run (all 2026-10-16)
1. Korean decree title + law.go.kr → found a MOFA PDF copy (fetch failed with a redirect loop) and digitalpolicyalert pages (secondary).
2. elaw.klri.re.kr enforcement decree → no direct hit. A later extended search found KLRI hseq=73696 (decree, English).
3. English decree title → secondary trackers only.
4. MSIT grace period (Korean/English) → secondary results. A domain-limited search (msit.go.kr) found MSIT English releases 1191, 1214, 1215 and 1238.
5. MSIT notice on compute calculation / high-impact guidelines → secondary only (BSA filings, news).
6. TC260 AI Safety Governance Framework 2.0 (Chinese) → CAC release notice and PDF link; TC260 postDetail page.
7. Framework 2.0 English PDF → secondary only.
8. GB 45438-2025 on openstd → secondary results. Then fetched the openstd catalogue list directly.
9. openstd hcno for GB 45438 → not found.
10. CAC orders 2026 on AI (cac.gov.cn, gov.cn) → anthropomorphic measures and the digital virtual human draft.
11. Mandatory AI standard drafts 2026 / TC260 → secondary reports (CGTN, secrss, sesec) and a TC260 practice-guide PDF.
12. Digital Agency generative AI procurement guideline revision 2026 → Digital Agency news page.

## Sources fetched and outcome
- japaneselawtranslation.go.jp 5066 (Japanese and bilingual views): readable. The page does not say whether the English is official or tentative.
- Cabinet Office AI Basic Plan EN PDF (14 Jul 2026): readable after local extraction. The plan index page is readable.
- Cabinet Office Guideline for Ensuring Appropriateness EN PDF: readable.
- soumu 001003032.pdf: readable. It is the **Outline** of AI Guidelines for Business v1.1 (4 Apr 2025), not the full guidelines.
- AISI Evaluation Perspectives v1.10 EN and the Task Force summary (15 Apr 2026): readable.
- KLRI Act hseq=73499 and Decree hseq=73696 (eng_service, eng_mobile, kor_mobile, kor_service): readable. In every view, the decree's compute exponent renders as "10^2?".
- law.go.kr decree page: the header shows Presidential Decree No. 36580 (18 Aug 2026, in force 20 Aug 2026, amendment by another statute). The body is loaded by script, so no article text was readable. lsInfoR.do shows a "service delayed" notice.
- mofa.go.kr decree PDF: "Too many redirects (exceeded 10)" on two attempts. Stopped (a non-MOLEG copy in any case).
- MSIT English releases 1191 (Nov 2025 legislative notice), 1214 (entry into force), 1215 (transparency guidelines) and 1238 (improvement working group): readable.
- opinion.lawmaking.go.kr 86822: readable. It is the decree amendment notice of 21 May to 19 Jun 2026.
- Korea AISI /eng/sub/30: readable.
- CAC pages: generative AI measures, algorithm provisions, labelling measures (CAC and news.cn), anthropomorphic measures, Cybersecurity Law decision, Framework 2.0 notice, the digital virtual human draft, and the expert commentary of 18 Mar 2025. All readable.
- CAC Framework 2.0 PDF: "maxContentLength size of 10485760 exceeded". This is the tool's size limit, not a site block.
- tc260.org.cn home page: readable. postDetail id=20250915124214 shows no attachment because the page is script-rendered. The TC260-PG-20268A PDF is readable.
- openstd.samr.gov.cn list searches (45438, 45654, 人工智能, 生成式人工智能): readable. Detail links are script-only.
- std.samr.gov.cn search: "no data".
- Digital Agency news page and the DS-920 v2.0 EN and JA PDFs: readable.

## Language note per source
- Japan AI Promotion Act: English on the MoJ translation database. Status (official or tentative) is not stated.
- Japan AI Basic Plan, Appropriateness Guideline, and Outline of AI Guidelines for Business: official English *provisional* translations ("refer to the original"). Japanese originals were not checked, except as noted.
- Japan AISI guides: AISI English versions.
- Japan DS-920 v2.0: English provisional translation, checked against the Japanese original for Secs. 3.2, 4.2.2 and 6.3.3. Sec. 6.3.3 reads "should" in English but uses the declarative 実施する in Japanese.
- Korea Act and Decree: KLRI English, which the site marks as reference only with no legal effect. The Korean original on law.go.kr could not be read.
- Korea MSIT: official English press releases. The MOLEG notice is Korean, read through the fetch tool's machine English rendering.
- China CAC texts: Chinese originals, read through the fetch tool's machine English rendering. No official English versions.
- China openstd catalogue: Chinese, read through machine rendering.
- TC260-PG-20268A: Chinese original extracted and read directly. The English paraphrase in the new rows is an unofficial translation.

## Searched for and NOT found
- Final MSIT notice (고시) on the compute calculation method (Decree Art. 24(2)) or on high-impact AI measures. Not found on MSIT English; secondary sources suggest it was still a draft in Aug 2026.
- Final adoption of the Korean decree amendment of May–Jun 2026. The content of Decree No. 36580 was not readable.
- An official English version of TC260 Framework 2.0.
- The standard text of GB 45438-2025 (only the catalogue was read).
- The adopted digital virtual human measures (only the draft exists).
- Primary record of the reported planned mandatory standard on AI agent application security.

## Conflicts
- Korea grace period: the Nov 2025 MSIT notice describes a grace period before fines only. The Jan 2026 release defers both investigations and penalties, with exceptions.
- Korea-014 (secondary) cited Decree Arts. 25, 27 and 28. The content is in Art. 27, with the measures in Act Art. 34(1).
- China-031 cited a "CAC commentary". It is an expert interpretation, not an official CAC statement.
- Japan-009: the English word "systems" refers to institutional rules (including the AI Act), not AI systems.
- Digitalpolicyalert (secondary) claims the final Korean decree is limited to enforcement dates and repeal. This conflicts with the KLRI text, which has 33 articles including Arts. 23–29. The secondary source is wrong.

## Documents the user should download by hand
1. **China AI Safety Governance Framework 2.0 (Chinese PDF)**: https://www.cac.gov.cn/rootimages/uploadimg/1759653474200838/1759653474200838.pdf. Over 10 MB, so beyond the fetch limit. Needed for clause-level verification of China-030.
2. **GB 45438-2025** full text: free online reading on openstd.samr.gov.cn (search "45438"). The viewer is script-rendered. Needed to verify the explicit/implicit method details in China-031.
3. **Korean Enforcement Decree, Korean original (current, Presidential Decree No. 36580)** from law.go.kr. The body is script-rendered. Needed to confirm the Art. 24(1)1 exponent (10^26) and the content of the Aug 2026 change.
