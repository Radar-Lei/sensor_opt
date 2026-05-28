#!/usr/bin/env python3
"""Fresh machine audit for TRACE-BiOpt paper-visible claims.

This script intentionally reads only paper source files and raw current-best
or Stage15 CSV/JSON artifacts. It does not read prior audit reports.
"""

from __future__ import annotations

import csv
import json
import math
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
from scipy import stats


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
STAGE15 = ROOT / "TRC-23-02333" / "trace_sl_results" / "stage15_biopt_allbudget_10seed_v2" / "combined"
CURRENT_BEST = ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence"
PAPER_SOURCES = ROOT / "TRC-23-02333" / "trace_sl_results" / "paper_sources"
OUT_DIR = PAPER / ".aris" / "paper-claim-audit"
OUT = OUT_DIR / "fresh_machine_claim_audit.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_table() -> dict[tuple[str, float], dict[str, object]]:
    text = read(PAPER / "tables" / "table_trace_biopt_dominance.tex")
    pattern = re.compile(
        r"^(?P<dataset>PeMS7\\_1026|PeMS7\\_228|Seattle)\s*&\s*"
        r"(?P<budget>\d+)\\%\s*&\s*"
        r"(?P<challenger>[^&]+)\s*&\s*"
        r"(?P<trace>[0-9.]+)\s*&\s*"
        r"(?P<best>[0-9.]+)\s*&\s*"
        r"(?P<delta>-?[0-9.]+)\s*&\s*"
        r"(?P<wins>\d+)/(?P<count>\d+)\s*&\s*"
        r"(?P<p>[0-9.eE+-]+)\s*\\\\",
        re.MULTILINE,
    )
    rows: dict[tuple[str, float], dict[str, object]] = {}
    for match in pattern.finditer(text):
        dataset = match.group("dataset").replace("\\_", "_")
        budget = int(match.group("budget")) / 100.0
        rows[(dataset, budget)] = {
            "challenger": match.group("challenger").strip(),
            "trace": float(match.group("trace")),
            "best": float(match.group("best")),
            "delta": float(match.group("delta")),
            "wins": int(match.group("wins")),
            "count": int(match.group("count")),
            "p": float(match.group("p")),
        }
    return rows


def load_delta_rows() -> dict[tuple[str, float], dict[str, str]]:
    path = CURRENT_BEST / "trace_biopt_best_baseline_delta.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return {(row["dataset"], float(row["budget"])): row for row in rows}


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def status_equal(name: str, got: object, expected: object) -> dict[str, object]:
    ok = got == expected
    def normalize(value: object) -> object:
        if isinstance(value, set):
            return sorted(value)
        return value
    return {
        "claim": name,
        "status": "exact_match" if ok else "mismatch",
        "paper_value": normalize(got),
        "evidence_value": normalize(expected),
    }


def status_round(name: str, got: float, expected: float, fmt: str) -> dict[str, object]:
    rendered = float(format(expected, fmt))
    ok = math.isclose(got, rendered, rel_tol=0.0, abs_tol=10 ** (-max(0, int(fmt[-2]) if fmt.endswith("f") else 12)))
    return {
        "claim": name,
        "status": "rounding_ok" if ok else "number_mismatch",
        "paper_value": got,
        "evidence_value": expected,
        "expected_display": format(expected, fmt),
    }


def status_p(name: str, got: float, expected: float) -> dict[str, object]:
    if expected < 0.001:
        expected_display = f"{expected:.1e}"
        ok = got == float(expected_display)
    else:
        expected_display = f"{expected:.4f}"
        ok = math.isclose(got, float(expected_display), rel_tol=0.0, abs_tol=1e-12)
    return {
        "claim": name,
        "status": "rounding_ok" if ok else "number_mismatch",
        "paper_value": got,
        "evidence_value": expected,
        "expected_display": expected_display,
    }


