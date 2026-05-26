# Project Research Summary

**Project:** TRACE-SL Transportation Research Part B Readiness
**Domain:** Robust bilevel reconstruction-aware traffic sensor layout optimization
**Researched:** 2026-05-26
**Confidence:** MEDIUM-HIGH

## Executive Summary

The v2.0 pivot is technically coherent and paper-strategic. Traffic sensor location literature already treats sparse sensor deployment as a budgeted network design problem, while Bayesian optimal experimental design and inverse-problem sensor placement provide the posterior-covariance, relaxation, and rounding language needed for a single method. The strongest direction is to define TRACE-BiOpt as one robust bilevel reconstruction-risk objective with a deterministic solver, not as a candidate pool.

The roadmap should start with a method lock: objective, lower-level MAP/GLS reconstruction, hyperparameters, solver steps, baseline registry, and claim boundaries. Implementation should then prove the pipeline can beat or tie the hardest known regimes before full Stage15 compute. The paper rewrite should wait until Stage15 and the theory/claim contracts say what can be claimed.

The main risk is circularity: if baselines enter the method as candidates, the reviewer critique returns. The second risk is overclaiming theory or dominance before full evidence exists. These are controllable through a spec-first phase, fail-closed evidence generation, and contracts that distinguish weak probes from full Stage15 evidence.

## Key Findings

### Recommended Stack

Use the existing Python/NumPy/SciPy/pandas stack and keep PyTorch optional. Local versions import successfully: NumPy 1.26.4, SciPy 1.17.1, pandas 3.0.1, scikit-learn 1.8.0, PyTorch 2.11.0+cu130. The method should be CPU-first and deterministic unless differentiable relaxation requires PyTorch.

**Core technologies:**
- NumPy/SciPy: lower MAP/GLS solves, objective evaluation, relaxation, rounding, exchange.
- pandas/CSV/JSON: Stage15 aggregation and paper-source artifacts.
- Existing TRACE-SL result structure: evidence compatibility and reproducibility.

### Expected Features

**Must have:**
- TRACE_BIOPT_SPEC.md with one objective and deterministic solver.
- Baseline registry that keeps comparators outside the method.
- TRACE-BiOpt implementation with relaxation, top-k rounding, and exchange refinement.
- Weak-regime probes on PeMS7_1026 10%, Seattle 10%, and PeMS7_228 10%.
- Objective and optimization diagnostic ledgers.

**Should have:**
- Full Stage15 over three datasets, three budgets, 10 splits, and all pre-registered baselines.
- Dominance report and best-baseline delta table.
- Theory and claim contracts.

**Defer:**
- Exact MIP/AMPL global bounds beyond small-instance diagnostics.
- Final TR Part B manuscript rewrite until method/evidence contracts are green.

### Architecture Approach

The architecture should be spec-first and artifact-first. A core `trace_biopt.py` module should own method logic; Stage15 scripts should own orchestration and baseline comparisons; paper-source generators should own dominance and claim artifacts. Probe outputs and full evidence outputs must be separated so single-run evidence is not accidentally reused as full paper support.

**Major components:**
1. Method spec and baseline registry - lock method identity and comparator set.
2. TRACE-BiOpt method module - compute one objective and one deterministic sensor layout.
3. Stage15 runner/evaluator - generate probe and full evidence.
4. Evidence summarizer - produce dominance, best-baseline, theory, and claim contracts.

### Critical Pitfalls

1. **Recreating pool selection** - prevent by freezing a baseline registry and banning baseline-derived candidates from TRACE-BiOpt.
2. **Post-hoc objective tuning** - prevent by validation-only tuning rules and parameter ledgers.
3. **Missing optimization diagnostics** - prevent by recording objective terms, descent curves, and exchange gaps.
4. **Overclaiming all-layout theory** - prevent by explicit bounded/block/effective-sample assumptions.
5. **Using probes as full evidence** - prevent by separate directories and fail-closed claim contracts.

## Implications for Roadmap

Based on research, suggested phase structure:

### Phase 17: TRACE-BiOpt Specification and Baseline Registry
**Rationale:** Method identity must be locked before implementation or evidence.
**Delivers:** `TRACE_BIOPT_SPEC.md`, baseline registry, parameter ledger, non-goals.
**Addresses:** Pool critique, post-hoc tuning risk.
**Avoids:** Baseline-in-pool circularity.

