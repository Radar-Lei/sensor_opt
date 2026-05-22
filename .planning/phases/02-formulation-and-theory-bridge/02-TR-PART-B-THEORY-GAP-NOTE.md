# TR Part B Theory-Gap Note

**Date**: 2026-05-22  
**Project**: TRACE-SL  
**Purpose**: Preserve optional TR Part B extension requirements for THEORY-06 while keeping Phase 2 focused on Transportation Science-ready formulation and theory-bridge documentation.

## Purpose

This note identifies the additional mathematical material that would be needed if TRACE-SL were later repositioned from the current Transportation Science framing toward a more theory-heavy TR Part B: Methodological submission. It implements THEORY-06, D-13, and D-14 by separating useful extension opportunities from the deliverables completed in Phase 2.

The note supports strong TRACE-SL claims by showing where the current reconstruction-aware sensor-set design formulation can grow; it is not a reason to weaken the current paper framing into a generic heuristic study.

## Core Boundary

Phase 2 establishes TRACE-SL as budgeted reconstruction-aware sensor-set design with a transparent GLS/MAP or GSP reconstruction map, validation-calibrated RCSS selection, held-out test evaluation, and posterior-certificate-aware diagnostics. The current theory bridge justifies posterior covariance trace as an expected squared hidden-state error proxy only under the linear-Gaussian squared-error identity.

This boundary means Phase 2 does **not** assign new experiments, baseline implementation, robustness testing, split-evidence regeneration, or final manuscript-package writing. Those remain downstream phase responsibilities. Broad mathematical guarantees beyond the scoped posterior-error bridge are extension material.

## Transportation Science Framing

For Transportation Science, the defensible core is a planning/design contribution: TRACE-SL chooses a sparse fixed sensor set for hidden-network reconstruction under a deployment budget, using train-derived reconstruction ingredients, validation-based layout selection, and held-out test evidence. The contribution can remain strong because the formulation, RCSS surrogate, offline planning interpretation, and certificate-guided diagnostics clarify why the method is more than post-hoc candidate tuning.

The correct terminology remains **certificate-guided** or **posterior-certificate-aware** unless a future result is explicitly scoped to the linear-Gaussian squared-error identity. Current posterior trace, condition number, scenario CVaR trace, logdet, and coverage quantities are transparent diagnostics and surrogate terms, not broad formal certificates of TRACE-SL optimality.

## TR Part B Framing

A TR Part B submission would likely need a sharper mathematical object and stronger algorithmic analysis than the current Transportation Science package requires. The natural route is not to abandon TRACE-SL, but to narrow a theorem-ready objective and prove properties for that restricted setting while keeping empirical validation/test evidence separate.

Potential TR Part B framing options include:

- a restricted linear-Gaussian A-optimal sensor design problem tied directly to posterior covariance trace;
- a surrogate-loss analysis showing when validation-calibrated RCSS approximates or upper-bounds a reconstruction-risk target;
- a stochastic or bilevel optimization formulation that models train-derived priors, validation selection, and deployment evaluation as distinct levels.

## What Would Be Needed for TR Part B

A future TR Part B-style extension would need some combination of the following additional material:

- **Monotonicity:** State and prove when adding observed sensors cannot increase the posterior covariance trace or the restricted reconstruction-risk surrogate, including the exact assumptions on precision regularization and observation weights.
- **Approximate submodularity:** Establish exact or approximate diminishing-returns behavior for a restricted posterior-trace objective, or explain why validation MAE, scenario CVaR trace, condition number, and coverage terms break classical submodularity.
- **Approximation guarantees:** If monotonicity and approximate submodularity hold for a narrowed objective, derive a greedy or local-search approximation guarantee; if they do not, state a weaker fixed-candidate local-optimality result.
- **Stability under covariance perturbation:** Bound how the selected layout or posterior-trace ranking changes when train-derived covariance or precision estimates are perturbed by sampling noise, shrinkage, temporal shift, or regularization choices.
- **Stronger stochastic or bilevel optimization analysis:** Formalize the separation between train-derived reconstruction ingredients, validation layout selection, and held-out deployment evaluation through a stochastic programming or bilevel model, with assumptions clear enough to analyze generalization or selection bias.

These items should be treated as optional extension work. They should not be written as already-proved TRACE-SL guarantees in the Transportation Science manuscript.

## Deferred v2

D-14 is the controlling boundary: broad approximation, submodularity, and stability proofs are deferred v2 work unless a future phase explicitly scopes a narrow theorem that is correct under the implemented linear-Gaussian squared-error setting.

Deferred v2 topics include:

- surrogate-error bounds beyond the posterior covariance trace identity;
- monotonicity, approximate submodularity, stability, or approximation-style guarantees for a restricted TRACE-SL objective;
- bilevel or stochastic programming theory that turns RCSS selection into a stronger optimization-theory contribution;
- scaling-theory work tied to sparse, Cholesky, rank-update, or low-rank posterior solvers that do not yet replace the current dense implementation.

## Suggested Paper Boundary Wording

> Our current contribution targets Transportation Science: a transparent reconstruction-aware sensor placement formulation, RCSS surrogate, posterior-certificate-aware diagnostics, and held-out empirical evidence for sparse fixed layouts. A more mathematical TR Part B extension would require additional monotonicity, approximate-submodularity, approximation, stability, or stochastic/bilevel analysis for a narrowed objective; these broader guarantees are deferred v2 work rather than assumptions of the present method.

## Self-Check

- [x] THEORY-06 is covered by explicit TR Part B extension needs.
- [x] D-13 is covered by naming monotonicity, approximate submodularity, approximation guarantees, stability under covariance perturbation, and stronger stochastic or bilevel optimization analysis.
- [x] D-14 is covered by marking broad approximation, submodularity, and stability proofs as deferred v2 unless a future narrow theorem is scoped.
- [x] Transportation Science remains the primary framing.
- [x] No new experiments, baseline implementation, robustness tests, or manuscript-package work are assigned to Phase 2.
