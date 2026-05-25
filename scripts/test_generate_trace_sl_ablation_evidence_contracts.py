#!/usr/bin/env python3
"""Regression tests for TRACE-SL ablation and evidence-classification contracts."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = PROJECT_ROOT / "scripts" / "generate_trace_sl_ablation_evidence_contracts.py"


REQUIRED_LAYOUTS = {
    "random",
    "best_random_by_validation",
    "greedy_a_trace",
    "rcss_selected",
    "validation_swap_selected",
    "multistart_swap_by_validation",
}


class AblationEvidenceContractGenerationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        subprocess.run(["git", "init", "--quiet"], cwd=self.root, check=True)

    def write_csv(self, relative_path: str, rows: list[dict[str, object]]) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(rows).to_csv(path, index=False)
        return path

    def write_json(self, relative_path: str, payload: dict[str, object]) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path

    def write_text(self, relative_path: str, content: str = "status: complete\n") -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def track(self, *paths: Path) -> None:
        relatives = [path.relative_to(self.root).as_posix() for path in paths]
        subprocess.run(["git", "add", *relatives], cwd=self.root, check=True)

    def import_generator(self):
        spec = importlib.util.spec_from_file_location("generate_trace_sl_ablation_evidence_contracts", GENERATOR_PATH)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not import generator from {GENERATOR_PATH}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def layout_rows(self, layouts: list[str] | None = None, split_count: int = 10) -> list[dict[str, object]]:
        labels = layouts or [
            "validation_swap_selected",
            "multistart_swap_by_validation",
            "rcss_selected",
            "best_random_by_validation",
            "random",
            "top_variance",
            "greedy_a_trace",
            "greedy_d_logdet",
            "graph_sampling_laplacian",
            "observability_proxy",
            "qr_pod_modes",
        ]
        rows: list[dict[str, object]] = []
        for budget in (0.10, 0.20, 0.30):
            for index, label in enumerate(labels):
                rows.append(
                    {
                        "budget": budget,
                        "layout_type": label,
                        "mean": 3.0 + budget + index / 100.0,
                        "std": 0.10 + index / 1000.0,
                        "count": split_count if label != "random" else split_count * 50,
                        "rmse_mean": 4.0 + index / 100.0,
                        "mape_mean": 0.20 + index / 1000.0,
                    }
                )
        return rows

    def paired_rows(self) -> list[dict[str, object]]:
        baselines = [
            "multistart_swap_by_validation",
            "best_random_by_validation",
            "random",
            "top_variance",
            "greedy_a_trace",
            "greedy_d_logdet",
            "graph_sampling_laplacian",
            "observability_proxy",
            "qr_pod_modes",
        ]
        rows: list[dict[str, object]] = []
        for budget in (0.10, 0.20, 0.30):
            for index, baseline in enumerate(baselines):
                rows.append(
                    {
                        "budget": budget,
                        "layout": "validation_swap_selected",
                        "baseline": baseline,
                        "delta_mean": -0.01 * (index + 1),
                        "ci95_low": -0.02 * (index + 1),
                        "ci95_high": -0.001,
                        "paired_t_p": 0.01,
                        "wilcoxon_p": 0.02,
                        "win_count": 9,
                        "count": 10,
                    }
                )
        return rows

    def combined_rows(self, split_count: int = 10) -> list[dict[str, object]]:
        rows: list[dict[str, object]] = []
        for seed in range(25, 25 + split_count):
            for budget in (0.10, 0.20, 0.30):
                rows.append(
                    {
                        "dataset": "fixture",
                        "split_seed": seed,
                        "budget": budget,
                        "method": "gls_map",
                        "layout_type": "validation_swap_selected",
                        "mae": 3.0 + budget,
                    }
                )
        return rows

    def make_core_stage12_sources(self, layouts: list[str] | None = None) -> list[Path]:
        base = "TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio"
        paths = [
            self.write_text(f"{base}/SUMMARY.md"),
            self.write_csv(f"{base}/combined_metrics.csv", self.combined_rows()),
            self.write_csv(f"{base}/gls_map_layout_summary.csv", self.layout_rows(layouts)),
            self.write_csv(f"{base}/gls_map_paired_delta_tests.csv", self.paired_rows()),
            self.write_csv(f"{base}/gls_map_win_counts.csv", [{"budget": 0.10, "best_layout": "validation_swap_selected", "wins": 10}]),
            self.write_csv(f"{base}/rcss_selected_sources.csv", [{"budget": 0.10, "source": "quality", "selected_count": 4}]),
        ]
        self.track(*paths)
        return paths

    def make_external_gate(self, pems_complete: bool = False, seattle_complete: bool = False, seattle_status: str = "blocked") -> Path:
        path = self.write_json(
            "TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.json",
            {
                "gate_schema": "trace_sl_external_evidence_gate_v1",
                "generated_at_utc": "1970-01-01T00:00:00Z",
                "generated_by": "scripts/generate_trace_sl_external_evidence_contracts.py",
                "required_split_count": 10,
                "pems7_1026_stage12_complete": pems_complete,
                "seattle_stage12_complete": seattle_complete,
                "seattle_core_claim_blocked": not seattle_complete,
                "v1_1_completion_allowed": pems_complete and seattle_complete,
                "datasets": {
                    "PeMS7_1026": {
                        "dataset": "PeMS7_1026",
                        "actual_split_count": 1 if not pems_complete else 10,
                        "required_split_count": 10,
                        "evidence_status": "completed" if pems_complete else "blocked",
                        "stage12_complete": pems_complete,
                        "core_claim_eligible": pems_complete,
                        "blocker_reason": "one-seed feasibility is non-evidence" if not pems_complete else "",
                        "source_dir": "TRC-23-02333/trace_sl_results/pems7_1026_stage12_feasibility_seed25",
                    },
                    "Seattle": {
                        "dataset": "Seattle",
                        "actual_split_count": 1 if not seattle_complete else 10,
                        "required_split_count": 10,
                        "evidence_status": "completed" if seattle_complete else seattle_status,
                        "stage12_complete": seattle_complete,
                        "core_claim_eligible": seattle_complete,
                        "blocker_reason": "Seattle Stage12 incomplete" if not seattle_complete else "",
                        "source_dir": "TRC-23-02333/trace_sl_results/seattle_stage12_feasibility_seed25",
                    },
                },
                "policy": {"raw_dataset_prefix": "TRC-23-02333/dataset/"},
            },
        )
        self.track(path)
        return path

    def test_ablation_contract_includes_required_families_and_layer_fields(self) -> None:
        generator = self.import_generator()
        self.make_core_stage12_sources()
        self.make_external_gate()

        rows = generator.build_ablation_contract(self.root)

        layout_types = {str(row["layout_type"]) for row in rows}
        self.assertTrue(REQUIRED_LAYOUTS.issubset(layout_types))
        layers = {str(row["component_layer"]) for row in rows}
        self.assertIn("certificate_candidate_generation", layers)
        self.assertIn("validation_based_candidate_selection", layers)
        self.assertIn("validation_aware_local_refinement", layers)
        for row in rows:
            rendered = json.dumps(row, sort_keys=True)
            self.assertNotIn("TRC-23-02333/dataset/", rendered)
            self.assertNotEqual(row.get("evidence_basis"), "validation_mae")
        caveat_rows = [row for row in rows if str(row["layout_type"]) == "multistart_swap_by_validation" or float(row["budget"]) == 0.1]
        self.assertTrue(caveat_rows)
        self.assertTrue(any(row["caveat_tag"] == "pems7_228_low_budget_multistart_not_dominant" for row in caveat_rows))

    def test_missing_required_core_layout_label_fails_closed(self) -> None:
        generator = self.import_generator()
        layouts = sorted(REQUIRED_LAYOUTS.difference({"random"}))
        self.make_core_stage12_sources(layouts=layouts)
        self.make_external_gate()

        with self.assertRaisesRegex(ValueError, "missing required layout_type"):
            generator.build_ablation_contract(self.root)

    def test_external_and_feasibility_sources_do_not_complete_evid_03_or_evid_04(self) -> None:
        generator = self.import_generator()
        self.make_core_stage12_sources()
        self.make_external_gate(pems_complete=False, seattle_complete=False)
        feasibility_paths = [
            self.write_csv("TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/gls_map_layout_summary.csv", self.layout_rows()),
            self.write_csv("TRC-23-02333/trace_sl_results/pems7_1026_stage12_feasibility_seed25/gls_map_layout_summary.csv", self.layout_rows(split_count=1)),
            self.write_json("TRC-23-02333/trace_sl_results/seattle_stage12_feasibility_seed25/stage12_status.json", {"status": "completed"}),
        ]
        self.track(*feasibility_paths)

        rows = generator.build_dataset_classification(self.root)
        by_dataset = {str(row["dataset"]): row for row in rows}

        pems = by_dataset["PeMS7_1026"]
        self.assertEqual(pems["evid_requirement"], "EVID-03")
        self.assertFalse(pems["requirement_complete"])
        self.assertIn(pems["evidence_lane"], {"external", "supporting", "conditional"})
        self.assertIn("non-evidence", pems["blocker_reason"])
        seattle = by_dataset["Seattle"]
        self.assertEqual(seattle["evid_requirement"], "EVID-04")
        self.assertFalse(seattle["core_claim_eligible"])
        self.assertFalse(seattle["requirement_complete"])
        self.assertIn(seattle["evidence_lane"], {"conditional", "blocked"})

    def test_build_all_contracts_metadata_is_deterministic_and_raw_paths_are_rejected(self) -> None:
        generator = self.import_generator()
        self.make_core_stage12_sources()
        self.make_external_gate()

        contracts = generator.build_all_contracts(self.root)

        self.assertTrue(contracts["ablation_contract"])
        self.assertTrue(contracts["dataset_evidence_classification"])
        metadata = contracts["metadata"]
        self.assertEqual(metadata["schema"], "trace_sl_ablation_evidence_contracts_v1")
        self.assertEqual(metadata["generated_at_utc"], "1970-01-01T00:00:00Z")
        self.assertFalse(metadata["external_gate_snapshot"]["pems7_1026_stage12_complete"])
        self.assertFalse(metadata["external_gate_snapshot"]["seattle_stage12_complete"])
        self.assertFalse(metadata["external_gate_snapshot"]["v1_1_completion_allowed"])
        rendered_rows = json.dumps(
            {
                "ablation_contract": contracts["ablation_contract"],
                "dataset_evidence_classification": contracts["dataset_evidence_classification"],
            },
            sort_keys=True,
        )
        self.assertNotIn("TRC-23-02333/dataset/", rendered_rows)
        with self.assertRaisesRegex(ValueError, "raw dataset"):
            generator.assert_no_raw_dataset_path("TRC-23-02333/dataset/PeMS7_228/PeMSD7_V_228.csv", "provenance")


if __name__ == "__main__":
    unittest.main()
