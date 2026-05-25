import importlib.util
import unittest
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


if __name__ == "__main__":
    unittest.main()
