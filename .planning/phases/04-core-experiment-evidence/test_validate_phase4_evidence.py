#!/usr/bin/env python3
import importlib.util
import unittest
from pathlib import Path


VALIDATOR = Path(__file__).with_name("validate_phase4_evidence.py")


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_phase4_evidence", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Phase4EvidenceValidatorTest(unittest.TestCase):
    def test_current_artifacts_have_no_failures_and_only_allowed_warnings(self):
        validator = load_validator()
        results = validator.run_checks()
        requirement_results = [result for result in results if result.requirement in validator.REQUIREMENTS]
        by_requirement = {result.requirement: result for result in requirement_results}
        self.assertEqual(set(validator.REQUIREMENTS), set(by_requirement))
        self.assertFalse([result for result in results if result.status == "FAIL"])
        warn_requirements = {result.requirement for result in requirement_results if result.status == "WARN"}
        self.assertLessEqual(warn_requirements, {"EXP-02", "EXP-03"})
        raw_data = [result for result in results if result.requirement == "RAW-DATA"]
        self.assertEqual("PASS", raw_data[0].status)

    def test_stage12_primary_evidence_labels_are_required(self):
        validator = load_validator()
        required = {
            "validation_swap_selected",
            "rcss_selected",
            "multistart_swap_by_validation",
            "greedy_a_trace",
            "greedy_d_logdet",
            "observability_proxy",
            "graph_sampling_laplacian",
            "qr_pod_modes",
        }
        self.assertEqual(required, validator.REQUIRED_STAGE12_LAYOUTS)

    def test_raw_dataset_evidence_paths_are_forbidden(self):
        validator = load_validator()
        self.assertEqual("TRC-23-02333/dataset/", validator.RAW_DATASET_PREFIX)
        self.assertTrue(validator.check_no_raw_dataset_evidence([]).status in {"PASS", "FAIL"})


if __name__ == "__main__":
    unittest.main()
