# Phase 5: Robustness and Generality - Context

**Gathered:** 2026-05-23
**Status:** Ready for planning
**Mode:** Auto-selected decisions from `/gsd-autonomous --from 4 非必要不要询问我，请自动推进`

<domain>
## Phase Boundary

This phase adds deployment-like robustness and generality evidence for TRACE-SL after the Phase 4 held-out evidence package. It must cover sensor failures, observation noise, missing readings/time blocks, heterogeneous sensor costs or a documented proxy, temporal distribution shift where timestamps support it, and candidate-count sensitivity across 50/100/200/500-style budgets.

The phase should extend the existing research pipeline rather than create a separate notebook workflow. Primary implementation should reuse `TRC-23-02333/transparent_estimator_eval.py`, `TRC-23-02333/summarize_trace_sl_rcss.py`, and reproducible shell launchers under `scripts/`. New evidence artifacts should live under curated `TRC-23-02333/trace_sl_results/` stage directories. Raw datasets under `TRC-23-02333/dataset/` remain local/ignored and must not be committed or cited as evidence.

</domain>

<decisions>
## Implementation Decisions

### Robustness Evidence Scope
- **D-01:** Phase 5 evidence must be artifact-backed CSV/Markdown/script output, not prose-only claims or pending commands.
- **D-02:** Use held-out GLS/MAP test metrics as the main robustness performance evidence; validation MAE remains selection/tuning evidence.
- **D-03:** Preserve Phase 4 stable method/layout labels, especially `validation_swap_selected`, `rcss_selected`, `multistart_swap_by_validation`, `greedy_a_trace`, `greedy_d_logdet`, `observability_proxy`, `graph_sampling_laplacian`, and `qr_pod_modes`.
- **D-04:** Treat Phase 5 as stress-test evidence for usefulness under perturbations, not as a proof of universal deployment robustness.

### Perturbation and Generality Design
- **D-05:** Sensor-failure experiments should drop a configured fraction of selected sensors after layout selection and record actual active sensor count, using rates 0.05, 0.10, and 0.20 plus an unperturbed baseline.
- **D-06:** Observation-noise experiments should perturb observed sensor readings at validation/test evaluation time with deterministic seeds and record noise scale/condition labels in `metrics.csv`.
- **D-07:** Missingness experiments should support random observed-reading missingness and at least one contiguous time-block missingness mode when test sequences are long enough.
- **D-08:** Heterogeneous sensor-cost evidence can be a deterministic proxy if full cost-aware placement is too broad: derive costs from observable graph/traffic properties, enforce or report cost-budget feasibility, and document limitations.
- **D-09:** Temporal distribution shift should use chronological/time-blocked day splits when dataset timestamps support it; if a dataset lacks trustworthy timestamps, document that limitation rather than fabricating shift evidence.
- **D-10:** Candidate-count sensitivity should build on Stage 13 and include performance plus runtime for 50, 100, 200, and 500-style candidate budgets when tractable; if only a minimal sweep is committed, the caveat must be explicit.

### Implementation Strategy
- **D-11:** Insert perturbations at evaluator boundaries (`evaluate_layout`, `validation_mae`, `solve_quadratic`, dataset splitting) so all layout types are evaluated consistently.
- **D-12:** Every generated metric row for robustness runs must include machine-readable condition columns such as `robustness_family`, `robustness_condition`, `failure_rate`, `noise_scale`, `missing_rate`, `missing_block_steps`, `cost_budget`, `split_mode`, and/or `candidate_count` when applicable.
- **D-13:** Extend aggregation to group by robustness/candidate/split condition columns before comparing layouts; do not collapse stress settings into one mean.
- **D-14:** Prefer a small PeMS7_228 Stage 14 robustness bundle with deterministic seeds and reduced runtime defaults over an unbounded multi-dataset sweep.
- **D-15:** Full external-dataset robustness is optional/supporting unless local runtime is clearly tractable; Phase 5 completion requires PeMS7_228 core robustness and documented external/generalization status.
- **D-16:** Phase 5 must end with a validator that checks ROBUST-01..06, required condition columns, result directories, runtime/candidate coverage, and raw-data hygiene.

