# TRACE-SL: Transparent Reconstruction-Aware Sensor Layout

TRACE-SL studies sparse traffic sensor placement for transparent full-network reconstruction. The current implementation uses GLS/MAP and GSP reconstruction evaluators, then searches for sensor layouts with Robust Certificate-guided Sensor Search (RCSS): an OR-guided candidate pool plus validation-calibrated selection and validation-aware swap refinement.

## Current claim

TRACE-SL is not framed as an RL estimator or a black-box imputation model. The core claim is that OR-guided candidate generation, transparent GLS/MAP reconstruction, and validation-calibrated swap selection produce interpretable sensor layouts that improve full-network reconstruction over strong random and topology baselines.

Method formulation: TRACE-SL is reconstruction-aware sensor-set design: choose a sparse fixed sensor set for hidden-node reconstruction using transparent GLS/MAP or GSP reconstruction, RCSS validation-calibrated selection, and posterior-certificate-aware diagnostics. The compact public pointer is here; detailed formulation and theory notes are in `.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md` and the optional `.planning/phases/02-formulation-and-theory-bridge/02-TR-PART-B-THEORY-GAP-NOTE.md`.

For a TR-B-style manuscript, the intended framing is stronger and narrower than "a new heuristic with lower PeMS MAE": TRACE-SL reframes sparse traffic sensor placement as reconstruction-aware inverse-problem design. Sensors are selected to make hidden network states recoverable under transparent GLS/MAP and GSP reconstruction, not merely to maximize coverage, topology centrality, or marginal variance. The current claim boundary is certificate-guided and posterior-certificate-aware, not certified, globally optimal, globally robust, or guaranteed to improve MAE outside the tested settings.

## Current paper-source truth

The current manuscript-facing source of truth is the Stage 12 paper-source package in `TRC-23-02333/trace_sl_results/paper_sources/`. Stage 11 results are retained as development and diagnostic history; Stage 12 baseline-portfolio artifacts supersede them for claim-facing tables.

The strongest claim should be written at the TRACE-SL framework/portfolio level: certificate-guided candidate generation, validation-calibrated selection, and validation-aware local refinement systematically produce recoverable layouts across tested networks and budgets. `validation_swap_selected` remains the main reported selector, but internal OR variants such as greedy A-trace and swap-from-greedy are mechanisms/comparators within the framework rather than evidence that the final selector dominates every variant everywhere.

## Stage 12 core PeMS7_228 result

Current core in-domain evidence is in `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/` and generated views under `TRC-23-02333/trace_sl_results/paper_sources/`.

| Budget | Validation-swap RCSS MAE | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.5901 | 3.7131 | 3.8331 | 3.7304 |
| 20% | 3.3547 | 3.4495 | 3.5746 | 3.4276 |
| 30% | 3.0842 | 3.2469 | 3.4037 | 3.2004 |

Paired Stage 12 tests support improvement over validation-selected random across all PeMS7_228 budgets: p=0.0000876 at 10%, p=0.00537 at 20%, and p=0.000509 at 30%. The 10% budget carries the explicit caveat `pems7_228_low_budget_multistart_not_dominant`, because the multistart comparator is statistically close there.

## Stage 12 external evidence

External evidence is complete in the Stage 12 gate: PeMS7_1026 and Seattle each have tracked ten-split Stage 12 aggregate artifacts and are marked core-eligible by `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.md`. This supports multi-network empirical evidence, not universal cross-network generalization.

| Dataset | Budget | Validation-swap RCSS MAE | Split count |
|---|---:|---:|---:|
| PeMS7_1026 | 10% | 3.7674 | 10 |
| PeMS7_1026 | 20% | 3.3467 | 10 |
| PeMS7_1026 | 30% | 3.0740 | 10 |
| Seattle | 10% | 3.1012 | 10 |
| Seattle | 20% | 2.8281 | 10 |
| Seattle | 30% | 2.6241 | 10 |

At PeMS7_1026 10%, `swap_from_greedy_a_trace` and `greedy_a_trace` slightly outperform `validation_swap_selected`; this is why manuscript claims should describe TRACE-SL as a reconstruction-aware layout design framework/portfolio rather than a single selector that dominates every internal OR variant.

