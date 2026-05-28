# TRACE-BiOpt: Recoverability-Driven Bilevel Transportation Network Design

**Current manuscript**: TRACE-BiOpt (bilevel optimization) is the paper-facing method for a Transportation Research Part B: Methodological submission. The manuscript title is *TRACE-BiOpt: Recoverability-Driven Bilevel Transportation Network Design for Sparse Traffic Sensor Siting*. The method is **not** a candidate-pool selector or AutoML-style portfolio chooser; it is one recoverability-driven bilevel objective with one transparent GLS/MAP lower-level inverse problem, one formal CVaR tail-risk epigraph, and one deterministic initialization-and-exchange solver.

**Legacy method**: TRACE-SL / RCSS (Robust Certificate-guided Sensor Search) was the predecessor candidate-pool framework. It remains available as a historical baseline and diagnostic comparator within the TRACE-BiOpt evidence chain, but is no longer the current manuscript method.

## TRACE-BiOpt Method Overview

TRACE-BiOpt chooses a fixed sensor layout `S` by minimizing a single bilevel objective:

```
J(S) = hidden_huber_reconstruction_loss(S)
     + beta  * posterior_trace(S) / n
     + gamma * scenario_cvar_trace(S) / n
     + eta   * spatial_redundancy_penalty(S)
```

under the transparent GLS/MAP lower-level inverse problem. The solver uses deterministic initialization (relaxed rounding or objective-forward construction) followed by greedy one-swap exchange refinement under the same objective `J(S)`.

Key evidence result: across 9 tested dataset-budget regimes (PeMS7_228, PeMS7_1026, Seattle at 10/20/30%), TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against 21 pre-registered baselines spanning 11 method families. After Holm correction across all 189 paired comparisons, no challenger remains statistically tied or significantly better.

## Current paper-source truth

The authoritative evidence source is:

```
TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/
```

with aggregate claim status `supported_submission_ready`. The method contract is in `TRACE_BIOPT_SPEC.md`. The theory contract is in `TRACE_BIOPT_THEORY.md`.

### Current-best TRACE-BiOpt headline evidence

| Dataset | Budget | TRACE-BiOpt MAE | Best baseline MAE | Holm-corrected screen |
|---|---:|---:|---:|---|
| PeMS7_228 | 10% | current-best contract | current-best contract | 189/189 wins |
| PeMS7_228 | 20% | current-best contract | current-best contract | 189/189 wins |
| PeMS7_228 | 30% | current-best contract | current-best contract | 189/189 wins |
| PeMS7_1026 | 10% | current-best contract | current-best contract | 189/189 wins |
| PeMS7_1026 | 20% | current-best contract | current-best contract | 189/189 wins |
| PeMS7_1026 | 30% | current-best contract | current-best contract | 189/189 wins |
| Seattle | 10% | current-best contract | current-best contract | 189/189 wins |
| Seattle | 20% | current-best contract | current-best contract | 189/189 wins |
| Seattle | 30% | current-best contract | current-best contract | 189/189 wins |

Exact numbers are in `trace_biopt_claim_contract.csv` and `trace_biopt_best_baseline_delta.csv` under the current-best evidence directory. 8/9 rows are promoted from Stage 16 calibrated reruns; Seattle 10% is retained on the audited Stage 15 lane.

## Repository layout

- `TRC-23-02333/trace_biopt.py`: CLI wrapper that invokes `transparent_estimator_eval.main()` with `--include-biopt`; the solver logic lives in `transparent_estimator_eval.py`.
- `TRC-23-02333/transparent_estimator_eval.py`: reconstruction evaluator and TRACE-SL/RCSS experiment driver (legacy baseline).
- `TRC-23-02333/summarize_trace_sl_rcss.py`: multi-split result aggregation script (used by both TRACE-BiOpt and TRACE-SL pipelines).
- `TRC-23-02333/trace_sl_results/`: checked-in result artifacts.
- `TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/`: TRACE-BiOpt current-best paper-facing evidence chain.
- `TRACE_BIOPT_SPEC.md`: TRACE-BiOpt method contract.
- `TRACE_BIOPT_THEORY.md`: TRACE-BiOpt theory statement contract.
- `scripts/refresh_current_best_trace_biopt_paper_chain.sh`: refreshes the current-best evidence chain.
- `paper/`: current TR Part B manuscript (Elsevier CAS template).
- `NARRATIVE_REPORT.md`: writing handoff with TRACE-BiOpt method framing and current evidence.
- `PAPER_PLAN.md`: paper structure, claims-evidence matrix, and figure plan.
- `RESEARCH_PIPELINE_REPORT.md`: research pipeline progress log.

