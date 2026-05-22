# Phase 2: Formulation and Theory Bridge

**Status:** Draft method/theory bridge for downstream manuscript work  
**Date:** 2026-05-22

## Phase Boundary

This phase-local artifact turns TRACE-SL/RCSS into a formal reconstruction-aware sparse sensor-set design method for paper writing. It provides the budgeted sensor-set problem, traffic-network notation, protocol separation, and a source register that later theory, baseline, evidence, robustness, and manuscript phases can extend.

For this Phase 2 plan slice, the artifact does **not** run new experiments, change algorithms, implement baselines, perform robustness tests, produce final manuscript sections, or read raw traffic datasets. It uses implementation identifiers and curated planning/evidence documents only.

## Source Register

### Planning and Claim-Scope Sources

- `.planning/PROJECT.md` — project value, target venue, active decisions, and raw-dataset/reproducibility constraints.
- `.planning/STATE.md` — current workflow state and active decisions for Phase 2.
- `.planning/ROADMAP.md` — Phase 2 goal and THEORY-01..THEORY-06 success criteria.
- `.planning/REQUIREMENTS.md` — formulation/theory requirements and global out-of-scope constraints.
- `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` — validation/test separation and certificate terminology guardrails.
- `.planning/phases/02-formulation-and-theory-bridge/02-CONTEXT.md` — decisions D-01..D-12 for this artifact.
- `.planning/phases/02-formulation-and-theory-bridge/02-PATTERNS.md` — artifact structure and implementation-source patterns.
- `refine-logs/WRITING_NOTES_GREEDY_OFFLINE_PLANNING.md` — offline planning framing for greedy and swap layout construction.

### Implementation Anchors Used as Method Source of Truth

- `split_daily_frame` — separates train, validation, and held-out test days.
- `solve_quadratic` — computes transparent GSP/GLS-MAP reconstruction from selected sensors.
- `certificate` — emits posterior trace, condition number, and information logdet diagnostics.
- `evaluate_layout` — evaluates a fixed sensor set by hiding complement nodes and measuring reconstruction error.
- `posterior_trace_for_layout`, `scenario_cvar_trace_for_layout`, `posterior_condition_for_layout`, and `coverage_penalty` — define RCSS diagnostic terms.
- `rcss_candidate_scores`, `make_rcss_row`, `split_validation_for_tuning`, `parse_weight_grid`, and `select_auto_rcss_weights` — define RCSS scoring and inner-validation auto-weight selection.
- `validation_swap_search` — defines validation-aware one-swap local refinement.

No raw traffic-dataset directory is used as an evidence source here.

## Notation

Let `G = (V, E)` denote the traffic network, where nodes/links in `V` index traffic measurement locations and edges in `E` encode network adjacency or distance. A traffic state at one time step is `x \in R^{|V|}`. A deployment chooses an observed sensor subset `S \subset V`; the hidden complement is `H = V \setminus S`. The observed vector is `y_S`, containing the entries of `x` revealed at `S`.

A transparent reconstruction model, such as GLS/MAP or GSP, maps the observed subset and train-derived priors to hidden-state estimates:

`\hat{x}_H(S) = R_H(y_S; S, \theta_train)`,

where `\theta_train` includes train-derived mean, time-of-day prior, covariance or precision, graph Laplacian, standardization constants, and regularization/observation weights. The deployment budget is a cardinality or budget-fraction constraint written as `|S| <= k`.

## Budgeted Reconstruction-Aware Sensor-Set Problem

TRACE-SL is the offline planning problem of choosing a sparse sensor set for hidden-node reconstruction, not post-hoc candidate-pool tuning. The ideal paper-facing objective is:

`min_{S \subset V, |S| <= k} E[ L_H(x_H, \hat{x}_H(S)) ]`,

where the loss is measured on `H`, the unobserved complement of `S`, under a transparent reconstruction map. For empirical reporting, final performance evidence must be measured on held-out test data after the layout rule is fixed.

This directly covers THEORY-01: the method is a budgeted sensor-set formulation with hidden-node reconstruction, held-out loss, and a transparent reconstruction model. It also implements D-01 and D-03 by making `S`, `H`, `x`, `y_S`, `\hat{x}_H(S)`, and `|S| <= k` the core design notation.

## Protocol Separation

TRACE-SL uses a strict three-stage protocol so selection evidence and final evidence are not conflated:

1. **Train-derived reconstruction ingredients:** Use training data to estimate the time-of-day prior, mean/standardization, covariance or precision, graph/precision prior, scenario matrices, and reconstruction hyperparameters for GLS/MAP or GSP. The function `split_daily_frame` is the implementation anchor for train/validation/test separation.
2. **Validation layout selection:** Use validation data to rank, tune, or refine sensor layouts. Validation MAE can define the RCSS surrogate and validation-aware swap acceptance rule, but it is selection evidence only.
3. **Held-out test evaluation:** After layout selection is fixed, evaluate reconstruction on held-out test data by observing only `S` and scoring hidden complement `H` through `evaluate_layout`. Held-out test evidence is the only performance evidence for final claims.

This implements D-02 and preserves the Phase 1 guardrail that validation MAE is not final performance evidence.

## Requirement Traceability

| Requirement | Coverage in this artifact |
|---|---|
| THEORY-01 | Covered by `Notation`, `Budgeted Reconstruction-Aware Sensor-Set Problem`, and `Protocol Separation`. |

## Self-Check

- [x] THEORY-01 is covered by the formal problem statement and protocol boundary.
- [x] D-01 is covered: TRACE-SL is stated as budgeted sparse sensor-set design for hidden-node reconstruction.
- [x] D-02 is covered: train-derived ingredients, validation selection, and held-out test evaluation are separated.
- [x] D-03 is covered: traffic-network notation includes `G`, `S`, `H`, `x`, `y_S`, `\hat{x}_H(S)`, and `|S| <= k`.
- [x] Raw dataset reads are excluded from this phase-local artifact.
