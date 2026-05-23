#!/usr/bin/env bash
set -euo pipefail

DATA_ROOT="${DATA_ROOT:-TRC-23-02333/dataset/PeMS7_228}"
OUTPUT_DIR="${OUTPUT_DIR:-TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness}"
SEEDS="${SEEDS:-25}"
BUDGETS="${BUDGETS:-0.20}"
NUM_LAYOUTS="${NUM_LAYOUTS:-10}"
RCSS_RANDOM_CANDIDATES="${RCSS_RANDOM_CANDIDATES:-10}"
RCSS_QUALITY_CANDIDATES="${RCSS_QUALITY_CANDIDATES:-10}"
SCENARIO_COUNT="${SCENARIO_COUNT:-2}"
VALIDATION_SWAP_STARTS="${VALIDATION_SWAP_STARTS:-2}"
VALIDATION_SWAP_ITER="${VALIDATION_SWAP_ITER:-3}"
VALIDATION_SWAP_ADD_POOL="${VALIDATION_SWAP_ADD_POOL:-12}"
VALIDATION_SWAP_REMOVE_POOL="${VALIDATION_SWAP_REMOVE_POOL:-6}"
MAX_TEST_STEPS="${MAX_TEST_STEPS:-0}"
THREADS_PER_JOB="${THREADS_PER_JOB:-1}"
DRY_RUN="${DRY_RUN:-0}"
PYTHON_BIN="${PYTHON_BIN:-python}"
COST_BUDGET="${COST_BUDGET:-45}"

export OMP_NUM_THREADS="${OMP_NUM_THREADS:-${THREADS_PER_JOB}}"
export OPENBLAS_NUM_THREADS="${OPENBLAS_NUM_THREADS:-${THREADS_PER_JOB}}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-${THREADS_PER_JOB}}"
export NUMEXPR_NUM_THREADS="${NUMEXPR_NUM_THREADS:-${THREADS_PER_JOB}}"
export VECLIB_MAXIMUM_THREADS="${VECLIB_MAXIMUM_THREADS:-${THREADS_PER_JOB}}"

mkdir -p "${OUTPUT_DIR}"
summary_inputs=()

run_or_print() {
  if [ "${DRY_RUN}" = "1" ]; then
    printf 'DRY_RUN:'
    printf ' %q' "$@"
    printf '\n'
  else
    "$@"
  fi
}

condition_args() {
  case "$1" in
    baseline)
      printf '%s\n' --robustness-family baseline --robustness-condition baseline
      ;;
    failure_0.05)
      printf '%s\n' --robustness-family sensor_failure --robustness-condition failure_0.05 --failure-rate 0.05
      ;;
    failure_0.10)
      printf '%s\n' --robustness-family sensor_failure --robustness-condition failure_0.10 --failure-rate 0.10
      ;;
    failure_0.20)
      printf '%s\n' --robustness-family sensor_failure --robustness-condition failure_0.20 --failure-rate 0.20
      ;;
    noise_0.05)
      printf '%s\n' --robustness-family observation_noise --robustness-condition noise_0.05 --noise-scale 0.05
      ;;
    random_missing_0.10)
      printf '%s\n' --robustness-family random_missing --robustness-condition random_missing_0.10 --missing-rate 0.10
      ;;
    block_missing_12)
      printf '%s\n' --robustness-family block_missing --robustness-condition block_missing_12 --missing-block-steps 12
      ;;
    cost_proxy_budget)
      printf '%s\n' --robustness-family cost_proxy --robustness-condition cost_proxy_budget --cost-proxy graph_traffic --cost-budget "${COST_BUDGET}"
      ;;
    chronological_split)
      printf '%s\n' --robustness-family temporal_shift --robustness-condition chronological_split --split-mode chronological
      ;;
    *)
      printf 'Unknown robustness condition: %s\n' "$1" >&2
      return 1
      ;;
  esac
}

CONDITIONS=(
  baseline
  failure_0.05
  failure_0.10
  failure_0.20
  noise_0.05
  random_missing_0.10
  block_missing_12
  cost_proxy_budget
  chronological_split
)

for condition in "${CONDITIONS[@]}"; do
  mapfile -t robustness_args < <(condition_args "${condition}")
  for seed in ${SEEDS}; do
    seed_dir="${OUTPUT_DIR}/${condition}/seed_${seed}"
    eval_cmd=(
      "${PYTHON_BIN}" TRC-23-02333/transparent_estimator_eval.py
      --data-root "${DATA_ROOT}"
      --output-dir "${seed_dir}"
      --budgets "${BUDGETS}"
      --num-layouts "${NUM_LAYOUTS}"
      --split-seed "${seed}"
      --layout-seed "$((2026 + seed))"
      --robustness-seed "$((5050 + seed))"
      --max-test-steps "${MAX_TEST_STEPS}"
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
      "${robustness_args[@]}"
    )
    if [ "${DRY_RUN}" = "1" ]; then
      run_or_print "${eval_cmd[@]}"
      summary_inputs+=("${seed_dir}")
    else
      mkdir -p "${OUTPUT_DIR}/${condition}"
      "${eval_cmd[@]}" 2>&1 | tee "${OUTPUT_DIR}/${condition}_seed_${seed}.log"
      summary_inputs+=("${seed_dir}")
    fi
  done
done

run_or_print "${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
  --input-root "${summary_inputs[@]}" \
  --output-dir "${OUTPUT_DIR}"
