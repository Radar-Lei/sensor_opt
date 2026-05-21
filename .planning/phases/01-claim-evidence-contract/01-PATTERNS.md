# Phase 1: Claim-Evidence Contract - Pattern Map

**Mapped:** 2026-05-21
**Files analyzed:** 1 recommended target artifact
**Analogs found:** 1 / 1

## Scope Extraction

`01-CONTEXT.md` 未给出具体待创建文件名，但明确 Phase 1 的主输出应位于 `.planning/phases/01-claim-evidence-contract/`，且“如果创建 reusable claim matrix，后续阶段应更新它”。因此推荐 planner 创建单一 phase-local Markdown 合同文件：

- `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md`

Phase 1 应引用现有 claim/evidence 文档和 curated result artifacts，不修改算法代码，不读取 `TRC-23-02333/dataset/` 原始数据。

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` | planning artifact / documentation | evidence-traceability transform | `.planning/REQUIREMENTS.md` + `.planning/ROADMAP.md` | role-match |

## Pattern Assignments

### `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` (planning artifact, evidence-traceability transform)

**Primary analogs:**
- `.planning/REQUIREMENTS.md` for requirement IDs, checkboxes, traceability table.
- `.planning/ROADMAP.md` for phase goal, requirements, success criteria, dependencies.
- `NARRATIVE_REPORT.md` and `TRC-23-02333/trace_sl_results/*/SUMMARY.md` for current claim/evidence snippets.

**Header/status pattern** — copy from `.planning/ROADMAP.md` lines 0-8 and `.planning/phases/01-claim-evidence-contract/01-CONTEXT.md` lines 0-4:

```markdown
# Roadmap: TRACE-SL Transportation Science Readiness

**Created:** 2026/05/21
**Mode:** Vertical MVP
**Granularity:** Standard

## Objective

Turn TRACE-SL from a strong experimental prototype into a Transportation Science-ready methodology paper while preserving strong claims and making every claim evidence-backed.
```

Use a concise phase header with date/status, e.g. `# Phase 1: Claim-Evidence Contract`, `**Status:** Draft contract for downstream phases`.

**Phase boundary pattern** — copy constraints from `.planning/phases/01-claim-evidence-contract/01-CONTEXT.md` lines 5-10:

```markdown
## Phase Boundary

This phase delivers the paper-facing claim-evidence contract for TRACE-SL before additional experiments, theory writing, or manuscript drafting. It locks the strongest defensible contribution claims, defines what evidence each claim requires, constrains terminology around certificates, handles the 10% PeMS7_228 multistart caveat, and positions TRACE-SL against deterministic full-observability TSLP and black-box imputation/forecasting.

It does not implement new baselines, run new experiments, prove theory, generate final paper tables, or rewrite the full manuscript. Those belong to later phases.
```

**Requirement-ID pattern** — copy from `.planning/REQUIREMENTS.md` lines 9-15:

```markdown
### Claim and Framing

- [ ] **CLAIM-01**: The paper states TRACE-SL as a transparent reconstruction-aware sensor placement problem, not as an ad hoc candidate-pool heuristic.
- [ ] **CLAIM-02**: Every primary contribution claim maps to explicit evidence: held-out experiment, robustness result, statistical comparison, theorem/derivation, or limitation note.
- [ ] **CLAIM-03**: The main performance claim avoids “best at all budgets” wording and correctly handles the 10% PeMS7_228 multistart-vs-RCSS caveat.
- [ ] **CLAIM-04**: The paper uses “certificate-guided” or equivalent wording unless a formal certificate theorem is added.
- [ ] **CLAIM-05**: The positioning distinguishes TRACE-SL from deterministic full-observability TSLP and from black-box traffic imputation/forecasting.
```

For the contract, use stable claim IDs such as `C-01..C-05` and map each back to `CLAIM-01..CLAIM-05`.

**Traceability table pattern** — copy from `.planning/REQUIREMENTS.md` lines 95-105:

```markdown
## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| CLAIM-01 | Phase 1 | Pending |
| CLAIM-02 | Phase 1 | Pending |
| CLAIM-03 | Phase 1 | Pending |
| CLAIM-04 | Phase 1 | Pending |
| CLAIM-05 | Phase 1 | Pending |
```

Adapt into a machine-auditable claim matrix with required columns from `01-CONTEXT.md` lines 42-43: `claim ID`, `claim wording`, `evidence required`, `current evidence source`, `caveat/limitation wording`, `downstream phase owner`.

**Decision-to-contract pattern** — copy locked decisions from `01-CONTEXT.md` lines 17-43:

```markdown
- **D-03:** The claim contract must separate method contribution, performance evidence, certificate evidence, and scope/limitations so later writing can strengthen unsupported claims with evidence rather than prematurely weakening them.
- **D-04:** Every primary claim must map to one or more explicit evidence types: held-out test result, paired/statistical comparison, robustness test, external-network evidence, formal derivation/theory, reproducible artifact, or limitation wording.
- **D-06:** The matrix should mark evidence status as present, needs audit, needs new experiment, theory-dependent, or wording-only limitation.
```

Use exactly these status values unless the planner has a strong reason to add a new one.

**Canonical reference pattern** — copy source list from `01-CONTEXT.md` lines 47-73:

```markdown
### Current Narrative and Claim Sources
- `README.md` — Current public-facing TRACE-SL overview, main claim, results, and reproduction entry points.
- `NARRATIVE_REPORT.md` — Writing handoff with current core claim, method summary, Stage 9-11 evidence, PeMS7_1026/Seattle discussion, certificate validity, and claim status.
- `TRC-23-02333/trace_sl_results/README.md` — Curated result inventory and guidance to use `validation_swap_selected` as the current main method.
```

In the new contract, include a `## Source Register` section that lists evidence sources but does not copy raw data.

**Current claim wording pattern** — copy from `NARRATIVE_REPORT.md` lines 6-9:

```markdown
## Core Claim

TRACE-SL improves full-network traffic state reconstruction by optimizing sensor placement for the recoverability of a transparent inverse problem. Its key mechanism is not a black-box state estimator, but an OR-guided sensor-layout search that uses posterior uncertainty, robust scenario risk, validation reconstruction error, and spatial coverage to select layouts that generalize better than random or topology-only placement.
```

Use this as the seed wording for `C-01 Method contribution`, but add evidence status and downstream owner.

**Recommended final claim wording pattern** — copy from `idea-stage/IDEA_REPORT.md` lines 138-147:

```markdown
> TRACE-SL is a transparent reconstruction-aware sensor placement framework. It builds a pre-specified portfolio of certificate-guided, scenario-risk, coverage-diverse, random-validation, and validation-swap layout generators, then selects layouts through nested validation for a GLS/MAP reconstruction objective. Across PeMS and Seattle networks, the resulting layouts reduce hidden-link reconstruction error relative to random, validation-selected random, variance/topology, and standard OR baselines; at very low budgets, multistart validation refinement emerges as a strong portfolio component rather than a failure of the framework.

Avoid:

- “Certified” unless qualified as empirical/posterior certificates.
- “Best at all budgets.”
- Presenting auto-weight or final candidate choice as manually tuned after seeing test results.
- Treating Seattle as full-strength external validation unless its protocol/result directory is fully curated in the repository and paper artifact list.
```

Use this as a candidate paper-facing wording row, but mark Seattle as `conditional/supporting-only` per Phase 1 decisions.

**Existing claim matrix pattern** — copy from `refine-logs/EXPERIMENT_PLAN.md` lines 7-15:

```markdown
## Claim Matrix

| Claim | Evidence | Required? |
|---|---|---|
| C1: Transparent estimators can reconstruct full-network state from sparse sensors | GSP/GLS/Kalman hidden MAE/RMSE vs baselines | 必须 |
| C2: OR layout improves reconstruction vs random/topology-only | Budget sweep and paired tests | 必须 |
| C3: Certificates explain layout quality | correlation between trace/logdet/coherence/condition and hidden error | 必须 |
| C4: RL is useful only if it amortizes search | solve time/quality across budgets/networks | 条件必须 |
| C5: Regime-aware layouts reveal TS insight | free-flow vs congestion layouts and budget marginal value | 强烈建议 |
```

Do not reuse the old RL-centric rows verbatim. Copy the table shape only, then replace with Phase 1 TRACE-SL claim IDs and evidence statuses.

**Evidence summary pattern** — copy from `NARRATIVE_REPORT.md` lines 113-127:

```markdown
Mean GLS/MAP test MAE across 10 splits:

| Budget | Auto-weight validation-swap RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.6055 | 3.6913 | 3.8359 | 3.7304 |
| 20% | 3.3095 | 3.3969 | 3.5648 | 3.4276 |
| 30% | 3.0665 | 3.1832 | 3.4032 | 3.2004 |

Auto-weight validation-swap deltas across 10 splits, negative is better:

| Budget | vs random mean | vs best random by validation | vs top variance | paired t-test p vs best-random | Wilcoxon p vs best-random |
|---:|---:|---:|---:|---:|---:|
| 10% | -0.2304 | -0.0858 | -0.1249 | 0.0343 | 0.0273 |
```

In the contract, cite these as `present / needs audit` rather than recomputing. The row must distinguish validation selection evidence from held-out test performance evidence.

**Low-budget caveat evidence pattern** — copy from `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/SUMMARY.md` lines 9-14 and paired-test lines 121-128:

```markdown
 budget                   layout_type     mean      std  count
    0.1 multistart_swap_by_validation 3.578255 0.296331     10
    0.1   swap_from_best_random_trace 3.598399 0.291192     10
    0.1                 rcss_selected 3.602807 0.293477     10
    0.1      validation_swap_selected 3.605467 0.287149     10
```

```markdown
 budget                   layout                      baseline  delta_mean  delta_std  win_count  count   paired_t_p  wilcoxon_p
    0.1 validation_swap_selected multistart_swap_by_validation    0.027213   0.042666          3     10 7.449269e-02    0.083984
```

Every performance claim row should reserve a caveat field for this comparator/portfolio issue.

**External-network evidence pattern** — copy from `NARRATIVE_REPORT.md` lines 139-161:

```markdown
### PeMS7_1026 external validation

Directory: `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`

PeMS7_1026 uses the same Stage 11 pipeline with 100 random layouts and 100 quality-coverage candidates per split. This is an external-network validation relative to the PeMS7_228 development and confirmatory runs.

Mean GLS/MAP test MAE across five PeMS7_1026 splits:

| Budget | Validation-swap RCSS | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.6557 | 3.7437 | 3.8266 | 3.8602 |
| 20% | 3.2547 | 3.4653 | 3.5317 | 3.5859 |
| 30% | 2.9951 | 3.2483 | 3.3309 | 3.3266 |
```

Mark PeMS7_1026 as `present / lower split count; Phase 4 owner for audit or extension`.

**Certificate evidence pattern** — copy from `NARRATIVE_REPORT.md` lines 187-198:

```markdown
### Certificate validity

GLS/MAP posterior certificates are stable predictors of hidden reconstruction error in the 10-split Stage 11 aggregate:

| Certificate | Pearson with MAE | Spearman with MAE |
|---|---:|---:|
| posterior trace | 0.8612 | 0.8513 |
| condition number | 0.8327 | 0.8592 |
| information logdet | -0.8209 | -0.8130 |
```

Use this for empirical interpretability claims only. Formal posterior-error theory rows should be `theory-dependent` and assigned to Phase 2.

**Curated artifact inventory pattern** — copy from `TRC-23-02333/trace_sl_results/README.md` lines 17-33:

```markdown
## Key Stage 11 files

- `SUMMARY.md`: human-readable aggregate table.
- `combined_metrics.csv`: all seed-level evaluation rows.
- `gls_map_layout_summary.csv`: GLS/MAP mean MAE by budget and layout type.
- `gls_map_delta_summary.csv`: RCSS deltas against selected baselines.
- `gls_map_win_counts.csv`: per-budget winner counts.
- `combined_certificate_correlations.csv`: seed-level certificate/error correlations.
- `certificate_correlation_summary.csv`: aggregate certificate stability table.
- `combined_rcss_candidates.csv`: candidate-level RCSS diagnostics.
- `rcss_selected_sources.csv`: selected candidate source counts.
- `validation_swap_delta_tests.csv`: paired tests for validation-swap RCSS against validation-selected random.
- `auto_weight_selection_summary.csv`: selected auto-weight patterns by budget and split.

## Reading the results

Use `validation_swap_selected` as the current main method. Use the PeMS7_228 10-split directory for the main in-domain table and the PeMS7_1026 directory for external validation; compare against `best_random_by_validation`, `random`, and `top_variance`.
```

The contract should cite CSV/summary file paths in `current evidence source`, not embed all numeric tables.

## Shared Patterns

### Evidence status taxonomy
**Source:** `01-CONTEXT.md` lines 22-35 and 42-43  
**Apply to:** all claim rows

Use these statuses exactly:

```markdown
present | needs audit | needs new experiment | theory-dependent | wording-only limitation
```

Recommended evidence-type vocabulary:

```markdown
held-out test result | paired/statistical comparison | robustness test | external-network evidence | formal derivation/theory | reproducible artifact | limitation wording
```

### Validation-vs-test separation
**Source:** `01-CONTEXT.md` lines 22-25 and code context lines 83-86  
**Apply to:** performance rows and method-selection rows

Pattern:

```markdown
Validation MAE is selection evidence only, not final performance evidence. Final performance claims must point to held-out test metrics from curated result artifacts.
```

### Certificate terminology guardrail
**Source:** `01-CONTEXT.md` lines 32-35  
**Apply to:** certificate/interpretable-method rows

Pattern:

```markdown
Use “certificate-guided”, “posterior-certificate-aware”, or “certificate diagnostics” language unless Phase 2 adds theorem-level formal certification.
```

### Scope and source hygiene
**Source:** `01-CONTEXT.md` lines 88-91 and `.planning/codebase/STRUCTURE.md` lines 37-47  
**Apply to:** all Phase 1 planning

Pattern:

```markdown
Do not read or commit raw files under `TRC-23-02333/dataset/` for this phase. Reference curated result summaries under `TRC-23-02333/trace_sl_results/` instead.
```

## Recommended Contract Skeleton

Planner should create the target artifact with this structure:

```markdown
# Phase 1: Claim-Evidence Contract

**Status:** Draft contract for downstream phases
**Date:** 2026-05-21

## Phase Boundary
## Source Register
## Claim-Evidence Matrix
| Claim ID | Requirement | Claim wording | Evidence required | Current evidence source | Evidence status | Caveat / limitation wording | Downstream phase owner |
|---|---|---|---|---|---|---|---|
## Reserved Caveats and Guardrails
## Downstream Phase Routing
## Non-Goals for Phase 1
```

## No Analog Found

No file lacked a usable analog. The exact target artifact is new, but its structure should be assembled from existing planning and evidence documents rather than invented from scratch.

## Metadata

**Analog search scope:** repository root Markdown, `.planning/`, `refine-logs/`, `idea-stage/`, and curated `TRC-23-02333/trace_sl_results/` summaries.  
**Excluded scope:** `TRC-23-02333/dataset/` raw data.  
**Files read for extraction:** 15.  
**Pattern extraction date:** 2026-05-21.
