# TRACE-BiOpt Method Contract

TRACE-BiOpt is the paper-facing v2 method for the Transportation Research Part B
submission. The contract here is intentionally narrower than a brainstorming
note: it records the unique optimization problem, the implemented deterministic
solver, the exposed hyperparameters, the current evidence lane, and the scope
boundaries that the manuscript is allowed to claim.

## 1. Method Identity

TRACE-BiOpt is not a candidate pool, portfolio selector, or AutoML-style
chooser over historical layouts. Baselines such as random, top variance,
degree, coverage, graph sampling, QR/POD, greedy A-trace, greedy D-logdet,
RCSS, and validation-swap TRACE-SL are evaluation rows only. They do not enter
the TRACE-BiOpt solver as method candidates.

The method claim is therefore:

```text
one recoverability-driven bilevel objective
+ one transparent GLS/MAP lower-level inverse problem
+ one formal CVaR tail-risk epigraph inside the upper-level objective
+ one deterministic initialization-and-exchange solver
+ one external audited comparison-class contract over 21 pre-registered
  baselines spanning 11 method families, with no surviving challenger after
  189 Holm-corrected paired comparisons.
```

## 2. Bilevel Optimization Problem

For a network with candidate sites `V`, `|V| = n`, and budget `k`, TRACE-BiOpt
chooses a fixed layout `S subset V`, `|S| = k`, by minimizing

```text
J(S) =
  hidden_huber_reconstruction_loss(S)
  + beta  * posterior_trace(S) / n
  + gamma * scenario_cvar_trace(S) / n
  + eta   * spatial_redundancy_penalty(S).
```

The four terms have distinct roles but are optimized jointly inside one design
problem:

- `hidden_huber_reconstruction_loss(S)`: validation hidden-state reconstruction
  loss under the transparent estimator;
- `posterior_trace(S)`: average hidden uncertainty certificate;
- `scenario_cvar_trace(S)`: coherent tail-risk penalty across traffic regimes
  under the paper's formal CVaR epigraph;
- `spatial_redundancy_penalty(S)`: discourages overly concentrated layouts.

This is a recoverability-driven network-design objective, not a coverage-only,
observability-only, or posterior-certificate-only criterion.

## 3. Lower-Level Transparent Reconstruction

For a binary sensor vector `s in {0,1}^n` with `1's = k`, let `M_s` denote the
observation operator. The lower-level reconstruction at time `t` solves the
regularized GLS/MAP inverse problem

```text
z_hat_t(s) = argmin_z
  0.5 ||M_s(z - x_t)||^2_{R^{-1}}
  + 0.5 lambda_Q (z - mu_t)' Q (z - mu_t)
  + 0.5 lambda_L z' L z
  + 0.5 epsilon ||z||_2^2.
```

For a fixed layout, this has the closed-form linear solution

```text
z_hat_t(s) = A(s)^{-1} b_t(s),
```

with

```text
A(s) = M_s' R^{-1} M_s + lambda_Q Q + lambda_L L + epsilon I,
b_t(s) = M_s' R^{-1} M_s x_t + lambda_Q Q mu_t.
```

This is the same lower-level estimator used in the paper theory, dominance
tables, and current-best evidence chain.

## 4. Deterministic Solver

TRACE-BiOpt uses one objective throughout initialization and exchange
refinement. The current implementation supports the following deterministic
pipeline.

### 4.1 Initialization

Two initialization routes are supported:

1. `trace_biopt_initializer=relaxed_rounding`
   - optimize a relaxed vector `s in [0,1]^n`, `sum_i s_i = k`;
   - use fractional observation weights in the same lower-level GLS/MAP model;
   - apply deterministic top-`k` rounding.
2. `trace_biopt_initializer=auto` (current evidence default)
   - smaller networks: objective-forward construction under the same `J(S)`;
   - larger networks: posterior-certificate warm start followed by `J(S)`
     refinement.

The initializer switch is based on network scale and solver tractability, not
on validation ranking among baseline methods.

### 4.2 Exchange Refinement

After initialization, TRACE-BiOpt repeatedly evaluates deterministic one-swap
moves under the same objective `J(S)` and accepts the best strict improvement.
On larger networks, remove/add candidates may be restricted to deterministic
active sets ranked by posterior uncertainty, scenario uncertainty, and spatial
recoverability. This is a solver acceleration, not a second method.

### 4.3 Stopping Rule

The solver stops when either:

- no searched one-exchange move improves `J(S)` by more than the declared
  tolerance `trace_biopt_min_improve`, or
- the declared exchange iteration cap is exhausted.

This implies a searched-neighborhood exchange certificate, not global optimality
over all `n choose k` layouts.

## 5. Exposed Hyperparameters

The paper-facing method contract uses the following parameter families.

- Objective weights:
  - `trace_biopt_beta`
  - `trace_biopt_gamma`
  - `trace_biopt_eta`
  - `trace_biopt_huber_delta`
- Relaxed initializer:
  - `trace_biopt_relax_iter`
  - `trace_biopt_relax_step`
  - `trace_biopt_relax_fd_eps`
  - `trace_biopt_relax_pool`
