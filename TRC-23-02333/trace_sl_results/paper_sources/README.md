# TRACE-SL paper source tables

This directory contains deterministic manuscript-facing CSV, JSON, and Markdown sources generated from committed aggregate result artifacts under `TRC-23-02333/trace_sl_results/`. They are inputs for later manuscript table/figure rendering, not manually copied paper values.

Regenerate paper-source tables from the repository root with:

```bash
python scripts/generate_trace_sl_paper_sources.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources
python scripts/generate_trace_sl_claim_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources
```

## Generated files

- `core_performance_table.csv` / `core_performance_table.md`: Stage 12 GLS/MAP core method and comparator performance by budget.
- `paired_delta_table.csv`: Stage 12 paired deltas/tests for `validation_swap_selected` against available baselines.
- `robustness_condition_table.csv`: Stage 14 condition-preserving robustness performance rows.
- `candidate_runtime_table.csv`: Stage 14 candidate-count runtime and candidate diagnostic sensitivity rows.
- `certificate_correlation_table.csv`: Stage 12/13 empirical certificate-error correlation summaries.
- `claim_contract.csv` / `claim_contract.json` / `claim_contract.md`: Phase 7 claim wording, evidence routing, and caveat policy.
- `main_table_contract.csv` / `main_table_contract.md`: Phase 7 Stage12 PeMS7_228 main-table contract with `paired_evidence_status`; descriptive-only rows keep layout-summary provenance and are not paired-test evidence.

Every generated row includes `source_stage`, `source_dir`, and `source_csv` provenance columns. The generators verify that source CSVs and nonempty evidence artifacts are tracked by git and read only committed aggregate CSVs, not raw traffic datasets.
