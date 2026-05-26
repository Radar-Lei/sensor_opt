# Feature Research

**Domain:** Robust bilevel reconstruction-aware traffic sensor layout optimization
**Researched:** 2026-05-26
**Confidence:** MEDIUM-HIGH

## Feature Landscape

### Table Stakes

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Formal TRACE-BiOpt specification | Needed to prove this is one method, not a pool selector. | MEDIUM | Include objective, lower MAP problem, hyperparameters, solver, stopping rule, outputs, and non-goals. |
| Single-method implementation | Main contribution must optimize one objective directly. | HIGH | Implement continuous relaxation, top-k rounding, and exchange refinement as one pipeline. |
| Baseline pre-registration | Strong claims require a fixed comparison set before evidence is generated. | MEDIUM | Baselines must never enter the main method. |
| Weak-regime probe suite | Avoid wasting full Stage15 compute before the hard cases look promising. | MEDIUM | Probe PeMS7_1026 10%, Seattle 10%, PeMS7_228 10%. |
| Stage15 full experiment runner | Needed for paper-grade dominance evidence. | HIGH | Three networks, 10/20/30% budgets, 10 splits, all baselines. |
| Dominance and best-baseline artifacts | Paper claim must compare TRACE-BiOpt against the best pre-registered competitor. | MEDIUM | Generate CSV/JSON/MD with delta, p-value, win count, and baseline name. |
| Theory and claim contracts | Prevent overclaiming when method changes. | MEDIUM | Route each theorem/claim to assumptions, proof status, and evidence. |

### Differentiators

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Robust bilevel objective | Positions contribution as recoverability-driven network design rather than heuristic selection. | HIGH | Combine Huber hidden validation risk, posterior trace, CVaR, and spatial regularization. |
| All-layout validation generalization statement | Stronger than finite candidate-pool validation bounds. | MEDIUM | Requires careful bounded/block/effective-sample-size assumptions. |
| Exchange gap certificate | Makes heuristic solver auditable and optimization-aware. | MEDIUM | Emit one-swap or p-swap gap curves and terminal certificate. |
| Objective descent diagnostics | Separates solver behavior from lucky validation selection. | MEDIUM | Plot/record relaxed objective, rounded objective, exchange improvements. |
| Sensor-map and error-map diagnostics | Mechanism analysis for TR Part B reviewers. | MEDIUM | Use after evidence exists; avoid replacing quantitative dominance. |

### Anti-Features

| Feature | Why Requested | Why Problematic | Alternative |
|---------|---------------|-----------------|-------------|
| Put every strong baseline into the candidate pool | Maximizes empirical chance of winning. | Makes method look like a selector and weakens originality. | Keep baselines external and optimize one TRACE-BiOpt objective. |
| Claim global optimality | Sounds strong. | Not supported by relaxation/rounding/exchange unless exact MIP is solved. | Claim exchange stationarity, measured gap, and empirical dominance. |
| Launch full Stage15 immediately | Faster path to a full table if it works. | Expensive and may fail on known weak regimes. | Probe weak regimes first, then scale. |
| Rewrite the manuscript before evidence | Produces visible progress. | Locks prose before the method/evidence truth is known. | Generate method/evidence/theory contracts first. |

## Feature Dependencies

```text
TRACE_BIOPT_SPEC
    -> single-method implementation
        -> weak-regime probes
            -> full Stage15 runner
                -> dominance artifacts
                    -> revised TR Part B paper story

Baseline pre-registration
    -> weak-regime probes
    -> full Stage15 runner
    -> dominance artifacts

Theory contract
    -> claim contract
    -> revised paper story
```

### Dependency Notes

- **Specification before implementation:** The solver must be locked before evidence to avoid post-hoc method drift.
- **Baseline registry before dominance table:** The claim is only meaningful against pre-registered baselines.
- **Probe before full Stage15:** PeMS7_1026 10% and Seattle 10% decide whether the pivot is viable.
- **Contracts before prose:** Claim and theory contracts determine what the manuscript is allowed to say.

## MVP Definition

### Launch With

- [ ] TRACE-BiOpt spec with explicit objective, lower MAP solve, and deterministic solver.
- [ ] Baseline registry excluding all baselines from the method itself.
- [ ] Prototype TRACE-BiOpt runner that emits selected layouts, objective diagnostics, and held-out metrics.
- [ ] Weak-regime probe report over PeMS7_1026 10%, Seattle 10%, and PeMS7_228 10%.

### Add After Validation

- [ ] Full Stage15 matrix over all datasets, budgets, and splits.
- [ ] Dominance and best-baseline delta paper-source tables.
- [ ] Theory and claim contracts aligned with observed evidence.
- [ ] Revised paper plan that demotes TRACE-SL pool selection.

### Future Consideration

- [ ] Exact or AMPL-backed MIP bounds for small networks.
- [ ] Multi-objective Pareto visualizations beyond the main TRACE-BiOpt objective.
- [ ] Additional robustness perturbation Stage15 variants if the main evidence is strong.

## Feature Prioritization Matrix

| Feature | User Value | Implementation Cost | Priority |
|---------|------------|---------------------|----------|
| TRACE-BiOpt spec | HIGH | MEDIUM | P1 |
| Baseline pre-registration | HIGH | MEDIUM | P1 |
| Single-method implementation | HIGH | HIGH | P1 |
| Weak-regime probes | HIGH | MEDIUM | P1 |
| Full Stage15 runner | HIGH | HIGH | P2 |
| Dominance artifacts | HIGH | MEDIUM | P2 |
| Theory contract | HIGH | MEDIUM | P2 |
| Paper rewrite | HIGH | HIGH | P3 for this milestone unless evidence passes early |

## Competitor / Baseline Analysis

| Feature | Standard Baselines | Current TRACE-SL | TRACE-BiOpt Approach |
|---------|--------------------|------------------|----------------------|
| Sensor objective | Coverage, observability, A/D-optimality, graph sampling, QR/POD, random variants | Candidate generation plus validation selection/swap | One robust reconstruction-risk objective |
| Solver | Greedy, QR/SVD, local search, MIP heuristics | Candidate pool and validation-swap | Relaxation, top-k rounding, deterministic exchange |
| Theory | Observability, submodularity, OED covariance, finite candidate bounds | Posterior trace bridge and finite-candidate validation | MAP stability, posterior Bayes risk, all-layout generalization, exchange certificate |
| Evidence claim | Per-baseline comparison | Best among selected candidate sources can look circular | Best pre-registered baseline comparison without using baselines in method |

## Sources

- `gpt_pro_suggestion_round1.md` - concrete v2.0 feature proposal.
- Sayyady et al. 2013, TRR, https://doi.org/10.3141/2339-04 - budgeted traffic sensor location and p-location framing.
- Mehr and Horowitz 2018, ACC, https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/Mehr_Submodular_Optimal_Sensor_Placement_ACC2018.pdf - traffic sensor placement baselines with submodular greedy guarantees.
- Yu et al. 2018, Journal of Process Control, https://doi.org/10.1016/j.jprocont.2017.03.011 - Bayesian inverse-problem sensor placement, relaxation, and rounding.
- Nugroho et al. 2022, arXiv:2110.00912, https://arxiv.org/abs/2110.00912 - traffic observability and integer-programming context.
- Eswar et al. 2025 version, arXiv:2402.16000, https://arxiv.org/abs/2402.16000 - Bayesian D-optimal sensor selection via SVD/QR/CSSP.

---
*Feature research for: TRACE-BiOpt v2.0*
*Researched: 2026-05-26*
