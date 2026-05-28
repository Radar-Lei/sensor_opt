# Quick Task 260528-2on Summary

## Outcome

This round closed a real remaining rigor gap in the discussion section.

The manuscript previously still described `exact mixed-integer benchmarks on
smaller subnetworks` as future work only. That left the solver-scope caveat
correct but under-supported. The fix here was not to overclaim global
optimality. The fix was to add one bounded exact-evidence lane that is honest
about scope and strong enough to be reviewer-visible.

I added:

- `scripts/generate_trace_biopt_exact_subnetwork_table.py`
- `paper/tables/table_trace_biopt_exact_subnetwork.tex`
- `TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/trace_biopt_exact_subnetwork_summary.csv`
- `TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/trace_biopt_exact_subnetwork_detail.csv`

The benchmark uses three deterministic anchor-centered 16-node induced
subnetworks per dataset, reuses the row-wise current-best TRACE-BiOpt route
parameters for `10/20/30%` budgets, and exhaustively enumerates every feasible
`k`-subset (`120 / 560 / 4368` layouts per anchor). The bounded result is
strong:

- `27/27` exact hits
- zero objective gap
- zero validation-MAE gap

That is now paper-visible in the discussion section as a solver-scope
clarification. It narrows the exactness caveat on small connected subnetworks
without pretending to solve the full-network global-optimality limitation.
The wording also stays explicit that this does **not** promote `Seattle 10%`
from its fail-closed Stage15 main-evidence status.

I also corrected a stale compute-posture paragraph and made the audit logic
less brittle by tying the solver-scale / compute checks to the generated CSV
and table text instead of frozen historical constants.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_exact_subnetwork_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/generate_trace_biopt_exact_subnetwork_table.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The full current-best paper chain is green again after the new exact benchmark:

- `paper-claim-audit`: `PASS` at `1326` checks
- `proof-checker`: `PASS`
- `citation-audit`: `PASS`
- `kill-argument`: `PASS`
- submission verifier: all four audits `OK / PASS / stale=false`
- `paper/main.pdf`: `44` pages

The manuscript is now stronger on one specific TR-B axis:

- the dominance chain is still the same audited `8/9` Stage16-promoted
  current-best mix;
- the discussion now has a bounded exact-subnetwork benchmark instead of
  leaving exactness entirely as future work;
- the non-claim boundary is still explicit about full-network global
  optimality remaining open.
