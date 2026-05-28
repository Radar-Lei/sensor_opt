import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

import pandas as pd

MODULE_PATH = Path(__file__).with_name("summarize_trace_sl_rcss.py")
spec = importlib.util.spec_from_file_location("summarize_trace_sl_rcss", MODULE_PATH)
summarizer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(summarizer)


class PairedComparisonStatsTest(unittest.TestCase):
    def test_paired_delta_stats_includes_interval_effect_size_and_tests(self):
        delta = pd.Series([-2.0, -1.0, -3.0, -4.0])

        stats = summarizer.paired_delta_stats(delta)

        self.assertEqual(stats["count"], 4)
        self.assertEqual(stats["win_count"], 4)
        self.assertEqual(stats["delta_mean"], -2.5)
        self.assertGreater(stats["delta_sem"], 0)
        self.assertLess(stats["ci95_low"], stats["delta_mean"])
        self.assertGreater(stats["ci95_high"], stats["delta_mean"])
        self.assertLess(stats["cohens_dz"], 0)
        self.assertTrue(pd.notna(stats["paired_t_p"]))
        self.assertTrue(pd.notna(stats["wilcoxon_p"]))

    def test_build_paired_comparisons_keeps_missing_layouts_and_insufficient_pairs_safe(self):
        pivot = pd.DataFrame(
            {
                "split_seed": [1, 2, 1],
                "budget": [0.1, 0.1, 0.2],
                "validation_swap_selected": [1.0, 1.2, 2.0],
                "multistart_swap_by_validation": [1.5, 1.1, 2.5],
                "observability_proxy": [1.7, 1.6, pd.NA],
            }
        ).set_index(["split_seed", "budget"])

        delta_summary, paired = summarizer.build_paired_comparisons(
            pivot,
            comparison_layouts=["validation_swap_selected"],
            baseline_layouts=["multistart_swap_by_validation", "observability_proxy", "qr_pod_modes"],
        )

        self.assertIn("validation_swap_selected_minus_multistart_swap_by_validation_mean", delta_summary.columns)
        self.assertTrue({"delta_sem", "ci95_low", "ci95_high", "cohens_dz"}.issubset(paired.columns))
        self.assertEqual(set(paired["baseline"]), {"multistart_swap_by_validation", "observability_proxy"})
        insufficient = paired[(paired["budget"] == 0.2) & (paired["baseline"] == "multistart_swap_by_validation")].iloc[0]
        self.assertEqual(insufficient["count"], 1)
        self.assertTrue(pd.isna(insufficient["delta_sem"]))
        self.assertTrue(pd.isna(insufficient["ci95_low"]))
        self.assertTrue(pd.isna(insufficient["cohens_dz"]))

    def test_dynamic_non_trace_baselines_include_validation_and_rcss_rows(self):
        pivot = pd.DataFrame(
            {
                "split_seed": [1, 2],
                "budget": [0.1, 0.1],
                "trace_biopt": [1.0, 1.1],
                "validation_swap_selected": [1.2, 1.3],
                "rcss_selected": [1.4, 1.5],
            }
        ).set_index(["split_seed", "budget"])
        baseline_layouts = sorted(str(name) for name in pivot.columns if str(name) != "trace_biopt")

        _, paired = summarizer.build_paired_comparisons(
            pivot,
            comparison_layouts=["trace_biopt"],
            baseline_layouts=baseline_layouts,
        )

        self.assertEqual(set(paired["baseline"]), {"validation_swap_selected", "rcss_selected"})



class CertificateSummaryTest(unittest.TestCase):
    def test_certificate_summary_includes_counts_and_empirical_markdown_wording(self):
        corr = pd.DataFrame(
            {
                "method": ["gls_map", "gls_map", "gsp"],
                "certificate": ["posterior_trace", "posterior_trace", "condition_number"],
                "pearson_mae": [0.8, 0.9, 0.2],
                "spearman_mae": [0.7, 0.6, 0.1],
                "n": [100, 100, 50],
            }
        )

        summary = summarizer.build_certificate_summary(corr)
        lines = summarizer.certificate_summary_lines(summary)
        text = "\n".join(lines).lower()

        self.assertIn(("pearson_mae", "count"), summary.columns)
        self.assertIn(("spearman_mae", "count"), summary.columns)
        self.assertIn("empirical certificate-error correlation", text)
        self.assertNotIn("guaranteed optimal", text)
        self.assertNotIn("certified optimal", text)


