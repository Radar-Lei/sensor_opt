# TRACE-BiOpt Theory Contract

This contract records the theory package needed to support the TR-B version of
TRACE-BiOpt. It is written as a paper-facing checklist: each statement must be
proved in the manuscript or explicitly routed to an appendix before any
submission-ready claim is made.

## Scope

TRACE-BiOpt solves a sparse traffic sensor siting problem by directly
optimizing a recoverability-driven bilevel stochastic network-design objective.
The lower level is a transparent GLS/MAP reconstruction problem; the upper
level chooses a size-`k` layout with one robust empirical reconstruction-risk
objective over hidden-state Huber loss, posterior uncertainty, scenario
tail-risk, and spatial redundancy.

The theory supports a principled network design method. It does not claim exact
global optimality of the implemented discrete solver, and it does not claim
dominance over baselines that were not pre-registered and evaluated.

## Notation

- `V = {1, ..., n}` is the set of candidate sensor nodes.
- `S subset V`, `|S| = k`, is a sensor layout.
- `M_S` is the diagonal/selection observation operator for `S`.
- `x_t` is the full traffic state at time `t`.
- `mu_t` is the historical or time-of-day prior mean.
- `Q` is a positive semidefinite prior precision.
- `L` is the graph Laplacian.
- `R` is the observation noise covariance.
- `A(S) = M_S' R^{-1} M_S + lambda_Q Q + lambda_L L + epsilon I`.

The `epsilon I` ridge term may be stated as a numerical/stability regularizer
when `Q + L` is only semidefinite.

## Theorem T1: Lower-Level MAP Closed Form and Stability

For a fixed layout `S`, define

```text
z_hat_t(S) = argmin_z 0.5 ||M_S(z - x_t)||^2_{R^{-1}}
                  + 0.5 lambda_Q (z - mu_t)' Q (z - mu_t)
                  + 0.5 lambda_L z' L z
                  + 0.5 epsilon ||z||_2^2.
```

If `R` is positive definite and
`lambda_Q Q + lambda_L L + epsilon I` is positive definite, then the lower
problem is strongly convex and has the unique solution

```text
z_hat_t(S) = A(S)^{-1} b_t(S),
```

where

```text
b_t(S) = M_S' R^{-1} M_S x_t + lambda_Q Q mu_t.
```

Moreover, for any two observations `x_t, x'_t` observed on `S`,

```text
||z_hat_t(S) - z_hat'_t(S)||_2
  <= ||A(S)^{-1} M_S' R^{-1} M_S||_2 ||x_t - x'_t||_2.
```

This establishes TRACE-BiOpt as a stable inverse-problem method rather than a
black-box layout selector.

## Theorem T2: Posterior Trace as Bayes Squared Reconstruction Risk

Under a linear-Gaussian model with positive definite `Sigma` and `R_S`,

```text
x ~ N(mu, Sigma),     y_S = M_S x + eps,     eps ~ N(0, R_S),
```

the posterior covariance is

```text
Sigma_{post}(S) = (Sigma^{-1} + M_S' R_S^{-1} M_S)^{-1}.
```

For the hidden node set `H = V \\ S`,

```text
E ||x_H - E[x_H | y_S]||_2^2 = tr(Sigma_{H|S}).
```

Thus the posterior trace term in `J(S)` is a Bayes-risk certificate, not an
arbitrary proxy. In the implementation, `posterior_trace_per_node` is the
normalized computable version of this certificate.

## Theorem T3: Uniform Generalization Over All Size-k Layouts

Let

```text
S_k = {S subset V : |S| = k}
```

and let `ell_t(S)` be the bounded validation reconstruction loss for layout
`S`, with `0 <= ell_t(S) <= B`. For `n_v` independent validation samples, with
probability at least `1 - delta`,

```text
sup_{S in S_k} |R(S) - R_hat_v(S)|
  <= B sqrt((k log(en/k) + log(2/delta)) / (2 n_v)).
```

If the implemented solver returns `S_hat` satisfying

```text
R_hat_v(S_hat) <= min_{S in S_k} R_hat_v(S) + epsilon_opt,
```

then

```text
R(S_hat) <= min_{S in S_k} R(S)
          + 2 B sqrt((k log(en/k) + log(2/delta)) / (2 n_v))
          + epsilon_opt.
```

For temporally dependent traffic data, the same statement must be written with
independent validation blocks or an effective sample size `n_eff` under mixing
assumptions. This theorem upgrades the prior finite-candidate validation
argument to all budget-feasible layouts.

## Theorem T4: TRACE-BiOpt Exchange Certificate

Define the TRACE-BiOpt objective

