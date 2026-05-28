# Quick Task 260527-xbu Summary

## Outcome

Added a reviewer-facing current-best tail-risk posture table:
`paper/tables/table_trace_biopt_tail_risk_posture.tex` with backing CSV
`current_best_trace_biopt_evidence/trace_biopt_tail_risk_posture.csv`.

The new table turns the TRACE-BiOpt CVaR interpretation into a bounded
current-best mechanism bridge instead of leaving it as prose around objective
weights. It now makes three points explicit:

- on the stable Seattle 20\% and 30\% rows, the winning current route keeps
  only about 1.37--1.40\% CVaR share in the final objective, yet the matched
  zero-weight strong-search probe still loses by 0.032--0.036 MAE;
- on the promoted PeMS7\_228 10\% row, the current route keeps only a 0.26\%
  CVaR share, but both the zero-weight probe and the heavier Stage15
  certificate-weighted route perform worse;
- the reviewer-facing conclusion is therefore bounded and regime-calibrated:
  CVaR is not the dominant mass of the objective, but a small explicit
  tail-risk term can still matter as a tie-breaker or stabilizer inside the
  winning route family.

This strengthens the TR-B-facing methodological story. The paper can now say
something more precise than “there is a CVaR term in the objective”: the
current-best winning routes keep that term small, auditable, and regime
dependent, and the controlled probes show that removing or over-weighting it is
not free.

The audit layer was extended at the same time. `scripts/audit_trace_biopt_claims.py`
now checks the new table inclusion, the three-row backing CSV, the Seattle and
PeMS7\_228 cvar-share values, the matched-probe comparison strings, and the new
bounded wording in Section 6.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_tail_risk_posture_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/generate_trace_biopt_tail_risk_posture_table.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The refreshed current-best paper chain stayed fully green. `paper-claim-audit`
expanded to 1070 checks, `proof-checker`, `citation-audit`, and
`kill-argument` all remained `PASS`, the submission verifier stayed
`OK / PASS / stale=false` on all four audits, and `paper/main.pdf` rebuilt
cleanly at 40 pages after eliminating the temporary overfull warning from the
new table. During the refresh, the in-flight `PeMS7_228 20/30` Stage16
calibrated sweep remained at 7/10 completed seeds while `seed_32` stayed on
the 30\% exchange stage at iteration 5.
