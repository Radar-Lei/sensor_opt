import importlib.util
from pathlib import Path

import pandas as pd


MODULE_PATH = Path(__file__).with_name("generate_trace_biopt_dominance.py")
spec = importlib.util.spec_from_file_location("generate_trace_biopt_dominance", MODULE_PATH)
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


def test_build_dominance_rows_selects_best_non_biopt_baseline():
    frame = pd.DataFrame(
        [
            {"dataset": "A", "budget": 0.1, "layout_type": "trace_biopt", "mean": 1.0},
            {"dataset": "A", "budget": 0.1, "layout_type": "greedy_a_trace", "mean": 1.2},
            {"dataset": "A", "budget": 0.1, "layout_type": "random", "mean": 2.0},
            {"dataset": "B", "budget": 0.1, "layout_type": "trace_biopt", "mean": 3.0},
            {"dataset": "B", "budget": 0.1, "layout_type": "validation_swap_selected", "mean": 2.9},
        ]
    )

    rows = generator.build_dominance_rows(frame)

    a = rows[rows["dataset"] == "A"].iloc[0]
    b = rows[rows["dataset"] == "B"].iloc[0]
    assert a["best_baseline_layout"] == "greedy_a_trace"
    assert a["trace_minus_best_baseline"] < 0
    assert bool(a["trace_beats_best_baseline"]) is True
    assert b["best_baseline_layout"] == "validation_swap_selected"
    assert b["trace_minus_best_baseline"] > 0
    assert bool(b["trace_beats_best_baseline"]) is False


def test_build_dominance_rows_fails_without_trace_biopt():
    frame = pd.DataFrame([{"budget": 0.1, "layout_type": "random", "mean": 2.0}])

    try:
        generator.build_dominance_rows(frame)
    except ValueError as exc:
        assert "missing trace_biopt" in str(exc)
    else:
        raise AssertionError("expected missing trace_biopt failure")


def test_attach_best_baseline_paired_stats_matches_selected_baseline():
    dominance = pd.DataFrame(
        [
            {
                "dataset": "A",
                "budget": 0.1,
                "best_baseline_layout": "validation_swap_selected",
                "trace_biopt_mean": 1.0,
                "best_baseline_mean": 1.2,
            }
        ]
    )
    paired = pd.DataFrame(
        [
            {
                "dataset": "A",
                "budget": 0.1,
                "layout": "trace_biopt",
                "baseline": "random",
                "delta_mean": -0.5,
                "win_count": 3,
                "count": 3,
            },
            {
                "dataset": "A",
                "budget": 0.1,
                "layout": "trace_biopt",
                "baseline": "validation_swap_selected",
                "delta_mean": -0.2,
                "paired_t_p": 0.04,
                "wilcoxon_p": 0.125,
                "win_count": 3,
                "count": 3,
            },
        ]
    )

    rows = generator.attach_best_baseline_paired_stats(dominance, paired)

    assert rows.iloc[0]["paired_delta_mean"] == -0.2
    assert rows.iloc[0]["paired_win_count"] == 3
    assert rows.iloc[0]["paired_count"] == 3
    assert rows.iloc[0]["paired_paired_t_p"] == 0.04
