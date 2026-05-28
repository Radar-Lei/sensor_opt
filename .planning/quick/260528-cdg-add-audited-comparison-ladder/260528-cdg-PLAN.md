# Quick Plan — 260528-cdg

## Goal

Add a Section 5 audited comparison-ladder table that compresses the full current-best empirical contract into one reviewer-facing main-text artifact: registry scope, row-wise strongest challenger wins, all-baseline corrected screening, family-level near misses, challenger diversity, and explicit non-claim boundaries.

## Scope

- Add a new generator for the comparison-ladder CSV and TeX table.
- Insert the ladder table into `paper/sections/5_experiments.tex`.
- Wire the generator into the refresh chain.
- Extend the machine claim audit so the ladder rows, numbers, and prose are required.
- Revalidate the full paper chain and confirm `paper/main.log` stays clean.

## Verification

- `python scripts/generate_trace_biopt_comparison_ladder_table.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`
- `rg -n -e 'Underfull' -e 'Overfull' -e 'Extra alignment' -e 'Misplaced \\\\noalign' -e 'undefined' paper/main.log`
