# Phase 5 Robustness Evidence Audit

**Scope:** Phase 5 verifies curated Stage 14 PeMS7_228 stress-test artifacts for robustness/generalization claims. PeMS7_228 Stage 14 is the core Phase 5 robustness bundle per D-14; external-dataset robustness remains supporting/optional per D-15. These artifacts support usefulness under tested perturbations and candidate-pool settings, not broad deployment guarantees.

## Validator Status Source

Run from the repository root:

```bash
python .planning/phases/05-robustness-and-generality/validate_phase5_robustness.py
```

Expected status on the committed Stage 14 bundle:

| Requirement | Validator status | Evidence interpretation |
|---|---|---|
| ROBUST-01 | PASS | Sensor-failure rows are present for failure_0.05, failure_0.10, and failure_0.20 with held-out `method == gls_map` evidence. |
| ROBUST-02 | PASS | Observation-noise rows include nonzero `noise_scale` and held-out GLS/MAP evidence. |
| ROBUST-03 | PASS | Random missingness and block missingness rows include `missing_rate` and `missing_block_steps` evidence. |
| ROBUST-04 | PASS | Cost evidence is a deterministic proxy with `cost_budget`, `layout_sensor_cost`, and `cost_feasible`; it is not a full cost-aware deployment model. |
| ROBUST-05 | PASS | Temporal-shift evidence includes `split_mode=chronological` rows. |
| ROBUST-06 | PASS | Candidate-count performance/runtime artifacts cover candidate_count 50, 100, 200, and 500. |

## Requirement-to-Artifact Map

| Requirement | Artifact paths | Required condition columns / values | Validator status | Caveats | Claim implication |
|---|---|---|---|---|---|
| ROBUST-01 | `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/combined_metrics.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_layout_summary.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_paired_delta_tests.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/SUMMARY.md` | `method`, `robustness_family`, `robustness_condition`, `failure_rate`, `active_sensor_count`, `dropped_sensor_count`; required conditions `failure_0.05`, `failure_0.10`, `failure_0.20` | PASS | Perturbation is post-selection held-out sensor failure on the Stage 14 PeMS7_228 bundle. | Supports claims that TRACE-SL was stress-tested under tested sensor-failure rates. |
| ROBUST-02 | `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/combined_metrics.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_layout_summary.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_paired_delta_tests.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/SUMMARY.md` | `method`, `robustness_family`, `robustness_condition`, `noise_scale`; at least one nonzero `noise_scale` condition such as `noise_0.05` | PASS | Noise evidence is bounded to evaluated noise scales and deterministic seeds. | Supports claims about evaluated observation-noise robustness only. |
| ROBUST-03 | `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/combined_metrics.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_layout_summary.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_paired_delta_tests.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/SUMMARY.md` | `method`, `robustness_family`, `robustness_condition`, `missing_rate`, `missing_block_steps`; random missingness and block missingness conditions | PASS | Missingness evidence covers the committed random/block settings, not every outage process. | Supports tested missing-reading and contiguous-block stress-test language. |
| ROBUST-04 | `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/combined_metrics.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_layout_summary.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_paired_delta_tests.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/SUMMARY.md` | `method`, `robustness_family`, `robustness_condition`, `cost_proxy`, `cost_budget`, `layout_sensor_cost`, `cost_feasible` | PASS | Cost evidence is a deterministic proxy with limitations per D-08; it should be reported as a proxy stress test, not full heterogeneous procurement optimization. | Supports bounded language that TRACE-SL was evaluated under a nonuniform-cost proxy. |
| ROBUST-05 | `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/combined_metrics.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_layout_summary.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_paired_delta_tests.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/SUMMARY.md` | `method`, `robustness_family`, `robustness_condition`, `split_mode`; required `split_mode=chronological` rows | PASS | Temporal-shift evidence uses the committed chronological split setting where timestamps support it. | Supports tested chronological-split generalization language. |
| ROBUST-06 | `TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/combined_metrics.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/candidate_sensitivity_summary.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/runtime_candidate_sensitivity.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/stage14_timing.csv`; `TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/SUMMARY.md`; optional `TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/candidate_sensitivity_caveat.json` | `candidate_count` must cover 50, 100, 200, and 500 in performance and runtime artifacts; runtime files require nonnegative `runtime_seconds` and success/completed status when status is present | PASS | ROBUST-06 caveats are accepted only through validator-recognized `candidate_sensitivity_caveat.json` with `allowed_exception=true`, attempted evidence, completed and missing counts, a nonempty reason, and limited-tractability disposition. No caveat is needed for the current committed bundle because all four counts are present. | Supports candidate-pool sensitivity and practical runtime language for tested candidate-count settings only. |

## Claim Boundaries

- Use `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/` as the core Phase 5 robustness evidence path.
- Use `TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/` as the core Phase 5 candidate-count/runtime sensitivity path.
- Treat external robustness as supporting unless a stronger synchronized external bundle is generated and reviewed.
- State that cost evidence uses a deterministic proxy with limitations; do not describe it as full cost-aware optimization.
- State that ROBUST-06 limitations are acceptable only when `candidate_sensitivity_caveat.json` is accepted by `validate_phase5_robustness.py`.
- Do not cite ignored local raw data as evidence. The evidence source is the curated Stage 14 artifact tree under `TRC-23-02333/trace_sl_results/`.
- Avoid wording that suggests complete deployment-level robustness across all networks, all sensor faults, all outage processes, all noise models, or all candidate-pool sizes.
