# Pitfalls Research

**Domain:** Robust bilevel reconstruction-aware traffic sensor layout optimization
**Researched:** 2026-05-26
**Confidence:** MEDIUM-HIGH

## Critical Pitfalls

### Pitfall 1: Recreating the Pool Critique

**What goes wrong:**
TRACE-BiOpt quietly imports baseline-generated layouts or candidate pools, so the method still looks like a portfolio selector.

**Why it happens:**
Including strong baselines improves empirical performance quickly, especially in weak regimes.

**How to avoid:**
Write a baseline registry and a method spec before implementation. The TRACE-BiOpt runner may compare against baselines but must not use their selected layouts as candidates.

**Warning signs:**
Code paths named "candidate_source", "selected_source", or "best_baseline" appear inside the main method selection logic.

**Phase to address:**
Phase 17.

---

### Pitfall 2: Post-Hoc Objective Tuning

**What goes wrong:**
Weights for Huber risk, posterior trace, CVaR, or spatial regularization are tuned after seeing test results.

**Why it happens:**
The objective has multiple terms and weak regimes will tempt reactive changes.

**How to avoid:**
Use validation-only tuning rules, frozen grids, and a parameter ledger. Test data should only appear in final evaluation.

**Warning signs:**
Parameter changes are not recorded; a single "best" config appears without search trace; test MAE is referenced in tuning notes.

**Phase to address:**
Phases 17-18.

---

### Pitfall 3: Optimization Gap Hidden by Empirical Wins

**What goes wrong:**
TRACE-BiOpt wins on mean MAE but lacks descent curves, exchange gaps, or solver termination evidence.

**Why it happens:**
Performance tables are easier to generate than optimization diagnostics.

**How to avoid:**
Emit objective ledger, descent history, rounded objective, exchange improvements, and terminal one-swap gap for every run.

**Warning signs:**
Selected layouts have no objective term values or only final MAE metrics.

**Phase to address:**
Phase 18 and Phase 19.

---

### Pitfall 4: Overclaiming All-Layout Theory

**What goes wrong:**
The paper states a uniform generalization theorem without bounded loss, independence/blocking, or optimization-gap assumptions.

**Why it happens:**
The all-layout bound is attractive and stronger than candidate-pool bounds.

**How to avoid:**
State assumptions explicitly: bounded/clipped loss, independent validation blocks or effective sample size, fixed budget k, and epsilon-optimization gap.

**Warning signs:**
The theory contract lacks assumption columns or treats time-series samples as IID without caveat.

**Phase to address:**
Phase 20.

---

### Pitfall 5: Probe Evidence Used as Full Evidence

**What goes wrong:**
Weak-regime probes are written as if they establish all dataset-budget dominance.

**Why it happens:**
Positive probe results are tempting to use immediately in prose.

**How to avoid:**
Mark probe artifacts as feasibility/probe only and require a full Stage15 gate before dominance claims.

**Warning signs:**
Paper-source claim contract cites `stage15_biopt_probes` for global or full-matrix claims.

**Phase to address:**
Phase 19 and Phase 21.

## Technical Debt Patterns

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
|----------|-------------------|----------------|-----------------|
| Hard-code weak-regime datasets in method code | Fast probes | Full Stage15 becomes brittle | Acceptable only in runner defaults, not method module. |
| Store only final layout IDs | Smaller artifacts | Cannot audit objective or exchange behavior | Never for evidence runs. |
| Reuse Stage12 candidate labels for TRACE-BiOpt | Less scripting | Confuses method identity | Avoid; use explicit `trace_biopt` method label. |
| Skip tests for projection/top-k/exchange | Faster implementation | Silent invalid layouts or budget violations | Not acceptable for Phase 18 completion. |

## Integration Gotchas

| Integration | Common Mistake | Correct Approach |
|-------------|----------------|------------------|
| Existing Stage12 outputs | Treat previous pool metrics as TRACE-BiOpt evidence. | Use Stage12 as baseline/context only. |
| Baseline registry | Let runner include unregistered baselines automatically. | Fail if a result method is not in the registry. |
| Paper-source generation | Overwrite v1.x contracts without versioning. | Add v2.0/Stage15-specific files or version columns. |
| Raw datasets | Leak raw paths/arrays into committed artifacts. | Store metadata, summaries, and checksums only. |

## Performance Traps

| Trap | Symptoms | Prevention | When It Breaks |
|------|----------|------------|----------------|
| Naive exchange over all swaps with full recomputation | Probe runs are slow or hang. | Cache solves/metrics; rank candidate swaps; limit two-swap beam. | Medium/large node counts and 10 splits. |
| Repeated posterior inversions | Runtime dominated by matrix inverse calls. | Use Cholesky solves and trace identities; avoid explicit inverse where possible. | Full Stage15 budgets. |
| GPU-dependent relaxation | Queue/resource contention. | CPU-first deterministic solve; optional GPU only behind a flag. | Multi-split runs. |

## "Looks Done But Isn't" Checklist

- [ ] **Method spec:** Includes non-goals and explicitly bans baseline-in-pool selection.
- [ ] **Implementation:** Enforces exact budget k after rounding/refinement.
- [ ] **Probe report:** Labels probe status and does not claim full dominance.
- [ ] **Full Stage15:** Verifies every dataset-budget-split-baseline row exists.
- [ ] **Dominance table:** Names the best baseline per row and includes paired statistics.
- [ ] **Theory contract:** Lists assumptions and proof status for each theorem.
- [ ] **Claim contract:** Wording changes when any row is tied or lost.

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
|---------|---------------|----------------|
| Pool critique reappears | HIGH | Refactor method to remove baseline-derived candidates; rerun probes. |
| Weak regimes fail | MEDIUM-HIGH | Inspect objective term ledger; adjust validation-only tuning; if still failing, narrow claims. |
| Full Stage15 incomplete | MEDIUM | Resume missing jobs; keep claim gate closed until coverage is complete. |
| Theory assumption too strong | MEDIUM | Downgrade theorem to proposition/conditional bound and adjust claim contract. |

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase | Verification |
|---------|------------------|--------------|
| Recreating pool critique | Phase 17 | Spec and baseline registry reviewed before implementation. |
| Post-hoc objective tuning | Phase 17-18 | Parameter ledger exists before test evaluation. |
| Missing optimization diagnostics | Phase 18-19 | Probe artifacts include descent and exchange gap fields. |
| Overclaiming theory | Phase 20 | Theory contract has assumptions and status. |
| Probe as full evidence | Phase 19-21 | Claim contract rejects full dominance wording until Stage15 coverage passes. |

## Sources

- `gpt_pro_suggestion_round1.md` - primary project-specific risk analysis.
- Sayyady et al. 2013, https://doi.org/10.3141/2339-04 - budget-constrained sensor location framing.
- Yu et al. 2018, https://doi.org/10.1016/j.jprocont.2017.03.011 - computational difficulty and relaxation/rounding patterns.
- Mehr and Horowitz 2018, https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/Mehr_Submodular_Optimal_Sensor_Placement_ACC2018.pdf - submodular traffic placement baselines and approximation claims.
- Liu et al. 2016 version, https://arxiv.org/abs/1507.07205 - robust observability under sensor/connection failures and NP-hardness context.

---
*Pitfalls research for: TRACE-BiOpt v2.0*
*Researched: 2026-05-26*
