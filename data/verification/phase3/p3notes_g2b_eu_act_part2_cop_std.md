# Phase 3 notes: g2b_eu_act_part2_cop_std (retrieved 2026-10-16)

## Sources fetched
| Source | Outcome |
|---|---|
| eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727 | Empty body twice (retried once), so stopped |
| eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng | Empty body |
| publications.europa.eu/resource/celex/02024R1689-20260727, then the cellar item `b1730fb2-8f1c-11f1-9262-01aa75ed71a1.0001.03/DOC_1` (XHTML) | OK. Same publisher's official endpoint (`alt_official_endpoint`). The text is 847,869 characters long and was read with offsets 300000 to 847869. Consolidation date 27.07.2026. The only amending act is M1, Reg. (EU) 2026/1744 of 8 July 2026 (OJ L 24.7.2026). |
| ec.europa.eu/newsroom/dae/redirection/document/118119 (GPAI CoP, Safety and Security chapter PDF) | OK this time; the phase 2 permission timeout did not recur. The fetch tool could not decode the PDF streams, so text was extracted locally (pypdf) from the copy that WebFetch saved. 43 pages. |
| digital-strategy.ec.europa.eu/en/policies/contents-code-gpai | OK (last update 7 Oct 2026) |
| Commission Opinion C(2025) 5361 (document/118688) | OK, extracted locally |
| digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation | OK (last update 3 Aug 2026) |
| cencenelec.eu AI topic page | OK on retry after the phase 2 timeout |
| cencenelec.eu news "EN 18286 in the Spotlight" | OK |
| standards.cencenelec.eu JTC 21 work programme | Session-checksum error, then HTTP 500. Stopped. |
| jtc21.eu and its JSON feed (site run by the JTC 21 secretariat, Dansk Standard) | OK |
| Commission Implementing Decision (EU) 2026/2274 | eur-lex ELI empty. Read on publications.europa.eu cellar `05805dc1-...0006.03/DOC_1` |
| Commission Implementing Regulation (EU) 2026/1755 | publications.europa.eu cellar `b8c9e6d4-...0006.03/DOC_1`, OK |
| Code of Practice on Transparency of AI-generated Content PDF (document/129555) | OK, extracted locally (38 pages) |
| EC pages on: Art 50 guidelines, Art 50 code opinion, Art 6 draft guidelines and consultation, serious incident draft consultation, "Supporting the implementation of the AI Act with clear guidelines", high-risk guidelines | OK |
| Press release IP/26/1714 (31 July 2026) | OK, extracted locally |
| AI Act Service Desk resources page | OK (page 1 of 4 only) |

## Searches run (2026-10-16, WebSearch, restricted to EU or CEN domains)
1. AI Board assessment GPAI Code of Practice adequacy
2. Commission guidelines on Art 6 high-risk classification, adopted
3. "guidelines" "high-risk" classification, Commission adopts final, 2026
4. Commission serious incident guidance, Art 73 template
5. Implementing decision on harmonised standards, AI Act, EN 18286
6. "First ever European standard on AI published in the OJEU"
7. Art 41 common specifications implementing act, 2026
8. GPAI Code of Practice update or review in 2026, Signatory Taskforce

## Searched for and NOT found
- Final (adopted) Art 6 high-risk classification guidelines. Only the 19 May 2026 draft exists, with adoption expected by the end of 2026.
- Final Art 73 serious incident guidance. Only the 26 Sept 2025 draft and template were found. The EC news page lists a template as "already published", but its link is a broken relative path.
- Any Art 41 common specifications implementing act. EUR-Lex search could not be read, so absence is not proven.
- The AI Board's own adequacy assessment document for the GPAI Code. Only the Commission's statement that the Board confirmed it was seen.
- A revised version of the GPAI Code (the current one is 10 July 2025).
- Any consolidated AI Act text later than 27.07.2026. Not checkable.

## Conflicts between sources
- **Art 50 guidelines.** The EC library page (20 July 2026) says they were adopted. Press release IP/26/1714 (31 July 2026) still links "Draft guidelines".
- **Serious incident template.** The EC guidelines news page lists it as published, but only draft documents can be found.
- **EC standardisation page (3 Aug 2026).** It shows no OJ citation, which is superseded by Implementing Decision (EU) 2026/2274 (OJ 14.10.2026). EU-Standards-002 ("no OJEU reference yet") is now out of date. That row is not in this input, so this is reported in the status file and as new row EU-Standards-P3-20.
- **Implementing Reg. 2026/1755 Art 3(6)(c)** cross-refers to "paragraph 4", but the provider-observations right is in paragraph 5.

## Coding notes
- **GPAI CoP rows** are coded `voluntary`. Signing is optional. However, Art 53(4) and Art 55(2) let providers rely on the Code to demonstrate compliance with binding obligations. Commission Opinion C(2025) 5361 found that the Code adequately covers Arts 53 and 55, so it is a recognised compliance route. Objective A says adherence is not conclusive evidence of compliance.
- **Arts 53(4) and 56** are proposed as `mandatory`. In 53(4) the duty to demonstrate compliance is binding. In 56 the duties fall on the AI Office, Commission and Board.

## Documents to download by hand
None required. Optional:
- The EUR-Lex PDF of the authentic OJ texts, to confirm against the Publications Office consolidated XHTML, which states that it has no legal effect:
  - Regulation (EU) 2024/1689 and Regulation (EU) 2026/1744: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
  - Implementing Decision (EU) 2026/2274
- The CEN-CENELEC JTC 21 work programme page (standards.cencenelec.eu, Technical Bodies > CEN/CLC/JTC 21 > Work programme), to confirm the draft stages that were read from the JTC 21 secretariat feed. The page could not be read with the fetch tool.
