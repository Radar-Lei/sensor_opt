# Quick Plan: TRACE-BiOpt Claim Contract

## Goal

Generate a row-level TRACE-BiOpt claim contract from Stage15 dominance evidence
so TR-B wording is tied to auditable artifacts rather than informal summaries.

## Tasks

- Read `trace_biopt_best_baseline_delta.csv` and fail closed unless TRACE-BiOpt
  beats the actual best non-BiOpt baseline in every dataset-budget row.
- Attach paired-test and layout-summary provenance to every row.
- Emit CSV, JSON, and Markdown claim-contract artifacts with allowed wording,
  required caveats, and forbidden overclaims.
- Wire the claim-contract generator into the Stage15 launcher after dominance
  generation.
- Add regression tests and update method/theory/GSD records.
