# Codebook for blind coders: how specific is the testing provision (phase 5)

You are an independent coder. You see only a framework name, a clause locator and a short paraphrase of a provision that concerns testing an AI system. You do not see whether the provision is binding. Do not open any other file in the repository. Do not search the web. Do not try to find any other coding of these rows.

Code one field, `specificity`, with exactly one of these values, using the highest level that the paraphrase clearly supports:

- S1 process only: the provision says that some testing, evaluation, assessment, review or monitoring takes place, should take place, or must be documented, but does not say what property is examined or how.
- S2 property named: the provision names the property or risk to be examined (for example accuracy, robustness, bias, security, privacy, oversight, harmful output), or the kind of test (for example red teaming, penetration test, pilot), but gives no method, metric, procedure, sample or criterion.
- S3 method or metric named: the provision names a method, metric, procedure, test condition, data requirement, required evaluator type or independence, or required content of the test report, beyond naming the property. It may still leave values for the provider to choose.
- S4 criterion set: the provision sets a pass or fail criterion, a numeric threshold, a fixed frequency or deadline for the test, or a named external test that must be passed.

Rules:
- Judge what the provision itself requires or describes, not what the wider document does.
- A list of many suggested actions takes the level of its most specific item that is stated in the paraphrase.
- A requirement to document test results at no stated level of detail is S1.
- A requirement that a third party performs the test is S3 only when the paraphrase states the independence or qualification of the evaluator as part of the provision.
- If the paraphrase is only a scope, date, penalty or definition and does not describe a test, use S1 and say so in the note.

Also give `confidence` (high, medium, low) and a one line `note`, required when confidence is not high.

## Output
A CSV written with Python's csv module with columns: row_id, specificity, confidence, note. One output row per input row, same row_id, same order.
