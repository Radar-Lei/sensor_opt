# TRACE-SL Transportation Science Readiness

## What This Is

TRACE-SL is a research project on sparse traffic sensor placement for full-network traffic state reconstruction. The current codebase already contains a strong experimental prototype built around transparent GLS/MAP and GSP reconstruction, OR-guided candidate generation, posterior/certification diagnostics, RCSS selection, and validation-aware swap refinement. This project will turn that prototype into a Transportation Science-ready methodology paper, with TR Part B: Methodological kept as a higher-risk backup path if stronger theory and algorithmic analysis are completed.

## Core Value

Make strong, publishable claims about transparent reconstruction-aware traffic sensor placement, but only where the formulation, theory, baselines, robustness tests, and held-out evidence can support them.

## Requirements

### Validated

- ✓ TRACE-SL has a runnable experiment pipeline for PeMS7_228, PeMS7_1026, and Seattle-style inputs — existing
- ✓ The repository evaluates transparent reconstruction methods including historical mean, neighbor average, GSP, and GLS/MAP — existing
- ✓ Stage 11 outputs show validation-swap RCSS improves over random, validation-selected random, and variance/topology baselines at moderate/high PeMS7_228 budgets — existing
- ✓ PeMS7_228 has 10-split aggregate evidence and PeMS7_1026 has external validation evidence — existing
- ✓ The method already emits posterior trace, condition number, logdet, scenario CVaR trace, coverage, and validation diagnostics — existing

### Active

- [ ] Reframe TRACE-SL as a transparent reconstruction-aware sensor placement problem rather than an empirical candidate-search heuristic
- [ ] Preserve a strong contribution claim while aligning every claim with held-out results, robustness evidence, statistical support, and theory where applicable
- [ ] Formalize the optimization objective, tractable surrogate, RCSS candidate/selection process, and validation-aware refinement
- [ ] Establish a principled bridge between GLS/MAP posterior covariance certificates and expected hidden-link reconstruction error
- [ ] Resolve the 10% budget issue where multistart validation refinement can outperform validation-swap RCSS, without post-hoc cherry-picking
- [ ] Strengthen baselines with observability-inspired, A/D-optimal design, graph sampling, QR/SVD/POD sparse placement, and a simple learning-based reconstruction check where feasible
- [ ] Expand external validation splits and report confidence intervals, effect sizes, paired tests, and bootstrap-style uncertainty instead of relying only on p-values
- [ ] Add robustness experiments for sensor failure, observation noise, missing readings, nonuniform sensor costs, temporal distribution shift, candidate-count sensitivity, and runtime
- [ ] Clean up Seattle evidence consistency: either curate and expose Seattle outputs or remove Seattle from the core paper claim
- [ ] Produce paper-ready figures, tables, and narrative that support a Transportation Science submission

### Out of Scope

- Claiming TRACE-SL is best at every budget and against every strong baseline — current 10% PeMS7_228 evidence does not support that wording
- Calling the method formally “certified” without a theorem or bound — current evidence supports certificate-guided or posterior-certificate-aware wording
- Treating validation MAE as final test evidence — final claims must use held-out test evaluation and paired comparisons
- Making TR Part B the primary target before theory and algorithmic analysis mature — current project priority is Transportation Science readiness
- Deleting or committing raw traffic datasets — datasets are local inputs and must remain protected unless explicitly approved

## Context

The research direction is strong because it connects sparse traffic sensor layout decisions directly to full-network reconstruction quality. The intended distinction from classical traffic sensor location problems is that TRACE-SL does not pursue deterministic full observability or minimum counting-point coverage; it optimizes partial-observation reconstruction quality, uncertainty, robustness, and validation performance under limited budgets.

The method’s current strengths are: transparent reconstruction via GLS/MAP/GSP rather than black-box imputation, OR-guided candidate generation, posterior/certificate diagnostics, validation-calibrated RCSS scoring, auto-weight selection using selector/tuner validation splits, and validation-aware local swap refinement. This is close to a Transportation Science framing if written as a stochastic reconstruction-aware sensor network design problem.

The main paper risk is that reviewers may read the current method as an empirical candidate pool plus validation search heuristic. The project must therefore turn the implementation into a clear methodological contribution: formal objective, justified surrogate, algorithm definition fixed before evaluation, theory/intuition for posterior certificates, stronger baselines, robustness testing, and disciplined claim-evidence alignment.

Known evidence caveats:
- PeMS7_228 10-split results support strong improvements at 20% and 30% budgets, but at 10% budget `multistart_swap_by_validation` can beat `validation_swap_selected`.
- PeMS7_1026 external validation currently has fewer splits than PeMS7_228; 5/5 wins can still yield a Wilcoxon p-value around 0.0625.
- Seattle results are referenced by narrative artifacts and scripts, but curated repository results must be synchronized before Seattle becomes a core paper claim.

## Constraints

- **Target venue:** Transportation Science is the primary submission target — it best matches transportation system design, optimization, computational experiments, and data-driven planning.
- **Backup venue:** TR Part B is possible only if the project adds stronger mathematical modeling, posterior-error theory, algorithmic properties, and generality beyond PeMS tuning.
- **Claim strategy:** Strong claims should be preserved and strengthened with evidence rather than narrowed prematurely — unsupported claims must be rephrased, tested, or moved to limitations.
- **Evidence standard:** Core claims must be supported by held-out test results, paired comparisons, statistical uncertainty, robustness checks, and reproducible artifacts.
- **Reproducibility:** Raw datasets stay local and ignored; curated result summaries, scripts, and non-sensitive artifacts should remain synchronized with paper claims.
- **Implementation state:** The current evaluator is monolithic and experiment-driven; changes should avoid breaking reproducibility and should be validated with smoke runs or aggregate checks.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Target Transportation Science first | The current contribution fits transportation network design and transparent optimization better than a theory-heavy TR Part B submission in its present state | — Pending |
| Keep strong claims, but require evidence-backed wording | The research has real promise; the right response is to add evidence and sharpen claims, not dilute the contribution into a weak incremental story | — Pending |
| Use “certificate-guided” unless formal certification is proved | Current posterior diagnostics correlate with MAE but are not yet formal certificates | — Pending |
| Treat multistart validation refinement as a serious comparator or portfolio member | At 10% budget it can outperform validation-swap RCSS, so ignoring it would invite reviewer criticism | — Pending |
| Make Seattle evidence either curated or non-core | Repository/paper consistency is necessary for reproducibility and reviewer trust | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd:complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026/05/21 after initialization*
