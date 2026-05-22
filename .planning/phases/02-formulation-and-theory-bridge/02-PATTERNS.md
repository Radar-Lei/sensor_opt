# Phase 2: Formulation and Theory Bridge - Pattern Map

**Mapped:** 2026-05-22
**Files analyzed:** 4
**Analogs found:** 4 / 4

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `/home/samuel/projects/sensor_opt/.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md` | documentation / method artifact | transform | `/home/samuel/projects/sensor_opt/.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` | role-match |
| `/home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md` | documentation / narrative | transform | `/home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md` | exact-existing |
| `/home/samuel/projects/sensor_opt/README.md` | documentation / public overview | transform | `/home/samuel/projects/sensor_opt/README.md` | exact-existing |
| `/home/samuel/projects/sensor_opt/.planning/phases/02-formulation-and-theory-bridge/02-TR-PART-B-THEORY-GAP-NOTE.md` | documentation / theory note | transform | `/home/samuel/projects/sensor_opt/refine-logs/WRITING_NOTES_GREEDY_OFFLINE_PLANNING.md` | role-match |

## Pattern Assignments

### `/home/samuel/projects/sensor_opt/.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md` (documentation / method artifact, transform)

**Analog:** `/home/samuel/projects/sensor_opt/.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md`

**Artifact header and boundary pattern** (lines 0-18):
```markdown
# Phase 1: Claim-Evidence Contract

**Status:** Draft contract for downstream phases  
**Date:** 2026-05-21

## Phase Boundary

This phase delivers the paper-facing claim-evidence contract for TRACE-SL before additional experiments, theory writing, or manuscript drafting. It locks the strongest defensible contribution claims, defines what evidence each claim requires, constrains terminology around certificates, handles the 10% PeMS7_228 multistart caveat, and positions TRACE-SL against deterministic full-observability TSLP and black-box imputation/forecasting.

It does not implement new baselines, run new experiments, prove theory, generate final paper tables, or rewrite the full manuscript. Those belong to later phases.

For Phase 1 execution, this means:

- No new experiments.
- No algorithm edits.
- No baseline implementation.
- No raw dataset reads.
- No final manuscript writing.
```

**Source register pattern** (lines 19-48):
```markdown
## Source Register

### Planning and Claim-Scope Sources

- `.planning/PROJECT.md` — project value, target venue, constraints, and active decisions.
- `.planning/STATE.md` — current workflow state and active decisions for Phase 1.
- `.planning/ROADMAP.md` — Phase 1 goal, requirements CLAIM-01..CLAIM-05, and downstream phase responsibilities.
- `.planning/REQUIREMENTS.md` — claim/framing requirements and global out-of-scope constraints.
- `.planning/phases/01-claim-evidence-contract/01-CONTEXT.md` — user decisions D-01..D-15 and Phase 1 boundary.
- `.planning/phases/01-claim-evidence-contract/01-PATTERNS.md` — artifact structure, evidence vocabulary, and source hygiene patterns.
- `README.md` — current public-facing TRACE-SL framing and reproduction entry points.
- `NARRATIVE_REPORT.md` — current method summary, evidence narrative, and claim status.
```

**Matrix/table pattern to copy for theory requirements** (lines 50-64):
```markdown
## Claim-Evidence Matrix

Evidence status taxonomy: present | needs audit | needs new experiment | theory-dependent | wording-only limitation

Evidence type vocabulary: held-out test result | paired/statistical comparison | robustness test | external-network evidence | formal derivation/theory | reproducible artifact | limitation wording

Validation MAE is selection evidence only, never final performance evidence. Final performance claims must point to held-out test metrics from curated result artifacts.

| Claim ID | Requirement | Claim wording | Evidence required | Current evidence source | Evidence status | Caveat / limitation wording | Downstream phase owner |
|---|---|---|---|---|---|---|---|
```

