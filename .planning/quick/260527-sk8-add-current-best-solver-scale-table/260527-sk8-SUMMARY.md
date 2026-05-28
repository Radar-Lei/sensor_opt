# Quick Task 260527-sk8 Summary

## Outcome

Added a generated current-best solver-scale diagnostic:
`paper/tables/table_trace_biopt_solver_scale.tex` with backing CSVs
`current_best_trace_biopt_evidence/trace_biopt_solver_scale_summary.csv` and
`trace_biopt_solver_scale_detail.csv`. The generator reads each current-best
row's per-seed `trace_biopt_history.json`, `config.json`, and progress logs to
report deterministic initializer family, exchange-step depth, searched
one-exchange coverage, stop certificates, and peak resident memory.

Section 6 now uses this table to state the audited computational burden rather
than a stale Stage15 approximation: PeMS7\_228 and Seattle stay below 0.5\,GB,
while the promoted calibrated PeMS7\_1026 rows span roughly 1.4--2.9\,GB.
This turns solver scale into an explicit part of the TRACE-BiOpt method
specification instead of an implicit runtime footnote. The fresh claim audit
now verifies the new table input, 9 summary rows, 90 seed-level rows, source
labels, initializer families, and representative peak-RSS values.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_solver_scale_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The current-best paper chain stayed fully green. `paper-claim-audit` expanded
to 729 checks, `paper/main.pdf` rebuilt to 29 pages, and submission verifier
artifacts remained `OK / PASS / stale=false`. The refresh also picked up new
Stage16 progress: `PeMS7_228 20/30` is now complete on 4/10 seeds per budget,
and the live checkpoint has moved to `seed_29`.
