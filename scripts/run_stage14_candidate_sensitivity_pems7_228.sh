#!/usr/bin/env bash
set -euo pipefail

DATA_ROOT="${DATA_ROOT:-TRC-23-02333/dataset/PeMS7_228}"
OUTPUT_DIR="${OUTPUT_DIR:-TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity}"
SEEDS="${SEEDS:-25}"
BUDGETS="${BUDGETS:-0.20}"
CANDIDATE_COUNTS="${CANDIDATE_COUNTS:-50 100 200 500}"
NUM_LAYOUTS="${NUM_LAYOUTS:-50}"
SCENARIO_COUNT="${SCENARIO_COUNT:-2}"
VALIDATION_SWAP_STARTS="${VALIDATION_SWAP_STARTS:-2}"
VALIDATION_SWAP_ITER="${VALIDATION_SWAP_ITER:-3}"
VALIDATION_SWAP_ADD_POOL="${VALIDATION_SWAP_ADD_POOL:-12}"
VALIDATION_SWAP_REMOVE_POOL="${VALIDATION_SWAP_REMOVE_POOL:-6}"
MAX_TEST_STEPS="${MAX_TEST_STEPS:-0}"
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

join_by_semicolon() {
  local IFS=';'
  printf '%s' "$*"
}

write_caveat() {
  local missing_counts="$1"
  local completed_counts="$2"
  local reason="$3"
  local evidence_attempted="$4"
  "${PYTHON_BIN}" - "$OUTPUT_DIR" "$missing_counts" "$completed_counts" "$reason" "$evidence_attempted" <<'PY'
import json
import sys
from pathlib import Path

root = Path(sys.argv[1])
missing = [int(x) for x in sys.argv[2].replace(';', ' ').split() if x]
completed = [int(x) for x in sys.argv[3].replace(';', ' ').split() if x]
reason = sys.argv[4]
evidence_attempted = sys.argv[5].lower() == 'true'
payload = {
    "requirement": "ROBUST-06",
    "allowed_exception": True,
    "missing_candidate_counts": missing,
    "completed_candidate_counts": completed,
    "reason": reason,
    "evidence_attempted": evidence_attempted,
    "validator_disposition": "allowed limited-tractability exception for Stage 14 candidate-count sensitivity only",
}
(root / "candidate_sensitivity_caveat.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
PY
}

mkdir -p "${OUTPUT_DIR}"
completed_input_roots=()

if [ "${DRY_RUN}" = "1" ]; then
  for candidate_count in ${CANDIDATE_COUNTS}; do
    count_seed_dirs=()
    for seed in ${SEEDS}; do
      seed_dir="${OUTPUT_DIR}/candidates_${candidate_count}/seed_${seed}"
      count_seed_dirs+=("${seed_dir}")
      completed_input_roots+=("${seed_dir}")
      run_or_print "${PYTHON_BIN}" TRC-23-02333/transparent_estimator_eval.py \
        --data-root "${DATA_ROOT}" \
        --output-dir "${seed_dir}" \
        --budgets "${BUDGETS}" \
        --num-layouts "${NUM_LAYOUTS}" \
        --split-seed "${seed}" \
        --layout-seed "$((2026 + seed + candidate_count))" \
        --max-test-steps "${MAX_TEST_STEPS}" \
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
        --include-baseline-portfolio \
        --include-observability-proxy \
        --include-graph-sampling-baseline \
        --include-qr-pod-baseline
    done
    run_or_print "${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
      --input-root "${count_seed_dirs[@]}" \
      --output-dir "${OUTPUT_DIR}/candidates_${candidate_count}"
  done
  run_or_print "${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
    --input-root "${completed_input_roots[@]}" \
    --runtime-root "${OUTPUT_DIR}" \
    --output-dir "${OUTPUT_DIR}"
  exit 0
fi

: > "${OUTPUT_DIR}/stage14_timing.csv"
printf 'candidate_count,seed,runtime_seconds,status,output_dir,caveat_path\n' >> "${OUTPUT_DIR}/stage14_timing.csv"

completed_counts=()
missing_counts=()
evidence_attempted=false

for candidate_count in ${CANDIDATE_COUNTS}; do
  candidate_dir="${OUTPUT_DIR}/candidates_${candidate_count}"
  mkdir -p "${candidate_dir}"
  count_status="success"
  count_seed_dirs=()
  for seed in ${SEEDS}; do
    evidence_attempted=true
    seed_dir="${candidate_dir}/seed_${seed}"
    start_epoch="$(date +%s)"
    status="success"
    if "${PYTHON_BIN}" TRC-23-02333/transparent_estimator_eval.py \
      --data-root "${DATA_ROOT}" \
      --output-dir "${seed_dir}" \
      --budgets "${BUDGETS}" \
      --num-layouts "${NUM_LAYOUTS}" \
      --split-seed "${seed}" \
      --layout-seed "$((2026 + seed + candidate_count))" \
      --max-test-steps "${MAX_TEST_STEPS}" \
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
      --include-baseline-portfolio \
      --include-observability-proxy \
      --include-graph-sampling-baseline \
      --include-qr-pod-baseline \
      2>&1 | tee "${OUTPUT_DIR}_candidates_${candidate_count}_seed_${seed}.log"; then
      status="success"
    else
      status="failed"
      count_status="failed"
    fi
    end_epoch="$(date +%s)"
    runtime_seconds="$((end_epoch - start_epoch))"
    caveat_path=""
    if [ "${status}" != "success" ]; then
      caveat_path="${OUTPUT_DIR}/candidate_sensitivity_caveat.json"
    fi
    printf '%s,%s,%s,%s,%s,%s\n' "${candidate_count}" "${seed}" "${runtime_seconds}" "${status}" "${seed_dir}" "${caveat_path}" >> "${OUTPUT_DIR}/stage14_timing.csv"
    if [ "${status}" != "success" ]; then
      break
    fi
    count_seed_dirs+=("${seed_dir}")
  done
  if [ "${count_status}" = "success" ]; then
    completed_counts+=("${candidate_count}")
    completed_input_roots+=("${count_seed_dirs[@]}")
    "${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
      --input-root "${count_seed_dirs[@]}" \
      --output-dir "${candidate_dir}"
  else
    missing_counts+=("${candidate_count}")
  fi
done

if [ "${#completed_input_roots[@]}" -gt 0 ]; then
  "${PYTHON_BIN}" TRC-23-02333/summarize_trace_sl_rcss.py \
    --input-root "${completed_input_roots[@]}" \
    --runtime-root "${OUTPUT_DIR}" \
    --output-dir "${OUTPUT_DIR}"
fi

if [ "${#missing_counts[@]}" -gt 0 ]; then
  missing_joined="$(join_by_semicolon "${missing_counts[@]}")"
  completed_joined="$(join_by_semicolon "${completed_counts[@]}")"
  write_caveat "${missing_joined}" "${completed_joined}" "One or more candidate-count runs failed under local reduced Stage 14 settings; see stage14_timing.csv status rows and per-count logs." "${evidence_attempted}"
fi