### Claude's Discretion
The planner may split this phase into evaluator-support, summarization/validation, Stage 14 launch/evidence, and documentation/claim-sync plans. Bias toward minimal, testable changes and curated artifacts. Avoid broad solver refactors unless needed to implement the required perturbation hooks.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### GSD Scope and Requirements
- `.planning/ROADMAP.md` — Defines Phase 5 goal, ROBUST-01..ROBUST-06, success criteria, and Phase 4 dependency.
- `.planning/REQUIREMENTS.md` — Defines robustness/generalization requirements and raw-data/reproducibility constraints.
- `.planning/STATE.md` — Current workflow state and active decisions.
- `.planning/PROJECT.md` — Defines target venue and evidence standard.
- `.planning/phases/04-core-experiment-evidence/04-CONTEXT.md` — Locks Phase 4 evidence discipline, stable labels, raw-data boundary, and runtime/candidate sensitivity framing.
- `.planning/phases/04-core-experiment-evidence/04-VERIFICATION.md` — Defines what Phase 4 delivered and which caveats remain.
- `.planning/phases/04-core-experiment-evidence/04-REVIEW.md` — Confirms Stage 12/13 review findings are resolved.
- `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` — Claim/evidence contract to update with Phase 5 robustness status if needed.

### Experiment Sources
- `TRC-23-02333/transparent_estimator_eval.py` — Primary evaluator, data splitting, layout generation, validation selection, reconstruction evaluation, and per-seed artifact writer.
- `TRC-23-02333/summarize_trace_sl_rcss.py` — Aggregates metrics, paired tests, certificate summaries, candidate sensitivity, runtime sensitivity, and Markdown summaries.
- `scripts/run_stage12_pems7_228.sh` — Primary Stage 12 PeMS7_228 baseline-portfolio launcher pattern.
- `scripts/run_stage13_candidate_sensitivity_pems7_228.sh` — Candidate-count/runtime sensitivity launcher pattern.
- `TRC-23-02333/trace_sl_results/README.md` — Curated result inventory and interpretation guidance.
- `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/` — Primary in-domain evidence bundle to extend or compare against.
- `TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/` — Existing candidate-count/runtime sensitivity evidence.

### Codebase Maps
- `.planning/codebase/ARCHITECTURE.md` — Evaluator/artifact flow if present.
- `.planning/codebase/STRUCTURE.md` — Script/result directory conventions if present.
- `.planning/codebase/TESTING.md` — Existing smoke/schema validation patterns if present.
- `.planning/codebase/CONVENTIONS.md` — Naming/reproducibility conventions if present.

</canonical_refs>

<code_context>
## Existing Code Insights

- `split_daily_frame(frame, dates, seed)` currently randomizes whole days into train/validation/test; it is the anchor for chronological/time-blocked split support.
- `evaluate_layout(test, tod, distance, laplacian, precision, mean, std, sensors, args)` centralizes held-out reconstruction metrics and is the main insertion point for sensor drops, noisy observations, and missing observed readings.
- `solve_quadratic(observed_z, prior_z, sensors, matrix, obs_weight)` assumes a fixed sensor set and uniform observation weight; robustness support may require passing active sensors or per-node weights.
- `validation_mae(...)` reuses `evaluate_layout(...)`; perturbation semantics must be explicit so selection/tuning and final test evidence do not accidentally mix conditions.
- Per-row output is assembled around `rows.append(row)` near the main loop; robustness condition columns should be added there so summaries remain machine-readable.
- `write_summary(...)` and `summarize_trace_sl_rcss.py` currently aggregate by budget/layout/method and candidate_count when present; Phase 5 plans must add robustness condition grouping before result interpretation.
- Stage 13 already provides a candidate-count launcher and runtime CSV pattern, but Phase 5 needs 50/100/200/500 coverage or explicit tractability caveat.

</code_context>

<specifics>
## Specific Ideas

- Add small pure helper functions for perturbation masks/noise/drop-cost proxies and tests around them before wiring CLI flags.
- Add `--robustness-family`, `--failure-rates`, `--noise-scales`, `--missing-rates`, `--missing-block-steps`, `--split-mode`, and cost-proxy flags only if the executor confirms simple signatures are enough.
- Use a Stage 14 PeMS7_228 launcher with `DRY_RUN=1`, BLAS thread caps, seed/budget/layout/candidate-count defaults, and a minimal committed run that closes ROBUST requirements.
- Create `.planning/phases/05-robustness-and-generality/validate_phase5_robustness.py` to verify every ROBUST requirement from artifacts.
- Update `TRC-23-02333/trace_sl_results/README.md` and, if appropriate, the Phase 1 claim-evidence contract with robustness status and caveats.

</specifics>

<deferred>
## Deferred Ideas

- Large-scale solver refactoring, sparse/rank-update posterior solvers, and larger-network scalability belong to v2.
- Full paper-ready tables/figures belong to Phase 6 or the paper-writing phase, though Phase 5 should generate source CSVs.
- Raw dataset deletion, movement, upload, or commit is out of scope.
- Full external dataset robustness is optional/supporting unless runtime and local data availability make it safe.

</deferred>

---

*Phase: 05-robustness-and-generality*
*Context gathered: 2026-05-23*
