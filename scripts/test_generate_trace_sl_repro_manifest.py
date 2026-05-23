#!/usr/bin/env python3
"""Regression tests for TRACE-SL reproducibility manifest generation."""

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from generate_trace_sl_repro_manifest import (  # noqa: E402
    collect_environment,
    inventory_result_dir,
    parse_shell_defaults,
)


class ManifestGeneratorTests(unittest.TestCase):
    def test_parse_shell_defaults_reads_assignments_without_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            launcher = Path(tmp) / "launcher.sh"
            launcher.write_text(
                "\n".join(
                    [
                        "#!/usr/bin/env bash",
                        "set -euo pipefail",
                        "SEEDS=\"${SEEDS:-25 26}\"",
                        "BUDGETS='${BUDGETS:-0.10 0.20}'",
                        "CANDIDATE_COUNTS=\"${CANDIDATE_COUNTS:-50 100 200}\"",
                        "OUTPUT_DIR=\"${OUTPUT_DIR:-TRC-23-02333/trace_sl_results/example}\"",
                        "SHOULD_NOT_RUN=$(printf executed)",
                    ]
                ),
                encoding="utf-8",
            )

            defaults = parse_shell_defaults(launcher)

        self.assertEqual(defaults["SEEDS"], ["25", "26"])
        self.assertEqual(defaults["BUDGETS"], ["0.10", "0.20"])
        self.assertEqual(defaults["CANDIDATE_COUNTS"], ["50", "100", "200"])
        self.assertEqual(
            defaults["OUTPUT_DIR"],
            "TRC-23-02333/trace_sl_results/example",
        )
        self.assertNotIn("SHOULD_NOT_RUN", defaults)

    def test_inventory_result_dir_records_artifacts_and_excludes_raw_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            result_dir = root / "TRC-23-02333" / "trace_sl_results" / "stage"
            result_dir.mkdir(parents=True)
            (result_dir / "combined_metrics.csv").write_text("method,mae\nrcss,1.0\n", encoding="utf-8")
            (result_dir / "SUMMARY.md").write_text("# Summary\n", encoding="utf-8")
            raw_file = root / "TRC-23-02333" / "dataset" / "PeMS7_228" / "raw.csv"
            raw_file.parent.mkdir(parents=True)
            raw_file.write_text("sensitive\n", encoding="utf-8")

            inventory = inventory_result_dir(root, result_dir)

        paths = {entry["path"] for entry in inventory["artifacts"]}
        self.assertIn("TRC-23-02333/trace_sl_results/stage/combined_metrics.csv", paths)
        self.assertIn("TRC-23-02333/trace_sl_results/stage/SUMMARY.md", paths)
        self.assertNotIn("TRC-23-02333/dataset/PeMS7_228/raw.csv", paths)
        self.assertTrue(all(entry["is_evidence_artifact"] for entry in inventory["artifacts"]))
        self.assertEqual(inventory["raw_dataset_policy"], "excluded_from_evidence")
        self.assertEqual(inventory["raw_dataset_prefix"], "TRC-23-02333/dataset/")

    def test_collect_environment_reports_python_and_optional_packages(self):
        environment = collect_environment()

        self.assertIn("python", environment)
        self.assertIn("version", environment["python"])
        packages = environment["packages"]
        for name in ("numpy", "pandas", "scipy", "scikit-learn", "sklearn"):
            self.assertIn(name, packages)
            self.assertIn("available", packages[name])
            self.assertIn("version", packages[name])


if __name__ == "__main__":
    unittest.main()
