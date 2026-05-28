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
        "cvar_tail_fraction": 0.5,
        "trace_biopt_beta": 0.05,
        "trace_biopt_gamma": 0.05,
        "trace_biopt_eta": 0.01,
        "trace_biopt_huber_delta": 1.0,
        "trace_biopt_exchange_iter": 5,
        "trace_biopt_min_improve": 1e-9,
        "trace_biopt_objective_steps": 0,
        "trace_biopt_relax_iter": 3,
        "trace_biopt_relax_step": 0.1,
        "trace_biopt_relax_fd_eps": 1e-4,
        "trace_biopt_relax_pool": 0,
        "trace_biopt_initializer": "objective_forward",
        "trace_biopt_auto_warm_start_threshold": 500,
        "data_root": "dataset/Unit",
        "output_dir": "unit_out",
        "split_seed": 1,
        "layout_seed": 2,
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


def test_certificate_averages_time_varying_lhs_stack():
    lhs_stack = np.array(
        [
            [[1.0, 0.0], [0.0, 1.0]],
            [[2.0, 0.0], [0.0, 1.0]],
            [[1.0, 0.0], [0.0, 1.0]],
        ],
        dtype=float,
    )

    cert = tev.certificate(lhs_stack)
    last_cert = tev.certificate(lhs_stack[-1])

    assert cert["posterior_trace"] != last_cert["posterior_trace"]
    assert_close_array(np.array([cert["posterior_trace"]]), np.array([(2.0 + 1.5 + 2.0) / 3.0]))


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


def test_robustness_metadata_defaults_and_cost_layout_record():
    inputs = make_eval_inputs()
    args = make_eval_args(
        cost_proxy="graph_traffic",
        cost_budget=2.5,
        split_mode="chronological",
        failure_rate=0.1,
        noise_scale=0.2,
        missing_rate=0.3,
        missing_block_steps=1,
    )
    costs = tev.derive_cost_proxy(inputs[0], inputs[2])
    sensors = np.array([0, 1], dtype=int)
    layout_metadata = tev.layout_robustness_metadata(sensors, costs, args)
    row_metadata = tev.robustness_row_metadata(args, layout_metadata, {"selected_sensor_count": 2, "active_sensor_count": 1, "dropped_sensor_count": 1})

    required = {
        "robustness_family",
        "robustness_condition",
        "failure_rate",
        "noise_scale",
        "missing_rate",
        "missing_block_steps",
        "cost_proxy",
        "cost_budget",
        "layout_sensor_cost",
        "cost_feasible",
        "split_mode",
        "selected_sensor_count",
        "active_sensor_count",
        "dropped_sensor_count",
    }
    assert required.issubset(row_metadata)
    assert_equal(row_metadata["split_mode"], "chronological")
    assert_equal(row_metadata["cost_proxy"], "graph_traffic")
    assert row_metadata["layout_sensor_cost"] > 0.0
    assert isinstance(row_metadata["cost_feasible"], bool)


def test_smooth_l1_mean_matches_huber_semantics():
    pred = np.array([0.0, 2.0, 4.0])
    true = np.array([0.0, 0.0, 0.0])

    value = tev.smooth_l1_mean(pred, true, delta=1.0)

    assert abs(value - ((0.0 + 1.5 + 3.5) / 3.0)) < 1e-9


def test_trace_biopt_objective_exposes_single_method_terms():
    test, tod, distance, laplacian, precision, mean, std = make_eval_inputs()
    args = make_eval_args()
    gls_matrix = args.gls_prior_weight * precision
    scenario_matrices = [gls_matrix, 2.0 * gls_matrix]

    terms = tev.trace_biopt_objective(
        test,
        tod,
        distance,
        mean,
        std,
        gls_matrix,
        scenario_matrices,
        np.array([0], dtype=int),
        args,
        trace_cache={},
    )

    assert set(terms) == {
        "objective",
        "reconstruction_huber",
        "posterior_trace_per_node",
        "scenario_cvar_trace_per_node",
        "spatial_penalty",
        "sensor_count",
    }
    assert terms["sensor_count"] == 1
    assert terms["objective"] >= terms["reconstruction_huber"]


def test_trace_biopt_eval_frame_uses_deterministic_time_subset():
    test, tod, *_ = make_eval_inputs()
    args = make_eval_args(trace_biopt_objective_steps=2)

    subset = tev.trace_biopt_eval_frame(test, tod, args)
    repeat = tev.trace_biopt_eval_frame(test, tod, args)

    np.testing.assert_array_equal(subset, repeat)
    assert_equal(subset.shape, (2, test.shape[1]))
    np.testing.assert_array_equal(subset[0], test[0])
    np.testing.assert_array_equal(subset[-1], test[-1])


