# TRACE-SL Narrative Report

**Project**: TRACE-SL — Transparent Reconstruction-Aware Sensor Layout
**Date**: 2026-05-26
**Current stage**: Stage 12 baseline-portfolio evidence is complete for PeMS7_228, PeMS7_1026, and Seattle; TR-B positioning should emphasize reconstruction-aware inverse-problem design, scoped theory, and multi-network evidence rather than a single heuristic benchmark win.

## Core Claim

TRACE-SL improves full-network traffic state reconstruction by optimizing sensor placement for the recoverability of a transparent inverse problem. Its key mechanism is not a black-box state estimator, but an OR-guided sensor-layout search that uses posterior uncertainty, robust scenario risk, validation reconstruction error, and spatial coverage to select layouts that are empirically more recoverable than random, topology-only, variance, graph-sampling, observability, and POD-style placements in the tested settings.

For a TR-B manuscript, the main contribution should be framed as **reconstruction-aware network design / transparent inverse problem design**: sensors are not selected to cover the graph as an end in itself, but to make the hidden complement of the traffic network recoverable under transparent GLS/MAP and GSP reconstruction models. The claim boundary is certificate-guided and posterior-certificate-aware, not certified, globally optimal, globally robust, or a guaranteed MAE improvement beyond the tested evidence.

## Method Summary

TRACE-SL uses GLS/MAP and GSP as transparent full-network reconstruction models. Given a candidate sensor set, the hidden-link reconstruction error is evaluated under deployment simulation: only selected sensors are observed, while non-sensor nodes are held out for MAE/RMSE evaluation.

The strengthened method is **Robust Certificate-guided Sensor Search (RCSS)**:

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

The final paper-facing evidence is Stage 12 baseline-portfolio evidence. Stage 10 strengthened the method by adding validation-aware swap refinement; Stage 11 removed the manual-weight concern by selecting RCSS weights through inner validation; Stage 12 expanded the comparator portfolio and external ten-split evidence. Stage 11 remains useful development history, but Stage 12 artifacts under `TRC-23-02333/trace_sl_results/paper_sources/` are the current manuscript-facing source of truth.

### Formulation and theory bridge

Phase 2 frames TRACE-SL as **budgeted reconstruction-aware sensor-set design**: choose a sparse fixed sensor set `S` under `|S| <= k` so transparent GLS/MAP or GSP reconstruction can recover the hidden complement of the traffic network. The design protocol keeps three evidence channels separate: train-derived reconstruction ingredients such as priors, covariance/precision estimates, graph structure, and regularization; validation layout selection through RCSS scoring, auto-weight tuning, and validation-aware swap refinement; and held-out test evaluation after the layout rule is fixed.

The RCSS surrogate combines validation reconstruction loss with posterior-certificate-aware diagnostics: posterior covariance trace, scenario CVaR trace, condition number, and spatial coverage. Under the scoped linear-Gaussian GLS/MAP derivation, the posterior covariance trace is tied to expected squared hidden-state error, giving an A-optimal uncertainty proxy for the hidden complement. Because the reported traffic metric is MAE and real traffic data can depart from Gaussian squared-error assumptions, this bridge motivates certificate-guided selection but does not turn posterior diagnostics into a broad MAE guarantee.

Detailed paper-writing support is in `.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md`. Optional TR Part B extension requirements are separated in `.planning/phases/02-formulation-and-theory-bridge/02-TR-PART-B-THEORY-GAP-NOTE.md`, including deferred v2 monotonicity, approximate-submodularity, approximation, stability, and stochastic/bilevel analysis needs.

## Current manuscript source of truth

The current paper-source package is generated from committed aggregate artifacts under `TRC-23-02333/trace_sl_results/paper_sources/`. It includes Stage 12 core performance, paired deltas, external evidence gates, ablation contracts, dataset evidence classification, certificate correlations, and scoped theory statements.

### Stage 12 core PeMS7_228 evidence

Directory: `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/`

Mean GLS/MAP test MAE across ten held-out splits:

| Budget | Validation-swap selected | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.5901 | 3.7131 | 3.8331 | 3.7304 |
| 20% | 3.3547 | 3.4495 | 3.5746 | 3.4276 |
| 30% | 3.0842 | 3.2469 | 3.4037 | 3.2004 |

Paired tests against validation-selected random support improvement at all three budgets: p=0.0000876 at 10%, p=0.00537 at 20%, and p=0.000509 at 30%. The 10% PeMS7_228 budget carries the caveat `pems7_228_low_budget_multistart_not_dominant`, because the multistart swap comparator is statistically close.

### Stage 12 external evidence

The external evidence gate reports PeMS7_1026 and Seattle as complete: both have ten tracked split seeds, held-out aggregate artifacts, paired evidence, and `core_claim_eligible=True` in `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.md`.

| Dataset | Budget | Validation-swap selected MAE | Split count |
|---|---:|---:|---:|
| PeMS7_1026 | 10% | 3.7674 | 10 |
| PeMS7_1026 | 20% | 3.3467 | 10 |
| PeMS7_1026 | 30% | 3.0740 | 10 |
| Seattle | 10% | 3.1012 | 10 |
| Seattle | 20% | 2.8281 | 10 |
| Seattle | 30% | 2.6241 | 10 |

