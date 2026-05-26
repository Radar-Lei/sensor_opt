# Architecture Research

**Domain:** Robust bilevel reconstruction-aware traffic sensor layout optimization
**Researched:** 2026-05-26
**Confidence:** MEDIUM-HIGH

## Standard Architecture

### System Overview

```text
Specification Layer
  TRACE_BIOPT_SPEC.md
  baseline_registry.json/csv
  theory_contract.md/json

Method Layer
  trace_biopt.py
    - objective terms
    - lower MAP/GLS solve
    - continuous relaxation
    - top-k rounding
    - exchange refinement

Experiment Layer
  run_stage15_biopt.py
  evaluate_biopt_all_baselines.py
    - weak probes
    - full Stage15 matrix
    - DRY_RUN / resume / progress

Evidence Layer
  trace_sl_results/stage15_biopt/
    - per-split metrics
    - layout diagnostics
    - dominance tables
    - paper-source contracts
```

### Component Responsibilities

| Component | Responsibility | Typical Implementation |
|-----------|----------------|------------------------|
| Method spec | Defines the mathematical method and what is not part of it. | Markdown plus machine-readable parameter table. |
| Baseline registry | Freezes comparator names, parameters, and inclusion rules. | CSV/JSON in paper-source style. |
| TRACE-BiOpt objective | Computes one scalar objective for a sensor set or relaxed vector. | NumPy/SciPy module with explicit term breakdown. |
| MAP/GLS solver | Reconstructs full network state from selected sensors. | Existing solve utilities plus Cholesky/Woodbury caching. |
| Relaxation solver | Optimizes relaxed sensor weights on simplex/cardinality constraint. | Projected gradient, Frank-Wolfe, or SciPy-constrained prototype. |
| Rounding/refinement | Converts relaxed solution to k sensors and improves by exchange. | Top-k rounding plus deterministic one-swap/limited two-swap. |
| Stage15 runner | Executes probes/full matrix and resumes incomplete jobs. | CLI script mirroring existing Stage12 conventions. |
| Evidence summarizer | Builds dominance and best-baseline tables. | pandas CSV/JSON/MD generator with fail-closed coverage checks. |

## Recommended Project Structure

```text
TRC-23-02333/
├── trace_biopt.py                         # Core method implementation
├── run_stage15_biopt.py                   # Stage15 runner
├── evaluate_biopt_all_baselines.py        # Baseline/dominance evaluation
├── trace_sl_results/
│   ├── stage15_biopt_probes/              # Weak-regime probes
│   ├── stage15_biopt_full/                # Full matrix when launched
│   └── paper_sources/                     # Generated dominance/contracts
└── tests or focused test_*.py             # Projection/objective/artifact checks

.planning/
├── research/                              # This research
├── REQUIREMENTS.md                        # v2.0 requirements
└── ROADMAP.md                             # phases 17+
```

### Structure Rationale

- **Keep method near existing TRACE-SL scripts:** Existing imports assume `TRC-23-02333/` working directory.
- **Separate probes and full results:** Prevent single-seed feasibility artifacts from being mistaken for full evidence.
- **Paper-source outputs stay curated:** New tables should join existing `trace_sl_results/paper_sources/` conventions.

## Architectural Patterns

### Pattern 1: Spec-First Method Lock

**What:** Implement only what `TRACE_BIOPT_SPEC.md` defines; parameter changes require artifact updates.
**When to use:** Before any evidence generation.
**Trade-offs:** Slower upfront, but prevents post-hoc tuning accusations.

### Pattern 2: Objective Term Ledger

**What:** Every selected layout stores total objective plus term-level values: Huber validation risk, posterior trace, CVaR, spatial penalty.
**When to use:** Throughout probes and full Stage15.
**Trade-offs:** More output columns, but makes the method auditable and supports mechanism analysis.

### Pattern 3: Probe-to-Full Gate

**What:** Run weak regimes first and scale only if results justify it.
**When to use:** Stage15 compute planning.
**Trade-offs:** Adds one gate, but avoids expensive full runs for a method that fails the key credibility tests.

