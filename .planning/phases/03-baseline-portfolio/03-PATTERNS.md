# Phase 3: Baseline Portfolio - Pattern Map

**Mapped:** 2026-05-22
**Files analyzed:** 4
**Analogs found:** 4 / 4

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|---|---|---|---|---|
| `TRC-23-02333/transparent_estimator_eval.py` | utility / experiment driver | batch + transform + file-I/O | `TRC-23-02333/transparent_estimator_eval.py` existing layout, RCSS, validation-swap, artifact-writing blocks | exact |
| `TRC-23-02333/summarize_trace_sl_rcss.py` | utility / aggregator | batch + transform + file-I/O | `TRC-23-02333/summarize_trace_sl_rcss.py` existing layout-type grouping and paired-delta summary | exact |
| `scripts/run_stage12_pems7_228.sh` | config / launcher | batch + file-I/O | `scripts/run_stage11_pems7_228.sh` | exact |
| `.planning/phases/03-baseline-portfolio/03-BASELINE-INVENTORY.md` | documentation / evidence artifact | transform + evidence mapping | `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` and `.planning/REQUIREMENTS.md` | exact |

## Pattern Assignments

### `TRC-23-02333/transparent_estimator_eval.py` (utility / experiment driver, batch + transform + file-I/O)

**Analog:** `TRC-23-02333/transparent_estimator_eval.py`

**Imports pattern** (lines 0-10):
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
```

**Input validation / fail-fast pattern** (lines 58-67):
```python
def load_seattle_dataset(data_root, seed):
    data_root = Path(data_root)
    tensor_path = data_root / "tensor.npz"
    adjacency_path = data_root / "Loop_Seattle_2015_A.npy"
    if not tensor_path.exists() or not adjacency_path.exists():
        raise FileNotFoundError(f"Expected tensor.npz and Loop_Seattle_2015_A.npy under {data_root}")

    tensor = np.load(tensor_path)["arr_0"].astype(float)
    if tensor.ndim != 3 or tensor.shape[2] != SLOTS_PER_DAY:
        raise ValueError(f"Expected Seattle tensor shape (nodes, days, {SLOTS_PER_DAY}), got {tensor.shape}")
```

**A/D-optimal greedy objective pattern** (lines 167-190):
```python
def greedy_posterior_layout(base_matrix, sensor_count, obs_weight, objective):
    posterior_inv = linalg.inv(base_matrix)
    selected = []
    remaining = set(range(base_matrix.shape[0]))
    for _ in range(sensor_count):
        best_node = None
        best_score = -np.inf
        for node in remaining:
            denom = 1.0 + obs_weight * posterior_inv[node, node]
            if objective == "a_trace":
                score = obs_weight * float(np.dot(posterior_inv[:, node], posterior_inv[:, node])) / denom
            elif objective == "d_logdet":
                score = math.log(denom)
            else:
                raise ValueError(f"Unsupported greedy objective: {objective}")
            if score > best_score:
                best_score = score
                best_node = node
        column = posterior_inv[:, best_node].copy()
        denom = 1.0 + obs_weight * posterior_inv[best_node, best_node]
        posterior_inv -= obs_weight * np.outer(column, column) / denom
        selected.append(best_node)
        remaining.remove(best_node)
    return np.array(selected, dtype=int)
```

**Topology / observability proxy layout pattern** (lines 275-297):
```python
def degree_layout(distance, sensor_count):
    similarity = make_similarity(distance)
    return np.argsort(-similarity.sum(axis=1))[:sensor_count]


def top_variance_layout(train, sensor_count):
    return np.argsort(-np.var(train, axis=0))[:sensor_count]


def coverage_layout(distance, sensor_count):
    n_nodes = distance.shape[0]
    positive = distance[distance > 0]
    fill_value = float(positive.max()) if positive.size else 1.0
    dist = np.where(distance > 0, distance, fill_value)
    first = int(np.argmin(dist.sum(axis=1)))
    selected = [first]
    nearest = dist[first].copy()
    while len(selected) < sensor_count:
        nearest[selected] = -np.inf
        node = int(np.argmax(nearest))
        selected.append(node)
        nearest = np.minimum(nearest, dist[node])
    return np.array(selected, dtype=int)