**Guardrail pattern** (lines 66-74):
```markdown
## Reserved Caveats and Guardrails

- **No “best at all budgets” claim (D-08):** The contract prohibits unsupported wording that TRACE-SL is best at all budgets or against every comparator. Claims must be scoped to supported held-out test evidence and named baselines.
- **No formal “certified” branding without theorem-level support (D-10, D-11):** Use certificate-guided, posterior-certificate-aware, or certificate diagnostics only. Posterior trace, condition number, and information logdet correlations are empirical guidance and interpretability evidence, not formal certified optimality or guaranteed reconstruction-error bounds.
- **No validation MAE as final performance evidence (D-05):** Validation MAE can select, tune, or refine layouts; it cannot be cited as final performance evidence. Final performance claims require held-out test metrics and paired/statistical comparison evidence from curated artifacts.
```

**Planner guidance:** Use the same phase-local Markdown structure, but replace claim rows with THEORY-01..THEORY-06 rows. Include sections for formal problem, TRACE-SL/RCSS surrogate, GLS/MAP posterior-error derivation, MAE bridge, validation-swap complexity/local optimality, TR Part B gap note, guardrails, and self-check.

---

### `/home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md` (documentation / narrative, transform)

**Analog:** `/home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md`

**Current claim wording to preserve and strengthen** (lines 6-9):
```markdown
## Core Claim

TRACE-SL improves full-network traffic state reconstruction by optimizing sensor placement for the recoverability of a transparent inverse problem. Its key mechanism is not a black-box state estimator, but an OR-guided sensor-layout search that uses posterior uncertainty, robust scenario risk, validation reconstruction error, and spatial coverage to select layouts that generalize better than random or topology-only placement.
```

**Method-summary pattern** (lines 10-29):
```markdown
## Method Summary

TRACE-SL uses GLS/MAP and GSP as transparent full-network reconstruction models. Given a candidate sensor set, the hidden-link reconstruction error is evaluated under deployment simulation: only selected sensors are observed, while non-sensor nodes are held out for MAE/RMSE evaluation.

The strengthened method is **Robust Certified Sensor Search (RCSS)**:

1. Build a candidate pool from multiple OR-guided layout generators:
   - greedy A-optimal posterior trace;
   - greedy D-optimal logdet;
   - scenario-average A-trace;
   - scenario-CVaR A-trace;
   - posterior-trace swap refinements;
   - quality-coverage sampling, which samples high posterior-uncertainty nodes while enforcing spatial diversity;
   - simple degree, top-variance, and coverage baselines;
   - validation-ranked random candidates for comparison.
2. Select RCSS weights by inner validation rather than fixing them manually. The validation days are split into `selector_val` and `tuner_val`; each candidate weight vector selects a layout on `selector_val`, and the vector with the lowest `tuner_val` GLS/MAP MAE is used.
3. Select the layout with the resulting data-driven score and evaluate it on unseen test days.
4. Refine the strongest RCSS candidates with validation-aware stochastic swap search. The swap search only accepts exchanges that improve validation GLS/MAP reconstruction error, using the OR-guided candidate pool as the add-node universe.
```

**Certificate-validity wording to keep empirical, not formal certification** (lines 187-197):
```markdown
### Certificate validity

GLS/MAP posterior certificates are stable predictors of hidden reconstruction error in the 10-split Stage 11 aggregate:

| Certificate | Pearson with MAE | Spearman with MAE |
|---|---:|---:|
| posterior trace | 0.8612 | 0.8513 |
| condition number | 0.8327 | 0.8592 |
| information logdet | -0.8209 | -0.8130 |

This supports the interpretability claim: the OR certificates are not decorative; they are strongly aligned with empirical hidden-link reconstruction quality.
```

**Planner guidance:** Add Phase 2 method/theory bridge text near `## Method Summary` or as a new theory subsection. Preserve strong wording, but add formal notation and assumptions. Do not turn certificate correlations into guaranteed MAE bounds.

---

### `/home/samuel/projects/sensor_opt/README.md` (documentation / public overview, transform)

**Analog:** `/home/samuel/projects/sensor_opt/README.md`

