# Evaluation of the evidence base and the checklist tool

This file is generated from the committed result files in `data/` (see `src/ikhtibar/eval_values.py`). Every number below is read from a result file, and a test fails if a result file is older than the table it describes. It is research, not legal advice.

## What is measured, and what is not

The project makes five kinds of claim, and each is checked by a different method.

| Claim | Check | Section |
|---|---|---|
| Binding status and test type codes are regular, not arbitrary | Simple baselines predict the codes from the text | 1 |
| The checklist tool decides applicability correctly and safely | 94 scenarios written before the tool was run, four naive baselines, and a simulation | 2 |
| The coding can be repeated by someone else | Two blind second codings of {{ag_n}} rows | 3 |
| The headline finding (binding test provisions are a minority) does not depend on coding choices | Sensitivity and bootstrap analysis | 4 |
| Table rows say what the sources say | Fresh independent verification of a random sample of {{vf_sampled}} rows | 5 |
| The table covers the relevant documents | Pilot recall against an independently built reference list | 6 |

Throughout, the labels are the analyst's own codes (made with AI assistance and then checked), so a high agreement or a high baseline score shows that the coding is regular, not that it is correct. Correctness of the rows is addressed only by section 5.

## 1. Baselines for the two codings

Population: {{bl_n}} headline test rows from {{bl_frameworks}} documents in {{bl_families}} families. Protocols: {{bl_repeats}} times repeated stratified five fold cross validation, and leave one family out, which removes every document of a family from training. Intervals are bootstrap 95% intervals over rows (2000 resamples, fixed seed). The models use scikit-learn {{bl_sklearn}}. Methods and cut offs were fixed before any result was seen.

### Binding status, five classes (mandatory, conditional, voluntary, guidance, ambiguous)

{{bl_binding5}}

### Binding status, three classes (binding, non binding, ambiguous)

{{bl_binding3}}

### Primary test type, fifteen classes

{{bl_type}}

### Reading the results

- Binding status is largely a property of the document, not of the sentence. The document prior reaches {{bl_fw5}}% accuracy when documents are seen in training, against {{bl_maj5}}% for the majority class. When a whole family is held out, the document prior falls back to the majority rate ({{bl_fw5_lofo}}%), because it has nothing to look up.
- A bag of words model does little better than the majority class on binding status ({{bl_tfidf5}}%). Wording alone is a weak signal, which is why the coding reads each provision in the context of its document.
- For test type, a keyword rule built from the taxonomy definitions ({{bl_kw}}%) beats TF-IDF with logistic regression ({{bl_tfidf_type}}%) and the majority class ({{bl_maj_type}}%). With 290 rows and fifteen classes, a learned model has too little data. This is a modest baseline, not evidence that test type is easy to code.
- The best baseline is therefore not a trained model. Any later classifier, or any language model coder, should be compared with the document prior and the keyword rule, not with the majority class alone.

## 2. Evaluation of the checklist tool

The tool reads a set of answers about a system and returns, for each of {{ev_items}} checklist items, APPLIES, DOES_NOT_APPLY or UNKNOWN. Missing answers never make a condition true or false.

Design. {{ev_scn}} scenarios were written from the checklist YAML alone by a separate author, with expected results from an independent oracle, and committed before the engine was run. {{ev_spec}} scenarios have a specified result, {{ev_unspec}} are invalid inputs with no specified result, and each of ten stated assumptions (A1 to A10) marks the scenarios whose expectation depended on it. Five pairs of scenarios test monotonicity (adding an answer must not flip APPLIES to DOES_NOT_APPLY).

{{ev_table}}

"Wrongly excluded" means the method said DOES_NOT_APPLY where the expected result was APPLIES or UNKNOWN. "Wrongly applied" means it said APPLIES where the expected result was DOES_NOT_APPLY or UNKNOWN.

Results.

- The engine agreed with the preregistered expectation on {{ev_ok}} of {{ev_dec}} item decisions ({{ev_acc}}%), and matched {{ev_exact}} of {{ev_spec}} scenarios exactly ({{ev_exact_pct}}%). It never wrongly excluded or wrongly applied an item ({{ev_wex}} and {{ev_wap}}).
- The two valued baselines look acceptable on accuracy alone but are unsafe: the closed version drops items the user cannot yet rule out, and the open version applies items that do not apply. The engine returns UNKNOWN in {{ev_unknown}} item decisions instead, and states which answer would settle each one.
- The first run, before any change, matched {{ev0_ok}} of {{ev_dec}} decisions ({{ev0_acc}}%) and {{ev0_exact}} of {{ev_spec}} scenarios, but wrongly excluded {{ev0_wex}} items (an empty list given for a multiple choice question was treated as a known answer that matched nothing) and crashed on {{ev0_crash}} of the {{ev_invalid_n}} invalid inputs (a list given for a single value question). These were reported in `data/evaluation/initial_run/`, fixed in the engine with tests, and the scenarios were rerun. The preregistered expectations were not edited.
- One scenario still disagrees (S43: an unknown inside a list of values). The oracle expected APPLIES under three valued OR; the engine returns UNKNOWN. The engine is deliberately conservative here, the specification was ambiguous (assumption A2), and the divergence is recorded in `docs/DECISIONS.md` rather than hidden.
- Of the {{ev_invalid_n}} invalid inputs, {{ev_invalid_rejected}} were rejected with a message that names the valid values and {{ev_invalid_crashed}} crashed.
- Simulation: {{ev_sim_profiles}} random profiles were answered one question at a time in random order ({{ev_sim_steps}} steps). No step flipped an item from APPLIES to DOES_NOT_APPLY or the reverse ({{ev_sim_flips}} flips).

