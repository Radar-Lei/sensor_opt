# Quick Task 260527-v3a Summary

## Outcome

Formalized the continuous-relaxation route as a paper-visible proposition
instead of leaving it as an implementation-side note.

The manuscript now includes `Proposition~\\ref{prop:relax-consistency}` in
`paper/sections/4_method_theory.tex`, a matching theory-table row in
`paper/tables/table_theory.tex`, and an appendix proof route that points to
the same proposition. `TRACE_BIOPT_THEORY.md` now records this as
`Proposition T5: Continuous-Relaxation Consistency`, and the former CVaR note
shifts to `Proposition T6`.

The point of the change is methodological clarity rather than a new empirical
claim. The audited paper chain now states explicitly that the capped-simplex
relaxation and deterministic `TopK` rounding only produce a budget-feasible
warm start; the accepted layout is still refined under the same discrete
TRACE-BiOpt objective, so the relaxed route is not a second solver family and
does not broaden the dominance claim scope.

To keep the proof gate aligned with the manuscript, `scripts/audit_trace_biopt_proofs.py`
was updated to accept proposition-level proof blocks in addition to theorem
blocks, instead of assuming a one-to-one theorem/proof count.

## Verification

- `python scripts/audit_trace_biopt_proofs.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The refreshed current-best paper chain stayed fully green. The manuscript
rebuilt cleanly at 35 pages, proof/claim/citation/kill audits all remained
`PASS`, and the submission verifier stayed `OK / PASS / stale=false` on all
four gates. During the same refresh, the in-flight `PeMS7_228 20/30` Stage16
calibrated fullsearch remained at 5/10 completed seeds while `seed_30`
advanced to the 30% exchange stage, iteration 4.
