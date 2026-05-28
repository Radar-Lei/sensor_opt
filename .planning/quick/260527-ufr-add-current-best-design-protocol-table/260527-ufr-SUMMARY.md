# Quick Task 260527-ufr Summary

## Outcome

Added a generated reviewer-facing design/deployment protocol table:
`paper/tables/table_trace_biopt_design_protocol.tex` with backing CSV
`current_best_trace_biopt_evidence/trace_biopt_design_protocol.csv`.

The new table compresses the current-best evidence chain into five explicit
transport-design rules: judge every regime against the row-wise strongest
audited comparator, recalibrate upper-level risk when validation support is
thin, scale one-exchange search budgets with network size when the cap binds,
retain certificate-weighted objectives on stable rows where zero-weight strong
search still loses, and treat the Stage14 perturbation frontier as bounded
deployment screening rather than as TRACE-BiOpt dominance evidence.

This lifts the paper's closing argument from prose-only discussion into a
machine-audited protocol artifact. Section 7 now ends with a table that a TR-B
reviewer can read as an explicit deployment checklist rather than inferring the
rules from scattered mechanism, weight-sensitivity, and robustness paragraphs.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_design_protocol_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/generate_trace_biopt_design_protocol_table.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The current-best paper chain stayed fully green. `paper-claim-audit` expanded
to 839 checks, `paper/main.pdf` rebuilt cleanly at 32 pages, and submission
verifier artifacts remained `OK / PASS / stale=false`. The in-flight
`PeMS7_228 20/30` Stage16 calibrated fullsearch remained at 4/10 completed
seeds, with `seed_29` still running in `trace_biopt_exchange_step` iteration 9.
