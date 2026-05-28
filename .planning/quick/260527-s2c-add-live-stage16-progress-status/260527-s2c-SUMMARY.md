# Quick Task 260527-s2c Summary

## Outcome

Extended `scripts/summarize_stage16_calibrated_progress.py` so the Stage16
progress bundle now includes `stage16_live_progress.csv` and a `Live
In-Progress Seeds` section in `STAGE16_PROGRESS.md`. The aggregator now reads
`progress/seed_*_checkpoint.json` plus the matching progress log, skips seeds
that already emitted `metrics.csv`, and reports the live seed's dataset,
budget, current solver stage, iteration, objective, reconstruction Huber term,
selected sensor count, memory usage, and update age with a stale flag.

At refresh time this now surfaces the real in-flight lane directly in the
generated progress page: `PeMS7_228 20/30` is currently on `seed_28`, budget
`0.3`, stage `trace_biopt_exchange_step`, iteration `9`, objective `2.817759`,
and the latest checkpoint is fresh.

## Verification

- `python -m py_compile scripts/summarize_stage16_calibrated_progress.py`
- `python scripts/summarize_stage16_calibrated_progress.py --stage16-root TRC-23-02333/trace_sl_results/stage16_calibrated_trace_sweep/pems7_1026_10_20_posterior_iter20 --stage16-root TRC-23-02333/trace_sl_results/stage16_calibrated_trace_sweep/pems7_228_20_30_fullsearch --stage16-root TRC-23-02333/trace_sl_results/stage16_calibrated_trace_probe/pems1026_30_trainval_lowcert --stage16-root TRC-23-02333/trace_sl_results/stage15_biopt_pems228_10_risksource_probe/train_val_lowcert_delta1_fullsearch --output-dir TRC-23-02333/trace_sl_results/stage16_calibrated_trace_sweep/combined_progress`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The progress bundle now exposes the active rerun without any manual `cat`/`tail`
inspection, and the refreshed current-best paper chain remained fully green with
claim/proof/citation/kill audits all `PASS`, `latexmk` success, and submission
verifier `OK / PASS / stale=false`.