class ConditionGroupingTest(unittest.TestCase):
    def test_condition_group_columns_preserve_stable_optional_order(self):
        frame = pd.DataFrame(
            {
                "dataset": ["PeMS7_228"],
                "budget": [0.1],
                "split_mode": ["chronological"],
                "candidate_count": [50],
                "robustness_condition": ["failure_0.10"],
                "noise_scale": [0.0],
            }
        )

        self.assertEqual(
            summarizer.condition_group_columns(frame),
            ["dataset", "budget", "candidate_count", "robustness_condition", "noise_scale", "split_mode"],
        )

    def test_layout_summary_keeps_datasets_separate_when_combined(self):
        gls = pd.DataFrame(
            {
                "dataset": ["PeMS7_228", "Seattle"],
                "method": ["gls_map", "gls_map"],
                "layout_type": ["trace_biopt", "trace_biopt"],
                "budget": [0.1, 0.1],
                "mae": [2.0, 5.0],
            }
        )

        summary = summarizer.build_layout_summary(gls)

        self.assertEqual(set(summary["dataset"]), {"PeMS7_228", "Seattle"})
        self.assertEqual(summary.shape[0], 2)

    def test_condition_aware_layout_summary_keeps_robustness_conditions_separate(self):
        gls = pd.DataFrame(
            {
                "method": ["gls_map", "gls_map"],
                "layout_type": ["validation_swap_selected", "validation_swap_selected"],
                "budget": [0.2, 0.2],
                "robustness_condition": ["failure_0.05", "failure_0.20"],
                "mae": [3.0, 9.0],
            }
        )

        summary = summarizer.build_layout_summary(gls)

        self.assertEqual(set(summary["robustness_condition"]), {"failure_0.05", "failure_0.20"})
        self.assertEqual(summary["count"].tolist(), [1, 1])
        self.assertEqual(set(summary["mean"]), {3.0, 9.0})

    def test_condition_group_columns_accept_old_stage_schema(self):
        old_stage = pd.DataFrame(
            {
                "budget": [0.1],
                "layout_type": ["validation_swap_selected"],
                "mae": [2.5],
            }
        )

        self.assertEqual(summarizer.condition_group_columns(old_stage), ["budget"])
        summary = summarizer.build_layout_summary(old_stage)
        self.assertEqual(summary.iloc[0]["mean"], 2.5)

    def test_collect_input_frames_accepts_explicit_seed_dirs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            seed_root = root / "seed_25"
            seed_root.mkdir(parents=True)
            pd.DataFrame(
                {
                    "method": ["gls_map"],
                    "layout_type": ["validation_swap_selected"],
                    "budget": [0.2],
                    "mae": [3.0],
                }
            ).to_csv(seed_root / "metrics.csv", index=False)
            pd.DataFrame(
                {
                    "budget": [0.2],
                    "source": ["quality_coverage_sample"],
                    "selected": [True],
                    "validation_mae": [3.1],
                }
            ).to_csv(seed_root / "rcss_candidates.csv", index=False)

            metrics, _, rcss = summarizer.collect_input_frames([], [seed_root])

        self.assertEqual(len(metrics), 1)
        self.assertEqual(metrics[0].iloc[0]["split_seed"], 25)
        self.assertEqual(len(rcss), 1)
        self.assertEqual(rcss[0].iloc[0]["split_seed"], 25)

    def test_main_outputs_preserve_condition_columns_and_markdown_context(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            input_root = root / "candidates_50"
            seed_root = input_root / "seed_25"
            output_dir = root / "summary"
            seed_root.mkdir(parents=True)
            pd.DataFrame(
                {
                    "method": ["gls_map", "gls_map", "gls_map", "gls_map", "gls_map", "gls_map"],
                    "layout_type": [
                        "validation_swap_selected",
                        "random",
                        "rcss_selected",
                        "validation_swap_selected",
                        "random",
                        "rcss_selected",
                    ],
                    "budget": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
                    "candidate_count": [50, 50, 50, 50, 50, 50],
                    "robustness_family": ["sensor_failure", "sensor_failure", "sensor_failure", "sensor_failure", "sensor_failure", "sensor_failure"],
                    "robustness_condition": ["failure_0.05", "failure_0.05", "failure_0.05", "failure_0.20", "failure_0.20", "failure_0.20"],
                    "failure_rate": [0.05, 0.05, 0.05, 0.20, 0.20, 0.20],
                    "split_mode": ["random_days", "random_days", "random_days", "random_days", "random_days", "random_days"],
                    "mae": [3.0, 3.4, 3.2, 9.0, 9.6, 9.4],
                }
            ).to_csv(seed_root / "metrics.csv", index=False)
            pd.DataFrame(
                {
                    "budget": [0.2, 0.2],
                    "candidate_count": [50, 50],
                    "robustness_condition": ["failure_0.05", "failure_0.20"],
                    "failure_rate": [0.05, 0.20],
                    "split_mode": ["random_days", "random_days"],
                    "source": ["quality_coverage_sample", "quality_coverage_sample"],
                    "selected": [True, True],
                    "validation_mae": [3.1, 9.1],
                }
            ).to_csv(seed_root / "rcss_candidates.csv", index=False)
            pd.DataFrame(
                {
                    "candidate_count": [50, 50],
                    "robustness_condition": ["failure_0.05", "failure_0.20"],
                    "runtime_seconds": [1.0, 2.0],
                    "status": ["complete", "complete"],
                }
            ).to_csv(input_root / "stage13_timing.csv", index=False)

            old_argv = sys.argv
            try:
                sys.argv = [
                    "summarize_trace_sl_rcss.py",
                    "--input-root",
                    str(input_root),
                    "--output-dir",
                    str(output_dir),
                ]
                summarizer.main()
            finally:
                sys.argv = old_argv

            layout = pd.read_csv(output_dir / "gls_map_layout_summary.csv")
            self.assertEqual(set(layout["robustness_condition"]), {"failure_0.05", "failure_0.20"})
            self.assertIn("split_mode", layout.columns)
            paired = pd.read_csv(output_dir / "gls_map_paired_delta_tests.csv")
            self.assertEqual(set(paired["robustness_condition"]), {"failure_0.05", "failure_0.20"})
            selected = pd.read_csv(output_dir / "rcss_selected_sources.csv")
            self.assertEqual(set(selected["robustness_condition"]), {"failure_0.05", "failure_0.20"})
            candidate = pd.read_csv(output_dir / "candidate_sensitivity_summary.csv")
            self.assertEqual(set(candidate["robustness_condition"]), {"failure_0.05", "failure_0.20"})
            runtime = pd.read_csv(output_dir / "runtime_candidate_sensitivity.csv")
            self.assertEqual(set(runtime["robustness_condition"]), {"failure_0.05", "failure_0.20"})
            markdown = (output_dir / "SUMMARY.md").read_text(encoding="utf-8").lower()
            self.assertIn("grouped by condition", markdown)
            self.assertIn("stress-test evidence", markdown)
            self.assertNotIn("universal robustness proof", markdown)


class CandidateSensitivitySummaryTest(unittest.TestCase):
    def test_candidate_sensitivity_summary_counts_sources_and_diagnostics(self):
        candidates = pd.DataFrame(
            {
                "budget": [0.1, 0.1, 0.1, 0.2],
                "source": ["random_validation_pool", "random_validation_pool", "quality_coverage_sample", "quality_coverage_sample"],
                "selected": [True, False, True, False],
                "validation_mae": [3.0, 5.0, 4.0, 6.0],
                "posterior_trace": [10.0, 20.0, 30.0, 40.0],
                "rcss_score": [0.1, 0.2, 0.3, 0.4],
            }
        )

        summary = summarizer.build_candidate_sensitivity_summary(candidates)

        self.assertTrue({"budget", "source", "candidate_row_count", "selected_count"}.issubset(summary.columns))
        random_pool = summary[(summary["budget"] == 0.1) & (summary["source"] == "random_validation_pool")].iloc[0]
        self.assertEqual(random_pool["candidate_row_count"], 2)
        self.assertEqual(random_pool["selected_count"], 1)
        self.assertEqual(random_pool["validation_mae_mean"], 4.0)
        self.assertEqual(random_pool["selected_validation_mae_mean"], 3.0)
        self.assertIn("posterior_trace_std", summary.columns)
        self.assertIn("selected_rcss_score_mean", summary.columns)

    def test_candidate_sensitivity_summary_preserves_candidate_count_dimension(self):
        candidates = pd.DataFrame(
            {
                "budget": [0.2, 0.2],
                "candidate_count": [50, 100],
                "source": ["quality_coverage_sample", "quality_coverage_sample"],
                "selected": [True, True],
                "validation_mae": [3.0, 4.0],
            }
        )

        summary = summarizer.build_candidate_sensitivity_summary(candidates)

        self.assertEqual(set(summary["candidate_count"]), {50, 100})
        self.assertEqual(summary["candidate_row_count"].tolist(), [1, 1])

    def test_paired_comparisons_preserve_candidate_count_dimension(self):
        pivot = pd.DataFrame(
            {
                "split_seed": [25, 25],
                "budget": [0.2, 0.2],
                "candidate_count": [50, 100],
                "validation_swap_selected": [3.0, 2.8],
                "rcss_selected": [3.1, 2.9],
            }
        ).set_index(["split_seed", "budget", "candidate_count"])

        delta_summary, paired = summarizer.build_paired_comparisons(
            pivot,
            comparison_layouts=["validation_swap_selected"],
            baseline_layouts=["rcss_selected"],
        )

        self.assertEqual(set(delta_summary["candidate_count"]), {50, 100})
        self.assertEqual(set(paired["candidate_count"]), {50, 100})

    def test_runtime_summary_only_uses_measured_runtime_fields(self):
        candidates = pd.DataFrame(
            {
                "budget": [0.1, 0.2],
                "source": ["random_validation_pool", "quality_coverage_sample"],
                "candidate_count": [50, 100],
                "runtime_seconds": [1.5, 2.5],
            }
        )
        without_runtime = candidates.drop(columns=["runtime_seconds"])

        runtime_summary = summarizer.build_runtime_candidate_sensitivity_summary(candidates)
        missing_summary = summarizer.build_runtime_candidate_sensitivity_summary(without_runtime)

        self.assertEqual(set(runtime_summary["candidate_count"]), {50, 100})
        self.assertEqual(set(runtime_summary["runtime_seconds"]), {1.5, 2.5})
        self.assertTrue(missing_summary.empty)

    def test_runtime_collection_prefers_raw_timing_over_existing_summary(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            raw = pd.DataFrame({"candidate_count": [50], "runtime_seconds": [7], "seed": [25]})
            stale = pd.DataFrame({"candidate_count": [50], "runtime_seconds": [99], "count": [2]})
            raw.to_csv(root / "stage13_timing.csv", index=False)
            stale.to_csv(root / "runtime_candidate_sensitivity.csv", index=False)

            frames = summarizer.collect_runtime_candidate_frames([root], [])
            runtime_summary = summarizer.build_runtime_candidate_sensitivity_summary(pd.concat(frames, ignore_index=True))

        self.assertEqual(len(frames), 1)
        self.assertEqual(runtime_summary.iloc[0]["runtime_seconds"], 7)
        self.assertEqual(runtime_summary.iloc[0]["count"], 1)

    def test_candidate_sensitivity_markdown_frames_tractability_not_scalability(self):
        candidate_summary = pd.DataFrame(
            {
                "budget": [0.1],
                "source": ["random_validation_pool"],
                "candidate_row_count": [2],
                "selected_count": [1],
            }
        )
        runtime_summary = pd.DataFrame(
            {
                "candidate_count": [50],
                "runtime_seconds": [1.5],
                "status": ["complete"],
            }
        )

        text = "\n".join(summarizer.candidate_sensitivity_lines(candidate_summary, runtime_summary)).lower()

        self.assertIn("candidate-count sensitivity", text)
        self.assertIn("practical tractability", text)
        self.assertIn("selection stability", text)
        self.assertNotIn("scalability guarantee", text)
        self.assertNotIn("runtime unavailable as complete", text)


if __name__ == "__main__":
    unittest.main()
