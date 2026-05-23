#!/usr/bin/env python3
"""Regression tests for TRACE-SL paper-source generation."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = PROJECT_ROOT / "scripts" / "generate_trace_sl_paper_sources.py"


def import_generator():
    spec = importlib.util.spec_from_file_location("generate_trace_sl_paper_sources", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not import generator from {GENERATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PaperSourceGenerationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def write_csv(self, relative_path: str, rows: list[dict[str, object]]) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(rows).to_csv(path, index=False)
        return path

    def test_core_rows_filter_labels_and_preserve_provenance(self) -> None:
        generator = import_generator()
        source_csv = self.write_csv(
            "TRC-23-02333/trace_sl_results/stage12/gls_map_layout_summary.csv",
            [
                {"budget": 0.1, "layout_type": "validation_swap_selected", "mean": 1.2, "count": 2},
                {"budget": 0.1, "layout_type": "rcss_selected", "mean": 1.4, "count": 2},
                {"budget": 0.1, "layout_type": "unused_layout", "mean": 9.9, "count": 2},
            ],
        )

        frame = generator.load_csv(source_csv)
        rows = generator.build_core_performance_rows(
            frame,
            source_stage="stage12",
            source_dir=source_csv.parent,
            source_csv=source_csv,
            layout_labels=("validation_swap_selected", "rcss_selected"),
        )

        self.assertEqual([row["layout_type"] for row in rows], ["validation_swap_selected", "rcss_selected"])
        self.assertEqual({row["budget"] for row in rows}, {0.1})
        for row in rows:
            self.assertEqual(row["source_stage"], "stage12")
            self.assertEqual(row["source_dir"], "TRC-23-02333/trace_sl_results/stage12")
            self.assertEqual(row["source_csv"], "gls_map_layout_summary.csv")
            self.assertIn("mean", row)

    def test_robustness_rows_retain_condition_and_source_paths(self) -> None:
        generator = import_generator()
        source_csv = self.write_csv(
            "TRC-23-02333/trace_sl_results/stage14/gls_map_layout_summary.csv",
            [
                {
                    "budget": 0.2,
                    "robustness_condition": "failure_0.10",
                    "robustness_family": "sensor_failure",
                    "layout_type": "validation_swap_selected",
                    "mean": 2.5,
                    "count": 3,
                }
            ],
        )

        rows = generator.build_robustness_condition_rows(
            generator.load_csv(source_csv),
            source_stage="stage14_robustness",
            source_dir=source_csv.parent,
            source_csv=source_csv,
            layout_labels=("validation_swap_selected",),
        )

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["robustness_condition"], "failure_0.10")
        self.assertEqual(rows[0]["robustness_family"], "sensor_failure")
        self.assertEqual(rows[0]["source_stage"], "stage14_robustness")
        self.assertEqual(rows[0]["source_dir"], "TRC-23-02333/trace_sl_results/stage14")
        self.assertEqual(rows[0]["source_csv"], "gls_map_layout_summary.csv")

    def test_missing_required_core_layout_label_fails_closed(self) -> None:
        generator = import_generator()
        source_csv = self.write_csv(
            "TRC-23-02333/trace_sl_results/stage12/gls_map_layout_summary.csv",
            [
                {"budget": 0.1, "layout_type": "validation_swap_selected", "mean": 1.2},
            ],
        )

        with self.assertRaisesRegex(ValueError, "missing required layout_type"):
            generator.build_core_performance_rows(
                generator.load_csv(source_csv),
                source_stage="stage12",
                source_dir=source_csv.parent,
                source_csv=source_csv,
                layout_labels=("validation_swap_selected", "rcss_selected"),
            )

    def test_markdown_rendering_is_deterministic_and_csv_backed(self) -> None:
        generator = import_generator()
        rows = [
            {"budget": 0.1, "layout_type": "validation_swap_selected", "mean": 1.234567, "source_stage": "stage12"},
            {"budget": 0.2, "layout_type": "rcss_selected", "mean": 2.0, "source_stage": "stage12"},
        ]
        columns = ["budget", "layout_type", "mean", "source_stage"]

        first = generator.markdown_table(rows, columns)
        second = generator.markdown_table(rows, columns)

        self.assertEqual(first, second)
        self.assertIn("| budget | layout_type | mean | source_stage |", first)
        self.assertIn("| 0.1 | validation_swap_selected | 1.234567 | stage12 |", first)
        self.assertNotIn("unused_layout", first)
        self.assertNotIn("not available", first.lower())


if __name__ == "__main__":
    unittest.main()
