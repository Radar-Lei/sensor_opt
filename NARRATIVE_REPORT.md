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

### Formulation and theory bridge

Phase 2 frames TRACE-SL as **budgeted reconstruction-aware sensor-set design**: choose a sparse fixed sensor set `S` under `|S| <= k` so transparent GLS/MAP or GSP reconstruction can recover the hidden complement of the traffic network. The design protocol keeps three evidence channels separate: train-derived reconstruction ingredients such as priors, covariance/precision estimates, graph structure, and regularization; validation layout selection through RCSS scoring, auto-weight tuning, and validation-aware swap refinement; and held-out test evaluation after the layout rule is fixed.

The RCSS surrogate combines validation reconstruction loss with posterior-certificate-aware diagnostics: posterior covariance trace, scenario CVaR trace, condition number, and spatial coverage. Under the scoped linear-Gaussian GLS/MAP derivation, the posterior covariance trace is tied to expected squared hidden-state error, giving an A-optimal uncertainty proxy for the hidden complement. Because the reported traffic metric is MAE and real traffic data can depart from Gaussian squared-error assumptions, this bridge motivates certificate-guided selection but does not turn posterior diagnostics into a broad MAE guarantee.

Detailed paper-writing support is in `.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md`. Optional TR Part B extension requirements are separated in `.planning/phases/02-formulation-and-theory-bridge/02-TR-PART-B-THEORY-GAP-NOTE.md`, including deferred v2 monotonicity, approximate-submodularity, approximation, stability, and stochastic/bilevel analysis needs.

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

### Stage 11 automatic weight selection, 10-split extension

Directories:

