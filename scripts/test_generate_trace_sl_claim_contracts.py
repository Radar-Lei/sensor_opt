#!/usr/bin/env python3
"""Regression tests for TRACE-SL claim/table contract generation."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = PROJECT_ROOT / "scripts" / "generate_trace_sl_claim_contracts.py"


FORBIDDEN_TERMS = (
    "optimal",
    "certified",
    "globally robust",
    "guaranteed MAE improvement",
    "generalizes across networks",
)
LOW_BUDGET_CAVEAT = "pems7_228_low_budget_multistart_not_dominant"


def import_generator():
    spec = importlib.util.spec_from_file_location("generate_trace_sl_claim_contracts", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not import generator from {GENERATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ClaimContractGenerationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.stage12_dir = self.root / "TRC-23-02333" / "trace_sl_results" / "pems7_228_stage12_baseline_portfolio"

    def write_csv(self, relative_path: str, rows: list[dict[str, object]]) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(rows).to_csv(path, index=False)
        return path

    def layout_rows(self, include_secondary_certificate_baseline: bool = False) -> list[dict[str, object]]:
        labels = [
            "validation_swap_selected",
            "multistart_swap_by_validation",
            "rcss_selected",
            "best_random_by_validation",
            "random",
            "top_variance",
            "greedy_a_trace",
            "graph_sampling_laplacian",
            "observability_proxy",
            "qr_pod_modes",
        ]
        if include_secondary_certificate_baseline:
            labels.append("greedy_d_logdet")
        rows: list[dict[str, object]] = []
        for budget in (0.1, 0.2):
            for index, label in enumerate(labels):
                rows.append(
                    {
                        "budget": budget,
                        "layout_type": label,
                        "mean": 3.0 + budget + index / 100.0,
                        "std": 0.1 + index / 1000.0,
                        "count": 10 if label != "random" else 500,
                        "rmse_mean": 4.0 + index / 100.0,
                        "mape_mean": 0.2 + index / 1000.0,
                    }
                )
        return rows

    def paired_rows(self, include_secondary_certificate_baseline: bool = False) -> list[dict[str, object]]:
        baselines = [
            "multistart_swap_by_validation",
            "best_random_by_validation",
            "random",
            "top_variance",
            "greedy_a_trace",
            "graph_sampling_laplacian",
            "observability_proxy",
            "qr_pod_modes",
        ]
        if include_secondary_certificate_baseline:
            baselines.append("greedy_d_logdet")
        rows: list[dict[str, object]] = []
        for budget in (0.1, 0.2):
            for index, baseline in enumerate(baselines):
                rows.append(
                    {
                        "budget": budget,
                        "layout": "validation_swap_selected",
                        "baseline": baseline,
                        "delta_mean": -0.01 * (index + 1),
                        "ci95_low": -0.02 * (index + 1),
                        "ci95_high": 0.01 if baseline == "multistart_swap_by_validation" else -0.001,
                        "paired_t_p": 0.8 if baseline == "multistart_swap_by_validation" and budget == 0.1 else 0.01,
                        "wilcoxon_p": 0.77 if baseline == "multistart_swap_by_validation" and budget == 0.1 else 0.02,
                        "win_count": 5 if baseline == "multistart_swap_by_validation" and budget == 0.1 else 9,
                        "count": 10,
                    }
                )
        return rows

    def make_stage12_sources(self, include_secondary_certificate_baseline: bool = False) -> tuple[Path, Path]:
        layout_csv = self.write_csv(
            "TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/gls_map_layout_summary.csv",
            self.layout_rows(include_secondary_certificate_baseline),
        )
        paired_csv = self.write_csv(
            "TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/gls_map_paired_delta_tests.csv",
            self.paired_rows(include_secondary_certificate_baseline),
        )
        return layout_csv, paired_csv

    def test_claim_contract_rows_include_lanes_wording_and_evidence_routing(self) -> None:
        generator = import_generator()
        layout_csv, paired_csv = self.make_stage12_sources()

        rows = generator.build_claim_contract_rows(layout_csv.parent, layout_csv, paired_csv)
        generator.validate_claim_contract_rows(rows)

        expected_columns = {
            "source_stage",
            "source_dir",
            "source_csv",
            "claim_id",
            "claim_lane",
            "claim_status",
            "allowed_wording",
            "forbidden_wording",
            "evidence_source",
            "evidence_artifact",
            "required_metric_basis",
            "required_caveat_tag",
            "phase_scope",
            "notes",
        }
        self.assertTrue(rows)
        for row in rows:
            self.assertEqual(set(row), expected_columns)
            self.assertNotIn("TRC-23-02333/dataset/", row["evidence_artifact"])
            artifact_path = Path(row["evidence_artifact"])
            self.assertEqual(row["source_dir"], artifact_path.parent.as_posix())
            self.assertEqual(row["source_csv"], artifact_path.name)

        evidence_sources = {row["evidence_source"] for row in rows}
        self.assertIn("PeMS7_1026", evidence_sources)
        self.assertNotIn("Seattle", evidence_sources)
        self.assertNotIn(
            "TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light",
            {row["evidence_artifact"] for row in rows},
        )

        lanes = {row["claim_lane"] for row in rows}
        statuses = {row["claim_status"] for row in rows}
        self.assertIn("core_in_domain", lanes)
        self.assertIn("tr_part_b_extension", lanes)
        self.assertIn("wording_guardrail", lanes)
        self.assertIn("external_evidence", lanes)
        self.assertIn("stress_test", lanes)
        self.assertIn("appendix", lanes)
        self.assertIn("transportation_science_ready", statuses)
        self.assertIn("requires_stronger_theory", statuses)
        self.assertIn("held_out_test_with_paired_comparisons", {row["required_metric_basis"] for row in rows})

    def test_forbidden_and_allowed_wording_policy_is_exact(self) -> None:
        generator = import_generator()
        self.assertEqual(tuple(generator.FORBIDDEN_WORDING), FORBIDDEN_TERMS)
        self.assertEqual(
            tuple(generator.BOUNDED_ALLOWED_WORDING),
            (
                "certificate-guided",
                "posterior-certificate-aware",
                "stress-tested",
                "improves in the tested setting",
                "external evidence",
            ),
        )
        layout_csv, paired_csv = self.make_stage12_sources()
        rows = generator.build_claim_contract_rows(layout_csv.parent, layout_csv, paired_csv)
        policy_rows = [row for row in rows if row["claim_lane"] == "wording_guardrail"]
        self.assertEqual([row["forbidden_wording"] for row in policy_rows], list(FORBIDDEN_TERMS))
        for phrase in generator.BOUNDED_ALLOWED_WORDING:
            self.assertIn(phrase, {row["allowed_wording"] for row in rows})

    def test_missing_columns_required_labels_empty_outputs_and_missing_policy_fail_closed(self) -> None:
        generator = import_generator()
        layout_csv, paired_csv = self.make_stage12_sources()
        layout_frame = generator.load_csv(layout_csv)
        paired_frame = generator.load_csv(paired_csv)

        with self.assertRaisesRegex(ValueError, "layout summary missing columns"):
            generator.build_main_table_contract_rows(layout_frame.drop(columns=["count"]), paired_frame, layout_csv.parent, layout_csv, paired_csv)

        with self.assertRaisesRegex(ValueError, "paired statistics missing columns"):
            generator.build_main_table_contract_rows(layout_frame, paired_frame.drop(columns=["paired_t_p"]), layout_csv.parent, layout_csv, paired_csv)

        with self.assertRaisesRegex(ValueError, "missing required layout_type rows"):
            generator.build_main_table_contract_rows(
                layout_frame[layout_frame["layout_type"] != "observability_proxy"],
                paired_frame,
                layout_csv.parent,
                layout_csv,
                paired_csv,
            )

        with self.assertRaises(FileNotFoundError):
            generator.load_csv(self.root / "TRC-23-02333/trace_sl_results/missing.csv")

        with self.assertRaisesRegex(ValueError, "empty"):
            generator.validate_claim_contract_rows([])

        rows = generator.build_claim_contract_rows(layout_csv.parent, layout_csv, paired_csv)
        with self.assertRaisesRegex(ValueError, "missing forbidden wording"):
            generator.validate_claim_contract_rows([row for row in rows if row["forbidden_wording"] != "optimal"])

        table_rows = generator.build_main_table_contract_rows(layout_frame, paired_frame, layout_csv.parent, layout_csv, paired_csv)
        with self.assertRaisesRegex(ValueError, LOW_BUDGET_CAVEAT):
            generator.validate_main_table_contract_rows(
                [dict(row, caveat_tag="") if row["budget"] == 0.1 else row for row in table_rows]
            )

        bad_source_rows = [dict(row) for row in table_rows]
        bad_source_rows[0]["source_dir"] = "TRC-23-02333/dataset/PeMS7_228"
        with self.assertRaisesRegex(ValueError, "raw dataset"):
            generator.validate_main_table_contract_rows(bad_source_rows)

    def test_external_datasets_cannot_be_core_transportation_science_claims_in_phase7(self) -> None:
        generator = import_generator()
        layout_csv, paired_csv = self.make_stage12_sources()
        rows = generator.build_claim_contract_rows(layout_csv.parent, layout_csv, paired_csv)

        external_rows = [
            row
            for row in rows
            if row["evidence_source"] in {"PeMS7_1026", "Seattle"}
        ]
        self.assertTrue(external_rows)
        for row in external_rows:
            self.assertNotEqual(row["claim_lane"], "core_in_domain")
            self.assertNotEqual(row["claim_status"], "transportation_science_ready")

        bad_rows = [dict(row) for row in rows]
        bad_rows.append(
            dict(
                rows[0],
                claim_id="BAD-EXTERNAL",
                claim_lane="core_in_domain",
                claim_status="transportation_science_ready",
                evidence_source="Seattle",
            )
        )
        with self.assertRaisesRegex(ValueError, "external evidence"):
            generator.validate_claim_contract_rows(bad_rows)

    def test_robustness_rows_stay_stress_test_or_appendix_without_multiseed_evidence(self) -> None:
        generator = import_generator()
        layout_csv, paired_csv = self.make_stage12_sources()
        rows = generator.build_claim_contract_rows(layout_csv.parent, layout_csv, paired_csv)

        robustness_rows = [row for row in rows if row["evidence_source"] == "Stage14 robustness"]
        self.assertTrue(robustness_rows)
        for row in robustness_rows:
            self.assertIn(row["claim_lane"], {"stress_test", "appendix"})

        bad_rows = [dict(row) for row in rows]
        bad_rows.append(
            dict(
                rows[0],
                claim_id="BAD-ROBUSTNESS",
                claim_lane="core_in_domain",
                claim_status="transportation_science_ready",
                evidence_source="Stage14 robustness",
                notes="single-seed perturbation evidence only",
            )
        )
        with self.assertRaisesRegex(ValueError, "robustness"):
            generator.validate_claim_contract_rows(bad_rows)

        supported_rows = [dict(row) for row in rows]
        supported_rows.append(
            dict(
                rows[0],
                claim_id="SUPPORTED-ROBUSTNESS",
                claim_lane="core_in_domain",
                claim_status="conditional_supported",
                evidence_source="Stage14 robustness",
                notes="multi-seed perturbation evidence",
            )
        )
        generator.validate_claim_contract_rows(supported_rows)

    def test_main_table_contract_rows_preserve_stage12_evidence_and_caveats(self) -> None:
        generator = import_generator()
        layout_csv, paired_csv = self.make_stage12_sources()
        layout_frame = generator.load_csv(layout_csv)
        paired_frame = generator.load_csv(paired_csv)

        rows = generator.build_main_table_contract_rows(layout_frame, paired_frame, layout_csv.parent, layout_csv, paired_csv)
        generator.validate_main_table_contract_rows(rows)

        expected_columns = {
            "source_stage",
            "source_dir",
            "source_csv",
            "budget",
            "method_label",
            "layout_type",
            "table_role",
            "test_mae_mean",
            "test_mae_std",
            "test_rmse_mean",
            "test_mape_mean",
            "paired_baseline",
            "delta_mean",
            "ci95_low",
            "ci95_high",
            "paired_t_p",
            "wilcoxon_p",
            "win_count",
            "split_count",
            "caveat_tag",
            "claim_lane",
        }
        self.assertTrue(rows)
        for row in rows:
            self.assertEqual(set(row), expected_columns)
            self.assertEqual(row["method_label"], "validation_swap_selected")
            self.assertEqual(row["claim_lane"], "core_in_domain")
            self.assertEqual(row["source_stage"], "stage12_baseline_portfolio")
            self.assertEqual(row["source_csv"], "gls_map_layout_summary.csv;gls_map_paired_delta_tests.csv")

        low_budget_rows = [row for row in rows if row["budget"] == 0.1]
        self.assertTrue(low_budget_rows)
        for row in low_budget_rows:
            self.assertEqual(row["caveat_tag"], LOW_BUDGET_CAVEAT)

        dominance_sensitive = [row for row in rows if row["paired_baseline"] == "multistart_swap_by_validation"]
        self.assertTrue(dominance_sensitive)
        for row in dominance_sensitive:
            self.assertEqual(row["caveat_tag"], LOW_BUDGET_CAVEAT)

        baselines = {row["paired_baseline"] for row in rows}
        self.assertIn("best_random_by_validation", baselines)
        self.assertIn("qr_pod_modes", baselines)

    def test_json_policy_uses_plan_required_schema_marker(self) -> None:
        generator = import_generator()
        layout_csv, paired_csv = self.make_stage12_sources(include_secondary_certificate_baseline=True)
        layout_frame = generator.load_csv(layout_csv)
        paired_frame = generator.load_csv(paired_csv)
        claim_rows = generator.build_claim_contract_rows(layout_csv.parent, layout_csv, paired_csv)
        main_rows = generator.build_main_table_contract_rows(layout_frame, paired_frame, layout_csv.parent, layout_csv, paired_csv)

        policy = generator.build_claim_contract_policy(claim_rows, main_rows)

        self.assertEqual(policy["claim_contract_schema"], "trace_sl_claim_contract_v1")
        self.assertEqual(
            set(policy["main_table_layout_labels"]),
            {row["layout_type"] for row in main_rows},
        )
        self.assertIn("greedy_d_logdet", policy["main_table_layout_labels"])

    def test_source_tracking_rejects_raw_dataset_or_untracked_sources(self) -> None:
        generator = import_generator()
        raw_source = self.root / "TRC-23-02333" / "dataset" / "PeMS7_228" / "raw.csv"
        raw_source.parent.mkdir(parents=True, exist_ok=True)
        raw_source.write_text("value\n1\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "outside curated trace_sl_results"):
            generator.assert_source_is_tracked(self.root, raw_source)
        with self.assertRaisesRegex(ValueError, "raw dataset"):
            generator.assert_evidence_artifact_is_tracked(self.root, "TRC-23-02333/dataset/PeMS7_228/raw.csv")

        untracked_source = self.write_csv(
            "TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/untracked.csv",
            [{"budget": 0.1}],
        )
        with self.assertRaisesRegex(ValueError, "not committed/tracked"):
            generator.assert_source_is_tracked(self.root, untracked_source)
        with self.assertRaisesRegex(ValueError, "not committed/tracked"):
            generator.assert_evidence_artifact_is_tracked(
                self.root,
                "TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light",
            )


if __name__ == "__main__":
    unittest.main()
