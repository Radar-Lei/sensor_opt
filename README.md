# TRACE-SL: Transparent Reconstruction-Aware Sensor Layout

TRACE-SL studies sparse traffic sensor placement for transparent full-network reconstruction. The current implementation uses GLS/MAP and GSP reconstruction evaluators, then searches for sensor layouts with Robust Certified Sensor Search (RCSS): an OR-guided candidate pool plus validation-calibrated selection and validation-aware swap refinement.

## Current claim

TRACE-SL is not framed as an RL estimator or a black-box imputation model. The core claim is that OR-guided candidate generation, transparent GLS/MAP reconstruction, and validation-calibrated swap selection produce interpretable sensor layouts that improve full-network reconstruction over strong random and topology baselines.

## Main PeMS7_228 result

The strongest current configuration is Stage 11: automatic RCSS weight selection with validation-aware swap refinement. The 10-split aggregate is in `TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`.

| Budget | Validation-swap RCSS MAE | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.6055 | 3.6913 | 3.8359 | 3.7304 |
| 20% | 3.3095 | 3.3969 | 3.5648 | 3.4276 |
| 30% | 3.0665 | 3.1832 | 3.4032 | 3.2004 |

Paired tests against validation-selected random now support the improvement across all budgets: p=0.0343 at 10%, p=0.0025 at 20%, and p=0.00008 at 30%. Stage 11 also finds that posterior certificates remain strongly aligned with GLS/MAP hidden-link reconstruction error: posterior trace Spearman correlation is about 0.851, condition number about 0.859, and information logdet about -0.813.

## External PeMS7_1026 validation

PeMS7_1026 external validation uses the same Stage 11 pipeline with 100 random/RCSS candidates per split. The aggregate is in `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/`.

| Budget | Validation-swap RCSS MAE | Best random by validation | Random mean | Top variance |
|---:|---:|---:|---:|---:|
| 10% | 3.6557 | 3.7437 | 3.8266 | 3.8602 |
| 20% | 3.2547 | 3.4653 | 3.5317 | 3.5859 |
| 30% | 2.9951 | 3.2483 | 3.3309 | 3.3266 |

Validation-swap RCSS wins against validation-selected random in all five PeMS7_1026 splits at every budget. Paired t-test p-values are 0.0212, 0.0007, and 0.0001 for 10%, 20%, and 30% respectively.

## Repository layout

- `TRC-23-02333/transparent_estimator_eval.py`: TRACE-SL evaluator and RCSS experiment driver.
- `TRC-23-02333/summarize_trace_sl_rcss.py`: multi-split result aggregation script.
- `TRC-23-02333/trace_sl_results/`: checked-in PeMS7_228 Stage 6--11 and PeMS7_1026 external-validation outputs.
- `scripts/run_stage11_pems7_228.sh`: reproduces Stage 11 PeMS7_228 split runs and aggregation.
- `scripts/run_stage11_pems7_1026.sh`: launches the same Stage 11 pipeline on PeMS7_1026 for external validation.
- `NARRATIVE_REPORT.md`: writing handoff with method framing and current evidence.
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

## Reproduce Stage 11 on PeMS7_228

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

## External validation starting point

PeMS7_1026 uses the same loader format. A smaller external validation default is provided because the network has 1026 nodes:

```bash
bash scripts/run_stage11_pems7_1026.sh
```

You can still override seeds and candidate counts:

```bash
SEEDS="25 26 27" NUM_LAYOUTS=50 RCSS_RANDOM_CANDIDATES=50 RCSS_QUALITY_CANDIDATES=50 \
bash scripts/run_stage11_pems7_1026.sh
```
