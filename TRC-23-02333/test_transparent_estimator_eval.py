import importlib.util
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd


MODULE_PATH = Path(__file__).resolve().parent / "transparent_estimator_eval.py"
spec = importlib.util.spec_from_file_location("transparent_estimator_eval", MODULE_PATH)
tev = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tev)


def assert_equal(actual, expected):
    assert actual == expected, f"expected {expected!r}, got {actual!r}"


def assert_close_array(actual, expected):
    np.testing.assert_allclose(actual, expected, rtol=1e-9, atol=1e-9)


def make_daily_frame(days=8, nodes=3):
    dates = pd.date_range("2026-01-01", periods=days, freq="D")
    index = pd.date_range(dates[0], periods=days * tev.SLOTS_PER_DAY, freq="5min")
    values = np.arange(len(index) * nodes, dtype=float).reshape(len(index), nodes)
    return pd.DataFrame(values, index=index), dates


def test_chronological_split_preserves_later_val_and_test_days():
    frame, dates = make_daily_frame(days=8, nodes=2)
    train, val, test, test_index, val_days, test_days = tev.split_daily_frame(frame, dates, seed=11, split_mode="chronological")

    assert_equal(train.shape, (4 * tev.SLOTS_PER_DAY, 2))
    assert_equal(val.shape, (2 * tev.SLOTS_PER_DAY, 2))
    assert_equal(test.shape, (2 * tev.SLOTS_PER_DAY, 2))
    assert_equal(val_days, ["2026-01-05", "2026-01-06"])
    assert_equal(test_days, ["2026-01-07", "2026-01-08"])
    assert test_index.min().date().isoformat() == "2026-01-07"


def test_random_split_default_shape_is_preserved():
    frame, dates = make_daily_frame(days=8, nodes=2)
    train, val, test, _, val_days, test_days = tev.split_daily_frame(frame, dates, seed=11)

    assert_equal(train.shape, (4 * tev.SLOTS_PER_DAY, 2))
    assert_equal(val.shape, (2 * tev.SLOTS_PER_DAY, 2))
    assert_equal(test.shape, (2 * tev.SLOTS_PER_DAY, 2))
    assert_equal(len(set(val_days + test_days)), 4)


def test_sensor_failure_drop_is_deterministic_and_sorted():
    sensors = np.array([7, 2, 4, 9, 1], dtype=int)
    first = tev.apply_sensor_failure(sensors, failure_rate=0.4, node_count=10, seed=505)
    second = tev.apply_sensor_failure(sensors, failure_rate=0.4, node_count=10, seed=505)

    assert_equal(first, second)
    active_sensors, selected_count, dropped_count, active_count = first
    assert_equal(selected_count, 5)
    assert_equal(dropped_count, 2)
    assert_equal(active_count, 3)
    assert_equal(active_sensors, sorted(active_sensors))
    assert set(active_sensors).issubset({1, 2, 4, 7, 9})


def test_noise_and_missing_helpers_are_deterministic_and_non_mutating():
    observed = np.arange(12, dtype=float).reshape(3, 4)
    original = observed.copy()
    sensors = np.array([1, 3], dtype=int)

    noisy_first = tev.apply_observation_noise(observed, sensors, noise_scale=0.5, seed=17)
    noisy_second = tev.apply_observation_noise(observed, sensors, noise_scale=0.5, seed=17)
    assert_close_array(noisy_first, noisy_second)
    assert_close_array(observed, original)
    assert_close_array(noisy_first[:, [0, 2]], original[:, [0, 2]])
    assert not np.allclose(noisy_first[:, sensors], original[:, sensors])

    random_mask_first = tev.observed_missing_mask(observed.shape, sensors, missing_rate=0.5, seed=23)
    random_mask_second = tev.observed_missing_mask(observed.shape, sensors, missing_rate=0.5, seed=23)
    np.testing.assert_array_equal(random_mask_first, random_mask_second)
    assert random_mask_first.dtype == bool
    assert not random_mask_first[:, sensors].all()
    assert random_mask_first[:, [0, 2]].all()

    block_mask_first = tev.observed_missing_block_mask(observed.shape, sensors, missing_block_steps=2, seed=31)
    block_mask_second = tev.observed_missing_block_mask(observed.shape, sensors, missing_block_steps=2, seed=31)
    np.testing.assert_array_equal(block_mask_first, block_mask_second)
    assert_equal(int((~block_mask_first[:, sensors]).sum()), 2 * len(sensors))
    assert block_mask_first[:, [0, 2]].all()


