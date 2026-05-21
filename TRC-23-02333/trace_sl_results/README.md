# TRACE-SL result stages

This directory contains checked-in TRACE-SL reproducibility outputs for PeMS7_228. Local sanity runs and new external-validation outputs may also appear here, but only curated result stages are intended to be committed.

## Stage inventory

| Stage | Directory | Purpose |
|---|---|---|
| 6 | `pems7_228_stage6_multisplit_cvar/` | Multi-split baseline with scenario/CVaR certificate diagnostics. |
| 7 | `pems7_228_stage7_rcss/` | Initial Robust Certified Sensor Search candidate scoring. |
| 8 | `pems7_228_stage8_rcss_confirmatory/` | Confirmatory split seeds showing the initial candidate pool was not sufficient. |
| 9 | `pems7_228_stage9_rcss_quality/` | Adds quality-coverage OR-guided candidates; RCSS beats validation-selected random on mean across budgets. |
| 10 | `pems7_228_stage10_validation_swap/` | Adds validation-aware swap refinement; widens the advantage, especially at 30% budget. |
| 11 | `pems7_228_stage11_auto_weight/` | Replaces fixed RCSS weights with inner-validation weight selection plus validation-aware swap on the original five held-out split seeds. |
| 11-10split | `pems7_228_stage11_auto_weight_10split/` | Aggregates Stage 11 seeds 25--34 for stronger statistics. |
| External | `pems7_1026_stage11_auto_weight/` | Runs the Stage 11 pipeline on PeMS7_1026 for external validation. |

## Key Stage 11 files

- `SUMMARY.md`: human-readable aggregate table.
- `combined_metrics.csv`: all seed-level evaluation rows.
- `gls_map_layout_summary.csv`: GLS/MAP mean MAE by budget and layout type.
- `gls_map_delta_summary.csv`: RCSS deltas against selected baselines.
- `gls_map_win_counts.csv`: per-budget winner counts.
- `combined_certificate_correlations.csv`: seed-level certificate/error correlations.
- `certificate_correlation_summary.csv`: aggregate certificate stability table.
- `combined_rcss_candidates.csv`: candidate-level RCSS diagnostics.
- `rcss_selected_sources.csv`: selected candidate source counts.
- `validation_swap_delta_tests.csv`: paired tests for validation-swap RCSS against validation-selected random.
- `auto_weight_selection_summary.csv`: selected auto-weight patterns by budget and split.

## Reading the results

Use `validation_swap_selected` as the current main method. Use the PeMS7_228 10-split directory for the main in-domain table and the PeMS7_1026 directory for external validation; compare against `best_random_by_validation`, `random`, and `top_variance`.