def main() -> int:
    table = parse_table()
    delta = load_delta_rows()
    contract = json.loads(read(CURRENT_BEST / "trace_biopt_claim_contract.json"))
    main_tex = read(PAPER / "main.tex")
    abstract_tex = read(PAPER / "sections" / "0_abstract.tex")
    intro_tex = read(PAPER / "sections" / "1_introduction.tex")
    exp_tex = read(PAPER / "sections" / "5_experiments.tex")
    mechanism_tex_section = read(PAPER / "sections" / "6_ablation_robustness.tex")
    robustness_section_tex = read(PAPER / "sections" / "7_robustness.tex")
    discussion_tex = read(PAPER / "sections" / "7_discussion.tex")
    appendix_tex = read(PAPER / "sections" / "A_appendix.tex")
    theory_contract_tex = read(ROOT / "TRACE_BIOPT_THEORY.md")
    table_tex = read(PAPER / "tables" / "table_trace_biopt_dominance.tex")
    contribution_stack_tex = read(PAPER / "tables" / "table_trace_biopt_contribution_stack.tex")
    reader_guide_tex = read(PAPER / "tables" / "table_trace_biopt_reader_guide.tex")
    novelty_identity_tex = read(PAPER / "tables" / "table_trace_biopt_novelty_identity.tex")
    comparison_class_contract_tex = read(PAPER / "tables" / "table_trace_biopt_comparison_class_contract.tex")
    problem_contract_tex = read(PAPER / "tables" / "table_trace_biopt_problem_contract.tex")
    method_contract_tex = read(PAPER / "tables" / "table_trace_biopt_method_contract.tex")
    theory_bridge_tex = read(PAPER / "tables" / "table_trace_biopt_theory_bridge.tex")
    generalization_burden_tex = read(PAPER / "tables" / "table_trace_biopt_generalization_burden.tex")
    map_stability_tex = read(PAPER / "tables" / "table_trace_biopt_map_stability_posture.tex")
    baseline_family_screen_tex = read(PAPER / "tables" / "table_trace_biopt_baseline_family_screen.tex")
    spatial_posture_tex = read(PAPER / "tables" / "table_trace_biopt_spatial_posture.tex")
    route_ablation_tex = read(PAPER / "tables" / "table_trace_biopt_route_ablation.tex")
    layout_consensus_tex = read(PAPER / "tables" / "table_trace_biopt_layout_consensus_posture.tex")
    claim_boundary_matrix_tex = read(PAPER / "tables" / "table_trace_biopt_claim_boundary_matrix.tex")
    provenance_tex = read(PAPER / "tables" / "table_trace_biopt_current_best_provenance.tex")
    full_matrix_tex = read(PAPER / "tables" / "table_trace_biopt_full_baseline_matrix.tex")
    significance_posture_tex = read(PAPER / "tables" / "table_trace_biopt_significance_posture.tex")
    challenger_posture_tex = read(PAPER / "tables" / "table_trace_biopt_challenger_posture.tex")
    comparison_ladder_tex = read(PAPER / "tables" / "table_trace_biopt_comparison_ladder.tex")
    regime_lessons_tex = read(PAPER / "tables" / "table_trace_biopt_regime_lessons.tex")
    mechanism_tex = read(PAPER / "tables" / "table_trace_biopt_mechanism.tex")
    registry_tex = read(PAPER / "tables" / "table_trace_biopt_baseline_registry.tex")
    optimization_tex = read(PAPER / "tables" / "table_trace_biopt_optimization.tex")
    solver_scale_tex = read(PAPER / "tables" / "table_trace_biopt_solver_scale.tex")
    initializer_posture_tex = read(PAPER / "tables" / "table_trace_biopt_initializer_posture.tex")
    compute_posture_tex = read(PAPER / "tables" / "table_trace_biopt_compute_posture.tex")
    robustness_tex = read(PAPER / "tables" / "table_robustness_routing.tex")
    robustness_frontier_tex = read(PAPER / "tables" / "table_trace_biopt_robustness_frontier.tex")
    deployment_stress_posture_tex = read(PAPER / "tables" / "table_trace_biopt_deployment_stress_posture.tex")
    design_protocol_tex = read(PAPER / "tables" / "table_trace_biopt_design_protocol.tex")
    budget_phasing_tex = read(PAPER / "tables" / "table_trace_biopt_budget_phasing.tex")
    discussion_boundary_tex = read(PAPER / "tables" / "table_trace_biopt_discussion_boundary.tex")
    exact_subnetwork_tex = read(PAPER / "tables" / "table_trace_biopt_exact_subnetwork.tex")
    planning_takeaways_tex = read(PAPER / "tables" / "table_trace_biopt_planning_takeaways.tex")
    certificate_removal_probe_tex = read(PAPER / "tables" / "table_trace_biopt_certificate_removal_probe.tex")
    posterior_risk_tex = read(PAPER / "tables" / "table_trace_biopt_posterior_risk_posture.tex")
    weight_sensitivity_tex = read(PAPER / "tables" / "table_trace_biopt_weight_sensitivity.tex")
    tail_risk_posture_tex = read(PAPER / "tables" / "table_trace_biopt_tail_risk_posture.tex")
    search_probe_tex = read(PAPER / "tables" / "table_trace_biopt_search_probe.tex")
    calibration_probe_tex = read(PAPER / "tables" / "table_trace_biopt_calibration_probe.tex")
    stage16_probe_tex = read(PAPER / "tables" / "table_trace_biopt_stage16_calibrated_probe.tex")
    mechanism_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_mechanism_diagnostics.csv")
    registry_csv = load_csv_rows(STAGE15 / "trace_biopt_baseline_registry.csv")
    optimization_csv = load_csv_rows(STAGE15 / "trace_biopt_optimization_diagnostics.csv")
    optimization_detail_csv = load_csv_rows(STAGE15 / "trace_biopt_optimization_diagnostics_detail.csv")
    solver_scale_summary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_solver_scale_summary.csv")
    solver_scale_detail_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_solver_scale_detail.csv")
    initializer_posture_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_initializer_posture.csv")
    compute_posture_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_compute_posture.csv")
    compute_posture_detail_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_compute_posture_detail.csv")
    exchange_certificate_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_exchange_certificate_summary.csv")
    objective_descent_summary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_objective_descent_summary.csv")
    objective_descent_curves_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_objective_descent_curves.csv")
    exchange_gap_summary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_exchange_gap_summary.csv")
    exchange_gap_curves_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_exchange_gap_curves.csv")
    certificate_removal_probe_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_certificate_removal_probe.csv")
    objective_mix_summary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_objective_mix_summary.csv")
    posterior_risk_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_posterior_risk_posture.csv")
    weight_sensitivity_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_weight_sensitivity.csv")
    tail_risk_posture_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_tail_risk_posture.csv")
    design_protocol_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_design_protocol.csv")
    budget_phasing_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_budget_phasing.csv")
    discussion_boundary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_discussion_boundary.csv")
    exact_subnetwork_summary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_exact_subnetwork_summary.csv")
    exact_subnetwork_detail_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_exact_subnetwork_detail.csv")
    planning_takeaways_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_planning_takeaways.csv")
    reader_guide_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_reader_guide.csv")
    novelty_identity_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_novelty_identity.csv")
    comparison_class_contract_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_comparison_class_contract.csv")
    problem_contract_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_problem_contract.csv")
    method_contract_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_method_contract.csv")
    theory_bridge_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_theory_bridge.csv")
    robustness_csv = load_csv_rows(PAPER_SOURCES / "robustness_routing_summary.csv")
    robustness_frontier_csv = load_csv_rows(PAPER_SOURCES / "robustness_frontier_summary.csv")
    deployment_stress_posture_csv = load_csv_rows(PAPER_SOURCES / "robustness_stress_posture_summary.csv")
    robustness_source_csv = load_csv_rows(PAPER_SOURCES / "robustness_condition_table.csv")
    search_probe_csv = load_csv_rows(PAPER_SOURCES / "trace_biopt_search_budget_probe.csv")
    calibration_probe_csv = load_csv_rows(PAPER_SOURCES / "trace_biopt_calibration_risk_probe.csv")
    stage16_probe_csv = load_csv_rows(PAPER_SOURCES / "trace_biopt_stage16_calibrated_probe.csv")
    provenance_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_current_best_provenance.csv")
    full_matrix_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_full_baseline_matrix.csv")
    full_baseline_heatmap_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_full_baseline_heatmap.csv")
    generalization_burden_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_generalization_burden.csv")
    map_stability_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_map_stability_posture.csv")
    baseline_family_screen_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_baseline_family_screen.csv")
    claim_boundary_matrix_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_claim_boundary_matrix.csv")
    performance_curves_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_performance_curves.csv")
    paired_margin_points_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_paired_margin_points.csv")
    paired_margin_summary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_paired_margin_summary.csv")
    significance_posture_summary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_significance_posture_summary.csv")
    significance_posture_detail_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_significance_posture_detail.csv")
    challenger_posture_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_challenger_posture.csv")
    comparison_ladder_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_comparison_ladder.csv")
    calibration_alignment_points_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_calibration_alignment_points.csv")
    calibration_alignment_summary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_calibration_alignment_summary.csv")
    sensor_map_summary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_sensor_map_summary.csv")
    spatial_posture_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_spatial_posture.csv")
    route_ablation_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_route_ablation_summary.csv")
    layout_consensus_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_layout_consensus_posture.csv")
    layout_fingerprint_summary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_layout_fingerprint_summary.csv")
    hidden_error_heatmap_grid_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_hidden_error_heatmap_grid.csv")
    hidden_error_heatmap_summary_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_hidden_error_heatmap_summary.csv")
    regime_lessons_csv = load_csv_rows(CURRENT_BEST / "trace_biopt_regime_lessons.csv")
    layout_summary = load_csv_rows(STAGE15 / "gls_map_layout_summary.csv")
    cert_rows = load_csv_rows(STAGE15 / "certificate_correlation_summary.csv")
    paper_text = "\n".join([main_tex, abstract_tex, exp_tex, table_tex, mechanism_tex_section, robustness_section_tex])
    normalized_exp_tex = re.sub(r"\s+", " ", exp_tex)
    analysis_tex = "\n".join([mechanism_tex_section, robustness_section_tex])
    normalized_analysis_tex = re.sub(r"\s+", " ", analysis_tex)
    normalized_discussion_tex = re.sub(r"\s+", " ", discussion_tex)
    calibration_section = normalized_analysis_tex.split("\\input{tables/table_trace_biopt_calibration_probe}", 1)[1].split("\\input{tables/table_trace_biopt_stage16_calibrated_probe}", 1)[0]
    stage16_section = normalized_analysis_tex.split("\\input{tables/table_trace_biopt_stage16_calibrated_probe}", 1)[1].split("Robustness evidence is routed as stress-test evidence.", 1)[0]
    stage16_rows = sum(row["evidence_source"].startswith("stage16_replaceable:") for row in delta.values())
    stage15_rows = sum(row["evidence_source"] == "stage15_main" for row in delta.values())
    directional_rows = [
        row for row in delta.values()
        if int(row["paired_win_count"]) < int(row["paired_count"]) or float(row["paired_paired_t_p"]) >= 0.05
    ]

    claims: list[dict[str, object]] = []
    claims.append(status_equal("dominance_table_row_count", len(table), 9))
    claims.append(status_equal("current_best_evidence_row_count", len(delta), 9))
    claims.append(status_equal("claim_contract_row_count", contract.get("row_count"), 9))
    aggregate_status = (
        "supported_submission_ready"
        if all(str(row["claim_status"]) == "supported_submission_ready" for row in contract["rows"])
        else "supported_directional"
    )
    claims.append(status_equal("aggregate_claim_status", contract["aggregate_claim"]["status"], aggregate_status))

    all_beats = all(row["trace_beats_best_baseline"] == "True" for row in delta.values())
    claims.append(status_equal("all_rows_trace_beats_best_baseline", all_beats, True))
    claims.append(status_equal("all_rows_ten_paired_splits", {int(row["paired_count"]) for row in delta.values()}, {10}))
    claims.append(status_equal("all_rows_baseline_count", {int(row["baseline_count"]) for row in delta.values()}, {21}))
    claims.append(status_equal("datasets_in_contract", set(contract["aggregate_claim"]["datasets"]), {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    claims.append(status_equal("budgets_in_contract", set(contract["aggregate_claim"]["budgets"]), {0.1, 0.2, 0.3}))
    claims.append(status_equal("title_mentions_recoverability_driven_network_design", "TRACE-BiOpt: Recoverability-Driven Bilevel Transportation Network Design for Sparse Traffic Sensor Siting" in main_tex, True))
    claims.append(status_equal("shorttitle_mentions_transportation_network_design", "\\shorttitle{TRACE-BiOpt Transportation Network Design}" in main_tex, True))
    claims.append(status_equal(
        "main_frontmatter_abstract_mentions_freeze_before_future_states",
        "Traffic agencies must freeze sparse sensor siting plans as long-lived fixed-infrastructure transportation network-design decisions before most future traffic states are observed" in main_tex,
        True,
    ))
    claims.append(status_equal(
        "main_frontmatter_abstract_mentions_bilevel_stochastic_network_design_problem",
        "We formulate that deployment-time question as a recoverability-driven bilevel stochastic network design problem" in main_tex,
        True,
    ))
    claims.append(status_equal(
        "main_frontmatter_abstract_mentions_single_bilevel_stochastic_transportation_network_design_method",
        "The proposed method, TRACE-BiOpt, is a single recoverability-driven bilevel stochastic transportation network-design method centered on a transparent inverse problem" in main_tex,
        True,
    ))
    claims.append(status_equal(
        "main_frontmatter_abstract_mentions_external_audited_comparison_class_contract",
        "The paper therefore claims one unified, analyzable, theory-backed bilevel stochastic transportation network-design method whose evidence contract is an external audited comparison-class contract that compresses to row-wise strongest-baseline dominance on the tested datasets and then survives all-baseline corrected paired tests, with global optimality and untested-baseline dominance explicitly excluded." in main_tex,
        True,
    ))
    claims.append(status_equal(
        "main_abstract_mentions_exact_benchmark",
        "bounded exact benchmark exact-hits 27/27 deterministic 16-node subnetworks under the same objective" in main_tex,
        True,
    ))
    claims.append(status_equal(
        "main_frontmatter_abstract_mentions_holm_189_no_nonworse_challenger",
        "Holm-corrected one-sided paired tests across all 189 current-best row-baseline comparisons leave no statistically tied or significantly better challenger" in main_tex,
        True,
    ))
    claims.append(status_equal(
        "main_frontmatter_abstract_mentions_21_baselines_11_families",
        "all 21 pre-registered non-BiOpt baselines spanning 11 method families" in main_tex,
        True,
    ))
    claims.append(status_equal(
        "main_abstract_mentions_front_screen_contract",
        "The intended first reading is simple: one long-lived infrastructure decision, one transparent inverse problem, one deterministic solver, one scoped theory package, and one external audited comparison-class contract over 21 pre-registered baselines spanning 11 method families with no surviving challenger after 189 Holm-corrected paired tests." in main_tex,
        True,
    ))
    claims.append(status_equal(
        "abstract_mentions_recoverability_driven_network_design",
        "recoverability-driven bilevel stochastic network design problem" in abstract_tex,
        True,
    ))
    claims.append(status_equal(
        "abstract_mentions_one_recoverability_driven_objective",
        "one recoverability-driven objective" in abstract_tex,
        True,
    ))
    claims.append(status_equal(
        "abstract_mentions_fixed_infrastructure_transportation_network_design_method",
        "single recoverability-driven bilevel stochastic transportation network-design method centered on a transparent inverse problem" in abstract_tex,
        True,
    ))
    claims.append(status_equal(
        "abstract_mentions_external_audited_comparison_class_contract",
        "TRACE-BiOpt should be evaluated as one fixed-infrastructure bilevel stochastic transportation network-design method built around a transparent inverse problem and judged under an external audited comparison-class contract that compresses to row-wise strongest-baseline dominance on held-out reconstruction error and then survives all-baseline corrected paired tests." in abstract_tex,
        True,
    ))
    claims.append(status_equal(
        "abstract_mentions_one_method_one_theory_one_evidence_contract",
        "The intended first reading is simple: one long-lived infrastructure decision, one transparent inverse problem, one deterministic solver, one scoped theory package, and one external audited comparison-class contract over 21 pre-registered baselines spanning 11 method families with no surviving challenger after 189 Holm-corrected paired tests." in abstract_tex,
        True,
    ))
    claims.append(status_equal(
        "abstract_mentions_fixed_infrastructure_network_design_decisions",
        "Traffic agencies must freeze sparse sensor siting plans as long-lived fixed-infrastructure transportation network-design decisions before most future traffic states are observed" in abstract_tex,
        True,
    ))
    claims.append(status_equal(
        "abstract_mentions_deployment_time_question",
        "We formulate that deployment-time question as a recoverability-driven bilevel stochastic network design problem" in abstract_tex,
        True,
    ))
    claims.append(status_equal(
        "abstract_mentions_holm_189_no_nonworse_challenger",
        "Holm-corrected one-sided paired tests across all 189 current-best row-baseline comparisons leave no statistically tied or significantly better challenger" in abstract_tex,
        True,
    ))
    claims.append(status_equal(
        "abstract_mentions_21_baselines_11_families",
        "all 21 pre-registered non-BiOpt baselines spanning 11 method families" in abstract_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_hidden_state_recoverability_not_visibility",
        "the design object is recoverability of the hidden network state rather than visibility of the observed subset" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_agencies_freeze_siting_before_future_states",
        "Traffic agencies must freeze sparse sensor siting plans before most future traffic states are observed" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_hidden_full_network_state_from_partial_measurements",
        "the operational question usually concerns the hidden full-network state that must later be inferred from partial measurements" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_fixed_infrastructure_transportation_network_design_problem",
        "create a fixed-infrastructure transportation network design problem rather than a pure coverage problem" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_recoverability_driven_network_design_for_transparent_state_reconstruction",
        "recoverability-driven stochastic network design for transparent state reconstruction" in intro_tex and "sparse traffic sensor siting" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_one_transportation_network_design_argument",
        "The siting plan and the reconstruction model must therefore be evaluated together as one transportation network design argument rather than as separate sensing and estimation steps." in re.sub(r"\s+", " ", intro_tex),
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_fixed_sparse_set_to_instrument",
        "we choose a fixed sparse set of nodes or links to instrument" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_fixed_infrastructure_traffic_sensor_siting",
        "fixed-infrastructure traffic sensor siting" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_recoverability_driven_bilevel_optimization_method",
        "transparent recoverability-driven bilevel stochastic optimization method for fixed-infrastructure traffic sensor siting" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_not_sparse_sensor_benchmark_result",
        "TRACE-BiOpt should be evaluated as one fixed-infrastructure transportation network-design method built around a transparent inverse problem and judged under an external audited comparison-class contract that compresses to row-wise strongest-baseline dominance on held-out reconstruction error and then survives all-baseline corrected paired tests, not as a sparse-sensor benchmark result with a different winner on each table." in re.sub(r"\s+", " ", intro_tex),
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_one_method_one_theory_one_evidence_contract",
        "The reviewer-facing summary is equally simple: one method, one deterministic solver, one scoped theory package, and one external audited comparison-class contract." in re.sub(r"\s+", " ", intro_tex),
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_front_screen_contract",
        "Put even more compactly, the front-screen contract is one long-lived infrastructure decision, one transparent inverse problem, one deterministic solver, one scoped theory package, and one external audited comparison-class contract." in re.sub(r"\s+", " ", intro_tex),
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_operational_contract_21_11_189",
        "Operationally, that contract means one auditable design argument tested against 21 pre-registered baselines spanning 11 method families, with no surviving challenger after 189 Holm-corrected paired comparisons." in re.sub(r"\s+", " ", intro_tex),
        True,
    ))
    claims.append(status_equal(
        "introduction_contribution_mentions_holm_189_no_nonworse_challenger",
        "Holm-corrected one-sided paired tests across all 189 current-best row-baseline comparisons leave no statistically tied or significantly better pre-registered challenger" in re.sub(r"\s+", " ", intro_tex),
        True,
    ))
    claims.append(status_equal(
        "introduction_contribution_mentions_21_baselines_11_families",
        "the audited comparison class spans 21 baselines across 11 method families" in re.sub(r"\s+", " ", intro_tex),
        True,
    ))
    claims.append(status_equal(
        "introduction_contribution_mentions_not_estimator_benchmark",
        "recoverability-driven bilevel stochastic network design problem rather than as coverage maximization, candidate-pool selection, or an estimator benchmark on a fixed graph" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_contributions_are_fivefold",
        "The contributions are fivefold." in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_contribution_mentions_transparent_gls_map_inverse_problem",
        "we define the lower level as a transparent gls/map inverse problem and the upper level as one recoverability-driven objective over hidden-state loss, posterior uncertainty, tail-risk, and spatial redundancy" in intro_tex.lower(),
        True,
    ))
    claims.append(status_equal(
        "introduction_contribution_mentions_formal_cvar_tail_risk_interpretation",
        "a formal CVaR tail-risk interpretation" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_contribution_mentions_same_recoverability_driven_objective",
        "same recoverability-driven objective" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_contribution_mentions_all_nine_rows_and_bounded_exact_benchmark",
        "all nine rows now satisfy the submission-ready paired-dominance gate" in intro_tex
        and "a bounded exact benchmark shows 27/27 exact hits on deterministic 16-node induced subnetworks under row-wise current-best parameters" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "problem_section_title_mentions_recoverability_driven_bilevel_network_design",
        "\\section{Recoverability-driven bilevel stochastic network design}" in read(PAPER / "sections" / "3_problem.tex"),
        True,
    ))
    claims.append(status_equal(
        "problem_section_mentions_hidden_state_not_visibility",
        "the network-design target is recoverability of the hidden state, not maximal visibility of the observed state" in read(PAPER / "sections" / "3_problem.tex"),
        True,
    ))
    claims.append(status_equal(
        "problem_section_mentions_siting_choice_before_future_traffic_states",
        "A transportation agency chooses a fixed sensor set $\\calS \\subseteq \\calV$ with $|\\calS|=k$ before most future traffic states are observed" in read(PAPER / "sections" / "3_problem.tex"),
        True,
    ))
    claims.append(status_equal(
        "problem_definition_mentions_output_layout_before_test_states_observed",
        "before future deployment-time states in $\\calD_{\\mathrm{te}}$ are observed" in read(PAPER / "sections" / "3_problem.tex")
        and "the design problem is to output a fixed layout $\\hat{\\calS}$" in read(PAPER / "sections" / "3_problem.tex"),
        True,
    ))
    claims.append(status_equal(
        "problem_section_mentions_transparent_inverse_problem_not_visibility_maximization",
        "The paper should therefore be read as a recoverability-driven network-design argument with a transparent inverse problem at its lower level, not as a visibility-maximization exercise." in read(PAPER / "sections" / "3_problem.tex"),
        True,
    ))
    normalized_problem_tex = re.sub(r"\s+", " ", read(PAPER / "sections" / "3_problem.tex"))
    claims.append(status_equal(
        "problem_section_inputs_problem_contract_table",
        "\\input{tables/table_trace_biopt_problem_contract}" in read(PAPER / "sections" / "3_problem.tex"),
        True,
    ))
    claims.append(status_equal(
        "problem_section_mentions_reviewer_facing_problem_contract",
        "Table~\\ref{tab:trace-biopt-problem-contract} turns that definition into a reviewer-facing problem contract before the method details begin." in normalized_problem_tex,
        True,
    ))
    claims.append(status_equal(
        "problem_section_mentions_one_deployment_time_decision_and_external_comparison_class",
        "one deployment-time network-design decision, one hidden-state recoverability target, one bilevel stochastic structure, one split discipline, and one external audited comparison class" in normalized_problem_tex,
        True,
    ))
    claims.append(status_equal(
        "conclusion_mentions_comparison_class_not_benchmark_ranking",
        "That is also the comparison class the paper asks a reviewer to use: fixed-infrastructure transportation network design under downstream recoverability, not estimator tuning, benchmark-style model ranking, or post-hoc layout selection." in re.sub(r"\s+", " ", read(PAPER / "sections" / "8_conclusion.tex")),
        True,
    ))
    claims.append(status_equal(
        "conclusion_mentions_not_benchmark_paper",
        "The intended reading is therefore that TRACE-BiOpt should be evaluated as one fixed-infrastructure transportation network-design method built around a transparent inverse problem and judged under an external audited comparison-class contract that compresses to row-wise strongest-baseline dominance on held-out reconstruction error and then survives all-baseline corrected paired tests, not as a sparse-sensor benchmark paper that happens to borrow traffic data." in re.sub(r"\s+", " ", read(PAPER / "sections" / "8_conclusion.tex")),
        True,
    ))
    claims.append(status_equal(
        "conclusion_mentions_one_method_one_theory_one_evidence_contract",
        "Its shortest reviewer-facing summary is the same one used at the front of the paper: one long-lived infrastructure decision, one transparent inverse problem, one deterministic solver, one scoped theory package, and one external audited comparison-class contract over 21 pre-registered baselines spanning 11 method families with no surviving challenger after 189 Holm-corrected paired tests." in re.sub(r"\s+", " ", read(PAPER / "sections" / "8_conclusion.tex")),
        True,
    ))
    claims.append(status_equal(
        "conclusion_mentions_agency_decision_contract",
        "freeze the sparse sensor siting plan as an infrastructure design decision before deployment, evaluate it by the recoverability it creates for the hidden network state under a transparent estimator, and compare it to the strongest audited alternative rather than to a weak fixed baseline or a post-hoc estimator gain." in re.sub(r"\s+", " ", read(PAPER / "sections" / "8_conclusion.tex")),
        True,
    ))
    claims.append(status_equal(
        "conclusion_mentions_compressed_trb_form",
        "one fixed-infrastructure transportation network-design method built around a transparent inverse problem can be made formulation-consistent, theory-backed, compressible to row-wise strongest-baseline dominance, multiplicity-robust against the full audited comparison class, and interpretable as a principled bilevel stochastic design method on the tested traffic networks without turning into a post-hoc selector story." in re.sub(r"\s+", " ", read(PAPER / "sections" / "8_conclusion.tex")),
        True,
    ))
    claims.append(status_equal(
        "conclusion_mentions_holm_189_no_nonworse_challenger",
        "Holm-corrected one-sided paired tests across all 189 current-best row-baseline comparisons leave no statistically tied or significantly better pre-registered challenger" in re.sub(r"\s+", " ", read(PAPER / "sections" / "8_conclusion.tex")),
        True,
    ))
    claims.append(status_equal(
        "conclusion_mentions_21_baselines_11_families",
        "the audited comparison class spans 21 baselines across 11 method families" in re.sub(r"\s+", " ", read(PAPER / "sections" / "8_conclusion.tex")),
        True,
    ))
    keyword_needles = [
        "transportation network design",
        "traffic sensor siting",
        "traffic state reconstruction",
        "bilevel stochastic optimization",
        "transparent inverse problem",
    ]
    for needle in keyword_needles:
        claims.append(status_equal(f"main_keywords:{needle}", needle in main_tex, True))
    claims.append(status_equal(
        "main_highlights_mentions_no_tied_or_better_pre_registered_challenger",
        "Current-best paired audits show strongest-baseline dominance on all nine tested dataset-budget rows, and Holm-corrected paired tests leave no statistically tied or better challenger across 21 pre-registered baselines spanning 11 method families." in main_tex,
        True,
    ))
    claims.append(status_equal("introduction_inputs_contribution_stack_table", "\\input{tables/table_trace_biopt_contribution_stack}" in intro_tex, True))
    claims.append(status_equal("introduction_inputs_reader_guide_table", "\\input{tables/table_trace_biopt_reader_guide}" in intro_tex, True))
    claims.append(status_equal(
        "introduction_organization_mentions_recoverability_driven_problem",
        "Section~\\ref{sec:problem} defines the recoverability-driven bilevel stochastic network design problem." in intro_tex,
        True,
    ))
    related_tex = read(PAPER / "sections" / "2_related_work.tex")
    normalized_related_tex = re.sub(r"\s+", " ", related_tex)
    claims.append(status_equal("related_work_inputs_novelty_identity_table", "\\input{tables/table_trace_biopt_novelty_identity}" in related_tex, True))
    claims.append(status_equal("related_work_inputs_comparison_class_contract_table", "\\input{tables/table_trace_biopt_comparison_class_contract}" in related_tex, True))
    claims.append(status_equal(
        "related_work_opening_fixes_comparison_class",
        "TRACE-BiOpt should be evaluated as one fixed-infrastructure transportation network-design method built around a transparent inverse problem and judged under an external audited comparison-class contract that compresses to row-wise strongest-baseline dominance on held-out reconstruction error and then survives all-baseline corrected paired tests, not as a sparse-sensor benchmark entry or an estimator-tuning exercise." in normalized_related_tex,
        True,
    ))
    claims.append(status_equal(
        "related_work_opening_mentions_front_page_summary",
        "The shortest comparison-class summary is the same as on the front page: one long-lived infrastructure decision, one transparent inverse problem, one deterministic solver, one scoped theory package, and one external audited comparison-class contract." in normalized_related_tex,
        True,
    ))
    claims.append(status_equal(
        "related_work_opening_mentions_21_11_189_no_survivor",
        "On the current-best evidence chain, that contract now means an audited comparison class of 21 pre-registered baselines spanning 11 method families, with no surviving challenger after 189 Holm-corrected paired comparisons." in normalized_related_tex,
        True,
    ))
    claims.append(status_equal(
        "related_work_opening_mentions_reviewer_facing_classification_rule",
        "Table~\\ref{tab:trace-biopt-comparison-class-contract} turns that opening paragraph into a reviewer-facing classification rule." in normalized_related_tex,
        True,
    ))
    claims.append(status_equal(
        "related_work_mentions_fixed_infrastructure_frozen_before_deployment",
        "It is a long-lived infrastructure layout that must be frozen before deployment and then justified by the recoverability it creates for the hidden network state." in normalized_related_tex,
        True,
    ))
    claims.append(status_equal(
        "related_work_mentions_same_fixed_infrastructure_planning_premise",
        "TRACE-BiOpt follows the same fixed-infrastructure planning premise---the layout must be chosen before measurements are collected---but recasts the design target as hidden-network recoverability under a transparent inverse problem rather than OD or route-demand estimation." in normalized_related_tex,
        True,
    ))
    claims.append(status_equal(
        "related_work_mentions_upstream_move_not_estimator_benchmark",
        "That upstream move is what makes the paper a transportation network-design contribution rather than an estimator benchmark." in normalized_related_tex,
        True,
    ))
    claims.append(status_equal(
        "related_work_mentions_transportation_network_design_comparison_class",
        "TRACE-BiOpt is meant to be read against transportation network design papers that optimize scarce physical resources under downstream system performance, not against leaderboard-style forecasting studies that assume the sensing graph is already given or sparse-sensor benchmark papers that only ask which registered layout scores best on one table." in normalized_related_tex,
        True,
    ))
    claims.append(status_equal(
        "related_work_mentions_fixed_infrastructure_not_sparse_sensor_benchmark",
        "the contribution is meant to be read as one fixed-infrastructure transportation network-design method with a transparent inverse problem and an external audited comparison-class contract, rather than as another sparse-sensor benchmarking exercise." in normalized_related_tex,
        True,
    ))
    claims.append(status_equal(
        "related_work_mentions_robust_bilevel_stochastic_network_design_problem",
        "it formulates sparse traffic sensing as a robust bilevel stochastic network-design problem whose objective is downstream hidden-state recoverability under a transparent estimator" in normalized_related_tex,
        True,
    ))
    claims.append(status_equal(
        "related_work_mentions_not_sparse_sensor_benchmark_papers",
        "not against leaderboard-style forecasting studies that assume the sensing graph is already given or sparse-sensor benchmark papers that only ask which registered layout scores best on one table." in normalized_related_tex,
        True,
    ))
    claims.append(status_equal("appendix_inputs_claim_boundary_matrix", "\\input{tables/table_trace_biopt_claim_boundary_matrix}" in appendix_tex, True))
    claims.append(status_equal("theory_inputs_generalization_burden_table", "\\input{tables/table_trace_biopt_generalization_burden}" in read(PAPER / "sections" / "4_method_theory.tex"), True))
    claims.append(status_equal("theory_inputs_method_contract_table", "\\input{tables/table_trace_biopt_method_contract}" in read(PAPER / "sections" / "4_method_theory.tex"), True))
    claims.append(status_equal("theory_inputs_theory_bridge_table", "\\input{tables/table_trace_biopt_theory_bridge}" in read(PAPER / "sections" / "4_method_theory.tex"), True))

    claims.append(status_equal("claim_boundary_matrix_row_count", len(claim_boundary_matrix_csv), 5))
    claim_boundary_lookup = {row["claim_lane"]: row for row in claim_boundary_matrix_csv}
    expected_claim_lanes = {
        "Main empirical dominance",
        "Calibrated rerun promotion",
        "Theory and solver scope",
        "Mechanism and regime diagnostics",
        "Bounded deployment stress evidence",
    }
    claims.append(status_equal("claim_boundary_matrix_lanes", set(claim_boundary_lookup), expected_claim_lanes))
    claims.append(status_equal("claim_boundary_main_mentions_rows", all(
        needle in claim_boundary_lookup["Main empirical dominance"]["paper_can_say"]
        for needle in ("9/9", "21", "submission-ready paired wins")
    ), True))
    claims.append(status_equal(
        "claim_boundary_promotion_mentions_rows",
        f"{stage16_rows}/9" in claim_boundary_lookup["Calibrated rerun promotion"]["paper_can_say"],
        True,
    ))
    claims.append(status_equal("claim_boundary_theory_nonclaim", "exact global optimality" in claim_boundary_lookup["Theory and solver scope"]["explicit_non_claim"], True))
    claims.append(status_equal("claim_boundary_mechanism_nonclaim", "not extra dominance rows" in claim_boundary_lookup["Mechanism and regime diagnostics"]["explicit_non_claim"], True))
    claims.append(status_equal("claim_boundary_stress_mentions_frontier", all(
        needle in claim_boundary_lookup["Bounded deployment stress evidence"]["paper_can_say"]
        for needle in ("8/9", "block-missing", "narrow failure/drift gaps")
    ), True))
    claim_boundary_table_needles = [
        "Reviewer-facing TRACE-BiOpt claim-boundary matrix",
        "Main empirical dominance",
        "Calibrated rerun promotion",
        "Theory and solver scope",
        "Mechanism and regime diagnostics",
        "Bounded deployment stress evidence",
    ]
    for needle in claim_boundary_table_needles:
        claims.append(status_equal(f"claim_boundary_table:{needle}", needle in claim_boundary_matrix_tex, True))

    for key, row in sorted(delta.items()):
        dataset, budget = key
        label = f"{dataset}-{int(budget * 100)}pct"
        if key not in table:
            claims.append({
                "claim": f"{label}:table_row_present",
                "status": "missing_evidence",
                "paper_value": None,
                "evidence_value": "row expected",
            })
            continue
        t = table[key]
        claims.append(status_round(f"{label}:trace_biopt_mean", float(t["trace"]), float(row["trace_biopt_mean"]), ".4f"))
        claims.append(status_round(f"{label}:best_baseline_mean", float(t["best"]), float(row["best_baseline_mean"]), ".4f"))
        claims.append(status_round(f"{label}:trace_minus_best", float(t["delta"]), float(row["trace_minus_best_baseline"]), ".4f"))
        claims.append(status_equal(f"{label}:paired_win_count", int(t["wins"]), int(row["paired_win_count"])))
        claims.append(status_equal(f"{label}:paired_count", int(t["count"]), int(row["paired_count"])))
        claims.append(status_p(f"{label}:paired_t_p", float(t["p"]), float(row["paired_paired_t_p"])))

    text_checks = {
        "abstract_claims_all_nine_regimes": "in every tested dataset-budget regime",
        "experiments_declares_ten_split_seeds": "ten split seeds, 25 through 34",
        "experiments_scope_pre_registered_non_biopt": "pre-registered non-BiOpt baseline set",
        "experiments_forbids_untested_baselines": "dominance over untested baselines",
        "experiments_mentions_pre_registered_baseline_registry": "The pre-registered baseline registry is fixed before evaluating TRACE-BiOpt dominance.",
        "experiments_mentions_previous_trace_sl_layout_rule": "validation-swap TRACE-SL layout rule",
        "mechanism_mentions_selector_centered_narrative": "selector-centered narrative",
    }
    for name, needle in text_checks.items():
        claims.append(status_equal(name, needle in paper_text, True))
    claims.append(status_equal(
        "abstract_mentions_exact_subnetwork_hits",
        "exact-hits 27/27 deterministic 16-node subnetworks" in abstract_tex,
        True,
    ))
    highlight_needles = [
        "We cast sparse traffic sensing as fixed-infrastructure transportation network design for hidden-state recoverability.",
        "TRACE-BiOpt commits one fixed layout under one recoverability-driven bilevel stochastic objective with a transparent inverse problem.",
        "Current-best paired audits show strongest-baseline dominance on all nine tested dataset-budget rows, and Holm-corrected paired tests leave no statistically tied or better challenger across 21 pre-registered baselines spanning 11 method families.",
        "The theory package covers MAP stability, posterior risk identity, CVaR tail-risk interpretation, layout-class generalization, and exchange-stationarity certificates.",
        "A bounded exact benchmark exact-hits 27/27 deterministic 16-node subnetworks under the same objective.",
    ]
    for needle in highlight_needles:
        claims.append(status_equal(f"main_highlights:{needle}", needle in main_tex, True))
    claims.append(status_equal(
        "introduction_mentions_bounded_exact_front_screen",
        "split-paired, and now also bounded-exact on audited subnetworks" in intro_tex,
        True,
    ))
    claims.append(status_equal(
        "introduction_mentions_reader_guide_questions",
        "is TRACE-BiOpt one method or a selector, does it beat the row-wise strongest audited comparator, how far does the solver guarantee go, and what still remains explicitly bounded" in re.sub(r"\s+", " ", intro_tex),
        True,
    ))
    method_tex = read(PAPER / "sections" / "4_method_theory.tex")
    normalized_method_tex = re.sub(r"\s+", " ", method_tex)
    claims.append(status_equal(
        "method_mentions_single_recoverability_driven_bilevel_optimization_method",
        "TRACE-BiOpt is a single recoverability-driven bilevel stochastic transportation network-design method." in normalized_method_tex,
        True,
    ))
    claims.append(status_equal(
        "method_mentions_transparent_bilevel_stochastic_design_criterion",
        "transparent bilevel stochastic design criterion" in normalized_method_tex,
        True,
    ))
    claims.append(status_equal(
        "method_mentions_principled_bilevel_transportation_network_design_method",
        "supports a transparent, principled bilevel transportation network-design method with a coherent tail-risk term." in normalized_method_tex,
        True,
    ))
    claims.append(status_equal(
        "method_mentions_not_proxy_selector_over_historical_layout_rules",
        "The upper level is not a proxy selector over historical layout rules." in normalized_method_tex,
        True,
    ))
    claims.append(status_equal(
        "method_mentions_not_limited_to_hand_coded_constructive_rules",
        "TRACE-BiOpt is not limited to hand-coded constructive rules;" in normalized_method_tex,
        True,
    ))
    claims.append(status_equal(
        "method_mentions_cvar_epigraph_proposition",
        "\\begin{proposition}[CVaR tail-risk epigraph and interpretation]" in method_tex,
        True,
    ))
    claims.append(status_equal(
        "method_mentions_rockafellar_uryasev_epigraph",
        "Rockafellar--Uryasev variational form of empirical CVaR" in normalized_method_tex
        and "\\min_{\\tau\\in\\mathbb{R}}" in method_tex
        and "coherent tail-risk penalty on deployment-time reconstruction uncertainty" in normalized_method_tex,
        True,
    ))
    claims.append(status_equal(
        "method_mentions_tail_risk_nonclaims_remark",
        "\\begin{remark}[Non-claims]" in method_tex
        and "It does not prove exact global optimality, dominance over untested baselines, or universal cross-network generalization." in normalized_method_tex,
        True,
    ))
    normalized_experiments_tex = re.sub(r"\s+", " ", read(PAPER / "sections" / "5_experiments.tex"))
    claims.append(status_equal(
        "experiments_mentions_recoverability_driven_bilevel_objective",
        "recoverability-driven bilevel objective is strong enough to beat the best" in normalized_experiments_tex,
        True,
    ))
    normalized_robustness_tex = re.sub(r"\s+", " ", read(PAPER / "sections" / "7_robustness.tex"))
    claims.append(status_equal(
        "robustness_mentions_recoverability_driven_robust_extensions",
        "recoverability-driven robust extensions." in normalized_robustness_tex,
        True,
    ))
    discussion_tex = read(PAPER / "sections" / "7_discussion.tex")
    normalized_discussion_tex = re.sub(r"\s+", " ", discussion_tex)
    claims.append(status_equal(
        "discussion_mentions_recoverability_driven_layout",
        "a recoverability-driven layout may instead choose sensors that reduce hidden-state uncertainty and improve recoverability." in normalized_discussion_tex,
        True,
    ))
    claims.append(status_equal(
        "discussion_mentions_recoverability_driven_sensor_siting",
        "reviewable design protocol for how recoverability-driven sensor siting should be audited on large networks." in normalized_discussion_tex,
        True,
    ))
    claims.append(status_equal(
        "discussion_mentions_auditable_network_design_method",
        "TRACE-BiOpt contributes not only a strong-performing auditable stochastic network-design method but also a reviewable design protocol" in normalized_discussion_tex,
        True,
    ))
    normalized_appendix_tex = re.sub(r"\s+", " ", appendix_tex)
    claims.append(status_equal(
        "appendix_mentions_not_undocumented_ad_hoc_local_search",
        "stronger than an undocumented ad hoc local-search routine." in normalized_appendix_tex,
        True,
    ))
    claims.append(status_equal(
        "appendix_mentions_post_hoc_layout_selector",
        "one of the key differences between TRACE-BiOpt and a post-hoc layout selector:" in normalized_appendix_tex,
        True,
    ))
    claims.append(status_equal(
        "appendix_mentions_ad_hoc_layout_rules_not_selector_registry",
        "handled separately by ad hoc layout rules." in normalized_appendix_tex
        and "rather than used to populate a selector registry." in normalized_appendix_tex,
        True,
    ))

    if directional_rows:
        directional_labels = [
            f"{row['dataset'].replace('_', '\\_')} at {int(float(row['budget']) * 100)}\\%"
            for row in sorted(directional_rows, key=lambda row: (row["dataset"], float(row["budget"])))
        ]
        directional_phrase = directional_labels[0] if len(directional_labels) == 1 else ", ".join(directional_labels[:-1]) + f", and {directional_labels[-1]}"
        claims.append(status_equal("abstract_caveats_directional_row", directional_phrase in main_tex and "directional mean dominance" in main_tex, True))
        claims.append(status_equal("table_note_directional_row", directional_phrase.replace(" at ", " ") in table_tex and "directional mean dominance" in table_tex, True))
    else:
        claims.append(status_equal("abstract_caveats_directional_row", "directional mean dominance" not in main_tex, True))
        claims.append(status_equal("table_note_directional_row", "directional mean dominance" not in table_tex, True))

    if directional_rows:
        strongest_sentence_ok = (
            "PeMS7\\_1026 at all three budgets" in normalized_exp_tex
            and "PeMS7\\_228 at 20\\% and 30\\%" in normalized_exp_tex
            and "Seattle at all three budgets" in normalized_exp_tex
            and "wins all ten paired splits" in normalized_exp_tex
        )
    else:
        strongest_sentence_ok = (
            "PeMS7\\_1026, PeMS7\\_228, and Seattle at all three budgets" in normalized_exp_tex
            and "all nine rows" in normalized_exp_tex
            and "wins all ten paired splits" in normalized_exp_tex
        )
    claims.append(status_equal("strongest_paired_evidence_sentence", strongest_sentence_ok, True))

    weakest = contract["aggregate_claim"]["weakest_margin_row"]
    claims.append(status_equal("weakest_margin_dataset", weakest["dataset"], "PeMS7_1026"))
    claims.append(status_equal("weakest_margin_budget", float(weakest["budget"]), 0.3))

    total_rows = len(delta)
    beaten_rows = sum(row["trace_beats_best_baseline"] == "True" for row in delta.values())
    significant_rows = sum(float(row["paired_paired_t_p"]) < 0.05 for row in delta.values())
    all_split_win_rows = sum(int(row["paired_win_count"]) == int(row["paired_count"]) for row in delta.values())
    baseline_counts = {int(row["baseline_count"]) for row in delta.values()}
    comparator_counts = Counter(row["best_baseline_layout"] for row in delta.values())
    weakest_delta = min(delta.values(), key=lambda row: abs(float(row["trace_minus_best_baseline"])))
    cert = {
        row["certificate"]: row
        for row in cert_rows
        if row["method"] == "gls_map"
    }
    expected_mechanism_needles = [
        f"{beaten_rows}/{total_rows} rows",
        f"{next(iter(baseline_counts))} baseline rows per regime" if len(baseline_counts) == 1 else "baseline rows per regime",
        f"{significant_rows}/{total_rows} rows have paired t-test p<0.05",
        f"{all_split_win_rows}/{total_rows} rows win all ten paired splits",
        f"{weakest_delta['dataset']} {int(float(weakest_delta['budget']) * 100)}%",
        f"delta {float(weakest_delta['trace_minus_best_baseline']):.4f} MAE",
        f"{int(weakest_delta['paired_win_count'])}/{int(weakest_delta['paired_count'])} paired wins",
        f"paired t p={float(weakest_delta['paired_paired_t_p']):.4f}",
        *[
            f"{name} in {count}/{total_rows} rows"
            for name, count in sorted(comparator_counts.items())
        ],
        f"posterior trace Spearman rho={float(cert['posterior_trace']['spearman_mae_mean']):.3f}",
        f"condition number rho={float(cert['condition_number']['spearman_mae_mean']):.3f}",
        f"information logdet rho={float(cert['information_logdet']['spearman_mae_mean']):.3f}",
        f"n={int(float(cert['posterior_trace']['spearman_mae_count']))}",
    ]
    mechanism_text = "\n".join(
        [mechanism_tex, *[f"{row['diagnostic']} {row['evidence']} {row['interpretation']}" for row in mechanism_csv]]
    )
    claims.append(status_equal("mechanism_table_row_count", len(mechanism_csv), 5))
    claims.append(status_equal("analysis_inputs_mechanism_table", "\\input{tables/table_trace_biopt_mechanism}" in analysis_tex, True))
    claims.append(status_equal("analysis_inputs_map_stability_table", "\\input{tables/table_trace_biopt_map_stability_posture}" in analysis_tex, True))
    claims.append(status_equal("analysis_inputs_posterior_risk_table", "\\input{tables/table_trace_biopt_posterior_risk_posture}" in analysis_tex, True))
    claims.append(status_equal("analysis_inputs_regime_lessons_table", "\\input{tables/table_trace_biopt_regime_lessons}" in analysis_tex, True))
    for needle in expected_mechanism_needles:
        claims.append(status_equal(f"mechanism_evidence:{needle}", needle in mechanism_text, True))
    claims.append(status_equal("analysis_inputs_route_ablation_table", "\\input{tables/table_trace_biopt_route_ablation}" in analysis_tex, True))
    claims.append(status_equal("route_ablation_row_count", len(route_ablation_csv), 5))
    route_ablation_lookup = {
        (row["case_label"], row["ablated_route_label"]): row
        for row in route_ablation_csv
    }
    expected_route_ablation = {
        ("PeMS7\\_228 10\\%", "Stage15 certified"): {"current_test_mae": 3.248442, "ablated_test_mae": 3.377498, "mae_penalty_vs_current": 0.129056},
        ("PeMS7\\_228 10\\%", "Zero-weight probe"): {"current_test_mae": 3.248442, "ablated_test_mae": 3.417499, "mae_penalty_vs_current": 0.169057},
        ("Seattle 20\\%", "Zero-weight probe"): {"current_test_mae": 2.674346, "ablated_test_mae": 2.710052, "mae_penalty_vs_current": 0.035706},
        ("Seattle 30\\%", "Zero-weight probe"): {"current_test_mae": 2.487537, "ablated_test_mae": 2.519570, "mae_penalty_vs_current": 0.032033},
        ("PeMS7\\_1026 30\\%", "Stage15 default"): {"current_test_mae": 3.036503, "ablated_test_mae": 3.071089, "mae_penalty_vs_current": 0.034586},
    }
    for key, expected in expected_route_ablation.items():
        row = route_ablation_lookup[key]
        label = f"{key[0]} / {key[1]}"
        claims.append(status_round(f"route_ablation_current_mae:{label}", float(row["current_test_mae"]), expected["current_test_mae"], ".6f"))
        claims.append(status_round(f"route_ablation_ablated_mae:{label}", float(row["ablated_test_mae"]), expected["ablated_test_mae"], ".6f"))
        claims.append(status_round(f"route_ablation_delta:{label}", float(row["mae_penalty_vs_current"]), expected["mae_penalty_vs_current"], ".6f"))
    route_ablation_needles = [
        "route-ablation result",
        "beats both the original Stage15 certified route by 0.129 MAE",
        "zero-weight strong-search probe by 0.169 MAE",
        "removing the posterior/CVaR/spatial terms under stronger search still worsens held-out MAE",
        "from 3.071 to 3.037",
        "route perturbations inside one audited objective family",
    ]
    for needle in route_ablation_needles:
        claims.append(status_equal(f"route_ablation_text:{needle}", needle in normalized_analysis_tex, True))
    route_ablation_table_needles = [
        "Reviewer-facing TRACE-BiOpt route-ablation slices",
        "PeMS7\\_228 10\\%",
        "Seattle 20\\%",
        "PeMS7\\_1026 30\\%",
        "0.169",
    ]
    for needle in route_ablation_table_needles:
        claims.append(status_equal(f"route_ablation_table:{needle}", needle in route_ablation_tex, True))
    claims.append(status_equal("analysis_inputs_calibration_alignment_figure", "\\includegraphics[width=0.98\\linewidth]{figures/fig_trace_biopt_calibration_alignment.pdf}" in analysis_tex, True))
    claims.append(status_equal("calibration_alignment_point_count", len(calibration_alignment_points_csv), 450))
    claims.append(status_equal("calibration_alignment_layout_types", {row["layout_type"] for row in calibration_alignment_points_csv}, {"trace_biopt", "validation_swap_selected", "multistart_swap_by_validation", "rcss_selected", "best_random_by_validation"}))
    claims.append(status_equal("calibration_alignment_datasets", {row["dataset"] for row in calibration_alignment_points_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    summary_lookup = {
        (row["scope"], row["metric_x"], row["statistic"]): row
        for row in calibration_alignment_summary_csv
    }
    claims.append(status_equal("calibration_alignment_summary_rows", len(calibration_alignment_summary_csv), 20))
    claims.append(status_equal("calibration_alignment_selected_n", int(summary_lookup[("selected_layout_rows", "validation_selected_mae", "spearman")]["n"]), 450))
    claims.append(status_round("calibration_alignment_validation_spearman", float(summary_lookup[("selected_layout_rows", "validation_selected_mae", "spearman")]["value"]), 0.5399133960501142, ".6f"))
    claims.append(status_round("calibration_alignment_posterior_spearman", float(summary_lookup[("selected_layout_rows", "posterior_trace", "spearman")]["value"]), 0.3186709616299088, ".6f"))
    fullpool_posterior_row = next(
        row for row in cert_rows
        if row["method"] == "gls_map" and row["certificate"] == "posterior_trace"
    )
    claims.append(status_round("calibration_alignment_fullpool_posterior_spearman_mean", float(summary_lookup[("full_layout_seedwise_summary", "posterior_trace", "spearman_mean")]["value"]), float(fullpool_posterior_row["spearman_mae_mean"]), ".6f"))
    calibration_alignment_needles = [
        "450 GLS/MAP",
        "Spearman $\\rho=0.540$",
        "PeMS7\\_228 at 10\\%",
        "PeMS7\\_1026 at 30\\%",
        "Spearman $\\rho=0.319$",
        "$\\rho=0.849$",
    ]
    for needle in calibration_alignment_needles:
        claims.append(status_equal(f"calibration_alignment_text:{needle}", needle in analysis_tex, True))
    expected_fingerprint_baselines = {
        "PeMS7_1026": "swap_from_greedy_a_trace",
        "PeMS7_228": "validation_swap_selected",
        "Seattle": "rcss_selected",
    }
    claims.append(status_equal("analysis_inputs_sensor_map_figure", "\\includegraphics[width=0.98\\linewidth]{figures/fig_trace_biopt_sensor_maps.pdf}" in analysis_tex, True))
    claims.append(status_equal("analysis_inputs_spatial_posture_table", "\\input{tables/table_trace_biopt_spatial_posture}" in analysis_tex, True))
    claims.append(status_equal("sensor_map_summary_rows", len(sensor_map_summary_csv), 6))
    claims.append(status_equal("spatial_posture_row_count", len(spatial_posture_csv), 3))
    spatial_lookup = {row["dataset"]: row for row in spatial_posture_csv}
    claims.append(status_round(
        "spatial_posture_pems228_pairwise_delta",
        float(spatial_lookup["PeMS7_228"]["pairwise_distance_delta"]),
        276.6730457211852,
        ".2f",
    ))
    claims.append(status_round(
        "spatial_posture_seattle_pairwise_delta",
        float(spatial_lookup["Seattle"]["pairwise_distance_delta"]),
        2.8391129032258036,
        ".2f",
    ))
    claims.append(status_round(
        "spatial_posture_pems1026_pairwise_delta",
        float(spatial_lookup["PeMS7_1026"]["pairwise_distance_delta"]),
        -3012.0378503712127,
        ".2f",
    ))
    claims.append(status_equal(
        "spatial_posture_pems1026_always_selected",
        (spatial_lookup["PeMS7_1026"]["trace_always_selected_nodes"], spatial_lookup["PeMS7_1026"]["baseline_always_selected_nodes"]),
        ("11", "20"),
    ))
    claims.append(status_equal(
        "spatial_posture_pems1026_unique_support",
        (spatial_lookup["PeMS7_1026"]["trace_unique_nodes"], spatial_lookup["PeMS7_1026"]["baseline_unique_nodes"]),
        ("291", "246"),
    ))
    sensor_map_expected_modes = {
        ("PeMS7_1026", "trace_biopt_current_best"): "distance_spectral_embedding",
        ("PeMS7_1026", "strongest_baseline"): "distance_spectral_embedding",
        ("PeMS7_228", "trace_biopt_current_best"): "geographic_station_coordinates",
        ("PeMS7_228", "strongest_baseline"): "geographic_station_coordinates",
        ("Seattle", "trace_biopt_current_best"): "geographic_cabinet_coordinates",
        ("Seattle", "strongest_baseline"): "geographic_cabinet_coordinates",
    }
    sensor_map_expected_sources = {
        ("PeMS7_1026", "trace_biopt_current_best"): "stage16_replaceable:pems7_1026_10_20_posterior_iter20",
        ("PeMS7_1026", "strongest_baseline"): "stage15_baseline",
        ("PeMS7_228", "trace_biopt_current_best"): "stage16_replaceable:train_val_lowcert_delta1_fullsearch",
        ("PeMS7_228", "strongest_baseline"): "stage15_baseline",
        ("Seattle", "trace_biopt_current_best"): "stage15_main",
        ("Seattle", "strongest_baseline"): "stage15_baseline",
    }
    sensor_map_expected_labels = {
        ("PeMS7_1026", "strongest_baseline"): "Swap from A-trace",
        ("PeMS7_228", "strongest_baseline"): "Prev. TRACE-SL",
        ("Seattle", "strongest_baseline"): "RCSS",
    }
    for row in sensor_map_summary_csv:
        key = (row["dataset"], row["layout_role"])
        claims.append(status_equal(f"sensor_map_budget:{key}", row["budget_pct"], "10"))
        claims.append(status_equal(f"sensor_map_coordinate_mode:{key}", row["coordinate_mode"], sensor_map_expected_modes[key]))
        claims.append(status_equal(f"sensor_map_evidence_source:{key}", row["evidence_source"], sensor_map_expected_sources[key]))
        if row["layout_role"] == "strongest_baseline":
            claims.append(status_equal(f"sensor_map_baseline_layout:{key}", row["layout_type"], expected_fingerprint_baselines[row["dataset"]]))
            claims.append(status_equal(f"sensor_map_baseline_label:{key}", row["layout_label"], sensor_map_expected_labels[(row["dataset"], row["layout_role"])]))
        else:
            claims.append(status_equal(f"sensor_map_trace_layout:{key}", row["layout_type"], "trace_biopt"))
            claims.append(status_equal(f"sensor_map_trace_label:{key}", row["layout_label"], "TRACE-BiOpt"))
    sensor_map_needles = [
        "transport-facing reading",
        "released cabinet or station coordinates are available",
        "distance-derived embedding",
        "does not replace the audited overlap statistics",
    ]
    for needle in sensor_map_needles:
        claims.append(status_equal(f"sensor_map_text:{needle}", needle in normalized_analysis_tex, True))
    spatial_posture_needles = [
        "more distributed than the row-wise strongest baselines",
        "always-selected nodes drop from 20 to 11",
        "expands from 246 to 291 nodes",
        "guardrail against local over-concentration",
    ]
    for needle in spatial_posture_needles:
        claims.append(status_equal(f"spatial_posture_text:{needle}", needle in normalized_analysis_tex, True))
    spatial_posture_table_needles = [
        "Reviewer-facing current-best low-budget spatial posture",
        "PeMS7\\_1026",
        "11/20",
        "291/246",
    ]
    for needle in spatial_posture_table_needles:
        claims.append(status_equal(f"spatial_posture_table:{needle}", needle in spatial_posture_tex, True))
    claims.append(status_equal("analysis_inputs_layout_consensus_table", "\\input{tables/table_trace_biopt_layout_consensus_posture}" in analysis_tex, True))
    claims.append(status_equal("layout_consensus_row_count", len(layout_consensus_csv), 3))
    layout_consensus_lookup = {row["dataset"]: row for row in layout_consensus_csv}
    claims.append(status_equal("layout_consensus_datasets", set(layout_consensus_lookup), {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    expected_layout_consensus = {
        "PeMS7_1026": {
            "trace_mean_pairwise_jaccard": 0.3462739895438519,
            "baseline_mean_pairwise_jaccard": 0.4291663277205465,
            "pairwise_jaccard_delta": -0.08289233817669461,
            "trace_pairwise_jaccard_std": 0.04089414477123581,
            "baseline_pairwise_jaccard_std": 0.04938734395715134,
            "trace_always_selected_nodes": "11",
            "baseline_always_selected_nodes": "20",
            "trace_unique_nodes": "291",
            "baseline_unique_nodes": "246",
            "best_baseline_layout": "swap_from_greedy_a_trace",
        },
        "PeMS7_228": {
            "trace_mean_pairwise_jaccard": 0.36706544031123806,
            "baseline_mean_pairwise_jaccard": 0.3496487280655162,
            "pairwise_jaccard_delta": 0.017416712245721833,
            "trace_pairwise_jaccard_std": 0.09781422311524599,
            "baseline_pairwise_jaccard_std": 0.15621912622987977,
            "trace_always_selected_nodes": "5",
            "baseline_always_selected_nodes": "0",
            "trace_unique_nodes": "58",
            "baseline_unique_nodes": "74",
            "best_baseline_layout": "validation_swap_selected",
        },
        "Seattle": {
            "trace_mean_pairwise_jaccard": 0.15384248976539128,
            "baseline_mean_pairwise_jaccard": 0.329914623933016,
            "pairwise_jaccard_delta": -0.17607213416762474,
            "trace_pairwise_jaccard_std": 0.052249527559142674,
            "baseline_pairwise_jaccard_std": 0.06788431141843236,
            "trace_always_selected_nodes": "0",
            "baseline_always_selected_nodes": "3",
            "trace_unique_nodes": "142",
            "baseline_unique_nodes": "100",
            "best_baseline_layout": "rcss_selected",
        },
    }
    for dataset, expected in expected_layout_consensus.items():
        row = layout_consensus_lookup[dataset]
        claims.append(status_equal(f"layout_consensus_budget:{dataset}", row["budget_pct"], "10"))
        claims.append(status_equal(f"layout_consensus_baseline:{dataset}", row["best_baseline_layout"], expected["best_baseline_layout"]))
        claims.append(status_round(f"layout_consensus_trace_mean:{dataset}", float(row["trace_mean_pairwise_jaccard"]), expected["trace_mean_pairwise_jaccard"], ".6f"))
        claims.append(status_round(f"layout_consensus_baseline_mean:{dataset}", float(row["baseline_mean_pairwise_jaccard"]), expected["baseline_mean_pairwise_jaccard"], ".6f"))
        claims.append(status_round(f"layout_consensus_delta:{dataset}", float(row["pairwise_jaccard_delta"]), expected["pairwise_jaccard_delta"], ".6f"))
        claims.append(status_round(f"layout_consensus_trace_std:{dataset}", float(row["trace_pairwise_jaccard_std"]), expected["trace_pairwise_jaccard_std"], ".6f"))
        claims.append(status_round(f"layout_consensus_baseline_std:{dataset}", float(row["baseline_pairwise_jaccard_std"]), expected["baseline_pairwise_jaccard_std"], ".6f"))
        claims.append(status_equal(f"layout_consensus_trace_always_selected:{dataset}", row["trace_always_selected_nodes"], expected["trace_always_selected_nodes"]))
        claims.append(status_equal(f"layout_consensus_baseline_always_selected:{dataset}", row["baseline_always_selected_nodes"], expected["baseline_always_selected_nodes"]))
        claims.append(status_equal(f"layout_consensus_trace_unique:{dataset}", row["trace_unique_nodes"], expected["trace_unique_nodes"]))
        claims.append(status_equal(f"layout_consensus_baseline_unique:{dataset}", row["baseline_unique_nodes"], expected["baseline_unique_nodes"]))
    layout_consensus_needles = [
        "adds the split-level consensus reading",
        "slightly more consensus-stable than the previous TRACE-SL baseline",
        "erratic swap noise",
        "broader yet still coherent support family",
        "split-fragile way",
    ]
    for needle in layout_consensus_needles:
        claims.append(status_equal(f"layout_consensus_text:{needle}", needle in normalized_analysis_tex, True))
    layout_consensus_table_needles = [
        "Reviewer-facing current-best low-budget layout-consensus posture",
        "PeMS7\\_228",
        "0.367",
        "0.098",
        "5/0",
    ]
    for needle in layout_consensus_table_needles:
        claims.append(status_equal(f"layout_consensus_table:{needle}", needle in layout_consensus_tex, True))
    claims.append(status_equal("analysis_inputs_layout_fingerprint_figure", "\\includegraphics[width=0.92\\linewidth]{figures/fig_trace_biopt_layout_fingerprints.pdf}" in analysis_tex, True))
    claims.append(status_equal("layout_fingerprint_summary_rows", len(layout_fingerprint_summary_csv), 3))
    for row in layout_fingerprint_summary_csv:
        dataset = row["dataset"]
        claims.append(status_equal(f"layout_fingerprint_budget:{dataset}", row["budget_pct"], "10"))
        claims.append(status_equal(f"layout_fingerprint_best_baseline:{dataset}", row["best_baseline_layout"], expected_fingerprint_baselines[dataset]))
    expected_jaccard = {
        "PeMS7_1026": 0.675241,
        "PeMS7_228": 0.302326,
        "Seattle": 0.351955,
    }
    for row in layout_fingerprint_summary_csv:
        dataset = row["dataset"]
        claims.append(status_round(f"layout_fingerprint_jaccard:{dataset}", float(row["unique_jaccard_overlap"]), expected_jaccard[dataset], ".6f"))
    layout_fingerprint_needles = [
        "0.30 unique-node Jaccard overlap",
        "0.35",
        "0.68",
        "different layout logic",
    ]
    for needle in layout_fingerprint_needles:
        claims.append(status_equal(f"layout_fingerprint_text:{needle}", needle in analysis_tex, True))
    claims.append(status_equal("analysis_inputs_hidden_error_heatmap_figure", "\\includegraphics[width=0.98\\linewidth]{figures/fig_trace_biopt_hidden_error_heatmaps.pdf}" in analysis_tex, True))
    claims.append(status_equal("hidden_error_heatmap_summary_rows", len(hidden_error_heatmap_summary_csv), 3))
    claims.append(status_equal("hidden_error_heatmap_datasets", {row["dataset"] for row in hidden_error_heatmap_summary_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    claims.append(status_equal("hidden_error_heatmap_grid_datasets", {row["dataset"] for row in hidden_error_heatmap_grid_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    claims.append(status_equal("hidden_error_heatmap_seed", {row["split_seed"] for row in hidden_error_heatmap_summary_csv}, {"25"}))
    expected_hidden_error_sources = {
        "PeMS7_1026": "Stage16 calibrated rerun",
        "PeMS7_228": "Stage16 calibrated rerun",
        "Seattle": "Stage15 main evidence",
    }
    expected_hidden_error_baselines = {
        "PeMS7_1026": "Swap from A-trace",
        "PeMS7_228": "Prev. TRACE-SL",
        "Seattle": "RCSS",
    }
    expected_hidden_error_improved_share = {
        "PeMS7_1026": 0.6033898305084746,
        "PeMS7_228": 0.6084656084656085,
        "Seattle": 0.5430711610486891,
    }
    expected_hidden_error_mean_gain = {
        "PeMS7_1026": 0.11282869311040485,
        "PeMS7_228": 0.10007840484300391,
        "Seattle": 0.03448340638503791,
    }
    for row in hidden_error_heatmap_summary_csv:
        dataset = row["dataset"]
        claims.append(status_equal(f"hidden_error_heatmap_budget:{dataset}", row["budget_pct"], "10"))
        claims.append(status_equal(f"hidden_error_heatmap_source:{dataset}", row["trace_source_label"], expected_hidden_error_sources[dataset]))
        claims.append(status_equal(f"hidden_error_heatmap_baseline:{dataset}", row["best_baseline_label"], expected_hidden_error_baselines[dataset]))
        claims.append(status_round(f"hidden_error_heatmap_improved_share:{dataset}", float(row["improved_hidden_share"]), expected_hidden_error_improved_share[dataset], ".12f"))
        claims.append(status_round(f"hidden_error_heatmap_mean_gain:{dataset}", float(row["mean_hidden_gain"]), expected_hidden_error_mean_gain[dataset], ".12f"))
    hidden_error_heatmap_needles = [
        "60.3\\% of nodes for PeMS7\\_1026, 60.8\\% for PeMS7\\_228, and 54.3\\% for Seattle",
        "mean node-wise gains are 0.113, 0.100, and 0.034",
        "bounded mechanism slices, not new aggregate dominance rows",
        "one or two extreme error spikes",
    ]
    for needle in hidden_error_heatmap_needles:
        claims.append(status_equal(f"hidden_error_heatmap_text:{needle}", needle in normalized_analysis_tex, True))

    stage16_rows = sum(row["source"] == "Stage16 calibrated rerun" for row in provenance_csv)
    paired_ready_rows = sum(
        row["claim_status"] == "supported_submission_ready"
        for row in contract["rows"]
    )
    exact_hits = sum(int(row["exact_hits"]) for row in exact_subnetwork_summary_csv)
    exact_cases = sum(int(row["exact_cases"]) for row in exact_subnetwork_summary_csv)
    aggregate_significance_row = next(
        row for row in significance_posture_summary_csv if row["dataset"] == "All rows"
    )
    contribution_needles = [
        "robust bilevel stochastic network-design problem",
        "single-objective deterministic solver",
        "formal CVaR tail-risk epigraph",
        "uniform validation generalization over all size-$k$ layouts",
        "external audited comparison-class contract",
        f"{len(contract['aggregate_claim']['baseline_registry'])} pre-registered non-BiOpt baselines",
        "11 audited method families",
        f"{len(contract['aggregate_claim']['datasets'])} networks and {len(contract['aggregate_claim']['budgets'])} budgets",
        f"{stage16_rows}/{len(provenance_csv)} main rows are already promoted from calibrated reruns",
        f"{paired_ready_rows}/{contract['row_count']} rows satisfy the submission-ready paired-dominance gate",
        f"Holm-corrected paired tests still show TRACE-BiOpt significantly better on {int(aggregate_significance_row['significantly_worse_baselines_holm'])}/{int(aggregate_significance_row['baseline_count'])} row-baseline comparisons with no surviving tied or better challenger",
        f"exact-hits {exact_hits}/{exact_cases} audited cases with zero objective gap",
        "explicitly excludes global optimality",
        "principled bilevel stochastic design method",
        "explicit external audited comparison-class contract instead of a selective benchmark screen",
    ]
    for needle in contribution_needles:
        claims.append(status_equal(f"contribution_stack:{needle}", needle in contribution_stack_tex, True))
    dominance_challenger_expectations = {
        ("PeMS7_1026", 0.1): "Swap from A-trace",
        ("PeMS7_1026", 0.2): "Prev. TRACE-SL",
        ("PeMS7_1026", 0.3): "Prev. TRACE-SL",
        ("PeMS7_228", 0.1): "Prev. TRACE-SL",
        ("PeMS7_228", 0.2): "Prev. TRACE-SL",
        ("PeMS7_228", 0.3): "Prev. TRACE-SL",
        ("Seattle", 0.1): "RCSS",
        ("Seattle", 0.2): "Prev. TRACE-SL",
        ("Seattle", 0.3): "Prev. TRACE-SL",
    }
    for key, label in dominance_challenger_expectations.items():
        claims.append(status_equal(f"dominance_table_challenger:{key[0]}-{int(key[1]*100)}pct", table[key]["challenger"], label))
    dominance_table_needles = [
        "Strongest challenger",
        "Challenger MAE",
        "Swap from A-trace",
        "Prev. TRACE-SL",
        "RCSS",
    ]
    for needle in dominance_table_needles:
        claims.append(status_equal(f"dominance_table:{needle}", needle in table_tex, True))
    novelty_identity_needles = [
        "formal CVaR tail-risk epigraph",
        "189/189",
        "no surviving tied or better challenger",
        "significance posture",
    ]
    for needle in novelty_identity_needles:
        claims.append(status_equal(f"novelty_identity:{needle}", needle in novelty_identity_tex, True))
    reader_guide_lookup = {row["question"]: row for row in reader_guide_csv}
    claims.append(status_equal("reader_guide_row_count", len(reader_guide_csv), 4))
    claims.append(status_equal(
        "reader_guide_questions",
        set(reader_guide_lookup),
        {
            "Is TRACE-BiOpt one method or a selector?",
            "Does it beat strong audited comparators?",
            "Is the solver only a heuristic?",
            "What remains explicitly bounded?",
        },
    ))
    claims.append(status_equal(
        "reader_guide_single_method_mentions_baselines",
        all(
            needle in reader_guide_lookup["Is TRACE-BiOpt one method or a selector?"]["current_best_answer"]
            for needle in ("One method.", "one deterministic solver", "21 pre-registered non-BiOpt", "11 audited method families", "external audited comparison class", "rather than method candidates")
        ),
        True,
    ))
    claims.append(status_equal(
        "reader_guide_dominance_mentions_stage16",
        all(
            needle in reader_guide_lookup["Does it beat strong audited comparators?"]["current_best_answer"]
            for needle in (
                f"{paired_ready_rows}/9",
                f"{stage16_rows}/9",
                f"{int(aggregate_significance_row['significantly_worse_baselines_holm'])}/{int(aggregate_significance_row['baseline_count'])}",
                "external audited comparison-class contract",
                "21 pre-registered baselines",
                "no surviving tied or better pre-registered challenger",
                "11 audited baseline families",
            )
        ),
        True,
    ))
    claims.append(status_equal(
        "reader_guide_exact_mentions_hits",
        all(
            needle in reader_guide_lookup["Is the solver only a heuristic?"]["current_best_answer"]
            for needle in (f"{exact_hits}/{exact_cases}", "zero objective gap", "full-network global optimality is still excluded")
        ),
        True,
    ))
    claims.append(status_equal(
        "reader_guide_bounded_mentions_seattle10",
        all(
            needle in reader_guide_lookup["What remains explicitly bounded?"]["current_best_answer"]
            for needle in ("Seattle 10%", "Stage15 main evidence", "bounded deployment screens")
        ),
        True,
    ))
    reader_guide_table_needles = [
        "Front-page reviewer guide for TRACE-BiOpt",
        "audited comparison-class contract visible on the front page",
        "Is TRACE-BiOpt one method or a selector?",
        "Does it beat strong audited comparators?",
        "Is the solver only a heuristic?",
        "What remains explicitly bounded?",
        "Seattle 10\\%",
    ]
    for needle in reader_guide_table_needles:
        claims.append(status_equal(f"reader_guide_table:{needle}", needle in reader_guide_tex, True))
    novelty_identity_lookup = {row["possible_misread"]: row for row in novelty_identity_csv}
    claims.append(status_equal("novelty_identity_row_count", len(novelty_identity_csv), 5))
    claims.append(status_equal(
        "novelty_identity_rows",
        set(novelty_identity_lookup),
        {
            "Portfolio or AutoML selector",
            "Surrogate OED or graph-sampling criterion",
            "Estimator benchmark on a fixed graph",
            "Weak-baseline empirical win",
            "Exact global optimization paper",
        },
    ))
    claims.append(status_equal("novelty_identity_selector_mentions_baselines", all(
        needle in novelty_identity_lookup["Portfolio or AutoML selector"]["trace_biopt_identity"]
        for needle in ("21 non-BiOpt layouts", "external audited comparison class", "rather than method candidates")
    ), True))
    claims.append(status_equal("novelty_identity_weak_baseline_mentions_rows", all(
        needle in novelty_identity_lookup["Weak-baseline empirical win"]["trace_biopt_identity"]
        for needle in ("9/9 rows", "8/9 rows")
    ), True))
    claims.append(status_equal("novelty_identity_exact_mentions_hits", all(
        needle in novelty_identity_lookup["Exact global optimization paper"]["trace_biopt_identity"]
        for needle in ("27/27", "full-network global optimality remains explicitly excluded")
    ), True))
    novelty_identity_table_needles = [
        "Reviewer-facing identity test for TRACE-BiOpt",
        "Portfolio or AutoML selector",
        "Surrogate OED or graph-sampling criterion",
        "Estimator benchmark on a fixed graph",
        "Weak-baseline empirical win",
        "Exact global optimization paper",
    ]
    for needle in novelty_identity_table_needles:
        claims.append(status_equal(f"novelty_identity_table:{needle}", needle in novelty_identity_tex, True))

    comparison_class_lookup = {row["axis"]: row for row in comparison_class_contract_csv}
    claims.append(status_equal("comparison_class_contract_row_count", len(comparison_class_contract_csv), 6))
    claims.append(status_equal(
        "comparison_class_contract_axes",
        set(comparison_class_lookup),
        {
            "Decision timing",
            "Optimized quantity",
            "Method identity",
            "Role of baselines",
            "Empirical claim",
            "Explicit scope",
        },
    ))
    claims.append(status_equal(
        "comparison_class_contract_role_of_baselines_counts",
        all(
            needle in comparison_class_lookup["Role of baselines"]["trace_biopt_contract"]
            for needle in ("21", "11", "external audited comparison class")
        ),
        True,
    ))
    claims.append(status_equal(
        "comparison_class_contract_empirical_claim_counts",
        all(
            needle in comparison_class_lookup["Empirical claim"]["trace_biopt_contract"]
            for needle in ("9/9", "189/189", "no surviving challenger")
        ),
        True,
    ))
    claims.append(status_equal(
        "comparison_class_contract_method_identity_nonmisread",
        all(
            needle in comparison_class_lookup["Method identity"]["paper_should_not_be_read_as"]
            for needle in ("portfolio selector", "post-hoc AutoML layout chooser")
        ),
        True,
    ))
    comparison_class_contract_needles = [
        "TRACE-BiOpt comparison-class contract",
        "fixed-infrastructure transportation network-design method",
        "external audited comparison class",
        "Reading axis",
        "The paper should not be read as",
    ]
    for needle in comparison_class_contract_needles:
        claims.append(status_equal(f"comparison_class_contract_table:{needle}", needle in comparison_class_contract_tex, True))

    problem_contract_lookup = {row["contract_axis"]: row for row in problem_contract_csv}
    claims.append(status_equal("problem_contract_row_count", len(problem_contract_csv), 6))
    claims.append(status_equal(
        "problem_contract_axes",
        set(problem_contract_lookup),
        {
            "Decision timing",
            "Target quantity",
            "Bilevel structure",
            "Deployment-time split discipline",
            "External comparison class",
            "Explicit problem scope",
        },
    ))
    claims.append(status_equal(
        "problem_contract_external_comparison_class_counts",
        all(
            needle in problem_contract_lookup["External comparison class"]["paper_visible_statement"]
            for needle in ("21", "11", "189/189", "no surviving challenger")
        ),
        True,
    ))
    claims.append(status_equal(
        "problem_contract_scope_mentions_submission_ready_rows",
        all(
            needle in problem_contract_lookup["Explicit problem scope"]["paper_visible_statement"]
            for needle in ("9/9", "submission-ready", "untested baselines")
        ),
        True,
    ))
    claims.append(status_equal(
        "problem_contract_bilevel_structure_mentions_one_objective",
        all(
            needle in problem_contract_lookup["Bilevel structure"]["reviewer_reading"]
            for needle in ("one transparent inverse problem", "one bilevel stochastic transportation network-design formulation")
        ),
        True,
    ))
    problem_contract_needles = [
        "TRACE-BiOpt problem contract",
        "hidden-state recoverability",
        "external audited comparison class",
        "Contract axis",
        "Reviewer-facing reading",
    ]
    for needle in problem_contract_needles:
        claims.append(status_equal(f"problem_contract_table:{needle}", needle in problem_contract_tex, True))

    method_contract_lookup = {row["contract_axis"]: row for row in method_contract_csv}
    claims.append(status_equal("method_contract_row_count", len(method_contract_csv), 6))
    claims.append(status_equal(
        "method_contract_axes",
        set(method_contract_lookup),
        {
            "Decision object",
            "Transparent inverse problem",
            "Unified objective",
            "Deterministic solver route",
            "External audited comparison class",
            "Explicit boundaries",
        },
    ))
    claims.append(status_equal(
        "method_contract_external_comparison_class_mentions_counts",
        all(
            needle in method_contract_lookup["External audited comparison class"]["paper_visible_statement"]
            for needle in ("21", "3 networks", "3 budgets", "189/189", "no surviving challenger")
        ),
        True,
    ))
    claims.append(status_equal(
        "method_contract_solver_mentions_single_route",
        all(
            needle in method_contract_lookup["Deterministic solver route"]["reviewer_reading"]
            for needle in ("single route", "selector")
        ),
        True,
    ))
    claims.append(status_equal(
        "method_contract_boundaries_mentions_exact_hits",
        all(
            needle in method_contract_lookup["Explicit boundaries"]["paper_visible_statement"]
            for needle in ("global optimality", "27/27", "zero objective gap")
        ),
        True,
    ))
    method_contract_needles = [
        "TRACE-BiOpt method contract",
        "Transparent inverse problem",
        "One deterministic solver uses scale-adaptive initialization",
        "external audited comparison class",
        "Contract axis",
        "Reviewer-facing reading",
    ]
    for needle in method_contract_needles:
        claims.append(status_equal(f"method_contract_table:{needle}", needle in method_contract_tex, True))

    claims.append(status_equal("theory_bridge_row_count", len(theory_bridge_csv), 6))
    theory_bridge_lookup = {row["theorem_label"]: row for row in theory_bridge_csv}
    claims.append(status_equal("theory_bridge_labels", set(theory_bridge_lookup), {"T1", "T2", "T3", "T4", "T5", "T6"}))
    claims.append(status_equal("theory_bridge_t1_readout", theory_bridge_lookup["T1"]["current_best_readout"], "6/9 rows lower condition on all 10 splits; max TRACE-BiOpt condition number 7026."))
    claims.append(status_equal("theory_bridge_t2_readout", theory_bridge_lookup["T2"]["current_best_readout"], "4/4 matched probes show lower posterior trace with lower held-out MAE."))
    claims.append(status_equal("theory_bridge_t3_mentions_range", "0.263" in theory_bridge_lookup["T3"]["current_best_readout"] and "0.770" in theory_bridge_lookup["T3"]["current_best_readout"], True))
    claims.append(status_equal("theory_bridge_t4_mentions_exact_hits", "27/27" in theory_bridge_lookup["T4"]["current_best_readout"], True))
    claims.append(status_equal("theory_bridge_t5_mentions_initializer_families", "objective_forward" in theory_bridge_lookup["T5"]["current_best_readout"] and "posterior_greedy_warm_start" in theory_bridge_lookup["T5"]["current_best_readout"], True))
    claims.append(status_equal("theory_bridge_t6_mentions_tail_share_range", "0.26\\%" in theory_bridge_lookup["T6"]["current_best_readout"] and "1.46\\%" in theory_bridge_lookup["T6"]["current_best_readout"], True))
    theory_bridge_needles = [
        "Table~\\ref{tab:trace-biopt-theory-bridge} turns the theorem list into a reviewer-facing bridge.",
        "each formal statement is paired with a visible current-best evidence lane",
        "the paper does not ask a reviewer to trust that theorems and experiments happen to point in the same direction",
    ]
    for needle in theory_bridge_needles:
        claims.append(status_equal(
            f"theory_bridge_text:{needle}",
            needle in re.sub(r"\s+", " ", read(PAPER / "sections" / "4_method_theory.tex")),
            True,
        ))
    theory_bridge_table_needles = [
        "Theory-to-evidence bridge for TRACE-BiOpt",
        "MAP stability posture table",
        "Posterior-risk posture probes",
        "Generalization-burden table",
        "Exchange-certificate table + bounded exact benchmark",
        "Initializer-posture table",
        "Tail-risk and weight-sensitivity posture tables",
    ]
    for needle in theory_bridge_table_needles:
        claims.append(status_equal(f"theory_bridge_table:{needle}", needle in theory_bridge_tex, True))

    claims.append(status_equal("generalization_burden_row_count", len(generalization_burden_csv), 9))
    claims.append(status_equal("generalization_burden_datasets", {row["dataset"] for row in generalization_burden_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    claims.append(status_equal("generalization_burden_nv", {int(row["n_v"]) for row in generalization_burden_csv}, {576}))
    claims.append(status_equal("generalization_burden_delta", {row["delta"] for row in generalization_burden_csv}, {"0.05"}))
    burden_lookup = {(row["dataset"], row["budget_pct"]): row for row in generalization_burden_csv}
    expected_burden = {
        ("PeMS7_1026", "10"): {"sensor_count": 103, "uniform_gap_factor_over_B": 0.546020, "evidence_source_label": "Stage16 calibrated rerun"},
        ("PeMS7_1026", "20"): {"sensor_count": 205, "uniform_gap_factor_over_B": 0.683907, "evidence_source_label": "Stage16 calibrated rerun"},
        ("PeMS7_1026", "30"): {"sensor_count": 308, "uniform_gap_factor_over_B": 0.769601, "evidence_source_label": "Stage16 calibrated rerun"},
        ("PeMS7_228", "10"): {"sensor_count": 23, "uniform_gap_factor_over_B": 0.262612, "evidence_source_label": "Stage16 calibrated rerun"},
        ("PeMS7_228", "20"): {"sensor_count": 46, "uniform_gap_factor_over_B": 0.327185, "evidence_source_label": "Stage16 calibrated rerun"},
        ("PeMS7_228", "30"): {"sensor_count": 68, "uniform_gap_factor_over_B": 0.365573, "evidence_source_label": "Stage16 calibrated rerun"},
        ("Seattle", "10"): {"sensor_count": 32, "uniform_gap_factor_over_B": 0.308545, "evidence_source_label": "Stage15 main evidence"},
        ("Seattle", "20"): {"sensor_count": 65, "uniform_gap_factor_over_B": 0.387412, "evidence_source_label": "Stage16 calibrated rerun"},
        ("Seattle", "30"): {"sensor_count": 97, "uniform_gap_factor_over_B": 0.434388, "evidence_source_label": "Stage16 calibrated rerun"},
    }
    for key, expected in expected_burden.items():
        row = burden_lookup[key]
        label = f"{key[0]} {key[1]}%"
        claims.append(status_equal(f"generalization_burden_sensor_count:{label}", int(row["sensor_count"]), expected["sensor_count"]))
        claims.append(status_round(f"generalization_burden_factor:{label}", float(row["uniform_gap_factor_over_B"]), expected["uniform_gap_factor_over_B"], ".6f"))
        claims.append(status_equal(f"generalization_burden_source:{label}", row["evidence_source_label"], expected["evidence_source_label"]))
    claims.append(status_equal("generalization_burden_min_row", min(generalization_burden_csv, key=lambda row: float(row["uniform_gap_factor_over_B"]))["dataset"] + " " + min(generalization_burden_csv, key=lambda row: float(row["uniform_gap_factor_over_B"]))["budget_pct"], "PeMS7_228 10"))
    claims.append(status_equal("generalization_burden_max_row", max(generalization_burden_csv, key=lambda row: float(row["uniform_gap_factor_over_B"]))["dataset"] + " " + max(generalization_burden_csv, key=lambda row: float(row["uniform_gap_factor_over_B"]))["budget_pct"], "PeMS7_1026 30"))
    generalization_needles = [
        "common two-day validation window",
        "PeMS7\\_1026 30\\% row reaches $B^{-1}\\Delta_{\\mathrm{unif}}=0.770$",
        "PeMS7\\_228 10\\% is only 0.263",
        "does not prove which row must win empirically",
        "all-layout validation burden is loosest on",
        "PeMS7\\_228 10\\% and tightest on PeMS7\\_1026 30\\%",
    ]
    for needle in generalization_needles:
        claims.append(status_equal(f"generalization_burden_text:{needle}", needle in ("\n".join([read(PAPER / "sections" / "4_method_theory.tex"), analysis_tex, generalization_burden_tex])), True))

    claims.append(status_equal("map_stability_row_count", len(map_stability_csv), 9))
    claims.append(status_equal("map_stability_datasets", {row["dataset"] for row in map_stability_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    map_lookup = {(row["dataset"], row["budget_pct"]): row for row in map_stability_csv}
    expected_map_stability = {
        ("PeMS7_1026", "10"): {"condition_ratio": 0.778069, "lower_condition_win_count": "10", "trace_source_label": "Stage16 calibrated rerun"},
        ("PeMS7_1026", "20"): {"condition_ratio": 0.774555, "lower_condition_win_count": "10", "trace_source_label": "Stage16 calibrated rerun"},
        ("PeMS7_1026", "30"): {"condition_ratio": 0.862612, "lower_condition_win_count": "10", "trace_source_label": "Stage16 calibrated rerun"},
        ("PeMS7_228", "10"): {"condition_ratio": 0.839062, "lower_condition_win_count": "10", "trace_source_label": "Stage16 calibrated rerun"},
        ("PeMS7_228", "20"): {"condition_ratio": 0.687626, "lower_condition_win_count": "10", "trace_source_label": "Stage16 calibrated rerun"},
        ("PeMS7_228", "30"): {"condition_ratio": 0.726983, "lower_condition_win_count": "10", "trace_source_label": "Stage16 calibrated rerun"},
        ("Seattle", "10"): {"condition_ratio": 1.288349, "lower_condition_win_count": "0", "trace_source_label": "Stage15 main evidence"},
        ("Seattle", "20"): {"condition_ratio": 1.221951, "lower_condition_win_count": "1", "trace_source_label": "Stage16 calibrated rerun"},
        ("Seattle", "30"): {"condition_ratio": 1.410572, "lower_condition_win_count": "1", "trace_source_label": "Stage16 calibrated rerun"},
    }
    for key, expected in expected_map_stability.items():
        row = map_lookup[key]
        label = f"{key[0]} {key[1]}%"
        claims.append(status_round(f"map_stability_ratio:{label}", float(row["condition_ratio"]), expected["condition_ratio"], ".6f"))
        claims.append(status_equal(f"map_stability_lower_cond_wins:{label}", row["lower_condition_win_count"], expected["lower_condition_win_count"]))
        claims.append(status_equal(f"map_stability_source:{label}", row["trace_source_label"], expected["trace_source_label"]))
    promoted_rows = [row for row in map_stability_csv if row["trace_source_label"] == "Stage16 calibrated rerun"]
    claims.append(status_equal("map_stability_promoted_rows", len(promoted_rows), 8))
    claims.append(status_equal("map_stability_promoted_all_lower_cond", {row["lower_condition_win_count"] for row in promoted_rows}, {"1", "10"}))
    claims.append(status_equal("map_stability_max_trace_condition", max(round(float(row["trace_condition_max"])) for row in map_stability_csv), 7026))
    map_stability_needles = [
        "Theorem~\\ref{thm:map-stability}",
        "All six",
        "promoted rows now lower the strongest-baseline condition number on all ten splits",
        "condition ratios between 0.69 and 0.86",
        "remaining Seattle rows are more mixed",
        "1.19--1.36",
        "MAE by pushing the inverse problem toward numerical singularity",
    ]
    for needle in map_stability_needles:
        claims.append(status_equal(
            f"map_stability_text:{needle}",
            needle in ("\n".join([normalized_analysis_tex, map_stability_tex])),
            True,
        ))

    claims.append(status_equal("posterior_risk_row_count", len(posterior_risk_csv), 4))
    expected_posterior_cases = {
        ("Seattle 20\\%", "Zero-weight probe"): {"posterior_trace_delta_vs_best": 20.426299, "test_mae_delta_vs_best": 0.035706, "best_route_label": "Seattle diagnostic certified", "best_route_posterior_share_pct": 63.105871},
        ("Seattle 30\\%", "Zero-weight probe"): {"posterior_trace_delta_vs_best": 9.413553, "test_mae_delta_vs_best": 0.032033, "best_route_label": "Seattle diagnostic certified", "best_route_posterior_share_pct": 63.783040},
        ("PeMS7\\_228 10\\%", "Stage15 certified"): {"posterior_trace_delta_vs_best": 35.566209, "test_mae_delta_vs_best": 0.129056, "best_route_label": "Calibrated low-cert", "best_route_posterior_share_pct": 18.849844},
        ("PeMS7\\_228 10\\%", "Zero-weight probe"): {"posterior_trace_delta_vs_best": 28.135938, "test_mae_delta_vs_best": 0.169057, "best_route_label": "Calibrated low-cert", "best_route_posterior_share_pct": 18.849844},
    }
    for row in posterior_risk_csv:
        key = (row["case_label"], row["comparison_route_label"])
        expected = expected_posterior_cases[key]
        label = f"{row['case_label']} / {row['comparison_route_label']}"
        claims.append(status_round(f"posterior_risk_trace_delta:{label}", float(row["posterior_trace_delta_vs_best"]), expected["posterior_trace_delta_vs_best"], ".6f"))
        claims.append(status_round(f"posterior_risk_mae_delta:{label}", float(row["test_mae_delta_vs_best"]), expected["test_mae_delta_vs_best"], ".6f"))
        claims.append(status_equal(f"posterior_risk_best_route:{label}", row["best_route_label"], expected["best_route_label"]))
        claims.append(status_round(f"posterior_risk_best_share:{label}", float(row["best_route_posterior_share_pct"]), expected["best_route_posterior_share_pct"], ".6f"))
        claims.append(status_equal(f"posterior_risk_reading:{label}", row["reading"], "Within a matched route probe, the lower posterior-trace route also achieves lower held-out MAE."))
    posterior_risk_needles = [
        "Theorem~\\ref{thm:trace-risk}",
        "certified route beats the zero-weight probe by lowering posterior trace by",
        "about 20.4 and 9.4",
        "PeMS7\\_228 10\\%, the promoted calibrated low-cert route beats both the Stage15",
        "certified route and the zero-weight probe while lowering posterior trace by",
        "35.6 and 28.1",
        "overstated as a universal MAE ranking theorem",
        "under non-Gaussian traffic data",
    ]
    for needle in posterior_risk_needles:
        claims.append(status_equal(f"posterior_risk_text:{needle}", needle in ("\n".join([analysis_tex, posterior_risk_tex])), True))

    evidence_baselines = sorted({row["layout_type"] for row in layout_summary if row["layout_type"] != "trace_biopt"})
    registry_baselines = sorted(row["baseline"] for row in registry_csv)
    registry_best_counts = {row["baseline"]: int(row["row_specific_best_count"]) for row in registry_csv}
    dominance_best_counts = Counter(row["best_baseline_layout"] for row in delta.values())
    claims.append(status_equal("appendix_inputs_baseline_registry_table", "\\input{tables/table_trace_biopt_baseline_registry}" in appendix_tex, True))
    claims.append(status_equal("appendix_inputs_full_baseline_matrix_table", "\\input{tables/table_trace_biopt_full_baseline_matrix}" in appendix_tex, True))
    claims.append(status_equal("appendix_inputs_current_best_provenance_table", "\\input{tables/table_trace_biopt_current_best_provenance}" in appendix_tex, True))
    claims.append(status_equal("appendix_mentions_trace_biopt_spec", "\\path{TRACE_BIOPT_SPEC.md}" in appendix_tex, True))
    claims.append(status_equal("appendix_mentions_trace_biopt_theory", "\\path{TRACE_BIOPT_THEORY.md}" in appendix_tex, True))
    spec_tex = read(ROOT / "TRACE_BIOPT_SPEC.md")
    claims.append(status_equal(
        "spec_mentions_formal_cvar_tail_risk_epigraph",
        "one formal CVaR tail-risk epigraph inside the upper-level objective" in spec_tex
        and "coherent tail-risk penalty across traffic regimes" in spec_tex,
        True,
    ))
    claims.append(status_equal(
        "spec_mentions_supported_submission_ready_and_8of9",
        "supported_submission_ready" in spec_tex and "8/9 rows are already promoted from Stage16 calibrated reruns" in spec_tex,
        True,
    ))
    claims.append(status_equal(
        "spec_mentions_holm_189_no_surviving_challenger",
        "189/189" in spec_tex and "0 statistically tied challengers" in spec_tex and "0 significantly better challengers" in spec_tex,
        True,
    ))
    claims.append(status_equal(
        "spec_mentions_external_audited_comparison_class_contract",
        "one external audited comparison-class contract over 21 pre-registered" in spec_tex
        and "11 method families" in spec_tex
        and "189 Holm-corrected paired comparisons" in spec_tex,
        True,
    ))
    claims.append(status_equal(
        "spec_mentions_bounded_exact_27of27",
        "27/27" in spec_tex and "deterministic 16-node audited subnetwork cases are exact hits" in spec_tex,
        True,
    ))
    claims.append(status_equal(
        "theory_contract_mentions_cvar_tail_risk_epigraph",
        "## Proposition T6: CVaR Tail-Risk Epigraph and Interpretation" in theory_contract_tex,
        True,
    ))
    claims.append(status_equal(
        "theory_contract_mentions_supported_submission_ready",
        "supported_submission_ready" in theory_contract_tex,
        True,
    ))
    claims.append(status_equal(
        "theory_contract_mentions_189_corrected_comparisons",
        "Holm-corrected" in theory_contract_tex and "189" in theory_contract_tex,
        True,
    ))
    claims.append(status_equal(
        "theory_contract_mentions_seattle10_fail_closed",
        "Seattle 10%" in theory_contract_tex and "fail_closed" in theory_contract_tex,
        True,
    ))
    claims.append(status_equal("appendix_mentions_current_best_claim_contract", "\\path{current_best_trace_biopt_evidence/trace_biopt_claim_contract.json}" in appendix_tex, True))
    claims.append(status_equal("current_best_provenance_row_count", len(provenance_csv), 9))
    claims.append(status_equal("current_best_provenance_stage16_rows", sum(row["source"] == "Stage16 calibrated rerun" for row in provenance_csv), stage16_rows))
    claims.append(status_equal("current_best_provenance_stage15_rows", sum(row["source"] == "Stage15 main evidence" for row in provenance_csv), stage15_rows))
    provenance_text = "\n".join(
        [provenance_tex, *[f"{row['dataset']} {int(float(row['budget']) * 100)}% {row['source']} {row['paired_status']} {row['wins']}" for row in provenance_csv]]
    )
    for row in provenance_csv:
        label = f"{row['dataset']} {int(float(row['budget']) * 100)}%"
        claims.append(status_equal(f"current_best_provenance_source:{label}", row["source"] in provenance_text, True))
        claims.append(status_equal(f"current_best_provenance_wins:{label}", row["wins"] in provenance_text, True))
    claims.append(status_equal("baseline_registry_row_count", len(registry_csv), 21))
    claims.append(status_equal("baseline_registry_matches_stage15_layouts", registry_baselines, evidence_baselines))
    claims.append(status_equal("baseline_registry_all_yes", {row["stage15_registry"] for row in registry_csv}, {"yes"}))
    claims.append(status_equal("baseline_registry_best_count_sum", sum(registry_best_counts.values()), 9))
    for baseline in evidence_baselines:
        claims.append(status_equal(f"baseline_registry_contains:{baseline}", baseline in registry_baselines, True))
        claims.append(status_equal(
            f"baseline_registry_best_count:{baseline}",
            registry_best_counts.get(baseline, 0),
            dominance_best_counts.get(baseline, 0),
        ))
        claims.append(status_equal(
            f"baseline_registry_table_mentions:{baseline}",
            baseline.replace("_", "\\_") in registry_tex,
            True,
        ))
    claims.append(status_equal("experiments_inputs_baseline_family_screen_table", "\\input{tables/table_trace_biopt_baseline_family_screen}" in exp_tex, True))
    claims.append(status_equal("baseline_family_screen_row_count", len(baseline_family_screen_csv), 11))
    baseline_family_lookup = {row["family"]: row for row in baseline_family_screen_csv}
    claims.append(status_equal(
        "baseline_family_screen_families",
        set(baseline_family_lookup),
        {
            "Coverage / observability",
            "Exchange-refined baseline",
            "Graph heuristic",
            "Graph signal processing",
            "Optimal-design surrogate",
            "Prior TRACE-SL / RCSS",
            "Random / validation-selected",
            "Robust coverage",
            "Scenario-risk surrogate",
            "Simple traffic heuristic",
            "Sparse modal placement",
        },
    ))
    claims.append(status_equal(
        "baseline_family_screen_total_baselines",
        sum(int(row["baseline_count"]) for row in baseline_family_screen_csv),
        21,
    ))
    claims.append(status_equal(
        "baseline_family_screen_total_tests",
        sum(int(row["comparison_count"]) for row in baseline_family_screen_csv),
        189,
    ))
    claims.append(status_equal(
        "baseline_family_screen_all_zero_survivors",
        {int(row["surviving_challengers"]) for row in baseline_family_screen_csv},
        {0},
    ))
    claims.append(status_equal(
        "baseline_family_screen_prior_trace_family",
        (
            int(baseline_family_lookup["Prior TRACE-SL / RCSS"]["baseline_count"]),
            int(baseline_family_lookup["Prior TRACE-SL / RCSS"]["strongest_mean_rows"]),
            int(baseline_family_lookup["Prior TRACE-SL / RCSS"]["hardest_corrected_rows"]),
        ),
        (3, 8, 7),
    ))
    claims.append(status_round(
        "baseline_family_screen_prior_trace_closest_delta",
        float(baseline_family_lookup["Prior TRACE-SL / RCSS"]["closest_mean_delta"]),
        -0.0375414801864488,
        ".4f",
    ))
    claims.append(status_equal(
        "baseline_family_screen_exchange_refined_rows",
        (
            int(baseline_family_lookup["Exchange-refined baseline"]["baseline_count"]),
            int(baseline_family_lookup["Exchange-refined baseline"]["strongest_mean_rows"]),
            int(baseline_family_lookup["Exchange-refined baseline"]["hardest_corrected_rows"]),
        ),
        (4, 1, 0),
    ))
    claims.append(status_equal(
        "baseline_family_screen_single_hardest_families",
        {
            family for family, row in baseline_family_lookup.items()
            if int(row["hardest_corrected_rows"]) == 1
        },
        {"Scenario-risk surrogate", "Simple traffic heuristic"},
    ))
    baseline_family_screen_needles = [
        "The 21 pre-registered baselines span 11 families",
        "prior TRACE-SL / RCSS family",
        "8/9 strongest-mean challengers and 7/9 hardest corrected challengers",
        "zero surviving challenger after Holm correction",
        "scenario-risk and simple-heuristic families appear once each as the hardest corrected family",
    ]
    for needle in baseline_family_screen_needles:
        claims.append(status_equal(f"baseline_family_screen_text:{needle}", needle in normalized_exp_tex, True))
    baseline_family_screen_table_needles = [
        "Family-level screen of the pre-registered non-BiOpt comparison class",
        "Prior TRACE-SL / RCSS",
        "Exchange-refined baseline",
        "Closest $\\Delta$",
        "Largest\\\\Holm $p$",
        "8/9 strongest-mean challengers and 7/9 hardest corrected challengers",
    ]
    for needle in baseline_family_screen_table_needles:
        claims.append(status_equal(f"baseline_family_screen_table:{needle}", needle in baseline_family_screen_tex, True))

    claims.append(status_equal("full_matrix_row_count", len(full_matrix_csv), 66))
    claims.append(status_equal("full_matrix_dataset_count", {row["dataset"] for row in full_matrix_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    for dataset in {"PeMS7_1026", "PeMS7_228", "Seattle"}:
        dataset_rows = [row for row in full_matrix_csv if row["dataset"] == dataset]
        claims.append(status_equal(f"full_matrix_layout_count:{dataset}", len(dataset_rows), 22))
        trace_row = next(row for row in dataset_rows if row["layout_type"] == "trace_biopt")
        claims.append(status_equal(f"full_matrix_trace_rank_10:{dataset}", int(trace_row["rank_10"]), 1))
        claims.append(status_equal(f"full_matrix_trace_rank_20:{dataset}", int(trace_row["rank_20"]), 1))
        claims.append(status_equal(f"full_matrix_trace_rank_30:{dataset}", int(trace_row["rank_30"]), 1))
        claims.append(status_equal(f"full_matrix_trace_avg_rank:{dataset}", float(trace_row["avg_rank"]), 1.0))
    full_matrix_needles = [
        "TRACE-BiOpt ranks first on every dataset-budget row",
        "PeMS7\\_1026",
        "PeMS7\\_228",
        "Seattle",
        "\\textbf{trace\\_biopt}",
    ]
    for needle in full_matrix_needles:
        claims.append(status_equal(f"full_matrix_table_mentions:{needle}", needle in full_matrix_tex, True))

    claims.append(status_equal("experiments_inputs_full_baseline_heatmap_figure", "\\includegraphics[width=0.98\\linewidth]{figures/fig_trace_biopt_full_baseline_heatmap.pdf}" in exp_tex, True))
    claims.append(status_equal("full_baseline_heatmap_row_count", len(full_baseline_heatmap_csv), 198))
    claims.append(status_equal("full_baseline_heatmap_datasets", {row["dataset"] for row in full_baseline_heatmap_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    claims.append(status_equal("full_baseline_heatmap_budget_labels", {row["budget_pct"] for row in full_baseline_heatmap_csv}, {"10", "20", "30"}))
    claims.append(status_equal("full_baseline_heatmap_nonnegative_gaps", all(float(row["trace_gap"]) >= -1e-12 for row in full_baseline_heatmap_csv), True))
    for dataset in {"PeMS7_1026", "PeMS7_228", "Seattle"}:
        trace_rows = [row for row in full_baseline_heatmap_csv if row["dataset"] == dataset and row["layout_type"] == "trace_biopt"]
        claims.append(status_equal(f"full_baseline_heatmap_trace_rows:{dataset}", len(trace_rows), 3))
        claims.append(status_equal(f"full_baseline_heatmap_trace_rank1:{dataset}", {int(row['rank']) for row in trace_rows}, {1}))
    full_baseline_heatmap_needles = [
        "22-method baseline heatmap",
        "Every non-TRACE-BiOpt cell remains nonnegative",
        "highlighted TRACE-BiOpt row remains rank 1 everywhere",
        "not a selective pairing against one convenient comparator",
    ]
    for needle in full_baseline_heatmap_needles:
        claims.append(status_equal(f"full_baseline_heatmap_text:{needle}", needle in normalized_exp_tex, True))

    claims.append(status_equal("experiments_inputs_current_best_performance_curves_figure", "\\includegraphics[width=0.98\\linewidth]{figures/fig_trace_biopt_current_best_curves.pdf}" in exp_tex, True))
    claims.append(status_equal("experiments_mentions_performance_curves", "\\subsection{Performance curves}" in exp_tex, True))
    claims.append(status_equal("performance_curves_row_count", len(performance_curves_csv), 9))
    claims.append(status_equal("performance_curves_datasets", {row["dataset"] for row in performance_curves_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    claims.append(status_equal("performance_curves_best_baseline_labels", {row["best_baseline_label"] for row in performance_curves_csv}, {"Prev. TRACE-SL", "RCSS", "Swap from A-trace"}))
    for row in performance_curves_csv:
        key = (row["dataset"], float(row["budget"]))
        delta_row = delta[key]
        label = f"{row['dataset']}-{row['budget_pct']}pct"
        claims.append(status_equal(f"performance_curves_budget_pct:{label}", int(row["budget_pct"]), int(round(float(row["budget"]) * 100))))
        claims.append(status_round(f"performance_curves_trace_mean:{label}", float(row["trace_biopt_mean"]), float(delta_row["trace_biopt_mean"]), ".10f"))
        claims.append(status_round(f"performance_curves_best_mean:{label}", float(row["best_baseline_mean"]), float(delta_row["best_baseline_mean"]), ".10f"))
        claims.append(status_equal(f"performance_curves_best_layout:{label}", row["best_baseline_layout"], delta_row["best_baseline_layout"]))
        claims.append(status_equal(f"performance_curves_evidence_source:{label}", row["evidence_source"], delta_row["evidence_source"]))
    performance_curve_needles = [
        "TRACE-BiOpt stays below",
        "row-specific strongest pre-registered non-BiOpt comparator",
        "search- and calibration-sensitive",
    ]
    for needle in performance_curve_needles:
        claims.append(status_equal(f"performance_curves_text:{needle}", needle in normalized_exp_tex, True))

    claims.append(status_equal("experiments_inputs_paired_margins_figure", "\\includegraphics[width=0.98\\linewidth]{figures/fig_trace_biopt_paired_margins.pdf}" in exp_tex, True))
    claims.append(status_equal("experiments_mentions_paired_margins", "\\subsection{Paired margins}" in exp_tex, True))
    claims.append(status_equal("paired_margin_points_row_count", len(paired_margin_points_csv), 90))
    claims.append(status_equal("paired_margin_summary_row_count", len(paired_margin_summary_csv), 9))
    claims.append(status_equal("paired_margin_all_negative", all(float(row["paired_margin"]) < 0.0 for row in paired_margin_points_csv), True))
    claims.append(status_equal(
        "paired_margin_source_labels",
        Counter(row["source_label"] for row in paired_margin_summary_csv),
        Counter({"Stage15 main evidence": stage15_rows, "Stage16 calibrated rerun": stage16_rows}),
    ))
    paired_margin_lookup = {
        (row["dataset"], float(row["budget"])): row
        for row in paired_margin_summary_csv
    }
    narrowest_margin_row = min(
        paired_margin_lookup.items(),
        key=lambda item: abs(float(item[1]["mean_paired_margin"])),
    )[0]
    largest_mean_margin_row = min(
        paired_margin_lookup.items(),
        key=lambda item: float(item[1]["mean_paired_margin"]),
    )[0]
    claims.append(status_equal("paired_margin_narrowest_row", narrowest_margin_row, ("PeMS7_1026", 0.3)))
    claims.append(status_equal("paired_margin_largest_mean_row", largest_mean_margin_row, ("PeMS7_228", 0.3)))
    pems228_mid_high = [
        row for row in paired_margin_summary_csv
        if row["dataset"] == "PeMS7_228" and float(row["budget"]) in {0.2, 0.3}
    ]
    claims.append(status_equal(
        "paired_margin_pems228_mid_high_baseline",
        {row["best_baseline_layout"] for row in pems228_mid_high},
        {"validation_swap_selected"},
    ))
    claims.append(status_equal(
        "paired_margin_pems228_mid_high_all_wins",
        all(int(row["win_count"]) == int(row["count"]) for row in pems228_mid_high),
        True,
    ))
    paired_margin_needles = [
        "Every one of the 90 current-best seed-level paired margins is below zero",
        "PeMS7\\_1026 at 30\\%",
        "largest mean paired margin now appears on PeMS7\\_228 at 30\\%",
        "mid/high-budget PeMS7\\_228 rows remain below the previous TRACE-SL swap family on every split",
    ]
    for needle in paired_margin_needles:
        claims.append(status_equal(f"paired_margin_text:{needle}", needle in normalized_exp_tex, True))

    claims.append(status_equal("experiments_inputs_significance_posture_table", "\\input{tables/table_trace_biopt_significance_posture}" in exp_tex, True))
    claims.append(status_equal("experiments_mentions_all_baseline_significance_posture", "\\subsection{All-baseline significance posture}" in exp_tex, True))
    claims.append(status_equal("significance_posture_summary_row_count", len(significance_posture_summary_csv), 10))
    claims.append(status_equal("significance_posture_detail_row_count", len(significance_posture_detail_csv), 189))
    row_level_significance = [row for row in significance_posture_summary_csv if row["dataset"] != "All rows"]
    claims.append(status_equal(
        "significance_posture_all_row_counts_are_21_of_21",
        {(int(row["significantly_worse_baselines_holm"]), int(row["baseline_count"])) for row in row_level_significance},
        {(21, 21)},
    ))
    claims.append(status_equal(
        "significance_posture_all_row_non_worse_zero",
        {int(row["non_worse_baselines_holm"]) for row in row_level_significance},
        {0},
    ))
    claims.append(status_equal(
        "significance_posture_all_row_better_zero",
        {int(row["baseline_significantly_better_holm"]) for row in row_level_significance},
        {0},
    ))
    aggregate_significance_row = next(row for row in significance_posture_summary_csv if row["dataset"] == "All rows")
    claims.append(status_equal("significance_posture_aggregate_worse_count", int(aggregate_significance_row["significantly_worse_baselines_holm"]), 189))
    claims.append(status_equal("significance_posture_aggregate_non_worse_count", int(aggregate_significance_row["non_worse_baselines_holm"]), 0))
    claims.append(status_equal("significance_posture_aggregate_better_count", int(aggregate_significance_row["baseline_significantly_better_holm"]), 0))
    claims.append(status_equal("significance_posture_aggregate_closest_challenger", aggregate_significance_row["closest_challenger_layout"], "multistart_swap_by_validation"))
    claims.append(status_round("significance_posture_aggregate_max_holm_p", float(aggregate_significance_row["max_paired_t_p_holm"]), 0.002617011842110027, ".4f"))
    claims.append(status_round("significance_posture_aggregate_max_wilcoxon_p", float(aggregate_significance_row["max_wilcoxon_p_less"]), 0.0048828125, ".4f"))
    claims.append(status_equal(
        "significance_posture_detail_all_trace_better_holm",
        all(row["trace_significantly_better_holm"] == "True" for row in significance_posture_detail_csv),
        True,
    ))
    claims.append(status_equal(
        "significance_posture_detail_all_baseline_better_false",
        all(row["baseline_significantly_better_holm"] == "False" for row in significance_posture_detail_csv),
        True,
    ))
    significance_posture_needles = [
        "Holm familywise correction over all 189 current-best row-baseline comparisons",
        "every registered baseline still remains significantly worse than TRACE-BiOpt",
        "no row retains a statistically tied or significantly better challenger after multiplicity correction",
        "Seattle at 10\\%",
        "multistart validation-swap baseline still trails by 0.0557 MAE",
        "raw one-sided Wilcoxon $p$ value stays below 0.005 on all 189 comparisons",
    ]
    for needle in significance_posture_needles:
        claims.append(status_equal(f"significance_posture_text:{needle}", needle in normalized_exp_tex, True))

    claims.append(status_equal("experiments_inputs_challenger_posture_table", "\\input{tables/table_trace_biopt_challenger_posture}" in exp_tex, True))
    claims.append(status_equal("challenger_posture_row_count", len(challenger_posture_csv), 9))
    challenger_posture_lookup = {
        (row["dataset"], int(float(row["budget_pct"]))): row
        for row in challenger_posture_csv
    }
    claims.append(status_equal(
        "challenger_posture_mismatch_count",
        sum(row["same_family"] == "No" for row in challenger_posture_csv),
        6,
    ))
    claims.append(status_equal(
        "challenger_posture_pems1026_10",
        (
            challenger_posture_lookup[("PeMS7_1026", 10)]["strongest_mean_challenger"],
            challenger_posture_lookup[("PeMS7_1026", 10)]["hardest_corrected_challenger"],
            challenger_posture_lookup[("PeMS7_1026", 10)]["same_family"],
        ),
        ("Swap from A-trace", "Prev. TRACE-SL", "No"),
    ))
    claims.append(status_equal(
        "challenger_posture_seattle_10",
        (
            challenger_posture_lookup[("Seattle", 10)]["strongest_mean_challenger"],
            challenger_posture_lookup[("Seattle", 10)]["hardest_corrected_challenger"],
            challenger_posture_lookup[("Seattle", 10)]["same_family"],
        ),
        ("RCSS", "Multistart validation-swap", "No"),
    ))
    claims.append(status_equal(
        "challenger_posture_same_family_rows",
        {
            key for key, row in challenger_posture_lookup.items()
            if row["same_family"] == "Yes"
        },
        {("PeMS7_1026", 30), ("Seattle", 20), ("Seattle", 30)},
    ))
    challenger_posture_needles = [
        "On 6/9 current-best rows, the strongest mean challenger and the hardest challenger after Holm correction come from different baseline families",
        "PeMS7\\_1026 at 10\\% is closest in mean MAE to Swap from A-trace but hardest after correction against the previous TRACE-SL route",
        "Seattle at 10\\% is closest in mean MAE to RCSS but hardest after correction against Multistart validation-swap",
        "no single baseline family remains the unique near-miss once both mean ranking and multiplicity-corrected paired inference are made explicit",
    ]
    for needle in challenger_posture_needles:
        claims.append(status_equal(f"challenger_posture_text:{needle}", needle in normalized_exp_tex, True))
    challenger_posture_table_needles = [
        "Strongest mean\\\\challenger",
        "Hardest corrected\\\\challenger",
        "Same family?",
        "Across 6/9 current-best rows",
        "Swap from A-trace versus Prev. TRACE-SL",
        "RCSS versus Multistart validation-swap",
    ]
    for needle in challenger_posture_table_needles:
        claims.append(status_equal(f"challenger_posture_table:{needle}", needle in challenger_posture_tex, True))

    claims.append(status_equal("experiments_inputs_comparison_ladder_table", "\\input{tables/table_trace_biopt_comparison_ladder}" in exp_tex, True))
    comparison_ladder_lookup = {row["ladder_step"]: row for row in comparison_ladder_csv}
    claims.append(status_equal("comparison_ladder_row_count", len(comparison_ladder_csv), 6))
    claims.append(status_equal(
        "comparison_ladder_steps",
        set(comparison_ladder_lookup),
        {
            "Registry scope",
            "Row-wise strongest challenger",
            "All-baseline corrected screen",
            "Family-level near misses",
            "Challenger diversity",
            "Explicit non-claim",
        },
    ))
    claims.append(status_equal(
        "comparison_ladder_registry_scope_counts",
        all(
            needle in comparison_ladder_lookup["Registry scope"]["paper_visible_statement"]
            for needle in ("21", "11", "audited method families")
        ),
        True,
    ))
    claims.append(status_equal(
        "comparison_ladder_rowwise_step_counts",
        all(
            needle in comparison_ladder_lookup["Row-wise strongest challenger"]["paper_visible_statement"]
            for needle in ("9/9", "8/9", "submission-ready paired-dominant")
        ),
        True,
    ))
    claims.append(status_equal(
        "comparison_ladder_corrected_screen_counts",
        all(
            needle in comparison_ladder_lookup["All-baseline corrected screen"]["paper_visible_statement"]
            for needle in ("189/189", "0 ties", "0 better challengers")
        ),
        True,
    ))
    claims.append(status_equal(
        "comparison_ladder_family_screen_counts",
        all(
            needle in comparison_ladder_lookup["Family-level near misses"]["paper_visible_statement"]
            for needle in ("8/9", "7/9", "-0.0375")
        ),
        True,
    ))
    claims.append(status_equal(
        "comparison_ladder_challenger_diversity_count",
        "6/9" in comparison_ladder_lookup["Challenger diversity"]["paper_visible_statement"],
        True,
    ))
    comparison_ladder_text_needles = [
        "compresses the whole empirical contract into one ladder",
        "first ask how broad the audited registry is",
        "then whether TRACE-BiOpt beats the row-wise strongest challenger",
        "then whether that result survives all-baseline correction",
        "multi-layer audited comparison-class contract with no surviving challenger",
    ]
    for needle in comparison_ladder_text_needles:
        claims.append(status_equal(f"comparison_ladder_text:{needle}", needle in normalized_exp_tex, True))
    comparison_ladder_table_needles = [
        "Audited comparison ladder for TRACE-BiOpt",
        "Registry scope",
        "Row-wise strongest challenger",
        "All-baseline corrected screen",
        "Family-level near misses",
        "Challenger diversity",
        "Explicit non-claim",
    ]
    for needle in comparison_ladder_table_needles:
        claims.append(status_equal(f"comparison_ladder_table:{needle}", needle in comparison_ladder_tex, True))

    claims.append(status_equal("regime_lessons_row_count", len(regime_lessons_csv), 9))
    expected_regime_labels = {
        "PeMS7_1026 10%",
        "PeMS7_1026 20%",
        "PeMS7_1026 30%",
        "PeMS7_228 10%",
        "PeMS7_228 20%",
        "PeMS7_228 30%",
        "Seattle 10%",
        "Seattle 20%",
        "Seattle 30%",
    }
    claims.append(status_equal("regime_lessons_labels", {row["regime"] for row in regime_lessons_csv}, expected_regime_labels))
    regime_needles = [
        "Stage16 calibrated rerun",
        "Stage15 main evidence",
        "search-budget sensitive",
        "searched-neighborhood stable",
        "RCSS selector",
        "A-trace swap family",
        "prior TRACE-SL swap family",
    ]
    for needle in regime_needles:
        claims.append(status_equal(f"regime_lessons_table_mentions:{needle}", needle in regime_lessons_tex, True))

    claims.append(status_equal("analysis_inputs_optimization_table", "\\input{tables/table_trace_biopt_optimization}" in analysis_tex, True))
    claims.append(status_equal("optimization_summary_row_count", len(optimization_csv), 9))
    claims.append(status_equal("optimization_detail_row_count", len(optimization_detail_csv), 90))
    claims.append(status_equal("optimization_all_rows_ten_runs", {int(row["runs"]) for row in optimization_csv}, {10}))
    claims.append(status_equal("optimization_all_detail_monotone", {row["objective_monotone"] for row in optimization_detail_csv}, {"True"}))
    claims.append(status_equal("optimization_text_mentions_90_runs", "90 dataset-budget-seed runs" in analysis_tex, True))
    claims.append(status_equal("optimization_detail_stop_reasons", {row["stop_reason"] for row in optimization_detail_csv}, {"exchange_budget_exhausted", "no_improving_one_exchange"}))
    optimization_text_needles = [
        "full $k(n-k)$ one-swap neighborhood",
        "no-improving searched exchange certificate",
        "exchange-iteration cap",
        "PeMS7\\_1026 rows remain the most search-budget-sensitive",
    ]
    for needle in optimization_text_needles:
        claims.append(status_equal(
            f"optimization_text:{needle}",
            needle in normalized_analysis_tex,
            True,
        ))
    for row in optimization_csv:
        label = f"{row['dataset']}-{int(float(row['budget']) * 100)}pct"
        table_needles = [
            row["dataset"].replace("_", "\\_"),
            f"{int(float(row['budget']) * 100)}\\%",
            f"{float(row['exchange_steps_mean']):.1f} [{int(row['exchange_steps_min'])},{int(row['exchange_steps_max'])}]",
            f"{float(row['searched_one_exchange_coverage_pct_mean']):.1f}\\%",
            f"{int(row['no_improving_stop_runs'])}/{int(row['exchange_budget_exhausted_runs'])}",
            f"{float(row['full_objective_drop_pct_mean']):.1f}\\%",
            f"{float(row['exchange_objective_drop_pct_mean']):.2f}\\%",
            f"{int(row['objective_monotone_runs'])}/{int(row['runs'])}",
        ]
        for needle in table_needles:
            claims.append(status_equal(f"optimization_table:{label}:{needle}", needle in optimization_tex, True))

    claims.append(status_equal("analysis_inputs_solver_scale_table", "\\input{tables/table_trace_biopt_solver_scale}" in analysis_tex, True))
    claims.append(status_equal("solver_scale_summary_row_count", len(solver_scale_summary_csv), 9))
    claims.append(status_equal("solver_scale_detail_row_count", len(solver_scale_detail_csv), 90))
    claims.append(status_equal("solver_scale_datasets", {row["dataset"] for row in solver_scale_summary_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    claims.append(status_equal("solver_scale_source_labels", {row["source_label"] for row in solver_scale_summary_csv}, {"Stage15 main evidence", "Stage16 calibrated rerun"}))
    claims.append(status_equal("solver_scale_initializers", {row["dominant_initializer"] for row in solver_scale_summary_csv}, {"objective_forward", "posterior_greedy_warm_start"}))
    claims.append(status_equal("solver_scale_stage16_rows", sum(row["source_label"] == "Stage16 calibrated rerun" for row in solver_scale_summary_csv), stage16_rows))
    claims.append(status_equal("solver_scale_stage15_rows", sum(row["source_label"] == "Stage15 main evidence" for row in solver_scale_summary_csv), stage15_rows))
    claims.append(status_equal("solver_scale_fullsearch_row_count", sum(float(row["searched_one_exchange_coverage_pct_mean"]) == 100.0 for row in solver_scale_summary_csv), 3))
    pems1026_20_peak_rss_gb = float(next(row for row in solver_scale_summary_csv if row["dataset"] == "PeMS7_1026" and float(row["budget"]) == 0.2)["peak_trace_rss_mb_mean"]) / 1024.0
    seattle_30_peak_rss_gb = float(next(row for row in solver_scale_summary_csv if row["dataset"] == "Seattle" and float(row["budget"]) == 0.3)["peak_trace_rss_mb_mean"]) / 1024.0
    claims.append(status_equal("solver_scale_pems1026_20_peak_rss_table", f"{pems1026_20_peak_rss_gb:.2f}" in solver_scale_tex, True))
    claims.append(status_equal("solver_scale_seattle_30_peak_rss_table", f"{seattle_30_peak_rss_gb:.2f}" in solver_scale_tex, True))
    solver_scale_needles = [
        "Current-best TRACE-BiOpt solver scale by dataset-budget row.",
        "zero-valued pools interpreted as complete enumeration",
        "current-best calibrated routes span roughly",
        "0.4--1.6\\,GB on PeMS7\\_228 and 1.4--2.9\\,GB on PeMS7\\_1026",
        "Seattle still stays below 0.5\\,GB",
    ]
    solver_scale_text = "\n".join(
        [
            solver_scale_tex,
            normalized_analysis_tex,
            *[
                f"{row['dataset']} {int(float(row['budget']) * 100)}% {row['source_label']} {row['dominant_initializer']}"
                for row in solver_scale_summary_csv
            ],
        ]
    )
    for needle in solver_scale_needles:
        claims.append(status_equal(f"solver_scale_text:{needle}", needle in solver_scale_text, True))

    claims.append(status_equal("analysis_inputs_initializer_posture_table", "\\input{tables/table_trace_biopt_initializer_posture}" in analysis_tex, True))
    claims.append(status_equal("initializer_posture_row_count", len(initializer_posture_csv), 3))
    init_lookup = {row["dataset"]: row for row in initializer_posture_csv}
    claims.append(status_equal("initializer_posture_datasets", set(init_lookup), {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    claims.append(status_equal("initializer_posture_pems1026_initializer", init_lookup["PeMS7_1026"]["initializer_family"], "posterior_greedy_warm_start"))
    claims.append(status_equal("initializer_posture_pems1026_stage_mode", init_lookup["PeMS7_1026"]["stage_mode"], "exchange_only_warm_start"))
    claims.append(status_equal("initializer_posture_pems228_initializer", init_lookup["PeMS7_228"]["initializer_family"], "objective_forward"))
    claims.append(status_equal("initializer_posture_pems228_stage_mode", init_lookup["PeMS7_228"]["stage_mode"], "forward_then_exchange"))
    claims.append(status_equal("initializer_posture_seattle_initializer", init_lookup["Seattle"]["initializer_family"], "objective_forward"))
    claims.append(status_equal("initializer_posture_seattle_stage_mode", init_lookup["Seattle"]["stage_mode"], "forward_then_exchange"))
    claims.append(status_equal("initializer_posture_pems228_fullsearch", init_lookup["PeMS7_228"]["searched_coverage_pct_range"], "100.0-100.0"))
    claims.append(status_equal("initializer_posture_pems1026_covered_rows", init_lookup["PeMS7_1026"]["covered_rows_pct"], "10/20/30%"))
    claims.append(status_equal("initializer_posture_seattle_source_mix", init_lookup["Seattle"]["source_mix"], "Stage15 main evidence, Stage16 calibrated rerun"))
    initializer_posture_needles = [
        "Reviewer-facing current-best TRACE-BiOpt initializer posture.",
        "size-adaptive solver family rather than as one opaque search trace",
        "posterior warm-start / exchange-only warm start",
        "objective-forward / forward then exchange",
        "PeMS7\\_1026",
        "PeMS7\\_228",
        "Seattle",
        "large-network warm-start regime",
        "mid-scale full-search regime",
        "light direct-construction regime",
    ]
    initializer_posture_text = "\n".join(
        [
            initializer_posture_tex,
            normalized_analysis_tex,
            *[
                f"{row['dataset']} {row['initializer_family']} {row['stage_mode']} {row['covered_rows_pct']}"
                for row in initializer_posture_csv
            ],
        ]
    )
    for needle in initializer_posture_needles:
        claims.append(status_equal(f"initializer_posture_text:{needle}", needle in initializer_posture_text, True))

    claims.append(status_equal("analysis_inputs_compute_posture_table", "\\input{tables/table_trace_biopt_compute_posture}" in analysis_tex, True))
    claims.append(status_equal("compute_posture_summary_row_count", len(compute_posture_csv), 6))
    claims.append(status_equal("compute_posture_detail_row_count", len(compute_posture_detail_csv), 60))
    compute_lookup = {row["route_label"]: row for row in compute_posture_csv}
    claims.append(status_equal(
        "compute_posture_routes",
        set(compute_lookup),
        {
            "PeMS7_1026 calibrated rerun (10/20%)",
            "PeMS7_1026 calibrated rerun (30%)",
            "PeMS7_228 calibrated rerun (10%)",
            "PeMS7_228 calibrated rerun (20/30%)",
            "Seattle Stage15 main route (10%)",
            "Seattle calibrated rerun (20/30%)",
        },
    ))
    expected_compute = {
        "PeMS7_1026 calibrated rerun (10/20%)": {
            "run_budget_count": "2",
            "source_scope": "paired-budget calibrated rerun",
            "wall_clock_minutes_mean": 136.31575551509857,
            "peak_rss_gb_mean": 2.7202060546875,
        },
        "PeMS7_1026 calibrated rerun (30%)": {
            "run_budget_count": "1",
            "source_scope": "single-budget calibrated rerun",
            "wall_clock_minutes_mean": 127.03638008912404,
            "peak_rss_gb_mean": 1.49202734375,
        },
        "PeMS7_228 calibrated rerun (10%)": {
            "run_budget_count": "1",
            "source_scope": "single-budget calibrated rerun",
            "wall_clock_minutes_mean": 119.10341806252798,
            "peak_rss_gb_mean": 0.399704296875,
        },
        "PeMS7_228 calibrated rerun (20/30%)": {
            "run_budget_count": "2",
            "source_scope": "paired-budget calibrated rerun",
            "wall_clock_minutes_mean": 98.95100625514985,
            "peak_rss_gb_mean": 1.4735943359374999,
        },
        "Seattle Stage15 main route (10%)": {
            "run_budget_count": "3",
            "source_scope": "all-budget main-evidence run",
            "wall_clock_minutes_mean": 2.2341266763210297,
            "peak_rss_gb_mean": 0.488381640625,
        },
        "Seattle calibrated rerun (20/30%)": {
            "run_budget_count": "3",
            "source_scope": "multi-budget calibrated rerun",
        },
    }
    for label, expected in expected_compute.items():
        row = compute_lookup[label]
        claims.append(status_equal(f"compute_posture_scope:{label}", row["source_scope"], expected["source_scope"]))
        claims.append(status_equal(f"compute_posture_budgets:{label}", row["run_budget_count"], expected["run_budget_count"]))
        claims.append(status_equal(f"compute_posture_table_wall_clock:{label}", f"{float(row['wall_clock_minutes_mean']):.1f}" in compute_posture_tex, True))
        claims.append(status_equal(f"compute_posture_table_peak_rss:{label}", f"{float(row['peak_rss_gb_mean']):.2f}" in compute_posture_tex, True))
    compute_posture_needles = [
        "Current-best TRACE-BiOpt compute posture by source route.",
        "current-best rerun chain is counted, the promoted PeMS routes are hour-scale rather than minute-scale",
        "paired PeMS7\\_1026 10/20\\% calibrated rerun now averages 136.4 minutes",
        "single-budget 30\\% rerun averages 127.1 minutes",
        "PeMS7\\_228 calibrated 10\\% and 20/30\\% routes average 119.2 and 99.0 minutes",
        "Seattle remains the light route family",
        "Seattle 20/30\\% calibrated rerun averages 6.5 minutes with a 0.47\\,GB mean peak",
    ]
    compute_posture_text = "\n".join([compute_posture_tex, normalized_analysis_tex])
    for needle in compute_posture_needles:
        claims.append(status_equal(f"compute_posture_text:{needle}", needle in compute_posture_text, True))

    exchange_certificate_tex = read(PAPER / "tables" / "table_trace_biopt_exchange_certificate.tex")
    claims.append(status_equal("analysis_inputs_exchange_certificate_table", "\\input{tables/table_trace_biopt_exchange_certificate}" in analysis_tex, True))
    claims.append(status_equal("exchange_certificate_row_count", len(exchange_certificate_csv), 9))
    claims.append(status_equal(
        "exchange_certificate_scopes",
        {row["certificate_scope"] for row in exchange_certificate_csv},
        {"complete one-exchange certificate", "mixed searched certificate", "searched active-set certificate", "budget-limited certificate"},
    ))
    complete_rows = [row for row in exchange_certificate_csv if row["certificate_scope"] == "complete one-exchange certificate"]
    claims.append(status_equal("exchange_certificate_complete_row_count", len(complete_rows), 1))
    claims.append(status_equal(
        "exchange_certificate_complete_row_label",
        {(row["dataset"], row["budget_pct"]) for row in complete_rows},
        {("PeMS7_228", "10")},
    ))
    claims.append(status_equal(
        "exchange_certificate_budget_limited_rows",
        {(row["dataset"], row["budget_pct"]) for row in exchange_certificate_csv if row["certificate_scope"] == "budget-limited certificate"},
        {("PeMS7_1026", "20"), ("PeMS7_1026", "30")},
    ))
    claims.append(status_equal(
        "exchange_certificate_seattle30_scope",
        next(row["certificate_scope"] for row in exchange_certificate_csv if row["dataset"] == "Seattle" and row["budget_pct"] == "30"),
        "searched active-set certificate",
    ))
    exchange_certificate_needles = [
        "cleanest certificate row",
        "complete one-exchange neighborhood",
        "$G_1(\\hat{\\calS})=0$ specialization",
        "$G^{\\mathrm{search}}_1(\\hat{\\calS})=0$ on the searched active set",
        "no zero-gap certificate is available there",
        "searched-active-set stationarity",
        "search-budget-sensitive rather than as contradiction rows",
    ]
    for needle in exchange_certificate_needles:
        claims.append(status_equal(f"exchange_certificate_text:{needle}", needle in normalized_analysis_tex, True))
    exchange_certificate_table_needles = [
        "Current-best TRACE-BiOpt exchange-gap certificate posture by dataset-budget row.",
        "complete one-exchange certificate",
        "mixed searched certificate",
        "budget-limited certificate",
        "searched active-set certificate",
        "A complete one-exchange certificate means $G_1(\\hat{\\calS})=0$ up to tolerance",
        "only $G^{\\mathrm{search}}_1(\\hat{\\calS})=0$ on the evaluated active set",
        "does not carry a zero-gap certificate",
    ]
    for needle in exchange_certificate_table_needles:
        claims.append(status_equal(f"exchange_certificate_table:{needle}", needle in exchange_certificate_tex, True))
    method_tex = read(PAPER / "sections" / "4_method_theory.tex")
    claims.append(status_equal(
        "method_mentions_exchange_gap_scope_proposition",
        all(
            needle in method_tex
            for needle in (
                "\\begin{proposition}[Gap-certified interpretation of stopping scopes]",
                "G_1(\\calS)=J(\\calS)-\\min_{\\calS'\\in\\mathcal{N}_1(\\calS)}J(\\calS')",
                "G^{\\mathrm{search}}_1(\\hat{\\calS})=0",
                "this strengthens to",
                "no zero-gap certificate is implied",
            )
        ),
        True,
    ))

    claims.append(status_equal("analysis_inputs_objective_descent_figure", "\\includegraphics[width=0.98\\linewidth]{figures/fig_trace_biopt_objective_descent.pdf}" in analysis_tex, True))
    claims.append(status_equal("objective_descent_summary_row_count", len(objective_descent_summary_csv), 9))
    claims.append(status_equal("objective_descent_curve_row_count", len(objective_descent_curves_csv), 1890))
    claims.append(status_equal("objective_descent_datasets", {row["dataset"] for row in objective_descent_summary_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    claims.append(status_equal("objective_descent_source_labels", {row["source_label"] for row in objective_descent_summary_csv}, {"Stage15 main evidence", "Stage16 calibrated rerun"}))
    claims.append(status_equal("objective_descent_stage_modes", Counter(row["dominant_stage_mode"] for row in objective_descent_summary_csv), Counter({"forward_then_exchange": 6, "exchange_only_warm_start": 3})))
    claims.append(status_equal("objective_descent_progress_grid", {row["progress_fraction"] for row in objective_descent_curves_csv}, {f"{index / 20:.2f}" for index in range(21)}))
    claims.append(status_equal(
        "objective_descent_norm_gap_bounds",
        (
            min(float(row["normalized_gap"]) for row in objective_descent_curves_csv) >= 0.0,
            max(float(row["normalized_gap"]) for row in objective_descent_curves_csv) <= 1.0,
        ),
        (True, True),
    ))
    objective_descent_lookup = {
        (row["dataset"], float(row["budget"])): row
        for row in objective_descent_summary_csv
    }
    claims.append(status_round(
        "objective_descent_pems1026_20_exchange_steps",
        float(objective_descent_lookup[("PeMS7_1026", 0.2)]["mean_exchange_steps"]),
        20.0,
        ".1f",
    ))
    claims.append(status_round(
        "objective_descent_pems228_30_total_drop_pct",
        float(objective_descent_lookup[("PeMS7_228", 0.3)]["mean_total_drop_pct"]),
        67.748765,
        ".1f",
    ))
    claims.append(status_round(
        "objective_descent_seattle_10_exchange_share_pct",
        float(objective_descent_lookup[("Seattle", 0.1)]["mean_exchange_share_pct"]),
        0.646458,
        ".1f",
    ))
    objective_descent_needles = [
        "54--72\\% of the recorded objective",
        "0.2--1.1\\% of the recorded drop",
        "exchange-only warm-start mode",
        "8--20 accepted exchange steps",
        "stronger warm start plus a visibly longer exchange tail",
    ]
    for needle in objective_descent_needles:
        claims.append(status_equal(f"objective_descent_text:{needle}", needle in normalized_analysis_tex, True))

    claims.append(status_equal("analysis_inputs_exchange_gap_figure", "\\includegraphics[width=0.98\\linewidth]{figures/fig_trace_biopt_exchange_gap_curves.pdf}" in analysis_tex, True))
    claims.append(status_equal("exchange_gap_summary_row_count", len(exchange_gap_summary_csv), 9))
    claims.append(status_equal("exchange_gap_curve_row_count", len(exchange_gap_curves_csv), 1827))
    claims.append(status_equal("exchange_gap_datasets", {row["dataset"] for row in exchange_gap_summary_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    claims.append(status_equal("exchange_gap_source_labels", {row["source_label"] for row in exchange_gap_summary_csv}, {"Stage15 main evidence", "Stage16 calibrated rerun"}))
    claims.append(status_equal("exchange_gap_progress_grid", {row["progress_fraction"] for row in exchange_gap_curves_csv}, {f"{index / 20:.2f}" for index in range(21)}))
    claims.append(status_equal(
        "exchange_gap_bounds",
        (
            min(float(row["residual_exchange_gap"]) for row in exchange_gap_curves_csv) >= 0.0,
            max(float(row["residual_exchange_gap"]) for row in exchange_gap_curves_csv) <= 1.0,
        ),
        (True, True),
    ))
    exchange_gap_lookup = {
        (row["dataset"], float(row["budget"])): row
        for row in exchange_gap_summary_csv
    }
    claims.append(status_round(
        "exchange_gap_pems1026_20_midpoint",
        float(exchange_gap_lookup[("PeMS7_1026", 0.2)]["mean_residual_gap_50pct"]),
        0.3215451480686568,
        ".6f",
    ))
    claims.append(status_round(
        "exchange_gap_pems1026_30_midpoint",
        float(exchange_gap_lookup[("PeMS7_1026", 0.3)]["mean_residual_gap_50pct"]),
        0.4373806882041167,
        ".6f",
    ))
    claims.append(status_round(
        "exchange_gap_pems228_10_midpoint",
        float(exchange_gap_lookup[("PeMS7_228", 0.1)]["mean_residual_gap_50pct"]),
        0.26053652310210806,
        ".6f",
    ))
    claims.append(status_round(
        "exchange_gap_pems1026_20_steps",
        float(exchange_gap_lookup[("PeMS7_1026", 0.2)]["mean_exchange_steps"]),
        20.0,
        ".1f",
    ))
    claims.append(status_round(
        "exchange_gap_pems1026_30_steps",
        float(exchange_gap_lookup[("PeMS7_1026", 0.3)]["mean_exchange_steps"]),
        8.0,
        ".1f",
    ))
    claims.append(status_round(
        "exchange_gap_pems228_10_steps",
        float(exchange_gap_lookup[("PeMS7_228", 0.1)]["mean_exchange_steps"]),
        7.1,
        ".1f",
    ))
    claims.append(status_equal(
        "exchange_gap_zero_exchange_rows",
        {
            (row["dataset"], row["budget_pct"], row["zero_exchange_runs"])
            for row in exchange_gap_summary_csv
            if int(row["zero_exchange_runs"]) > 0
        },
        {
            ("Seattle", "10", "1"),
            ("Seattle", "20", "1"),
            ("Seattle", "30", "1"),
        },
    ))
    exchange_gap_needles = [
        "isolates the accepted exchange phase itself",
        "about 0.322 of the eventual exchange improvement still remains on",
        "about 0.437 still remains on PeMS7\\_1026 30\\%",
        "mean residual exchange gap is down to 0.261 with 7.1 accepted swaps",
        "their midpoint residual gaps are about 0.220 and 0.232",
        "Only Seattle 10/30\\% still show zero-exchange runs",
        "exchange phase often becomes optional rather than binding",
    ]
    for needle in exchange_gap_needles:
        claims.append(status_equal(f"exchange_gap_text:{needle}", needle in normalized_analysis_tex, True))

    claims.append(status_equal("analysis_inputs_certificate_removal_probe_table", "\\input{tables/table_trace_biopt_certificate_removal_probe}" in analysis_tex, True))
    claims.append(status_equal("certificate_removal_probe_row_count", len(certificate_removal_probe_csv), 2))
    claims.append(status_equal("certificate_removal_probe_datasets", {row["dataset"] for row in certificate_removal_probe_csv}, {"Seattle"}))
    claims.append(status_equal("certificate_removal_probe_budgets", {int(row["budget_pct"]) for row in certificate_removal_probe_csv}, {20, 30}))
    claims.append(status_equal("certificate_removal_probe_route_labels", {row["probe_route_label"] for row in certificate_removal_probe_csv}, {"Zero-weight strong-search probe"}))
    certificate_probe_lookup = {
        int(row["budget_pct"]): row
        for row in certificate_removal_probe_csv
    }
    claims.append(status_round(
        "certificate_removal_probe_20_test_delta",
        float(certificate_probe_lookup[20]["test_probe_minus_default"]),
        0.03570629073603593,
        ".3f",
    ))
    claims.append(status_round(
        "certificate_removal_probe_30_test_delta",
        float(certificate_probe_lookup[30]["test_probe_minus_default"]),
        0.03203269605310677,
        ".3f",
    ))
    certificate_probe_needles = [
        "Seattle 20\\% and 30\\%",
        "0.032--0.036 MAE",
        "0.013--0.022 MAE",
        "not explained by search depth alone",
    ]
    for needle in certificate_probe_needles:
        claims.append(status_equal(f"certificate_removal_probe_text:{needle}", needle in normalized_analysis_tex, True))
    table_needles = [
        "Single-seed certificate-removal probe on stable Seattle diagnostic slices.",
        "2.957",
        "2.970",
        "2.488",
        "+0.032",
    ]
    for needle in table_needles:
        claims.append(status_equal(f"certificate_removal_probe_table:{needle}", needle in certificate_removal_probe_tex, True))

    claims.append(status_equal("analysis_inputs_objective_mix_figure", "\\includegraphics[width=0.98\\linewidth]{figures/fig_trace_biopt_objective_mix.pdf}" in analysis_tex, True))
    claims.append(status_equal("objective_mix_summary_row_count", len(objective_mix_summary_csv), 9))
    claims.append(status_equal("objective_mix_datasets", {row["dataset"] for row in objective_mix_summary_csv}, {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    objective_mix_lookup = {
        (row["dataset"], int(row["budget_pct"])): row
        for row in objective_mix_summary_csv
    }
    claims.append(status_round(
        "objective_mix_seattle20_posterior_share",
        float(objective_mix_lookup[("Seattle", 20)]["posterior_share_pct"]),
        63.105871,
        ".1f",
    ))
    claims.append(status_round(
        "objective_mix_seattle30_recon_share",
        float(objective_mix_lookup[("Seattle", 30)]["reconstruction_share_pct"]),
        34.782266,
        ".1f",
    ))
    claims.append(status_round(
        "objective_mix_pems1026_10_recon_share",
        float(objective_mix_lookup[("PeMS7_1026", 10)]["reconstruction_share_pct"]),
        83.595440,
        ".1f",
    ))
    claims.append(status_round(
        "objective_mix_pems228_20_posterior_share",
        float(objective_mix_lookup[("PeMS7_228", 20)]["posterior_share_pct"]),
        18.373836,
        ".1f",
    ))
    objective_mix_needles = [
        "81--87\\%",
        "13--19\\%",
        "61--64\\%",
        "35--37\\%",
        "posterior-driven",
    ]
    for needle in objective_mix_needles:
        claims.append(status_equal(f"objective_mix_text:{needle}", needle in normalized_analysis_tex, True))

    claims.append(status_equal("analysis_inputs_weight_sensitivity_table", "\\input{tables/table_trace_biopt_weight_sensitivity}" in analysis_tex, True))
    claims.append(status_equal("weight_sensitivity_row_count", len(weight_sensitivity_csv), 7))
    claims.append(status_equal("weight_sensitivity_case_labels", {row["case_label"] for row in weight_sensitivity_csv}, {"Seattle 20\\%", "Seattle 30\\%", "PeMS7\\_228 10\\%"}))
    claims.append(status_equal("weight_sensitivity_risk_sources", {row["risk_source"] for row in weight_sensitivity_csv}, {"val", "train_val"}))
    weight_lookup = {
        (row["case_label"], row["route_label"]): row
        for row in weight_sensitivity_csv
    }
    claims.append(status_round(
        "weight_sensitivity_seattle20_current_test",
        float(weight_lookup[("Seattle 20\\%", "Seattle diagnostic certified")]["test_mae"]),
        2.6743456218827726,
        ".3f",
    ))
    claims.append(status_round(
        "weight_sensitivity_seattle20_zero_delta",
        float(weight_lookup[("Seattle 20\\%", "Zero-weight probe")]["test_delta_vs_case_best"]),
        0.03570629073603593,
        ".3f",
    ))
    claims.append(status_round(
        "weight_sensitivity_seattle30_zero_delta",
        float(weight_lookup[("Seattle 30\\%", "Zero-weight probe")]["test_delta_vs_case_best"]),
        0.03203269605310677,
        ".3f",
    ))
    claims.append(status_round(
        "weight_sensitivity_pems22810_calibrated_test",
        float(weight_lookup[("PeMS7\\_228 10\\%", "Calibrated low-cert")]["test_mae"]),
        3.24844189706894,
        ".3f",
    ))
    claims.append(status_round(
        "weight_sensitivity_pems22810_default_delta",
        float(weight_lookup[("PeMS7\\_228 10\\%", "Stage15 certified")]["test_delta_vs_case_best"]),
        0.12905606497860916,
        ".3f",
    ))
    claims.append(status_round(
        "weight_sensitivity_pems22810_zero_delta",
        float(weight_lookup[("PeMS7\\_228 10\\%", "Zero-weight probe")]["test_delta_vs_case_best"]),
        0.16905731573641775,
        ".3f",
    ))
    weight_sensitivity_needles = [
        "0.036 and 0.032 MAE",
        "held-out MAE to 3.248 from 3.377",
        "3.417 for the zero-weight route",
        "regime sensitivity",
        "not a universal monotonic statement",
    ]
    for needle in weight_sensitivity_needles:
        claims.append(status_equal(f"weight_sensitivity_text:{needle}", needle in normalized_analysis_tex, True))
    weight_table_needles = [
        "Regime-specific TRACE-BiOpt objective-weight sensitivity slices",
        "Seattle 20\\%",
        "PeMS7\\_228 10\\%",
        "train+val",
        "+0.129",
        "+0.169",
    ]
    for needle in weight_table_needles:
        claims.append(status_equal(f"weight_sensitivity_table:{needle}", needle in weight_sensitivity_tex, True))

    claims.append(status_equal("analysis_inputs_tail_risk_posture_table", "\\input{tables/table_trace_biopt_tail_risk_posture}" in analysis_tex, True))
    claims.append(status_equal("tail_risk_posture_row_count", len(tail_risk_posture_csv), 3))
    tail_lookup = {
        row["case_label"]: row
        for row in tail_risk_posture_csv
    }
    claims.append(status_round(
        "tail_risk_posture_seattle20_cvar_share",
        float(tail_lookup["Seattle 20\\%"]["current_cvar_share_pct"]),
        1.457364,
        ".2f",
    ))
    claims.append(status_round(
        "tail_risk_posture_seattle30_cvar_share",
        float(tail_lookup["Seattle 30\\%"]["current_cvar_share_pct"]),
        1.427718,
        ".2f",
    ))
    claims.append(status_round(
        "tail_risk_posture_pems22810_cvar_share",
        float(tail_lookup["PeMS7\\_228 10\\%"]["current_cvar_share_pct"]),
        0.260095,
        ".2f",
    ))
    claims.append(status_equal(
        "tail_risk_posture_seattle20_comparator_text",
        "0.036 MAE" in tail_lookup["Seattle 20\\%"]["comparator_summary"],
        True,
    ))
    claims.append(status_equal(
        "tail_risk_posture_seattle30_comparator_text",
        "0.032 MAE" in tail_lookup["Seattle 30\\%"]["comparator_summary"],
        True,
    ))
    claims.append(status_equal(
        "tail_risk_posture_pems22810_comparator_text",
        ("0.169 MAE" in tail_lookup["PeMS7\\_228 10\\%"]["comparator_summary"]) and ("0.129 MAE" in tail_lookup["PeMS7\\_228 10\\%"]["comparator_summary"]),
        True,
    ))
    tail_risk_needles = [
        "1.37--1.40\\%",
        "0.26\\%",
        "0.036 and 0.032",
        "bounded and regime-calibrated",
        "not ``larger CVaR is always better,''",
    ]
    for needle in tail_risk_needles:
        claims.append(status_equal(f"tail_risk_posture_text:{needle}", needle in normalized_analysis_tex, True))
    tail_risk_table_needles = [
        "Reviewer-facing TRACE-BiOpt tail-risk posture slices",
        "Seattle 20\\%",
        "Zero-weight strong-search is worse by 0.036 MAE",
        "heavy-cert Stage15 is worse by 0.129 MAE",
    ]
    for needle in tail_risk_table_needles:
        claims.append(status_equal(f"tail_risk_posture_table:{needle}", needle in tail_risk_posture_tex, True))

    claims.append(status_equal("analysis_inputs_search_probe_table", "\\input{tables/table_trace_biopt_search_probe}" in analysis_tex, True))
    claims.append(status_equal("search_probe_row_count", len(search_probe_csv), 10))
    claims.append(status_equal("search_probe_dataset", {row["dataset"] for row in search_probe_csv}, {"PeMS7_1026"}))
    claims.append(status_equal("search_probe_budget", {float(row["budget"]) for row in search_probe_csv}, {0.3}))
    claims.append(status_equal("search_probe_original_stage15_seeds", {int(row["split_seed"]) for row in search_probe_csv}, set(range(25, 35))))
    claims.append(status_equal("search_probe_scope", {row["probe_scope"] for row in search_probe_csv}, {"diagnostic weak-row search-budget probe"}))
    claims.append(status_equal("search_probe_all_enhanced_win", {row["enhanced_beats_best_baseline"] for row in search_probe_csv}, {"True"}))
    mean_default_delta = sum(float(row["default_delta"]) for row in search_probe_csv) / len(search_probe_csv)
    mean_enhanced_delta = sum(float(row["enhanced_delta"]) for row in search_probe_csv) / len(search_probe_csv)
    mean_gain = sum(float(row["trace_mae_improvement"]) for row in search_probe_csv) / len(search_probe_csv)
    enhanced_delta = pd.Series([float(row["enhanced_delta"]) for row in search_probe_csv])
    improvement = pd.Series([float(row["trace_mae_improvement"]) for row in search_probe_csv])
    paired_t_p = float(stats.ttest_1samp(enhanced_delta, 0.0, alternative="less").pvalue)
    wilcoxon_p = float(stats.wilcoxon(enhanced_delta, alternative="less").pvalue)
    improvement_p = float(stats.ttest_1samp(improvement, 0.0, alternative="greater").pvalue)
    claims.append(status_equal("search_probe_text_scopes_ten_seed", "original ten Stage15 split seeds" in analysis_tex, True))
    claims.append(status_equal("search_probe_text_reports_all_ten_wins", "wins all ten probed seeds" in analysis_tex, True))
    forbids_replacement = re.search(
        r"not used to replace\s+Table~\\ref\{tab:trace-biopt-dominance\}",
        analysis_tex,
    ) is not None
    claims.append(status_equal("search_probe_text_forbids_table_replacement", forbids_replacement, True))
    search_probe_text = re.search(
        r"changes the mean margin against the seed-matched best pre-registered baseline\s+from (-?[0-9.]+) to (-?[0-9.]+), and wins all ten probed seeds",
        analysis_tex,
    )
    claims.append(status_equal("search_probe_text_margin_sentence_present", search_probe_text is not None, True))
    claims.append(status_round("search_probe_text_mean_default_delta", float(search_probe_text.group(1)), mean_default_delta, ".4f"))
    claims.append(status_round("search_probe_text_mean_enhanced_delta", float(search_probe_text.group(2)), mean_enhanced_delta, ".4f"))
    claims.append(status_round("search_probe_text_mean_gain", float(re.search(r"by ([0-9.]+) on average", analysis_tex).group(1)), mean_gain, ".4f"))
    claims.append(status_equal("search_probe_text_ttest_p", f"p={paired_t_p:.1e}".replace("e-0", "e{-}0") in analysis_tex, True))
    claims.append(status_equal("search_probe_text_wilcoxon_p", f"p={wilcoxon_p:.4f}" in analysis_tex, True))
    for row in search_probe_csv:
        seed = int(row["split_seed"])
        claims.append(status_equal(f"search_probe_table_seed:{seed}", f"{seed} &" in search_probe_tex, True))
        claims.append(status_equal(f"search_probe_table_best:{seed}", row["best_baseline_layout"].replace("_", "\\_") in search_probe_tex, True))
        claims.append(status_round(f"search_probe_table_default_delta:{seed}", float(row["default_delta"]), float(row["default_delta"]), ".4f"))
        claims.append(status_equal(f"search_probe_table_default_delta_rendered:{seed}", f"{float(row['default_delta']):.4f}" in search_probe_tex, True))
        claims.append(status_equal(f"search_probe_table_enhanced_delta_rendered:{seed}", f"{float(row['enhanced_delta']):.4f}" in search_probe_tex, True))
        claims.append(status_equal(f"search_probe_table_gain_rendered:{seed}", f"{float(row['trace_mae_improvement']):.4f}" in search_probe_tex, True))
    claims.append(status_equal("search_probe_table_mean_default", f"{mean_default_delta:.4f}" in search_probe_tex, True))
    claims.append(status_equal("search_probe_table_mean_enhanced", f"{mean_enhanced_delta:.4f}" in search_probe_tex, True))
    claims.append(status_equal("search_probe_table_mean_gain", f"{mean_gain:.4f}" in search_probe_tex, True))
    claims.append(status_equal("search_probe_table_win_count", f"10/{len(search_probe_csv)}" in search_probe_tex, True))
    claims.append(status_equal("search_probe_table_ttest_p", f"p={paired_t_p:.1e}" in search_probe_tex, True))
    claims.append(status_equal("search_probe_table_wilcoxon_p", f"p={wilcoxon_p:.4f}" in search_probe_tex, True))
    claims.append(status_equal("search_probe_table_gain_ttest_p", f"p={improvement_p:.1e}" in search_probe_tex, True))

    claims.append(status_equal("analysis_inputs_calibration_probe_table", "\\input{tables/table_trace_biopt_calibration_probe}" in analysis_tex, True))
    claims.append(status_equal("calibration_probe_row_count", len(calibration_probe_csv), 10))
    claims.append(status_equal("calibration_probe_dataset", {row["dataset"] for row in calibration_probe_csv}, {"PeMS7_228"}))
    claims.append(status_equal("calibration_probe_budget", {float(row["budget"]) for row in calibration_probe_csv}, {0.1}))
    claims.append(status_equal("calibration_probe_original_stage15_seeds", {int(row["split_seed"]) for row in calibration_probe_csv}, set(range(25, 35))))
    claims.append(status_equal("calibration_probe_scope", {row["probe_scope"] for row in calibration_probe_csv}, {"diagnostic low-budget calibration-risk probe"}))
    claims.append(status_equal("calibration_probe_all_calibrated_win", {row["calibrated_beats_best_baseline"] for row in calibration_probe_csv}, {"True"}))
    calibration_default_delta = sum(float(row["default_delta"]) for row in calibration_probe_csv) / len(calibration_probe_csv)
    calibration_delta = sum(float(row["calibrated_delta"]) for row in calibration_probe_csv) / len(calibration_probe_csv)
    calibration_gain = sum(float(row["trace_mae_improvement"]) for row in calibration_probe_csv) / len(calibration_probe_csv)
    calibration_delta_series = pd.Series([float(row["calibrated_delta"]) for row in calibration_probe_csv])
    calibration_gain_series = pd.Series([float(row["trace_mae_improvement"]) for row in calibration_probe_csv])
    calibration_t_p = float(stats.ttest_1samp(calibration_delta_series, 0.0, alternative="less").pvalue)
    calibration_wilcoxon_p = float(stats.wilcoxon(calibration_delta_series, alternative="less").pvalue)
    calibration_gain_p = float(stats.ttest_1samp(calibration_gain_series, 0.0, alternative="greater").pvalue)
    claims.append(status_equal("calibration_probe_text_scopes_low_budget", "PeMS7\\_228 at 10\\%" in calibration_section, True))
    claims.append(status_equal("calibration_probe_text_reports_trainval", "train+validation days" in calibration_section, True))
    claims.append(status_equal("calibration_probe_text_reports_all_ten_wins", "wins all ten probed seeds" in calibration_section, True))
    calibration_route_ok = (
        "evidence route currently used for the PeMS7\\_228 10\\% main-table row" in calibration_section
        or "not used to replace Table~\\ref{tab:trace-biopt-dominance}" in calibration_section
    )
    claims.append(status_equal("calibration_probe_text_forbids_table_replacement", calibration_route_ok, True))
    calibration_text = re.search(
        r"from (-?[0-9.]+) to (-?[0-9.]+), improves TRACE-BiOpt MAE by ([0-9.]+) on average",
        calibration_section,
    )
    claims.append(status_equal("calibration_probe_text_numbers_present", calibration_text is not None, True))
    if calibration_text is not None:
        claims.append(status_round("calibration_probe_text_mean_default_delta", float(calibration_text.group(1)), calibration_default_delta, ".4f"))
        claims.append(status_round("calibration_probe_text_mean_delta", float(calibration_text.group(2)), calibration_delta, ".4f"))
        claims.append(status_round("calibration_probe_text_mean_gain", float(calibration_text.group(3)), calibration_gain, ".4f"))
    claims.append(status_equal("calibration_probe_text_ttest_p", f"p={calibration_t_p:.1e}".replace("e-0", "e{-}0") in analysis_tex, True))
    claims.append(status_equal("calibration_probe_text_wilcoxon_p", f"p={calibration_wilcoxon_p:.4f}" in analysis_tex, True))
    for row in calibration_probe_csv:
        seed = int(row["split_seed"])
        claims.append(status_equal(f"calibration_probe_table_seed:{seed}", f"{seed} &" in calibration_probe_tex, True))
        claims.append(status_equal(f"calibration_probe_table_best:{seed}", row["best_baseline_layout"].replace("_", "\\_") in calibration_probe_tex, True))
        claims.append(status_equal(f"calibration_probe_table_default_delta_rendered:{seed}", f"{float(row['default_delta']):.4f}" in calibration_probe_tex, True))
        claims.append(status_equal(f"calibration_probe_table_delta_rendered:{seed}", f"{float(row['calibrated_delta']):.4f}" in calibration_probe_tex, True))
        claims.append(status_equal(f"calibration_probe_table_gain_rendered:{seed}", f"{float(row['trace_mae_improvement']):.4f}" in calibration_probe_tex, True))
    claims.append(status_equal("calibration_probe_table_mean_default", f"{calibration_default_delta:.4f}" in calibration_probe_tex, True))
    claims.append(status_equal("calibration_probe_table_mean_delta", f"{calibration_delta:.4f}" in calibration_probe_tex, True))
    claims.append(status_equal("calibration_probe_table_mean_gain", f"{calibration_gain:.4f}" in calibration_probe_tex, True))
    claims.append(status_equal("calibration_probe_table_win_count", f"10/{len(calibration_probe_csv)}" in calibration_probe_tex, True))
    claims.append(status_equal("calibration_probe_table_ttest_p", f"p={calibration_t_p:.1e}" in calibration_probe_tex, True))
    claims.append(status_equal("calibration_probe_table_wilcoxon_p", f"p={calibration_wilcoxon_p:.4f}" in calibration_probe_tex, True))
    claims.append(status_equal("calibration_probe_table_gain_ttest_p", f"p={calibration_gain_p:.1e}" in calibration_probe_tex, True))

    claims.append(status_equal("analysis_inputs_stage16_probe_table", "\\input{tables/table_trace_biopt_stage16_calibrated_probe}" in analysis_tex, True))
    claims.append(status_equal("stage16_probe_row_count", len(stage16_probe_csv), 10))
    claims.append(status_equal("stage16_probe_dataset", {row["dataset"] for row in stage16_probe_csv}, {"PeMS7_1026"}))
    claims.append(status_equal("stage16_probe_budget", {float(row["budget"]) for row in stage16_probe_csv}, {0.3}))
    claims.append(status_equal("stage16_probe_original_stage15_seeds", {int(row["split_seed"]) for row in stage16_probe_csv}, set(range(25, 35))))
    claims.append(status_equal("stage16_probe_scope", {row["probe_scope"] for row in stage16_probe_csv}, {"diagnostic Stage16 calibrated-risk probe"}))
    claims.append(status_equal("stage16_probe_all_calibrated_win", {row["calibrated_beats_best_baseline"] for row in stage16_probe_csv}, {"True"}))
    stage16_default_delta = sum(float(row["default_delta"]) for row in stage16_probe_csv) / len(stage16_probe_csv)
    stage16_delta = sum(float(row["calibrated_delta"]) for row in stage16_probe_csv) / len(stage16_probe_csv)
    stage16_gain = sum(float(row["trace_mae_improvement"]) for row in stage16_probe_csv) / len(stage16_probe_csv)
    stage16_delta_series = pd.Series([float(row["calibrated_delta"]) for row in stage16_probe_csv])
    stage16_gain_series = pd.Series([float(row["trace_mae_improvement"]) for row in stage16_probe_csv])
    stage16_t_p = float(stats.ttest_1samp(stage16_delta_series, 0.0, alternative="less").pvalue)
    stage16_wilcoxon_p = float(stats.wilcoxon(stage16_delta_series, alternative="less").pvalue)
    stage16_gain_p = float(stats.ttest_1samp(stage16_gain_series, 0.0, alternative="greater").pvalue)
    claims.append(status_equal("stage16_probe_text_scopes_pems1026_30", "PeMS7\\_1026 at 30\\%" in stage16_section, True))
    claims.append(status_equal("stage16_probe_text_reports_all_ten_wins", "wins all ten probed seeds with calibrated-risk" in stage16_section, True))
    stage16_scope_ok = (
        "future full Stage16 table must rerun the same configuration for all nine dataset-budget regimes" in stage16_section
        or "only PeMS7\\_228 20/30 still awaits the same configuration on more seeds" in stage16_section
    )
    claims.append(status_equal("stage16_probe_text_requires_full_stage16", stage16_scope_ok, True))
    stage16_text = re.search(
        r"from (-?[0-9.]+) to (-?[0-9.]+), improves TRACE-BiOpt MAE by ([0-9.]+) on average",
        stage16_section,
    )
    claims.append(status_equal("stage16_probe_text_numbers_present", stage16_text is not None, True))
    if stage16_text is not None:
        claims.append(status_round("stage16_probe_text_mean_default_delta", float(stage16_text.group(1)), stage16_default_delta, ".4f"))
        claims.append(status_round("stage16_probe_text_mean_delta", float(stage16_text.group(2)), stage16_delta, ".4f"))
        claims.append(status_round("stage16_probe_text_mean_gain", float(stage16_text.group(3)), stage16_gain, ".4f"))
    claims.append(status_equal("stage16_probe_text_ttest_p", f"p={stage16_t_p:.1e}".replace("e-0", "e{-}0") in analysis_tex, True))
    claims.append(status_equal("stage16_probe_text_wilcoxon_p", f"p={stage16_wilcoxon_p:.4f}" in analysis_tex, True))
    for row in stage16_probe_csv:
        seed = int(row["split_seed"])
        claims.append(status_equal(f"stage16_probe_table_seed:{seed}", f"{seed} &" in stage16_probe_tex, True))
        claims.append(status_equal(f"stage16_probe_table_best:{seed}", row["best_baseline_layout"].replace("_", "\\_") in stage16_probe_tex, True))
        claims.append(status_equal(f"stage16_probe_table_default_delta_rendered:{seed}", f"{float(row['default_delta']):.4f}" in stage16_probe_tex, True))
        claims.append(status_equal(f"stage16_probe_table_delta_rendered:{seed}", f"{float(row['calibrated_delta']):.4f}" in stage16_probe_tex, True))
        claims.append(status_equal(f"stage16_probe_table_gain_rendered:{seed}", f"{float(row['trace_mae_improvement']):.4f}" in stage16_probe_tex, True))
    claims.append(status_equal("stage16_probe_table_mean_default", f"{stage16_default_delta:.4f}" in stage16_probe_tex, True))
    claims.append(status_equal("stage16_probe_table_mean_delta", f"{stage16_delta:.4f}" in stage16_probe_tex, True))
    claims.append(status_equal("stage16_probe_table_mean_gain", f"{stage16_gain:.4f}" in stage16_probe_tex, True))
    claims.append(status_equal("stage16_probe_table_win_count", f"10/{len(stage16_probe_csv)}" in stage16_probe_tex, True))
    claims.append(status_equal("stage16_probe_table_ttest_p", f"p={stage16_t_p:.1e}" in stage16_probe_tex, True))
    claims.append(status_equal("stage16_probe_table_wilcoxon_p", f"p={stage16_wilcoxon_p:.4f}" in stage16_probe_tex, True))
    claims.append(status_equal("stage16_probe_table_gain_ttest_p", f"p={stage16_gain_p:.1e}" in stage16_probe_tex, True))

    claims.append(status_equal("analysis_inputs_robustness_routing_table", "\\input{tables/table_robustness_routing}" in analysis_tex, True))
    claims.append(status_equal("robustness_routing_row_count", len(robustness_csv), 9))
    claims.append(status_equal("robustness_routing_all_stress_test_only", {row["claim_route"] for row in robustness_csv}, {"stress-test only"}))
    claims.append(status_equal("robustness_source_stage14_only", {row["source_stage"] for row in robustness_csv}, {"stage14_robustness"}))
    expected_robustness_conditions = {
        "baseline",
        "block missing 12 steps",
        "cost proxy budget 45",
        "observation noise 5%",
        "random missing 10%",
        "sensor failure 5%",
        "sensor failure 10%",
        "sensor failure 20%",
        "chronological split",
    }
    claims.append(status_equal("robustness_routing_conditions", {row["condition"] for row in robustness_csv}, expected_robustness_conditions))
    source_groups: dict[tuple[str, str], list[dict[str, str]]] = {}
    for row in robustness_source_csv:
        source_groups.setdefault((row["robustness_family"], row["robustness_condition"]), []).append(row)
    for row in robustness_csv:
        source_group = source_groups[(row["robustness_family"], {
            "baseline": "baseline",
            "block_missing": "block_missing_12",
            "cost_proxy": "cost_proxy_budget",
            "observation_noise": "noise_0.05",
            "random_missing": "random_missing_0.10",
            "sensor_failure": {
                "sensor failure 5%": "failure_0.05",
                "sensor failure 10%": "failure_0.10",
                "sensor failure 20%": "failure_0.20",
            }.get(row["condition"], row["condition"]),
            "temporal_shift": "chronological_split",
        }[row["robustness_family"]])]
        best = min(source_group, key=lambda item: (float(item["mean"]), item["layout_type"]))
        label = row["condition"]
        claims.append(status_equal(f"robustness_best_layout:{label}", row["best_layout"], best["layout_type"]))
        claims.append(status_equal(f"robustness_layout_rows:{label}", int(row["layout_rows"]), len(source_group)))
        claims.append(status_equal(f"robustness_split_count:{label}", row["split_count_range"], str(int(float(best["count"])))))
        claims.append(status_equal(f"robustness_table_condition:{label}", label.replace("%", "\\%") in robustness_tex, True))
        claims.append(status_equal(f"robustness_table_route:{label}", "stress-test only" in robustness_tex, True))
        claims.append(status_round(f"robustness_best_mae:{label}", float(row["best_mae"]), float(best["mean"]), ".4f"))

    claims.append(status_equal("analysis_inputs_robustness_frontier_table", "\\input{tables/table_trace_biopt_robustness_frontier}" in analysis_tex, True))
    claims.append(status_equal("robustness_frontier_row_count", len(robustness_frontier_csv), 9))
    claims.append(status_equal("robustness_frontier_all_stress_test_only", {row["claim_route"] for row in robustness_frontier_csv}, {"stress-test only"}))
    claims.append(status_equal("robustness_frontier_graph_spectral_wins", sum(row["winner_family"] == "graph-spectral" for row in robustness_frontier_csv), 8))
    frontier_lookup = {row["condition"]: row for row in robustness_frontier_csv}
    claims.append(status_equal("robustness_frontier_block_missing_winner", frontier_lookup["block missing 12 steps"]["winner_layout"], "greedy_d_logdet"))
    claims.append(status_equal("robustness_frontier_chronological_runner_up", frontier_lookup["chronological split"]["runner_up_layout"], "multistart_swap"))
    claims.append(status_round("robustness_frontier_chronological_gap", float(frontier_lookup["chronological split"]["gap_to_runner_up"]), 0.005822285514708092, ".4f"))
    claims.append(status_round("robustness_frontier_failure20_gap", float(frontier_lookup["sensor failure 20%"]["gap_to_runner_up"]), 0.0005976554413948953, ".4f"))
    claims.append(status_round("robustness_frontier_noise_gap", float(frontier_lookup["observation noise 5%"]["gap_to_runner_up"]), 0.04836629285981675, ".4f"))
    claims.append(status_round("robustness_frontier_missing_gap", float(frontier_lookup["random missing 10%"]["gap_to_runner_up"]), 0.040585608908736415, ".4f"))
    frontier_needles = [
        "graph-spectral surrogate",
        "wins 8 of the 9 perturbation slices",
        "block missing 12 steps",
        "0.0058 MAE",
        "0.0006 MAE",
        "0.0484 and 0.0406 MAE",
        "does move across perturbation types",
    ]
    for needle in frontier_needles:
        claims.append(status_equal(f"robustness_frontier_text:{needle}", needle in normalized_analysis_tex, True))
    frontier_table_needles = [
        "Stage14 PeMS7\\_228 stress frontier",
        "graph\\_sampling",
        "greedy\\_d\\_logdet",
        "chronological split",
        "0.0058",
    ]
    for needle in frontier_table_needles:
        claims.append(status_equal(f"robustness_frontier_table:{needle}", needle in robustness_frontier_tex, True))

    claims.append(status_equal("analysis_inputs_deployment_stress_posture_table", "\\input{tables/table_trace_biopt_deployment_stress_posture}" in analysis_tex, True))
    claims.append(status_equal("deployment_stress_posture_row_count", len(deployment_stress_posture_csv), 5))
    posture_lookup = {row["stress_regime"]: row for row in deployment_stress_posture_csv}
    expected_posture_regimes = {
        "Nominal and cost-limited screen",
        "Diffuse corruption",
        "Escalating sensor attrition",
        "Chronological drift",
        "Contiguous outage",
    }
    claims.append(status_equal("deployment_stress_posture_regimes", set(posture_lookup), expected_posture_regimes))
    claims.append(status_equal("deployment_stress_posture_nominal_conditions", posture_lookup["Nominal and cost-limited screen"]["supporting_conditions"], "baseline; cost proxy budget 45"))
    claims.append(status_equal("deployment_stress_posture_nominal_gap", "0.0297" in posture_lookup["Nominal and cost-limited screen"]["frontier_reading"], True))
    claims.append(status_equal("deployment_stress_posture_diffuse_gaps", all(
        needle in posture_lookup["Diffuse corruption"]["frontier_reading"] for needle in ("0.0484", "0.0406")
    ), True))
    claims.append(status_equal("deployment_stress_posture_attrition_gap", "0.0006" in posture_lookup["Escalating sensor attrition"]["frontier_reading"], True))
    claims.append(status_equal("deployment_stress_posture_chrono_gap", "0.0058" in posture_lookup["Chronological drift"]["frontier_reading"], True))
    claims.append(status_equal("deployment_stress_posture_outage_shift", all(
        needle in posture_lookup["Contiguous outage"]["frontier_reading"] for needle in ("logdet", "0.0301")
    ), True))
    posture_needles = [
        "cost-driven posture change",
        "observation noise and random missingness keep graph-spectral as the frontier winner",
        "temporal nonstationarity should trigger re-validation",
        "shrinks to 0.0006 MAE",
        "block missing 12 steps, where logdet takes over",
        "deployment posture statement, not a TRACE-BiOpt robustness claim",
    ]
    for needle in posture_needles:
        claims.append(status_equal(f"deployment_stress_posture_text:{needle}", needle in normalized_analysis_tex, True))
    posture_table_needles = [
        "Reviewer-facing deployment stress posture",
        "Nominal and cost-limited screen",
        "Diffuse corruption",
        "Escalating sensor attrition",
        "Chronological drift",
        "Contiguous outage",
    ]
    for needle in posture_table_needles:
        claims.append(status_equal(f"deployment_stress_posture_table:{needle}", needle in deployment_stress_posture_tex, True))

    claims.append(status_equal("discussion_inputs_design_protocol_table", "\\input{tables/table_trace_biopt_design_protocol}" in discussion_tex, True))
    claims.append(status_equal("design_protocol_row_count", len(design_protocol_csv), 5))
    design_lookup = {row["decision_context"]: row for row in design_protocol_csv}
    design_row_count = int(contract["aggregate_claim"]["row_count"])
    design_paired_ready_rows = sum(
        row["claim_status"] == "supported_submission_ready"
        for row in contract["rows"]
    )
    expected_design_contexts = {
        "Claim-facing benchmark comparison",
        "Thin-validation low-budget regime",
        "Large-network binding-search regime",
        "Stable certified mid/high-budget regimes",
        "Deployment stress screening",
    }
    claims.append(status_equal("design_protocol_contexts", set(design_lookup), expected_design_contexts))
    benchmark_row = design_lookup["Claim-facing benchmark comparison"]
    claims.append(status_equal("design_protocol_benchmark_mentions_baselines", f"{len(contract['aggregate_claim']['baseline_registry'])} non-BiOpt baselines" in benchmark_row["evidence_trigger"], True))
    claims.append(status_equal("design_protocol_benchmark_mentions_paired_gate", f"{design_paired_ready_rows}/{design_row_count}" in benchmark_row["paper_support"], True))
    thin_validation_row = design_lookup["Thin-validation low-budget regime"]
    claims.append(status_equal("design_protocol_thin_validation_mentions_stage16", "Stage16 train+validation calibrated rerun" in thin_validation_row["evidence_trigger"], True))
    claims.append(status_equal("design_protocol_thin_validation_support_values", all(
        needle in thin_validation_row["paper_support"]
        for needle in ("3.248", "3.377", "3.417")
    ), True))
    large_network_row = design_lookup["Large-network binding-search regime"]
    promoted_rows_count = sum(row["source"] == "Stage16 calibrated rerun" for row in provenance_csv)
    pems1026_sensitive_count = sum(
        row["regime"].startswith("PeMS7_1026") and row["search_signal"] == "search-budget sensitive"
        for row in regime_lessons_csv
    )
    claims.append(status_equal("design_protocol_large_network_mentions_counts", all(
        needle in large_network_row["evidence_trigger"]
        for needle in (f"{pems1026_sensitive_count}/3", f"{promoted_rows_count}/9")
    ), True))
    stable_row = design_lookup["Stable certified mid/high-budget regimes"]
    stable_count = sum(row["search_signal"] == "searched-neighborhood stable" for row in regime_lessons_csv)
    claims.append(status_equal("design_protocol_stable_mentions_count", f"{stable_count}/9" in stable_row["evidence_trigger"], True))
    claims.append(status_equal("design_protocol_stable_mentions_zero_weight_penalties", all(
        needle in stable_row["evidence_trigger"] for needle in ("0.036", "0.032")
    ), True))
    stress_row = design_lookup["Deployment stress screening"]
    claims.append(status_equal("design_protocol_stress_mentions_frontier", all(
        needle in stress_row["evidence_trigger"]
        for needle in ("8/9", "logdet", "0.0006")
    ), True))
    design_discussion_needles = [
        "claim-facing deployment checklist",
        "row-wise strongest audited comparator",
        "calibrate upper-level reconstruction risk when validation support is thin",
        "scale the deterministic search budget with network size",
        "zero-weight strong-search still loses",
        "bounded deployment screens rather than as TRACE-BiOpt dominance evidence",
    ]
    for needle in design_discussion_needles:
        claims.append(status_equal(f"design_protocol_discussion:{needle}", needle in normalized_discussion_tex, True))
    design_table_needles = [
        "Reviewer-facing TRACE-BiOpt design and deployment protocol",
        "Claim-facing benchmark comparison",
        "Thin-validation low-budget regime",
        "Large-network binding-search regime",
        "Stable certified mid/high-budget regimes",
        "Deployment stress screening",
    ]
    for needle in design_table_needles:
        claims.append(status_equal(f"design_protocol_table:{needle}", needle in design_protocol_tex, True))

    claims.append(status_equal("discussion_inputs_budget_phasing_table", "\\input{tables/table_trace_biopt_budget_phasing}" in discussion_tex, True))
    claims.append(status_equal("budget_phasing_row_count", len(budget_phasing_csv), 3))
    budget_phasing_lookup = {row["dataset"]: row for row in budget_phasing_csv}
    claims.append(status_equal(
        "budget_phasing_datasets",
        set(budget_phasing_lookup),
        {"PeMS7_1026", "PeMS7_228", "Seattle"},
    ))
    for dataset in {"PeMS7_1026", "PeMS7_228", "Seattle"}:
        row10 = delta[(dataset, 0.1)]
        row20 = delta[(dataset, 0.2)]
        row30 = delta[(dataset, 0.3)]
        trace10 = float(row10["trace_biopt_mean"])
        trace20 = float(row20["trace_biopt_mean"])
        trace30 = float(row30["trace_biopt_mean"])
        base10 = float(row10["best_baseline_mean"])
        base20 = float(row20["best_baseline_mean"])
        base30 = float(row30["best_baseline_mean"])
        expected = {
            "trace_gain_10_20": trace10 - trace20,
            "trace_gain_20_30": trace20 - trace30,
            "trace_first_step_share": (trace10 - trace20) / (trace10 - trace30),
            "margin_10": base10 - trace10,
            "margin_20": base20 - trace20,
            "margin_30": base30 - trace30,
        }
        row = budget_phasing_lookup[dataset]
        for key, value in expected.items():
            claims.append(status_round(f"budget_phasing:{dataset}:{key}", float(row[key]), value, ".10f"))
    budget_phasing_needles = [
        "the first 10-point budget increase already captures 57--67\\% of TRACE-BiOpt's total 10--30\\% MAE reduction",
        "the strongest-baseline margin still contracts from 0.124 at 20\\% to 0.038 at 30\\%",
        "the strongest-baseline margin widens from 0.142 to 0.276 to 0.336",
        "the strongest-baseline margin widening from 0.056 to 0.094",
    ]
    for needle in budget_phasing_needles:
        claims.append(status_equal(f"budget_phasing_text:{needle}", needle in normalized_discussion_tex, True))
    budget_phasing_table_needles = [
        "Current-best TRACE-BiOpt budget-phasing posture.",
        "TRACE-BiOpt MAE path",
        "TRACE-BiOpt marginal gain",
        "Margin path vs strongest baseline",
        "Deployment readout",
    ]
    for needle in budget_phasing_table_needles:
        claims.append(status_equal(f"budget_phasing_table:{needle}", needle in budget_phasing_tex, True))

    claims.append(status_equal("discussion_inputs_boundary_table", "\\input{tables/table_trace_biopt_discussion_boundary}" in discussion_tex, True))
    claims.append(status_equal("discussion_boundary_row_count", len(discussion_boundary_csv), 5))
    discussion_boundary_lookup = {row["boundary_label"]: row for row in discussion_boundary_csv}
    claims.append(status_equal(
        "discussion_boundary_labels",
        set(discussion_boundary_lookup),
        {"Baseline scope", "Calibrated rerun status", "Theory and solver", "Mechanism diagnostics", "Stress evidence"},
    ))
    claims.append(status_equal(
        "discussion_boundary_baseline_mentions_rank1",
        "9/9 tested rows" in discussion_boundary_lookup["Baseline scope"]["what_still_stands"],
        True,
    ))
    claims.append(status_equal(
        "discussion_boundary_calibrated_mentions_4of9",
        f"{stage16_rows}/9 current-best rows" in discussion_boundary_lookup["Calibrated rerun status"]["what_still_stands"],
        True,
    ))
    claims.append(status_equal(
        "discussion_boundary_theory_nonclaim",
        "exact global optimality" in discussion_boundary_lookup["Theory and solver"]["explicit_non_claim"],
        True,
    ))
    claims.append(status_equal(
        "discussion_boundary_mechanism_nonclaim",
        "not extra dominance rows" in discussion_boundary_lookup["Mechanism diagnostics"]["explicit_non_claim"],
        True,
    ))
    claims.append(status_equal(
        "discussion_boundary_stress_nonclaim",
        "do not become TRACE-BiOpt robustness dominance claims" in discussion_boundary_lookup["Stress evidence"]["explicit_non_claim"],
        True,
    ))
    discussion_boundary_needles = [
        "compresses the companion boundary story into one discussion-facing readout",
        "The paper still claims an external audited comparison-class contract",
        "Holm-corrected all-baseline screen over 21 pre-registered baselines spanning 11 method families",
        "no surviving challenger after 189 Holm-corrected paired comparisons",
        "It also says just as plainly what does not follow",
        "universal baseline dominance, exact global optimality, universal MAE theorems",
    ]
    for needle in discussion_boundary_needles:
        claims.append(status_equal(f"discussion_boundary_text:{needle}", needle in normalized_discussion_tex, True))
    discussion_boundary_table_needles = [
        "Discussion-facing TRACE-BiOpt boundary table.",
        "Baseline scope",
        "Calibrated rerun status",
        "Theory and solver",
        "Mechanism diagnostics",
        "Stress evidence",
    ]
    for needle in discussion_boundary_table_needles:
        claims.append(status_equal(f"discussion_boundary_table:{needle}", needle in discussion_boundary_tex, True))

    claims.append(status_equal("discussion_inputs_exact_subnetwork_table", "\\input{tables/table_trace_biopt_exact_subnetwork}" in discussion_tex, True))
    claims.append(status_equal("exact_subnetwork_summary_row_count", len(exact_subnetwork_summary_csv), 3))
    claims.append(status_equal("exact_subnetwork_detail_row_count", len(exact_subnetwork_detail_csv), 27))
    exact_summary_lookup = {row["dataset"]: row for row in exact_subnetwork_summary_csv}
    claims.append(status_equal(
        "exact_subnetwork_summary_datasets",
        set(exact_summary_lookup),
        {"PeMS7_1026", "PeMS7_228", "Seattle"},
    ))
    for dataset in {"PeMS7_1026", "PeMS7_228", "Seattle"}:
        row = exact_summary_lookup[dataset]
        claims.append(status_equal(f"exact_subnetwork:{dataset}:hits", f"{row['exact_hits']}/{row['exact_cases']}", "9/9"))
        claims.append(status_round(f"exact_subnetwork:{dataset}:mean_objective_gap", float(row["mean_objective_gap"]), 0.0, ".12f"))
        claims.append(status_round(f"exact_subnetwork:{dataset}:max_objective_gap", float(row["max_objective_gap"]), 0.0, ".12f"))
        claims.append(status_round(f"exact_subnetwork:{dataset}:mean_validation_mae_gap", float(row["mean_validation_mae_gap"]), 0.0, ".12f"))
        claims.append(status_round(f"exact_subnetwork:{dataset}:max_validation_mae_gap", float(row["max_validation_mae_gap"]), 0.0, ".12f"))
        claims.append(status_equal(f"exact_subnetwork:{dataset}:total_layouts", int(row["total_enumerated_layouts"]), 15144))
    claims.append(status_equal(
        "exact_subnetwork_detail_route_labels",
        {
            row["route_parameter_scope"] for row in exact_subnetwork_detail_csv
        },
        {"Stage16 promoted row parameters", "Retained Stage15 current-best route"},
    ))
    claims.append(status_equal(
        "exact_subnetwork_detail_budgets",
        sorted({float(row["budget"]) for row in exact_subnetwork_detail_csv}),
        [0.1, 0.2, 0.3],
    ))
    claims.append(status_equal(
        "exact_subnetwork_detail_anchor_count",
        len({(row["dataset"], int(row["anchor_node"])) for row in exact_subnetwork_detail_csv}),
        9,
    ))
    claims.append(status_equal(
        "exact_subnetwork_detail_all_matches",
        all(row["layout_match"] == "True" for row in exact_subnetwork_detail_csv),
        True,
    ))
    exact_subnetwork_needles = [
        "three deterministic anchor-centered 16-node induced subnetworks",
        "27 audited subnetwork cases",
        "hits the exact optimum every time",
        "zero objective gap",
        "does not remove the full-network caveat",
        "does not upgrade Seattle 10\\% from fail-closed dominance evidence",
        "larger exact mixed-integer or exhaustive benchmarks beyond the audited 16-node subnetworks",
    ]
    for needle in exact_subnetwork_needles:
        claims.append(status_equal(f"exact_subnetwork_text:{needle}", needle in normalized_discussion_tex, True))
    exact_subnetwork_table_needles = [
        "Bounded exact-subnetwork benchmark for TRACE-BiOpt.",
        "Exact benchmark setup",
        "Exact hit count",
        "Objective / MAE gap",
        "9/9 exact hits",
        "120 / 560 / 4368 layouts per anchor.",
    ]
    for needle in exact_subnetwork_table_needles:
        claims.append(status_equal(f"exact_subnetwork_table:{needle}", needle in exact_subnetwork_tex, True))
    introduction_tex = read(PAPER / "sections" / "1_introduction.tex")
    introduction_exact_needles = [
        "bounded exact benchmark shows 27/27 exact hits on deterministic 16-node induced subnetworks under row-wise current-best parameters",
        "split-paired, and now also bounded-exact on audited subnetworks",
    ]
    for needle in introduction_exact_needles:
        claims.append(status_equal(f"introduction_exact_text:{needle}", needle in introduction_tex, True))
    conclusion_tex = read(PAPER / "sections" / "8_conclusion.tex")
    normalized_conclusion_tex = re.sub(r"\s+", " ", conclusion_tex)
    claims.append(status_equal(
        "conclusion_mentions_exact_subnetwork_hits",
        "exact-hits 27/27 deterministic 16-node subnetworks with zero objective gap" in conclusion_tex,
        True,
    ))
    claims.append(status_equal("conclusion_inputs_planning_takeaways_table", "\\input{tables/table_trace_biopt_planning_takeaways}" in conclusion_tex, True))
    claims.append(status_equal("planning_takeaways_row_count", len(planning_takeaways_csv), 3))
    takeaway_lookup = {row["dataset"]: row for row in planning_takeaways_csv}
    claims.append(status_equal("planning_takeaways_datasets", set(takeaway_lookup), {"PeMS7_1026", "PeMS7_228", "Seattle"}))
    claims.append(status_equal("planning_takeaways_pems1026_archetype", takeaway_lookup["PeMS7_1026"]["planning_archetype"], "Large search-sensitive network"))
    claims.append(status_equal("planning_takeaways_pems228_archetype", takeaway_lookup["PeMS7_228"]["planning_archetype"], "Expansion-friendly medium network"))
    claims.append(status_equal("planning_takeaways_seattle_archetype", takeaway_lookup["Seattle"]["planning_archetype"], "Low-variance staged-rollout network"))
    claims.append(status_equal("planning_takeaways_pems1026_mentions_margin_path", "0.130 -> 0.124 -> 0.038" in takeaway_lookup["PeMS7_1026"]["current_best_readout"], True))
    claims.append(status_equal("planning_takeaways_pems228_mentions_margin_path", "0.142 -> 0.276 -> 0.336" in takeaway_lookup["PeMS7_228"]["current_best_readout"], True))
    claims.append(status_equal("planning_takeaways_seattle_mentions_stage15", "Stage15 main evidence" in takeaway_lookup["Seattle"]["current_best_readout"], True))
    claims.append(status_equal("planning_takeaways_pems1026_mentions_63of63", "63/63" in takeaway_lookup["PeMS7_1026"]["current_best_readout"], True))
    claims.append(status_equal("planning_takeaways_pems228_mentions_63of63", "63/63" in takeaway_lookup["PeMS7_228"]["current_best_readout"], True))
    claims.append(status_equal("planning_takeaways_seattle_mentions_63of63", "63/63" in takeaway_lookup["Seattle"]["current_best_readout"], True))
    planning_takeaway_needles = [
        "network-level planning readout",
        "search-budget-sensitive large network",
        "expansion-friendly calibrated rollout",
        "conservative staged-rollout case",
    ]
    for needle in planning_takeaway_needles:
        claims.append(status_equal(f"planning_takeaways_conclusion:{needle}", needle in normalized_conclusion_tex, True))
    planning_takeaway_table_needles = [
        "Network-level planning takeaways from the TRACE-BiOpt current-best evidence chain",
        "Large search-sensitive network",
        "Expansion-friendly medium network",
        "Low-variance staged-rollout network",
        "Seattle 10\\%",
    ]
    for needle in planning_takeaway_table_needles:
        claims.append(status_equal(f"planning_takeaways_table:{needle}", needle in planning_takeaways_tex, True))
    design_protocol_needles = [
        "189/189",
        "no surviving tied or better challenger",
        "multiplicity-corrected all-baseline screen",
    ]
    for needle in design_protocol_needles:
        claims.append(status_equal(f"design_protocol:{needle}", needle in design_protocol_tex, True))
    discussion_boundary_needles = [
        "189/189",
        "no surviving tied or better challenger",
        "formal CVaR tail-risk epigraph",
        "external audited comparison-class contract with a multiplicity-robust all-baseline screen",
    ]
    for needle in discussion_boundary_needles:
        claims.append(status_equal(f"discussion_boundary:{needle}", needle in discussion_boundary_tex, True))

    counts: dict[str, int] = {}
    for claim in claims:
        counts[claim["status"]] = counts.get(claim["status"], 0) + 1
    bad = [c for c in claims if c["status"] not in {"exact_match", "rounding_ok"}]
    verdict = "PASS" if not bad else "FAIL"

    artifact = {
        "audit_type": "fresh_machine_paper_claim_audit",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "verdict": verdict,
        "counts": counts,
        "claims_checked": len(claims),
        "failed_claims": bad,
        "claims": claims,
        "evidence_files": [
            str(CURRENT_BEST / "trace_biopt_best_baseline_delta.csv"),
            str(CURRENT_BEST / "trace_biopt_claim_contract.json"),
            str(CURRENT_BEST / "trace_biopt_claim_boundary_matrix.csv"),
            str(PAPER / "tables" / "table_trace_biopt_dominance.tex"),
            str(PAPER / "tables" / "table_trace_biopt_claim_boundary_matrix.tex"),
            str(PAPER / "tables" / "table_trace_biopt_full_baseline_matrix.tex"),
            str(PAPER / "tables" / "table_trace_biopt_significance_posture.tex"),
            str(PAPER / "tables" / "table_trace_biopt_baseline_family_screen.tex"),
            str(PAPER / "tables" / "table_trace_biopt_regime_lessons.tex"),
            str(PAPER / "tables" / "table_trace_biopt_current_best_provenance.tex"),
            str(PAPER / "tables" / "table_trace_biopt_mechanism.tex"),
            str(PAPER / "tables" / "table_trace_biopt_exchange_certificate.tex"),
            str(PAPER / "tables" / "table_trace_biopt_compute_posture.tex"),
            str(PAPER / "tables" / "table_trace_biopt_route_ablation.tex"),
            str(PAPER / "tables" / "table_trace_biopt_layout_consensus_posture.tex"),
            str(PAPER / "figures" / "fig_trace_biopt_current_best_curves.pdf"),
            str(PAPER / "figures" / "fig_trace_biopt_paired_margins.pdf"),
            str(PAPER / "figures" / "fig_trace_biopt_calibration_alignment.pdf"),
            str(PAPER / "figures" / "fig_trace_biopt_exchange_gap_curves.pdf"),
            str(PAPER / "figures" / "fig_trace_biopt_hidden_error_heatmaps.pdf"),
            str(PAPER / "figures" / "fig_trace_biopt_layout_fingerprints.pdf"),
            str(PAPER / "tables" / "table_trace_biopt_baseline_registry.tex"),
            str(PAPER / "tables" / "table_trace_biopt_optimization.tex"),
            str(PAPER / "tables" / "table_robustness_routing.tex"),
            str(PAPER / "tables" / "table_trace_biopt_robustness_frontier.tex"),
            str(PAPER / "tables" / "table_trace_biopt_deployment_stress_posture.tex"),
            str(PAPER / "tables" / "table_trace_biopt_design_protocol.tex"),
            str(PAPER / "tables" / "table_trace_biopt_budget_phasing.tex"),
            str(PAPER / "tables" / "table_trace_biopt_discussion_boundary.tex"),
            str(PAPER / "tables" / "table_trace_biopt_exact_subnetwork.tex"),
            str(PAPER / "tables" / "table_trace_biopt_search_probe.tex"),
            str(PAPER / "tables" / "table_trace_biopt_calibration_probe.tex"),
            str(PAPER / "tables" / "table_trace_biopt_stage16_calibrated_probe.tex"),
            str(PAPER / "figures" / "fig_trace_biopt_full_baseline_heatmap.pdf"),
            str(CURRENT_BEST / "trace_biopt_mechanism_diagnostics.csv"),
            str(STAGE15 / "trace_biopt_baseline_registry.csv"),
            str(STAGE15 / "trace_biopt_optimization_diagnostics.csv"),
            str(STAGE15 / "trace_biopt_optimization_diagnostics_detail.csv"),
            str(CURRENT_BEST / "trace_biopt_compute_posture.csv"),
            str(CURRENT_BEST / "trace_biopt_compute_posture_detail.csv"),
            str(CURRENT_BEST / "trace_biopt_exchange_certificate_summary.csv"),
            str(PAPER_SOURCES / "robustness_routing_summary.csv"),
            str(PAPER_SOURCES / "robustness_frontier_summary.csv"),
            str(PAPER_SOURCES / "robustness_stress_posture_summary.csv"),
            str(PAPER_SOURCES / "robustness_condition_table.csv"),
            str(PAPER_SOURCES / "trace_biopt_search_budget_probe.csv"),
            str(PAPER_SOURCES / "trace_biopt_calibration_risk_probe.csv"),
            str(PAPER_SOURCES / "trace_biopt_stage16_calibrated_probe.csv"),
            str(CURRENT_BEST / "trace_biopt_current_best_provenance.csv"),
            str(CURRENT_BEST / "trace_biopt_full_baseline_matrix.csv"),
            str(CURRENT_BEST / "trace_biopt_full_baseline_heatmap.csv"),
            str(CURRENT_BEST / "trace_biopt_performance_curves.csv"),
            str(CURRENT_BEST / "trace_biopt_paired_margin_points.csv"),
            str(CURRENT_BEST / "trace_biopt_paired_margin_summary.csv"),
            str(CURRENT_BEST / "trace_biopt_significance_posture_summary.csv"),
            str(CURRENT_BEST / "trace_biopt_significance_posture_detail.csv"),
            str(CURRENT_BEST / "trace_biopt_baseline_family_screen.csv"),
            str(CURRENT_BEST / "trace_biopt_calibration_alignment_points.csv"),
            str(CURRENT_BEST / "trace_biopt_calibration_alignment_summary.csv"),
            str(CURRENT_BEST / "trace_biopt_route_ablation_summary.csv"),
            str(CURRENT_BEST / "trace_biopt_exchange_gap_summary.csv"),
            str(CURRENT_BEST / "trace_biopt_exchange_gap_curves.csv"),
            str(CURRENT_BEST / "trace_biopt_hidden_error_heatmap_grid.csv"),
            str(CURRENT_BEST / "trace_biopt_hidden_error_heatmap_summary.csv"),
            str(CURRENT_BEST / "trace_biopt_layout_consensus_posture.csv"),
            str(CURRENT_BEST / "trace_biopt_layout_fingerprint_summary.csv"),
            str(CURRENT_BEST / "trace_biopt_regime_lessons.csv"),
            str(CURRENT_BEST / "trace_biopt_design_protocol.csv"),
            str(CURRENT_BEST / "trace_biopt_budget_phasing.csv"),
            str(CURRENT_BEST / "trace_biopt_discussion_boundary.csv"),
            str(CURRENT_BEST / "trace_biopt_exact_subnetwork_summary.csv"),
            str(CURRENT_BEST / "trace_biopt_exact_subnetwork_detail.csv"),
            str(STAGE15 / "certificate_correlation_summary.csv"),
            str(STAGE15 / "gls_map_layout_summary.csv"),
            str(PAPER / "sections" / "5_experiments.tex"),
            str(PAPER / "sections" / "6_ablation_robustness.tex"),
            str(PAPER / "sections" / "7_robustness.tex"),
            str(PAPER / "sections" / "7_discussion.tex"),
            str(PAPER / "sections" / "A_appendix.tex"),
            str(PAPER / "main.tex"),
        ],
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{verdict}: checked {len(claims)} claims; counts={counts}; output={OUT}")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
