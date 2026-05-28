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

- [x] Define TRACE-BiOpt as one robust bilevel reconstruction-risk optimization method with a deterministic solver.
- [x] Implement TRACE-BiOpt and Stage15-compatible launch/evaluation scripts.
- [x] Pre-register baselines and keep them outside the method itself.
- [x] Run weak-regime probes before committing full Stage15 compute.
- [x] Run full Stage15 experiments when probes justify scaling.
- [x] Generate dominance, best-baseline, theory, and claim artifacts for a revised TR Part B paper.
- [x] Rewrite the paper narrative around TRACE-BiOpt now that the Stage15 ten-seed evidence gate has passed.
- [x] Run the local submission verifier on the rewritten TRACE-BiOpt manuscript and regenerate current audit artifacts.
- [x] Run fresh web citation audit and fix bibliography metadata issues.
- [x] Run fresh deterministic machine paper-claim audit against Stage15 evidence.
- [x] Run fresh deterministic machine proof audit and tighten theorem scope.
- [x] Address the machine adversarial kill-argument gate.
- [ ] Fill author metadata and submission package before declaring actual TR-B submission readiness.

### Out of Scope

- Claiming TRACE-BiOpt beats every possible baseline — current evidence supports dominance only against the pre-registered non-BiOpt baseline set in the tested Stage15 dataset-budget regimes.
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
- The weakest current Stage15 ten-seed regime remains PeMS7_1026 at 30% budget in the main table (`3.07109 < 3.07404`, directional mean dominance). A separate same-objective enhanced-search diagnostic over the original seeds 25-34 improves TRACE-BiOpt MAE by 0.0312 on average and wins 10/10 seed-matched comparisons, but does not replace the full nine-regime Stage15 main table.
- PeMS7_228 at 10% budget was diagnosed as a calibration-risk issue rather than only a search-budget issue. A same-objective enhanced-search diagnostic improved the mean margin but won only 7/10 seeds; the later train+validation calibrated-risk full-exchange diagnostic wins 10/10 seeds and improves the mean margin to -0.1022. Treat this as row-level diagnostic evidence until the same configuration is rerun across all nine Stage15 regimes.
- PeMS7_1026 at 30% budget also improves under the train+validation calibrated-risk direction. With scalable active-set exchange search, the Stage16 diagnostic wins 10/10 seeds and improves the mean margin from -0.0026 to -0.0372. This supports a unified calibrated-risk Stage16 direction, but the manuscript main table should not be replaced until all nine regimes are rerun with that same configuration.
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
| Pivot v2.0 to TRACE-BiOpt as the main method | A pool/selector story risks weakening originality and theory; a single robust bilevel reconstruction-risk objective better fits TR Part B network design expectations | ✓ Done |
| Keep baselines outside the method | Baselines should be pre-registered comparators, not candidates selected by the main algorithm | ✓ Done |
| Gate full Stage15 on weak-regime probes | PeMS7_1026 10% and Seattle 10% were the critical credibility tests for the stronger claim before scaling | ✓ Done |
| Treat v1.2 manuscript polishing as superseded until the method pivot is evaluated | Final paper writing should not polish a method story the project may replace | — Pending |
| Retarget v1.2 manuscript to Transportation Research Part B | User corrected the submission target before manuscript drafting; the existing theory and evidence foundation should now be written for TR Part B expectations | ✓ Done |
| Use `els-cas-templates` for manuscript source | TR Part B is an Elsevier journal and the user provided the local template directory | — Pending |
| Run `$paper-writing` with submission assurance | The requested deliverable is a submission-gated paper package, not only a draft PDF | Partial: local submission verifier OK; proof, claim, citation, and kill-argument audits PASS; author/submission metadata remains |
| Generate TRACE-BiOpt claim contract from Stage15 dominance evidence | Row-level TR-B wording now has an auditable artifact tied to dominance, paired tests, and layout summaries | ✓ Done |
| Use Stage15 ten-seed evidence as the current TRACE-BiOpt claim basis | `stage15_biopt_allbudget_10seed_v2` beats the best pre-registered non-BiOpt baseline on all nine dataset-budget rows; weak mixed rows remain directional | ✓ Done |
| Add mechanism diagnostics to the TR-B manuscript | The manuscript needs to show why TRACE-BiOpt wins against strong reconstruction-aware comparators, not only report the dominance table | ✓ Done |
| Add full Stage15 baseline registry to the appendix | The all-baselines claim should enumerate every fixed non-BiOpt comparator and tie the registry to source artifacts | ✓ Done |
| Add TRACE-BiOpt optimization diagnostics | The method story needs solver-history evidence showing a single objective is improved before held-out evaluation | ✓ Done |
| Add bounded robustness routing | Robustness, cost, missingness, and temporal-shift evidence should be visible but explicitly prevented from becoming unsupported TRACE-BiOpt robustness claims | ✓ Done |
| Expand TR-B related work with audited citations | The TR-B manuscript needs stronger positioning against traffic count-location, observability, path reconstruction, and sensor-reliability literature | ✓ Done |
| Add method-positioning table | The innovation claim should make clear that TRACE-BiOpt is not OD count-location, full observability, OED-only placement, graph sampling, or estimator benchmarking | ✓ Done |
| Probe PeMS7_1026 30% weak-row search budget | The weakest Stage15 row may be limited by deterministic exchange-search budget rather than by the TRACE-BiOpt objective; diagnose before changing main claims | ✓ Done: over seeds 25-34, enhanced same-objective exchange search improves MAE by 0.0312 on average, changes the mean margin from -0.0026 to -0.0338, and wins 10/10 seed-matched comparisons |
| Probe PeMS7_228 10% low-budget search budget | The second mixed paired-evidence row might also be search-budget limited; diagnose before strengthening main claims | Fail-closed: enhanced search improves mean margin but wins only 7/10 seeds (`p=0.0671`), and full one-exchange checks on failed seeds still lose |
| Add train+validation calibration-risk diagnostic | PeMS7_228 10% showed validation/test mismatch under the two-day validation objective; test whether a larger calibration-risk sample fixes the low-budget row while preserving one TRACE-BiOpt objective | ✓ Done: `--trace-biopt-risk-source train_val` plus low certificate weights and complete one-exchange search wins 10/10 seeds, margin -0.1022, paired t-test `p=6.4e-05` |
| Probe Stage16 calibrated risk on PeMS7_1026 30% | The weakest Stage15 main-table row should also improve under a unified calibrated-risk direction before scaling to all regimes | ✓ Done: train+validation calibrated risk plus scalable active-set search wins 10/10 seeds, margin -0.0372, paired t-test `p=4.6e-05` |
| Target Transportation Science first | This was the previous v1.0/v1.1 planning assumption and is now superseded by the Transportation Research Part B target | Superseded |
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
*Last updated: 2026/05/27 after adding the PeMS7_1026 30% Stage16 calibrated-risk diagnostic*