### Phase 18: TRACE-BiOpt Solver Implementation
**Rationale:** The method needs a runnable CPU-first deterministic implementation before experiments.
**Delivers:** `trace_biopt.py`, projection/rounding/exchange tests, objective diagnostics.
**Uses:** NumPy/SciPy, existing MAP/GLS utilities.
**Implements:** Single objective and deterministic solver.

### Phase 19: Weak-Regime Probe Gate
**Rationale:** PeMS7_1026 10% and Seattle 10% are the credibility bottlenecks.
**Delivers:** Probe runner, probe report, term diagnostics, gate decision.
**Addresses:** Scale risk and early method failure.

### Phase 20: Theory and Claim Contract Upgrade
**Rationale:** The stronger method story requires theorem assumptions and claim boundaries before paper rewrite.
**Delivers:** MAP stability, posterior Bayes risk, all-layout generalization, exchange certificate contracts.
**Uses:** Probe findings to avoid unsupported claims.

### Phase 21: Full Stage15 Dominance Evidence
**Rationale:** Paper-grade dominance claims require the full matrix, not probes.
**Delivers:** Three datasets x three budgets x 10 splits x all baselines, dominance table, best-baseline delta table.
**Addresses:** Final empirical support.

### Phase 22: TRACE-BiOpt Paper Handoff
**Rationale:** Manuscript rewriting should consume final contracts and evidence.
**Delivers:** revised paper plan, method narrative handoff, figure/table source inventory, claim wording map.
**Uses:** Stage15 and theory/claim artifacts.

### Phase Ordering Rationale

- Spec and registry first prevent circular method definition.
- Solver comes before probes so diagnostics are built into the method rather than retrofitted.
- Probes precede full Stage15 to manage compute and credibility risk.
- Theory/claim contracts precede paper rewrite to avoid unsupported prose.
- Full Stage15 must close before dominance wording.

### Research Flags

Phases likely needing deeper research during planning:
- **Phase 17:** exact objective assumptions, Huber/CVaR weighting, and baseline registry boundaries.
- **Phase 18:** efficient relaxed optimization and exchange caching.
- **Phase 20:** formal all-layout generalization under dependent traffic time series.

Phases with standard patterns:
- **Phase 21:** aggregation and fail-closed CSV/JSON summarization can follow existing paper-source conventions.
- **Phase 22:** paper handoff can follow existing v1.x claim/table contract patterns.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | Local imports work and existing project already uses this stack. |
| Features | HIGH | Directly grounded in user-approved suggestion and v1.x evidence gaps. |
| Architecture | MEDIUM-HIGH | Matches existing script/artifact style; exact module names may shift during phase planning. |
| Pitfalls | HIGH | Main pitfalls are already visible from current pool-selector critique and evidence history. |
| Theory | MEDIUM | Direction is sound; proof details need Phase 20 work, especially dependent validation samples. |

**Overall confidence:** MEDIUM-HIGH

### Gaps to Address

- **Objective weight policy:** Define validation-only tuning or a small fixed grid before evidence.
- **Gradient strategy:** Decide whether to hand-code relaxed gradients, use finite differences sparingly, or isolate PyTorch autograd.
- **Effective sample size:** Formalize block/effective-sample assumptions for traffic time-series generalization.
- **Probe pass criteria:** Define what result is enough to scale to full Stage15.

## Sources

### Primary / High Confidence
- Sayyady, Fathi, List, and Stone, "Locating Traffic Sensors on a Highway Network: Models and Algorithms", Transportation Research Record, 2013, https://doi.org/10.3141/2339-04.
- Yu, Zavala, and Anitescu, "A scalable design of experiments framework for optimal sensor placement", Journal of Process Control, 2018, https://doi.org/10.1016/j.jprocont.2017.03.011.
- Mehr and Horowitz, "A Submodular Approach for Optimal Sensor Placement in Traffic Networks", ACC 2018, https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/Mehr_Submodular_Optimal_Sensor_Placement_ACC2018.pdf.
- Nugroho et al., "Where Should Traffic Sensors Be Placed on Highways?", arXiv:2110.00912, https://arxiv.org/abs/2110.00912.
- Eswar, Rao, and Saibaba, "Bayesian D-Optimal Experimental Designs via Column Subset Selection", arXiv:2402.16000, https://arxiv.org/abs/2402.16000.

### Project-Specific
- `gpt_pro_suggestion_round1.md`.
- `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`.
- Existing `TRC-23-02333/trace_sl_results/paper_sources/` artifacts.

---
*Research completed: 2026-05-26*
*Ready for roadmap: yes*
