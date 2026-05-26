# TRACE-SL Transportation Research Part B Readiness

## Current State

TRACE-SL v1.0 shipped on 2026/05/23. The completed foundation milestones turn the prior experimental prototype into a Transportation Research Part B paper package for transparent reconstruction-aware sparse traffic sensor placement.

The repository now has:

- A claim-evidence contract constraining TRACE-SL claims to explicit theory, held-out evidence, robustness evidence, statistical comparisons, or limitations.
- A formal budgeted sensor-set formulation, RCSS surrogate, GLS/MAP posterior-error bridge, and validation-aware swap analysis.
- A reviewer-facing baseline portfolio covering observability/TSLP-style baselines, A/D-optimal design, graph/GSP connections, QR/SVD/POD sparse placement, learning-check framing, and multistart comparators.
- Curated PeMS7_228, PeMS7_1026, Seattle, candidate-count, runtime, and certificate-error evidence with paired statistics and bounded caveats.
- Robustness artifacts for sensor failure, observation noise, missingness, nonuniform costs, temporal shift, and candidate-count sensitivity.
- A reproducibility handoff with deterministic manifests, generated paper-source tables, launcher smoke checks, aggregate validators, and raw-data hygiene boundaries.

## Current Milestone: v2.0 TRACE-BiOpt Robust Bilevel Method Development

**Goal:** Upgrade TRACE-SL from a candidate-pool / validation-selector narrative into a single robust bilevel reconstruction-aware sensor layout optimization method, then produce Stage15 evidence showing TRACE-BiOpt dominates or is not significantly outperformed by pre-registered baselines.

**Target features:**
- Define `TRACE_BIOPT_SPEC.md` with one objective, lower-level MAP/GLS reconstruction, Huber hidden-state validation risk, posterior uncertainty, CVaR tail risk, spatial regularization, solver details, and deterministic stopping rules.
- Implement the TRACE-BiOpt method as a single optimizer rather than a portfolio selector, with projected continuous relaxation, top-k rounding, and deterministic exchange refinement.
- Add Stage15 launch/evaluation entry points for TRACE-BiOpt and all pre-registered baselines.
- First validate weak regimes: PeMS7_1026 10%, Seattle 10%, and PeMS7_228 10%.
- Expand to full Stage15 evidence over PeMS7_228, PeMS7_1026, Seattle, 10/20/30% budgets, 10 splits, and all pre-registered baselines.
- Generate dominance, best-baseline delta, theory-contract, and claim-contract artifacts for paper reuse.
- Reframe the previous TRACE-SL pool method as a previous version, ablation, or comparator rather than the final main method.
- Strengthen theory around MAP uniqueness/stability, posterior trace Bayes risk, all-layout validation generalization, and exchange local optimality certificates.

**Explicit non-goal:** This milestone does not continue polishing the current pool-centered manuscript as the final submission story. It does not claim global exact optimality, universal dominance beyond pre-registered baselines, or guaranteed improvement before Stage15 evidence supports the wording.

## Core Value

Make strong, publishable claims about transparent reconstruction-aware traffic sensor placement, but only where the formulation, theory, baselines, robustness tests, and held-out evidence can support them.

## Requirements

### Validated

- ✓ TRACE-SL has a runnable experiment pipeline for PeMS7_228, PeMS7_1026, and Seattle-style inputs — existing
- ✓ The repository evaluates transparent reconstruction methods including historical mean, neighbor average, GSP, and GLS/MAP — existing
- ✓ Stage 12 outputs show validation-swap RCSS improves over random, validation-selected random, and reviewer-facing baselines on PeMS7_228 while preserving the low-budget multistart caveat — v1.1
- ✓ PeMS7_228, PeMS7_1026, and Seattle have tracked 10-split Stage12 aggregate evidence — v1.1
- ✓ The method emits posterior trace, condition number, logdet, scenario CVaR trace, coverage, and validation diagnostics — existing
- ✓ TRACE-SL is framed as transparent reconstruction-aware sensor placement rather than an empirical candidate-pool heuristic — v1.0
- ✓ Primary claims are mapped to explicit evidence or bounded limitation wording — v1.0
- ✓ The 10% PeMS7_228 multistart caveat is preserved in the claim/evidence routing — v1.0
- ✓ The method uses certificate-guided wording unless formal certification is proved — v1.0
- ✓ TRACE-SL is positioned against deterministic full-observability TSLP and black-box traffic imputation/forecasting — v1.0
- ✓ The optimization objective, tractable surrogate, RCSS process, and validation-aware refinement are formalized — v1.0
- ✓ The GLS/MAP posterior covariance bridge to expected hidden-state squared error is documented — v1.0
- ✓ Reviewer-resistant baselines are implemented or bounded, including observability, A/D-optimal, graph/GSP, QR/SVD/POD, learning-check, and multistart comparisons — v1.0
- ✓ Core held-out evidence includes paired deltas, intervals, effect sizes, certificate-error correlations, runtime, and candidate-count sensitivity — v1.0
- ✓ Robustness evidence covers sensor failure, observation noise, missingness, heterogeneous costs, temporal shift, and candidate-pool size — v1.0
- ✓ Reproducibility artifacts trace paper-visible numbers to curated scripts, summaries, manifests, and generated tables without committing raw datasets — v1.0
- ✓ The full v1.1 paper foundation is frozen: claim/table contracts, Stage12 external evidence, ablation contracts, dataset classification, theory statements, and handoff manifest — v1.1

