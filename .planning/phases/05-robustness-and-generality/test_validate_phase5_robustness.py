import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = Path(__file__).resolve().with_name("validate_phase5_robustness.py")
REQUIRED_COUNTS = [50, 100, 200, 500]


def write_csv(path, rows, fieldnames=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def gls_row(condition, family, **overrides):
    row = {
        "method": "gls_map",
        "mae": 1.0,
        "rmse": 1.1,
        "mape": 0.1,
        "dataset": "PeMS7_228",
        "budget": 0.1,
        "layout_type": "validation_swap_selected",
        "split_seed": 25,
        "robustness_family": family,
        "robustness_condition": condition,
        "failure_rate": 0.0,
        "noise_scale": 0.0,
        "missing_rate": 0.0,
        "missing_block_steps": 0,
        "split_mode": "random",
        "cost_proxy": "none",
        "cost_budget": 0.0,
        "layout_sensor_cost": 0.0,
        "cost_feasible": True,
        "selected_sensor_count": 23,
        "active_sensor_count": 23,
        "dropped_sensor_count": 0,
    }
    row.update(overrides)
    return row


def full_robustness_rows():
    rows = [gls_row("baseline", "baseline")]
    rows.extend(
        [
            gls_row("failure_0.05", "sensor_failure", failure_rate=0.05, active_sensor_count=22, dropped_sensor_count=1),
            gls_row("failure_0.10", "sensor_failure", failure_rate=0.10, active_sensor_count=21, dropped_sensor_count=2),
            gls_row("failure_0.20", "sensor_failure", failure_rate=0.20, active_sensor_count=18, dropped_sensor_count=5),
            gls_row("noise_0.05", "observation_noise", noise_scale=0.05),
            gls_row("random_missing_0.10", "random_missing", missing_rate=0.10),
            gls_row("block_missing_12", "block_missing", missing_block_steps=12),
            gls_row("cost_proxy_budget", "cost_proxy", cost_proxy="traffic_degree_proxy", cost_budget=45.0, layout_sensor_cost=40.0, cost_feasible=True),
            gls_row("chronological_split", "temporal_shift", split_mode="chronological"),
        ]
    )
    return rows


def candidate_metric_rows(counts=REQUIRED_COUNTS):
    rows = []
    for count in counts:
        rows.append(
            {
                "method": "gls_map",
                "mae": 1.0,
                "dataset": "PeMS7_228",
                "budget": 0.1,
                "layout_type": "validation_swap_selected",
                "split_seed": 25,
                "candidate_count": count,
            }
        )
    return rows


def candidate_robustness_values(condition="baseline", family="baseline"):
    return {
        "robustness_family": family,
        "robustness_condition": condition,
        "failure_rate": 0.05 if condition == "failure_0.05" else 0.0,
        "noise_scale": 0.05 if condition == "noise_0.05" else 0.0,
        "missing_rate": 0.10 if condition == "random_missing_0.10" else 0.0,
        "missing_block_steps": 12 if condition == "block_missing_12" else 0,
        "cost_proxy": "traffic_degree_proxy" if condition == "cost_proxy_budget" else "none",
        "cost_budget": 45.0 if condition == "cost_proxy_budget" else 0.0,
        "split_mode": "chronological" if condition == "chronological_split" else "random",
    }


def candidate_condition_rows():
    return [
        ("baseline", "baseline"),
        ("failure_0.05", "sensor_failure"),
        ("failure_0.10", "sensor_failure"),
        ("failure_0.20", "sensor_failure"),
        ("noise_0.05", "observation_noise"),
        ("random_missing_0.10", "random_missing"),
        ("block_missing_12", "block_missing"),
        ("cost_proxy_budget", "cost_proxy"),
        ("chronological_split", "temporal_shift"),
    ]


def candidate_summary_rows(counts=REQUIRED_COUNTS):
    rows = []
    for count in counts:
        for condition, family in candidate_condition_rows():
            rows.append(
                {
                    "budget": 0.1,
                    "candidate_count": count,
                    "source": "quality_coverage",
                    "candidate_row_count": count,
                    "selected_count": 1,
                    **candidate_robustness_values(condition, family),
                }
            )
    return rows


def rcss_candidate_rows():
    rows = []
    for condition, family in candidate_condition_rows():
        rows.append(
            {
                "budget": 0.1,
                "source": "quality_coverage",
                "candidate_count": 50,
                "selected": True,
                "validation_mae": 1.0,
                "sensors": "[1, 2]",
                **candidate_robustness_values(condition, family),
            }
        )
    return rows


def selected_source_rows():
    return [
        {
            "budget": 0.1,
            "source": "quality_coverage",
            "selected_count": 1,
            **candidate_robustness_values(condition, family),
        }
        for condition, family in candidate_condition_rows()
    ]


def runtime_rows(counts=REQUIRED_COUNTS):
    return [
        {
            "candidate_count": count,
            "status": "success",
            "runtime_seconds": float(count) / 10.0,
            "count": 1,
        }
        for count in counts
    ]


def timing_rows(counts=REQUIRED_COUNTS):
    return [
        {
            "candidate_count": count,
            "seed": 25,
            "runtime_seconds": float(count) / 10.0,
            "status": "success",
        }
        for count in counts
    ]


def create_complete_artifacts(root, candidate_counts=REQUIRED_COUNTS):
    result_root = root / "TRC-23-02333" / "trace_sl_results"
    robustness = result_root / "pems7_228_stage14_robustness"
    candidates = result_root / "pems7_228_stage14_candidate_sensitivity"
    robustness.mkdir(parents=True, exist_ok=True)
    candidates.mkdir(parents=True, exist_ok=True)

    robust_rows = full_robustness_rows()
    write_csv(robustness / "combined_metrics.csv", robust_rows)
    write_csv(robustness / "gls_map_layout_summary.csv", robust_rows)
    write_csv(robustness / "gls_map_paired_delta_tests.csv", robust_rows)
    write_csv(robustness / "combined_rcss_candidates.csv", rcss_candidate_rows())
    write_csv(robustness / "candidate_sensitivity_summary.csv", candidate_summary_rows(candidate_counts))
    write_csv(robustness / "rcss_selected_sources.csv", selected_source_rows())
    (robustness / "SUMMARY.md").write_text("Stage 14 robustness summary\n", encoding="utf-8")

    write_csv(candidates / "combined_metrics.csv", candidate_metric_rows(candidate_counts))
    write_csv(candidates / "candidate_sensitivity_summary.csv", candidate_summary_rows(candidate_counts))
    write_csv(candidates / "runtime_candidate_sensitivity.csv", runtime_rows(candidate_counts))
    write_csv(candidates / "stage14_timing.csv", timing_rows(candidate_counts))
    (candidates / "SUMMARY.md").write_text("Stage 14 candidate summary\n", encoding="utf-8")
    return robustness, candidates


def run_validator(root):
    return subprocess.run(
        [sys.executable, str(VALIDATOR), "--project-root", str(root)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


class Phase5RobustnessValidatorTests(unittest.TestCase):
    def test_complete_synthetic_artifacts_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            create_complete_artifacts(Path(tmp))
            result = run_validator(Path(tmp))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for token in ["ROBUST-01 PASS", "ROBUST-02 PASS", "ROBUST-03 PASS", "ROBUST-04 PASS", "ROBUST-05 PASS", "ROBUST-06 PASS"]:
            self.assertIn(token, result.stdout)

    def test_missing_core_robustness_artifact_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            robustness, _ = create_complete_artifacts(Path(tmp))
            (robustness / "combined_metrics.csv").unlink()
            result = run_validator(Path(tmp))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ROBUST-01 FAIL", result.stdout)

    def test_missing_required_condition_column_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            robustness, _ = create_complete_artifacts(Path(tmp))
            rows = full_robustness_rows()
            fieldnames = [name for name in rows[0].keys() if name != "noise_scale"]
            write_csv(robustness / "combined_metrics.csv", rows, fieldnames=fieldnames)
            result = run_validator(Path(tmp))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ROBUST-02 FAIL", result.stdout)
        self.assertIn("noise_scale", result.stdout)

    def test_candidate_summary_missing_condition_column_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            robustness, _ = create_complete_artifacts(Path(tmp))
            rows = candidate_summary_rows()
            fieldnames = [name for name in rows[0].keys() if name != "robustness_condition"]
            write_csv(robustness / "candidate_sensitivity_summary.csv", rows, fieldnames=fieldnames)
            selected_rows = selected_source_rows()
            selected_fieldnames = [name for name in selected_rows[0].keys() if name != "robustness_condition"]
            write_csv(robustness / "rcss_selected_sources.csv", selected_rows, fieldnames=selected_fieldnames)
            result = run_validator(Path(tmp))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ROBUST-01 FAIL", result.stdout)
        self.assertIn("candidate_sensitivity_summary", result.stdout)
        self.assertIn("rcss_selected_sources", result.stdout)

    def test_raw_dataset_doc_scan_helper_detects_curated_reference(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location("validator_under_test", VALIDATOR)
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            doc = root / "evidence.md"
            doc.write_text("bad evidence path TRC-23-02333/dataset/PeMS7_228/file.csv\n", encoding="utf-8")
            offenders = validator.docs_referencing_raw_dataset(root, [Path("evidence.md")])
        self.assertEqual(offenders, ["evidence.md"])

    def test_missing_candidate_runtime_coverage_fails_without_caveat(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, candidates = create_complete_artifacts(Path(tmp))
            write_csv(candidates / "runtime_candidate_sensitivity.csv", runtime_rows([50, 100, 200]))
            result = run_validator(Path(tmp))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ROBUST-06 FAIL", result.stdout)
        self.assertIn("500", result.stdout)

    def test_valid_candidate_count_caveat_warns_and_exits_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, candidates = create_complete_artifacts(Path(tmp), candidate_counts=[50, 100, 200])
            caveat = {
                "requirement": "ROBUST-06",
                "allowed_exception": True,
                "missing_candidate_counts": [500],
                "completed_candidate_counts": [50, 100, 200],
                "reason": "500-candidate local run exceeded limited tractability budget after evidence attempt.",
                "evidence_attempted": True,
                "validator_disposition": "WARN: limited tractability exception accepted",
            }
            (candidates / "candidate_sensitivity_caveat.json").write_text(json.dumps(caveat), encoding="utf-8")
            result = run_validator(Path(tmp))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("ROBUST-06 WARN", result.stdout)
        self.assertIn("limited tractability", result.stdout.lower())

    def write_valid_candidate_caveat(self, candidates):
        caveat = {
            "requirement": "ROBUST-06",
            "allowed_exception": True,
            "missing_candidate_counts": [500],
            "completed_candidate_counts": [50, 100, 200],
            "reason": "500-candidate local run exceeded limited tractability budget after evidence attempt.",
            "evidence_attempted": True,
            "validator_disposition": "WARN: limited tractability exception accepted",
        }
        (candidates / "candidate_sensitivity_caveat.json").write_text(json.dumps(caveat), encoding="utf-8")

    def test_valid_candidate_count_caveat_does_not_hide_missing_core_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, candidates = create_complete_artifacts(Path(tmp), candidate_counts=[50, 100, 200])
            (candidates / "SUMMARY.md").unlink()
            self.write_valid_candidate_caveat(candidates)
            result = run_validator(Path(tmp))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ROBUST-06 FAIL", result.stdout)
        self.assertIn("SUMMARY.md", result.stdout)

    def test_valid_candidate_count_caveat_does_not_hide_runtime_schema_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, candidates = create_complete_artifacts(Path(tmp), candidate_counts=[50, 100, 200])
            rows = runtime_rows([50, 100, 200])
            fieldnames = [name for name in rows[0].keys() if name != "runtime_seconds"]
            write_csv(candidates / "runtime_candidate_sensitivity.csv", rows, fieldnames=fieldnames)
            self.write_valid_candidate_caveat(candidates)
            result = run_validator(Path(tmp))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ROBUST-06 FAIL", result.stdout)
        self.assertIn("runtime_seconds", result.stdout)

    def test_valid_candidate_count_caveat_does_not_hide_missing_gls_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, candidates = create_complete_artifacts(Path(tmp), candidate_counts=[50, 100, 200])
            rows = candidate_metric_rows([50, 100, 200])
            for row in rows:
                row["method"] = "gsp"
            write_csv(candidates / "combined_metrics.csv", rows)
            self.write_valid_candidate_caveat(candidates)
            result = run_validator(Path(tmp))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ROBUST-06 FAIL", result.stdout)
        self.assertIn("method == gls_map", result.stdout)


if __name__ == "__main__":
    unittest.main()
