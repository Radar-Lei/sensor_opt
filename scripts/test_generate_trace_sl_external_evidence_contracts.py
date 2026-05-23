#!/usr/bin/env python3
"""Regression tests for TRACE-SL external Stage12 evidence contracts."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = PROJECT_ROOT / "scripts" / "generate_trace_sl_external_evidence_contracts.py"


def import_generator():
    spec = importlib.util.spec_from_file_location("generate_trace_sl_external_evidence_contracts", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not import generator from {GENERATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ExternalEvidenceContractGenerationTests(unittest.TestCase):
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

    def write_text(self, relative_path: str, content: str = "status: complete\n") -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def track(self, *relative_paths: str) -> None:
        subprocess.run(["git", "add", *relative_paths], cwd=self.root, check=True)

    def combined_rows(self, split_count: int = 10) -> list[dict[str, object]]:
        seeds = list(range(25, 25 + split_count))
        rows: list[dict[str, object]] = []
        for seed in seeds:
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

    def layout_rows(self, split_count: int = 10) -> list[dict[str, object]]:
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
        rows: list[dict[str, object]] = []
        for budget in (0.10, 0.20, 0.30):
            for index, label in enumerate(labels):
                rows.append(
                    {
                        "budget": budget,
                        "layout_type": label,
                        "mean": 3.0 + budget + index / 100.0,
                        "std": 0.1 + index / 1000.0,
                        "count": split_count if label != "random" else split_count * 50,
                        "rmse_mean": 4.0 + index / 100.0,
                        "mape_mean": 0.2 + index / 1000.0,
                    }
                )
        return rows

    def paired_rows(self, missing_stat: bool = False) -> list[dict[str, object]]:
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
                        "paired_t_p": "" if missing_stat and baseline == "random" else 0.01,
                        "wilcoxon_p": 0.02,
                        "win_count": 9,
                        "count": 10,
                    }
                )
        return rows

    def make_stage12_sources(
        self,
        directory_name: str,
        split_count: int = 10,
        tracked: bool = True,
        missing_paired_stat: bool = False,
        status_payload: dict[str, object] | None = None,
    ) -> Path:
        base = f"TRC-23-02333/trace_sl_results/{directory_name}"
        paths = [
            self.write_text(f"{base}/SUMMARY.md", "status: complete\n"),
            self.write_csv(f"{base}/combined_metrics.csv", self.combined_rows(split_count)),
            self.write_csv(f"{base}/gls_map_layout_summary.csv", self.layout_rows(split_count)),
            self.write_csv(f"{base}/gls_map_delta_summary.csv", [{"budget": 0.10, "layout": "validation_swap_selected"}]),
            self.write_csv(f"{base}/gls_map_paired_delta_tests.csv", self.paired_rows(missing_paired_stat)),
            self.write_csv(f"{base}/gls_map_win_counts.csv", [{"budget": 0.10, "best_layout": "validation_swap_selected", "wins": 10}]),
            self.write_csv(f"{base}/rcss_selected_sources.csv", [{"budget": 0.10, "source": "quality"}]),
        ]
        if status_payload is not None:
            paths.append(self.write_text(f"{base}/stage12_status.json", json.dumps(status_payload) + "\n"))
        if tracked:
            self.track(*(path.relative_to(self.root).as_posix() for path in paths))
        return self.root / base

    def test_ten_split_tracked_pems_and_seattle_allow_v1_1_completion(self) -> None:
        generator = import_generator()
        self.make_stage12_sources("pems7_1026_stage12_baseline_portfolio")
        self.make_stage12_sources("seattle_stage12_baseline_portfolio", status_payload={"status": "completed"})

        contracts = generator.build_all_contracts(self.root)

        rows = contracts["external_evidence_contract"]
        gate = contracts["external_evidence_gate"]
        self.assertTrue(gate["pems7_1026_stage12_complete"])
        self.assertTrue(gate["seattle_stage12_complete"])
        self.assertTrue(gate["v1_1_completion_allowed"])
        self.assertFalse(gate["seattle_core_claim_blocked"])
        self.assertTrue(rows)
        completed = [row for row in rows if row["evidence_status"] == "completed"]
        self.assertTrue(completed)
        self.assertEqual({row["actual_split_count"] for row in completed}, {10})
        self.assertTrue(all(row["core_claim_eligible"] for row in completed))

    def test_untracked_aggregate_sources_are_pending_tracking_not_complete(self) -> None:
        generator = import_generator()
        self.make_stage12_sources("pems7_1026_stage12_baseline_portfolio", tracked=False)
        self.make_stage12_sources("seattle_stage12_baseline_portfolio", tracked=False)

        contracts = generator.build_all_contracts(self.root)
        gate = contracts["external_evidence_gate"]

        self.assertFalse(gate["pems7_1026_stage12_complete"])
        self.assertFalse(gate["seattle_stage12_complete"])
        self.assertFalse(gate["v1_1_completion_allowed"])
        statuses = {row["dataset"]: row["evidence_status"] for row in contracts["external_evidence_contract"]}
        self.assertEqual(statuses["PeMS7_1026"], "pending_tracking")
        self.assertEqual(statuses["Seattle"], "pending_tracking")

    def test_stage11_directory_is_rejected_as_stage12_completion(self) -> None:
        generator = import_generator()
        stage11_dir = self.make_stage12_sources("pems7_1026_stage11_auto_weight")
        spec = dict(generator.DATASET_SPECS[0], result_dir=stage11_dir.relative_to(self.root))

        dataset = generator.build_dataset_contract(self.root, spec)

        self.assertEqual(dataset["summary"]["evidence_status"], "blocked")
        self.assertFalse(dataset["summary"]["stage12_complete"])
        self.assertIn("Stage11", dataset["summary"]["blocker_reason"])

    def test_raw_dataset_paths_raise_hygiene_errors(self) -> None:
        generator = import_generator()
        spec = dict(generator.DATASET_SPECS[0], result_dir=Path("TRC-23-02333/dataset/PeMS7_1026"))

        with self.assertRaisesRegex(ValueError, "raw dataset"):
            generator.build_dataset_contract(self.root, spec)
        with self.assertRaisesRegex(ValueError, "raw dataset"):
            generator.assert_no_raw_dataset_path("TRC-23-02333/dataset/Seattle/tensor.npz", "evidence artifact")

    def test_seattle_status_json_is_authoritative_blocker(self) -> None:
        generator = import_generator()
        self.make_stage12_sources("pems7_1026_stage12_baseline_portfolio")
        status_path = self.write_text(
            "TRC-23-02333/trace_sl_results/seattle_stage12_baseline_portfolio/stage12_status.json",
            json.dumps({"status": "blocked", "blocker_reason": "Seattle run incomplete"}) + "\n",
        )
        self.track(status_path.relative_to(self.root).as_posix())

        contracts = generator.build_all_contracts(self.root)
        gate = contracts["external_evidence_gate"]
        seattle = gate["datasets"]["Seattle"]

        self.assertFalse(gate["seattle_stage12_complete"])
        self.assertTrue(gate["seattle_core_claim_blocked"])
        self.assertEqual(seattle["evidence_status"], "blocked")
        self.assertIn("Seattle run incomplete", seattle["blocker_reason"])

    def test_paired_statistics_are_honest_and_missing_pairs_are_descriptive_only(self) -> None:
        generator = import_generator()
        self.make_stage12_sources("pems7_1026_stage12_baseline_portfolio")
        self.make_stage12_sources("seattle_stage12_baseline_portfolio", status_payload={"status": "completed"})

        contracts = generator.build_all_contracts(self.root)
        rows = contracts["external_evidence_contract"]

        descriptive = [row for row in rows if row["layout_type"] == "rcss_selected"]
        self.assertTrue(descriptive)
        for row in descriptive:
            self.assertEqual(row["paired_evidence_status"], "descriptive_only")
            self.assertEqual(row["source_csv"], "gls_map_layout_summary.csv")
            self.assertEqual(row["delta_mean"], "")

        paired = [row for row in rows if row["layout_type"] == "random"]
        self.assertTrue(paired)
        for row in paired:
            self.assertEqual(row["paired_evidence_status"], "paired_stats_available")
            self.assertIn("gls_map_paired_delta_tests.csv", row["source_csv"])
            self.assertNotEqual(row["paired_t_p"], "")

        self.tmp.cleanup()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        subprocess.run(["git", "init", "--quiet"], cwd=self.root, check=True)
        self.make_stage12_sources("pems7_1026_stage12_baseline_portfolio", missing_paired_stat=True)
        with self.assertRaisesRegex(ValueError, "paired_stats_available row missing paired statistics"):
            generator.build_dataset_contract(self.root, generator.DATASET_SPECS[0])

    def test_seattle_core_eligibility_fails_closed_without_ten_splits(self) -> None:
        generator = import_generator()
        self.make_stage12_sources("pems7_1026_stage12_baseline_portfolio")
        self.make_stage12_sources("seattle_stage12_baseline_portfolio", split_count=9, status_payload={"status": "completed"})

        contracts = generator.build_all_contracts(self.root)
        gate = contracts["external_evidence_gate"]
        seattle = gate["datasets"]["Seattle"]

        self.assertFalse(gate["seattle_stage12_complete"])
        self.assertTrue(gate["seattle_core_claim_blocked"])
        self.assertFalse(seattle["core_claim_eligible"])
        self.assertEqual(seattle["actual_split_count"], 9)
        self.assertIn("10 split", seattle["blocker_reason"])


if __name__ == "__main__":
    unittest.main()
