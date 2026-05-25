#!/usr/bin/env python3
"""Regression tests for TRACE-SL theory and handoff contracts."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = PROJECT_ROOT / "scripts" / "generate_trace_sl_theory_handoff_contracts.py"


class TheoryHandoffContractGenerationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        subprocess.run(["git", "init", "--quiet"], cwd=self.root, check=True)

    def import_generator(self):
        spec = importlib.util.spec_from_file_location("generate_trace_sl_theory_handoff_contracts", GENERATOR_PATH)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not import generator from {GENERATOR_PATH}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def write_text(self, relative_path: str, content: str = "ok\n") -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def write_csv(self, relative_path: str) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame([{"value": 1}]).to_csv(path, index=False)
        return path

    def write_json(self, relative_path: str) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"ok": True}) + "\n", encoding="utf-8")
        return path

    def commit(self, *paths: Path) -> None:
        relatives = [path.relative_to(self.root).as_posix() for path in paths]
        subprocess.run(["git", "add", *relatives], cwd=self.root, check=True)
        subprocess.run(
            [
                "git",
                "-c",
                "user.name=Phase 10 Test",
                "-c",
                "user.email=phase10@example.invalid",
                "commit",
                "--quiet",
                "-m",
                "fixture handoff artifacts",
                "--",
                *relatives,
            ],
            cwd=self.root,
            check=True,
        )

    def make_required_artifacts(self) -> None:
        paths = [
            self.write_json("TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json"),
            self.write_csv("TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv"),
            self.write_json("TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.json"),
            self.write_json("TRC-23-02333/trace_sl_results/paper_sources/ablation_contract.json"),
            self.write_json("TRC-23-02333/trace_sl_results/paper_sources/dataset_evidence_classification.json"),
            self.write_json("TRC-23-02333/trace_sl_results/reproducibility_manifest.json"),
            self.write_text("TRC-23-02333/transparent_estimator_eval.py", "def posterior_trace_for_layout():\n    return 1\ndef validation_swap_search():\n    return []\n"),
        ]
        self.commit(*paths)

    def test_theory_rows_cover_all_theory_requirements_and_boundaries(self) -> None:
        generator = self.import_generator()
        self.make_required_artifacts()

        rows = generator.build_theory_rows(self.root)

        requirements = {row["requirement_id"] for row in rows}
        self.assertEqual(requirements, {"THEORY-01", "THEORY-02", "THEORY-03", "THEORY-04", "THEORY-05"})
        names = {row["statement_name"] for row in rows}
        self.assertIn("budgeted_hidden_network_reconstruction", names)
        self.assertIn("posterior_trace_squared_error_identity", names)
        self.assertIn("posterior_covariance_monotonicity", names)
        self.assertIn("validation_aware_one_swap_local_optimality", names)
        self.assertIn("rcss_candidate_search_evaluation_complexity", names)
        rendered = json.dumps(rows, sort_keys=True)
        self.assertIn("train/validation/test", rendered)
        self.assertIn("does not assert global optimality", rendered)
        self.assertNotIn("TRC-23-02333/dataset/", rendered)

    def test_handoff_manifest_links_committed_artifacts_without_manuscript_prose(self) -> None:
        generator = self.import_generator()
        self.make_required_artifacts()

        contracts = generator.build_all_contracts(self.root)
        rows = contracts["paper_foundation_handoff_manifest"]
        metadata = contracts["metadata"]

        self.assertEqual(metadata["schema"], "trace_sl_theory_handoff_contracts_v1")
        self.assertTrue(rows)
        artifact_types = {row["artifact_type"] for row in rows}
        self.assertIn("claim_contract", artifact_types)
        self.assertIn("theory_contract", artifact_types)
        self.assertIn("reproducibility_manifest", artifact_types)
        for row in rows:
            self.assertTrue(row["safe_for_writing"])
            self.assertTrue(row["raw_dataset_free"])
            self.assertEqual(row["manuscript_prose_status"], "not_manuscript_prose")
        rendered = json.dumps(contracts, sort_keys=True).lower()
        for heading in generator.FORBIDDEN_MANUSCRIPT_HEADINGS:
            self.assertNotIn(heading, rendered)
        self.assertNotIn("TRC-23-02333/dataset/", rendered)
        self.assertNotIn("raw_dataset_prefix", metadata)
        self.assertEqual(metadata["raw_dataset_policy_marker"], "protected local raw dataset input prefix")

    def test_uncommitted_or_dirty_handoff_artifacts_fail_closed(self) -> None:
        generator = self.import_generator()
        self.make_required_artifacts()
        claim_path = self.root / "TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json"
        claim_path.write_text(json.dumps({"dirty": True}) + "\n", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "uncommitted changes"):
            generator.build_all_contracts(self.root)

        with tempfile.TemporaryDirectory() as tmp:
            clean_root = Path(tmp)
            subprocess.run(["git", "init", "--quiet"], cwd=clean_root, check=True)
            raw_path = clean_root / "TRC-23-02333/dataset/PeMS7_228/raw.csv"
            raw_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path.write_text("raw\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "raw dataset"):
                generator.assert_artifact_is_safe(clean_root, "TRC-23-02333/dataset/PeMS7_228/raw.csv", "raw")

    def test_validate_rows_rejects_manuscript_heading_markers(self) -> None:
        generator = self.import_generator()
        row = dict(generator.THEORY_ROWS[0])
        row["statement_name"] = "introduction"

        with self.assertRaisesRegex(ValueError, "manuscript prose"):
            generator.validate_rows([row], generator.THEORY_STATEMENT_COLUMNS, "theory statement")


if __name__ == "__main__":
    unittest.main()
