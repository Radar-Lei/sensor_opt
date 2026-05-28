#!/usr/bin/env bash
set -euo pipefail

OUTPUT_ROOT="${OUTPUT_ROOT:-TRC-23-02333/trace_sl_results/stage15_biopt_weak_points}"
SEEDS="${SEEDS:-25}"
BUDGETS="${BUDGETS:-0.10}"
NUM_LAYOUTS="${NUM_LAYOUTS:-25}"
RCSS_RANDOM_CANDIDATES="${RCSS_RANDOM_CANDIDATES:-25}"
RCSS_QUALITY_CANDIDATES="${RCSS_QUALITY_CANDIDATES:-25}"
SCENARIO_COUNT="${SCENARIO_COUNT:-8}"
VALIDATION_SWAP_STARTS="${VALIDATION_SWAP_STARTS:-3}"
VALIDATION_SWAP_ITER="${VALIDATION_SWAP_ITER:-8}"
VALIDATION_SWAP_ADD_POOL="${VALIDATION_SWAP_ADD_POOL:-30}"
VALIDATION_SWAP_REMOVE_POOL="${VALIDATION_SWAP_REMOVE_POOL:-10}"
TRACE_BIOPT_BETA="${TRACE_BIOPT_BETA:-2.0}"
TRACE_BIOPT_GAMMA="${TRACE_BIOPT_GAMMA:-0.05}"
TRACE_BIOPT_ETA="${TRACE_BIOPT_ETA:-0.01}"
TRACE_BIOPT_HUBER_DELTA="${TRACE_BIOPT_HUBER_DELTA:-5.0}"
TRACE_BIOPT_EXCHANGE_ITER="${TRACE_BIOPT_EXCHANGE_ITER:-3}"
TRACE_BIOPT_FORWARD_POOL="${TRACE_BIOPT_FORWARD_POOL:-24}"
TRACE_BIOPT_EXCHANGE_ADD_POOL="${TRACE_BIOPT_EXCHANGE_ADD_POOL:-24}"
TRACE_BIOPT_EXCHANGE_REMOVE_POOL="${TRACE_BIOPT_EXCHANGE_REMOVE_POOL:-8}"
TRACE_BIOPT_OBJECTIVE_STEPS="${TRACE_BIOPT_OBJECTIVE_STEPS:-96}"
TRACE_BIOPT_INITIALIZER="${TRACE_BIOPT_INITIALIZER:-auto}"
TRACE_BIOPT_AUTO_WARM_START_THRESHOLD="${TRACE_BIOPT_AUTO_WARM_START_THRESHOLD:-500}"
TRACE_BIOPT_RELAX_ITER="${TRACE_BIOPT_RELAX_ITER:-6}"
TRACE_BIOPT_RELAX_STEP="${TRACE_BIOPT_RELAX_STEP:-0.2}"
TRACE_BIOPT_RELAX_FD_EPS="${TRACE_BIOPT_RELAX_FD_EPS:-0.001}"
TRACE_BIOPT_RELAX_POOL="${TRACE_BIOPT_RELAX_POOL:-40}"
SEATTLE_TRACE_BIOPT_EXCHANGE_ITER="${SEATTLE_TRACE_BIOPT_EXCHANGE_ITER:-8}"
SEATTLE_TRACE_BIOPT_FORWARD_POOL="${SEATTLE_TRACE_BIOPT_FORWARD_POOL:-64}"
SEATTLE_TRACE_BIOPT_EXCHANGE_ADD_POOL="${SEATTLE_TRACE_BIOPT_EXCHANGE_ADD_POOL:-64}"
SEATTLE_TRACE_BIOPT_EXCHANGE_REMOVE_POOL="${SEATTLE_TRACE_BIOPT_EXCHANGE_REMOVE_POOL:-20}"
MAX_RSS_MB="${MAX_RSS_MB:-0}"
DRY_RUN="${DRY_RUN:-0}"
PYTHON_BIN="${PYTHON_BIN:-python}"

export OMP_NUM_THREADS="${OMP_NUM_THREADS:-1}"
export OPENBLAS_NUM_THREADS="${OPENBLAS_NUM_THREADS:-1}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-1}"
export NUMEXPR_NUM_THREADS="${NUMEXPR_NUM_THREADS:-1}"
export VECLIB_MAXIMUM_THREADS="${VECLIB_MAXIMUM_THREADS:-1}"

