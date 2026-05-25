import importlib.util
import unittest
from argparse import Namespace
from pathlib import Path

import numpy as np
from scipy import linalg


MODULE_PATH = Path(__file__).resolve().parents[1] / "TRC-23-02333" / "transparent_estimator_eval.py"
SPEC = importlib.util.spec_from_file_location("transparent_estimator_eval", MODULE_PATH)
tee = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tee)


class Stage12RuntimeTraceCacheTests(unittest.TestCase):
    def setUp(self):
        self.base_matrix = np.array(
            [
                [3.0, 0.2, 0.1, 0.0, 0.0],
                [0.2, 3.4, 0.0, 0.1, 0.0],
                [0.1, 0.0, 3.2, 0.2, 0.1],
                [0.0, 0.1, 0.2, 3.6, 0.2],
                [0.0, 0.0, 0.1, 0.2, 3.3],
            ],
            dtype=float,
        )
        self.scenario_matrices = [
            self.base_matrix + np.eye(5) * 0.2,
            self.base_matrix + np.diag([0.1, 0.3, 0.2, 0.4, 0.5]),
            self.base_matrix + np.array(
                [
                    [0.6, 0.02, 0.0, 0.0, 0.0],
                    [0.02, 0.1, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.4, 0.01, 0.0],
                    [0.0, 0.0, 0.01, 0.2, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 0.3],
                ],
                dtype=float,
            ),
        ]
        self.layouts = [
            np.array([0, 2], dtype=int),
            np.array([1, 3, 4], dtype=int),
            np.array([0, 1, 4], dtype=int),
        ]
        self.obs_weight = 1.7

    def direct_posterior_inverse(self, base_matrix, sensors):
        selector = np.zeros(base_matrix.shape[0], dtype=float)
        selector[np.asarray(sensors, dtype=int)] = self.obs_weight
        return linalg.inv(base_matrix + np.diag(selector))

    def test_cached_posterior_trace_matches_direct_inverse_trace(self):
        cache = {}
        for sensors in self.layouts:
            with self.subTest(sensors=sensors.tolist()):
                cached = tee.posterior_trace_for_layout(self.base_matrix, sensors, self.obs_weight, trace_cache=cache)
                expected = float(np.trace(self.direct_posterior_inverse(self.base_matrix, sensors)))
                self.assertAlmostEqual(cached, expected, delta=1e-8)

    def test_cached_scenario_cvar_trace_matches_direct_tail_semantics(self):
        cache = {}
        tail_fraction = 0.5
        for sensors in self.layouts:
            with self.subTest(sensors=sensors.tolist()):
                cached = tee.scenario_cvar_trace_for_layout(
                    self.scenario_matrices,
                    sensors,
                    self.obs_weight,
                    tail_fraction,
                    trace_cache=cache,
                )
                traces = np.array(
                    [float(np.trace(self.direct_posterior_inverse(matrix, sensors))) for matrix in self.scenario_matrices],
                    dtype=float,
                )
                tail_count = max(1, int(np.ceil(len(traces) * tail_fraction)))
                expected = float(np.sort(traces)[-tail_count:].mean())
                self.assertAlmostEqual(cached, expected, delta=1e-8)

    def test_cached_condition_number_matches_direct_semantics(self):
        cache = {}
        for sensors in self.layouts:
            with self.subTest(sensors=sensors.tolist()):
                cached = tee.posterior_condition_for_layout(self.base_matrix, sensors, self.obs_weight, trace_cache=cache)
                selector = np.zeros(self.base_matrix.shape[0], dtype=float)
                selector[sensors] = self.obs_weight
                expected = float(np.linalg.cond(self.base_matrix + np.diag(selector)))
                np.testing.assert_allclose(cached, expected, rtol=1e-7, atol=1e-7)

    def test_repeated_calls_reuse_cache_without_changing_values(self):
        cache = {}
        sensors = self.layouts[0]
        first = tee.posterior_trace_for_layout(self.base_matrix, sensors, self.obs_weight, trace_cache=cache)
        second = tee.posterior_trace_for_layout(self.base_matrix, sensors, self.obs_weight, trace_cache=cache)
        scenario_first = tee.scenario_cvar_trace_for_layout(
            self.scenario_matrices,
            sensors,
            self.obs_weight,
            0.5,
            trace_cache=cache,
        )
        scenario_second = tee.scenario_cvar_trace_for_layout(
            self.scenario_matrices,
            sensors,
            self.obs_weight,
            0.5,
            trace_cache=cache,
        )

        self.assertEqual(first, second)
        self.assertEqual(scenario_first, scenario_second)
        self.assertIn("base", cache)
        self.assertGreaterEqual(len(cache["base"]), 1)

    def test_validation_mae_cache_does_not_reuse_stale_matrix_ids(self):
        n_nodes = 5
        test = np.array(
            [
                [10.0, 11.0, 12.0, 13.0, 14.0],
                [10.5, 11.5, 12.5, 13.5, 14.5],
                [11.0, 12.0, 13.0, 14.0, 15.0],
            ],
            dtype=float,
        )
        tod = np.tile(test.mean(axis=0), (tee.SLOTS_PER_DAY, 1))
        distance = np.abs(np.arange(n_nodes).reshape(-1, 1) - np.arange(n_nodes).reshape(1, -1)).astype(float)
        laplacian = tee.make_laplacian(distance)
        precision = self.base_matrix.copy()
        mean = test.mean(axis=0)
        std = test.std(axis=0) + 1e-6
        sensors = np.array([0, 2], dtype=int)
        cache = {}
        args = Namespace(
            selection_method="gls_map",
            obs_weight=self.obs_weight,
            gls_prior_weight=1.0,
            gsp_lambda=0.3,
            prior_gamma=0.7,
            num_neighbors=2,
            validation_mae_hidden_chunk_size=2,
        )

        for _ in range(100):
            args.selection_method = "gls_map"
            gls_cached = tee.validation_mae(test, tod, distance, laplacian, precision, mean, std, sensors, args, cache)
            gls_direct = tee.validation_mae(test, tod, distance, laplacian, precision, mean, std, sensors, args, {})
            args.selection_method = "gsp"
            gsp_cached = tee.validation_mae(test, tod, distance, laplacian, precision, mean, std, sensors, args, cache)
            gsp_direct = tee.validation_mae(test, tod, distance, laplacian, precision, mean, std, sensors, args, {})
            self.assertAlmostEqual(gls_cached, gls_direct, delta=1e-10)
            self.assertAlmostEqual(gsp_cached, gsp_direct, delta=1e-10)
        self.assertLessEqual(len(cache.get("base", {})), 2)
        self.assertLessEqual(len(cache.get("validation_matrix", {})), 2)

    def test_chunked_hidden_validation_mae_matches_full_gain_path(self):
        n_nodes = 8
        rng = np.random.default_rng(321)
        test = rng.normal(size=(7, n_nodes))
        tod = np.tile(test.mean(axis=0), (tee.SLOTS_PER_DAY, 1))
        distance = np.abs(np.arange(n_nodes).reshape(-1, 1) - np.arange(n_nodes).reshape(1, -1)).astype(float)
        laplacian = tee.make_laplacian(distance)
        precision = np.eye(n_nodes) * 1.4 + 0.05
        mean = test.mean(axis=0)
        std = test.std(axis=0) + 1e-6
        sensors = np.array([0, 3, 6], dtype=int)
        args = Namespace(
            selection_method="gls_map",
            obs_weight=1.2,
            gls_prior_weight=1.0,
            gsp_lambda=0.3,
            prior_gamma=0.7,
            num_neighbors=2,
            validation_mae_hidden_chunk_size=2,
        )
        hidden = np.array([idx for idx in range(n_nodes) if idx not in set(sensors)], dtype=int)
        observed_z = (test - mean) / std
        prior_z = (tod[: test.shape[0]] - mean) / std
        base_inverse = np.linalg.inv(precision)
        residual = observed_z[:, sensors] - prior_z[:, sensors]
        gain = tee.posterior_gain_from_base_inverse(base_inverse, sensors, args.obs_weight)
        expected = tee.mae(mean[hidden] + std[hidden] * (prior_z[:, hidden] + residual @ gain[hidden].T), test[:, hidden])
        actual = tee.hidden_mae_from_base_inverse(
            base_inverse,
            sensors,
            args.obs_weight,
            residual,
            prior_z,
            test,
            hidden,
            mean,
            std,
            args.validation_mae_hidden_chunk_size,
        )

        self.assertAlmostEqual(actual, expected, delta=1e-10)

    def test_make_rcss_row_cache_matches_direct_metrics(self):
        cache = {}
        val = np.array(
            [
                [10.0, 11.0, 12.0, 13.0, 14.0],
                [10.5, 11.5, 12.5, 13.5, 14.5],
                [11.0, 12.0, 13.0, 14.0, 15.0],
            ],
            dtype=float,
        )
        tod = np.tile(val.mean(axis=0), (tee.SLOTS_PER_DAY, 1))
        distance = np.abs(np.arange(5).reshape(-1, 1) - np.arange(5).reshape(1, -1)).astype(float)
        args = Namespace(
            selection_method="historical_tod_mean",
            obs_weight=self.obs_weight,
            cvar_tail_fraction=0.5,
        )

        row = tee.make_rcss_row(
            "synthetic",
            0,
            self.layouts[1],
            val,
            tod,
            distance,
            tee.make_laplacian(distance),
            self.base_matrix,
            val.mean(axis=0),
            val.std(axis=0) + 1e-6,
            self.base_matrix,
            self.scenario_matrices,
            args,
            trace_cache=cache,
        )

        expected_trace = float(np.trace(self.direct_posterior_inverse(self.base_matrix, self.layouts[1])))
        self.assertAlmostEqual(row["posterior_trace"], expected_trace, delta=1e-8)
        self.assertIn("base", cache)
        self.assertIn("trace", cache)
        self.assertIn("condition", cache)


if __name__ == "__main__":
    unittest.main()
