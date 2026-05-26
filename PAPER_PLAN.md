# Paper Plan

**Title**: TRACE-SL: Reconstruction-Aware Sensor Layout Design for Traffic State Estimation
**Venue**: Transportation Research Part B: Methodological (Elsevier CAS template)
**Type**: Method + empirical + scoped theory
**Date**: 2026-05-26
**Page budget**: Full journal manuscript, targeting 12-14 pages before appendix
**Section count**: 8 main sections plus appendix

## Claims-Evidence Matrix

| Claim | Evidence | Status | Section |
|-------|----------|--------|---------|
| TRACE-SL formulates sparse traffic sensing as reconstruction-aware hidden-network design rather than counting-point coverage alone. | `claim_contract.json`, `theory_statement_contract.json`, method implementation | Supported | §1, §3 |
| The posterior-trace certificate is a principled squared-error uncertainty proxy under a scoped linear-Gaussian GLS/MAP model. | `theory_statement_contract.json`, `transparent_estimator_eval.py` | Supported with assumptions | §4 |
| Validation-aware TRACE-SL improves held-out GLS/MAP reconstruction on PeMS7_228 against reviewer-facing baselines. | `core_performance_table.csv`, `paired_delta_table.csv` | Supported | §5 |
| PeMS7_1026 and Seattle provide multi-network empirical evidence but not universal generalization proof. | `external_evidence_contract.csv`, `external_evidence_gate.json` | Supported with caveat | §5 |
| Candidate generation, validation selection, and validation-aware swap each have distinct roles. | `ablation_contract.csv` | Supported | §6 |
| Robustness evidence is stress-test evidence, not global robustness certification. | `robustness_condition_table.csv`, claim contract | Bounded | §6, §7 |

## Structure

### §0 Abstract
- Problem: fixed sparse sensors are often chosen for coverage or observability, not for hidden-network reconstruction quality.
- Approach: TRACE-SL combines transparent GLS/MAP reconstruction with posterior certificates, validation selection, and local swap refinement.
- Key result: on PeMS7_228, TRACE-SL reduces held-out MAE relative to validation-selected random layouts by 0.123, 0.095, and 0.163 at 10%, 20%, and 30% budgets.
- Implication: the layout problem can be treated as transparent reconstruction-aware network design.

### §1 Introduction
- Open with the cost and permanence of traffic sensor deployments.
- Gap: classical count-location formulations do not directly optimize full-network state reconstruction.
- Contributions: formulation, TRACE-SL algorithm, scoped theory bridge, multi-network evidence, reproducible claim routing.

### §2 Related Work
- Traffic counting and detector location.
- Sensor selection and optimal experimental design.
- Graph signal sampling and sparse reconstruction.
- Traffic state estimation and black-box forecasting.

### §3 Reconstruction-Aware Layout Problem
- Define graph, candidate sensors, hidden complement, train/validation/test split, transparent reconstructors.
- Present the budgeted design objective and evidence discipline.

### §4 TRACE-SL Method
- Candidate generation, posterior/scenario certificates, validation-tuned scoring, validation-aware one-swap refinement.
- State scoped posterior trace identity, monotonicity, local optimality, and workload complexity.

### §5 Experimental Design and Main Results
- Datasets, budgets, baselines, metrics, and Stage12 protocol.
- Main PeMS7_228 table and paired tests.
- External PeMS7_1026 and Seattle evidence.

### §6 Ablations and Robustness
- Random pool, validation-selected random, certificate-only candidates, RCSS, validation-swap, multistart.
- Robustness and stress-test routing.

### §7 Discussion and Limitations
- Interpret why reconstruction-aware design helps.
- Preserve multistart and non-universal-generalization caveats.

### §8 Conclusion
- Summarize reconstruction-aware sensor layout design and scoped evidence.

## Figure Plan

| ID | Type | Description | Data Source | Priority |
|----|------|-------------|-------------|----------|
| Fig 1 | Workflow | TRACE-SL train/validation/test and candidate-to-layout pipeline | generated | HIGH |
| Fig 2 | Line plot | PeMS7_228 held-out MAE across budgets for main baselines | `core_performance_table.csv` | HIGH |
| Table 1 | Main table | PeMS7_228 Stage12 mean MAE and paired p-values | `core_performance_table.csv`, `paired_delta_table.csv` | HIGH |
| Table 2 | External table | PeMS7_1026 and Seattle main-method MAE across budgets | `external_evidence_contract.csv` | HIGH |
| Table 3 | Ablation table | Component-layer comparison on PeMS7_228 | `ablation_contract.csv` | HIGH |
| Table 4 | Theory table | Scoped statements and non-claim boundaries | `theory_statement_contract.csv` | MEDIUM |

## Citation Plan

- §1-§2 traffic counting location: `yang1998optimal`.
- §2 sensor selection/design: `joshi2009sensor`, `krause2008near`.
- §2 graph sampling/reconstruction: `chen2015sampling`, `anis2016sampling`, `manohar2018sparse`.
- §2 traffic forecasting context: `li2018dcrnn`, `yu2018stgcn`.

## Reviewer Feedback

Inline planning review: the draft should avoid claiming global optimality, certified robustness, or universal cross-network generalization. The paper should sell the TR Part B contribution as reconstruction-aware network design with transparent inverse-problem evidence, not as another black-box traffic imputation benchmark.

## Next Steps

- [x] Generate figures and tables.
- [x] Draft CAS LaTeX.
- [ ] Compile PDF.
- [ ] Run improvement loop.
- [ ] Run submission audits.
