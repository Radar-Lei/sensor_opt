# Paper Plan

**Title**: TRACE-BiOpt: Recoverability-Driven Bilevel Transportation Network Design for Sparse Traffic Sensor Siting
**Venue**: Transportation Research Part B: Methodological (Elsevier CAS template)
**Type**: Method + scoped theory + multi-network empirical evidence
**Date**: 2026-05-28
**Page budget**: Full journal manuscript, targeting 12--14 pages before appendix
**Aggregate claim status**: `supported_submission_ready`

## Claims-Evidence Matrix

| Claim | Evidence | Status | Section |
|-------|----------|--------|---------|
| TRACE-BiOpt formulates sparse traffic sensor siting as a recoverability-driven bilevel network-design problem, not a candidate-pool selection or coverage-only counting problem. | `TRACE_BIOPT_SPEC.md`, `trace_biopt_problem_contract.csv`, method implementation | Supported | §1, §3 |
| The bilevel objective jointly optimizes hidden-state reconstruction, posterior uncertainty, scenario CVaR tail risk, and spatial redundancy under one transparent GLS/MAP lower-level inverse problem. | `TRACE_BIOPT_SPEC.md` §2--3, `trace_biopt_method_contract.csv` | Supported | §3, §4 |
| The posterior-trace certificate is a principled squared-error uncertainty proxy under a scoped linear-Gaussian GLS/MAP model. | `TRACE_BIOPT_THEORY.md`, `trace_biopt_theory_bridge.csv` | Supported with assumptions | §4 |
| The deterministic initialization-and-exchange solver produces a searched-neighborhood exchange certificate. | `trace_biopt_exchange_certificate_summary.csv`, `trace_biopt_exchange_gap_summary.csv` | Supported | §4 |
| TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against 21 pre-registered baselines spanning 11 method families across 9 tested dataset-budget regimes. | `trace_biopt_claim_contract.json`, `trace_biopt_full_baseline_matrix.csv`, `trace_biopt_best_baseline_delta.csv` | Supported | §5 |
| After Holm correction across all 189 paired comparisons, no pre-registered challenger remains statistically tied or significantly better. | `trace_biopt_significance_posture_summary.csv`, `TRACE_BIOPT_DOMINANCE.md` | Supported | §5 |
| 27/27 deterministic 16-node subnetwork cases are exact hits with zero objective gap. | `trace_biopt_exact_subnetwork_summary.csv` | Supported | §5 |
| TRACE-SL/RCSS (predecessor) is a baseline row within the TRACE-BiOpt comparison class. | `trace_biopt_comparison_class_contract.csv`, Stage 12--14 historical artifacts | Supported as baseline | §5 |
| Robustness evidence is stress-test evidence, not global robustness certification. | `trace_biopt_tail_risk_posture.csv`, `trace_biopt_posterior_risk_posture.csv`, claim contract | Bounded | §6, §7 |

## Structure

### §0 Abstract
- Problem: fixed sparse sensors are often chosen for coverage or observability, not for recoverability-driven network design.
- Approach: TRACE-BiOpt is a recoverability-driven bilevel optimization that jointly minimizes hidden-state reconstruction loss, posterior uncertainty, scenario CVaR tail risk, and spatial redundancy under a transparent GLS/MAP inverse problem.
- Key result: across PeMS7_228, PeMS7_1026, and Seattle at 10/20/30% budgets, TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against 21 pre-registered baselines; no challenger survives Holm-corrected comparison.
- Implication: sparse traffic sensor siting can be formulated and solved as a recoverability-driven bilevel network-design problem.

### §1 Introduction
- Open with the cost and permanence of traffic sensor deployments.
- Gap: classical count-location and candidate-pool selection formulations do not directly optimize full-network recoverability under transparent reconstruction.
- Contributions: bilevel formulation, deterministic solver, scoped theory bridge (exchange certificate, posterior trace identity, CVaR epigraph), multi-network evidence with Holm-corrected dominance, and reproducible audited comparison-class contract.