**Overview and current-claim pattern** (lines 0-6):
```markdown
# TRACE-SL: Transparent Reconstruction-Aware Sensor Layout

TRACE-SL studies sparse traffic sensor placement for transparent full-network reconstruction. The current implementation uses GLS/MAP and GSP reconstruction evaluators, then searches for sensor layouts with Robust Certified Sensor Search (RCSS): an OR-guided candidate pool plus validation-calibrated selection and validation-aware swap refinement.

## Current claim

TRACE-SL is not framed as an RL estimator or a black-box imputation model. The core claim is that OR-guided candidate generation, transparent GLS/MAP reconstruction, and validation-calibrated swap selection produce interpretable sensor layouts that improve full-network reconstruction over strong random and topology baselines.
```

**Evidence-summary style** (lines 8-18):
```markdown
## Main PeMS7_228 result

The strongest current configuration is Stage 11: automatic RCSS weight selection with validation-aware swap refinement. The 10-split aggregate is in `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`.

| Budget | Validation-swap RCSS MAE | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.6055 | 3.6913 | 3.8359 | 3.7304 |
| 20% | 3.3095 | 3.3969 | 3.5648 | 3.4276 |
| 30% | 3.0665 | 3.1832 | 3.4032 | 3.2004 |

Paired tests against validation-selected random now support the improvement across all budgets: p=0.0343 at 10%, p=0.0025 at 20%, and p=0.00008 at 30%. Stage 11 also finds that posterior certificates remain strongly aligned with GLS/MAP hidden-link reconstruction error: posterior trace Spearman correlation is about 0.851, condition number about 0.859, and information logdet about -0.813.
```

**Repository layout pattern for cross-links** (lines 32-40):
```markdown
## Repository layout

- `TRC-23-02333/transparent_estimator_eval.py`: TRACE-SL evaluator and RCSS experiment driver.
- `TRC-23-02333/summarize_trace_sl_rcss.py`: multi-split result aggregation script.
- `TRC-23-02333/trace_sl_results/`: checked-in PeMS7_228 Stage 6--11 and PeMS7_1026 external-validation outputs.
- `scripts/run_stage11_pems7_228.sh`: reproduces Stage 11 PeMS7_228 split runs and aggregation.
- `scripts/run_stage11_pems7_1026.sh`: launches the same Stage 11 pipeline on PeMS7_1026 for external validation.
- `NARRATIVE_REPORT.md`: writing handoff with method framing and current evidence.
- `RESEARCH_PIPELINE_REPORT.md`: research pipeline progress log.
```

**Planner guidance:** If README is modified, keep it short and public-facing. Add only a compact “method formulation” paragraph, not the full derivation. Point readers to the phase-local theory artifact or later manuscript source for details.

---

### `/home/samuel/projects/sensor_opt/.planning/phases/02-formulation-and-theory-bridge/02-TR-PART-B-THEORY-GAP-NOTE.md` (documentation / theory note, transform)

**Analog:** `/home/samuel/projects/sensor_opt/refine-logs/WRITING_NOTES_GREEDY_OFFLINE_PLANNING.md`

**Theory-note header and purpose pattern** (lines 0-4):
```markdown
# Writing Note: Greedy Layout Is Offline Planning, Not Sequential Deployment

**Date**: 2026-05-18  
**Project**: TRACE-SL  
**Purpose**: Preserve the paper-writing rationale for explaining greedy A/D-optimal and swap local-search layout algorithms in a realistic transportation sensor deployment setting.
```

**Core framing pattern** (lines 6-20):
```markdown
## Core Framing

Greedy A-optimal, greedy D-optimal, and swap local search should be framed as **offline planning algorithms**, not as real-world sequential deployment protocols.

The word “greedy” describes the computational construction of a fixed sensor set under a budget constraint. It does **not** mean that an agency physically installs one sensor, waits for new traffic observations, then decides where to install the next sensor.

In practice, the workflow is:

1. Use historical full-network data, existing detector data, simulation data, or archived planning data to calibrate a transparent reconstruction model.
2. Estimate posterior covariance / uncertainty certificates for candidate sensor layouts.
3. Run greedy or local-search heuristics offline to construct a fixed deployment set `S`.
4. Deploy the selected sensor set as a planning decision.
5. In the evaluation protocol, simulate deployment by revealing only observations on `S` and measuring hidden-network reconstruction error.
```

