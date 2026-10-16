# Codebook: normative force of non-binding testing provisions (phase 3)

Purpose: the research question separates testing that is REQUIRED, RECOMMENDED or merely DESCRIBED. Binding status (mandatory, conditional) already captures "required". This codebook splits the remaining test rows (binding_status voluntary, guidance or ambiguous) by the force of the text itself. It is an interpretive coding of the row paraphrase, not a legal reading.

Code each row with exactly one value in `normative_force`:

- **OBLIGATION_WORDING**: the text states the test as something that must or shall be done (for example "must", "shall", "is required", a declarative duty), even though the document as a whole is not binding or its binding force is unclear.
- **RECOMMENDS**: the text advises or encourages the test ("should", "is recommended", "consider", "may wish to", "best practice is", a suggested action, a voluntary standard's requirement that applies only if the organisation adopts the standard).
- **DESCRIBES**: the text reports or explains a testing practice, method, case study, finding or capability without advising anyone to do it (for example an institute describing what it evaluates, a case study, a definition, a catalogue of methods, a statement of what a tool can do).

Rules:
1. Code from the row's `requirement_paraphrase` (and `framework`, `clause_or_page` for context). Do not open sources.
2. If two values seem to fit, pick the stronger force present for the test activity itself (OBLIGATION_WORDING > RECOMMENDS > DESCRIBES), and record the doubt in `note`.
3. A voluntary standard's "shall" (for example an ISO requirement or a code of practice commitment for signatories) is RECOMMENDS unless the paraphrase says adoption itself is required.
4. Write `confidence` as high, medium or low.

Output: CSV with columns `row_id,normative_force,confidence,note`, one line per input row, written with Python's csv module.
