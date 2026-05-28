# Quick Task 260527-w6v Summary

## Outcome

Added a reviewer-facing current-best generalization-burden table:
`paper/tables/table_trace_biopt_generalization_burden.tex` with backing CSV
`current_best_trace_biopt_evidence/trace_biopt_generalization_burden.csv`.

The new table lifts Theorem T3 out of pure asymptotic prose and binds it to the
actual nine current-best rows under the same two-day validation window
(`n_v=576`). It now makes the combinatorial validation burden visible by row:

- `PeMS7_1026 30%` is the heaviest current row, with
  `B^{-1}\Delta_unif = 0.770`.
- `PeMS7_228 10%` is the lightest current row, with
  `B^{-1}\Delta_unif = 0.263`.
- The Seattle rows sit between the two PeMS extremes.

This gives the manuscript a cleaner theorem-to-evidence bridge. The paper can
now say something stricter than “large networks seem harder”: under the same
validation window, the all-layout validation discrimination burden grows
materially with the layout family size, which is consistent with why the
largest-network, higher-budget rows benefit most from calibrated reruns and
stronger exchange search. The wording remains bounded: this is a validation-
burden diagnostic, not a standalone empirical dominance claim.

The audit layer was extended at the same time. `scripts/audit_trace_biopt_claims.py`
now checks the table inclusion, the nine-row backing CSV, the common
`n_v=576` / `delta=0.05` settings, the row-specific burden factors, the
lightest/heaviest rows, and the surrounding reviewer-facing wording in the
theory and mechanism sections.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_generalization_burden_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/generate_trace_biopt_generalization_burden_table.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The refreshed current-best paper chain stayed fully green. `paper-claim-audit`
expanded to 983 checks, `proof-checker`, `citation-audit`, and
`kill-argument` all remained `PASS`, the submission verifier stayed
`OK / PASS / stale=false` on all four audits, and `paper/main.pdf` rebuilt
cleanly at 37 pages. The in-flight `PeMS7_228 20/30` Stage16 calibrated sweep
remained at 6/10 completed seeds while `seed_31` advanced to the 30% exchange
stage, iteration 9.
