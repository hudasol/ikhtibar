# Evaluation of the evidence base and the checklist tool

This file is generated from the committed result files in `data/` (see `src/ikhtibar/eval_values.py`). Every number below is read from a result file. Tests check that the main result files agree with the current table (by hash for the baselines, by recomputation for the engine results, robustness, completeness and verification counts), but not every figure in every file is recomputed. It is research, not legal advice.

## What is measured, and what is not

The project makes five kinds of claim, and each is checked by a different method.

| Claim | Check | Section |
|---|---|---|
| Binding status and test type codes are regular, not arbitrary | Simple baselines predict the codes from the text | 1 |
| The checklist tool decides applicability correctly and safely | 94 scenarios written before the tool was run, four naive baselines, and a simulation | 2 |
| The coding can be repeated by someone else | Two blind second codings of {{ag_n}} rows | 3 |
| The headline finding (binding test provisions are a minority) does not depend on coding choices | Sensitivity and bootstrap analysis | 4 |
| Table rows say what the sources say | Fresh independent verification of a random sample of {{vf_sampled}} rows (readable rows only) | 5 |
| The table covers the relevant documents | Pilot recall against an independently built reference list | 6 |

Throughout, the labels are the analyst's own codes (made with AI assistance and then checked), so a high agreement or a high baseline score shows that the coding is regular, not that it is correct. Correctness of the rows is addressed only by section 5.

## 1. Baselines for the two codings

Population: {{bl_n}} headline test rows from {{bl_frameworks}} documents in {{bl_families}} families. Protocols: {{bl_repeats}} times repeated stratified five fold cross validation, and leave one family out, which removes every document of a family from training. Intervals are bootstrap 95% intervals over rows (2000 resamples, fixed seed). The models use scikit-learn {{bl_sklearn}}. Methods were chosen by the analyst, who had seen the table, and were committed together with the code.

### Binding status, five classes (mandatory, conditional, voluntary, guidance, ambiguous)

{{bl_binding5}}

### Binding status, three classes (binding, non binding, ambiguous)

{{bl_binding3}}

### Primary test type, fifteen classes

{{bl_type}}

### Reading the results

- Binding status is largely a property of the document, in the sense that a document prior reaches {{bl_fw5}}% accuracy when other provisions of the same document were seen in training, against {{bl_maj5}}% for the majority class. This is close to tautological. When a whole family is held out, the document prior falls back to the majority rate ({{bl_fw5_lofo}}%), because it has nothing to look up, and the wording rule is the better method.
- A bag of words model does little better than the majority class on binding status ({{bl_tfidf5}}%). Wording alone is a weak signal, which is why the coding reads each provision in the context of its document.
- For test type, a keyword rule built from the taxonomy definitions ({{bl_kw}}%) beats TF-IDF with logistic regression ({{bl_tfidf_type}}%) and the majority class ({{bl_maj_type}}%). With 290 rows and fifteen classes, a learned model has too little data. This is a modest baseline, not evidence that test type is easy to code.
- Limits of these baselines: intervals are bootstrap intervals over rows and ignore clustering by document, so they understate uncertainty. The keyword lexicon was written by an analyst who had seen the table. The text classified is the analyst's own paraphrase. The labels are the analyst's own codes.
- The best baseline is therefore not a trained model. Any later classifier, or any language model coder, should be compared with the document prior and the keyword rule, not with the majority class alone.

## 2. Evaluation of the checklist tool

The tool reads a set of answers about a system and returns, for each of {{ev_items}} checklist items, APPLIES, DOES_NOT_APPLY or UNKNOWN. Missing answers never make a condition true or false.

Design. {{ev_scn}} scenarios were written from the checklist YAML alone by a separate author, with expected results from an independent oracle, and committed before the engine was run. {{ev_spec}} scenarios have a specified result, {{ev_unspec}} are invalid inputs with no specified result, and each of ten stated assumptions (A1 to A10) marks the scenarios whose expectation depended on it. Five pairs of scenarios test monotonicity (adding an answer must not flip APPLIES to DOES_NOT_APPLY).

{{ev_table}}

"Wrongly excluded" means the method said DOES_NOT_APPLY where the expected result was APPLIES or UNKNOWN. "Wrongly applied" means it said APPLIES where the expected result was DOES_NOT_APPLY or UNKNOWN.