This evidence supports a multi-network empirical claim. It should not be phrased as universal generalization. At PeMS7_1026 10%, internal OR variants such as `swap_from_greedy_a_trace` and `greedy_a_trace` slightly outperform `validation_swap_selected`, so the safest and most accurate method identity is TRACE-SL as a reconstruction-aware layout design framework/portfolio with a main selected layout, not a single selector that dominates every internal variant everywhere.

### Stage 12 theory and claim contracts

The theory contract now covers formulation, posterior trace squared-error identity under scoped linear-Gaussian assumptions, posterior covariance monotonicity, validation-aware one-swap local optimality, and RCSS workload complexity. These statements are ready to be converted into manuscript theorem/proposition form, but they do not imply non-Gaussian traffic MAE guarantees, submodularity, approximation ratios, global optimality, or certified robustness.

## Legacy development evidence

The sections below record the development path through Stages 9--11. They should not be used as the primary manuscript source of truth when Stage 12 paper-source artifacts are available.

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

Selected weight distribution in the original five-split Stage 11 run:

| Budget | Dominant selected weight |
|---:|---|
| 10% | validation-only, 5/5 splits |
| 20% | validation-only, 3/5 splits; mixed CVaR/coverage variants, 2/5 splits |
| 30% | validation-only, 5/5 splits |

This means the paper should not present `0.70/0.10/0.20` as a manually chosen coefficient vector. The cleaner claim is that TRACE-SL creates an OR-guided candidate space, then uses inner validation to select either validation-only or certificate-regularized RCSS scoring depending on the split.

### Stage 11 PeMS7_1026 external-validation history

Directory: `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`

PeMS7_1026 used the same Stage 11 pipeline with 100 random layouts and 100 quality-coverage candidates per split. This remains useful history, but Stage 12 PeMS7_1026 evidence supersedes it for manuscript claims.

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

This was the first external-validation signal that TRACE-SL's validation-swap RCSS transferred to a larger PeMS7 network. Use Stage 12 paper-source rows for final external evidence and for any baseline-portfolio claims.

### Stage 11 Seattle heterogeneous-network history

Directory: `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/`

Seattle used the same Stage 11 pipeline on the available 323-sensor tensor representation, with five split seeds, 50 random layouts, and 50 quality-coverage candidates per split. This remains historical lightweight external validation; Stage 12 Seattle ten-split evidence supersedes it for current claims.

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

This lightweight run was later superseded by the completed Stage 12 Seattle gate. The current repository-visible source of truth is `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.md`.

### Certificate validity

GLS/MAP posterior certificates are stable predictors of hidden reconstruction error in the Stage 12 PeMS7_228 aggregate:

| Certificate | Pearson with MAE | Spearman with MAE |
|---|---:|---:|
| posterior trace | 0.7931 | 0.8068 |
| condition number | 0.8129 | 0.8548 |
| information logdet | -0.7019 | -0.7625 |

This supports the interpretability claim: the OR certificates are not decorative; they are aligned with empirical hidden-link reconstruction quality. They should still be described as empirical diagnostic certificates, not formal MAE guarantees.

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
- C2: OR-guided TRACE-SL layouts improve reconstruction over random placement, validation-selected random placement, and multiple reviewer-facing baselines in Stage 12 PeMS7_228 evidence; PeMS7_1026 and Seattle provide completed ten-split external evidence for multi-network discussion.
- C3: Certificates explain layout quality — supported by Stage 12 certificate-error correlations, but only as empirical diagnostic certificates rather than certified MAE guarantees.
- C4: RL is not yet needed for the core claim — RCSS currently provides an OR-guided non-DL method; RL can remain optional for amortizing repeated search later.
- C5: Regime-aware TS insight remains a paper extension, not required for the current core evidence.

## Figure and Table Inventory

Ready from existing CSV outputs:

1. Budget-vs-MAE table: `gls_map_layout_summary.csv`.
2. Delta table vs random/baselines: `gls_map_delta_summary.csv`.
3. Main ablation table: `gls_map_ablation_summary.csv`.
4. Script-generated paired tests: `gls_map_paired_delta_tests.csv`.
5. Validation-swap paired tests in the main ten-split aggregate: use `gls_map_paired_delta_tests.csv` rows for `validation_swap_selected` comparisons.
6. Auto-weight selection summary: `auto_weight_selection_summary.csv` in the original five-split Stage 11 output; use with directory-qualified provenance until regenerated for the ten-split aggregate.
7. Certificate stability table: `certificate_correlation_summary.csv`.
8. Selected-source mechanism table: `rcss_selected_sources.csv`.
9. Candidate-level analysis: `combined_rcss_candidates.csv`.

Recommended figures:

1. Bar chart: RCSS vs best-random vs top-variance vs random mean across budgets.
2. Scatter plot: posterior trace vs hidden MAE for GLS/MAP.
3. Method diagram: RCSS candidate pool -> robust selector -> transparent GLS/MAP evaluation.
4. Optional sensor maps if PeMS node coordinates are available.

## Remaining Follow-up

1. Convert the theory contract into manuscript theorem/proposition form: problem definition, posterior trace identity, posterior covariance monotonicity, finite-candidate validation-selection bound, one-swap local optimality, and complexity.
2. Generate final figures from Stage 12 `paper_sources` and include PeMS7_228, PeMS7_1026, and Seattle in the main evidence package.
3. Add or clearly defer chronological and regime-shift splits; random split evidence should not be the only temporal validation story for TR-B.
4. If RL is retained, frame it as optional amortized search over the RCSS candidate-generation process, not as the estimator.
