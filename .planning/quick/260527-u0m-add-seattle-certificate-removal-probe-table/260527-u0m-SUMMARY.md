# Quick Task 260527-u0m Summary

## Outcome

Added a generated Seattle-only certificate-removal mechanism table:
`paper/tables/table_trace_biopt_certificate_removal_probe.tex` with backing CSV
`current_best_trace_biopt_evidence/trace_biopt_certificate_removal_probe.csv`.

The table promotes an existing completed strong-search diagnostic into the
paper chain. It shows that on the stable Seattle 20\% and 30\% current-best
rows, removing the posterior-trace, scenario-CVaR, and spatial terms and
falling back to a reconstruction-only strong-search route worsens both
validation and held-out GLS/MAP MAE. The held-out penalty is about
0.032--0.036 MAE, so the Seattle gains are not explained by search depth
alone.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_certificate_removal_probe_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The current-best paper chain stayed fully green. `paper-claim-audit` expanded
to 761 checks, `paper/main.pdf` rebuilt cleanly at 29 pages, submission
verifier artifacts remained `OK / PASS / stale=false`, and the Stage16 watcher
stayed active while `PeMS7_228 20/30` remained at 4/10 completed seeds and
continued `seed_29`.
