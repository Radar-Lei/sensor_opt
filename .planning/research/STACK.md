# Stack Research

**Domain:** Robust bilevel reconstruction-aware traffic sensor layout optimization
**Researched:** 2026-05-26
**Confidence:** MEDIUM-HIGH

## Recommended Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Python | current project runtime | Method implementation, experiment launchers, artifact generation | Existing TRACE-SL pipeline is Python-based and already contains Stage12 summaries, scripts, and paper-source generators. |
| NumPy | 1.26.4 local | Dense linear algebra inputs, masks, metrics, projections | Existing pipeline already uses NumPy heavily; TRACE-BiOpt objective and evaluation can reuse the same array contracts. |
| SciPy | 1.17.1 local | Cholesky solves, sparse matrices, constrained continuous optimization helpers | Project needs repeated SPD solves, simplex projection, and deterministic optimization utilities without adding heavy new dependencies. |
| pandas | 3.0.1 local | Stage15 result aggregation and dominance tables | Existing paper-source outputs are CSV-first; pandas is the natural bridge to new dominance and best-baseline artifacts. |
| scikit-learn | 1.8.0 local | Existing normalization and metrics support | Keep compatibility with current dataloader and result scripts. |
| PyTorch | 2.11.0+cu130 local | Optional differentiable relaxation experiments | Use only if needed for automatic differentiation of relaxed objectives; avoid coupling Stage15 evidence to GPU unless necessary. |

### Supporting Libraries

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| `scipy.linalg` / `scipy.sparse.linalg` | local SciPy | SPD solves, factorization reuse | Core lower-level MAP/GLS reconstruction and posterior metrics. |
| `scipy.optimize` | local SciPy | Projected or constrained relaxation prototypes | Use for deterministic baselines/prototypes; keep custom projection for reproducibility if SciPy behavior is too opaque. |
| `json` / `csv` | stdlib | Manifest and evidence contracts | Required for paper-source artifacts and fail-closed audit gates. |
| `argparse` | stdlib | Stage15 CLI surface | Match existing Stage scripts and DRY_RUN patterns. |

### Development Tools

| Tool | Purpose | Notes |
|------|---------|-------|
| `pytest` if available, otherwise script smoke checks | Fast verification | Project lacks formal test config; add focused tests around projection, objective monotonicity, and artifact schemas. |
| `gsd-sdk` | Planning state and commits | Continue using it for milestone/phase artifacts. |
| Existing Stage12 result directories | Baseline compatibility reference | Stage15 should not break paper-source conventions already used by v1.x. |

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| NumPy/SciPy deterministic optimizer | PyTorch autograd optimizer | Use PyTorch only if hand-derived gradients are too slow or fragile. |
| Cholesky/Woodbury direct solves | Generic black-box nonlinear solvers | Use black-box solvers only for diagnostic prototypes; paper method should remain transparent. |
| CSV/JSON paper-source artifacts | Pickle-only result blobs | Avoid pickle-only evidence because it weakens auditability and paper traceability. |
| Custom Stage15 scripts near existing TRACE-SL code | Separate package rewrite | Avoid a package rewrite until the method has evidence. |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| Baseline-in-pool selection | Recreates the reviewer critique that the method is a portfolio selector. | Pre-register baselines and keep them outside TRACE-BiOpt. |
| GPU-only method path | Stage15 has many small split/budget jobs; CPU deterministic solves are easier to audit and resume. | CPU-first NumPy/SciPy path, optional PyTorch acceleration later. |
| Untracked raw-data outputs | Violates existing reproducibility and raw-data hygiene constraints. | Curated aggregate CSV/JSON outputs under `trace_sl_results`. |
| Global exact MIP claim | Exact global solve is not the planned method and may be computationally infeasible. | State relaxation/rounding/exchange certificates and measured optimization gaps. |

## Stack Patterns by Variant

**If weak-regime probes are the current phase:**
- Use CPU-first deterministic objective evaluation.
- Reuse existing Stage12 data/evaluation loaders.
- Emit compact probe artifacts before full Stage15.

**If full Stage15 is launched:**
- Use resumable per-seed/per-budget output directories.
- Preserve max-jobs discipline from Stage12 unless compute constraints are updated.
- Fail closed when a dataset-budget-split is missing.

**If differentiable relaxation is needed:**
- Prefer a thin PyTorch module for the relaxed objective only.
- Convert final selected sets back to NumPy/CSV-compatible artifacts.

## Version Compatibility

| Package A | Compatible With | Notes |
|-----------|-----------------|-------|
| SciPy 1.17.1 | NumPy 1.26.4 | Local import succeeds; validate Cholesky and sparse solve APIs during Phase 18. |
| pandas 3.0.1 | CSV/JSON artifacts | Local import succeeds; beware changed defaults around nullable dtypes. |
| torch 2.11.0+cu130 | CUDA runtime | Available locally, but Stage15 should not require CUDA unless explicitly justified. |

## Sources

- `gpt_pro_suggestion_round1.md` - project-specific critique and TRACE-BiOpt proposal.
- Yu, Zavala, and Anitescu, "A scalable design of experiments framework for optimal sensor placement", Journal of Process Control, 2018, https://doi.org/10.1016/j.jprocont.2017.03.011 - supports continuous relaxation and sum-up rounding for sensor placement in inverse problems.
- Sayyady et al., "Locating Traffic Sensors on a Highway Network: Models and Algorithms", TRR, 2013, https://doi.org/10.3141/2339-04 - supports budgeted traffic sensor location framing.
- Mehr and Horowitz, "A Submodular Approach for Optimal Sensor Placement in Traffic Networks", ACC 2018, https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/Mehr_Submodular_Optimal_Sensor_Placement_ACC2018.pdf - supports submodular/greedy traffic baselines and approximation language.
- Nugroho et al., "Where Should Traffic Sensors Be Placed on Highways?", arXiv:2110.00912, https://arxiv.org/abs/2110.00912 - supports observability-plus-integer-programming baseline context.
- Eswar, Rao, and Saibaba, "Bayesian D-Optimal Experimental Designs via Column Subset Selection", arXiv:2402.16000, https://arxiv.org/abs/2402.16000 - supports Bayesian OED and QR/SVD/CSSP-style baselines.

---
*Stack research for: TRACE-BiOpt v2.0*
*Researched: 2026-05-26*
