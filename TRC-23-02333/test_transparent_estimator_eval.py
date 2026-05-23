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


def run_all():
    test_chronological_split_preserves_later_val_and_test_days()
    test_random_split_default_shape_is_preserved()
    test_sensor_failure_drop_is_deterministic_and_sorted()
    test_noise_and_missing_helpers_are_deterministic_and_non_mutating()
    test_cost_proxy_is_positive_and_deterministic()
    print("transparent-estimator-task1-tests-ok")


if __name__ == "__main__":
    run_all()