## Data placement

Datasets are intentionally not committed. Place PeMS data under:

```text
TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv
TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv
TRC-23-02333/dataset/PeMS7_1026/PeMSD7_V_1026.csv
TRC-23-02333/dataset/PeMS7_1026/PeMSD7_W_1026.csv
```

Seattle heterogeneous-network files:

```text
TRC-23-02333/dataset/Seattle/tensor.npz
TRC-23-02333/dataset/Seattle/Loop_Seattle_2015_A.npy
```

The evaluator auto-detects `PeMSD7_V_*.csv` and `PeMSD7_W_*.csv` within `--data-root`.

## Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Note:** Raw datasets are not distributed with this repository (excluded via `.gitignore`). See [Data placement](#data-placement) for required file paths.

## Smoke test

Quick sanity check with a small budget and one seed (requires PeMS7_228 data):

```bash
python TRC-23-02333/trace_biopt.py \
  --data-root TRC-23-02333/dataset/PeMS7_228 \
  --budgets "0.10" \
  --seeds 25 \
  --include-baseline-portfolio \
  --output-dir TRC-23-02333/trace_sl_results/example_trace_biopt
```

Run the unit-test suite (no dataset required):

```bash
python TRC-23-02333/test_transparent_estimator_eval.py
```

## Reproduce TRACE-BiOpt evidence

Run the TRACE-BiOpt solver and refresh the current-best paper chain:

```bash
python TRC-23-02333/trace_biopt.py --data-root TRC-23-02333/dataset/PeMS7_228 \
  --include-biopt --output-dir TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_seed25

# Paper table regeneration:
bash scripts/refresh_current_best_trace_biopt_paper_chain.sh
```

Or use the transparent evaluator with the `--include-biopt` flag:

```bash
python TRC-23-02333/transparent_estimator_eval.py --data-root TRC-23-02333/dataset/PeMS7_228 \
  --include-biopt --output-dir TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_seed25
```

Compile the manuscript:

```bash
cd paper && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

## Historical TRACE-SL / RCSS Baseline (legacy)

TRACE-SL (Transparent Reconstruction-Aware Sensor Layout) was the predecessor method that used GLS/MAP and GSP reconstruction evaluators with Robust Certificate-guided Sensor Search (RCSS): an OR-guided candidate pool plus validation-calibrated selection and validation-aware swap refinement. TRACE-SL remains available as baseline row `validation_swap_selected` within the TRACE-BiOpt comparison class.

### Legacy Stage 12 TRACE-SL evidence

The Stage 12 baseline-portfolio evidence for TRACE-SL/RCSS is preserved in:

- `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/`
- `TRC-23-02333/trace_sl_results/pems7_1026_stage12_baseline_portfolio/`
- `TRC-23-02333/trace_sl_results/seattle_stage12_baseline_portfolio/`
- `TRC-23-02333/trace_sl_results/paper_sources/`

These artifacts are superseded by the TRACE-BiOpt current-best evidence chain for current manuscript claims, but remain valid as historical baseline evidence.

### Legacy reproduction commands

```bash
# Stage 12 TRACE-SL baseline-portfolio runs
bash scripts/run_stage12_pems7_228.sh
bash scripts/run_stage12_pems7_1026.sh
bash scripts/run_stage12_seattle.sh

# Stage 11 TRACE-SL development runs (historical)
bash scripts/run_stage11_pems7_228.sh
bash scripts/run_stage11_pems7_1026.sh
bash scripts/run_stage11_seattle.sh
```