## Repository layout

- `TRC-23-02333/transparent_estimator_eval.py`: TRACE-SL evaluator and RCSS experiment driver.
- `TRC-23-02333/summarize_trace_sl_rcss.py`: multi-split result aggregation script.
- `TRC-23-02333/trace_sl_results/`: checked-in TRACE-SL result artifacts, including Stage 12 baseline portfolios for PeMS7_228, PeMS7_1026, and Seattle.
- `TRC-23-02333/trace_sl_results/paper_sources/`: generated manuscript-facing CSV/JSON/Markdown source tables and claim/evidence/theory contracts.
- `scripts/run_stage11_pems7_228.sh`: reproduces Stage 11 PeMS7_228 split runs and aggregation.
- `scripts/run_stage11_pems7_1026.sh`: launches the same Stage 11 pipeline on PeMS7_1026 for external validation.
- `scripts/run_stage12_pems7_228.sh`, `scripts/run_stage12_pems7_1026.sh`, `scripts/run_stage12_seattle.sh`: reproduce Stage 12 baseline-portfolio evidence.
- `NARRATIVE_REPORT.md`: writing handoff with method framing and current evidence.
- `.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md`: Phase 2 budgeted reconstruction-aware formulation, RCSS surrogate, posterior-error bridge, and validation-swap analysis.
- `.planning/phases/02-formulation-and-theory-bridge/02-TR-PART-B-THEORY-GAP-NOTE.md`: optional TR Part B theory-gap note for deferred v2 monotonicity, approximation, stability, and stochastic/bilevel analysis.
- `RESEARCH_PIPELINE_REPORT.md`: research pipeline progress log.

## Data placement

Datasets are intentionally not committed. Place PeMS data under:

```text
TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv
TRC-23-02333/dataset/PeMS7_228/PeMSD7_W_228.csv
TRC-23-02333/dataset/PeMS7_1026/PeMSD7_V_1026.csv
TRC-23-02333/dataset/PeMS7_1026/PeMSD7_W_1026.csv
```

The evaluator auto-detects `PeMSD7_V_*.csv` and `PeMSD7_W_*.csv` within `--data-root`.

## Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Reproduce Stage 12 evidence

```bash
bash scripts/run_stage12_pems7_228.sh
bash scripts/run_stage12_pems7_1026.sh
bash scripts/run_stage12_seattle.sh
```

Regenerate paper-source tables after Stage 12 aggregates are present:

```bash
python scripts/generate_trace_sl_paper_sources.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources
python scripts/generate_trace_sl_claim_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources
python scripts/generate_trace_sl_external_evidence_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources
python scripts/generate_trace_sl_ablation_evidence_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources
python scripts/generate_trace_sl_theory_handoff_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources
```

## Legacy Stage 11 development run

```bash
bash scripts/run_stage11_pems7_228.sh
```

By default this runs split seeds `25 26 27 28 29` and writes to:

```text
TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight/
```

The scripts default to `THREADS_PER_JOB=1` to avoid BLAS oversubscription when running seeds in parallel. To run additional split seeds for stronger statistics:

```bash
SEEDS="30 31 32 33 34" \
OUTPUT_DIR="TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_extra" \
bash scripts/run_stage11_pems7_228.sh
```

To merge the original and extra split directories:

```bash
python TRC-23-02333/summarize_trace_sl_rcss.py \
  --input-root TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight \
               TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_extra \
  --output-dir TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split
```

## Legacy external validation starting point

PeMS7_1026 uses the same loader format. This Stage 11 default is kept for development-history reproduction; current external evidence should use the Stage 12 scripts above.

```bash
bash scripts/run_stage11_pems7_1026.sh
```

You can still override seeds and candidate counts:

```bash
SEEDS="25 26 27" NUM_LAYOUTS=50 RCSS_RANDOM_CANDIDATES=50 RCSS_QUALITY_CANDIDATES=50 \
bash scripts/run_stage11_pems7_1026.sh
```