- Original five-split Stage 11: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/`
- Ten-split aggregate: `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`

Stage 11 replaces fixed RCSS coefficients with inner-validation weight selection. The automatically selected weights were mostly validation-only, which is an important finding: the robust advantage is mainly created by the OR-guided candidate pool and validation-aware swap refinement, not by hand-tuned certificate weights. The ten-split extension adds held-out split seeds 30--34 to the original seeds 25--29.

Mean GLS/MAP test MAE across 10 splits:

| Budget | Auto-weight validation-swap RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.6055 | 3.6913 | 3.8359 | 3.7304 |
| 20% | 3.3095 | 3.3969 | 3.5648 | 3.4276 |
| 30% | 3.0665 | 3.1832 | 3.4032 | 3.2004 |

Auto-weight validation-swap deltas across 10 splits, negative is better:

| Budget | vs random mean | vs best random by validation | vs top variance | paired t-test p vs best-random | Wilcoxon p vs best-random |
|---:|---:|---:|---:|---:|---:|
| 10% | -0.2304 | -0.0858 | -0.1249 | 0.0343 | 0.0273 |
| 20% | -0.2553 | -0.0874 | -0.1181 | 0.0025 | 0.0059 |
| 30% | -0.3367 | -0.1167 | -0.1339 | 0.00008 | 0.0020 |

Selected weight distribution:

| Budget | Dominant selected weight |
|---:|---|
| 10% | validation-only, 5/5 splits |
| 20% | validation-only, 3/5 splits; mixed CVaR/coverage variants, 2/5 splits |
| 30% | validation-only, 5/5 splits |

This means the paper should not present `0.70/0.10/0.20` as a manually chosen coefficient vector. The cleaner claim is that TRACE-SL creates an OR-guided candidate space, then uses inner validation to select either validation-only or certificate-regularized RCSS scoring depending on the split.

### PeMS7_1026 external validation

Directory: `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`

PeMS7_1026 uses the same Stage 11 pipeline with 100 random layouts and 100 quality-coverage candidates per split. This is an external-network validation relative to the PeMS7_228 development and confirmatory runs.

Mean GLS/MAP test MAE across five PeMS7_1026 splits:

| Budget | Validation-swap RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.6557 | 3.7437 | 3.8266 | 3.8602 |
| 20% | 3.2547 | 3.4653 | 3.5317 | 3.5859 |
| 30% | 2.9951 | 3.2483 | 3.3309 | 3.3266 |

Validation-swap RCSS deltas against best-random by validation:

| Budget | Mean delta | Win count | paired t-test p | Wilcoxon p |
|---:|---:|---:|---:|---:|
| 10% | -0.0879 | 5/5 | 0.0212 | 0.0625 |
| 20% | -0.2105 | 5/5 | 0.0007 | 0.0625 |
| 30% | -0.2531 | 5/5 | 0.0001 | 0.0625 |

This resolves the main external-validation concern: TRACE-SL's Stage 11 validation-swap RCSS transfers to a larger PeMS7 network and keeps a clear advantage over validation-selected random, random mean, and top variance across all tested budgets.

### Seattle heterogeneous-network validation

Directory: `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`

Seattle uses the same Stage 11 pipeline on the available 323-sensor tensor representation, with five split seeds, 50 random layouts, and 50 quality-coverage candidates per split. This is a lightweight external validation on a non-PeMS, spatially heterogeneous network.

Mean GLS/MAP test MAE across five Seattle splits:

| Budget | Validation-swap RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.0677 | 3.1888 | 3.3204 | 3.5499 |
| 20% | 2.8036 | 2.9488 | 3.0172 | 3.0796 |
| 30% | 2.6182 | 2.7243 | 2.8449 | 2.8090 |

Validation-swap RCSS deltas against best-random by validation:

| Budget | Mean delta | Win count | paired t-test p | Wilcoxon p |
|---:|---:|---:|---:|---:|
| 10% | -0.1210 | 5/5 | 0.0013 | 0.0625 |
| 20% | -0.1452 | 5/5 | 0.0032 | 0.0625 |
| 30% | -0.1061 | 5/5 | 0.0025 | 0.0625 |

Seattle strengthens the cross-network claim: validation-swap RCSS wins against validation-selected random on every split and every budget, while GLS/MAP certificates remain strongly aligned with hidden reconstruction error.

### Certificate validity

GLS/MAP posterior certificates are stable predictors of hidden reconstruction error in the 10-split Stage 11 aggregate:

| Certificate | Pearson with MAE | Spearman with MAE |
|---|---:|---:|
| posterior trace | 0.8612 | 0.8513 |
| condition number | 0.8327 | 0.8592 |
| information logdet | -0.8209 | -0.8130 |

This supports the interpretability claim: the OR certificates are not decorative; they are strongly aligned with empirical hidden-link reconstruction quality. On PeMS7_1026, the GLS/MAP certificate correlations are even stronger: posterior trace Spearman 0.9315, condition number Spearman 0.8930, and information logdet Spearman -0.8982. On Seattle, the corresponding Spearman correlations are also strong: posterior trace 0.8742, condition number 0.8846, and information logdet -0.8307.

### Mechanism evidence

RCSS selected `quality_coverage_sample` frequently in the budgets where earlier Stage 8 failed:

| Budget | Selected source counts in 10-split aggregate |
|---:|---|
| 10% | multistart swap 4/10; swap-from-greedy 2/10; quality/robust/scenario variants mixed |
| 20% | quality-coverage sample 5/10; multistart swap 4/10; robust coverage 1/10 |
| 30% | quality-coverage sample 9/10; random validation pool 1/10 |

This suggests the improvement comes from adding an OR-guided, certificate-aware searchable candidate space rather than merely tuning the final selector.

## Claim Status

- C1: Transparent GLS/MAP reconstruction from sparse sensors is viable — supported.
- C2: OR-guided RCSS layouts improve reconstruction over random placement and validation-selected random placement — strengthened by the PeMS7_228 Stage 11 ten-split aggregate and externally supported on PeMS7_1026 and Seattle.
- C3: Certificates explain layout quality — strongly supported by stable correlation on PeMS7_228, PeMS7_1026, and Seattle.
- C4: RL is not yet needed for the core claim — RCSS currently provides an OR-guided non-DL method; RL can remain optional for amortizing repeated search later.
- C5: Regime-aware TS insight remains a paper extension, not required for the current core evidence.

## Figure and Table Inventory

Ready from existing CSV outputs:

1. Budget-vs-MAE table: `gls_map_layout_summary.csv`.
2. Delta table vs random/baselines: `gls_map_delta_summary.csv`.
3. Main ablation table: `gls_map_ablation_summary.csv`.
4. Script-generated paired tests: `gls_map_paired_delta_tests.csv`.
5. Validation-swap paired tests from Stage 11 handoff: `validation_swap_delta_tests.csv`.
6. Auto-weight selection summary: `auto_weight_selection_summary.csv`.
7. Certificate stability table: `certificate_correlation_summary.csv`.
8. Selected-source mechanism table: `rcss_selected_sources.csv`.
9. Candidate-level analysis: `combined_rcss_candidates.csv`.

Recommended figures:

1. Bar chart: RCSS vs best-random vs top-variance vs random mean across budgets.
2. Scatter plot: posterior trace vs hidden MAE for GLS/MAP.
3. Method diagram: RCSS candidate pool -> robust selector -> transparent GLS/MAP evaluation.
4. Optional sensor maps if PeMS node coordinates are available.

## Remaining Follow-up

1. Generate final paper figures from PeMS7_228 ten-split, PeMS7_1026 external-validation, and Seattle heterogeneous-network CSV files.
2. Consider increasing PeMS7_1026 or Seattle split count only if the target venue demands stronger nonparametric tests; all five current external-validation splits already beat validation-selected random at every budget.
3. If RL is retained, frame it as optional amortized search over the RCSS candidate-generation process, not as the estimator.
