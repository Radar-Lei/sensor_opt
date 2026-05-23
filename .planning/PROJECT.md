# TRACE-SL Transportation Science Readiness

## Current State

TRACE-SL v1.0 shipped on 2026/05/23. The completed milestone turns the prior experimental prototype into a Transportation Science-ready evidence package for transparent reconstruction-aware sparse traffic sensor placement.

The repository now has:

- A claim-evidence contract constraining TRACE-SL claims to explicit theory, held-out evidence, robustness evidence, statistical comparisons, or limitations.
- A formal budgeted sensor-set formulation, RCSS surrogate, GLS/MAP posterior-error bridge, and validation-aware swap analysis.
- A reviewer-facing baseline portfolio covering observability/TSLP-style baselines, A/D-optimal design, graph/GSP connections, QR/SVD/POD sparse placement, learning-check framing, and multistart validation refinement.
- Curated PeMS7_228, PeMS7_1026, Seattle-supporting, candidate-count, runtime, and certificate-error evidence with paired statistics and bounded caveats.
- Stage 14 robustness artifacts for sensor failure, observation noise, missingness, nonuniform costs, temporal shift, and candidate-count sensitivity.
- A reproducibility handoff with deterministic manifests, generated paper-source tables, launcher smoke checks, aggregate validators, and raw-data hygiene boundaries.

## Core Value

Make strong, publishable claims about transparent reconstruction-aware traffic sensor placement, but only where the formulation, theory, baselines, robustness tests, and held-out evidence can support them.

## Requirements

### Validated

- ✓ TRACE-SL has a runnable experiment pipeline for PeMS7_228, PeMS7_1026, and Seattle-style inputs — existing
- ✓ The repository evaluates transparent reconstruction methods including historical mean, neighbor average, GSP, and GLS/MAP — existing
- ✓ Stage 11 outputs show validation-swap RCSS improves over random, validation-selected random, and variance/topology baselines at moderate/high PeMS7_228 budgets — existing
- ✓ PeMS7_228 has 10-split aggregate evidence and PeMS7_1026 has external validation evidence — existing
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

- [ ] Write the Transportation Science manuscript from the curated v1.0 evidence handoff.
- [ ] Produce paper-ready figures, tables, and narrative from committed result artifacts.
- [ ] Keep Seattle evidence supporting/conditional unless curated outputs justify core-claim status.
- [ ] Keep PeMS7_1026 framed as lower-power external evidence unless more splits are added.

### Out of Scope

- Claiming TRACE-SL is best at every budget and against every strong baseline — current 10% PeMS7_228 evidence does not support that wording.
- Calling the method formally “certified” without a theorem or bound — current evidence supports certificate-guided or posterior-certificate-aware wording.
- Treating validation MAE as final test evidence — final claims must use held-out test evaluation and paired comparisons.
- Making TR Part B the primary target before theory and algorithmic analysis mature — current project priority is Transportation Science readiness.
- Deleting or committing raw traffic datasets — datasets are local inputs and must remain protected unless explicitly approved.

## Next Milestone Goals

The next milestone should start fresh requirements for manuscript writing. The likely scope is PAPER-01 through PAPER-05: introduction, related work, method narrative, results narrative, and limitations for a Transportation Science submission.

## Context

The research direction is strong because it connects sparse traffic sensor layout decisions directly to full-network reconstruction quality. The intended distinction from classical traffic sensor location problems is that TRACE-SL does not pursue deterministic full observability or minimum counting-point coverage; it optimizes partial-observation reconstruction quality, uncertainty, robustness, and validation performance under limited budgets.

Known evidence caveats after v1.0:

- PeMS7_228 supports strong improvements at moderate/high budgets, while low-budget claims must preserve the multistart validation refinement caveat.
- PeMS7_1026 remains lower-power external evidence where documented.
- Seattle remains supporting/conditional evidence unless further curated into the core claim set.
- Stage 14 robustness is bounded to the tested perturbations and reduced PeMS7_228 settings.
- Raw datasets remain local/ignored and must not be committed.

## Constraints

- **Target venue:** Transportation Science is the primary submission target.
- **Backup venue:** TR Part B remains possible only with stronger mathematical modeling, posterior-error theory, algorithmic properties, and generality beyond PeMS tuning.
- **Claim strategy:** Strong claims should be preserved and strengthened with evidence rather than narrowed prematurely.
- **Evidence standard:** Core claims must be supported by held-out test results, paired comparisons, statistical uncertainty, robustness checks, and reproducible artifacts.
- **Reproducibility:** Raw datasets stay local and ignored; curated result summaries, scripts, and non-sensitive artifacts should remain synchronized with paper claims.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Target Transportation Science first | The contribution fits transportation network design and transparent optimization better than a theory-heavy TR Part B submission in its present state | ✓ Good |
| Keep strong claims, but require evidence-backed wording | The research has real promise; the right response is to add evidence and sharpen claims, not dilute the contribution | ✓ Good |
| Use “certificate-guided” unless formal certification is proved | Current posterior diagnostics correlate with MAE but are not formal certificates | ✓ Good |
| Treat multistart validation refinement as a serious comparator or portfolio member | At 10% budget it can outperform validation-swap RCSS, so ignoring it would invite reviewer criticism | ✓ Good |
| Make Seattle evidence supporting/conditional unless curated | Repository/paper consistency is necessary for reproducibility and reviewer trust | ✓ Good |
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
*Last updated: 2026/05/23 after v1.0 milestone completion*
