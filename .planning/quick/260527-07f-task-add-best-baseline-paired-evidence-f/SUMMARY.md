# Quick Summary: TRACE-BiOpt Best-Baseline Paired Evidence

## Completed

- Updated `TRC-23-02333/summarize_trace_sl_rcss.py` so paired comparisons are
  generated against all non-BiOpt layouts rather than a fixed subset.
- Updated `scripts/generate_trace_biopt_dominance.py` so each dominance row
  carries paired statistics for its actual best non-BiOpt baseline.
- Re-ran `stage15_biopt_allbudget_3seed_v2` with seeds 25, 26, and 27 across
  PeMS7_1026, Seattle, and PeMS7_228 at 10, 20, and 30 percent budgets.
- TRACE-BiOpt beats the best non-BiOpt baseline on all nine dataset-budget
  rows in
  `TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_3seed_v2/combined/TRACE_BIOPT_DOMINANCE.md`.

## Evidence Notes

- Paired counts are 3 per row.
- Paired win counts are 3/3 on six rows.
- Paired win counts are 2/3 on PeMS7_1026 30 percent, PeMS7_228 10 percent,
  and Seattle 10 percent.
- Three seeds are enough to confirm the all-budget dominance direction under
  the current launcher, but not enough for final submission-level significance
  wording.

## Verification

- `python -m py_compile TRC-23-02333/summarize_trace_sl_rcss.py scripts/generate_trace_biopt_dominance.py`
- `pytest -q TRC-23-02333/test_summarize_trace_sl_rcss.py scripts/test_generate_trace_biopt_dominance.py`
- `OUTPUT_ROOT=TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_3seed_v2 SEEDS="25 26 27" BUDGETS="0.10 0.20 0.30" scripts/run_stage15_biopt_weak_points.sh`

## Remaining

- Add more seeds and generate a claim contract before using final TR-B
  dominance wording.
