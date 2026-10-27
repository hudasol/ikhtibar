# Executive brief: testing AI before deployment

Prepared for Huda Mueen. Version 3.0, 16 October 2026. Generated from the data files. **Research analysis, not legal advice.** A dagger after a row identifier means the row is excluded from the counts (unverified, or resting on a summary or secondary report only).

## The question

Which governments and institutes require, recommend or merely describe testing of AI systems before deployment, and where does that leave UAE government deployers?

## What was found

- **Most testing text is not binding.** Of 290 test provisions that are not excluded, 81 (28%) are mandatory or conditional, 174 (60%) are voluntary or guidance and 35 (12%) are ambiguous.
- **Recommended is far more common than merely described.** Of 209 such headline rows, 140 recommend a test, 40 only describe testing practice, 19 use obligation wording in a document that is not binding or whose force is unclear, and 10 were disputed between the coders (agreement 95.2% on these rows; 95.4% and Cohen's kappa 0.9 on all 216 rows coded).
- **Binding rules usually say that testing must happen, not how** (our reading of the rows cited). The EU Act, OMB M-25-21 and the Abu Dhabi DoH Standard require testing against metrics or benchmarks that the regulated party defines or that the text does not name (`EU-AI-Act-018`, `US-OMB-003`, `UAE-AbuDhabi-DoH-003`). The only EU harmonised standard cited so far (14 October 2026) is about quality management, not test methods (`EU-Standards-P3-20`).
- **Independent assessment is binding only in narrow places.** EU notified bodies for some biometric systems and AI Office evaluations of general purpose models with systemic risk (`EU-AI-Act-040`, `EU-AI-Act-071`); independent validation and audit for Dubai health AI (`UAE-Dubai-025`); certification for DIFC high risk processing, which reviews governance documents rather than testing performance (`UAE-DIFC-ADGM-018`, `UAE-DIFC-ADGM-020`).
- **Binding red teaming is narrow:** only one provision obliges a provider to run adversarial tests, for EU general purpose models with systemic risk (`EU-AI-Act-068`).
- **For the UAE, one cross government instrument uses "shall" for AI testing, and it is about security.** The National Cyber Security Policy for AI (version 1.1) uses "shall" for testing and validation, secure development and regular testing, and applies to federal ministries and authorities and non government critical infrastructure entities (coded mandatory for them; the document does not state its legal basis); whether it reaches emirate government entities directly needs a human reading (`UAE-Federal-P3-01`, `UAE-Federal-P3-08`). It puts AI ethics and fairness outside its scope. Its "test before deployment" wording is guidance (`UAE-Federal-P3-02`). No binding federal text was found that requires testing accuracy or fairness before deployment; binding performance testing remains sector specific (Abu Dhabi and Dubai health, `UAE-AbuDhabi-DoH-003`, `UAE-Dubai-025`), and DIFC requires certification for commercial high risk processing (`UAE-DIFC-ADGM-004`). The federal data protection law excludes government entities (`UAE-Federal-034`). No Abu Dhabi government wide AI policy was found, and Dubai's AI policy for government entities is not published.

## What this does not mean

These are gaps in the documents retrieved. They are not statements of what the UAE requires. Public sources were searched in English and Arabic; non public instruments may exist.

## How reliable is it

Separate verifier agents checked a fresh random sample of 30 rows on 16 October 2026: 3 errors in 23 verifiable rows under a strict rubric (13.0%, 95% interval 4.5% to 32.1%; the interval is wide because the sample is small). All 56 new rows were also checked (7 errors in 56). Every error found was corrected. Rows phase 2 could not read were the hardest; graded strictly, 15 of 142 had errors before correction. 38 rows remain excluded from the counts, mainly Canada's Directive, whose site blocks automated reading. All checking was by AI agents, not human experts.

## Items to confirm

- **EU Act dates:** confirmed in operative text on 16 October 2026: Annex III high risk rules from 2 December 2027 and Annex I from 2 August 2028 (amended Article 113). The first harmonised standard (quality management) was cited on 14 October 2026.
- **UAE National Cyber Security Policy for AI:** confirm by hand whether it reaches emirate government entities directly; two verifiers read the scope clause differently.
- **DoH Responsible AI Standard:** still V1 (October 2025); its revision falls due in October 2026, so check for a new version. The DoH listing shows only the 2018 AI policy.
- **DIFC Regulation 10:** a June 2026 consultation proposes a pre-use safety verification test; not enacted as of 16 October 2026.
- **Saudi instruments:** none is final or binding on its face; the NCA document is a draft that says it is not mandatory, and SDAIA documents could not be read.
- **Moved UAE sources:** six UAE documents verified on 12 October could not be re-read on 16 October; open them in a browser before quoting.

## The checklist and the tool

A proposed checklist of 30 items is in `data/checklist.yaml`. The command line tool `python -m ikhtibar.cli` takes answers about a system and returns, for each item, APPLIES, DOES_NOT_APPLY or UNKNOWN with source traces. Anything the answers do not settle is UNKNOWN. A hypothetical example based on the synthetic Madoun prototype is in `examples/MADOUN_EXAMPLE.md`; it is not deployed and no authority uses or endorses it.

## Before relying on any of this

Have a qualified lawyer review it. Download the blocked documents listed in `docs/DOWNLOAD_LIST.md`. Check the items above.
