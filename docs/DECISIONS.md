# Decision log

Judgement calls made during phase 4 (28 October 2026), recorded so a reader can disagree with them. Each entry gives what was decided, why, and what would change it.

## D1. Korea-002 set to conditional, not mandatory

The fresh verifier proposed changing the binding status from guidance to mandatory. The clause applies only when a condition in the source is met, so the status was set to conditional. The row was also one of the five strict errors in the verification sample. A legal reader of the Korean text should confirm this.

## D2. Two rows moved from MINOR to ERROR on strict grading

Korea-003 (the source says public agencies "must give preferential consideration" to certified products, the row said "should prefer") and US-NIST-033 (the row named an actor the source does not name) were graded MINOR by the verifier. The rubric treats a wrong obligation level or an unsupported actor as an error, so the lead regraded both. Both grades are kept: the report gives the rate as graded by the verifier (4 of 94 after the retry rounds) and the rate after strict grading (6 of 94). The strict rate is the one used in the paper.

## D3. S43 left as a documented divergence

Scenario S43 gives an unknown value inside a list of values. The independent oracle expected APPLIES (three valued OR); the engine returns UNKNOWN. The engine was not changed, for two reasons: the specification did not say how an unknown inside a list should be handled (assumption A2), and returning UNKNOWN is the safer error, because it asks the user to settle the answer instead of asserting that an item applies. The three item level misses are reported in `data/evaluation/misses.csv`. If a reviewer decides that APPLIES is intended, the change is not one line: the unknown inside a list is dropped in `validate_answers`, and keeping it there would make the `any_contains` operator return FALSE for a list with no match plus an unknown, which breaks assumption A2 and wrongly excludes items. A correct change needs a rule in `evaluate` as well, and new tests.

## D4. Engine input validation changed after the first run

The preregistered invalid input scenarios exposed two defects: a list given for a single value question crashed the engine, and an empty list for a multiple choice question was treated as a known answer that matched nothing. The engine now raises a clear error for the first and treats the second as unknown. The first run is preserved in `data/evaluation/initial_run/` and the scenario expectations were not edited after the run.

## D5. The original coding is not called inaccurate

Blind coders agree with each other far more than with the original coding. The main disagreement is the original coder using ambiguous where both blind coders use guidance. The original coder read the whole document and the blind coders read one provision, and the two codebooks also differed (the blind codebook asks for ambiguous to be used sparingly), so the gap cannot be assigned to information or to error. The blind coders saw the analyst's paraphrase and the document name, so agreement is probably higher than on raw text. The report states the agreement figures and does not equate agreement with accuracy. A human gold set (100 rows, template provided) is the intended resolution.

## D6. Verification rates are for readable rows only

At first 39% of the fresh sample could not be read, and 22% (26 of 120) still could not be read after two retry rounds, in the working session because of a session level domain allowlist, not because the sites refused access. No workaround was used (no changed user agents, caches or mirrors). The error rates are stated for the readable rows, with the extreme bounds if every unreadable row were an error, and the unreadable rows are listed for manual checking.

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

## D11. Model identity is recorded as data, not named in prose

The overnight brief asks for the exact model name and version of every coder, extractor and verifier run to be recorded in a `model_identity` field and in `data/model_identity_log.csv`. Another standing rule asks that no product name appears in public material. I read the first as a data requirement and the second as a rule for prose: the identifier is kept only in the log and in result file fields, and sentences in the paper and the documents say "language model agents" without a product name. If she prefers the identifier redacted, the log can be replaced by the generic text without changing any result. Where an agent could not report its identity, the log says so.

## D12. Fetch tool allowlist and the search workaround

During this run the fetch tool accepted only addresses that had appeared in search results or in pages already read. The readers were therefore told to search the exact title and fetch the official result link (rule 3a of the phase 4 rules, copied to `data/verification/phase5/RULES_P5.md`). The search budget for the turn (200, shared by all agents) was then used up, so later tasks could fetch only addresses seen before. No cache, mirror, archive or third party copy was used. The fetch tool also answers through a summarising model, so readers saw summaries, not verbatim pages; page numbers and wording from that route are less reliable, and every affected row says so in `evidence_grade` and `text_basis`.

## D13. Tag push and the frozen reference

The remote refused the push of tag `v4.0-paper-frozen` (HTTP 403 on tag refs through the session proxy, one retry). The tag exists locally at commit fa3e410, and a branch `frozen/v4.0-paper` was created at the same commit through the repository connector. The branch must not be advanced. Copies of the version 4.0 result files are in `data/phase5/frozen_v4/` so the new numbers can be set next to them.

## D14. Extraction recall: sample exclusions and the precision basis

Of the 14 documents drawn (seed 20261103), two (X01 and X10) were excluded because the reader could not obtain the text (X01 unreadable, X10 headings only). Only three documents (X02, X06, X12) were read in their whole text; for the others the summarising fetch tool reached only part, so recall is computed over what the reader reached and precision is computed only over the three documents read whole. Recall counts yes or partial matches. The recall figure is therefore a rough measure, and the partial reading may bias it in either direction. Missed provisions are in `missed_candidates.csv` and are not added to the headline table.