### Active

- [ ] Define TRACE-BiOpt as one robust bilevel reconstruction-risk optimization method with a deterministic solver.
- [ ] Implement TRACE-BiOpt and Stage15-compatible launch/evaluation scripts.
- [ ] Pre-register baselines and keep them outside the method itself.
- [ ] Run weak-regime probes before committing full Stage15 compute.
- [ ] Run full Stage15 experiments when probes justify scaling.
- [ ] Generate dominance, best-baseline, theory, and claim artifacts for a revised TR Part B paper.
- [ ] Rewrite the paper narrative around TRACE-BiOpt only after method and evidence gates pass.

### Out of Scope

- Claiming TRACE-SL is best at every budget and against every strong baseline — current 10% PeMS7_228 evidence does not support that wording.
- Calling the method formally “certified” without a theorem or bound — current evidence supports certificate-guided or posterior-certificate-aware wording.
- Claiming optimal sensor placement, guaranteed MAE improvement, global robustness, or generalization across networks without the required evidence and theory.
- Treating validation MAE as final test evidence — final claims must use held-out test evaluation and paired comparisons.
- Re-targeting to Transportation Science formatting in this milestone — the user corrected the target to Transportation Research Part B.
- Running new Stage12 or robustness experiments by default — only do this if audits reveal a blocking evidence gap.
- Deleting or committing raw traffic datasets — datasets are local inputs and must remain protected unless explicitly approved.
- Treating baselines as candidates inside the main TRACE-BiOpt method — this would recreate the pool/selector critique.
- Claiming TRACE-BiOpt beats all possible baselines — allowed wording is limited to pre-registered baselines and tested dataset-budget regimes.
- Continuing v1.2 manuscript polishing as the final story before the method pivot is evaluated — paper writing should follow the v2.0 method/evidence outcome.

## Next Milestone Goals

After v2.0, the next milestone should rewrite and audit the TR Part B manuscript around TRACE-BiOpt if Stage15 supports the stronger method story. If Stage15 does not support dominance, the next milestone should either narrow claims or decide whether to return to a bounded TRACE-SL comparator narrative.

## Context

The research direction is strong because it connects sparse traffic sensor layout decisions directly to full-network reconstruction quality. The intended distinction from classical traffic sensor location problems is that TRACE-SL does not pursue deterministic full observability or minimum counting-point coverage; it optimizes partial-observation reconstruction quality, uncertainty, robustness, and validation performance under limited budgets.

Known evidence caveats for v2.0:

- PeMS7_228 supports strong improvements against reviewer-facing baselines, while low-budget claims must preserve the multistart validation refinement caveat.
- PeMS7_1026 and Seattle have complete Stage12 10-split evidence and may support multi-network empirical discussion.
- The existing pool-centered TRACE-SL story risks reading as a portfolio or AutoML-style selector rather than a unified traffic network design method.
- The weakest current regimes are PeMS7_1026 10% and Seattle 10%, so v2.0 should probe those before scaling full Stage15.
- Multi-network evidence must not be phrased as universal cross-network generalization.
- Robustness is bounded to the tested perturbations and reduced PeMS7_228 settings.
- Raw datasets remain local/ignored and must not be committed.

## Constraints

