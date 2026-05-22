#!/usr/bin/env bash
set -euo pipefail

DATA_ROOT="${DATA_ROOT:-TRC-23-02333/dataset/PeMS7_228}"
OUTPUT_DIR="${OUTPUT_DIR:-TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity}"
SEEDS="${SEEDS:-25}"
BUDGETS="${BUDGETS:-0.20}"
CANDIDATE_COUNTS="${CANDIDATE_COUNTS:-50 100 200 500}"
NUM_LAYOUTS="${NUM_LAYOUTS:-50}"
SCENARIO_COUNT="${SCENARIO_COUNT:-4}"
VALIDATION_SWAP_STARTS="${VALIDATION_SWAP_STARTS:-3}"
VALIDATION_SWAP_ITER="${VALIDATION_SWAP_ITER:-5}"
VALIDATION_SWAP_ADD_POOL="${VALIDATION_SWAP_ADD_POOL:-20}"
VALIDATION_SWAP_REMOVE_POOL="${VALIDATION_SWAP_REMOVE_POOL:-8}"
THREADS_PER_JOB="${THREADS_PER_JOB:-1}"
DRY_RUN="${DRY_RUN:-0}"
PYTHON_BIN="${PYTHON_BIN:-python}"

export OMP_NUM_THREADS="${OMP_NUM_THREADS:-${THREADS_PER_JOB}}"
export OPENBLAS_NUM_THREADS="${OPENBLAS_NUM_THREADS:-${THREADS_PER_JOB}}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-${THREADS_PER_JOB}}"
export NUMEXPR_NUM_THREADS="${NUMEXPR_NUM_THREADS:-${THREADS_PER_JOB}}"
export VECLIB_MAXIMUM_THREADS="${VECLIB_MAXIMUM_THREADS:-${THREADS_PER_JOB}}"

run_or_print() {
  if [ "${DRY_RUN}" = "1" ]; then
    printf 'DRY_RUN:'
    printf ' %q' "$@"
    printf '\n'
  else
    "$@"
  fi
}

mkdir -p "${OUTPUT_DIR}"

if [ "${DRY_RUN}" = "1" ]; then
  for candidate_count in ${CANDIDATE_COUNTS}; do
    run_or_print "${PYTHON_BIN}" TRC-23-02333/transparent_estimator_eval.py \
      --data-root "${DATA_ROOT}" \
      --output-dir "${OUTPUT_DIR}/candidates_${candidate_count}/seed_25" \
      --budgets "${BUDGETS}" \
      --num-layouts "${NUM_LAYOUTS}" \
      --split-seed 25 \
      --layout-seed 2051 \
      --include-simple-baselines \
      --include-greedy \
      --include-swap \
      --include-scenario-greedy \
      --include-rcss \
      --rcss-auto-weights \
      --rcss-random-candidates "${candidate_count}" \
      --rcss-quality-candidates "${candidate_count}" \
      --scenario-count "${SCENARIO_COUNT}" \
      --include-validation-swap \
      --validation-swap-starts "${VALIDATION_SWAP_STARTS}" \
      --validation-swap-iter "${VALIDATION_SWAP_ITER}" \
      --validation-swap-add-pool "${VALIDATION_SWAP_ADD_POOL}" \
      --validation-swap-remove-pool "${VALIDATION_SWAP_REMOVE_POOL}"
    run_or_print "${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
      --input-root "${OUTPUT_DIR}/candidates_${candidate_count}" \
      --output-dir "${OUTPUT_DIR}/candidates_${candidate_count}"
  done
  run_or_print "${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
    --input-root "${OUTPUT_DIR}"/candidates_* \
    --runtime-root "${OUTPUT_DIR}" \
    --output-dir "${OUTPUT_DIR}"
  exit 0
fi

: > "${OUTPUT_DIR}/stage13_timing.csv"
printf 'candidate_count,seed,runtime_seconds,status,output_dir\n' >> "${OUTPUT_DIR}/stage13_timing.csv"

for candidate_count in ${CANDIDATE_COUNTS}; do
  candidate_dir="${OUTPUT_DIR}/candidates_${candidate_count}"
  mkdir -p "${candidate_dir}"
  for seed in ${SEEDS}; do
    seed_dir="${candidate_dir}/seed_${seed}"
    start_epoch="$(date +%s)"
    "${PYTHON_BIN}" TRC-23-02333/transparent_estimator_eval.py \
      --data-root "${DATA_ROOT}" \
      --output-dir "${seed_dir}" \
      --budgets "${BUDGETS}" \
      --num-layouts "${NUM_LAYOUTS}" \
      --split-seed "${seed}" \
      --layout-seed "$((2026 + seed + candidate_count))" \
      --include-simple-baselines \
      --include-greedy \
      --include-swap \
      --include-scenario-greedy \
      --include-rcss \
      --rcss-auto-weights \
      --rcss-random-candidates "${candidate_count}" \
      --rcss-quality-candidates "${candidate_count}" \
      --scenario-count "${SCENARIO_COUNT}" \
      --include-validation-swap \
      --validation-swap-starts "${VALIDATION_SWAP_STARTS}" \
      --validation-swap-iter "${VALIDATION_SWAP_ITER}" \
      --validation-swap-add-pool "${VALIDATION_SWAP_ADD_POOL}" \
      --validation-swap-remove-pool "${VALIDATION_SWAP_REMOVE_POOL}" \
      2>&1 | tee "${OUTPUT_DIR}_candidates_${candidate_count}_seed_${seed}.log"
    end_epoch="$(date +%s)"
    runtime_seconds="$((end_epoch - start_epoch))"
    printf '%s,%s,%s,complete,%s\n' "${candidate_count}" "${seed}" "${runtime_seconds}" "${seed_dir}" >> "${OUTPUT_DIR}/stage13_timing.csv"
  done
  "${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
    --input-root "${candidate_dir}" \
    --output-dir "${candidate_dir}"
done

"${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
  --input-root "${OUTPUT_DIR}"/candidates_* \
  --runtime-root "${OUTPUT_DIR}" \
  --output-dir "${OUTPUT_DIR}"