## D15. Phase 5 ids and retrieval dates for the US candidate rows

The 19 US candidate rows from the completeness pilot were renamed from the P4 ids to `<family>-P5-<nn>`, as the brief asks. Their retrieval date is recorded as 3 November 2026, the date the fresh verifiers read the sources. The verifier corrections (locator fixes, one binding status corrected from conditional to mandatory for the OMB authorization to operate clause) are applied through `data/verification/phase5/patches_p5_us.json`.

## D16. Which existing rows were sampled for the fresh check

Every family had been touched by an earlier fresh draw, so "families not previously sampled" could not be applied literally. I took the families where earlier fresh draws had covered at most a quarter of the rows (Canada, Saudi, UAE Abu Dhabi DoH), drew from rows never in any fresh draw (seed 20261103, 30 rows), and report the rest of the result separately. Most of these rows could not be read because of the allowlist and site blocks (see the stats file); the error rate rests on a handful of readable rows and is reported with its wide interval.

## D17. Choice of instruments for new rows

The second reference list has 189 instruments (91 with a testing provision). I extracted rows for 36 of the 58 that were read, had a testing provision and were not in the table, choosing a spread across jurisdictions and sources and skipping near duplicates (several ITU recommendations, several Japanese road transport documents, drafts without readable text). The rest are listed in `data/completeness/reference_list_p5.csv` and remain candidates. New rows from catalogue pages only are marked `catalogue-level only` and do not enter the headline counts.

## D18. UAE Arabic check and time sensitive rereads blocked

The four Arabic readers and the National Cyber Security Policy scope check returned nothing, because the search budget was already used up and the fetch tool refused addresses it had not seen. Tasks 4 and 5 are logged as blocked and can be rerun when the budget resets. No result is claimed; the scope question stays open and the UAE rows stay "not read in original Arabic". The script, input files and tests are in place.

## D19. Completeness comparison with the first list

The second list was built and matched by agents using the same tools as the table, so the two lists are not independent samples and no capture recapture estimate is made. Matching used titles, issuers and addresses only, and two matchers said they relied on catalogue knowledge for some standards; the matching file shows the notes. The table at matching time already contained the 19 US rows, which were the misses of the first pilot.

## D20. Texas H.B. 149 rows left ambiguous

Two fresh verifiers disagreed about the two Texas rows (one proposed conditional, the other mandatory), and both noted that the text read is the Senate committee substitute, not the enacted act. The enacted text could not be fetched in the session. I kept their wording corrections but set the binding status of both rows to ambiguous with a note, because a status cannot be settled from a version that is not the law. This is a status of the text read, not a statement about what Texas requires.

## D21. Model identity recorded without the vendor product name

The overnight brief asks for the exact name and version of the model behind every coder, extractor and verifier run. A later instruction from the author says that no vendor or assistant name may appear anywhere in the repository. The two cannot both be met in full. I kept the record and removed the name: `data/model_identity_log.csv` and the run metadata files state "language model version 5.5 (mid size tier)" and the configured identifier field reads "identifier withheld". The exact identifier was reported by the agents and is known to the author from the session settings; it can be added back by her if a venue requires it. Local paths that contained the workspace user name were replaced by neutral placeholders. Names of companies and products that occur inside quoted source text (for example a signatory list in an international commitment, or a coding assistant named in a regulator's text) are source content, not attribution, and were left untouched.

## D22. Traces in published history

The local `main` branch and the frozen branch contain no assistant author, committer, trailer or session link. The remote reference `refs/pull/1/head` (the closed first pull request) still holds three early commits authored as the assistant, with attribution trailers. They cannot be removed without rewriting published history, which is forbidden, so they are listed in `docs/MORNING_NOTE.md`. Handoff item 7 was stale on this point and was corrected.

## D23. New primary analysis and the failed criterion (phase 6)

On the author's instruction to build the strongest paper and not to keep the old headline, the primary analysis was moved from the row share of binding provisions to document level force, registered in `docs/PREREG_PHASE6.md`. The split (seed 20261106) and the analysis code were committed at b58df0b before the confirmation half was analysed. Design work changed two thresholds: the concordance excess threshold from 30 to 20 points, and the row level share was made non decisive (a long statute moved it in the design half). Criterion C2 still failed on confirmation (lower bound 14.4); I did not lower the threshold again and I did not drop it. The follow up statistic (prevalence adjusted within document kappa, `src/ikhtibar/exploratory6.py`) was written after the confirmation result and is labelled exploratory. Disclosure: aggregate shares over the whole table had been seen in phase 5, so confirmation marginals were not unseen. Everything in the earlier sections is labelled exploratory and designed on the version 4.0 pilot.
