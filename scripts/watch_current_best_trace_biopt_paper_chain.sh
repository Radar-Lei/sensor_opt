#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT"

INTERVAL=180
ONCE=0
EXPECTED=50

while [[ $# -gt 0 ]]; do
  case "$1" in
    --interval)
      INTERVAL="$2"
      shift 2
      ;;
    --expected)
      EXPECTED="$2"
      shift 2
      ;;
    --once)
      ONCE=1
      shift
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

count_metrics() {
  find TRC-23-02333/trace_sl_results \
    \( -path '*/stage16_calibrated_trace_sweep/pems7_1026_10_20_posterior_iter20/seed_*/metrics.csv' -o \
       -path '*/stage16_calibrated_trace_sweep/pems7_228_20_30_fullsearch/seed_*/metrics.csv' -o \
       -path '*/stage16_calibrated_trace_sweep/seattle_10_20_30_trainval/seed_*/metrics.csv' -o \
       -path '*/stage16_calibrated_trace_probe/pems1026_30_trainval_lowcert/seed_*/metrics.csv' -o \
       -path '*/stage15_biopt_pems228_10_risksource_probe/train_val_lowcert_delta1_fullsearch/seed_*/metrics.csv' \) \
    -print | wc -l
}

last_count=-1

refresh_chain() {
  printf '[%s] refreshing current-best paper chain\n' "$(date -Is)"
  bash scripts/refresh_current_best_trace_biopt_paper_chain.sh
}

while true; do
  current_count=$(count_metrics)
  if [[ "$current_count" != "$last_count" ]]; then
    refresh_chain
    last_count="$current_count"
  fi

  if [[ "$ONCE" -eq 1 ]]; then
    exit 0
  fi

  if [[ "$current_count" -ge "$EXPECTED" ]]; then
    printf '[%s] watcher complete: metrics=%s expected=%s\n' "$(date -Is)" "$current_count" "$EXPECTED"
    exit 0
  fi

  sleep "$INTERVAL"
done