```

**Scenario / graph-risk baseline pattern** (lines 205-243):
```python
def scenario_greedy_layout(base_matrices, sensor_count, obs_weight, objective, tail_fraction):
    posterior_invs = [linalg.inv(matrix) for matrix in base_matrices]
    selected = []
    remaining = set(range(base_matrices[0].shape[0]))
    traces = np.array([np.trace(inv) for inv in posterior_invs], dtype=float)
    for _ in range(sensor_count):
        best_node = None
        best_score = np.inf if objective == "cvar_trace" else -np.inf
        for node in remaining:
            gains = np.array(
                [obs_weight * float(np.dot(inv[:, node], inv[:, node])) / (1.0 + obs_weight * inv[node, node]) for inv in posterior_invs],
                dtype=float,
            )
            if objective == "average_trace":
                score = float(gains.mean())
                better = score > best_score
            elif objective == "cvar_trace":
                next_traces = traces - gains
                tail_count = max(1, int(math.ceil(len(next_traces) * tail_fraction)))
                score = float(np.sort(next_traces)[-tail_count:].mean())
                better = score < best_score
            else:
                raise ValueError(f"Unsupported scenario objective: {objective}")
            if better:
                best_score = score
                best_node = node
```

**Validation-selection pattern** (lines 393-398):
```python
def validation_mae(test, tod, distance, laplacian, precision, mean, std, sensors, args):
    rows, _ = evaluate_layout(test, tod, distance, laplacian, precision, mean, std, sensors, args)
    for row in rows:
        if row["method"] == args.selection_method:
            return row["mae"]
    raise ValueError(f"Selection method not evaluated: {args.selection_method}")
```

**RCSS candidate row pattern** (lines 455-466):
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

**Multistart validation refinement pattern** (lines 830-858):
```python
            top_validation = sorted(random_validation, key=lambda item: item[2])[: args.multistart_count]
            swap_candidates = []
            for rank, (layout_id, sensors, val_mae, _) in enumerate(top_validation, start=1):
                swap_sensors, history = swap_trace_local_search(gls_matrix, sensors, args.obs_weight, args.swap_max_iter)
                swap_val_mae = validation_mae(val, tod, distance, laplacian, precision, mean, std, swap_sensors, args)
                swap_candidates.append((rank, layout_id, swap_sensors, swap_val_mae))
                swap_records.append(
                    {
                        "budget": budget,
                        "start": "validation_random",
                        "rank": rank,
                        "start_layout_id": layout_id,
                        "start_validation_mae": val_mae,
                        "swap_validation_mae": swap_val_mae,
                        "history": history,
                    }
                )
            best_swap_rank, best_swap_id, best_swap, best_swap_val = min(swap_candidates, key=lambda item: item[3])
            swap_outputs.append(("multistart_swap_by_validation", best_swap_id, best_swap, best_swap_val))
            layouts.append(swap_outputs[-1])
```

**CLI flag pattern** (lines 697-744):
```python
def main():
    parser = argparse.ArgumentParser(description="TRACE-SL transparent estimator CPU pilot")
    default_data = Path(__file__).resolve().parent / "dataset" / "PeMS7_228"
    parser.add_argument("--data-root", type=str, default=str(default_data))
    parser.add_argument("--output-dir", type=str, default="trace_sl_results/pems7_228_cpu_pilot")
    parser.add_argument("--budgets", type=str, default="0.10 0.20 0.30")
    parser.add_argument("--num-layouts", type=int, default=20)
    parser.add_argument("--include-greedy", action="store_true")
    parser.add_argument("--include-swap", action="store_true")
    parser.add_argument("--include-simple-baselines", action="store_true")
    parser.add_argument("--include-scenario-greedy", action="store_true")
    parser.add_argument("--include-rcss", action="store_true")
```

**Independent layout row pattern** (lines 791-810):
```python
        if args.include_simple_baselines:
            layouts.extend(
                [
                    ("degree", 0, degree_layout(distance, sensor_count), np.nan),
                    ("top_variance", 0, top_variance_layout(train, sensor_count), np.nan),
                    ("coverage", 0, coverage_layout(distance, sensor_count), np.nan),
                ]
            )
        greedy_a = greedy_posterior_layout(gls_matrix, sensor_count, args.obs_weight, "a_trace")
        scenario_avg = None
        scenario_cvar = None
        if args.include_scenario_greedy:
            scenario_avg = scenario_greedy_layout(scenario_matrices, sensor_count, args.obs_weight, "average_trace", args.cvar_tail_fraction)
            scenario_cvar = scenario_greedy_layout(scenario_matrices, sensor_count, args.obs_weight, "cvar_trace", args.cvar_tail_fraction)
            layouts.append(("scenario_average_a_trace", 0, scenario_avg, np.nan))
            layouts.append(("scenario_cvar_a_trace", 0, scenario_cvar, np.nan))
        if args.include_greedy:
            layouts.append(("greedy_a_trace", 0, greedy_a, np.nan))
            layouts.append(("greedy_d_logdet", 0, greedy_posterior_layout(gls_matrix, sensor_count, args.obs_weight, "d_logdet"), np.nan))
