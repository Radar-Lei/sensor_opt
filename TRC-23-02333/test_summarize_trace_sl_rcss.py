import importlib.util
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
