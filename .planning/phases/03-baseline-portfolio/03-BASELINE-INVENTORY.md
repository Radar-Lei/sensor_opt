# Phase 3 Baseline Portfolio Inventory

**Status:** Phase 3 wiring complete; held-out full evidence deferred to Phase 4  
**Date:** 2026-05-22

## Phase Boundary

This inventory maps each Phase 3 baseline requirement to a reviewer objection, an implementation hook, a stable evaluator `layout_type` or artifact name, and the evidence action required before paper claims are made. Phase 3 adds portfolio surface area and machine-auditable wiring; Phase 4 owns full split regeneration, statistical comparisons, and final held-out evidence curation.

Validation MAE remains selection evidence only. Implemented layout rows are compared through the existing held-out hidden-node reconstruction loop, especially `method == gls_map`, before any manuscript performance claim is made.

## Baseline Coverage Matrix

| Requirement | Reviewer objection answered | Portfolio status | Implementation hook | Evaluator layout_type / artifact | Held-out evidence status | Deferral reason / Phase 4 action |
|---|---|---|---|---|---|---|
| BASE-01 | TRACE-SL ignores classical TSLP/full-observability or counting-point placement logic. | implemented; requires Phase 4 full evidence | `observability_proxy_layout(distance, sensor_count)` in `TRC-23-02333/transparent_estimator_eval.py`, enabled by `--include-observability-proxy` or `--include-baseline-portfolio` | `observability_proxy`; Stage 12 launcher artifact `pems7_228_stage12_baseline_portfolio` | Wired for held-out hidden-node reconstruction metrics; no Phase 3 raw-data run is claimed as evidence. | The proxy optimizes observability/coverage-style graph structure, not reconstruction error directly. Phase 4 must run and report held-out `gls_map` deltas against TRACE-SL methods with this objective mismatch stated. |
| BASE-02 | A-optimal and D-optimal design are hidden inside candidate generation rather than reported as independent baselines. | implemented; requires Phase 4 full evidence | Existing `greedy_posterior_layout(base_matrix, sensor_count, obs_weight, objective)` exposed under portfolio path by `--include-greedy` and `--include-baseline-portfolio` | `greedy_a_trace`, `greedy_d_logdet`; summarized by `gls_map_layout_summary.csv` and paired deltas | Independent rows enter `layouts` before `evaluate_layout(test, ...)`; no Phase 3 raw-data run is claimed as evidence. | Phase 4 must regenerate/audit split outputs so A/D-optimal rows are present in final comparison tables and paired tests. |
| BASE-03 | Graph sampling or GSP-style placement is missing even though graph signal reconstruction is evaluated. | implemented; requires Phase 4 full evidence | `graph_sampling_laplacian_layout(laplacian, distance, sensor_count)` uses Laplacian low-frequency mode leverage and graph centrality, enabled by `--include-graph-sampling-baseline` or portfolio flag | `graph_sampling_laplacian`; existing reconstruction method `gsp` remains a method-level comparator | Layout row is wired for held-out `gls_map` and `gsp` metrics; no Phase 3 raw-data run is claimed as evidence. | Phase 4 must decide whether to report the layout row, the method-level GSP reconstruction row, or both, without double-counting the same reviewer objection. |
| BASE-04 | Sparse QR/SVD/POD sensor placement is absent despite being a common modal-placement baseline. | implemented; requires Phase 4 full evidence | `qr_pod_layout(train, sensor_count)` computes standardized training-traffic POD modes and deterministic QR column pivots; enabled by `--include-qr-pod-baseline` or portfolio flag | `qr_pod_modes` | Uses training data only for placement and is evaluated later through held-out reconstruction metrics; no Phase 3 raw-data run is claimed as evidence. | Phase 4 must include `qr_pod_modes` in Stage 12 or successor full evidence runs and compare it against TRACE-SL portfolio rows. |
| BASE-05 | A black-box learned reconstruction method may outperform transparent reconstruction, so omission could look selective. | deferred with reason | No new dependency or learned predictor is added in Phase 3; inventory records the transparent-method boundary from Phase 1 D-14 and Phase 3 D-13 | `03-BASELINE-INVENTORY.md`; no fake `layout_type` row | Not an implemented Phase 3 metric row. | A learned reconstruction check needs a predeclared training protocol, leakage controls, hyperparameter budget, and paper-positioning rule. Phase 4/Phase 7 must either run a lightweight sanity check under that protocol or state as a scoped limitation; Phase 3 deliberately avoids shifting the contribution toward black-box imputation. |
| BASE-06 | The 10% PeMS7_228 multistart-vs-RCSS issue is ignored after being observed. | implemented/predeclared portfolio member; requires Phase 4 full evidence | Existing multistart trace-swap branch under `--include-swap`; Stage 12 passes `--include-validation-swap` and `--include-baseline-portfolio` | `multistart_swap_by_validation`; paired-delta summaries include it as a baseline | Row is already emitted and now explicitly tracked in the Phase 3 portfolio; no new Phase 3 raw-data run is claimed as evidence. | Phase 4 must report whether `validation_swap_selected`, `rcss_selected`, or the predeclared multistart comparator wins by budget, especially at 10%, without post-hoc best-method wording. |

## Stage 12 Artifact Contract

`scripts/run_stage12_pems7_228.sh` is the reusable baseline portfolio launcher. It defaults to `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio`, uses override-friendly small defaults, exports BLAS thread caps, invokes the existing evaluator with Phase 3 flags, and then runs `TRC-23-02333/summarize_trace_sl_rcss.py` so `gls_map_layout_summary.csv`, paired delta CSVs, and the aggregate `SUMMARY.md` remain the paper-facing artifact surface.

## Guardrails

- Raw traffic datasets under `TRC-23-02333/dataset/` are local inputs, not Phase 3 evidence artifacts; Phase 3 verification deliberately does not open PeMS or Seattle raw data files.
- Every implemented baseline row is a real `layouts` entry evaluated by the existing `evaluate_layout(test, ...)` loop. Fake metric rows or prose-only labels are not allowed.
- Validation MAE is allowed for selection/refinement diagnostics only; final baseline claims require held-out test metrics and paired/statistical audit in Phase 4.
- Learning-style reconstruction is documented as a transparent-method deferral, not omitted silently and not treated as a future enhancement outside the claim-evidence contract.

## Requirement Traceability

| Requirement | Coverage in this artifact |
|---|---|
| BASE-01 | Covered by `observability_proxy_layout`, `observability_proxy`, and objective-mismatch caveat. |
| BASE-02 | Covered by independent `greedy_a_trace` and `greedy_d_logdet` rows. |
| BASE-03 | Covered by `graph_sampling_laplacian` plus existing method-level `gsp` awareness. |
| BASE-04 | Covered by training-data-only `qr_pod_modes`. |
| BASE-05 | Covered by documented learning-style deferral with concrete Phase 4/Phase 7 action. |
| BASE-06 | Covered by `multistart_swap_by_validation` as a named comparator/predeclared portfolio member. |
