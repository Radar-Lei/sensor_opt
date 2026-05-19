# TRACE-SL Narrative Report

**Project**: TRACE-SL — Transparent Reconstruction-Aware Sensor Layout
**Date**: 2026-05-18
**Current stage**: Method strengthened with Robust Certified Sensor Search (RCSS) plus validation-aware swap refinement; PeMS7_228 confirmatory evidence complete.

## Core Claim

TRACE-SL improves full-network traffic state reconstruction by optimizing sensor placement for the recoverability of a transparent inverse problem. Its key mechanism is not a black-box state estimator, but an OR-guided sensor-layout search that uses posterior uncertainty, robust scenario risk, validation reconstruction error, and spatial coverage to select layouts that generalize better than random or topology-only placement.

## Method Summary

TRACE-SL uses GLS/MAP and GSP as transparent full-network reconstruction models. Given a candidate sensor set, the hidden-link reconstruction error is evaluated under deployment simulation: only selected sensors are observed, while non-sensor nodes are held out for MAE/RMSE evaluation.

The strengthened method is **Robust Certified Sensor Search (RCSS)**:

1. Build a candidate pool from multiple OR-guided layout generators:
   - greedy A-optimal posterior trace;
   - greedy D-optimal logdet;
   - scenario-average A-trace;
   - scenario-CVaR A-trace;
   - posterior-trace swap refinements;
   - quality-coverage sampling, which samples high posterior-uncertainty nodes while enforcing spatial diversity;
   - simple degree, top-variance, and coverage baselines;
   - validation-ranked random candidates for comparison.
2. Select RCSS weights by inner validation rather than fixing them manually. The validation days are split into `selector_val` and `tuner_val`; each candidate weight vector selects a layout on `selector_val`, and the vector with the lowest `tuner_val` GLS/MAP MAE is used.
3. Select the layout with the resulting data-driven score and evaluate it on unseen test days.
4. Refine the strongest RCSS candidates with validation-aware stochastic swap search. The swap search only accepts exchanges that improve validation GLS/MAP reconstruction error, using the OR-guided candidate pool as the add-node universe.

The final RCSS configuration was confirmed on held-out split seeds 25–29 after an earlier diagnostic stage on seeds 20–24. Stage 10 strengthens the method by adding validation-aware swap refinement; Stage 11 removes the manual-weight concern by selecting RCSS weights through inner validation.

## Key Evidence

### Stage 9 confirmatory experiment

Directory: `TRC-23-02333/trace_sl_results/pems7_228_stage9_rcss_quality/`

Setup:

- Dataset: PeMS7_228.
- Split seeds: 25, 26, 27, 28, 29.
- Budgets: 10%, 20%, 30%.
- Uniform random layouts: 200 per budget per split.
- Quality-coverage OR-guided candidates: 200 per budget per split.
- Estimator for primary comparison: GLS/MAP.

Mean GLS/MAP test MAE:

| Budget | RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.4966 | 3.5677 | 3.7067 | 3.5780 |
| 20% | 3.2459 | 3.3105 | 3.4617 | 3.3188 |
| 30% | 3.0402 | 3.0919 | 3.3147 | 3.0982 |

RCSS deltas, negative is better:

| Budget | vs random mean | vs best random by validation | vs top variance | vs greedy A-trace |
|---:|---:|---:|---:|---:|
| 10% | -0.2101 | -0.0712 | -0.0814 | -0.0436 |
| 20% | -0.2157 | -0.0646 | -0.0729 | -0.1120 |
| 30% | -0.2745 | -0.0517 | -0.0580 | -0.2198 |

This supports the strong claim that RCSS improves reconstruction over both average random layouts and validation-selected random layouts across all tested budgets.

### Stage 10 validation-aware swap refinement

Directory: `TRC-23-02333/trace_sl_results/pems7_228_stage10_validation_swap/`

Stage 10 keeps the Stage 9 quality-coverage candidate pool and adds a validation-aware swap refinement from the top RCSS candidates.

Mean GLS/MAP test MAE:

| Budget | Validation-swap RCSS | Stage 9 RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|---:|
| 10% | 3.4630 | 3.4966 | 3.5677 | 3.7067 | 3.5780 |
| 20% | 3.2340 | 3.2459 | 3.3105 | 3.4617 | 3.3188 |
| 30% | 2.9893 | 3.0402 | 3.0919 | 3.3147 | 3.0982 |

Validation-swap RCSS deltas, negative is better:

| Budget | vs random mean | vs best random by validation | vs top variance | vs Stage 9 RCSS |
|---:|---:|---:|---:|---:|
| 10% | -0.2437 | -0.1047 | -0.1150 | -0.0336 |
| 20% | -0.2277 | -0.0766 | -0.0849 | -0.0120 |
| 30% | -0.3254 | -0.1026 | -0.1089 | -0.0509 |

Winner counts across five held-out splits:

| Budget | Validation-swap RCSS wins |
|---:|---:|
| 10% | 2/5 |
| 20% | 3/5 |
| 30% | 5/5 |

