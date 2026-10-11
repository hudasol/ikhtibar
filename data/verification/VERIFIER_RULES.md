# Rules for every subagent in this phase (read fully before doing anything)

Context: an AI-governance evidence review (pre-deployment testing requirements). Protocol: /home/claude/docs/PROTOCOL.md (binding_status definitions, translation handling). Retrieval date to record: 2026-10-12. This is research, not legal advice. Everything must be free: never suggest or require purchasing a standard, subscription or paid API.

## ACCESS RULE (strict)
1. For web content use ONLY the WebFetch and WebSearch tools. Do NOT use curl, wget, python requests, a headless browser or any other route to fetch web pages.
2. If a site blocks a fetch (HTTP 403/429/406, "Request Rejected", bot challenge, empty 202, robots.txt disallow, permission prompt timeout), you may retry the same URL ONCE. If it is still blocked, STOP for that source: do not change the user agent, do not use caches, web archives, mirrors, translation proxies or third-party copies, and do not use search-result snippets as evidence. Record the exact URL blocked, the exact error text, and the exact document the user should download by hand.
3. Official pages of the same publisher at a DIFFERENT, documented machine-access endpoint (for example the EU Publications Office dissemination service at publications.europa.eu) may be used only if you label the access path "alt_official_endpoint" and say which primary host blocked. Anything else is a workaround and is not allowed.
4. Secondary sources (law firms, news, blogs, newsletters) may help you LOCATE a primary source but are never evidence for a clause.
5. The fetch tool may return a summary or extracted text rather than raw bytes. When you rely on a clause, ask the tool for the exact passage and the section/page locator, then PARAPHRASE. Quotes must be under 15 words and attributed. Never invent clause numbers, page numbers, dates or quotations: if you did not see a locator, write "locator not seen".
6. Do not read other working files unless your task names them (independence matters). Do not edit /home/claude/docs or /home/claude/ikhtibar. Write only the output files your task names, under /home/claude/work2/.
7. Never include credentials, cookies or personal data in outputs.

## Verdict vocabulary (verification tasks)
- PASS: clause exists at the stated locator, paraphrase faithful, binding_status correct under the protocol, who/what tested supported, dates/versions right.
- MINOR: small imprecision that does not change meaning (page off by a little, wording slightly strong, citation incomplete).
- ERROR: a check clearly fails (clause absent or elsewhere with different meaning, paraphrase unfaithful or overstated, wrong status, unsupported who/what, wrong version or date).
- UNVERIFIED_BLOCKED: source was blocked per rule 2. Give the exact document to download.
- UNVERIFIABLE_OTHER: source readable but the relevant passage could not be located or read (truncated, garbled, image-only). Say exactly why.
Be sceptical: your job is to find faults. Do not assume the row is right. Check clause numbers yourself.

## Output
CSV written with Python's csv module (proper quoting). Your final message must be short: counts per verdict and a bullet list of every non-PASS row with the proposed correction.
