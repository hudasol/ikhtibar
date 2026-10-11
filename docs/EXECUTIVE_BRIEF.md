# Executive brief: testing AI before deployment

Prepared for Huda Mueen. Version 2.0, 12 October 2026. Generated from the data files. **Research analysis, not legal advice.** A dagger after a row identifier means the row is excluded from the counts (unverified, or resting on a summary or secondary report only).

## The question

Which governments and institutes require, recommend or merely describe testing of AI systems before deployment, and where does that leave UAE government deployers?

## What was found

- **Most testing text is not binding.** Of 212 test provisions that are not marked unverified, 61 (29%) are mandatory or conditional, 132 (62%) are voluntary or guidance and 19 (9%) are ambiguous. If the 56 excluded test rows were counted, the split would be 85 mandatory or conditional (32%), 162 voluntary or guidance (60%) and 21 ambiguous (8%) of 268.
- **Binding rules usually say that testing must happen, not how.** The EU Act, OMB M-25-21 and the Abu Dhabi DoH Standard require testing against metrics or benchmarks that the regulated party defines or that are not named (`EU-AI-Act-018`, `US-OMB-003`, `UAE-AbuDhabi-DoH-003`).
- **Independent testing is binding only in narrow places.** Dubai health (`UAE-Dubai-025`, `UAE-Dubai-026`) and DIFC high risk processing (`UAE-DIFC-ADGM-004`, `UAE-DIFC-ADGM-018`).
- **Red teaming is not binding in any verified row** (0 of 15).
- **For the UAE,** binding testing text found is sector or zone specific: Abu Dhabi health, Dubai health, DIFC, and Dubai government security controls that are not AI specific. Federal documents retrieved give guidance in "should" language (`UAE-Federal-009`, `UAE-Federal-018`). The federal data protection law excludes government entities (`UAE-Federal-034`).

## What this does not mean

These are gaps in the documents retrieved. They are not statements of what the UAE requires. Public sources were searched in English and Arabic (230 searches and fetches logged); non public instruments may exist.

## How reliable is it

Phase 2 re checked 389 rows with the standard fetch tool only: 13 errors among 293 verifiable rows (4.4%, interval 2.6% to 7.4%). 108 rows are excluded: they could not be verified (source blocked or passage not located) or rest on a summary or secondary report only. Phase 1 verdicts that depended on a user agent workaround were re verified.

## Items to confirm

- **EU Omnibus (Regulation (EU) 2026/1744):** identity, 27 July 2026 entry into force and the 2 August 2027 sandbox date are confirmed. The Annex III date (2 December 2027) and Annex I date (2 August 2028) are confirmed at recital level only; the operative Article 113 text is still to be read.
- **DoH Responsible AI Standard:** V1, October 2025, revision due October 2026. Whether it has been revised is open (listing pages unreadable).
- **DIFC Regulation 10:** the Commissioner has published an accreditation and certification framework; amendments after Version No. 2 are unchecked.
- **Saudi drafts:** none can be called final from the evidence retrieved; the NCA document is a draft and SDAIA 2025 documents were blocked.

## The checklist and the tool

A proposed checklist of 29 items is in `data/checklist.yaml`. The command line tool `python -m ikhtibar.cli` takes answers about a system and returns, for each item, APPLIES, DOES_NOT_APPLY or UNKNOWN with source traces. Anything the answers do not settle is UNKNOWN. A hypothetical example based on the synthetic Madoun prototype is in `examples/MADOUN_EXAMPLE.md`; it is not deployed and no authority uses or endorses it.

## Before relying on any of this

Have a qualified lawyer review it. Download the blocked documents listed in `docs/DOWNLOAD_LIST.md`. Check the items above.
