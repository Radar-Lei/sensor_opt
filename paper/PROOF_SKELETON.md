# TRACE-BiOpt Proof Skeleton

## Dependency DAG

- Definition: budgeted hidden-network reconstruction design -> T1/T3.
- T1 MAP closed form/stability -> lower-level transparency and objective evaluation.
- T2 posterior trace Bayes risk -> posterior-trace interpretation.
- T3 uniform validation generalization -> validation-risk scope statement.
- T4 exchange certificate -> deterministic solver stationarity statement.
- T6 CVaR epigraph proposition -> coherent tail-risk interpretation and non-claims.

## Theorem Obligations

- T1 `thm:map-stability`: MAP closed form and stability; guard=ridge_or_precision_positive_definite.
- T2 `thm:trace-risk`: Posterior trace as Bayes squared reconstruction risk; guard=singular_covariance_excluded.
- T3 `thm:uniform-layout`: Uniform validation generalization over size-$k$ layouts; guard=temporal_dependence_qualified.
- T4 `thm:exchange`: TRACE-BiOpt exchange certificate; guard=restricted_active_set_not_overclaimed.

## Counterexample Pass

- Singular posterior covariance: excluded by positive definite Sigma and R_S in T2.
- Semidefinite reconstruction precision: excluded by positive definite ridge/precision condition in T1.
- Temporally dependent validation samples: qualified by independent blocks or effective sample size in T3.
- Restricted exchange active set: T4 is explicitly scoped to N_1^search and does not claim unevaluated swaps.
