# Quick Task 260527-u5w Summary

## Outcome

Added a generated current-best objective-mix figure:
`paper/figures/fig_trace_biopt_objective_mix.pdf` with backing CSV
`current_best_trace_biopt_evidence/trace_biopt_objective_mix_summary.csv`.

The figure makes the TRACE-BiOpt objective composition reviewer-visible rather
than leaving it implicit inside per-seed history JSON files. The promoted
Stage16 rows, which use the lighter `(\beta,\gamma,\eta)=(0.5,0.01,0)` family,
remain reconstruction-dominated: their final objectives draw about 81--87\% of
their weighted mass from hidden Huber reconstruction loss, with posterior trace
contributing about 13--19\%. The stable Stage15 Seattle rows and PeMS7\_228
20/30\% rows look different. There the posterior term carries about 59--61\%
of the final objective while reconstruction accounts for about 38--41\%.

This gives the Seattle certificate-removal probe a tighter interpretation. The
stable rows are not just search-deep variants of the same mechanism; they are
posterior-driven design regimes, so removing certificate terms changes the
actual optimization target rather than only simplifying notation.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_objective_mix_figure.py scripts/audit_trace_biopt_claims.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The current-best paper chain stayed fully green. `paper-claim-audit` expanded
to 773 checks, `paper/main.pdf` rebuilt to 30 pages, submission verifier
artifacts remained `OK / PASS / stale=false`, `stage17_certificate_weight_probe/`
contained no residual files, and the in-flight `PeMS7_228 20/30` Stage16 sweep
remained at 4/10 completed seeds while `seed_29` continued in exchange.
