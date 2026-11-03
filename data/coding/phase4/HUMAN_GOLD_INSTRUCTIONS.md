# Human gold labelling: instructions (about one hour)

Purpose: give the table one coding that is not made by a language model, so that agreement between a person and the table can be measured. Nothing else in the repository depends on your doing this now.

1. Open `human_gold_template.csv` (100 rows). Do not open `data/evidence_table.csv` while you label, and do not look at the other coders' files in this folder. The rows were drawn at random with a recorded seed, and the original codes are hidden on purpose.
2. For each row read the framework, the locator and the paraphrase. Fill the three columns that begin with YOUR_.
   - `YOUR_binding_status`: one of mandatory, conditional, voluntary, guidance, ambiguous. Definitions are in `CODEBOOK.md` in this folder and in `docs/PROTOCOL.md`. Use ambiguous when the paraphrase alone does not settle it, and say why in the note.
   - `YOUR_primary_test_type`: one of the test type codes listed in `CODEBOOK.md`.
   - `YOUR_note`: one line, required for ambiguous rows.
3. Save the file as `human_gold.csv` in this folder (same columns, UTF 8). Do not edit the template.
4. Run `python -m ikhtibar.coding_agreement` after the file exists. Report the new agreement beside the model coders, with your own name as the coder, and keep the model coders' numbers in the paper.

If you have time left, label the rows in the same way a second time a week later; the difference between your two passes is your own reliability.
