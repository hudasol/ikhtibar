# Codebook for blind coders (phase 4)

You are an independent coder. You see only a framework name, a clause locator and a short paraphrase of a provision about testing an AI system. Code two fields. Do not open any other file in the repository. Do not search the web. Do not try to find the original coding.

## Field 1: binding_status
- mandatory: legally binding on the stated actor, with the testing or assessment duty in operative text.
- conditional: binding only if a trigger applies (risk classification, impact level, compute threshold, sector, scope, commercial use).
- voluntary: a formal scheme or standard that an organisation may adopt; testing steps exist but adoption is optional (including certifiable management system standards).
- guidance: a recommendation that is not binding, a framework, or a description of practice.
- ambiguous: the paraphrase or framework gives conflicting signals about force, or force cannot be settled from what you see. Use sparingly, and say why in the note.

Rules: operative text outranks recitals. "Should" in non binding guidance is guidance. A policy binding only on government bodies is mandatory (or conditional) for those bodies. Use the framework name: a statute or regulation is binding in a way a guidance document or standard is not. If the framework name and the paraphrase together do not settle it, use ambiguous.

## Field 2: primary_test_type (choose exactly one code)
- PERF: performance and validity evaluation (does the system do its task, how accurately, on what data, is the test valid).
- ROB: robustness, reliability and fault testing (perturbed inputs, outliers, faults, repeated runs, fail safe).
- FAIR: fairness, bias and representativeness testing.
- SEC: security and adversarial resilience testing (security assessment, code review, vulnerability scanning, penetration testing, AI specific attacks).
- RED: red teaming and dangerous capability evaluation (adversarial probing for misuse, dangerous capabilities, systemic risk model evaluation).
- CSAFE: content safety evaluation (harmful output rates, refusal and over refusal against question banks).
- PRIV: privacy and data protection assessment or testing (leakage, re identification, data protection impact assessment).
- TRANS: transparency, explainability, labelling and reproducibility.
- OVER: human oversight and operational control validation (testing that override, review and escalation work).
- RISK: risk, impact and compliance assessment (structured assessment of risks, impacts on rights or groups, legal compliance).
- DATA: data and training corpus quality validation.
- CONF: conformity assessment, independent review, audit, certification, or filing with a regulator.
- REAL: real world, sandbox and pilot testing.
- MON: post deployment monitoring and re assessment (outcome monitoring, incident handling, re testing triggers).
- GATE: acceptance criteria and release decision (pre set thresholds, go or no go, approval authority by risk level).

Boundary rules: misuse probing is RED; harmful output or refusal rates against fixed banks are CSAFE; ordinary accuracy is PERF. Impact assessments are RISK. Documentation of validation results takes the code of the test it supports. Assessment of accreditation of third party assurers is CONF.

## Output
A CSV written with Python's csv module with columns: row_id, binding_status, primary_test_type, confidence (high, medium or low), note (one short line, required when confidence is not high or the status is ambiguous). One output row per input row, same row_id.
