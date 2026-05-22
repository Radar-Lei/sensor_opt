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


if __name__ == "__main__":
    unittest.main()