run_or_print() {
  if [ "${DRY_RUN}" = "1" ]; then
    printf 'DRY_RUN:'
    printf ' %q' "$@"
    printf '\n'
  else
    "$@"
  fi
}

run_dataset() {
  local name="$1"
  local data_root="$2"
  local layout_seed_offset="$3"
  local dataset_prefix="$4"
  local output_dir="${OUTPUT_ROOT}/${name}"
  local trace_biopt_beta_var="${dataset_prefix}_TRACE_BIOPT_BETA"
  local trace_biopt_gamma_var="${dataset_prefix}_TRACE_BIOPT_GAMMA"
  local trace_biopt_eta_var="${dataset_prefix}_TRACE_BIOPT_ETA"
  local trace_biopt_huber_delta_var="${dataset_prefix}_TRACE_BIOPT_HUBER_DELTA"
  local trace_biopt_exchange_iter_var="${dataset_prefix}_TRACE_BIOPT_EXCHANGE_ITER"
  local trace_biopt_forward_pool_var="${dataset_prefix}_TRACE_BIOPT_FORWARD_POOL"
  local trace_biopt_exchange_add_pool_var="${dataset_prefix}_TRACE_BIOPT_EXCHANGE_ADD_POOL"
  local trace_biopt_exchange_remove_pool_var="${dataset_prefix}_TRACE_BIOPT_EXCHANGE_REMOVE_POOL"
  local trace_biopt_objective_steps_var="${dataset_prefix}_TRACE_BIOPT_OBJECTIVE_STEPS"
  local trace_biopt_initializer_var="${dataset_prefix}_TRACE_BIOPT_INITIALIZER"
  local trace_biopt_auto_warm_start_threshold_var="${dataset_prefix}_TRACE_BIOPT_AUTO_WARM_START_THRESHOLD"
  local trace_biopt_relax_iter_var="${dataset_prefix}_TRACE_BIOPT_RELAX_ITER"
  local trace_biopt_relax_step_var="${dataset_prefix}_TRACE_BIOPT_RELAX_STEP"
  local trace_biopt_relax_fd_eps_var="${dataset_prefix}_TRACE_BIOPT_RELAX_FD_EPS"
  local trace_biopt_relax_pool_var="${dataset_prefix}_TRACE_BIOPT_RELAX_POOL"
  local trace_biopt_beta="${!trace_biopt_beta_var:-$TRACE_BIOPT_BETA}"
  local trace_biopt_gamma="${!trace_biopt_gamma_var:-$TRACE_BIOPT_GAMMA}"
  local trace_biopt_eta="${!trace_biopt_eta_var:-$TRACE_BIOPT_ETA}"
  local trace_biopt_huber_delta="${!trace_biopt_huber_delta_var:-$TRACE_BIOPT_HUBER_DELTA}"
  local trace_biopt_exchange_iter="${!trace_biopt_exchange_iter_var:-$TRACE_BIOPT_EXCHANGE_ITER}"
  local trace_biopt_forward_pool="${!trace_biopt_forward_pool_var:-$TRACE_BIOPT_FORWARD_POOL}"
  local trace_biopt_exchange_add_pool="${!trace_biopt_exchange_add_pool_var:-$TRACE_BIOPT_EXCHANGE_ADD_POOL}"
  local trace_biopt_exchange_remove_pool="${!trace_biopt_exchange_remove_pool_var:-$TRACE_BIOPT_EXCHANGE_REMOVE_POOL}"
  local trace_biopt_objective_steps="${!trace_biopt_objective_steps_var:-$TRACE_BIOPT_OBJECTIVE_STEPS}"
  local trace_biopt_initializer="${!trace_biopt_initializer_var:-$TRACE_BIOPT_INITIALIZER}"
  local trace_biopt_auto_warm_start_threshold="${!trace_biopt_auto_warm_start_threshold_var:-$TRACE_BIOPT_AUTO_WARM_START_THRESHOLD}"
  local trace_biopt_relax_iter="${!trace_biopt_relax_iter_var:-$TRACE_BIOPT_RELAX_ITER}"
  local trace_biopt_relax_step="${!trace_biopt_relax_step_var:-$TRACE_BIOPT_RELAX_STEP}"
  local trace_biopt_relax_fd_eps="${!trace_biopt_relax_fd_eps_var:-$TRACE_BIOPT_RELAX_FD_EPS}"
  local trace_biopt_relax_pool="${!trace_biopt_relax_pool_var:-$TRACE_BIOPT_RELAX_POOL}"
  mkdir -p "${output_dir}/progress"
  for seed in ${SEEDS}; do
    run_or_print "${PYTHON_BIN}" TRC-23-02333/transparent_estimator_eval.py \
      --data-root "${data_root}" \
      --output-dir "${output_dir}/seed_${seed}" \
      --budgets "${BUDGETS}" \
      --num-layouts "${NUM_LAYOUTS}" \
      --split-seed "${seed}" \
      --layout-seed "$((layout_seed_offset + seed))" \
      --include-biopt \
      --trace-biopt-beta "${trace_biopt_beta}" \
      --trace-biopt-gamma "${trace_biopt_gamma}" \
      --trace-biopt-eta "${trace_biopt_eta}" \
      --trace-biopt-huber-delta "${trace_biopt_huber_delta}" \
      --trace-biopt-exchange-iter "${trace_biopt_exchange_iter}" \
      --trace-biopt-forward-pool "${trace_biopt_forward_pool}" \
      --trace-biopt-exchange-add-pool "${trace_biopt_exchange_add_pool}" \
      --trace-biopt-exchange-remove-pool "${trace_biopt_exchange_remove_pool}" \
      --trace-biopt-objective-steps "${trace_biopt_objective_steps}" \
      --trace-biopt-initializer "${trace_biopt_initializer}" \
      --trace-biopt-auto-warm-start-threshold "${trace_biopt_auto_warm_start_threshold}" \
      --trace-biopt-relax-iter "${trace_biopt_relax_iter}" \
      --trace-biopt-relax-step "${trace_biopt_relax_step}" \
      --trace-biopt-relax-fd-eps "${trace_biopt_relax_fd_eps}" \
      --trace-biopt-relax-pool "${trace_biopt_relax_pool}" \
      --include-baseline-portfolio \
      --rcss-auto-weights \
      --rcss-random-candidates "${RCSS_RANDOM_CANDIDATES}" \
      --rcss-quality-candidates "${RCSS_QUALITY_CANDIDATES}" \
      --scenario-count "${SCENARIO_COUNT}" \
      --include-validation-swap \
      --validation-swap-starts "${VALIDATION_SWAP_STARTS}" \
      --validation-swap-iter "${VALIDATION_SWAP_ITER}" \
      --validation-swap-add-pool "${VALIDATION_SWAP_ADD_POOL}" \
      --validation-swap-remove-pool "${VALIDATION_SWAP_REMOVE_POOL}" \
      --max-rss-mb "${MAX_RSS_MB}" \
      --progress-log "${output_dir}/progress/seed_${seed}_progress.jsonl" \
      --checkpoint-json "${output_dir}/progress/seed_${seed}_checkpoint.json"
  done
  run_or_print "${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
    --input-root "${output_dir}" \
    --output-dir "${output_dir}"
}

