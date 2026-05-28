# Quick Task 260527-x6r Summary

## Outcome

Added a reviewer-facing current-best posterior-risk posture table:
`paper/tables/table_trace_biopt_posterior_risk_posture.tex` with backing CSV
`current_best_trace_biopt_evidence/trace_biopt_posterior_risk_posture.csv`.

The new table lifts Theorem T2 out of purely analytical scope and binds it to
matched-route current-best probes instead of treating posterior trace as a
universal MAE ranking device. It now makes the bounded posterior-risk reading
visible in controlled comparisons:

- `Seattle 20%` and `Seattle 30%` current certified routes both beat matched
  zero-weight probes on posterior trace and held-out MAE;
- `PeMS7_228 10%` improved only after moving from the heavier Stage15
  certificate mix to the promoted lighter train+validation calibrated route;
- the wording is explicit that this is a theorem-to-evidence bridge over
  matched route probes, not a new aggregate dominance theorem under arbitrary
  non-Gaussian traffic data.

This gives the manuscript a cleaner story for why the posterior-risk terms stay
in the objective family even though the paper's main claim remains empirical
dominance against pre-registered non-BiOpt baselines. The paper can now say
something stricter than “certificate weights sometimes help”: in the audited
matched probes, lower posterior trace and lower held-out MAE move together, but
only within the bounded route families that were actually tested.

The audit layer was extended at the same time. `scripts/audit_trace_biopt_claims.py`
now checks the new table inclusion, the four-row backing CSV, the row-specific
trace and held-out deltas, the matched-probe scope wording, and the surrounding
reviewer-facing text in Section 6.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_posterior_risk_posture_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/generate_trace_biopt_posterior_risk_posture_table.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The refreshed current-best paper chain stayed fully green. `paper-claim-audit`
expanded to 1053 checks, `proof-checker`, `citation-audit`, and
`kill-argument` all remained `PASS`, the submission verifier stayed
`OK / PASS / stale=false` on all four audits, and `paper/main.pdf` rebuilt
cleanly at 38 pages. During the refresh, the in-flight `PeMS7_228 20/30`
Stage16 calibrated sweep remained at 7/10 completed seeds while `seed_32`
advanced to the 30% forward stage, iteration 31.