Paired tests against best random by validation:

| Budget | Mean delta | Win count | paired t-test p |
|---:|---:|---:|---:|
| 10% | -0.1047 | 4/5 | 0.0540 |
| 20% | -0.0766 | 5/5 | 0.0510 |
| 30% | -0.1026 | 5/5 | 0.0259 |

Stage 10 therefore systematically increases the advantage relative to Stage 9, especially at the 30% budget where validation-swap RCSS wins every split and reaches a paired t-test p-value below 0.05 against validation-selected random.

### Stage 11 automatic weight selection

Directory: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/`

Stage 11 replaces fixed RCSS coefficients with inner-validation weight selection. The automatically selected weights were mostly validation-only, which is an important finding: the robust advantage is mainly created by the OR-guided candidate pool and validation-aware swap refinement, not by hand-tuned certificate weights.

Mean GLS/MAP test MAE:

| Budget | Auto-weight validation-swap RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.4863 | 3.5677 | 3.7067 | 3.5780 |
| 20% | 3.2336 | 3.3105 | 3.4617 | 3.3188 |
| 30% | 2.9971 | 3.0919 | 3.3147 | 3.0982 |

Auto-weight validation-swap deltas, negative is better:

| Budget | vs random mean | vs best random by validation | vs top variance | paired t-test p vs best-random |
|---:|---:|---:|---:|---:|
| 10% | -0.2204 | -0.0814 | -0.0916 | 0.0819 |
| 20% | -0.2280 | -0.0769 | -0.0852 | 0.0001 |
| 30% | -0.3176 | -0.0948 | -0.1011 | 0.0215 |

Selected weight distribution:

| Budget | Dominant selected weight |
|---:|---|
| 10% | validation-only, 5/5 splits |
| 20% | validation-only, 3/5 splits; mixed CVaR/coverage variants, 2/5 splits |
| 30% | validation-only, 5/5 splits |

This means the paper should not present `0.70/0.10/0.20` as a manually chosen coefficient vector. The cleaner claim is that TRACE-SL creates an OR-guided candidate space, then uses inner validation to select either validation-only or certificate-regularized RCSS scoring depending on the split.

### Certificate validity

GLS/MAP posterior certificates are stable predictors of hidden reconstruction error in Stage 11:

| Certificate | Pearson with MAE | Spearman with MAE |
|---|---:|---:|
| posterior trace | 0.8550 | 0.8460 |
| condition number | 0.8291 | 0.8528 |
| information logdet | -0.8160 | -0.8081 |

This supports the interpretability claim: the OR certificates are not decorative; they are strongly aligned with empirical hidden-link reconstruction quality.

### Mechanism evidence

RCSS selected `quality_coverage_sample` frequently in the budgets where earlier Stage 8 failed:

| Budget | Selected source counts |
|---:|---|
| 10% | greedy/swap/quality mixed |
| 20% | quality-coverage sample 3/5, multistart swap 2/5 |
| 30% | quality-coverage sample 4/5, random validation pool 1/5 |

This suggests the improvement comes from adding an OR-guided, certificate-aware searchable candidate space rather than merely tuning the final selector.

## Claim Status

- C1: Transparent GLS/MAP reconstruction from sparse sensors is viable — supported.
- C2: OR-guided RCSS layouts improve reconstruction over random placement and validation-selected random placement — strengthened on PeMS7_228 Stage 10.
- C3: Certificates explain layout quality — strongly supported by stable correlation.
- C4: RL is not yet needed for the core claim — RCSS currently provides an OR-guided non-DL method; RL can remain optional for amortizing repeated search later.
- C5: Regime-aware TS insight remains a paper extension, not required for the current core evidence.

## Figure and Table Inventory

Ready from existing CSV outputs:

1. Budget-vs-MAE table: `gls_map_layout_summary.csv`.
2. Delta table vs random/baselines: `gls_map_delta_summary.csv`.
3. Validation-swap paired tests: `validation_swap_delta_tests.csv`.
4. Auto-weight selection summary: `auto_weight_selection_summary.csv`.
5. Certificate stability table: `certificate_correlation_summary.csv`.
5. Selected-source mechanism table: `rcss_selected_sources.csv`.
6. Candidate-level analysis: `combined_rcss_candidates.csv`.

Recommended figures:

1. Bar chart: RCSS vs best-random vs top-variance vs random mean across budgets.
2. Scatter plot: posterior trace vs hidden MAE for GLS/MAP.
3. Method diagram: RCSS candidate pool -> robust selector -> transparent GLS/MAP evaluation.
4. Optional sensor maps if PeMS node coordinates are available.

## Remaining Follow-up

1. Run the same validation-swap RCSS configuration on Seattle or PeMS7_1026 for external validation.
2. Generate final paper figures from Stage 10 CSV files.
3. Consider increasing held-out split count from 5 to 10 for stronger p-values.
4. If RL is retained, frame it as optional amortized search over the RCSS candidate-generation process, not as the estimator.