Results.

- The engine agreed with the preregistered expectation on {{ev_ok}} of {{ev_dec}} item decisions ({{ev_acc}}%), and matched {{ev_exact}} of {{ev_spec}} scenarios exactly ({{ev_exact_pct}}%). It never wrongly excluded or wrongly applied an item ({{ev_wex}} and {{ev_wap}}).
- The two valued baselines score about 57% because they cannot express unknown, and they are unsafe in opposite ways: the closed version drops items the user cannot yet rule out, and the open version applies items that do not apply. The oracle uses three valued logic, so two valued designs are penalised by construction. The fairer comparison is the design that ignores the answers and returns UNKNOWN for conditional items ({{ev_struct_acc}}% with no errors); the engine beats it because it uses the answers. The engine returns UNKNOWN in {{ev_unknown}} item decisions and states which answer would settle each one. The final figure is after two defects found by these scenarios were fixed.
- The first run, before any change, matched {{ev0_ok}} of {{ev_dec}} decisions ({{ev0_acc}}%) and {{ev0_exact}} of {{ev_spec}} scenarios, but wrongly excluded {{ev0_wex}} items (an empty list given for a multiple choice question was treated as a known answer that matched nothing) and crashed on {{ev0_crash}} of the {{ev_invalid_n}} invalid inputs (a list given for a single value question). These were reported in `data/evaluation/initial_run/`, fixed in the engine with tests, and the scenarios were rerun. The preregistered expectations were not edited.
- One scenario still disagrees (S43: an unknown inside a list of values). The oracle expected APPLIES under three valued OR; the engine returns UNKNOWN. The engine is deliberately conservative here, the specification was ambiguous (assumption A2), and the divergence is recorded in `docs/DECISIONS.md` rather than hidden.
- Of the {{ev_invalid_n}} invalid inputs, {{ev_invalid_rejected}} were rejected with a message that names the valid values, {{ev_invalid_accepted}} were accepted and {{ev_invalid_crashed}} crashed. The accepted case is a comma separated string for a multiple choice question, which the engine splits into a list by design (scenario S75); the preregistration had expected rejection or unknown, so this is a disagreement and is reported.
- The preregistration rests on the order of commits (the scenario file was committed before the harness that runs the engine) and on the author's report; there is no external timestamp.
- Simulation (a property that holds by construction of three valued logic, so it tests the implementation and not the design): {{ev_sim_profiles}} random profiles were answered one question at a time in random order ({{ev_sim_steps}} steps). No step flipped an item from APPLIES to DOES_NOT_APPLY or the reverse ({{ev_sim_flips}} flips).

What this does not show. The scenarios test whether the engine implements the checklist as written. They do not show that the checklist rules are legally correct, which needs a domain reviewer.

## 3. Coding reliability

Two blind coders, working only from the row text and a written codebook, recoded {{ag_n}} randomly chosen headline test rows. Cells show percentage agreement with Cohen's kappa in brackets.

{{ag_table}}

The two blind coders agree with each other closely (kappa {{ag_k_blind}} on five classes). Each agrees less with the original coding (kappa {{ag_k_orig_range}}). In {{ag_odd_original}} of the {{ag_odd_total}} binding status disagreements where exactly one coder differs (one more row has three different codes), the original is the odd one out. The original coder used ambiguous on {{ag_amb_orig}} of {{ag_n}} rows, against {{ag_amb_b2}} and {{ag_amb_b3}} for the blind coders, and the dominant pattern is ambiguous in the original against guidance in both blind codings. Two causes are possible and cannot be separated here: the original coder read the whole document while the blind coders read one provision, and the written instructions differed (the blind codebook asks for ambiguous to be used sparingly). The blind coders also saw the analyst's paraphrase and the document name, so agreement is probably higher than it would be on raw text. For these reasons the original coding is not described as inaccurate, and agreement is not described as accuracy. A human second coding is still needed; a template of 100 rows is provided in `data/coding/phase4/human_gold_template.csv`, and the agreement script reads it when it is filled in.

## 4. Robustness of the headline finding

Claim under test: binding (mandatory or conditional) test provisions are a minority of test provisions. Headline: {{rb_bind}} of {{rb_n}} ({{rb_pct}}%).

