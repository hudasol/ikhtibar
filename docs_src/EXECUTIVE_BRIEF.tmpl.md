# Executive brief: testing AI before deployment

Prepared for Huda Mueen. Version 3.0, 16 October 2026. Generated from the data files. **Research analysis, not legal advice.** A dagger after a row identifier means the row is excluded from the counts (unverified, or resting on a summary or secondary report only).

## The question

Which governments and institutes require, recommend or merely describe testing of AI systems before deployment, and where does that leave UAE government deployers?

## What was found

- **Most testing text is not binding.** Of {{n_test_head}} test provisions that are not marked unverified, {{head_mc}} ({{head_mc_pct}}) are mandatory or conditional, {{head_vg}} ({{head_vg_pct}}) are voluntary or guidance and {{head_am}} ({{head_am_pct}}) are ambiguous.
- **Recommended is far more common than merely described.** {{nf_summary}}
- **Binding rules usually say that testing must happen, not how.** The EU Act, OMB M-25-21 and the Abu Dhabi DoH Standard require testing against metrics or benchmarks that the regulated party defines or that are not named (`EU-AI-Act-018`, `US-OMB-003`, `UAE-AbuDhabi-DoH-003`). The only EU harmonised standard cited so far (14 October 2026) is about quality management, not test methods (`EU-Standards-P3-20`).
- **Independent testing is binding only in narrow places.** EU notified bodies for some biometric systems and AI Office evaluations of the largest general purpose models (`EU-AI-Act-040`, `EU-AI-Act-071`); Dubai health (`UAE-Dubai-025`); DIFC high risk processing (`UAE-DIFC-ADGM-018`).
- **Binding red teaming is narrow:** {{n_RED_binding}} of {{n_RED}} verified red teaming rows are binding ({{RED_binding_ids}}).
- **For the UAE, one cross government instrument binds entities to test AI, and it is about security.** The National Cyber Security Policy for AI (version 1.1) uses "shall" for testing and validation, secure development and regular testing, and applies to federal ministries and authorities and critical infrastructure entities; whether it reaches emirate government entities directly needs a human reading (`UAE-Federal-P3-01`, `UAE-Federal-P3-08`). It puts AI ethics and fairness outside its scope. Its "test before deployment" wording is guidance (`UAE-Federal-P3-02`). No binding federal text was found that requires testing accuracy or fairness before deployment; that remains sector specific (Abu Dhabi and Dubai health) or zone specific (DIFC). The federal data protection law excludes government entities (`UAE-Federal-034`). No Abu Dhabi government wide AI policy was found, and Dubai's AI policy for government entities is not published.

## What this does not mean

These are gaps in the documents retrieved. They are not statements of what the UAE requires. Public sources were searched in English and Arabic; non public instruments may exist.

## How reliable is it

Separate verifier agents checked a fresh random sample of {{p3f_n}} rows on 16 October 2026: {{p3f_err}} errors in {{p3f_verifiable}} verifiable rows under a strict rubric ({{p3f_rate}}%, 95% interval {{p3f_lo}}% to {{p3f_hi}}%; the interval is wide because the sample is small). All {{p3n_n}} new rows were also checked ({{p3n_err}} errors in {{p3n_verifiable}}). Every error found was corrected. Rows phase 2 could not read were the hardest; graded strictly, {{p3r_err}} of {{p3r_verifiable}} had errors before correction. {{n_unreliable_rows}} rows remain excluded from the counts, mainly Canada's Directive, whose site blocks automated reading. All checking was by AI agents, not human experts.

## Items to confirm

{{brief_time}}

## The checklist and the tool

A proposed checklist of {{n_checklist_items}} items is in `data/checklist.yaml`. The command line tool `python -m ikhtibar.cli` takes answers about a system and returns, for each item, APPLIES, DOES_NOT_APPLY or UNKNOWN with source traces. Anything the answers do not settle is UNKNOWN. A hypothetical example based on the synthetic Madoun prototype is in `examples/MADOUN_EXAMPLE.md`; it is not deployed and no authority uses or endorses it.

## Before relying on any of this

Have a qualified lawyer review it. Download the blocked documents listed in `docs/DOWNLOAD_LIST.md`. Check the items above.
