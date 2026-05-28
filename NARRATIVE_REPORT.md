# TRACE-BiOpt Narrative Report

**Project**: TRACE-BiOpt — Recoverability-Driven Bilevel Transportation Network Design for Sparse Traffic Sensor Siting
**Date**: 2026-05-28
**Target venue**: Transportation Research Part B: Methodological (Elsevier CAS template)
**Current stage**: TRACE-BiOpt evidence complete; manuscript compiled; aggregate claim status `supported_submission_ready`.

## Core Claim

TRACE-BiOpt is a recoverability-driven bilevel transportation network-design method for sparse traffic sensor siting. It optimizes one objective under one transparent GLS/MAP inverse problem, with a formal CVaR tail-risk epigraph in the upper-level objective and deterministic initialization-and-exchange solver. The key mechanism is not a candidate-pool selector, black-box estimator, or portfolio chooser: it is a single recoverability-driven bilevel objective that jointly optimizes hidden-state reconstruction loss, posterior uncertainty, scenario tail risk, and spatial redundancy.

Across the tested datasets (PeMS7_228, PeMS7_1026, Seattle) and 10/20/30% budget regimes, TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against 21 pre-registered baselines spanning 11 method families. After Holm correction across all 189 paired comparisons, no statistically tied or significantly better pre-registered challenger remains.

The claim boundary is: TRACE-BiOpt is not allowed to claim global optimality over all size-`k` layouts, dominance over untested baselines, universal cross-network generalization, robustness outside the explicitly tested perturbation regimes, or relaxed-rounding evidence claims without a matching multi-seed evidence run.

## Method Summary

TRACE-BiOpt chooses a fixed sensor layout `S subset V`, `|S| = k`, by minimizing:

```
J(S) = hidden_huber_reconstruction_loss(S)
     + beta  * posterior_trace(S) / n
     + gamma * scenario_cvar_trace(S) / n
     + eta   * spatial_redundancy_penalty(S)
```

### Lower-level transparent reconstruction

For a binary sensor vector `s in {0,1}^n`, the lower-level reconstruction solves the regularized GLS/MAP inverse problem with closed-form linear solution `z_hat_t(s) = A(s)^{-1} b_t(s)`. This is the same lower-level estimator used in the paper theory, dominance tables, and current-best evidence chain.

### Deterministic solver

1. **Initialization**: either relaxed rounding (optimize a relaxed vector in `[0,1]^n`, then deterministic top-`k` rounding) or objective-forward construction (current evidence default).
2. **Exchange refinement**: repeatedly evaluate deterministic one-swap moves under `J(S)` and accept the best strict improvement. On larger networks, remove/add candidates may be restricted to deterministic active sets.
3. **Stopping**: no searched one-exchange move improves `J(S)` by more than the declared tolerance, or the exchange iteration cap is exhausted.

This implies a searched-neighborhood exchange certificate, not global optimality over all `n choose k` layouts.

### Relationship to TRACE-SL/RCSS (predecessor)

TRACE-SL/RCSS was the predecessor candidate-pool framework: OR-guided candidate generation, validation-calibrated RCSS scoring, and validation-aware swap refinement. TRACE-BiOpt replaces this pipeline with a single bilevel objective solved deterministically. TRACE-SL/RCSS remains available as baseline rows within the TRACE-BiOpt comparison class.

## Current manuscript source of truth

The authoritative evidence source is:

```
TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/
```

Key artifacts:
- `trace_biopt_claim_contract.json`: row-level and aggregate wording contract (`supported_submission_ready`).
- `trace_biopt_best_baseline_delta.csv`: TRACE-BiOpt MAE vs best baseline per dataset-budget.
- `trace_biopt_full_baseline_matrix.csv`: full 9-row x 21-baseline comparison matrix.
- `trace_biopt_current_best_provenance.csv`: row-level source policy (Stage 15 or Stage 16).
- `TRACE_BIOPT_DOMINANCE.md`: Holm-corrected dominance summary (189/189 wins, 0 tied, 0 better challengers).
- `trace_biopt_exact_subnetwork_summary.csv`: 27/27 exact 16-node subnetwork hits with zero objective gap.

### Current-best provenance

8/9 current-best main rows are promoted from Stage 16 calibrated reruns:
- PeMS7_228: 10%, 20%, 30%
- PeMS7_1026: 10%, 20%, 30%
- Seattle: 20%, 30%

Seattle 10% is intentionally retained on the fail-closed Stage 15 lane because the calibrated rerun did not satisfy the replacement gate.

### TRACE-BiOpt baseline comparison class

21 pre-registered baselines spanning 11 method families, including:
- Random placement (uniform, validation-selected)
- Topology-only (degree, coverage)
- Variance-based (top-variance)
- Graph sampling (spectral, QR/POD)
- Greedy A-trace (A-optimal posterior)
- Greedy D-logdet (D-optimal)
- Scenario-average A-trace
- Scenario-CVaR A-trace
- Posterior-trace swap refinement
- Quality-coverage sampling
- Robust coverage/CVaR
- **TRACE-SL/RCSS validation-swap selected** (the predecessor method as a baseline row)

