# TRACE-BiOpt and TRACE-SL result stages

This directory contains checked-in reproducibility outputs for the TRACE-BiOpt bilevel optimization method and the predecessor TRACE-SL/RCSS candidate-pool framework. The current manuscript-facing method is TRACE-BiOpt; TRACE-SL/RCSS stages are preserved as historical baseline and development evidence.

## Current TRACE-BiOpt evidence

### `current_best_trace_biopt_evidence/` — TRACE-BiOpt paper-facing evidence chain

This is the authoritative headline-evidence source for the current manuscript. Aggregate claim status: `supported_submission_ready`.

Key artifacts:
- `trace_biopt_claim_contract.json`: row-level and aggregate wording contract.
- `trace_biopt_best_baseline_delta.csv`: TRACE-BiOpt MAE vs best baseline per dataset-budget.
- `trace_biopt_full_baseline_matrix.csv`: full 9-row x 21-baseline comparison matrix.
- `trace_biopt_current_best_provenance.csv`: row-level source policy (Stage 15 or Stage 16).
- `TRACE_BIOPT_DOMINANCE.md`: Holm-corrected dominance summary (189/189 wins).
- `trace_biopt_exact_subnetwork_summary.csv`: 27/27 exact 16-node subnetwork hits.
- `trace_biopt_significance_posture_summary.csv`: Holm-corrected significance posture.
- `trace_biopt_solver_scale_summary.csv`: solver scale and runtime evidence.
- `trace_biopt_route_ablation_summary.csv`: objective component ablation.
- `trace_biopt_weight_sensitivity.csv`: objective weight sensitivity.
- `trace_biopt_exchange_gap_summary.csv`: exchange convergence evidence.
- `trace_biopt_objective_descent_summary.csv`: objective descent curves.

Paper-visible numbers should be sourced from this directory for the current TRACE-BiOpt manuscript. The refresh pipeline is `scripts/refresh_current_best_trace_biopt_paper_chain.sh`.

### Stage 15 — TRACE-BiOpt main evidence

| Directory | Purpose |
|---|---|
| `stage15_biopt_allbudget_10seed_v2/` | Stage 15 TRACE-BiOpt 10-seed run for all datasets and budgets (primary evidence). |
| `stage15_biopt_allbudget_3seed_v2/` | Stage 15 TRACE-BiOpt 3-seed lightweight run. |
| `stage15_biopt_allbudget_seed25/` | Stage 15 TRACE-BiOpt single-seed run (seed 25). |
| `stage15_biopt_allbudget_seed25_v2/` | Stage 15 TRACE-BiOpt single-seed run v2. |
| `stage15_biopt_pems1026_30_extra/` | Stage 15 PeMS7_1026 30% budget extra evidence. |

Stage 15 is the main TRACE-BiOpt evidence generation stage. Seattle 10% from Stage 15 is intentionally retained in the current-best chain because the Stage 16 calibrated rerun did not satisfy the replacement gate.

### Stage 16 — TRACE-BiOpt calibrated rerun

| Directory | Purpose |
|---|---|
| `stage16_calibrated_trace_probe/` | Stage 16 calibrated trace probe. |
| `stage16_calibrated_trace_sweep/` | Stage 16 calibrated trace sweep. |

8/9 current-best rows are promoted from Stage 16 calibrated reruns (all except Seattle 10%). Stage 16 refined solver parameters produce the strongest TRACE-BiOpt evidence currently available.

## Historical TRACE-SL/RCSS stages (Stages 6--14)

The stages below record the predecessor TRACE-SL/RCSS development path. They are preserved as historical baseline and diagnostic evidence. For current manuscript claims, use the TRACE-BiOpt current-best evidence chain above.

### Stage inventory

