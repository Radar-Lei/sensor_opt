# Phase 04 Dataset Claim Status

**Scope:** PeMS7_1026 and Seattle evidence status for EXP-02/EXP-03. This artifact cites curated `trace_sl_results/` outputs and reproducible launcher scripts only; raw dataset paths and file contents remain out of scope.

## PeMS7_1026

| Item | Status |
|---|---|
| Claim status | lower-power external evidence |
| Current curated result bundle | `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/` |
| Current split count | 5 held-out GLS/MAP split seeds: 25, 26, 27, 28, 29 |
| Budget coverage | 0.10, 0.20, 0.30 |
| Available aggregate artifacts | `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_delta_summary.csv`, `gls_map_paired_delta_tests.csv`, `gls_map_ablation_summary.csv`, `gls_map_win_counts.csv`, `combined_rcss_candidates.csv`, `rcss_selected_sources.csv`, `certificate_correlation_summary.csv`, `SUMMARY.md` |
| Stage 12 extension launcher | `scripts/run_stage12_pems7_1026.sh` |
| Stage 12 default output | `TRC-23-02333/trace_sl_results/pems7_1026_stage12_lower_power_external/` |

PeMS7_1026 satisfies D-06 as lower-power external evidence, not as a ten-split core-equivalent bundle. The committed Stage 11 artifact has five held-out GLS/MAP splits, which supports external validation directionally but should be reported with uncertainty/effect-size language and should not be used to claim the same evidentiary power as the PeMS7_228 ten-split core bundle.

The Stage 12 launcher keeps a five-seed default because the current audit did not establish that a ten-split PeMS7_1026 extension is safe or already synchronized locally. To extend it explicitly, run from the repository root with an override such as:

```bash
DRY_RUN=1 SEEDS="25 26 27 28 29 30 31 32 33 34" OUTPUT_DIR="TRC-23-02333/trace_sl_results/pems7_1026_stage12_10split_external" scripts/run_stage12_pems7_1026.sh
SEEDS="25 26 27 28 29 30 31 32 33 34" OUTPUT_DIR="TRC-23-02333/trace_sl_results/pems7_1026_stage12_10split_external" scripts/run_stage12_pems7_1026.sh
```

Paper-facing implication: describe PeMS7_1026 as lower-power external validation unless that ten-split extension is generated, aggregated, reviewed, and committed.

## Seattle

| Synchronization check | Status | Evidence |
|---|---|---|
| Reproducible script exists | synchronized | `scripts/run_stage11_seattle.sh`; `scripts/run_stage12_seattle.sh` |
| Curated result directory exists | synchronized | `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/` |
| Aggregate summary exists | synchronized | `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/SUMMARY.md` |
| Stage inventory guidance | synchronized as supporting/conditional | `TRC-23-02333/trace_sl_results/README.md` now lists Seattle as supporting/conditional rather than core |
| Current split count | synchronized lower-power bundle | 5 held-out GLS/MAP split seeds: 25, 26, 27, 28, 29 |
| Budget coverage | synchronized | 0.10, 0.20, 0.30 |

Seattle satisfies D-07 as **supporting/conditional** evidence. Scripts, result directory, README guidance, and generated summaries are now synchronized, but the current committed evidence is a light five-split bundle rather than a primary core-evidence package. It may support generality discussion or appendix-level evidence, but it should not be elevated to the core claim set unless a stronger synchronized Stage 12 bundle is generated and reviewed.

The synchronized extension command is:

```bash
DRY_RUN=1 scripts/run_stage12_seattle.sh
scripts/run_stage12_seattle.sh
```

Paper-facing implication: include Seattle only as supporting/conditional evidence, or remove it from the core claim set if manuscript space requires a stricter evidence boundary. Core performance claims should continue to rely on PeMS7_228 ten-split evidence, with PeMS7_1026 framed as lower-power external evidence.