**Suggested wording pattern** (lines 22-28):
```markdown
## Suggested Paper Wording

> We use greedy selection and swap local search as offline optimization heuristics for solving the reconstruction-aware sensor placement problem. The sequential nature of these algorithms should not be interpreted as a sequential deployment policy. Rather, the algorithms use historical calibration data to construct a fixed sensor set under a budget constraint before deployment. During deployment simulation, only the selected sensors are observed, and all unobserved locations are used solely for evaluation.
```

**Planner guidance:** Use the same short writing-note format for TR Part B theory gaps. Include “what would be needed” bullets: monotonicity, approximate submodularity, approximation guarantees, stability under covariance perturbation, and stronger stochastic/bilevel analysis. Mark these as deferred v2 unless narrowly proved in Phase 2.

---

## Implementation Source Patterns To Cite In Method/Theory Text

### Imports / numerical stack
**Source:** `/home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py` lines 0-13
```python
import argparse
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import linalg
from scipy.sparse.csgraph import shortest_path
from scipy.stats import pearsonr, spearmanr
from sklearn.covariance import LedoitWolf


SLOTS_PER_DAY = 288
```

### Train/validation/test separation
**Source:** `/home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py` lines 20-43
```python
def split_daily_frame(frame, dates, seed):
    rng = np.random.default_rng(seed)
    train_days = rng.choice(dates.to_numpy(), size=len(dates) - 4, replace=False)
    remaining = np.array([d for d in dates.to_numpy() if d not in set(train_days)])
    val_days = rng.choice(remaining, size=2, replace=False)
    test_days = np.array([d for d in remaining if d not in set(val_days)])

    train_dates = pd.to_datetime(train_days).date
    val_dates = pd.to_datetime(val_days).date
    test_dates = pd.to_datetime(test_days).date
    date_index = pd.Series(frame.index.date, index=frame.index)
    train = frame[date_index.isin(train_dates)].values
    val = frame[date_index.isin(val_dates)].values
    test = frame[date_index.isin(test_dates)].values
    test_index = frame[date_index.isin(test_dates)].index
```

### GLS/MAP reconstruction and certificate pattern
**Source:** `/home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py` lines 146-164 and 599-625
```python
def solve_quadratic(observed_z, prior_z, sensors, matrix, obs_weight):
    n_nodes = observed_z.shape[1]
    selector = np.zeros(n_nodes)
    selector[sensors] = obs_weight
    lhs = matrix + np.diag(selector)
    rhs = prior_z @ matrix.T
    rhs[:, sensors] += obs_weight * observed_z[:, sensors]
    solution = linalg.solve(lhs, rhs.T, assume_a="pos").T
    return solution, lhs


def certificate(lhs):
    inv_lhs = linalg.inv(lhs)
    sign, logdet = np.linalg.slogdet(lhs)
    return {
        "posterior_trace": float(np.trace(inv_lhs)),
        "condition_number": float(np.linalg.cond(lhs)),
        "information_logdet": float(logdet if sign > 0 else np.nan),
    }
```

```python
def evaluate_layout(test, tod, distance, laplacian, precision, mean, std, sensors, args):
    n_nodes = test.shape[1]
    sensors = np.array(sorted(sensors), dtype=int)
    hidden = np.array([i for i in range(n_nodes) if i not in set(sensors)], dtype=int)
    tod_test = historical_mean_predict(tod, test.shape[0])
    observed_z = (test - mean) / std
    prior_z = (tod_test - mean) / std
    true_hidden = test[:, hidden]
```

