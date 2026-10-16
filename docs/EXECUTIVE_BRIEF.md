# Executive brief: testing AI before deployment

Prepared for Huda Mueen. Version 3.0, 16 October 2026. Generated from the data files. **Research analysis, not legal advice.** A dagger after a row identifier means the row is excluded from the counts (unverified, or resting on a summary or secondary report only).

## The question

Which governments and institutes require, recommend or merely describe testing of AI systems before deployment, and where does that leave UAE government deployers?

## What was found

- **Most testing text is not binding.** Of 290 test provisions that are not marked unverified, 81 (28%) are mandatory or conditional, 173 (60%) are voluntary or guidance and 36 (12%) are ambiguous.
- **Recommended is far more common than merely described.** Of 209 such headline rows, 140 recommend a test, 40 only describe testing practice, 19 use obligation wording in a document that is not binding or whose force is unclear, and 10 were disputed between the coders (agreement 95.4%, Cohen's kappa 0.9).
- **Binding rules usually say that testing must happen, not how.** The EU Act, OMB M-25-21 and the Abu Dhabi DoH Standard require testing against metrics or benchmarks that the regulated party defines or that are not named (`EU-AI-Act-018`, `US-OMB-003`, `UAE-AbuDhabi-DoH-003`). The only EU harmonised standard cited so far (14 October 2026) is about quality management, not test methods (`EU-Standards-P3-20`).
- **Independent testing is binding only in narrow places.** EU notified bodies for some biometric systems and AI Office evaluations of the largest general purpose models (`EU-AI-Act-040`, `EU-AI-Act-071`); Dubai health (`UAE-Dubai-025`); DIFC high risk processing (`UAE-DIFC-ADGM-018`).
- **Binding red teaming is narrow:** 4 of 26 verified red teaming rows are binding (`EU-AI-Act-063`, `EU-AI-Act-068`, `EU-AI-Act-071`, `EU-AI-Act-P3-20`).
- **For the UAE, one cross government instrument binds entities to test AI, and it is about security.** The National Cyber Security Policy for AI (version 1.1) uses "shall" for testing and validation, secure development and regular testing, and applies to federal ministries and authorities and critical infrastructure entities; whether it reaches emirate government entities directly needs a human reading (`UAE-Federal-P3-01`, `UAE-Federal-P3-08`). It puts AI ethics and fairness outside its scope. Its "test before deployment" wording is guidance (`UAE-Federal-P3-02`). No binding federal text was found that requires testing accuracy or fairness before deployment; that remains sector specific (Abu Dhabi and Dubai health) or zone specific (DIFC). The federal data protection law excludes government entities (`UAE-Federal-034`). No Abu Dhabi government wide AI policy was found, and Dubai's AI policy for government entities is not published.

## What this does not mean

These are gaps in the documents retrieved. They are not statements of what the UAE requires. Public sources were searched in English and Arabic; non public instruments may exist.

## How reliable is it

Separate verifier agents checked a fresh random sample of 30 rows on 16 October 2026: 3 errors in 23 verifiable rows under a strict rubric (13.0%, 95% interval 4.5% to 32.1%; the interval is wide because the sample is small). All 56 new rows were also checked (7 errors in 56). Every error found was corrected. Rows phase 2 could not read were the hardest; graded strictly, 15 of 142 had errors before correction. 38 rows remain excluded from the counts, mainly Canada's Directive, whose site blocks automated reading. All checking was by AI agents, not human experts.

## Items to confirm

- **EU Omnibus (Regulation (EU) 2026/1744):** identity, 27 July 2026 entry into force and the 2 August 2027 sandbox date are confirmed. The Annex III date (2 December 2027) and Annex I date (2 August 2028) are confirmed at recital level only; the operative Article 113 text is still to be read.
- **DoH Responsible AI Standard:** V1, October 2025, revision due October 2026. Whether it has been revised is open (listing pages unreadable).
- **DIFC Regulation 10:** the Commissioner has published an accreditation and certification framework; amendments after Version No. 2 are unchecked.
- **Saudi drafts:** none can be called final from the evidence retrieved; the NCA document is a draft and SDAIA 2025 documents were blocked.

## The checklist and the tool

A proposed checklist of 30 items is in `data/checklist.yaml`. The command line tool `python -m ikhtibar.cli` takes answers about a system and returns, for each item, APPLIES, DOES_NOT_APPLY or UNKNOWN with source traces. Anything the answers do not settle is UNKNOWN. A hypothetical example based on the synthetic Madoun prototype is in `examples/MADOUN_EXAMPLE.md`; it is not deployed and no authority uses or endorses it.

## Before relying on any of this

Have a qualified lawyer review it. Download the blocked documents listed in `docs/DOWNLOAD_LIST.md`. Check the items above.
