# Phase 2: Formulation and Theory Bridge - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-22
**Phase:** 2-Formulation and Theory Bridge
**Areas discussed:** Formalization target, RCSS surrogate definition, posterior-error derivation, algorithm analysis, TR Part B extension boundary
**Mode:** Auto-selected under `/gsd-autonomous --only 2`; no user prompts were issued.

---

## Formalization Target

| Option | Description | Selected |
|--------|-------------|----------|
| Heuristic-first description | Describe RCSS mainly as an empirical candidate-pool and validation-search procedure | |
| Reconstruction-aware design formulation | Define budgeted sensor-set optimization for hidden-node reconstruction with transparent reconstruction model | ✓ |
| Full stochastic programming rewrite | Recast the whole project as a new stochastic/bilevel optimization model | |

**User's choice:** Auto-selected reconstruction-aware design formulation.
**Notes:** Matches Phase 1 decision to preserve strong method framing and avoid ad hoc heuristic positioning.

---

## RCSS Surrogate Definition

| Option | Description | Selected |
|--------|-------------|----------|
| Manual coefficient story | Present fixed RCSS weights as the main contribution | |
| Predeclared portfolio with inner validation | Define fixed candidate generation, fixed diagnostic terms, and fixed inner-validation weight selection | ✓ |
| Post-hoc best method per budget | Pick whichever layout wins after seeing held-out tests | |

**User's choice:** Auto-selected predeclared portfolio with inner validation.
**Notes:** Avoids cherry-picking and aligns with Stage 11 auto-weight implementation.

---

## Posterior-Error Derivation

| Option | Description | Selected |
|--------|-------------|----------|
| No theory | Rely only on certificate-error correlations | |
| Linear-Gaussian GLS/MAP bridge | Derive posterior covariance trace as expected hidden-state squared-error proxy under idealized assumptions | ✓ |
| Broad certified guarantee | Claim formal certification for arbitrary traffic data and MAE | |

**User's choice:** Auto-selected linear-Gaussian GLS/MAP bridge.
**Notes:** Supports THEORY-03 and preserves “certificate-guided” wording without overclaiming.

---

## Algorithm Analysis

| Option | Description | Selected |
|--------|-------------|----------|
| Omit complexity | Keep algorithm text purely descriptive | |
| Fixed-candidate local-search analysis | State dense reconstruction solve cost, starts/swap iterations, candidate universe size, and one-swap local optimality | ✓ |
| New scalable solver analysis | Analyze sparse/rank-update solvers not implemented yet | |

**User's choice:** Auto-selected fixed-candidate local-search analysis.
**Notes:** Matches current implementation and flags dense-solver scaling as limitation.

---

## TR Part B Extension Boundary

| Option | Description | Selected |
|--------|-------------|----------|
| Ignore TR Part B theory needs | Only target Transportation Science narrative | |
| Explicit optional theory-gap note | List monotonicity, submodularity-like, approximation, and stability analyses as future TR Part B needs | ✓ |
| Attempt full TR Part B proof package now | Expand Phase 2 beyond current milestone scope | |

**User's choice:** Auto-selected explicit optional theory-gap note.
**Notes:** Satisfies THEORY-06 while keeping advanced theory as v2 unless narrowly provable.

---

## Claude's Discretion

- The planner may decide whether the main output is a phase-local theory artifact, edits to `NARRATIVE_REPORT.md`/`README.md`, or both, as long as downstream paper-writing receives manuscript-ready method/theory text.
- The planner should avoid unnecessary algorithm-code changes unless required to align documentation with implemented behavior.

## Deferred Ideas

- New baselines: Phase 3.
- Core evidence/statistical regeneration: Phase 4.
- Robustness and generality experiments: Phase 5.
- Broad approximation/submodularity/stability theory: v2/TR Part B extension unless a narrow correct statement is available now.
