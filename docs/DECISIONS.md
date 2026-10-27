# Decision log

Judgement calls made during phase 4 (28 October 2026), recorded so a reader can disagree with them. Each entry gives what was decided, why, and what would change it.

## D1. Korea-002 set to conditional, not mandatory

The fresh verifier proposed changing the binding status from guidance to mandatory. The clause applies only when a condition in the source is met, so the status was set to conditional. The row was also one of the five strict errors in the verification sample. A legal reader of the Korean text should confirm this.

## D2. Two rows moved from MINOR to ERROR on strict grading

Korea-003 (the source says public agencies "must give preferential consideration" to certified products, the row said "should prefer") and US-NIST-033 (the row named an actor the source does not name) were graded MINOR by the verifier. The rubric treats a wrong obligation level or an unsupported actor as an error, so the lead regraded both. Both grades are kept: the report gives the rate as graded by the verifier (3 of 73) and the rate after strict grading (5 of 73). The strict rate is the one used in the paper.

## D3. S43 left as a documented divergence

Scenario S43 gives an unknown value inside a list of values. The independent oracle expected APPLIES (three valued OR); the engine returns UNKNOWN. The engine was not changed, for two reasons: the specification did not say how an unknown inside a list should be handled (assumption A2), and returning UNKNOWN is the safer error, because it asks the user to settle the answer instead of asserting that an item applies. The three item level misses are reported in `data/evaluation/misses.csv`. If a reviewer decides that APPLIES is intended, the change is not one line: the unknown inside a list is dropped in `validate_answers`, and keeping it there would make the `any_contains` operator return FALSE for a list with no match plus an unknown, which breaks assumption A2 and wrongly excludes items. A correct change needs a rule in `evaluate` as well, and new tests.

## D4. Engine input validation changed after the first run

The preregistered invalid input scenarios exposed two defects: a list given for a single value question crashed the engine, and an empty list for a multiple choice question was treated as a known answer that matched nothing. The engine now raises a clear error for the first and treats the second as unknown. The first run is preserved in `data/evaluation/initial_run/` and the scenario expectations were not edited after the run.

## D5. The original coding is not called inaccurate

Blind coders agree with each other far more than with the original coding. The main disagreement is the original coder using ambiguous where both blind coders use guidance. The original coder read the whole document and the blind coders read one provision, and the two codebooks also differed (the blind codebook asks for ambiguous to be used sparingly), so the gap cannot be assigned to information or to error. The blind coders saw the analyst's paraphrase and the document name, so agreement is probably higher than on raw text. The report states the agreement figures and does not equate agreement with accuracy. A human gold set (100 rows, template provided) is the intended resolution.

## D6. Verification rates are for readable rows only

About 39% of the fresh sample could not be read in the working session because of a session level domain allowlist, not because the sites refused access. No workaround was used (no changed user agents, caches or mirrors). The error rates are stated for the readable rows, with the extreme bounds if every unreadable row were an error, and the unreadable rows are listed for manual checking.

## D7. Accepted patches

Twenty five verifier patches were accepted after review and none was rejected. Two changed a binding status (UK-004 from ambiguous to guidance, Korea-002 as above); the others changed locators, paraphrases or dates. The patch file records the reason for each.

## D8. Baselines are reported as they came out

The wording rule and the learned text model do poorly on binding status, and the best baseline is a document prior that cannot work for an unseen document. The report says so and does not tune the models to look better. Methods and cut offs were fixed before the results were seen.

## D9. Completeness is a pilot

The reference list used for the recall estimate was built under the same tool limits as the table, and 58 of its candidates could not be resolved either way. The result is reported with its interval and a pessimistic bound, and is not presented as a population estimate.

## D10. Review findings not acted on

An independent review of the repository raised these points; they were examined and left, with reasons.

- Rewriting commit history, adding a `.mailmap`, or removing the assistant trailers from earlier commits: published history is not rewritten under the author's standing rule. A `.mailmap` would change only local display and is not added. See `docs/HANDOFF.md`.
- Removing assistant or organisation names, an official contact address and local paths from data files: they are source facts (a UK AISI report title, a DoH contact address on a source page, a path recorded in a preregistration file that must not be edited after the fact).
- A cluster bootstrap for the baseline intervals: noted as a limit in the evaluation report instead; the document level bootstrap is used for the headline claim.
- Reference metadata gaps (missing authors, years and venues): listed in the handoff note for the author to resolve against the sources.
