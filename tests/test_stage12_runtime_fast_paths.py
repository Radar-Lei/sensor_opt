import importlib.util
import unittest
from argparse import Namespace
from pathlib import Path
from unittest import mock

import numpy as np


MODULE_PATH = Path(__file__).resolve().parents[1] / "TRC-23-02333" / "transparent_estimator_eval.py"
SPEC = importlib.util.spec_from_file_location("transparent_estimator_eval", MODULE_PATH)
tee = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tee)


class Stage12RuntimeFastPathTests(unittest.TestCase):
    def setUp(self):
        self.test = np.array(
            [
                [10.0, 20.0, 30.0, 40.0],
                [11.0, 21.0, 31.0, 41.0],
                [12.0, 22.0, 32.0, 42.0],
                [13.0, 23.0, 33.0, 43.0],
            ],
            dtype=float,
        )
        self.tod = np.tile(self.test.mean(axis=0), (tee.SLOTS_PER_DAY, 1))
        self.distance = np.array(
            [
                [0.0, 1.0, 2.0, 3.0],
                [1.0, 0.0, 1.0, 2.0],
                [2.0, 1.0, 0.0, 1.0],
                [3.0, 2.0, 1.0, 0.0],
            ],
            dtype=float,
        )
        self.laplacian = tee.make_laplacian(self.distance)
        self.precision = np.array(
            [
                [2.5, 0.1, 0.0, 0.0],
                [0.1, 2.2, 0.1, 0.0],
                [0.0, 0.1, 2.4, 0.1],
                [0.0, 0.0, 0.1, 2.3],
            ],
            dtype=float,
        )
        self.mean = np.array([10.0, 20.0, 30.0, 40.0], dtype=float)
        self.std = np.array([2.0, 3.0, 4.0, 5.0], dtype=float)
        self.sensors = np.array([0, 2], dtype=int)

    def args_for(self, selection_method):
        return Namespace(
            selection_method=selection_method,
            gsp_lambda=0.2,
            prior_gamma=0.05,
            gls_prior_weight=0.2,
            obs_weight=1.0,
            num_neighbors=2,
        )

    def test_validation_mae_returns_finite_values_for_supported_methods(self):
        for method in ["historical_tod_mean", "neighbor_average", "gsp", "gls_map"]:
            with self.subTest(method=method):
                result = tee.validation_mae(
                    self.test,
                    self.tod,
                    self.distance,
                    self.laplacian,
                    self.precision,
                    self.mean,
                    self.std,
                    self.sensors,
                    self.args_for(method),
                )
                self.assertTrue(np.isfinite(result))
                self.assertGreaterEqual(result, 0.0)

    def test_validation_mae_does_not_call_evaluate_layout(self):
        with mock.patch.object(tee, "evaluate_layout", side_effect=AssertionError("evaluate_layout called")):
            result = tee.validation_mae(
                self.test,
                self.tod,
                self.distance,
                self.laplacian,
                self.precision,
                self.mean,
                self.std,
                self.sensors,
                self.args_for("gls_map"),
            )
        self.assertTrue(np.isfinite(result))

    def test_solve_quadratic_collapses_constant_observation_weights(self):
        observed_z = (self.test - self.mean) / self.std
        prior_z = np.zeros_like(observed_z)
        matrix = np.array(
            [
                [3.0, 0.2, 0.0, 0.0],
                [0.2, 3.5, 0.1, 0.0],
                [0.0, 0.1, 3.2, 0.1],
                [0.0, 0.0, 0.1, 3.4],
            ],
            dtype=float,
        )
        scalar_solution, scalar_lhs = tee.solve_quadratic(observed_z, prior_z, self.sensors, matrix, 1.7)
        vector_weights = np.zeros(observed_z.shape[1], dtype=float)
        vector_weights[self.sensors] = 1.7
        vector_solution, vector_lhs = tee.solve_quadratic(observed_z, prior_z, self.sensors, matrix, vector_weights)
        constant_weights = np.repeat(vector_weights.reshape(1, -1), observed_z.shape[0], axis=0)
        constant_solution, constant_lhs = tee.solve_quadratic(observed_z, prior_z, self.sensors, matrix, constant_weights)

        np.testing.assert_allclose(vector_solution, scalar_solution, rtol=1e-9, atol=1e-9)
        np.testing.assert_allclose(constant_solution, scalar_solution, rtol=1e-9, atol=1e-9)
        np.testing.assert_allclose(vector_lhs, scalar_lhs, rtol=1e-12, atol=1e-12)
        np.testing.assert_allclose(constant_lhs, scalar_lhs, rtol=1e-12, atol=1e-12)
        self.assertEqual(scalar_lhs.ndim, 2)
        self.assertEqual(vector_lhs.ndim, 2)
        self.assertEqual(constant_lhs.ndim, 2)

    def test_solve_quadratic_keeps_lhs_stack_for_true_time_varying_weights(self):
        observed_z = (self.test - self.mean) / self.std
        prior_z = np.zeros_like(observed_z)
        matrix = np.eye(observed_z.shape[1]) * 2.0
        varying_weights = np.ones_like(observed_z)
        varying_weights[1, self.sensors[0]] = 0.5
        varying_weights[2, self.sensors[1]] = 1.5

        solution, lhs_stack = tee.solve_quadratic(observed_z, prior_z, self.sensors, matrix, varying_weights)

        self.assertEqual(solution.shape, observed_z.shape)
        self.assertEqual(lhs_stack.shape, (observed_z.shape[0], observed_z.shape[1], observed_z.shape[1]))
        self.assertFalse(np.allclose(lhs_stack[0], lhs_stack[1]))


if __name__ == "__main__":
    unittest.main()
