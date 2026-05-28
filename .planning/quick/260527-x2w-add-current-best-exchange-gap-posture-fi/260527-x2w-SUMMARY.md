# Quick Task 260527-x2w Summary

## Outcome

Added a reviewer-facing current-best exchange-gap figure:
`paper/figures/fig_trace_biopt_exchange_gap_curves.pdf` with backing CSVs
`current_best_trace_biopt_evidence/trace_biopt_exchange_gap_summary.csv` and
`trace_biopt_exchange_gap_curves.csv`.

The new figure isolates the accepted exchange phase instead of folding it into
the full solver path. It now makes three optimization facts paper-visible:

- the promoted `PeMS7_1026 20/30%` rows remain the clearest binding-search
  regimes: at the halfway point of accepted exchange progress, they still
  retain about `0.322` and `0.437` of their eventual exchange-phase
  improvement, with `20.0` and `8.0` accepted swaps on average;
- the promoted `PeMS7_228 10%` rerun is shorter and cleaner, dropping to a
  halfway residual exchange gap of `0.261` with `7.1` accepted swaps;
- the retained `PeMS7_228 20/30%` rows and `Seattle 10/30%` rows already show
  the opposite stability signature: `1--4` of the ten split-specific runs
  accept no exchange at all beyond the forward path, so the exchange phase is
  often optional rather than binding there.

This improves the TR-B-facing solver story. The manuscript can now show not
just that accepted objective histories are monotone, but also how the exchange
tail behaves by regime: large-network rows stay exchange-tail heavy, while
stable rows often terminate close enough to local stationarity that no swap is
accepted at all.

The audit layer was extended at the same time. `scripts/audit_trace_biopt_claims.py`
now checks the new figure inclusion, the summary/detail CSVs, the midpoint
residual-gap values, the mean accepted exchange counts, the zero-exchange row
pattern, and the reviewer-facing wording in Section 6.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_exchange_gap_figure.py scripts/audit_trace_biopt_claims.py`
- `python scripts/generate_trace_biopt_exchange_gap_figure.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The refreshed current-best paper chain stayed fully green. `paper-claim-audit`
expanded to 1152 checks, `proof-checker`, `citation-audit`, and
`kill-argument` all remained `PASS`, the submission verifier stayed
`OK / PASS / stale=false` on all four audits, and `paper/main.pdf` rebuilt
cleanly at 41 pages. During the refresh, the in-flight `PeMS7_228 20/30`
Stage16 calibrated sweep remained at `8/10` completed seeds per budget and the
live checkpoint rolled to `seed_33`, `30%` budget, `trace_biopt_exchange_step`
iteration `4`.