def test_cost_proxy_is_positive_and_deterministic():
    train = np.array(
        [
            [10.0, 20.0, 15.0],
            [11.0, 19.0, 16.0],
            [12.0, 18.0, 17.0],
        ],
        dtype=float,
    )
    distance = np.array(
        [
            [0.0, 1.0, 2.0],
            [1.0, 0.0, 1.0],
            [2.0, 1.0, 0.0],
        ],
        dtype=float,
    )

    first = tev.derive_cost_proxy(train, distance)
    second = tev.derive_cost_proxy(train, distance)
    assert_close_array(first, second)
    assert first.shape == (3,)
    assert np.all(first > 0.0)


def make_eval_args(**overrides):
    data = {
        "num_neighbors": 1,
        "gsp_lambda": 0.2,
        "prior_gamma": 0.05,
        "gls_prior_weight": 0.2,
        "obs_weight": 1.0,
        "selection_method": "gls_map",
        "robustness_family": "baseline",
        "robustness_condition": "baseline",
        "failure_rate": 0.0,
        "noise_scale": 0.0,
        "missing_rate": 0.0,
        "missing_block_steps": 0,
        "robustness_seed": 505,
    }
    data.update(overrides)
    return SimpleNamespace(**data)


def make_eval_inputs():
    test = np.array(
        [
            [10.0, 20.0, 30.0],
            [11.0, 21.0, 31.0],
            [12.0, 22.0, 32.0],
        ],
        dtype=float,
    )
    tod = test.copy()
    distance = np.array(
        [
            [0.0, 1.0, 2.0],
            [1.0, 0.0, 1.0],
            [2.0, 1.0, 0.0],
        ],
        dtype=float,
    )
    laplacian = tev.make_laplacian(distance)
    precision = np.eye(3)
    mean = np.array([10.0, 20.0, 30.0], dtype=float)
    std = np.ones(3, dtype=float)
    return test, tod, distance, laplacian, precision, mean, std


def test_solve_quadratic_accepts_per_node_observation_weights():
    observed_z = np.array([[100.0, 5.0]], dtype=float)
    prior_z = np.array([[1.0, 2.0]], dtype=float)
    matrix = np.eye(2)

    solution, lhs = tev.solve_quadratic(observed_z, prior_z, np.array([0, 1]), matrix, np.array([[0.0, 1.0]]))

    assert_close_array(lhs, np.array([[1.0, 0.0], [0.0, 2.0]]))
    assert abs(solution[0, 0] - prior_z[0, 0]) < 1e-9
    assert solution[0, 1] > prior_z[0, 1]


def test_evaluate_layout_unperturbed_output_shape_and_keys():
    inputs = make_eval_inputs()
    rows, hidden, context = tev.evaluate_layout(*inputs, np.array([0], dtype=int), make_eval_args(), apply_robustness=False)

    assert_equal([row["method"] for row in rows], ["historical_tod_mean", "neighbor_average", "gsp", "gls_map"])
    assert_equal(hidden.tolist(), [1, 2])
    assert_equal(context["selected_sensor_count"], 1)
    assert_equal(context["active_sensor_count"], 1)
    assert_equal(context["dropped_sensor_count"], 0)
    for row in rows:
        assert "mae" in row and "rmse" in row and "mape" in row


def test_evaluate_layout_missing_observations_use_zero_weight():
    inputs = make_eval_inputs()
    args = make_eval_args(missing_rate=1.0, robustness_family="missingness", robustness_condition="missing_random")
    rows, hidden, context = tev.evaluate_layout(*inputs, np.array([0], dtype=int), args, apply_robustness=True)

    assert_equal(context["active_sensor_count"], 1)
    assert_equal(context["observed_sensor_count"], 0)
    assert_equal(context["dropped_sensor_count"], 0)
    assert_equal(hidden.tolist(), [1, 2])
    assert any(row["method"] == "gls_map" for row in rows)


def test_validation_mae_is_not_perturbed_by_held_out_flags():
    inputs = make_eval_inputs()
    baseline_args = make_eval_args()
    robust_args = make_eval_args(failure_rate=1.0, noise_scale=10.0, missing_rate=1.0, robustness_family="sensor_failure")

    baseline = tev.validation_mae(*inputs, np.array([0], dtype=int), baseline_args)
    robust = tev.validation_mae(*inputs, np.array([0], dtype=int), robust_args)

    assert abs(baseline - robust) < 1e-9


def run_all():
    test_chronological_split_preserves_later_val_and_test_days()
    test_random_split_default_shape_is_preserved()
    test_sensor_failure_drop_is_deterministic_and_sorted()
    test_noise_and_missing_helpers_are_deterministic_and_non_mutating()
    test_cost_proxy_is_positive_and_deterministic()
    test_solve_quadratic_accepts_per_node_observation_weights()
    test_evaluate_layout_unperturbed_output_shape_and_keys()
    test_evaluate_layout_missing_observations_use_zero_weight()
    test_validation_mae_is_not_perturbed_by_held_out_flags()
    print("transparent-estimator-tests-ok")


if __name__ == "__main__":
    run_all()
