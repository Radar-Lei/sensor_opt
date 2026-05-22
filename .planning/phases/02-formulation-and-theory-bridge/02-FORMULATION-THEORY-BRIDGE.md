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

## TRACE-SL/RCSS Surrogate Objective

The exact budgeted reconstruction objective is combinatorial and expensive because every candidate `S` changes the hidden reconstruction map. TRACE-SL therefore uses RCSS as a predeclared tractable surrogate and algorithmic portfolio, not as post-hoc tuning. For each candidate layout, `make_rcss_row` records five named diagnostics:

1. **validation loss** — validation GLS/MAP reconstruction MAE from `validation_mae`, used only for layout selection;
2. **posterior trace** — `posterior_trace_for_layout`, an A-style uncertainty diagnostic for the GLS/MAP posterior matrix;
3. **scenario CVaR trace** — `scenario_cvar_trace_for_layout`, a tail-risk summary over train-derived scenario precision matrices;
4. **condition number** — `posterior_condition_for_layout`, a numerical stability diagnostic for the observation-regularized system;
5. **coverage** — `coverage_penalty`, a spatial dispersion term that discourages overly concentrated layouts.

`rcss_candidate_scores` normalizes these diagnostics and applies a fixed five-term weight vector to obtain a scalar RCSS score. This covers THEORY-02 and D-04 by tying the surrogate to validation loss, posterior trace, scenario CVaR trace, condition number, and coverage.

### Auto-Weight Selection

When auto weights are enabled, `split_validation_for_tuning` divides validation data into selector and tuner validation splits. `parse_weight_grid` defines a fixed weight grid, and `select_auto_rcss_weights` performs inner-validation model selection: each candidate weight vector selects the best layout on the selector split, then the tuner split chooses the weight vector with the lowest tuner validation GLS/MAP MAE. The selected weight vector is then applied before held-out test evaluation.

This implements D-05: auto-weight selection is a predeclared fixed weight grid procedure over selector/tuner validation splits, not manual coefficient tuning after seeing test outcomes.

## Linear-Gaussian GLS/MAP Posterior-Error Bridge

The GLS/MAP implementation in `solve_quadratic` solves a regularized quadratic problem. In standardized units, write a linear observation model for a fixed sensor set `S` as

`y_S = P_S x + epsilon`, with `epsilon ~ N(0, sigma^2 W_S^{-1})`,

and a Gaussian prior or precision model

`x ~ N(mu, Q^{-1})`,

where `Q` is train-derived from covariance or graph/precision structure and regularized for numerical stability. The posterior precision for a fixed observation pattern can be written schematically as

`Q_S = Q + P_S^T W_S P_S`,

matching the implementation pattern `matrix + diag(selector)` in `solve_quadratic`, `certificate`, and `posterior_inverse_for_layout`. The posterior covariance is

`Sigma_{post}(S) = Q_S^{-1}`.

For the hidden complement `H`, the posterior covariance block `Sigma_{HH|S}` gives the conditional uncertainty in hidden states after observing `S`. Under the Gaussian/linear model and squared-error loss, the posterior mean/MAP estimator satisfies the identity

`E[ ||x_H - E[x_H | y_S]||_2^2 | y_S ] = trace(Sigma_{HH|S})`.

Thus, the posterior covariance trace is an A-optimal proxy for expected hidden-state squared error under the idealized model. This covers THEORY-03 and D-07.

### Assumptions and Scope of the Derivation

The bridge requires these assumptions from D-08:

- Gaussian/linear observation model for the selected sensors;
- train-derived covariance or precision used as the reconstruction prior;
- regularized graph/precision prior so the solve is numerically well-posed;
- fixed sensor observations for a fixed `S` rather than adaptive deployment;
- squared-error analysis, not direct MAE optimality.

## MAE-Oriented Interpretation and Caveats

Posterior trace and related certificates motivate MAE-oriented sensor selection because reducing posterior variance should reduce squared hidden-state reconstruction uncertainty under the linear-Gaussian bridge, and current curated evidence reports empirical certificate-error alignment. However, this remains an empirical bridge rather than a broad guarantee.

Real traffic data can be non-Gaussian, temporally shifted, heteroskedastic, and affected by validation selection. The reported paper metric is often MAE, while the derivation is a squared-error identity. Therefore the correct terminology is **certificate-guided** or **posterior-certificate-aware** sensor placement: posterior trace, condition number, information logdet, scenario CVaR trace, and coverage are transparent diagnostics and surrogate terms, not broad project-level certification of optimality or guaranteed MAE dominance.

This covers THEORY-04, D-09, and D-12.

## Validation-Aware Swap Analysis

`validation_swap_search` is an offline local-refinement heuristic for a fixed deployment set, not a sequential physical installation policy. The fixed add-node universe is derived from the OR-guided candidate pool: the implementation forms a candidate union from RCSS candidate layouts and only proposes add nodes from that universe, excluding nodes already selected in the current layout.

For each start layout, the algorithm evaluates one-swap neighborhoods. A trial is a **single remove/add swap**: remove one selected sensor and add one candidate node from the fixed add-node universe. The swap is accepted only when the candidate layout improves validation GLS/MAP reconstruction loss under the implemented acceptance rule:

`row["validation_mae"] < best_row["validation_mae"] - validation_swap_min_improve`.

At each iteration, among improving trials, the implementation accepts the trial with the lowest validation GLS/MAP reconstruction loss. It terminates when there are no trials, no improving trials, no candidate add nodes, or the configured swap-iteration limit is reached. This implements D-06.