- Search budget:
  - `trace_biopt_forward_pool`
  - `trace_biopt_exchange_add_pool`
  - `trace_biopt_exchange_remove_pool`
  - `trace_biopt_exchange_iter`
  - `trace_biopt_objective_steps`
- Risk sample source:
  - `trace_biopt_risk_source in {val, train_val}`

Current paper evidence uses the explicit `auto` initializer configuration.
Relaxed-rounding-specific performance claims therefore still require a matching
multi-seed evidence run.

## 6. Current Code Entry Points

- Main implementation path:
  - `TRC-23-02333/transparent_estimator_eval.py --include-biopt`
- Layout label:
  - `trace_biopt`
- History artifact:
  - `trace_biopt_history.json`
- Theory contract:
  - `TRACE_BIOPT_THEORY.md`
- Current-best evidence contract:
  - `TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/trace_biopt_claim_contract.json`
- Refresh pipeline:
  - `scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## 7. Current Evidence State

The authoritative headline-evidence source is no longer the raw Stage15
directional contract. It is the hybrid current-best chain under

```text
TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/
```

whose aggregate claim status is currently:

```text
supported_submission_ready
```

The allowed aggregate wording is:

```text
Across the tested datasets and 10/20/30 percent budgets, TRACE-BiOpt has the
lowest mean held-out GLS/MAP MAE against the pre-registered non-BiOpt baseline set.
```

The current-best chain also supports the stronger corrected-comparison wording:

```text
Holm-corrected one-sided paired tests across all 189 current-best row-baseline
comparisons leave no statistically tied or significantly better pre-registered
challenger.
```

### 7.1 Current Main-Row Provenance

Current-best main rows are split into two evidence lanes:

- Stage16 calibrated rerun already promoted into the main chain:
  - PeMS7_1026 10%
  - PeMS7_1026 20%
  - PeMS7_1026 30%
  - PeMS7_228 10%
  - PeMS7_228 20%
  - PeMS7_228 30%
  - Seattle 20%
  - Seattle 30%
- Stage15 main evidence currently retained:
  - Seattle 10%

All nine current rows now satisfy submission-ready paired dominance in the
current-best claim contract.

Within that contract, 8/9 rows are already promoted from Stage16 calibrated
reruns, and Seattle 10% remains intentionally retained on the fail-closed
Stage15 lane.

Stated plainly for the paper-facing contract: supported_submission_ready still
holds, 8/9 rows are already promoted from Stage16 calibrated reruns, and only
Seattle 10% remains fail-closed on the retained Stage15 lane.

### 7.2 Remaining Non-Promoted Row

The only current-best main row that intentionally remains non-promoted is:

```text
Seattle 10%: fail_closed on Stage16 promotion, retained on the audited Stage15 path.
```

The current-best paper chain therefore no longer has an unfinished PeMS
promotion queue. The remaining non-promoted row is preserved because the
Seattle 10\% calibrated rerun did not satisfy the replacement gate, not because
the promotion workflow is incomplete.

### 7.3 Current Auxiliary Evidence Gates

The current-best paper-facing contract also includes two higher-strength
evidence summaries:

- Holm-corrected all-baseline screen:
  - `189/189` current-best row-baseline paired comparisons remain significant
    TRACE-BiOpt wins;
  - `0` statistically tied challengers;
  - `0` significantly better challengers.
- Bounded exact benchmark:
  - `27/27` deterministic 16-node audited subnetwork cases are exact hits with
    zero objective gap under row-wise current-best parameters.

In plain paper-facing language, that means 189/189 corrected comparisons remain
TRACE-BiOpt wins, 0 statistically tied challengers survive, and 0 significantly better challengers survive.

## 8. Claim Boundary

TRACE-BiOpt is allowed to claim:

- it is a recoverability-driven bilevel transportation network-design method
  for sparse traffic sensor siting;
- it optimizes one objective under one transparent GLS/MAP inverse problem;
- it achieves the lowest mean held-out GLS/MAP MAE against the pre-registered
  non-BiOpt registry on the tested dataset-budget regimes recorded in the
  current-best contract;
- after Holm correction across all current-best row-baseline paired tests, no
  pre-registered challenger remains statistically tied or significantly better
  on the tested dataset-budget regimes;
- the paper-facing rows satisfy the paired-dominance gate currently reported by
  that contract.

TRACE-BiOpt is not allowed to claim:

- global optimality over all size-`k` layouts;
- dominance over untested baselines;
- universal cross-network generalization;
- robustness outside the explicitly tested perturbation regimes;
- relaxed-rounding evidence claims without a matching multi-seed evidence run.

## 9. Relationship to the Manuscript

This method contract is the prose counterpart to four machine-checked evidence
artifacts:

- `TRACE_BIOPT_THEORY.md`: theory statement contract;
- `trace_biopt_claim_contract.json`: row-level and aggregate wording contract;
- `trace_biopt_current_best_provenance.csv`: row-level source policy;
- `table_trace_biopt_contribution_stack.tex`: reviewer-facing compression of
  formulation, algorithm, theory, evidence, and claim discipline.

The manuscript should remain synchronized with these artifacts. If current-best
evidence changes, this contract should be refreshed before claiming that the
paper source is final.