- **Target venue:** Transportation Research Part B remains the primary submission target, but v2.0 changes the method story before final manuscript submission.
- **Template:** Use the local `els-cas-templates/` CAS template files for the paper source.
- **Method strategy:** TRACE-BiOpt must be presented as one objective and one deterministic optimization pipeline, not as a candidate pool or baseline selector.
- **Claim strategy:** Strong claims should be preserved and strengthened with Stage15 evidence rather than narrowed prematurely.
- **Evidence standard:** Core claims must be supported by held-out test results, paired comparisons, statistical uncertainty, robustness checks, and reproducible artifacts.
- **External evidence:** PeMS7_1026 and Seattle have complete Stage12 10-split evidence; use them as external empirical evidence, not as universal generalization proof.
- **Execution concurrency:** Completed Stage12 external evidence closure used max jobs set to 1. Future reruns should preserve this constraint unless the compute environment changes.
- **Reproducibility:** Raw datasets stay local and ignored; curated result summaries, scripts, and non-sensitive artifacts should remain synchronized with paper claims.
- **Stage15 scale gate:** Full Stage15 should follow weak-regime probes rather than launch blindly.
- **Submission assurance:** Later paper-writing must run with `assurance: submission`; final completion requires proof, claim, citation, and verifier artifacts.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Pivot v2.0 to TRACE-BiOpt as the main method | A pool/selector story risks weakening originality and theory; a single robust bilevel reconstruction-risk objective better fits TR Part B network design expectations | — Pending |
| Keep baselines outside the method | Baselines should be pre-registered comparators, not candidates selected by the main algorithm | — Pending |
| Gate full Stage15 on weak-regime probes | PeMS7_1026 10% and Seattle 10% are the critical credibility tests for the stronger claim | — Pending |
| Treat v1.2 manuscript polishing as superseded until the method pivot is evaluated | Final paper writing should not polish a method story the project may replace | — Pending |
| Retarget v1.2 manuscript to Transportation Research Part B | User corrected the submission target before manuscript drafting; the existing theory and evidence foundation should now be written for TR Part B expectations | — Pending |
| Use `els-cas-templates` for manuscript source | TR Part B is an Elsevier journal and the user provided the local template directory | — Pending |
| Run `$paper-writing` with submission assurance | The requested deliverable is a submission-gated paper package, not only a draft PDF | — Pending |
| Target Transportation Science first | This was the previous v1.0/v1.1 planning assumption and is now superseded for v1.2 writing | ⚠ Revisit |
| Keep strong claims, but require evidence-backed wording | The research has real promise; the right response is to add evidence and sharpen claims, not dilute the contribution | ✓ Good |
| Frame v1.1 as paper foundation, not manuscript drafting | The claim, external evidence, ablation logic, and theory layer needed to be frozen before writing begins | ✓ Good |
| Require PeMS7_1026 Stage12 10-split evidence before stronger external PeMS claims | The earlier PeMS7_1026 evidence was promising but lower-power | ✓ Done |
| Require Seattle Stage12 10-split evidence before core-claim use | Seattle should not remain conditional if it is used as external/transfer-style evidence | ✓ Done |
| Limit remaining Stage12 closure execution to max_jobs=1 | User-confirmed compute constraint; parallel split/seed/dataset jobs risk overrunning the available environment | ✓ Done |
| Use “certificate-guided” unless formal certification is proved | Current posterior diagnostics correlate with MAE but are not formal certificates | ✓ Good |
| Treat multistart validation refinement as a serious comparator or portfolio member | At 10% budget it can outperform validation-swap RCSS, so ignoring it would invite reviewer criticism | ✓ Good |
| Use generated paper-source tables as the manuscript handoff | This keeps paper-visible numbers tied to committed aggregate evidence and provenance | ✓ Good |
| Use DRY_RUN launcher smoke checks for final reproducibility validation | Full experiment reruns are expensive; smoke checks validate command surfaces without raw-data exposure | ✓ Good |

## Archived Milestones

<details>
<summary>v1.1 TRACE-SL Transportation Science Paper Foundation — complete 2026/05/26</summary>

Archived files:

- `.planning/milestones/v1.1-ROADMAP.md`
- `.planning/milestones/v1.1-REQUIREMENTS.md`
- `.planning/v1.1-MILESTONE-AUDIT.md`

</details>

<details>
<summary>v1.0 TRACE-SL Readiness — shipped 2026/05/23</summary>

Archived files:

- `.planning/milestones/v1.0-ROADMAP.md`
- `.planning/milestones/v1.0-REQUIREMENTS.md`
- `.planning/milestones/v1.0-MILESTONE-AUDIT.md`

</details>

## Evolution

This document evolves at phase transitions and milestone boundaries.

---
*Last updated: 2026/05/26 after starting v2.0 TRACE-BiOpt robust bilevel method development*
