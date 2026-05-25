#!/usr/bin/env bash
set -euo pipefail

DATA_ROOT="${DATA_ROOT:-TRC-23-02333/dataset/PeMS7_1026}"
OUTPUT_DIR="${OUTPUT_DIR:-TRC-23-02333/trace_sl_results/pems7_1026_stage12_baseline_portfolio}"
SEEDS="${SEEDS:-25 26 27 28 29 30 31 32 33 34}"
BUDGETS="${BUDGETS:-0.10 0.20 0.30}"
NUM_LAYOUTS="${NUM_LAYOUTS:-100}"
RCSS_RANDOM_CANDIDATES="${RCSS_RANDOM_CANDIDATES:-100}"
RCSS_QUALITY_CANDIDATES="${RCSS_QUALITY_CANDIDATES:-100}"
SCENARIO_COUNT="${SCENARIO_COUNT:-8}"
VALIDATION_SWAP_STARTS="${VALIDATION_SWAP_STARTS:-3}"
VALIDATION_SWAP_ITER="${VALIDATION_SWAP_ITER:-8}"
VALIDATION_SWAP_ADD_POOL="${VALIDATION_SWAP_ADD_POOL:-30}"
VALIDATION_SWAP_REMOVE_POOL="${VALIDATION_SWAP_REMOVE_POOL:-10}"
THREADS_PER_JOB="${THREADS_PER_JOB:-1}"
MAX_JOBS="${MAX_JOBS:-1}"
MAX_RSS_MB="${MAX_RSS_MB:-0}"
DRY_RUN="${DRY_RUN:-0}"
ENABLE_PROGRESS="${ENABLE_PROGRESS:-1}"
PROGRESS_DIR="${PROGRESS_DIR:-${OUTPUT_DIR}/progress}"
FEASIBILITY_RUN="${FEASIBILITY_RUN:-0}"
PYTHON_BIN="${PYTHON_BIN:-python}"

export OMP_NUM_THREADS="${OMP_NUM_THREADS:-${THREADS_PER_JOB}}"
export OPENBLAS_NUM_THREADS="${OPENBLAS_NUM_THREADS:-${THREADS_PER_JOB}}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-${THREADS_PER_JOB}}"
export NUMEXPR_NUM_THREADS="${NUMEXPR_NUM_THREADS:-${THREADS_PER_JOB}}"
export VECLIB_MAXIMUM_THREADS="${VECLIB_MAXIMUM_THREADS:-${THREADS_PER_JOB}}"

mkdir -p "${OUTPUT_DIR}"
if [ "${ENABLE_PROGRESS}" = "1" ]; then
  mkdir -p "${PROGRESS_DIR}"
fi

run_or_print() {
  if [ "${DRY_RUN}" = "1" ]; then
    printf 'DRY_RUN:'
    printf ' %q' "$@"
    printf '\n'
  else
    "$@"
  fi
}

running_jobs=0
status=0

for seed in ${SEEDS}; do
  progress_args=()
  if [ "${ENABLE_PROGRESS}" = "1" ]; then
    progress_args+=(
      --progress-log "${PROGRESS_DIR}/seed_${seed}_progress.jsonl"
      --checkpoint-json "${PROGRESS_DIR}/seed_${seed}_checkpoint.json"
    )
  fi
  if [ "${FEASIBILITY_RUN}" = "1" ]; then
    progress_args+=(--non-evidence-feasibility-run)
  fi

  eval_cmd=(
    "${PYTHON_BIN}" TRC-23-02333/transparent_estimator_eval.py
    --data-root "${DATA_ROOT}"
    --output-dir "${OUTPUT_DIR}/seed_${seed}"
    --budgets "${BUDGETS}"
    --num-layouts "${NUM_LAYOUTS}"
    --split-seed "${seed}"
    --layout-seed "$((3026 + seed))"
    --include-simple-baselines
    --include-greedy
    --include-swap
    --include-scenario-greedy
    --include-rcss
    --rcss-auto-weights
    --rcss-random-candidates "${RCSS_RANDOM_CANDIDATES}"
    --rcss-quality-candidates "${RCSS_QUALITY_CANDIDATES}"
    --scenario-count "${SCENARIO_COUNT}"
    --include-validation-swap
    --validation-swap-starts "${VALIDATION_SWAP_STARTS}"
    --validation-swap-iter "${VALIDATION_SWAP_ITER}"
    --validation-swap-add-pool "${VALIDATION_SWAP_ADD_POOL}"
    --validation-swap-remove-pool "${VALIDATION_SWAP_REMOVE_POOL}"
    --include-baseline-portfolio
    --include-observability-proxy
    --include-graph-sampling-baseline
    --include-qr-pod-baseline
    --max-rss-mb "${MAX_RSS_MB}"
    "${progress_args[@]}"
  )
  if [ "${DRY_RUN}" = "1" ]; then
    run_or_print "${eval_cmd[@]}"
  else
    (
      "${eval_cmd[@]}" > "${OUTPUT_DIR}_seed_${seed}.log" 2>&1
    ) &
    running_jobs=$((running_jobs + 1))
    if [ "${running_jobs}" -ge "${MAX_JOBS}" ]; then
      if ! wait -n; then
        status=1
      fi
      running_jobs=$((running_jobs - 1))
    fi
  fi
done

while [ "${running_jobs}" -gt 0 ]; do
  if ! wait -n; then
    status=1
  fi
  running_jobs=$((running_jobs - 1))
done

if [ "${status}" -ne 0 ]; then
  exit "${status}"
fi

run_or_print "${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
  --input-root "${OUTPUT_DIR}" \
  --output-dir "${OUTPUT_DIR}"
