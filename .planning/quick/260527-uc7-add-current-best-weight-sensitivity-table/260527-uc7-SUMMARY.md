# Quick Task 260527-uc7 Summary

## Outcome

Added a generated current-best weight-sensitivity mechanism table:
`paper/tables/table_trace_biopt_weight_sensitivity.tex` with backing CSV
`current_best_trace_biopt_evidence/trace_biopt_weight_sensitivity.csv`.

The table compresses completed single-seed Seattle and PeMS7\_228 diagnostics
into one reviewer-facing artifact. It shows that the stable Seattle 20\% and
30\% rows prefer the certificate-weighted current route over a matched
zero-weight strong-search probe by 0.036 and 0.032 MAE, respectively. It also
shows that the weak PeMS7\_228 10\% row does not prefer either the original
heavy-cert Stage15 route or the zero-weight strong-search route; the promoted
current-best route is the lighter train+validation calibrated full-search rerun,
which lowers held-out MAE to 3.248 from 3.377 and 3.417 on the same split.

This turns `sensitivity to (\beta,\gamma,\eta)` from an implicit reading of
scattered diagnostics into an audited paper-visible mechanism statement. The
right interpretation is regime sensitivity, not a universal monotonic claim
about certificate weights.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_weight_sensitivity_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The current-best paper chain stayed fully green. `paper-claim-audit` expanded
to 794 checks, `paper/main.pdf` rebuilt cleanly at 31 pages, the new table
compiled without its earlier `tabularx` warning after a final layout pass, and
submission verifier artifacts remained `OK / PASS / stale=false` while
`PeMS7_228 20/30` stayed at 4/10 completed seeds and `seed_29` continued in
exchange.