def test_project_capped_simplex_preserves_budget_and_bounds():
    projected = tev.project_capped_simplex(np.array([2.0, 0.5, -1.0, 0.25]), target_sum=2)

    assert abs(float(projected.sum()) - 2.0) < 1e-9
    assert np.all(projected >= -1e-12)
    assert np.all(projected <= 1.0 + 1e-12)


def test_trace_biopt_relaxed_objective_exposes_continuous_terms():
    test, tod, distance, laplacian, precision, mean, std = make_eval_inputs()
    args = make_eval_args(trace_biopt_beta=0.1, trace_biopt_gamma=0.1, trace_biopt_eta=0.1)
    gls_matrix = args.gls_prior_weight * precision
    scenario_matrices = [gls_matrix, 2.0 * gls_matrix]
    relaxed = np.array([0.7, 0.2, 0.1], dtype=float)

    terms = tev.trace_biopt_relaxed_objective(
        test,
        tod,
        distance,
        mean,
        std,
        gls_matrix,
        scenario_matrices,
        relaxed,
        args,
    )

    assert set(terms) == {
        "relaxed_objective",
        "relaxed_reconstruction_huber",
        "relaxed_posterior_trace_per_hidden_mass",
        "relaxed_scenario_cvar_trace_per_hidden_mass",
        "relaxed_spatial_penalty",
        "relaxed_sum",
    }
    assert abs(terms["relaxed_sum"] - 1.0) < 1e-9
    assert terms["relaxed_objective"] >= terms["relaxed_reconstruction_huber"]


def test_trace_biopt_layout_is_deterministic_and_not_pool_selected():
    test, tod, distance, laplacian, precision, mean, std = make_eval_inputs()
    args = make_eval_args(trace_biopt_beta=0.0, trace_biopt_gamma=0.0, trace_biopt_eta=0.0)
    gls_matrix = args.gls_prior_weight * precision
    scenario_matrices = [gls_matrix]

    first_sensors, first_terms, first_history = tev.trace_biopt_layout(
        test,
        tod,
        distance,
        mean,
        std,
        gls_matrix,
        scenario_matrices,
        sensor_count=1,
        args=args,
        trace_cache={},
    )
    second_sensors, second_terms, second_history = tev.trace_biopt_layout(
        test,
        tod,
        distance,
        mean,
        std,
        gls_matrix,
        scenario_matrices,
        sensor_count=1,
        args=args,
        trace_cache={},
    )

    np.testing.assert_array_equal(first_sensors, second_sensors)
    assert first_terms == second_terms
    assert first_history == second_history
    assert first_sensors.shape == (1,)
    assert {row["stage"] for row in first_history}.issubset({"forward", "exchange", "exchange_stop"})


def test_trace_biopt_relaxed_rounding_initializer_is_deterministic():
    test, tod, distance, laplacian, precision, mean, std = make_eval_inputs()
    args = make_eval_args(
        trace_biopt_initializer="relaxed_rounding",
        trace_biopt_relax_iter=2,
        trace_biopt_relax_step=0.05,
        trace_biopt_relax_pool=0,
        trace_biopt_exchange_iter=1,
    )
    gls_matrix = args.gls_prior_weight * precision
    scenario_matrices = [gls_matrix]

    first_sensors, first_terms, first_history = tev.trace_biopt_layout(
        test,
        tod,
        distance,
        mean,
        std,
        gls_matrix,
        scenario_matrices,
        sensor_count=2,
        args=args,
        trace_cache={},
    )
    second_sensors, second_terms, second_history = tev.trace_biopt_layout(
        test,
        tod,
        distance,
        mean,
        std,
        gls_matrix,
        scenario_matrices,
        sensor_count=2,
        args=args,
        trace_cache={},
    )

    np.testing.assert_array_equal(first_sensors, second_sensors)
    assert first_terms == second_terms
    assert first_history == second_history
    assert first_sensors.shape == (2,)
    assert first_history[0]["stage"] == "relax"
    assert any(row["stage"] == "relaxed_rounding" for row in first_history)
    assert any(row["stage"] == "relaxed_warm_start" for row in first_history)