What this does not show. The scenarios test whether the engine implements the checklist as written. They do not show that the checklist rules are legally correct, which needs a domain reviewer.

## 3. Coding reliability

Two blind coders, working only from the row text and a written codebook, recoded {{ag_n}} randomly chosen headline test rows. Cells show percentage agreement with Cohen's kappa in brackets.

{{ag_table}}

The two blind coders agree with each other closely (kappa {{ag_k_blind}} on five classes). Each agrees less with the original coding (kappa about {{ag_k_orig}}). In {{ag_odd_original}} of the {{ag_odd_total}} binding status disagreements where exactly one coder differs, the original is the odd one out. The dominant pattern is the original coder coding a provision as ambiguous where both blind coders code it as guidance. This is an information difference, not a pure error: the original coder read the whole document, and the blind coders saw one provision. For that reason the original coding is not described as inaccurate, and the blind agreement is not described as accuracy either. A human second coding is still needed; a template of 100 rows is provided in `data/coding/phase4/human_gold_template.csv`, and the agreement script reads it when it is filled in.

## 4. Robustness of the headline finding

Claim under test: binding (mandatory or conditional) test provisions are a minority of test provisions. Headline: {{rb_bind}} of {{rb_n}} ({{rb_pct}}%).

{{rb_table}}

The claim {{rb_survives}}. Even when every excluded row and every ambiguous row is counted as binding, the binding share is {{rb_max}}%. The share is also not driven by a few long documents: of {{rb_docs}} documents, {{rb_docs_any}} ({{rb_docs_any_pct}}%) contain any binding test provision. The conclusion that binding provisions are a minority is supported, but the size of the minority depends on coding choices and should be quoted with the interval, not as one number.

## 5. Fresh independent verification

{{vf_sampled}} rows were drawn at random (fixed seed) from the {{vf_pop}} rows that earlier checks had marked as verified and readable. A verifier who saw only the row and the rules re read the primary source. A source can be read only when the session can fetch it, and {{vf_unread}} of {{vf_sampled}} rows ({{vf_unread_pct}}%) could not be read in this session, mostly because of a session level domain allowlist, not because the sites refused. The error rates below therefore describe the {{vf_read}} readable rows only.

| Measure | Rows | Rate | 95% interval (Wilson) |
|---|---|---|---|
| Errors, as graded by the verifier | {{vf_err_g}} of {{vf_read}} | {{vf_err_g_pct}}% | {{vf_err_g_ci}} |
| Errors, after the lead applied the rubric strictly | {{vf_err_s}} of {{vf_read}} | {{vf_err_s_pct}}% | {{vf_err_s_ci}} |
| Any fault, including minor | {{vf_fault}} of {{vf_read}} | {{vf_fault_pct}}% | {{vf_fault_ci}} |
| Strict errors pooled with the phase 3 fresh sample | {{vf_pool}} | | |

Rows with a strict error: {{vf_err_rows}}. Accepted corrections were applied to the table and listed in `data/verification/phase4/patches_p4.json`. If every unreadable row were an error, the rate for the sample could be as high as {{vf_bound_hi}}%, so the rate describes readable rows and must not be extended to the rest without saying so. The unreadable rows are listed for manual checking.

## 6. Completeness pilot

A separate agent built a reference list of {{cp_ref}} candidate documents without seeing the table, and the matches were made by hand. {{cp_out}} candidates were outside the stated frame. Of {{cp_pos}} candidates confirmed to contain a testing provision, {{cp_in}} are in the table: recall {{cp_rec}}% (95% interval {{cp_ci}}). A further {{cp_unres}} candidates could not be confirmed either way, of which {{cp_unres_in}} are in the table, so the most pessimistic recall is {{cp_lb}}%. Missed documents: {{cp_missed}}.

This is a pilot, not a population estimate. The reference list was built under the same tool limits as the table, so the two are not independent of search behaviour, and the interval is wide because the count is small.

## 7. What these results allow

- The table can be described as a documented, partly independently checked evidence base. It can not be described as complete or error free.
- The headline that binding test provisions are a minority is robust to the coding choices tested here.
- The checklist tool implements its specification safely (it never excluded an item it should not), with one documented conservative divergence. Its legal correctness has not been reviewed.
- Open items that need the author or an outside reviewer are listed in `docs/GAP_ANALYSIS.md`.