```text
J(S) = empirical_hidden_huber_loss(S)
     + beta posterior_trace(S) / n
     + gamma CVaR_alpha(scenario_trace(S)) / n
     + eta spatial_penalty(S).
```

For the deterministic searched one-exchange active-set neighborhood

```text
N_1^search(S) = {S \\ {i} union {j}: i in R(S), j in A(S)},
```

define the exchange gap

```text
G_1^search(S) = J(S) - min_{S' in N_1^search(S)} J(S').
```

When the solver stops because no improving one-exchange move exists,
`G_1^search(S_hat) = 0` up to the numerical tolerance
`trace_biopt_min_improve`. Therefore `S_hat` is a one-exchange stationary
point for the single TRACE-BiOpt objective over the deterministic searched
active-set neighborhood.

The certificate is conditional on the declared solver budget. If an evidence
run uses a restricted active set, `N_1(S)` is the searched deterministic
one-exchange neighborhood, not the complete `k(n-k)` swap set. The run manifest
must therefore report the forward pool, exchange add pool, exchange remove
pool, and exchange iteration cap.

If a future two-swap or beam variant is added, it must expose the corresponding
`G_p(S)` certificate and keep the same `J(S)` objective.

## Proposition T5: Continuous-Relaxation Consistency

Let `s_tilde in [0,1]^n` satisfy `sum_i s_tilde_i = k`, and let
`S^(0) = TopK(s_tilde)` be the deterministic top-k rounding of that capped
simplex iterate. Then `S^(0)` is budget-feasible and the subsequent
TRACE-BiOpt exchange phase continues under the same discrete objective `J(S)`
used by the forward and posterior-certificate warm starts. The continuous
relaxation therefore does not define a second selection rule; it is only a
warm-start construction for the same bilevel design problem.

This supports the paper method narrative requested for TRACE-BiOpt, but the
current multi-seed dominance evidence was generated with the explicit `auto`
initializer configuration. Relaxed-rounding-specific empirical claims still
require a matching evidence run.

## Proposition T6: CVaR Tail-Risk Epigraph and Interpretation

Let `ell_t(S)` denote the sampled scenario reconstruction-risk losses used
inside TRACE-BiOpt's upper-level objective, and let

```text
Phi_tail(S) = CVaR_alpha({ell_t(S)}_t).
```

Then the empirical tail-risk term admits the equivalent epigraph form

```text
Phi_tail(S)
  = min_tau
      tau
      + (1 / ((1-alpha) |T_v|))
        sum_t (ell_t(S) - tau)_+.
```

Any minimizer `tau*` is an empirical `VaR_alpha` threshold, and the minimized
value equals the sampled upper-tail average up to the usual quantile
interpolation. Consequently, when TRACE-BiOpt lowers `Phi_tail(S)`, it lowers
a coherent tail-risk penalty on deployment-time reconstruction uncertainty
rather than only an average-risk proxy.

## Evidence Gate

The theory package supports the paper-facing method claim only when paired with
the current-best held-out evidence chain under

```text
TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/
```

Current authoritative evidence:

- `trace_biopt_claim_contract.json` reports aggregate status
  `supported_submission_ready`.
- All `9/9` current-best dataset-budget rows satisfy the submission-ready
  paired-dominance gate against the `21` pre-registered non-BiOpt baselines.
- `8/9` current-best rows are Stage16 calibrated promotions:
  - PeMS7_1026 10/20/30
  - PeMS7_228 10/20/30
  - Seattle 20/30
- The only intentionally retained non-promoted row is:
  - Seattle 10%, kept on the audited Stage15 main path because the Stage16
    calibrated rerun is `fail_closed`, not because the workflow is incomplete.
- `trace_biopt_significance_posture_detail.csv` shows that Holm-corrected
  one-sided paired tests across all `189` current-best row-baseline
  comparisons leave zero statistically tied or significantly better
  pre-registered challengers.
- `trace_biopt_exact_subnetwork_summary.csv` and
  `trace_biopt_exact_subnetwork_detail.csv` show `27/27` exact hits on audited
  deterministic 16-node subnetworks under row-wise current-best parameters.

Allowed paper-facing aggregate wording:

```text
TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against the
pre-registered non-BiOpt baseline registry on all tested dataset-budget rows,
no pre-registered challenger remains statistically tied or better after
Holm-corrected paired tests over the current-best comparison family, and the
implemented solver exact-hits the audited 16-node subnetwork benchmarks.
```

Forbidden upgrades remain:

- exact global optimality over all size-`k` layouts;
- dominance over untested baselines;
- universal cross-network generalization;
- robustness claims outside the explicitly tested perturbation lanes;
- promotion of Seattle 10% beyond its retained Stage15 fail-closed status.