{{rb_table}}

The claim {{rb_survives}}. Even when every excluded row and every ambiguous row is counted as binding, the binding share is {{rb_max}}%. The share is also not driven by a few long documents: of {{rb_docs}} documents, {{rb_docs_any}} ({{rb_docs_any_pct}}%) contain any binding test provision. The conclusion that binding provisions are a minority is supported, but the size of the minority depends on coding choices and should be quoted with the interval, not as one number.

## 5. Fresh independent verification

{{vf_sampled}} rows were drawn at random (fixed seed) from the {{vf_pop}} rows that earlier checks had marked as verified and readable. A verifier who saw only the row and the rules reread the primary source. A source can be read only when the session can fetch it, and {{vf_unread}} of {{vf_sampled}} rows ({{vf_unread_pct}}%) could not be read in this session, mostly because of a session level domain allowlist, not because the sites refused. The error rates below therefore describe the {{vf_read}} readable rows only.

| Measure | Rows | Rate | 95% interval (Wilson) |
|---|---|---|---|
| Errors, as graded by the verifier | {{vf_err_g}} of {{vf_read}} | {{vf_err_g_pct}}% | {{vf_err_g_ci}} |
| Errors, after the lead applied the rubric strictly | {{vf_err_s}} of {{vf_read}} | {{vf_err_s_pct}}% | {{vf_err_s_ci}} |
| Any fault, including minor | {{vf_fault}} of {{vf_read}} | {{vf_fault_pct}}% | {{vf_fault_ci}} |

Rows with a strict error: {{vf_err_rows}}. Only {{vf_eu_read}} of {{vf_eu_sampled}} sampled European Union rows could be read, and that family supplies a large share of the binding rows, so the rate says little about the rows behind the headline. It is also a rate among rows that earlier checks had already passed. The phase 3 fresh sample (drawn before the corrections) is reported separately because it was drawn at a different time: {{p3f_err}} errors in {{p3f_verifiable}} verifiable rows ({{p3f_rate}}%, 95% interval {{p3f_lo}}% to {{p3f_hi}}%); the phase 3 recheck of rows phase 2 had left open found {{p3r_err}} in {{p3r_verifiable}} ({{p3r_rate}}%). The true error rate of the whole table is plausibly higher than the readable subset of this sample suggests. Accepted corrections were applied to the table and listed in `data/verification/phase4/patches_p4.json`. If every unreadable row were an error, the rate for the sample could be as high as {{vf_bound_hi}}%, so the rate describes readable rows and must not be extended to the rest without saying so. The unreadable rows are listed for manual checking.

## 6. Completeness pilot

A separate agent built a reference list of {{cp_ref}} candidate documents without seeing the table, and the matches were made by hand. {{cp_out}} candidates were outside the stated frame. Of {{cp_pos}} candidates confirmed to contain a testing provision, {{cp_in}} are in the table: recall {{cp_rec}}% (95% interval {{cp_ci}}). A further {{cp_unres}} candidates could not be confirmed either way, of which {{cp_unres_in}} are in the table, so the most pessimistic recall is {{cp_lb}}%. Missed documents (all United States federal): {{cp_missed}}. Of the {{cp_unres_miss}} unresolved candidates not in the table, {{cp_unres_miss_uae}} are UAE instruments. Matching was done by hand by the author of the table. After the benchmark was scored, the six confirmed misses were read from official hosts ({{us_read}} of {{us_total}} readable) and {{us_cand_rows}} candidate rows were drafted from them in `data/completeness/us_docs_candidate_rows.csv`. Those rows are not in the table and were not used to change the recall figure, because they have not been independently verified; adding them unverified would also raise recall by construction.

This is a pilot, not a population estimate. The reference list was built under the same tool limits as the table, so the two are not independent of search behaviour, and the interval is wide because the count is small.

## 7. What these results allow

- The table can be described as a documented, partly independently checked evidence base. It can not be described as complete or error free.
- The headline that binding test provisions are a minority is robust to the coding choices tested here.
- The checklist tool implements its specification safely (it never excluded an item it should not), with one documented conservative divergence. Its legal correctness has not been reviewed.
- Open items that need the author or an outside reviewer are listed in `docs/GAP_ANALYSIS.md`.