No surviving challenger after 189 Holm-corrected paired comparisons.

## Auxiliary Evidence

### Exact subnetwork benchmark

27/27 deterministic 16-node audited subnetwork cases are exact hits with zero objective gap under row-wise current-best parameters. This supports the claim that TRACE-BiOpt's deterministic solver recovers the optimal layout in small-scale exhaustive-search-verified subnetworks.

### Certificate and mechanism diagnostics

GLS/MAP posterior certificates remain stable predictors of hidden reconstruction error in the TRACE-BiOpt evidence chain. Detailed certificate-error correlations, layout fingerprints, objective descent curves, and mechanism diagnostics are in `current_best_trace_biopt_evidence/`.

### Solver scale and compute posture

TRACE-BiOpt measured runtime and tractability evidence is available in `trace_biopt_solver_scale_summary.csv` and `trace_biopt_compute_posture.csv` under the current-best evidence directory.

## Historical TRACE-SL/RCSS Evidence

The sections below record the predecessor TRACE-SL/RCSS development path through Stages 9--14. They should not be used as the primary manuscript source of truth for the current TRACE-BiOpt paper. The current-best TRACE-BiOpt evidence chain in `current_best_trace_biopt_evidence/` supersedes all historical TRACE-SL paper-source artifacts.

### Stage 12 TRACE-SL core PeMS7_228 evidence (historical)

Directory: `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/`

Mean GLS/MAP test MAE across ten held-out splits:

| Budget | Validation-swap selected | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.5901 | 3.7131 | 3.8331 | 3.7304 |
| 20% | 3.3547 | 3.4495 | 3.5746 | 3.4276 |
| 30% | 3.0842 | 3.2469 | 3.4037 | 3.2004 |

### Stage 12 TRACE-SL external evidence (historical)

| Dataset | Budget | Validation-swap selected MAE | Split count |
|---|---:|---:|---:|
| PeMS7_1026 | 10% | 3.7674 | 10 |
| PeMS7_1026 | 20% | 3.3467 | 10 |
| PeMS7_1026 | 30% | 3.0740 | 10 |
| Seattle | 10% | 3.1012 | 10 |
| Seattle | 20% | 2.8281 | 10 |
| Seattle | 30% | 2.6241 | 10 |

### Stage 9--11 development history (historical)

Stage 9 added quality-coverage OR-guided candidates and confirmed RCSS wins over validation-selected random. Stage 10 added validation-aware swap refinement. Stage 11 replaced fixed RCSS weights with inner-validation weight selection. These stages remain useful development history for understanding the evolution from TRACE-SL to TRACE-BiOpt.

### Certificate validity (historical)

GLS/MAP posterior certificates were stable predictors of hidden reconstruction error in the Stage 12 TRACE-SL aggregate:

| Certificate | Pearson with MAE | Spearman with MAE |
|---|---:|---:|
| posterior trace | 0.7931 | 0.8068 |
| condition number | 0.8129 | 0.8548 |
| information logdet | -0.7019 | -0.7625 |

## Claim Status

- C1: TRACE-BiOpt is a recoverability-driven bilevel network-design method — supported (`supported_submission_ready`).
- C2: TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against 21 pre-registered baselines across 9 tested dataset-budget regimes — supported with Holm-corrected 189/189 dominance.
- C3: No statistically tied or significantly better pre-registered challenger survives after Holm correction — supported.
- C4: 27/27 deterministic subnetwork cases are exact hits — supported.
- C5: TRACE-SL/RCSS (predecessor) is a baseline row within the TRACE-BiOpt comparison class — supported as historical comparator.
- C6: The claim boundary excludes global optimality, universal generalization, untested baseline dominance, and untested perturbation robustness — bounded by design.

## Figure and Table Inventory

Current-best TRACE-BiOpt evidence provides:

1. `trace_biopt_full_baseline_matrix.csv`: full 9-row x 21-baseline comparison heatmap.
2. `trace_biopt_best_baseline_delta.csv`: TRACE-BiOpt vs best baseline per dataset-budget.
3. `trace_biopt_paired_margin_summary.csv`: paired margin evidence.
4. `trace_biopt_significance_posture_summary.csv`: Holm-corrected significance posture.
5. `trace_biopt_exact_subnetwork_summary.csv`: exact subnetwork benchmark.
6. `trace_biopt_objective_descent_summary.csv`: objective descent curves.
7. `trace_biopt_exchange_gap_summary.csv`: exchange gap convergence.
8. `trace_biopt_solver_scale_summary.csv`: solver scale and runtime.
9. `trace_biopt_weight_sensitivity.csv`: objective weight sensitivity.
10. `trace_biopt_route_ablation_summary.csv`: ablation by objective component.

Recommended figures for the manuscript are specified in `PAPER_PLAN.md`.

## Remaining Follow-up

1. Generate final manuscript figures from `current_best_trace_biopt_evidence/` CSV files.
2. Final proofreading pass on the compiled manuscript.
3. Prepare submission package for Transportation Research Part B: Methodological.