### Pattern 4: Fail-Closed Evidence Summary

**What:** Missing split/budget/baseline rows make the dominance artifact incomplete rather than silently ignored.
**When to use:** All paper-source evidence generation.
**Trade-offs:** Strict, but necessary for paper claims.

## Data Flow

### Method Flow

```text
Dataset split and budget
    -> training/validation/test arrays and graph priors
    -> relaxed TRACE-BiOpt objective
    -> continuous optimizer
    -> top-k layout
    -> deterministic exchange refinement
    -> selected layout + objective ledger
    -> held-out test evaluation
```

### Experiment Flow

```text
Stage15 CLI
    -> baseline registry
    -> TRACE-BiOpt run per dataset/budget/split
    -> external baseline evaluation
    -> per-split CSV/JSON
    -> aggregate dominance summary
    -> paper-source contracts
```

### Key Data Flows

1. **Specification to implementation:** Spec defines objective terms, hyperparameters, and allowed solver steps.
2. **Implementation to probes:** Probe outputs verify weak regimes before full compute.
3. **Full evidence to claims:** Dominance tables determine permitted paper wording.

## Scaling Considerations

| Scale | Architecture Adjustments |
|-------|--------------------------|
| Weak probes | Run serially or max-jobs=1; prioritize diagnostics. |
| Full Stage15 | Resume per split/budget; cache posterior/MAP computations; use fail-closed aggregation. |
| Optional extensions | Add AMPL/MIP bounds only for small instances or appendix validation. |

### Scaling Priorities

1. **First bottleneck:** repeated MAP/GLS solves during objective/exchange; reuse factorization and Woodbury caches.
2. **Second bottleneck:** exchange neighborhood evaluation; rank candidate swaps and cache term components.
3. **Third bottleneck:** full matrix orchestration; make per-job outputs resumable and machine-checkable.

## Anti-Patterns

### Anti-Pattern 1: Selector Disguised as Optimizer

**What people do:** Include baselines as candidate layouts inside the final method.
**Why wrong:** It makes dominance circular and weakens originality.
**Do this instead:** Keep TRACE-BiOpt generated layouts separate from pre-registered baselines.

### Anti-Pattern 2: Evidence Without Registry

**What people do:** Add or remove baselines after seeing results.
**Why wrong:** Reviewers can view this as cherry-picking.
**Do this instead:** Freeze baseline registry before weak probes.

### Anti-Pattern 3: Probe Artifacts as Full Evidence

**What people do:** Use one split or one budget as paper-wide support.
**Why wrong:** It overstates evidence and repeats prior caveat problems.
**Do this instead:** Label probes as feasibility only until full Stage15 closes.

## Integration Points

| Boundary | Communication | Notes |
|----------|---------------|-------|
| Existing Stage12 code -> TRACE-BiOpt | Direct Python imports where stable | Avoid changing Stage12 outputs unless needed. |
| TRACE-BiOpt -> result artifacts | CSV/JSON/MD | Match existing paper-source schema style. |
| Evidence artifacts -> paper writing | Claim/theory contracts | Later manuscript should consume contracts, not ad hoc numbers. |

## Sources

- `gpt_pro_suggestion_round1.md` - method architecture and Stage15 proposal.
- Yu et al. 2018, https://doi.org/10.1016/j.jprocont.2017.03.011 - bilevel/mixed-integer nature of sensor placement and relaxation/rounding.
- Mehr and Horowitz 2018, https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/Mehr_Submodular_Optimal_Sensor_Placement_ACC2018.pdf - traffic sensor placement with submodular greedy baselines.
- Nugroho et al. 2022, https://arxiv.org/abs/2110.00912 - observability and integer programming for traffic sensors.
- Eswar et al. 2025 version, https://arxiv.org/abs/2402.16000 - QR/SVD/CSSP Bayesian OED baseline family.

---
*Architecture research for: TRACE-BiOpt v2.0*
*Researched: 2026-05-26*