### Posterior trace / condition / CVaR diagnostics
**Source:** `/home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py` lines 246-272
```python
def posterior_inverse_for_layout(base_matrix, sensors, obs_weight):
    selector = np.zeros(base_matrix.shape[0])
    selector[np.asarray(sensors, dtype=int)] = obs_weight
    return linalg.inv(base_matrix + np.diag(selector))


def posterior_trace_for_layout(base_matrix, sensors, obs_weight):
    return float(np.trace(posterior_inverse_for_layout(base_matrix, sensors, obs_weight)))


def posterior_condition_for_layout(base_matrix, sensors, obs_weight):
    selector = np.zeros(base_matrix.shape[0])
    selector[np.asarray(sensors, dtype=int)] = obs_weight
    return float(np.linalg.cond(base_matrix + np.diag(selector)))


def posterior_logdet_for_layout(base_matrix, sensors, obs_weight):
    selector = np.zeros(base_matrix.shape[0])
    selector[np.asarray(sensors, dtype=int)] = obs_weight
    sign, logdet = np.linalg.slogdet(base_matrix + np.diag(selector))
    return float(logdet if sign > 0 else np.nan)
```

### RCSS surrogate scoring terms
**Source:** `/home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py` lines 424-466
```python
def rcss_candidate_scores(rows, args, weights=None):
    val_norm = normalize_minmax([row["validation_mae"] for row in rows])
    trace_norm = normalize_minmax([row["posterior_trace"] for row in rows])
    cvar_norm = normalize_minmax([row["scenario_cvar_trace"] for row in rows])
    cond_norm = normalize_minmax([math.log(max(row["condition_number"], 1.0)) for row in rows])
    coverage_norm = normalize_minmax([row["coverage_penalty"] for row in rows])
```

```python
def make_rcss_row(source, layout_id, sensors, val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args):
    sensors = np.array(sorted(int(x) for x in sensors), dtype=int)
    return {
        "source": source,
        "layout_id": layout_id,
        "sensors": sensors,
        "validation_mae": validation_mae(val, tod, distance, laplacian, precision, mean, std, sensors, args),
        "posterior_trace": posterior_trace_for_layout(gls_matrix, sensors, args.obs_weight),
        "scenario_cvar_trace": scenario_cvar_trace_for_layout(scenario_matrices, sensors, args.obs_weight, args.cvar_tail_fraction),
        "condition_number": posterior_condition_for_layout(gls_matrix, sensors, args.obs_weight),
        "coverage_penalty": coverage_penalty(distance, sensors),
    }
```

### Auto-weight inner-validation model selection
**Source:** `/home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py` lines 401-421 and 484-503
```python
def split_validation_for_tuning(val):
    midpoint = max(1, val.shape[0] // 2)
    return val[:midpoint], val[midpoint:]


def parse_weight_grid(raw):
    weights = []
    for chunk in raw.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        values = [float(x) for x in chunk.replace(",", " ").split()]
        if len(values) != 5:
            raise ValueError("Each RCSS weight grid entry must have five values: validation trace cvar condition coverage")
        total = sum(values)
        if total <= 0:
            raise ValueError("RCSS weight grid entries must have positive total weight")
        weights.append(tuple(x / total for x in values))
    if not weights:
        raise ValueError("RCSS auto-weight grid is empty")
    return weights
```

```python
def select_auto_rcss_weights(candidates, selector_val, tuner_val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args):
    selector_rows = build_rcss_rows(candidates, selector_val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args)
    tuner_rows = build_rcss_rows(candidates, tuner_val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args)
    tuner_by_key = {tuple(row["sensors"].tolist()): row["validation_mae"] for row in tuner_rows}
    best = None
    for weights in parse_weight_grid(args.rcss_auto_weight_grid):
        scored = rcss_candidate_scores([row.copy() for row in selector_rows], args, weights)
        selected = min(scored, key=lambda row: row["rcss_score"])
        tuner_mae = tuner_by_key[tuple(selected["sensors"].tolist())]
```

