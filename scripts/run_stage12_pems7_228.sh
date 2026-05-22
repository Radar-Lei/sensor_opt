#!/usr/bin/env bash
set -euo pipefail

DATA_ROOT="${DATA_ROOT:-TRC-23-02333/dataset/PeMS7_228}"
OUTPUT_DIR="${OUTPUT_DIR:-TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio}"
SEEDS="${SEEDS:-25}"
BUDGETS="${BUDGETS:-0.10 0.20 0.30}"
NUM_LAYOUTS="${NUM_LAYOUTS:-50}"
RCSS_RANDOM_CANDIDATES="${RCSS_RANDOM_CANDIDATES:-50}"
RCSS_QUALITY_CANDIDATES="${RCSS_QUALITY_CANDIDATES:-50}"
SCENARIO_COUNT="${SCENARIO_COUNT:-4}"
VALIDATION_SWAP_STARTS="${VALIDATION_SWAP_STARTS:-3}"
VALIDATION_SWAP_ITER="${VALIDATION_SWAP_ITER:-5}"
VALIDATION_SWAP_ADD_POOL="${VALIDATION_SWAP_ADD_POOL:-20}"
VALIDATION_SWAP_REMOVE_POOL="${VALIDATION_SWAP_REMOVE_POOL:-8}"
THREADS_PER_JOB="${THREADS_PER_JOB:-1}"

export OMP_NUM_THREADS="${OMP_NUM_THREADS:-${THREADS_PER_JOB}}"
export OPENBLAS_NUM_THREADS="${OPENBLAS_NUM_THREADS:-${THREADS_PER_JOB}}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-${THREADS_PER_JOB}}"
export NUMEXPR_NUM_THREADS="${NUMEXPR_NUM_THREADS:-${THREADS_PER_JOB}}"
export VECLIB_MAXIMUM_THREADS="${VECLIB_MAXIMUM_THREADS:-${THREADS_PER_JOB}}"

mkdir -p "${OUTPUT_DIR}"

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
    --include-baseline-portfolio \
    --include-observability-proxy \
    --include-graph-sampling-baseline \
    --include-qr-pod-baseline \
    2>&1 | tee "${OUTPUT_DIR}_seed_${seed}.log"
done

python TRC-23-02333/summarize_trace_sl_rcss.py \
  --input-root "${OUTPUT_DIR}" \
  --output-dir "${OUTPUT_DIR}"