run_dataset "pems7_1026" "TRC-23-02333/dataset/PeMS7_1026" 5026 "PEMS7_1026"
run_dataset "seattle" "TRC-23-02333/dataset/Seattle" 6026 "SEATTLE"
run_dataset "pems7_228" "TRC-23-02333/dataset/PeMS7_228" 7026 "PEMS7_228"

run_or_print "${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
  --input-root "${OUTPUT_ROOT}/pems7_1026" "${OUTPUT_ROOT}/seattle" "${OUTPUT_ROOT}/pems7_228" \
  --output-dir "${OUTPUT_ROOT}/combined"

run_or_print "${PYTHON_BIN}" scripts/generate_trace_biopt_dominance.py \
  --layout-summary "${OUTPUT_ROOT}/combined/gls_map_layout_summary.csv" \
  --paired-tests "${OUTPUT_ROOT}/combined/gls_map_paired_delta_tests.csv" \
  --output-dir "${OUTPUT_ROOT}/combined"

run_or_print "${PYTHON_BIN}" scripts/generate_trace_biopt_claim_contract.py \
  --dominance "${OUTPUT_ROOT}/combined/trace_biopt_best_baseline_delta.csv" \
  --paired-tests "${OUTPUT_ROOT}/combined/gls_map_paired_delta_tests.csv" \
  --layout-summary "${OUTPUT_ROOT}/combined/gls_map_layout_summary.csv" \
  --output-dir "${OUTPUT_ROOT}/combined"
