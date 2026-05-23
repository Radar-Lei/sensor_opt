#!/usr/bin/env python3
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock


MODULE_PATH = Path(__file__).resolve().with_name("validate_phase6_reproducibility.py")
spec = importlib.util.spec_from_file_location("validate_phase6_reproducibility", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def write_text(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_csv(path, header, rows):
    write_text(path, header + "\n" + "\n".join(rows) + "\n")


class Phase6ValidatorTests(unittest.TestCase):
    def make_root(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        results = root / "TRC-23-02333" / "trace_sl_results"
        phase4 = root / ".planning" / "phases" / "04-core-experiment-evidence"
        phase5 = root / ".planning" / "phases" / "05-robustness-and-generality"
        phase6 = root / ".planning" / "phases" / "06-reproducibility-and-artifact-curation"
        for directory in [results, phase4, phase5, phase6, root / "scripts"]:
            directory.mkdir(parents=True, exist_ok=True)
        return temp, root

    def write_complete_manifest(self, root):
        results = root / "TRC-23-02333" / "trace_sl_results"
        stage_specs = [
            ("12", "pems7_228_stage12_baseline_portfolio", "scripts/run_stage12_pems7_228.sh", {"SEEDS": "25 26", "BUDGETS": "0.10 0.20", "RCSS_RANDOM_CANDIDATES": "50", "RCSS_QUALITY_CANDIDATES": "50"}),
            ("13", "pems7_228_stage13_candidate_sensitivity", "scripts/run_stage13_candidate_sensitivity_pems7_228.sh", {"SEEDS": "25", "BUDGETS": "0.20", "CANDIDATE_COUNTS": "50 100 200 500"}),
            ("14", "pems7_228_stage14_robustness", "scripts/run_stage14_pems7_228_robustness.sh", {"SEEDS": "25", "BUDGETS": "0.20", "RCSS_RANDOM_CANDIDATES": "10", "RCSS_QUALITY_CANDIDATES": "10"}),
            ("14", "pems7_228_stage14_candidate_sensitivity", "scripts/run_stage14_candidate_sensitivity_pems7_228.sh", {"SEEDS": "25", "BUDGETS": "0.20", "CANDIDATE_COUNTS": "50 100 200 500"}),
        ]
        stages = []
        for stage, directory, launcher, defaults in stage_specs:
            (results / directory).mkdir(parents=True, exist_ok=True)
            defaults = {**defaults, "PYTHON_BIN": "python", "OUTPUT_DIR": f"TRC-23-02333/trace_sl_results/{directory}"}
            stages.append({
                "stage": stage,
                "directory": f"TRC-23-02333/trace_sl_results/{directory}",
                "launcher": launcher,
                "launcher_exists": True,
                "launcher_defaults": defaults,
                "required_artifacts": [{"path": f"TRC-23-02333/trace_sl_results/{directory}/combined_metrics.csv", "exists": True}],
                "inventory": {"exists": True, "artifact_count": 1, "artifacts": [{"path": f"TRC-23-02333/trace_sl_results/{directory}/combined_metrics.csv", "size_bytes": 10}]},
            })
        manifest = {
            "manifest_schema": "trace-sl-reproducibility-manifest-v1",
            "curated_result_stages": stages,
            "environment": {"python": {"version": "3.12"}, "packages": {"pandas": {"available": True, "version": "3.0.1"}}},
            "git": {"commit": "abc123", "branch": "main", "tracked_raw_dataset_path_count": 0, "tracked_raw_dataset_paths": []},
            "policy": {"raw_dataset_prefix": "TRC-23-02333/dataset/", "raw_dataset_disposition": "ignored local input"},
        }
        write_text(results / "reproducibility_manifest.json", json.dumps(manifest))
        write_text(results / "REPRODUCIBILITY_MANIFEST.md", "# Manifest\nNo raw dataset evidence.\n")
        return manifest

    def write_paper_sources(self, root):
        paper = root / "TRC-23-02333" / "trace_sl_results" / "paper_sources"
        paper.mkdir(parents=True, exist_ok=True)
        write_csv(paper / "core_performance_table.csv", "source_stage,source_dir,source_csv,budget,layout_type,mean", ["stage12,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_layout_summary.csv,0.2,validation_swap_selected,1.0"])
        write_csv(paper / "paired_delta_table.csv", "source_stage,source_dir,source_csv,layout_type,baseline,mean_delta", ["stage12,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,validation_swap_selected,greedy_a_trace,-0.1"])
        write_csv(paper / "robustness_condition_table.csv", "source_stage,source_dir,source_csv,robustness_condition,layout_type,mean", ["stage14,TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness,gls_map_layout_summary.csv,baseline,validation_swap_selected,1.0"])
        write_csv(paper / "candidate_runtime_table.csv", "source_stage,source_dir,source_csv,candidate_count,runtime_seconds", ["stage14,TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity,runtime_candidate_sensitivity.csv,50,1.0"])
        write_csv(paper / "certificate_correlation_table.csv", "source_stage,source_dir,source_csv,method,certificate", ["stage12,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,certificate_correlation_summary.csv,gls_map,posterior_trace"])
        write_text(paper / "core_performance_table.md", "| source |\n|---|\n| generated |\n")
        write_text(paper / "README.md", "Every row has source_csv provenance and no raw dataset evidence.\n")

    def write_docs(self, root):
        results = root / "TRC-23-02333" / "trace_sl_results"
        write_text(results / "README.md", "Use reproducibility_manifest.json, REPRODUCIBILITY_MANIFEST.md, and paper_sources/ only. No raw dataset evidence.\n")
        write_text(root / ".planning" / "phases" / "06-reproducibility-and-artifact-curation" / "06-REPRODUCIBILITY-AUDIT.md", "REPRO-01 REPRO-02 REPRO-03 REPRO-04 REPRO-05. No raw dataset evidence.\n")

    def write_aggregates(self, root):
        results = root / "TRC-23-02333" / "trace_sl_results"
        stage12 = results / "pems7_228_stage12_baseline_portfolio"
        stage14 = results / "pems7_228_stage14_robustness"
        stage14cand = results / "pems7_228_stage14_candidate_sensitivity"
        stage13 = results / "pems7_228_stage13_candidate_sensitivity"
        for path in [stage12, stage14, stage14cand, stage13]:
            path.mkdir(parents=True, exist_ok=True)
        baseline_rows = [
            "gls_map,validation_swap_selected,0.2,baseline,",
            "gls_map,rcss_selected,0.2,baseline,",
            "gls_map,multistart_swap_by_validation,0.2,baseline,",
            "gls_map,greedy_a_trace,0.2,baseline,",
            "gls_map,greedy_d_logdet,0.2,baseline,",
            "gls_map,observability_proxy,0.2,baseline,",
            "gls_map,graph_sampling_laplacian,0.2,baseline,",
            "gls_map,qr_pod_modes,0.2,baseline,",
        ]
        write_csv(stage12 / "combined_metrics.csv", "method,layout_type,budget,robustness_condition,candidate_count", baseline_rows)
        robust_rows = baseline_rows + [f"gls_map,validation_swap_selected,0.2,{condition}," for condition in validator.REQUIRED_ROBUSTNESS_CONDITIONS]
        write_csv(stage14 / "combined_metrics.csv", "method,layout_type,budget,robustness_condition,candidate_count", robust_rows)
        candidate_rows = [f"gls_map,validation_swap_selected,0.2,baseline,{count}" for count in [50, 100, 200, 500]]
        write_csv(stage14cand / "combined_metrics.csv", "method,layout_type,budget,robustness_condition,candidate_count", candidate_rows)
        write_csv(stage13 / "combined_metrics.csv", "method,layout_type,budget,robustness_condition,candidate_count", candidate_rows[:2])

    def write_launchers(self, root):
        for script in validator.LAUNCHER_SCRIPTS:
            write_text(root / script, "#!/usr/bin/env bash\nset -euo pipefail\necho DRY_RUN\n")

    def write_complete_project(self, root):
        self.write_complete_manifest(root)
        self.write_paper_sources(root)
        self.write_docs(root)
        self.write_aggregates(root)
        self.write_launchers(root)

    def test_manifest_missing_required_metadata_fails_repro01(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        self.write_complete_project(root)
        manifest_path = root / "TRC-23-02333" / "trace_sl_results" / "reproducibility_manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["environment"]["packages"] = {}
        manifest["curated_result_stages"][0]["launcher_defaults"].pop("SEEDS")
        manifest["curated_result_stages"][1]["launcher_defaults"].pop("CANDIDATE_COUNTS")
        write_text(manifest_path, json.dumps(manifest))

        context = validator.ValidationContext(root)
        validator.validate_repro_01(context)

        self.assertTrue(context.has_failures("REPRO-01"), context.errors)
        self.assertIn("package metadata", " ".join(context.messages_for("REPRO-01")))
        self.assertIn("SEEDS", " ".join(context.messages_for("REPRO-01")))
        self.assertIn("candidate counts", " ".join(context.messages_for("REPRO-01")))

    def test_paper_source_missing_required_csv_or_source_csv_fails_repro04(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        self.write_complete_project(root)
        (root / "TRC-23-02333" / "trace_sl_results" / "paper_sources" / "paired_delta_table.csv").unlink()
        write_csv(
            root / "TRC-23-02333" / "trace_sl_results" / "paper_sources" / "core_performance_table.csv",
            "source_stage,source_dir,budget,layout_type,mean",
            ["stage12,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,0.2,validation_swap_selected,1.0"],
        )

        context = validator.ValidationContext(root)
        validator.validate_repro_04(context)

        self.assertTrue(context.has_failures("REPRO-04"), context.errors)
        messages = " ".join(context.messages_for("REPRO-04"))
        self.assertIn("paired_delta_table.csv", messages)
        self.assertIn("source_csv", messages)

    def test_tracked_raw_dataset_paths_fail_repro02_without_masking(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        self.write_complete_project(root)

        with mock.patch.object(validator, "git_ls_files", return_value=["TRC-23-02333/dataset/PeMS7_228/raw.csv"]):
            context = validator.ValidationContext(root)
            validator.validate_repro_02(context)

        self.assertTrue(context.has_failures("REPRO-02"), context.errors)
        self.assertIn("tracked raw dataset", " ".join(context.messages_for("REPRO-02")))

    def test_status_rendering_emits_one_row_for_each_repro_requirement(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        self.write_complete_project(root)
        context = validator.ValidationContext(root)
        context.pass_check("REPRO-01", "ok")
        context.fail("REPRO-02", "bad")
        context.pass_check("REPRO-03", "ok")
        context.pass_check("REPRO-04", "ok")
        context.pass_check("REPRO-05", "ok")

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            validator.print_status_rows(context)

        lines = [line for line in output.getvalue().splitlines() if line.startswith("REPRO-")]
        self.assertEqual([f"REPRO-0{i}" for i in range(1, 6)], [line.split()[0] for line in lines])
        self.assertEqual(5, len(lines))

    def test_required_smoke_command_set_covers_four_launchers_and_missing_one_fails_repro05(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        self.write_complete_project(root)
        commands = validator.required_smoke_commands(root)
        command_text = [" ".join(command.args) for command in commands]

        self.assertTrue(any("run_stage12_pems7_228.sh" in text and command.env.get("DRY_RUN") == "1" for text, command in zip(command_text, commands)))
        self.assertTrue(any("run_stage13_candidate_sensitivity_pems7_228.sh" in text and command.env.get("DRY_RUN") == "1" for text, command in zip(command_text, commands)))
        self.assertTrue(any("run_stage14_pems7_228_robustness.sh" in text and command.env.get("DRY_RUN") == "1" for text, command in zip(command_text, commands)))
        self.assertTrue(any("run_stage14_candidate_sensitivity_pems7_228.sh" in text and command.env.get("DRY_RUN") == "1" for text, command in zip(command_text, commands)))

        missing_stage13 = [command for command in commands if "run_stage13_candidate_sensitivity_pems7_228.sh" not in " ".join(command.args)]
        with mock.patch.object(validator, "required_smoke_commands", return_value=missing_stage13), \
             mock.patch.object(validator, "run_command", return_value=validator.CommandResult(0, "ok", "")):
            context = validator.ValidationContext(root)
            validator.validate_repro_05(context)

        self.assertTrue(context.has_failures("REPRO-05"), context.errors)
        self.assertIn("Stage 13 candidate sensitivity", " ".join(context.messages_for("REPRO-05")))


if __name__ == "__main__":
    unittest.main()
