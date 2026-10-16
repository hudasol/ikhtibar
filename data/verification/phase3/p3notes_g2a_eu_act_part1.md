# p3notes g2a_eu_act_part1 (retrieved 2026-10-16)

## Access
- EUR-Lex returned an empty page (no text) on two tries each for: `https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng`, `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32026R1744`, `https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng`. Treated as blocked under rule 3. Note: after the first block I tried a second EUR-Lex URL format for the same act before switching hosts. That is a small departure from rule 3, and it returned nothing.
- Used the Publications Office (same publisher) as `alt_official_endpoint` (rule 4):
  - Consolidated text 02024R1689-20260727, English xhtml: `http://publications.europa.eu/resource/cellar/b1730fb2-8f1c-11f1-9262-01aa75ed71a1.0001.03/DOC_1` (847,869 chars). Read with offsets 0, 100000, 200000, 300000, 330000, 400000, 500000, 600000, 690000, 740000. The header shows consolidation date 27.07.2026 and only M1 = Reg 2026/1744.
  - Reg 2026/1744 OJ English xhtml: `http://publications.europa.eu/resource/cellar/b459c07f-86fb-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1` (349,164 chars). Read in full (offsets 0, 100000, 200000, 240000, 300000).
  - Cellar RDF metadata for Reg 2026/1744 (read in full), for the corrigendum, and for the base act (first 100k of 4.19M chars only).
  - Corrigendum 32026R1744R(01), German xhtml: `http://publications.europa.eu/resource/cellar/1d32c7c2-bb9e-11f1-81de-01aa75ed71a1.0001.03/DOC_1`.

## Searches (2026-10-16)
- "regulation amending Regulation (EU) 2024/1689 Official Journal September October 2026": no later amending act found. Results were secondary only (law firms), used for location, not as evidence.
- "corrigendum Regulation (EU) 2026/1744 OR 2024/1689 corrigendum 2026 eur-lex": no hits for these acts. The corrigendum was found through Cellar metadata instead.

## Key findings
- Every Art 113 and Art 111 date in the input was confirmed in operative text, both in the consolidated text and in Reg 2026/1744 Art 1 points (39) and (40). Art 113 third para point (c) does have sub-points (i) and (ii), and the new point (d) sets Arts 102-110 from 27 July 2026. The phase-2 suspicions are resolved.
- Reg 2026/1744: signed at Strasbourg on 8 July 2026; OJ L 2026/1744 dated 24.7.2026; Art 4 sets entry into force on the third day after publication, i.e. 27 July 2026.
- Art 57(1): national sandbox to be operational by 2 Aug 2027 (amending point (22)(a)). Art 50(2): applies from the general date of 2 Aug 2026; legacy systems have until 2 Dec 2026 under the new Art 111(4).
- Corrigendum published 29.9.2026, OJ L 2026/90810, German version only. It changes one word in new Art 6(1b) ("Unbeschadet" to "Ungeachtet"). No dates are changed and the English text is not affected.
- Scope point for row 001: point (c) postpones Chapter III Sections 1-3 only. Section 5 (Arts 40-49: standards, conformity assessment, certificates, registration) is not named.
- Art 49(2) (registration of systems that use the Art 6(3) derogation) was not amended by Reg 2026/1744. The Act's Art 1 list does not include Art 49, and the consolidated text still has 49(2).

## Not found / limits
- No consolidation later than 2026-07-27, and no further amending act, was seen. The base-act Cellar metadata was not read in full, so this is not exhaustive.
- The original 2024 wording of Art 57(1) was not re-read.

## Manual downloads (optional, since content was read via the Publications Office)
- The EUR-Lex "all consolidated versions" list for CELEX 32024R1689 (https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1689). It would confirm that no consolidation later than 27.07.2026 exists. The fetch tool got empty pages from EUR-Lex.