### §2 Related Work
- Traffic counting and detector location.
- Sensor selection and optimal experimental design.
- Graph signal sampling and sparse reconstruction.
- Bilevel optimization in transportation network design.
- Traffic state estimation and black-box forecasting.

### §3 Recoverability-Driven Bilevel Network Design Problem
- Define graph, candidate sites, hidden complement, transparent GLS/MAP lower-level reconstruction.
- Present the bilevel objective `J(S)` with four terms.
- State the formal CVaR tail-risk epigraph.
- Present the audited comparison-class contract.

### §4 TRACE-BiOpt Solver
- Deterministic initialization: relaxed rounding or objective-forward construction.
- Greedy one-swap exchange refinement under `J(S)`.
- Stopping rule and searched-neighborhood exchange certificate.
- State scoped posterior trace identity, CVaR epigraph formulation, and workload complexity.

### §5 Experimental Design and Main Results
- Datasets (PeMS7_228, PeMS7_1026, Seattle), budgets (10/20/30%), 21 pre-registered baselines, metrics, and evidence protocol.
- Main dominance table: TRACE-BiOpt vs all baselines across 9 dataset-budget regimes.
- Holm-corrected paired comparison screen: 189/189 wins.
- Exact subnetwork benchmark: 27/27 hits.

### §6 Ablations and Sensitivity
- Objective component ablation (reconstruction loss, posterior trace, CVaR, spatial penalty).
- Objective weight sensitivity.
- Solver scale and tractability.
- Candidate pool size sensitivity.
- Exchange convergence curves.

### §7 Discussion and Limitations
- Interpret why recoverability-driven bilevel design helps.
- Preserve exchange-certificate (not global optimality) and non-universal-generalization caveats.
- Seattle 10% retain-on-Stage15 discussion.

### §8 Conclusion
- Summarize TRACE-BiOpt as recoverability-driven bilevel transportation network design with audited evidence.

## Figure Plan

| ID | Type | Description | Data Source | Priority |
|----|------|-------------|-------------|----------|
| Fig 1 | Workflow | TRACE-BiOpt bilevel structure: upper-level layout design + lower-level GLS/MAP reconstruction | generated | HIGH |
| Fig 2 | Heatmap | Full 9-row x 21-baseline MAE comparison matrix | `trace_biopt_full_baseline_matrix.csv` | HIGH |
| Fig 3 | Line plot | Held-out MAE across budgets for TRACE-BiOpt and top baselines | `trace_biopt_best_baseline_delta.csv` | HIGH |
| Fig 4 | Convergence | Objective descent curves during exchange refinement | `trace_biopt_objective_descent_summary.csv` | MEDIUM |
| Fig 5 | Exact benchmark | 16-node exact subnetwork results | `trace_biopt_exact_subnetwork_summary.csv` | MEDIUM |
| Table 1 | Main table | TRACE-BiOpt MAE vs best baseline and Holm p-values per dataset-budget | `trace_biopt_claim_contract.csv` | HIGH |
| Table 2 | Ablation table | Objective component ablation on PeMS7_228 | `trace_biopt_route_ablation_summary.csv` | HIGH |
| Table 3 | Theory table | Scoped statements and non-claim boundaries | `TRACE_BIOPT_THEORY.md` | MEDIUM |

## Citation Plan

- §1--§2 traffic counting location: `yang1998optimal`.
- §2 sensor selection/design: `joshi2009sensor`, `krause2008near`.
- §2 graph sampling/reconstruction: `chen2015sampling`, `anis2016sampling`, `manohar2018sparse`.
- §2 bilevel optimization: standard bilevel references.
- §2 traffic forecasting context: `li2018dcrnn`, `yu2018stgcn`.

## Reviewer Feedback

Inline planning review: the draft should avoid claiming global optimality, certified robustness, or universal cross-network generalization. The paper should sell the TR Part B contribution as recoverability-driven bilevel network design with transparent inverse-problem evidence and an audited comparison-class contract.

## Next Steps

- [x] Generate figures and tables.
- [x] Draft CAS LaTeX.
- [x] Compile PDF.
- [ ] Run improvement loop.
- [ ] Run submission audits.
- [ ] Submit to Transportation Research Part B: Methodological.
