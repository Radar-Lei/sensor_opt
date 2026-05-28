# Quick Task 260527-unh Summary

## Outcome

Added a generated current-best paired-margin figure:
`paper/figures/fig_trace_biopt_paired_margins.pdf` with backing CSVs
`current_best_trace_biopt_evidence/trace_biopt_paired_margin_points.csv` and
`current_best_trace_biopt_evidence/trace_biopt_paired_margin_summary.csv`.

The new artifact opens the nine-row current-best dominance claim at split
level. Instead of only reporting 10/10 wins and paired p-values, the paper now
shows all 90 seed-level TRACE-BiOpt minus strongest-baseline MAE margins in one
figure, with Stage16-promoted rows and retained Stage15 rows distinguished
visually. The experiments section now states the specific split-level reading:
all 90 paired margins remain below zero, the narrowest cluster is
PeMS7\_1026 30\%, and the largest mean paired margin occurs on PeMS7\_228 20\%.

This makes the headline dominance claim more reviewer-facing without adding any
new experiment load. The figure is computed directly from the same
current-best strongest-comparator route already used by the dominance table.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_paired_margin_figure.py scripts/audit_trace_biopt_claims.py`
- `python scripts/generate_trace_biopt_paired_margin_figure.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The refreshed current-best paper chain stayed fully green. `paper-claim-audit`
expanded to 888 checks, `paper/main.pdf` rebuilt cleanly at 33 pages, and the
submission verifier remained `OK / PASS / stale=false` on all four audits.
During the same refresh, the in-flight `PeMS7_228 20/30` Stage16 calibrated
fullsearch advanced from 4/10 to 5/10 completed seeds as `seed_29` finished
and live progress rolled over to `seed_30`.
