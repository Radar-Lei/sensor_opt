#!/usr/bin/env bash
set -euo pipefail

OUTPUT_ROOT="${OUTPUT_ROOT:-TRC-23-02333/trace_sl_results/stage17_seattle_trainval_zero_weight_probe}"
SEEDS="${SEEDS:-25}"
BUDGETS="${BUDGETS:-0.20 0.30}"
LAYOUT_SEED_OFFSET="${LAYOUT_SEED_OFFSET:-9051}"
TRACE_BIOPT_BETA="${TRACE_BIOPT_BETA:-0.0}"
TRACE_BIOPT_GAMMA="${TRACE_BIOPT_GAMMA:-0.0}"
TRACE_BIOPT_ETA="${TRACE_BIOPT_ETA:-0.0}"
TRACE_BIOPT_HUBER_DELTA="${TRACE_BIOPT_HUBER_DELTA:-5.0}"
TRACE_BIOPT_EXCHANGE_ITER="${TRACE_BIOPT_EXCHANGE_ITER:-8}"
TRACE_BIOPT_FORWARD_POOL="${TRACE_BIOPT_FORWARD_POOL:-64}"
TRACE_BIOPT_EXCHANGE_ADD_POOL="${TRACE_BIOPT_EXCHANGE_ADD_POOL:-64}"
TRACE_BIOPT_EXCHANGE_REMOVE_POOL="${TRACE_BIOPT_EXCHANGE_REMOVE_POOL:-20}"
TRACE_BIOPT_OBJECTIVE_STEPS="${TRACE_BIOPT_OBJECTIVE_STEPS:-96}"
TRACE_BIOPT_INITIALIZER="${TRACE_BIOPT_INITIALIZER:-auto}"
TRACE_BIOPT_AUTO_WARM_START_THRESHOLD="${TRACE_BIOPT_AUTO_WARM_START_THRESHOLD:-500}"
TRACE_BIOPT_RELAX_ITER="${TRACE_BIOPT_RELAX_ITER:-6}"
TRACE_BIOPT_RELAX_STEP="${TRACE_BIOPT_RELAX_STEP:-0.2}"
TRACE_BIOPT_RELAX_FD_EPS="${TRACE_BIOPT_RELAX_FD_EPS:-0.001}"
TRACE_BIOPT_RELAX_POOL="${TRACE_BIOPT_RELAX_POOL:-40}"
SCENARIO_COUNT="${SCENARIO_COUNT:-8}"
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

mkdir -p "${OUTPUT_ROOT}/progress"

for seed in ${SEEDS}; do
  metrics_path="${OUTPUT_ROOT}/seed_${seed}/metrics.csv"
  if [ -f "${metrics_path}" ]; then
    printf '[%s] skip completed Seattle Stage17 seed %s (%s)\n' "$(date -Is)" "${seed}" "${metrics_path}"
    continue
  fi
  run_or_print "${PYTHON_BIN}" TRC-23-02333/transparent_estimator_eval.py \
    --data-root "TRC-23-02333/dataset/Seattle" \
    --output-dir "${OUTPUT_ROOT}/seed_${seed}" \
    --budgets "${BUDGETS}" \
    --num-layouts 1 \
    --split-seed "${seed}" \
    --layout-seed "$((LAYOUT_SEED_OFFSET + seed))" \
    --include-biopt \
    --trace-biopt-beta "${TRACE_BIOPT_BETA}" \
    --trace-biopt-gamma "${TRACE_BIOPT_GAMMA}" \
    --trace-biopt-eta "${TRACE_BIOPT_ETA}" \
    --trace-biopt-huber-delta "${TRACE_BIOPT_HUBER_DELTA}" \
    --trace-biopt-exchange-iter "${TRACE_BIOPT_EXCHANGE_ITER}" \
    --trace-biopt-forward-pool "${TRACE_BIOPT_FORWARD_POOL}" \
    --trace-biopt-exchange-add-pool "${TRACE_BIOPT_EXCHANGE_ADD_POOL}" \
    --trace-biopt-exchange-remove-pool "${TRACE_BIOPT_EXCHANGE_REMOVE_POOL}" \
    --trace-biopt-objective-steps "${TRACE_BIOPT_OBJECTIVE_STEPS}" \
    --trace-biopt-risk-source "train_val" \
    --trace-biopt-initializer "${TRACE_BIOPT_INITIALIZER}" \
    --trace-biopt-auto-warm-start-threshold "${TRACE_BIOPT_AUTO_WARM_START_THRESHOLD}" \
    --trace-biopt-relax-iter "${TRACE_BIOPT_RELAX_ITER}" \
    --trace-biopt-relax-step "${TRACE_BIOPT_RELAX_STEP}" \
    --trace-biopt-relax-fd-eps "${TRACE_BIOPT_RELAX_FD_EPS}" \
    --trace-biopt-relax-pool "${TRACE_BIOPT_RELAX_POOL}" \
    --scenario-count "${SCENARIO_COUNT}" \
    --max-rss-mb "${MAX_RSS_MB}" \
    --progress-log "${OUTPUT_ROOT}/progress/seed_${seed}_progress.jsonl" \
    --checkpoint-json "${OUTPUT_ROOT}/progress/seed_${seed}_checkpoint.json"
done