def test_trace_biopt_posterior_greedy_warm_start_is_deterministic():
    test, tod, distance, laplacian, precision, mean, std = make_eval_inputs()
    args = make_eval_args(trace_biopt_initializer="posterior_greedy")
    gls_matrix = args.gls_prior_weight * precision
    scenario_matrices = [gls_matrix]

    sensors, terms, history = tev.trace_biopt_layout(
        test,
        tod,
        distance,
        mean,
        std,
        gls_matrix,
        scenario_matrices,
        sensor_count=2,
        args=args,
        trace_cache={},
    )

    expected = tev.greedy_posterior_layout(gls_matrix, 2, args.obs_weight, "a_trace")
    assert history[0]["stage"] == "posterior_greedy_warm_start"
    assert history[0]["sensors"] == sorted(int(x) for x in expected)
    assert sensors.shape == (2,)
    assert terms["sensor_count"] == 2


def test_trace_biopt_auto_initializer_uses_network_size_threshold():
    test, tod, distance, laplacian, precision, mean, std = make_eval_inputs()
    gls_matrix = args_matrix = 0.2 * precision
    scenario_matrices = [args_matrix]

    small_args = make_eval_args(trace_biopt_initializer="auto", trace_biopt_auto_warm_start_threshold=3)
    _, _, small_history = tev.trace_biopt_layout(
        test,
        tod,
        distance,
        mean,
        std,
        gls_matrix,
        scenario_matrices,
        sensor_count=1,
        args=small_args,
        trace_cache={},
    )

    large_args = make_eval_args(trace_biopt_initializer="auto", trace_biopt_auto_warm_start_threshold=2)
    _, _, large_history = tev.trace_biopt_layout(
        test,
        tod,
        distance,
        mean,
        std,
        gls_matrix,
        scenario_matrices,
        sensor_count=1,
        args=large_args,
        trace_cache={},
    )

    assert small_history[0]["stage"] == "forward"
    assert large_history[0]["stage"] == "posterior_greedy_warm_start"


def test_candidate_robustness_metadata_records_failure_counts():
    inputs = make_eval_inputs()
    args = make_eval_args(
        robustness_family="sensor_failure",
        robustness_condition="failure_0.50",
        failure_rate=0.5,
        robustness_seed=505,
    )
    costs = tev.derive_cost_proxy(inputs[0], inputs[2])
    sensors = np.array([0, 1], dtype=int)

    metadata = tev.candidate_robustness_metadata(sensors, costs, args, node_count=3)

    required = {
        "robustness_family",
        "robustness_condition",
        "failure_rate",
        "noise_scale",
        "missing_rate",
        "missing_block_steps",
        "cost_proxy",
        "cost_budget",
        "layout_sensor_cost",
        "cost_feasible",
        "split_mode",
        "selected_sensor_count",
        "active_sensor_count",
        "dropped_sensor_count",
    }
    assert required.issubset(metadata)
    assert_equal(metadata["selected_sensor_count"], 2)
    assert_equal(metadata["active_sensor_count"], 1)
    assert_equal(metadata["dropped_sensor_count"], 1)


def test_candidate_robustness_metadata_non_failure_keeps_all_active():
    inputs = make_eval_inputs()
    args = make_eval_args(robustness_family="observation_noise", robustness_condition="noise_0.05", noise_scale=0.05)
    costs = tev.derive_cost_proxy(inputs[0], inputs[2])
    sensors = np.array([0, 1], dtype=int)

    metadata = tev.candidate_robustness_metadata(sensors, costs, args, node_count=3)

    assert_equal(metadata["selected_sensor_count"], 2)
    assert_equal(metadata["active_sensor_count"], 2)
    assert_equal(metadata["dropped_sensor_count"], 0)


def run_all():
    test_chronological_split_preserves_later_val_and_test_days()
    test_random_split_default_shape_is_preserved()
    test_sensor_failure_drop_is_deterministic_and_sorted()
    test_noise_and_missing_helpers_are_deterministic_and_non_mutating()
    test_cost_proxy_is_positive_and_deterministic()
    test_solve_quadratic_accepts_per_node_observation_weights()
    test_certificate_averages_time_varying_lhs_stack()
    test_evaluate_layout_unperturbed_output_shape_and_keys()
    test_evaluate_layout_missing_observations_use_zero_weight()
    test_validation_mae_is_not_perturbed_by_held_out_flags()
    test_robustness_metadata_defaults_and_cost_layout_record()
    test_candidate_robustness_metadata_records_failure_counts()
    test_candidate_robustness_metadata_non_failure_keeps_all_active()
    print("transparent-estimator-tests-ok")


if __name__ == "__main__":
    run_all()