| Stage | Directory | Claim status | Purpose |
|---|---|---|---|
| 6 | `pems7_228_stage6_multisplit_cvar/` | historical/supporting | Multi-split baseline with scenario/CVaR certificate diagnostics. |
| 7 | `pems7_228_stage7_rcss/` | historical/supporting | Initial Robust Certified Sensor Search candidate scoring. |
| 8 | `pems7_228_stage8_rcss_confirmatory/` | historical/supporting | Confirmatory split seeds showing the initial candidate pool was not sufficient. |
| 9 | `pems7_228_stage9_rcss_quality/` | historical/supporting | Adds quality-coverage OR-guided candidates; RCSS beats validation-selected random on mean across budgets. |
| 10 | `pems7_228_stage10_validation_swap/` | historical/supporting | Adds validation-aware swap refinement; widens the advantage, especially at 30% budget. |
| 11 | `pems7_228_stage11_auto_weight/` | historical/supporting | Replaces fixed RCSS weights with inner-validation weight selection plus validation-aware swap on the original five held-out split seeds. |
| 11-10split | `pems7_228_stage11_auto_weight_10split/` | historical in-domain evidence | Aggregates Stage 11 seeds 25--34 for stronger statistics. |
| 12 | `pems7_228_stage12_baseline_portfolio/` | historical in-domain baseline-portfolio evidence | Adds Phase 3 reviewer-facing portfolio baselines to ten held-out PeMS7_228 splits. |
| 13 | `pems7_228_stage13_candidate_sensitivity/` | historical tractability/sensitivity evidence | Adds candidate-count sensitivity, selected-source diagnostics, and measured runtime evidence for PeMS7_228. |
| 14 | `pems7_228_stage14_robustness/` | historical stress-test robustness evidence | Adds PeMS7_228 held-out stress-test evidence. |
| 14 | `pems7_228_stage14_candidate_sensitivity/` | historical candidate-count/runtime sensitivity evidence | Adds PeMS7_228 candidate-count performance and measured runtime evidence. |
| External | `pems7_1026_stage11_auto_weight/` | historical external supporting evidence | Runs the Stage 11 pipeline on five held-out PeMS7_1026 splits. |
| External Stage12 | `pems7_1026_stage12_baseline_portfolio/` | historical external Stage12 evidence | Ten-split Stage12 baseline-portfolio evidence for PeMS7_1026. |
| Supporting | `seattle_stage11_auto_weight_light/` | historical supporting evidence | Runs the Stage 11 pipeline on five held-out Seattle splits with light candidate defaults. |
| External Stage12 | `seattle_stage12_baseline_portfolio/` | historical external Stage12 evidence | Ten-split Stage12 Seattle baseline-portfolio evidence. |

## Key reproducibility handoff artifacts

- `reproducibility_manifest.json`: machine-readable Phase 6 provenance inventory for curated Stage 12/13/14 results, launcher defaults, package metadata, git provenance, and raw-data hygiene.
- `REPRODUCIBILITY_MANIFEST.md`: human-readable rendering of the manifest for reproducibility review.
- `paper_sources/`: generated manuscript-facing CSV/Markdown table sources with `source_stage`, `source_dir`, and `source_csv` provenance on CSV rows. These are TRACE-SL/RCSS paper-source artifacts; TRACE-BiOpt paper sources are in `current_best_trace_biopt_evidence/`.

Paper-visible numbers for the current TRACE-BiOpt manuscript should be sourced from `current_best_trace_biopt_evidence/`. Paper-visible numbers for TRACE-SL/RCSS historical claims should be sourced from curated aggregate result directories listed above or from generated files under `paper_sources/`.

## Key aggregate files (historical TRACE-SL/RCSS)

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
- `candidate_sensitivity_summary.csv`: candidate-source diagnostic stability by budget and candidate count.
- `runtime_candidate_sensitivity.csv`: measured runtime summary by candidate count.
- `stage14_timing.csv`: Stage 14 measured runtime/status rows.
- `candidate_sensitivity_caveat.json`: machine-readable ROBUST-06 limited-tractability exception.
- `validation_swap_delta_tests.csv`: paired tests for validation-swap RCSS.
- `auto_weight_selection_summary.csv`: selected auto-weight patterns by budget and split.

## Reading the results

For the current TRACE-BiOpt manuscript, use `current_best_trace_biopt_evidence/` as the authoritative source. The layout label is `trace_biopt`. The method contract is in `TRACE_BIOPT_SPEC.md`.

For historical TRACE-SL/RCSS evidence, use `validation_swap_selected` as the TRACE-SL main method label. Stage 12 baseline-portfolio artifacts under `pems7_228_stage12_baseline_portfolio/`, `pems7_1026_stage12_baseline_portfolio/`, and `seattle_stage12_baseline_portfolio/` provide the strongest historical TRACE-SL evidence.

TRACE-SL/RCSS (`validation_swap_selected`) is also a baseline row within the TRACE-BiOpt comparison class in the current manuscript.

See `.planning/phases/04-core-experiment-evidence/04-DATASET-CLAIM-STATUS.md` for the PeMS7_1026 and Seattle claim-status decision record.
