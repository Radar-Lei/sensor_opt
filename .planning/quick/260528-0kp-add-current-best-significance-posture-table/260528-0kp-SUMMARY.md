# Quick Summary — 260528-0kp

## What changed

- Added `scripts/generate_trace_biopt_significance_posture_table.py`, which
  converts the current-best seed-level evidence into a paper-visible
  all-baseline significance posture under one-sided paired tests with Holm
  familywise correction over the full comparison family.
- Added the generated artifacts:
  - `paper/tables/table_trace_biopt_significance_posture.tex`
  - `TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/trace_biopt_significance_posture_summary.csv`
  - `TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/trace_biopt_significance_posture_detail.csv`
- Updated `paper/sections/5_experiments.tex` with a new
  `All-baseline significance posture` subsection so the manuscript now says,
  in main text, that no pre-registered baseline remains statistically tied or
  better after multiplicity correction.
- Wired the new generator into
  `scripts/refresh_current_best_trace_biopt_paper_chain.sh`.
- Extended `scripts/audit_trace_biopt_claims.py` so the manuscript now
  machine-checks:
  - the presence of the new experiments subsection,
  - the 9-row plus aggregate significance summary,
  - the full 189 row-baseline comparisons,
  - the `189/189` Holm-corrected significant wins,
  - the absence of statistically tied or significantly better challengers,
  - the hardest challenger facts for `Seattle 10%`.
- Tightened the significance table layout so the generated LaTeX table no
  longer produces alignment or overfull-box noise in `paper/main.log`.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_significance_posture_table.py scripts/audit_trace_biopt_claims.py` — PASS
- `python scripts/generate_trace_biopt_significance_posture_table.py` — PASS
- `python scripts/audit_trace_biopt_claims.py` — PASS
  - `paper-claim-audit`: PASS (`1475` checks)
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh` — PASS
  - `paper-claim-audit`: PASS (`1475` checks)
  - `proof-checker`: PASS
  - `citation-audit`: PASS
  - `kill-argument`: PASS
  - submission verifier: all `OK / PASS / stale=false`
  - `paper/main.pdf`: rebuilt at `48` pages
- `rg -n "Extra alignment|Overfull|Underfull|table_trace_biopt_significance_posture|Warning" paper/main.log`
  - confirms the new significance table does not leave alignment or box warnings

## Result

The manuscript now supports a stronger reviewer-facing version of
`beat all baselines`: under Holm-corrected one-sided paired tests across all
`189` current-best row-baseline comparisons, every pre-registered non-BiOpt
baseline remains significantly worse than TRACE-BiOpt, with no statistically
tied or significantly better challenger remaining.