```

**Held-out evaluation row pattern** (lines 967-996):
```python
        for layout_type, layout_id, sensors, validation_selected_mae in layouts:
            layout_records.append(
                {
                    "dataset": Path(args.data_root).name,
                    "budget": budget,
                    "sensor_count": sensor_count,
                    "layout_type": layout_type,
                    "layout_id": layout_id,
                    "posterior_trace_objective": posterior_trace_for_layout(gls_matrix, sensors, args.obs_weight),
                    "validation_selected_mae": float(validation_selected_mae) if np.isfinite(validation_selected_mae) else None,
                    "sensors": sorted(int(x) for x in sensors),
                }
            )
            hidden_count = n_nodes - sensor_count
            layout_rows, _ = evaluate_layout(test, tod, distance, laplacian, precision, mean, std, sensors, args)
            for row in layout_rows:
                row.update(
                    {
                        "dataset": Path(args.data_root).name,
                        "budget": budget,
                        "sensor_count": sensor_count,
                        "hidden_count": hidden_count,
                        "layout_type": layout_type,
```

**Artifact-writing pattern** (lines 998-1019):
```python
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows)
    correlations = summarize_correlations(rows)
    frame.to_csv(output_dir / "metrics.csv", index=False)
    (output_dir / "metrics.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    (output_dir / "layouts.json").write_text(json.dumps(layout_records, indent=2), encoding="utf-8")
    (output_dir / "swap_history.json").write_text(json.dumps(swap_records, indent=2), encoding="utf-8")
    (output_dir / "rcss_candidates.json").write_text(json.dumps(rcss_records, indent=2), encoding="utf-8")
    pd.DataFrame(rcss_records).to_csv(output_dir / "rcss_candidates.csv", index=False)
    pd.DataFrame(correlations).to_csv(output_dir / "certificate_correlations.csv", index=False)
    config = vars(args).copy()
    config["val_days"] = val_days
    config["test_days"] = test_days
    config["scenario_day_indices"] = scenario_day_indices
    config["train_shape"] = list(train.shape)
    config["val_shape"] = list(val.shape)
    config["test_shape"] = list(test.shape)
    (output_dir / "config.json").write_text(json.dumps(config, indent=2), encoding="utf-8")
    write_summary(output_dir, args, rows, correlations, test_days)
```

**How to apply to Phase 3:**
- Add new baseline helper functions as top-level pure functions near `degree_layout`, `top_variance_layout`, `coverage_layout`, `greedy_posterior_layout`, and `scenario_greedy_layout`.
- Keep helpers returning `np.array(..., dtype=int)` sensor indices.
- Add CLI flags in `main()` with explicit `--include-*` switches, not implicit behavior changes.
- Add independent `layout_type` rows to `layouts` before the final held-out `evaluate_layout()` loop.
- Preserve validation/test separation: validation can select layouts; `evaluate_layout(test, ...)` produces final performance rows.
- Use stable paper-readable names such as `greedy_a_trace`, `greedy_d_logdet`, `qr_pod_modes`, `observability_proxy`, `graph_sampling_*`, and `multistart_swap_by_validation`.

---

### `TRC-23-02333/summarize_trace_sl_rcss.py` (utility / aggregator, batch + transform + file-I/O)

**Analog:** `TRC-23-02333/summarize_trace_sl_rcss.py`

**Imports and CLI pattern** (lines 0-10):
```python
import argparse
from pathlib import Path

import pandas as pd
from scipy.stats import ttest_rel, wilcoxon


def main():
    parser = argparse.ArgumentParser(description="Summarize TRACE-SL multi-split RCSS results")
    parser.add_argument("--input-root", required=True, nargs="+")
    parser.add_argument("--output-dir", required=True)
```

**Input discovery and error handling pattern** (lines 13-39):
```python
    input_roots = [Path(raw) for raw in args.input_root]
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    metrics = []
    correlations = []
    rcss_candidates = []
    for input_root in input_roots:
        for path in sorted(input_root.glob("seed_*/metrics.csv")):
            seed = int(path.parent.name.split("_", 1)[1])
            frame = pd.read_csv(path)
            frame["split_seed"] = seed
            metrics.append(frame)
```

```python
    if not metrics:
        roots = ", ".join(str(path) for path in input_roots)
        raise SystemExit(f"No seed metrics found under {roots}")
```

**Layout-type summary pattern** (lines 41-63):
```python
    combined = pd.concat(metrics, ignore_index=True)
    combined.to_csv(output_dir / "combined_metrics.csv", index=False)

    gls = combined[combined["method"] == "gls_map"].copy()
    layout_summary = (
        gls.groupby(["budget", "layout_type"])["mae"]
        .agg(["mean", "std", "count"])
        .reset_index()
        .sort_values(["budget", "mean"])
    )
    layout_summary.to_csv(output_dir / "gls_map_layout_summary.csv", index=False)

    pivot = gls.pivot_table(index=["split_seed", "budget"], columns="layout_type", values="mae", aggfunc="mean")
    comparison_layouts = ["validation_swap_selected", "rcss_selected", "robust_coverage_cvar"]
    baseline_layouts = [
        "random",
        "best_random_by_validation",
        "top_variance",
        "greedy_a_trace",
        "scenario_cvar_a_trace",
        "multistart_swap_by_validation",
        "swap_from_scenario_cvar",
    ]
```

**Paired-delta pattern** (lines 66-91):
```python
    for budget, sub in pivot.groupby(level="budget"):
        sub = sub.droplevel("budget")
        row = {"budget": budget}
        for layout in comparison_layouts:
            if layout in sub.columns:
                for baseline in baseline_layouts:
                    if baseline in sub.columns:
                        delta = sub[layout] - sub[baseline]
                        row[f"{layout}_minus_{baseline}_mean"] = delta.mean()
                        row[f"{layout}_minus_{baseline}_std"] = delta.std()
                        paired_row = {
                            "budget": budget,
                            "layout": layout,
                            "baseline": baseline,
                            "delta_mean": delta.mean(),
                            "delta_std": delta.std(),
                            "win_count": int((delta < 0).sum()),
                            "count": int(delta.notna().sum()),
                        }
                        if delta.notna().sum() >= 2:
                            paired_row["paired_t_p"] = ttest_rel(sub[layout], sub[baseline], nan_policy="omit").pvalue
                            try:
                                paired_row["wilcoxon_p"] = wilcoxon(delta.dropna()).pvalue
                            except ValueError:
                                paired_row["wilcoxon_p"] = pd.NA
                        paired_rows.append(paired_row)
```

**CSV and Markdown output pattern** (lines 93-127 and 129-204):
```python
    delta_summary = pd.DataFrame(delta_rows)
    delta_summary.to_csv(output_dir / "gls_map_delta_summary.csv", index=False)
    paired_tests = pd.DataFrame(paired_rows)
    paired_tests.to_csv(output_dir / "gls_map_paired_delta_tests.csv", index=False)
```

```python
    lines = [
        "---",
        "status: complete",
        "---",
        "",
        "# TRACE-SL RCSS Multi-Split Summary",
        "",
        "## Mean GLS/MAP test MAE across splits",
        "",
        "```",
        layout_summary.to_string(index=False),
        "```",
```

**How to apply to Phase 3:**
- Add new Phase 3 baseline names to `baseline_layouts` and/or `ablation_layouts` only when those names are emitted by evaluator `layout_type` rows.
- Preserve `gls_map` as the reconstruction-centered comparison surface unless the phase explicitly adds another reported method section.
- Emit machine-readable CSVs before Markdown summaries.
- Keep paired tests conditional on enough split rows and tolerate Wilcoxon `ValueError` as existing code does.

---

### `scripts/run_stage12_pems7_228.sh` (config / launcher, batch + file-I/O)

**Analog:** `scripts/run_stage11_pems7_228.sh`

**Shell safety and environment defaults pattern** (lines 0-23):
```bash
#!/usr/bin/env bash
set -euo pipefail

DATA_ROOT="${DATA_ROOT:-TRC-23-02333/dataset/PeMS7_228}"
OUTPUT_DIR="${OUTPUT_DIR:-TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight}"
SEEDS="${SEEDS:-25 26 27 28 29}"
BUDGETS="${BUDGETS:-0.10 0.20 0.30}"
NUM_LAYOUTS="${NUM_LAYOUTS:-200}"
RCSS_RANDOM_CANDIDATES="${RCSS_RANDOM_CANDIDATES:-200}"
RCSS_QUALITY_CANDIDATES="${RCSS_QUALITY_CANDIDATES:-200}"
SCENARIO_COUNT="${SCENARIO_COUNT:-8}"
VALIDATION_SWAP_STARTS="${VALIDATION_SWAP_STARTS:-5}"
VALIDATION_SWAP_ITER="${VALIDATION_SWAP_ITER:-10}"
VALIDATION_SWAP_ADD_POOL="${VALIDATION_SWAP_ADD_POOL:-30}"
VALIDATION_SWAP_REMOVE_POOL="${VALIDATION_SWAP_REMOVE_POOL:-10}"
THREADS_PER_JOB="${THREADS_PER_JOB:-1}"

export OMP_NUM_THREADS="${OMP_NUM_THREADS:-${THREADS_PER_JOB}}"
export OPENBLAS_NUM_THREADS="${OPENBLAS_NUM_THREADS:-${THREADS_PER_JOB}}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-${THREADS_PER_JOB}}"
export NUMEXPR_NUM_THREADS="${NUMEXPR_NUM_THREADS:-${THREADS_PER_JOB}}"
export VECLIB_MAXIMUM_THREADS="${VECLIB_MAXIMUM_THREADS:-${THREADS_PER_JOB}}"

mkdir -p "${OUTPUT_DIR}"
```

**Per-seed evaluator invocation pattern** (lines 25-47):
```bash
for seed in ${SEEDS}; do
  python TRC-23-02333/transparent_estimator_eval.py \
    --data-root "${DATA_ROOT}" \
    --output-dir "${OUTPUT_DIR}/seed_${seed}" \
    --budgets "${BUDGETS}" \
    --num-layouts "${NUM_LAYOUTS}" \
    --split-seed "${seed}" \
    --layout-seed "$((2026 + seed))" \
    --include-simple-baselines \
    --include-greedy \
    --include-swap \
    --include-scenario-greedy \
    --include-rcss \
    --rcss-auto-weights \
    --rcss-random-candidates "${RCSS_RANDOM_CANDIDATES}" \
    --rcss-quality-candidates "${RCSS_QUALITY_CANDIDATES}" \
    --scenario-count "${SCENARIO_COUNT}" \
    --include-validation-swap \
    --validation-swap-starts "${VALIDATION_SWAP_STARTS}" \
    --validation-swap-iter "${VALIDATION_SWAP_ITER}" \
    --validation-swap-add-pool "${VALIDATION_SWAP_ADD_POOL}" \
    --validation-swap-remove-pool "${VALIDATION_SWAP_REMOVE_POOL}" \
    2>&1 | tee "${OUTPUT_DIR}_seed_${seed}.log"
done
```

**Aggregation pattern** (lines 50-52):
```bash
python TRC-23-02333/summarize_trace_sl_rcss.py \
  --input-root "${OUTPUT_DIR}" \
  --output-dir "${OUTPUT_DIR}"
```

**How to apply to Phase 3:**
- Follow `run_stage{N}_{dataset}.sh` naming; for a baseline portfolio stage, `scripts/run_stage12_pems7_228.sh` fits existing convention.
- Use `OUTPUT_DIR` default under `TRC-23-02333/trace_sl_results/`, e.g. `pems7_228_stage12_baseline_portfolio`.
- Expose new baseline-scale knobs through uppercase environment variables before the loop.
- Keep BLAS thread caps and `tee` log pattern unchanged.
- Add new evaluator flags only after they exist in `transparent_estimator_eval.py`.

---

### `.planning/phases/03-baseline-portfolio/03-BASELINE-INVENTORY.md` (documentation / evidence artifact, transform + evidence mapping)

**Analogs:** `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md`, `.planning/REQUIREMENTS.md`, `.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md`

**Phase header and boundary pattern** (`01-CLAIM-EVIDENCE-CONTRACT.md` lines 0-17):
```markdown
# Phase 1: Claim-Evidence Contract

**Status:** Draft contract for downstream phases  
**Date:** 2026-05-21

## Phase Boundary

This phase delivers the paper-facing claim-evidence contract for TRACE-SL before additional experiments, theory writing, or manuscript drafting. It locks the strongest defensible contribution claims, defines what evidence each claim requires, constrains terminology around certificates, handles the 10% PeMS7_228 multistart caveat, and positions TRACE-SL against deterministic full-observability TSLP and black-box imputation/forecasting.

It does not implement new baselines, run new experiments, prove theory, generate final paper tables, or rewrite the full manuscript. Those belong to later phases.
```

**Baseline requirement source pattern** (`.planning/REQUIREMENTS.md` lines 26-34):
```markdown
### Baselines and Method Portfolio

- [ ] **BASE-01**: The experiment suite includes observability-inspired or TSLP-style baselines, with clear explanation that their objective differs from reconstruction-error minimization.
- [ ] **BASE-02**: A-optimal and D-optimal design baselines are reported as independent baselines, not only candidate sources inside RCSS.
- [ ] **BASE-03**: Graph sampling or graph signal reconstruction baselines are included or explicitly justified as already represented by existing GSP-related comparisons.
- [ ] **BASE-04**: QR/SVD/POD sparse sensor placement baseline is implemented and evaluated where compatible with the traffic matrix representation.
- [ ] **BASE-05**: A simple learning-based reconstruction check is run or scoped with a documented reason if deferred.
- [ ] **BASE-06**: Multistart validation refinement is treated as a strong comparator or predeclared portfolio member, not ignored after observing the 10% budget result.
```

**Matrix / taxonomy pattern** (`01-CLAIM-EVIDENCE-CONTRACT.md` lines 50-64):
```markdown
## Claim-Evidence Matrix

Evidence status taxonomy: present | needs audit | needs new experiment | theory-dependent | wording-only limitation

Evidence type vocabulary: held-out test result | paired/statistical comparison | robustness test | external-network evidence | formal derivation/theory | reproducible artifact | limitation wording

Validation MAE is selection evidence only, never final performance evidence. Final performance claims must point to held-out test metrics from curated result artifacts.

| Claim ID | Requirement | Claim wording | Evidence required | Current evidence source | Evidence status | Caveat / limitation wording | Downstream phase owner |
|---|---|---|---|---|---|---|---|
```

**Implementation anchor source-register pattern** (`02-FORMULATION-THEORY-BRIDGE.md` lines 24-34):
```markdown
### Implementation Anchors Used as Method Source of Truth

- `split_daily_frame` — separates train, validation, and held-out test days.
- `solve_quadratic` — computes transparent GSP/GLS-MAP reconstruction from selected sensors.
- `certificate` — emits posterior trace, condition number, and information logdet diagnostics.
- `evaluate_layout` — evaluates a fixed sensor set by hiding complement nodes and measuring reconstruction error.
- `posterior_trace_for_layout`, `scenario_cvar_trace_for_layout`, `posterior_condition_for_layout`, and `coverage_penalty` — define RCSS diagnostic terms.
- `rcss_candidate_scores`, `make_rcss_row`, `split_validation_for_tuning`, `parse_weight_grid`, and `select_auto_rcss_weights` — define RCSS scoring and inner-validation auto-weight selection.
- `validation_swap_search` — defines validation-aware one-swap local refinement.

No raw traffic-dataset directory is used as an evidence source here.
```

**Guardrails pattern** (`02-FORMULATION-THEORY-BRIDGE.md` lines 150-156):
```markdown
## Guardrails

- This artifact defines method/theory wording only; it does not run new experiments, implement baseline work, perform robustness tests, rebuild split evidence, curate Seattle outputs, or write the final manuscript.
- Validation MAE remains selection evidence for RCSS scoring, auto-weight tuning, and validation-aware swap; held-out test evaluation remains the final performance evidence channel.
- Certificate language remains certificate-guided, posterior-certificate-aware, or diagnostic. Posterior trace identities are scoped to the linear-Gaussian squared-error bridge.
- Raw dataset reads are excluded from this phase-local artifact, and raw traffic-dataset directories are not cited as evidence sources.
- Phase 3 owns reviewer-grade baselines and the multistart comparator/portfolio decision; Phase 4 owns held-out evidence/statistical audit and any needed split-evidence regeneration; Phase 5 owns robustness tests; Phase 7 owns final Transportation Science manuscript integration.
```

**Requirement traceability pattern** (`02-FORMULATION-THEORY-BRIDGE.md` lines 158-166):
```markdown
## Requirement Traceability

| Requirement | Coverage in this artifact |
|---|---|
| THEORY-01 | Covered by `Notation`, `Budgeted Reconstruction-Aware Sensor-Set Problem`, and `Protocol Separation`. |
| THEORY-02 | Covered by `TRACE-SL/RCSS Surrogate Objective` with validation loss, posterior trace, scenario CVaR trace, condition number, and coverage. |
| THEORY-03 | Covered by `Linear-Gaussian GLS/MAP Posterior-Error Bridge`. |
| THEORY-04 | Covered by `MAE-Oriented Interpretation and Caveats`. |
| THEORY-05 | Covered by `Validation-Aware Swap Analysis`, complexity discussion, dense-solver scaling limitation, and fixed-candidate local optimality. |
```

**How to apply to Phase 3:**
- Use a table with stable rows `BASE-01` through `BASE-06`.
- Recommended columns: `Requirement`, `Reviewer objection answered`, `Portfolio status`, `Implementation hook`, `Evaluator layout_type / artifact`, `Held-out evidence status`, `Deferral reason / Phase 4 action`.
- Status vocabulary should distinguish `implemented`, `already represented`, `deferred with reason`, and `requires Phase 4 full evidence`.
- Explicitly state raw datasets are not read by the inventory.

## Shared Patterns

### Validation/test separation

**Source:** `TRC-23-02333/transparent_estimator_eval.py` lines 747-763 and 967-996  
**Apply to:** all evaluator baseline additions

Use train data for priors and scenario matrices, validation data for layout selection/refinement, and held-out `test` data only inside the final evaluation loop.

```python
    train, val, test, test_index, distance, val_days, test_days = load_pems_dataset(args.data_root, args.split_seed)
    args.val_days = val_days
```

```python
            layout_rows, _ = evaluate_layout(test, tod, distance, laplacian, precision, mean, std, sensors, args)
```

### Stable `layout_type` rows

**Source:** `TRC-23-02333/transparent_estimator_eval.py` lines 791-810 and 967-996  
**Apply to:** A/D-optimal, graph sampling, QR/SVD/POD, observability proxy, multistart comparator rows

Every implemented baseline should become a tuple `(layout_type, layout_id, sensors, validation_selected_mae)` in `layouts`; the final loop adds dataset, budget, split seed, layout seed, validation-selected MAE, and reconstruction metrics.

### Error handling

**Source:** `TRC-23-02333/transparent_estimator_eval.py` lines 58-67, 393-398, 406-421; `TRC-23-02333/summarize_trace_sl_rcss.py` lines 37-39  
**Apply to:** unsupported objective names, invalid grids, missing outputs, incompatible baseline modes

Use `ValueError` for invalid algorithm/option inputs and `SystemExit` for missing aggregate outputs. Keep messages explicit and f-string based.

### Artifact writing

**Source:** `TRC-23-02333/transparent_estimator_eval.py` lines 998-1019; `TRC-23-02333/summarize_trace_sl_rcss.py` lines 41-51 and 93-127  
**Apply to:** all new result artifacts and summaries

Write machine-readable CSV/JSON first, then Markdown summaries. Keep outputs under `TRC-23-02333/trace_sl_results/<stage>/`.

### Shell reproducibility

**Source:** `scripts/run_stage11_pems7_228.sh` lines 0-52  
**Apply to:** new Stage 12 / Phase 3 baseline launcher

Use `set -euo pipefail`, uppercase environment overrides, BLAS thread caps, per-seed loop, `tee` logs, and final summarizer invocation.

### Baseline inventory / requirement traceability

**Source:** `.planning/REQUIREMENTS.md` lines 26-34; `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` lines 50-64; `.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md` lines 158-166  
**Apply to:** `.planning/phases/03-baseline-portfolio/03-BASELINE-INVENTORY.md`

Each BASE row must map to the reviewer objection answered and the concrete evaluator/layout/script artifact that implements, represents, defers, or routes the baseline to Phase 4 evidence.

## No Analog Found

None. All inferred files have exact or strong role/data-flow analogs in the existing repository.

## Metadata

**Analog search scope:** `TRC-23-02333/*.py`, `scripts/run_stage*.sh`, `.planning/**/*.md`  
**Files scanned:** 10+ candidate source/artifact files via targeted search and reads  
**Pattern extraction date:** 2026-05-22