### Validation-aware swap acceptance and local-optimality source
**Source:** `/home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py` lines 512-558
```python
def validation_swap_search(initial_sensors, candidate_nodes, val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args, rng):
    selected = set(int(x) for x in initial_sensors)
    n_nodes = gls_matrix.shape[0]
    best_sensors = np.array(sorted(selected), dtype=int)
    best_row = make_rcss_row("validation_swap", 0, best_sensors, val, tod, distance, laplacian, precision, mean, std, gls_matrix, scenario_matrices, args)
    candidate_nodes = [int(x) for x in candidate_nodes if int(x) not in selected]
    history = []
    for iteration in range(args.validation_swap_iter):
        if not candidate_nodes:
            break
```

```python
        trials = [(row, remove_node, add_node, trial) for row, remove_node, add_node, trial in trials if row["validation_mae"] < best_row["validation_mae"] - args.validation_swap_min_improve]
        if not trials:
            break
        row, remove_node, add_node, trial = min(trials, key=lambda item: item[0]["validation_mae"])
        selected = trial
        best_sensors = np.array(sorted(selected), dtype=int)
        best_row = row
```

### Dense-solver limitation source
**Source:** `/home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py` lines 153-164 and 246-249
```python
    solution = linalg.solve(lhs, rhs.T, assume_a="pos").T
    return solution, lhs


def certificate(lhs):
    inv_lhs = linalg.inv(lhs)
```

```python
def posterior_inverse_for_layout(base_matrix, sensors, obs_weight):
    selector = np.zeros(base_matrix.shape[0])
    selector[np.asarray(sensors, dtype=int)] = obs_weight
    return linalg.inv(base_matrix + np.diag(selector))
```

## Shared Patterns

### Validation/test separation
**Source:** `/home/samuel/projects/sensor_opt/.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` lines 56 and 70
**Apply to:** all Phase 2 method/theory artifacts and any narrative/README edits
```markdown
Validation MAE is selection evidence only, never final performance evidence. Final performance claims must point to held-out test metrics from curated result artifacts.
```

### Certificate terminology
**Source:** `/home/samuel/projects/sensor_opt/.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` lines 68-73
**Apply to:** posterior-error derivation, RCSS surrogate text, README/NARRATIVE wording
```markdown
Use certificate-guided, posterior-certificate-aware, or certificate diagnostics only. Posterior trace, condition number, and information logdet correlations are empirical guidance and interpretability evidence, not formal certified optimality or guaranteed reconstruction-error bounds.
```

### Offline planning framing
**Source:** `/home/samuel/projects/sensor_opt/refine-logs/WRITING_NOTES_GREEDY_OFFLINE_PLANNING.md` lines 8-20
**Apply to:** validation-aware swap, greedy posterior, scenario greedy, TR Part B note
```markdown
Greedy A-optimal, greedy D-optimal, and swap local search should be framed as **offline planning algorithms**, not as real-world sequential deployment protocols.
```

### Documentation artifact style
**Source:** `/home/samuel/projects/sensor_opt/.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` lines 87-110
**Apply to:** phase-local Phase 2 artifact
```markdown
## Self-Check

- [x] CLAIM-01 is covered by C-01.
...
- [x] Deferred ideas are excluded: no new experiments, algorithm changes, baseline implementation, raw dataset reads, or final manuscript writing are assigned to Phase 1.
- [x] Raw dataset paths are not used as Phase 1 evidence sources.
```

## No Analog Found

None. This phase is documentation/theory-focused; all likely files have close Markdown or implementation-source analogs.

## Metadata

**Analog search scope:** `/home/samuel/projects/sensor_opt/.planning/phases`, `/home/samuel/projects/sensor_opt/.planning/codebase`, `/home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md`, `/home/samuel/projects/sensor_opt/README.md`, `/home/samuel/projects/sensor_opt/refine-logs`, `/home/samuel/projects/sensor_opt/TRC-23-02333/transparent_estimator_eval.py`, `/home/samuel/projects/sensor_opt/TRC-23-02333/trace_sl_results/README.md`
**Files scanned:** 14
**Pattern extraction date:** 2026-05-22
