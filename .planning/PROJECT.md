# TRACE-SL Transportation Science Readiness

## Current State

TRACE-SL v1.0 shipped on 2026/05/23. The completed milestone turns the prior experimental prototype into a Transportation Science-ready evidence package for transparent reconstruction-aware sparse traffic sensor placement.

The repository now has:

- A claim-evidence contract constraining TRACE-SL claims to explicit theory, held-out evidence, robustness evidence, statistical comparisons, or limitations.
- A formal budgeted sensor-set formulation, RCSS surrogate, GLS/MAP posterior-error bridge, and validation-aware swap analysis.
- A reviewer-facing baseline portfolio covering observability/TSLP-style baselines, A/D-optimal design, graph/GSP connections, QR/SVD/POD sparse placement, learning-check framing, and multistart comparators.
- Curated PeMS7_228, PeMS7_1026, Seattle, candidate-count, runtime, and certificate-error evidence with paired statistics and bounded caveats.
- Stage 14 robustness artifacts for sensor failure, observation noise, missingness, nonuniform costs, temporal shift, and candidate-count sensitivity.
- A reproducibility handoff with deterministic manifests, generated paper-source tables, launcher smoke checks, aggregate validators, and raw-data hygiene boundaries.

## Current Milestone: v1.1 TRACE-SL Transportation Science Paper Foundation

**Goal:** Freeze the Transportation Science paper foundation before manuscript drafting: core claim, main result table, ablation logic, external validation evidence, and a lightweight theory layer that make TRACE-SL ready to write without starting the paper text.

**Target features:**
- Freeze the paper-level narrative as transparent reconstruction-aware sensor layout design, not a heuristic or baseline-beating story.
- Freeze the main method and main evidence around `validation_swap_selected` and the Stage12 PeMS7_228 baseline portfolio, while preserving the multistart caveat.
- Organize or fill ablation evidence showing the separate roles of certificate candidate generation, validation selection, and validation-aware swap refinement.
- Use completed PeMS7_1026 Stage12 10-split external evidence as multi-network empirical support, without claiming universal cross-network generalization.
- Use completed Seattle Stage12 10-split external/transfer-style evidence according to the regenerated external evidence gate.
- Keep the completed PeMS7_1026 and Seattle Stage12 closure provenance tied to the `max_jobs=1` / one-active-job execution constraint used for reliability.
- Keep robustness as stress-test or appendix evidence unless multi-seed perturbation results are added.
- Prepare the Transportation Science theory layer: posterior trace bridge, monotonicity, validation-aware swap local optimality, and complexity.
- Avoid TR Part B-level or unsupported wording such as optimal, certified, globally robust, guaranteed MAE improvement, or generalizes across networks.

**Explicit non-goal:** This milestone does not start manuscript drafting and does not generate introduction, related work, method, results, or limitations prose. It only prepares the claim-evidence-theory-experiment foundation for later writing.

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

### Active

- [x] Freeze the TRACE-SL paper foundation around a Transportation Science claim, not a toy-project or heuristic-improvement framing.
- [x] Freeze the Stage12 PeMS7_228 baseline portfolio as the main in-domain result table and preserve the multistart caveat.
- [x] Organize or complete the ablation evidence needed to show why certificate candidate generation, validation selection, and validation-aware swap each matter.
- [x] Complete PeMS7_1026 Stage12 10-split evidence using the same budgets and reviewer-facing baseline portfolio.
- [x] Complete Seattle Stage12 10-split external/transfer-style evidence before allowing Seattle into any core claim.
- [x] Prepare a theory-ready package for posterior trace identity, monotonicity, validation-aware swap local optimality, and complexity.
- [x] Produce paper-foundation artifacts that a later writing milestone can consume without starting manuscript prose now.

### Out of Scope

- Writing manuscript prose for introduction, related work, method, results, limitations, abstract, or conclusion — v1.1 prepares the foundation only.
- Claiming TRACE-SL is best at every budget and against every strong baseline — current 10% PeMS7_228 evidence does not support that wording.
- Calling the method formally “certified” without a theorem or bound — current evidence supports certificate-guided or posterior-certificate-aware wording.
- Claiming optimal sensor placement, guaranteed MAE improvement, global robustness, or generalization across networks without the required evidence and theory.
- Treating validation MAE as final test evidence — final claims must use held-out test evaluation and paired comparisons.
- Making TR Part B the primary target before theory and algorithmic analysis mature — current project priority is Transportation Science readiness.
- Deleting or committing raw traffic datasets — datasets are local inputs and must remain protected unless explicitly approved.

## Next Milestone Goals

After v1.1, the next milestone should begin manuscript drafting from the frozen paper foundation: introduction, related work, method narrative, results narrative, and limitations for a Transportation Science submission.

## Context

The research direction is strong because it connects sparse traffic sensor layout decisions directly to full-network reconstruction quality. The intended distinction from classical traffic sensor location problems is that TRACE-SL does not pursue deterministic full observability or minimum counting-point coverage; it optimizes partial-observation reconstruction quality, uncertainty, robustness, and validation performance under limited budgets.

Known evidence caveats after v1.1:

- PeMS7_228 supports strong improvements against reviewer-facing baselines, while low-budget claims must preserve the multistart validation refinement caveat.
- PeMS7_1026 and Seattle have complete Stage12 10-split evidence and may support multi-network empirical discussion.
- Multi-network evidence must not be phrased as universal cross-network generalization.
- Stage 14 robustness is bounded to the tested perturbations and reduced PeMS7_228 settings.
- Raw datasets remain local/ignored and must not be committed.

## Constraints

- **Target venue:** Transportation Science is the primary submission target.
- **Backup venue:** TR Part B remains possible only with stronger mathematical modeling, posterior-error theory, algorithmic properties, and generality beyond PeMS tuning.
- **Claim strategy:** Strong claims should be preserved and strengthened with evidence rather than narrowed prematurely.
- **Evidence standard:** Core claims must be supported by held-out test results, paired comparisons, statistical uncertainty, robustness checks, and reproducible artifacts.
- **External evidence:** PeMS7_1026 and Seattle have complete Stage12 10-split evidence; use them as external empirical evidence, not as universal generalization proof.
- **Execution concurrency:** Completed Stage12 external evidence closure used max jobs set to 1. Future reruns should preserve this constraint unless the compute environment changes.
- **Reproducibility:** Raw datasets stay local and ignored; curated result summaries, scripts, and non-sensitive artifacts should remain synchronized with paper claims.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Target Transportation Science first | The contribution fits transportation network design and transparent optimization better than a theory-heavy TR Part B submission in its present state | ✓ Good |
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
<summary>v1.0 TRACE-SL Readiness — shipped 2026/05/23</summary>

Archived files:

- `.planning/milestones/v1.0-ROADMAP.md`
- `.planning/milestones/v1.0-REQUIREMENTS.md`
- `.planning/milestones/v1.0-MILESTONE-AUDIT.md`

</details>

## Evolution

This document evolves at phase transitions and milestone boundaries.

---
*Last updated: 2026/05/26 after EVID-03/EVID-04 Stage12 closure and TR-B narrative alignment*
