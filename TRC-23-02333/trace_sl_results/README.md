# TRACE-SL result stages

This directory contains checked-in TRACE-SL reproducibility outputs for PeMS7_228 and curated external/supporting TRACE-SL evidence. Local sanity runs and new external-validation outputs may also appear here, but only curated result stages are intended to be committed.

## Stage inventory

| Stage | Directory | Claim status | Purpose |
|---|---|---|---|
| 6 | `pems7_228_stage6_multisplit_cvar/` | historical/supporting | Multi-split baseline with scenario/CVaR certificate diagnostics. |
| 7 | `pems7_228_stage7_rcss/` | historical/supporting | Initial Robust Certified Sensor Search candidate scoring. |
| 8 | `pems7_228_stage8_rcss_confirmatory/` | historical/supporting | Confirmatory split seeds showing the initial candidate pool was not sufficient. |
| 9 | `pems7_228_stage9_rcss_quality/` | historical/supporting | Adds quality-coverage OR-guided candidates; RCSS beats validation-selected random on mean across budgets. |
| 10 | `pems7_228_stage10_validation_swap/` | historical/supporting | Adds validation-aware swap refinement; widens the advantage, especially at 30% budget. |
| 11 | `pems7_228_stage11_auto_weight/` | historical/supporting | Replaces fixed RCSS weights with inner-validation weight selection plus validation-aware swap on the original five held-out split seeds. |
| 11-10split | `pems7_228_stage11_auto_weight_10split/` | core in-domain evidence | Aggregates Stage 11 seeds 25--34 for stronger statistics. |
| 12 | `pems7_228_stage12_baseline_portfolio/` | core in-domain baseline-portfolio evidence | Adds Phase 3 reviewer-facing portfolio baselines to ten held-out PeMS7_228 splits. |
| External | `pems7_1026_stage11_auto_weight/` | lower-power external evidence | Runs the Stage 11 pipeline on five held-out PeMS7_1026 splits; use uncertainty/effect-size language until a ten-split extension is generated. |
| Supporting | `seattle_stage11_auto_weight_light/` | supporting/conditional evidence | Runs the Stage 11 pipeline on five held-out Seattle splits with light candidate defaults; do not treat as a core claim unless a stronger synchronized bundle is generated and reviewed. |

## Key aggregate files

- `SUMMARY.md`: human-readable aggregate table.
- `combined_metrics.csv`: all seed-level evaluation rows.
- `gls_map_layout_summary.csv`: GLS/MAP mean MAE by budget and layout type.
- `gls_map_delta_summary.csv`: RCSS deltas against selected baselines.
- `gls_map_paired_delta_tests.csv`: paired tests for GLS/MAP layout comparisons.
- `gls_map_win_counts.csv`: per-budget winner counts.
- `combined_certificate_correlations.csv`: seed-level certificate/error correlations.
- `certificate_correlation_summary.csv`: aggregate certificate stability table.
- `combined_rcss_candidates.csv`: candidate-level RCSS diagnostics.
- `rcss_selected_sources.csv`: selected candidate source counts.
- `validation_swap_delta_tests.csv`: paired tests for validation-swap RCSS against validation-selected random where present.
- `auto_weight_selection_summary.csv`: selected auto-weight patterns by budget and split where present.

## Reading the results

Use `validation_swap_selected` as the current main method label. Use `pems7_228_stage12_baseline_portfolio/` and `pems7_228_stage11_auto_weight_10split/` for the main in-domain evidence, preserving the documented 10% multistart caveat. Use `pems7_1026_stage11_auto_weight/` only as lower-power external evidence unless regenerated with a ten-split Stage 12 extension. Use `seattle_stage11_auto_weight_light/` only as supporting/conditional evidence; it is synchronized with scripts and summaries, but it is not part of the core claim set.

See `.planning/phases/04-core-experiment-evidence/04-DATASET-CLAIM-STATUS.md` for the PeMS7_1026 and Seattle claim-status decision record.
