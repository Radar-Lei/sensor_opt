#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT"

STAGE16_ROOTS=(
  "TRC-23-02333/trace_sl_results/stage16_calibrated_trace_sweep/pems7_1026_10_20_posterior_iter20"
  "TRC-23-02333/trace_sl_results/stage16_calibrated_trace_sweep/pems7_228_20_30_fullsearch"
  "TRC-23-02333/trace_sl_results/stage16_calibrated_trace_sweep/seattle_10_20_30_trainval"
  "TRC-23-02333/trace_sl_results/stage16_calibrated_trace_probe/pems1026_30_trainval_lowcert"
  "TRC-23-02333/trace_sl_results/stage15_biopt_pems228_10_risksource_probe/train_val_lowcert_delta1_fullsearch"
)

python scripts/summarize_stage16_calibrated_progress.py \
  --stage16-root "${STAGE16_ROOTS[0]}" \
  --stage16-root "${STAGE16_ROOTS[1]}" \
  --stage16-root "${STAGE16_ROOTS[2]}" \
  --stage16-root "${STAGE16_ROOTS[3]}" \
  --stage16-root "${STAGE16_ROOTS[4]}" \
  --output-dir TRC-23-02333/trace_sl_results/stage16_calibrated_trace_sweep/combined_progress

python scripts/generate_stage16_replacement_claim_artifacts.py \
  --stage16-root "${STAGE16_ROOTS[0]}" \
  --stage16-root "${STAGE16_ROOTS[1]}" \
  --stage16-root "${STAGE16_ROOTS[2]}" \
  --stage16-root "${STAGE16_ROOTS[3]}" \
  --stage16-root "${STAGE16_ROOTS[4]}" \
  --output-dir TRC-23-02333/trace_sl_results/stage16_calibrated_trace_sweep/replacement_status

python scripts/generate_current_best_trace_biopt_evidence.py \
  --output-dir TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence

python scripts/generate_current_best_trace_biopt_provenance_table.py
python scripts/generate_trace_biopt_contribution_stack_table.py
python scripts/generate_trace_biopt_reader_guide_table.py
python scripts/generate_trace_biopt_novelty_identity_table.py
python scripts/generate_trace_biopt_comparison_class_table.py
python scripts/generate_trace_biopt_problem_contract_table.py
python scripts/generate_trace_biopt_method_contract_table.py
python scripts/generate_trace_biopt_theory_bridge_table.py
python scripts/generate_trace_biopt_generalization_burden_table.py
python scripts/generate_trace_biopt_map_stability_table.py
python scripts/generate_trace_biopt_baseline_family_screen_table.py
python scripts/generate_trace_biopt_full_baseline_matrix_table.py
python scripts/generate_trace_biopt_full_baseline_heatmap_figure.py
python scripts/generate_trace_biopt_performance_curves.py
python scripts/generate_trace_biopt_paired_margin_figure.py
python scripts/generate_trace_biopt_significance_posture_table.py
python scripts/generate_trace_biopt_challenger_posture_table.py
python scripts/generate_trace_biopt_comparison_ladder_table.py
python scripts/generate_trace_biopt_calibration_alignment_figure.py
python scripts/generate_trace_biopt_sensor_map_figure.py
python scripts/generate_trace_biopt_spatial_posture_table.py
python scripts/generate_trace_biopt_route_ablation_table.py
python scripts/generate_trace_biopt_layout_consensus_table.py
python scripts/generate_trace_biopt_layout_fingerprint_figure.py
python scripts/generate_trace_biopt_hidden_error_heatmap_figure.py
python scripts/generate_trace_biopt_regime_lessons_table.py
python scripts/generate_trace_biopt_mechanism_table.py
python scripts/generate_trace_biopt_optimization_diagnostics.py
python scripts/generate_trace_biopt_solver_scale_table.py
python scripts/generate_trace_biopt_initializer_posture_table.py
python scripts/generate_trace_biopt_compute_posture_table.py
python scripts/generate_trace_biopt_exchange_certificate_table.py
python scripts/generate_trace_biopt_objective_descent_figure.py
python scripts/generate_trace_biopt_exchange_gap_figure.py
python scripts/generate_trace_biopt_certificate_removal_probe_table.py
python scripts/generate_trace_biopt_objective_mix_figure.py
python scripts/generate_trace_biopt_posterior_risk_posture_table.py
python scripts/generate_trace_biopt_weight_sensitivity_table.py
python scripts/generate_trace_biopt_tail_risk_posture_table.py
python scripts/generate_trace_biopt_robustness_frontier_table.py
python scripts/generate_trace_biopt_deployment_stress_posture_table.py
python scripts/generate_trace_biopt_design_protocol_table.py
python scripts/generate_trace_biopt_budget_phasing_table.py
python scripts/generate_trace_biopt_discussion_boundary_table.py
python scripts/generate_trace_biopt_exact_subnetwork_table.py
python scripts/generate_trace_biopt_planning_takeaway_table.py
python scripts/generate_trace_biopt_claim_boundary_matrix_table.py
python scripts/generate_paper_audit_artifacts.py

(
  cd paper
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
)

bash /home/samuel/aris_repo/tools/verify_paper_audits.sh paper/ --assurance submission
