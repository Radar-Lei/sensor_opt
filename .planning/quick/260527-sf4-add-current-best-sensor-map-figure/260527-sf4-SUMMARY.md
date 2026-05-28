# Quick Task 260527-sf4 Summary

## Outcome

Added a new current-best low-budget sensor map figure:
`paper/figures/fig_trace_biopt_sensor_maps.pdf` with backing summary CSV
`current_best_trace_biopt_evidence/trace_biopt_sensor_map_summary.csv`.
The figure shows the three 10\% current-best regimes as actual network-facing
layout maps instead of only graph-space fingerprints: PeMS7\_228 uses released
station coordinates, Seattle uses released cabinet coordinates, and PeMS7\_1026
uses a deterministic distance-derived spectral embedding because public station
coordinates are not bundled with the benchmark artifact.

Section 6 now uses this figure to give a more reviewer-facing transport reading
of the low-budget wins: the promoted TRACE-BiOpt layouts remain visibly
distributed across recoverability-critical corridors rather than collapsing onto
one local detector stack, while the strongest baseline panels still show
different layout logic. The fresh claim audit also now verifies the figure
inclusion, six summary rows, coordinate modes, baseline labels, and evidence
source routing.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_sensor_map_figure.py scripts/audit_trace_biopt_claims.py`
- `python scripts/generate_trace_biopt_sensor_map_figure.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The current-best paper chain stayed fully green. `paper-claim-audit` expanded
to 714 checks, `paper/main.pdf` rebuilt to 28 pages, and submission verifier
artifacts remained `OK / PASS / stale=false` while the in-flight
`PeMS7_228 20/30` Stage16 rerun kept progressing in the background.
