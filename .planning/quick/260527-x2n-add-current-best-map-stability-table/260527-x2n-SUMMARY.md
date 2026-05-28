# Quick Task 260527-x2n Summary

## Outcome

Added a reviewer-facing current-best MAP stability posture table:
`paper/tables/table_trace_biopt_map_stability_posture.tex` with backing CSV
`current_best_trace_biopt_evidence/trace_biopt_map_stability_posture.csv`.

The new table lifts Theorem T1 out of purely analytical scope and binds it to
the actual nine current-best rows. It now makes the lower-level inverse-system
conditioning posture visible against the row-wise strongest baseline:

- all four promoted Stage16 rows (`PeMS7_1026 10/20/30` and `PeMS7_228 10%`)
  improve MAE while lowering the GLS/MAP condition number on all ten split-
  specific runs;
- the retained Stage15 rows are more mixed, but even there the current-best
  max condition number stays below about `7.1e3`, so the manuscript can rule
  out a “near-singular inverse problem” story;
- the bounded interpretation is explicit: this is a theorem-to-evidence bridge
  for lower-level stability, not a new dominance claim.

This gives the paper a stronger method-theory-evidence chain. The manuscript
can now say something more concrete than “the lower-level problem is well
posed”: the current-best promoted rows actually strengthen numerical
conditioning relative to the strongest audited baselines, while the rows that
retain slightly higher conditioning remain finite and auditable rather than
numerically pathological.

The audit layer was extended at the same time. `scripts/audit_trace_biopt_claims.py`
now checks the new table inclusion, the nine-row backing CSV, the row-specific
condition ratios and lower-condition win counts, the four promoted lower-
conditioning rows, the global max current-best condition number, and the
reviewer-facing wording in Section 6.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_map_stability_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/generate_trace_biopt_map_stability_table.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The refreshed current-best paper chain stayed fully green. `paper-claim-audit`
expanded to 1023 checks, `proof-checker`, `citation-audit`, and
`kill-argument` all remained `PASS`, the submission verifier stayed
`OK / PASS / stale=false` on all four audits, and `paper/main.pdf` rebuilt
cleanly at 38 pages. During the refresh, the in-flight `PeMS7_228 20/30`
Stage16 calibrated sweep advanced from 6/10 to 7/10 completed seeds and rolled
live progress to `seed_32` at the 20% exchange stage.
