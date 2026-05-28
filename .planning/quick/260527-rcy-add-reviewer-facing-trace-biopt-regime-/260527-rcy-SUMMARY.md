# Quick Task 260527-rcy Summary

## Outcome

Added a generated reviewer-facing regime-lessons artifact:
`paper/tables/table_trace_biopt_regime_lessons.tex` with backing CSV
`current_best_trace_biopt_evidence/trace_biopt_regime_lessons.csv`.
The table rewrites the nine current-best dataset-budget rows as transport-design
regimes, identifying the strongest non-BiOpt family, the current evidence lane
(`Stage16 calibrated rerun` or `Stage15 main evidence`), the search signal, and
the row-level lesson. Section 6 now uses this table to explain why some rows
are calibration-sensitive, why PeMS7_1026 30% remains search-budget-sensitive,
and why Seattle/PeMS7_228 mid/high-budget rows behave like stable direct
optimization wins.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_regime_lessons_table.py scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The refreshed paper chain stayed fully green, the paper-claim audit expanded to
595 checks, and the manuscript gained a reviewer-facing explanation layer that
connects row-level dominance evidence to transport design principles.
