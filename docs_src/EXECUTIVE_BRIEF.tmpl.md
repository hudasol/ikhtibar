# Executive brief: testing AI before deployment

Prepared for Huda Mueen. Version 2.0, 12 October 2026. Generated from the data files. **Research analysis, not legal advice.** A dagger after a row identifier means the row is excluded from the counts (unverified, or resting on a summary or secondary report only).

## The question

Which governments and institutes require, recommend or merely describe testing of AI systems before deployment, and where does that leave UAE government deployers?

## What was found

- **Most testing text is not binding.** Of {{n_test_head}} test provisions that are not marked unverified, {{head_mc}} ({{head_mc_pct}}) are mandatory or conditional, {{head_vg}} ({{head_vg_pct}}) are voluntary or guidance and {{head_am}} ({{head_am_pct}}) are ambiguous. {{sensitivity_text}}
- **Binding rules usually say that testing must happen, not how.** The EU Act, OMB M-25-21 and the Abu Dhabi DoH Standard require testing against metrics or benchmarks that the regulated party defines or that are not named (`EU-AI-Act-018`, `US-OMB-003`, `UAE-AbuDhabi-DoH-003`).
- **Independent testing is binding only in narrow places.** Dubai health (`UAE-Dubai-025`, `UAE-Dubai-026`) and DIFC high risk processing (`UAE-DIFC-ADGM-004`, `UAE-DIFC-ADGM-018`).
- **Red teaming is not binding in any verified row** ({{n_RED_binding}} of {{n_RED}}).
- **For the UAE,** binding testing text found is sector or zone specific: Abu Dhabi health, Dubai health, DIFC, and Dubai government security controls that are not AI specific. Federal documents retrieved give guidance in "should" language (`UAE-Federal-009`, `UAE-Federal-018`). The federal data protection law excludes government entities (`UAE-Federal-034`).

## What this does not mean

These are gaps in the documents retrieved. They are not statements of what the UAE requires. Public sources were searched in English and Arabic ({{n_uae_logs}} searches and fetches logged); non public instruments may exist.

## How reliable is it

Phase 2 re checked {{ver_all_n}} rows with the standard fetch tool only: {{ver_all_err}} errors among {{ver_all_verifiable}} verifiable rows ({{ver_all_rate}}%, interval {{ver_all_lo}}% to {{ver_all_hi}}%). {{n_unreliable_rows}} rows are excluded: they could not be verified (source blocked or passage not located) or rest on a summary or secondary report only. Phase 1 verdicts that depended on a user agent workaround were re verified.

## Items to confirm

{{brief_time}}

## The checklist and the tool

A proposed checklist of {{n_checklist_items}} items is in `data/checklist.yaml`. The command line tool `python -m ikhtibar.cli` takes answers about a system and returns, for each item, APPLIES, DOES_NOT_APPLY or UNKNOWN with source traces. Anything the answers do not settle is UNKNOWN. A hypothetical example based on the synthetic Madoun prototype is in `examples/MADOUN_EXAMPLE.md`; it is not deployed and no authority uses or endorses it.

## Before relying on any of this

Have a qualified lawyer review it. Download the blocked documents listed in `docs/DOWNLOAD_LIST.md`. Check the items above.