### Complexity and Dense-Solver Limitation

Let `U` be the candidate universe size, `k` the sensor budget, `T_val` the number of validation samples or time steps, `C_solve(n, T_val)` the cost of one reconstruction evaluation over a network with `n` nodes and validation data, `B` the number of starts, and `I` the number of swap iterations. In the unrestricted one-swap neighborhood, each iteration can inspect up to `O(k(U-k))` remove/add trials, giving a high-level cost of

`O(B I k (U-k) C_solve(n, T_val))`,

plus diagnostic costs for posterior trace, scenario CVaR trace, condition number, and coverage. The implementation can cap remove and add pools through `validation_swap_remove_pool` and `validation_swap_add_pool`, replacing `k` and `U-k` by those pool sizes in the inspected-neighborhood cost.

Dense-solver scaling is a limitation. The current implementation uses dense `linalg.solve` in `solve_quadratic` and explicit dense inverse operations in `certificate` and `posterior_inverse_for_layout`. This makes the analysis faithful to the present code and motivates later scaling work rather than implying sparse/rank-update solvers already exist. This covers D-10 and THEORY-05.

### Fixed-Candidate Local Optimality

The validation-aware swap statement is intentionally local and implementation-scoped: at termination without hitting a preset iteration cap, no evaluated single remove/add swap from the fixed add-node universe improves the chosen validation objective under the implemented acceptance rule and active add/remove pool restrictions. If the pools are unrestricted, this is one-swap local optimality over the fixed candidate universe. It is not a global optimality guarantee and is not evidence of broad certified optimization. This covers D-11 and preserves D-12.

## Guardrails

- This artifact defines method/theory wording only; it does not run new experiments, implement baseline work, perform robustness tests, rebuild split evidence, curate Seattle outputs, or write the final manuscript.
- Validation MAE remains selection evidence for RCSS scoring, auto-weight tuning, and validation-aware swap; held-out test evaluation remains the final performance evidence channel.
- Certificate language remains certificate-guided, posterior-certificate-aware, or diagnostic. Posterior trace identities are scoped to the linear-Gaussian squared-error bridge.
- Raw dataset reads are excluded from this phase-local artifact, and raw traffic-dataset directories are not cited as evidence sources.
- Phase 3 owns reviewer-grade baselines and the multistart comparator/portfolio decision; Phase 4 owns held-out evidence/statistical audit and any needed split-evidence regeneration; Phase 5 owns robustness tests; Phase 7 owns final Transportation Science manuscript integration.

## Requirement Traceability

| Requirement | Coverage in this artifact |
|---|---|
| THEORY-01 | Covered by `Notation`, `Budgeted Reconstruction-Aware Sensor-Set Problem`, and `Protocol Separation`. |
| THEORY-02 | Covered by `TRACE-SL/RCSS Surrogate Objective` with validation loss, posterior trace, scenario CVaR trace, condition number, and coverage. |
| THEORY-03 | Covered by `Linear-Gaussian GLS/MAP Posterior-Error Bridge`. |
| THEORY-04 | Covered by `MAE-Oriented Interpretation and Caveats`. |
| THEORY-05 | Covered by `Validation-Aware Swap Analysis`, complexity discussion, dense-solver scaling limitation, and fixed-candidate local optimality. |

## Self-Check

- [x] THEORY-01 is covered by the formal problem statement and protocol boundary.
- [x] THEORY-02 is covered by the RCSS surrogate objective and auto-weight selection text.
- [x] THEORY-03 is covered by the posterior covariance trace to expected hidden-state squared error derivation.
- [x] THEORY-04 is covered by the MAE-oriented caveats and certificate terminology scope.
- [x] THEORY-05 is covered by validation-aware swap complexity and local optimality text.
- [x] D-01 is covered: TRACE-SL is stated as budgeted sparse sensor-set design for hidden-node reconstruction.
- [x] D-02 is covered: train-derived ingredients, validation selection, and held-out test evaluation are separated.
- [x] D-03 is covered: traffic-network notation includes `G`, `S`, `H`, `x`, `y_S`, `\hat{x}_H(S)`, and `|S| <= k`.
- [x] D-04 is covered: RCSS names validation loss, posterior trace, scenario CVaR trace, condition number, and coverage.
- [x] D-05 is covered: auto weights use selector/tuner validation splits and fixed weight grid selection.
- [x] D-06 is covered: validation-aware swap uses the fixed add-node universe from the OR-guided candidate pool and accepts only validation GLS/MAP reconstruction loss improvements.
- [x] D-07 is covered: posterior trace is connected to expected hidden-state squared error under linear-Gaussian assumptions.
- [x] D-08 is covered: Gaussian/linear, train-derived prior, regularization, fixed observations, and squared-error assumptions are explicit.
- [x] D-09 is covered: posterior variance is presented as MAE-oriented empirical guidance, not an MAE theorem.
- [x] D-10 is covered: complexity names candidate universe size, budget k, validation samples, reconstruction solve cost, number of starts, and swap iterations.
- [x] D-11 is covered: fixed-candidate single-swap local optimality is stated under the implemented validation-loss acceptance rule.
- [x] D-12 is covered: certificate terminology is scoped to certificate-guided or posterior-certificate-aware language.
- [x] Deferred ideas are excluded: no new experiments, baseline implementation, robustness tests, final manuscript writing, or raw dataset reads are part of this phase-local artifact.
- [x] Raw dataset reads are excluded from this phase-local artifact.
