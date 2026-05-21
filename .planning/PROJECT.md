# TRACE-SL Transportation Science Preparation

## What This Is

TRACE-SL is a research codebase and reproducibility package for sparse traffic sensor placement aimed at full-network traffic state reconstruction. The project turns the current strong experimental prototype into a Transportation Science-ready methodological paper by strengthening the formulation, theory bridge, baselines, robustness evidence, and repository consistency.

The intended paper positioning is not black-box traffic imputation or forecasting. It is transparent reconstruction-aware traffic sensor network design: given a traffic network, historical states, a sparse sensor budget, and a transparent GLS/MAP/GSP reconstruction model, choose sensor layouts that improve hidden-link reconstruction quality with interpretable posterior certificates.

## Core Value

Maintain a strong TRACE-SL claim and make the method, theory, and experiments strong enough that the claim is supported by evidence rather than weakened by cautious wording.

## Requirements

### Validated

- ✓ TRACE-SL experiment pipeline can run multi-split sparse sensor layout studies on PeMS7_228, PeMS7_1026, and Seattle-style datasets — existing
- ✓ Current pipeline evaluates transparent reconstruction methods including historical mean, neighbor average, GSP, and GLS/MAP — existing
- ✓ Current pipeline produces RCSS-style candidate diagnostics, validation-aware swap results, posterior certificates, paired summaries, and reproducibility artifacts — existing
- ✓ Codebase already contains curated PeMS7_228 and PeMS7_1026 Stage 11 result artifacts and documentation for reproduction — existing

### Active

- [ ] Formalize TRACE-SL as a transparent reconstruction-aware stochastic sensor placement problem rather than an empirical candidate-search heuristic.
- [ ] Establish a principled bridge between GLS/MAP posterior certificates and expected hidden-link reconstruction error.
- [ ] Preserve the strong TRACE-SL claim by adding experiments and method evidence that support it directly.
- [ ] Resolve the low-budget multistart-vs-RCSS issue without post-hoc cherry-picking, either by predefined portfolio selection or clearer algorithmic positioning backed by results.
- [ ] Add stronger Transportation Science-level baselines: observability-inspired, A-/D-optimal design, graph sampling/GSP, QR/SVD/POD sparse placement, and at least one learning-based reconstruction check if feasible.
- [ ] Expand external validation and statistical reporting so claims are supported by enough splits, confidence intervals, effect sizes, and paired tests.
- [ ] Add robustness experiments for sensor failure, observation noise, missingness, non-uniform sensor costs, temporal distribution drift, and candidate-count sensitivity.
- [ ] Fix repository/paper consistency around Seattle outputs and all narrative claims before paper drafting.
- [ ] Generate publication-ready tables/figures directly from checked result artifacts.
- [ ] Prepare a Transportation Science-first paper narrative, with TR Part B retained only if theory and algorithmic analysis become substantially stronger.

### Out of Scope

- Directly submitting the current prototype without major strengthening — current evidence is promising but not yet sufficient for the target claim.
- Narrowing TRACE-SL into a conservative “competitive candidate generator” claim — the user explicitly wants strong claims supported by stronger evidence.
- Treating “certified” as a formal guarantee unless a matching theorem or bound is added — use certificate-guided/posterior-certificate-aware language otherwise.
- Making Seattle a core paper claim while its outputs are not curated and consistent with the repository — either curate it or remove it from the main evidence line.
- Replacing the transparent model-based story with a black-box GNN-only paper — learning baselines may be checks, not the main contribution.

## Context

The current review-style guidance judges the direction as promising but not yet ready for Transportation Science or Transportation Research Part B in its current form. The main risk is that reviewers may see the current contribution as an empirical candidate pool plus validation search heuristic, not as an independent and generalizable transportation OR methodology.

The recommended venue strategy is Transportation Science first, with TR Part B as a more ambitious backup only after adding harder mathematical modeling, properties, algorithmic analysis, and stronger generality. The project should frame TRACE-SL against classic traffic sensor location and observability work by emphasizing that TRACE-SL does not seek deterministic full observability; it optimizes reconstruction quality, uncertainty, and robustness under partial observation and finite budgets.

The strongest current assets are the transparent reconstruction model, posterior diagnostics, OR-guided candidate generation, validation calibration, validation-aware swap refinement, multi-split PeMS evidence, and certificate-error empirical correlations. The main evidence gaps are low-budget competition against multistart validation refinement, limited external split count, missing/unclear Seattle curation, insufficient strong baselines, and lack of robustness experiments.

Existing code is a CPU-oriented Python research pipeline centered on `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`, and shell launchers under `scripts/`. Existing codebase mapping is available under `.planning/codebase/` and should inform phase planning.

## Constraints

- **Claim strategy**: Strong TRACE-SL claims must be preserved and supported with experiments/theory; do not solve weaknesses by narrowing the contribution.
- **Venue strategy**: Optimize first for Transportation Science; treat TR Part B as conditional on stronger formal analysis.
- **Evidence standard**: Claims must trace to raw or curated result artifacts; paper narrative must not outrun repository evidence.
- **Reproducibility**: Preserve local TRC datasets; they are ignored from Git and must not be deleted without confirmation.
- **Transparency**: Keep GLS/MAP/GSP and posterior certificates central; learning baselines are comparison checks, not the identity of the method.
- **Computation**: Current pipeline is CPU-oriented and uses dense matrix operations; large-network or high-candidate experiments need careful runtime planning.
- **Artifact hygiene**: New curated results should live under `TRC-23-02333/trace_sl_results/<dataset>_<stage>/` and avoid overwriting published directories without traceability.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Target Transportation Science first | Current work fits transportation system design, optimization, computational experiments, and transparent model-based sparse sensing better than a theory-heavy TR Part B submission. | — Pending |
| Preserve strong TRACE-SL claim | User explicitly wants strong claims, provided the evidence is strengthened to support them. | — Pending |
| Strengthen evidence rather than narrow narrative | Low-budget and baseline gaps should be fixed through method/experiment design, not rhetorical retreat. | — Pending |
| Use “certificate-guided” unless formal guarantees are proven | Current certificate evidence is empirical and principled, but not yet a formal certificate. | — Pending |
| Treat Seattle as conditional evidence | Seattle can strengthen cross-network generality only if outputs are curated and consistent with documentation. | — Pending |

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
