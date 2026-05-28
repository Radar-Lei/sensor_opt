# Quick Task 260527-rm8 Summary

## Outcome

Added a generated mechanism-alignment figure:
`paper/figures/fig_trace_biopt_calibration_alignment.pdf` with backing CSVs
`current_best_trace_biopt_evidence/trace_biopt_calibration_alignment_points.csv`
and
`current_best_trace_biopt_evidence/trace_biopt_calibration_alignment_summary.csv`.
The figure visualizes two relationships over the 450 GLS/MAP selected-layout
rows from three networks, three budgets, ten seeds, and five layout families:
validation-selected MAE versus held-out MAE, and posterior trace versus
held-out MAE. Section 6 now uses these plots to explain why low-budget rows can
still require calibrated train+validation reruns even when validation alignment
is positive, and why certificate terms stay informative without replacing
direct reconstruction loss.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_calibration_alignment_figure.py scripts/audit_trace_biopt_claims.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The refreshed paper chain stayed fully green. `paper-claim-audit` increased to
663 checks, `paper/main.pdf` rebuilt to 26 pages, and the new mechanism figure
is now part of the audited current-best manuscript path.
