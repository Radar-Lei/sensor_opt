# TRACE-SL paper source tables

This directory contains deterministic manuscript-facing CSV and Markdown sources generated from committed aggregate result artifacts under `TRC-23-02333/trace_sl_results/`. They are inputs for later manuscript table/figure rendering, not manually copied paper values.

Regenerate from the repository root with:

```bash
python scripts/generate_trace_sl_paper_sources.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources
```

## Generated files

- `core_performance_table.csv` / `core_performance_table.md`: Stage 12 GLS/MAP core method and comparator performance by budget.
- `paired_delta_table.csv`: Stage 12 paired deltas/tests for `validation_swap_selected` against available baselines.
- `robustness_condition_table.csv`: Stage 14 condition-preserving robustness performance rows.
- `candidate_runtime_table.csv`: Stage 14 candidate-count runtime and candidate diagnostic sensitivity rows.
- `certificate_correlation_table.csv`: Stage 12/13 empirical certificate-error correlation summaries.

Every generated row includes `source_stage`, `source_dir`, and `source_csv` provenance columns. The generator verifies that source CSVs are tracked by git and reads only committed aggregate CSVs, not raw traffic datasets.
