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
| 13 | `pems7_228_stage13_candidate_sensitivity/` | core tractability/sensitivity evidence | Adds candidate-count sensitivity, selected-source diagnostics, and measured runtime evidence for PeMS7_228. |
| 14 | `pems7_228_stage14_robustness/` | core stress-test robustness evidence | Adds PeMS7_228 held-out stress-test evidence for baseline, sensor failure, observation noise, random/block missingness, cost proxy, and chronological split conditions; this is usefulness-under-perturbation evidence, not a universal robustness guarantee. |
| 14 | `pems7_228_stage14_candidate_sensitivity/` | core candidate-count/runtime sensitivity evidence | Adds PeMS7_228 50/100/200/500 candidate-count performance and measured runtime evidence via `stage14_timing.csv`; `candidate_sensitivity_caveat.json` is the only allowed ROBUST-06 limited-tractability exception if present. |
| External | `pems7_1026_stage11_auto_weight/` | lower-power external supporting/optional evidence | Runs the Stage 11 pipeline on five held-out PeMS7_1026 splits; use uncertainty/effect-size language until a ten-split extension is generated. |
| External Stage12 | `pems7_1026_stage12_baseline_portfolio/` | blocked external Stage12 evidence | Stage12 launcher/status path for PeMS7_1026; Phase 8 gate keeps EVID-03 incomplete until required ten-split aggregate artifacts exist and are tracked. |
| Supporting | `seattle_stage11_auto_weight_light/` | supporting/conditional evidence | Runs the Stage 11 pipeline on five held-out Seattle splits with light candidate defaults; do not treat as a core claim unless a stronger synchronized bundle is generated and reviewed. |
| External Stage12 | `seattle_stage12_baseline_portfolio/` | blocked external Stage12 evidence | Stage12 Seattle status path with `stage12_status.json`; Phase 8 gate keeps Seattle out of core claims until complete tracked ten-split evidence exists. |

## Key reproducibility handoff artifacts

- `reproducibility_manifest.json`: machine-readable Phase 6 provenance inventory for curated Stage 12/13/14 results, launcher defaults, package metadata, git provenance, and raw-data hygiene.
- `REPRODUCIBILITY_MANIFEST.md`: human-readable rendering of the manifest for reproducibility review.
- `paper_sources/`: generated manuscript-facing CSV/Markdown table sources with `source_stage`, `source_dir`, and `source_csv` provenance on CSV rows.

Paper-visible numbers should be sourced only from curated aggregate result directories listed below or from generated files under `paper_sources/`. Local raw traffic datasets are launcher inputs, not paper-visible evidence artifacts.

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
- `candidate_sensitivity_summary.csv`: candidate-source diagnostic stability by budget and, for Stage 13/14, candidate count.
- `runtime_candidate_sensitivity.csv`: measured runtime summary by candidate count where present.
- `stage14_timing.csv`: Stage 14 measured runtime/status rows by candidate_count and split seed.
- `candidate_sensitivity_caveat.json`: machine-readable ROBUST-06 limited-tractability exception, only valid for Stage 14 candidate sensitivity when a required count was attempted but could not complete locally.
- `validation_swap_delta_tests.csv`: paired tests for validation-swap RCSS against validation-selected random where present.
- `auto_weight_selection_summary.csv`: selected auto-weight patterns by budget and split where present.

## Reading the results

Use `validation_swap_selected` as the current main method label. Use `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/` and `pems7_228_stage11_auto_weight_10split/` for the main in-domain evidence, preserving the documented 10% multistart caveat. Use `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/` as the core PeMS7_228 robustness/generalization stress-test path with `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_paired_delta_tests.csv`, and `SUMMARY.md`; interpret it as evaluated perturbation evidence, not a universal deployment proof. Use `TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/` for 50/100/200/500 candidate-count performance/runtime evidence with `combined_metrics.csv`, `candidate_sensitivity_summary.csv`, `runtime_candidate_sensitivity.csv`, `stage14_timing.csv`, and `SUMMARY.md`; if present, `candidate_sensitivity_caveat.json` is the only allowed ROBUST-06 limited-tractability exception. Use `TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/` as predecessor candidate-count sensitivity and measured runtime/tractability evidence, not as a broad scalability guarantee. Use `pems7_1026_stage11_auto_weight/` only as lower-power external supporting/optional evidence unless regenerated with a complete tracked ten-split Stage 12 extension. Use `paper_sources/external_evidence_gate.json` as the machine-checkable Phase 8 gate: current PeMS7_1026 Stage12 evidence is blocked by missing required aggregate artifacts, and current Seattle Stage12 evidence is blocked by `seattle_stage12_baseline_portfolio/stage12_status.json`. Use `seattle_stage11_auto_weight_light/` only as supporting/conditional evidence; it is synchronized with scripts and summaries, but it is not part of the core claim set.

Stage 14 artifacts are stress-test evidence for usefulness under the specified perturbations and candidate budgets. External robustness remains supporting/optional unless a synchronized stronger bundle is generated and reviewed.

See `.planning/phases/04-core-experiment-evidence/04-DATASET-CLAIM-STATUS.md` for the PeMS7_1026 and Seattle claim-status decision record.
