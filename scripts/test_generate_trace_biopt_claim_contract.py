import importlib.util
from pathlib import Path

import pandas as pd
import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = PROJECT_ROOT / "scripts" / "generate_trace_biopt_claim_contract.py"
spec = importlib.util.spec_from_file_location("generate_trace_biopt_claim_contract", GENERATOR_PATH)
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


def dominance_frame(beats=True):
    return pd.DataFrame(
        [
            {
                "dataset": "UnitNet",
                "budget": 0.1,
                "trace_biopt_mean": 1.0,
                "best_baseline_mean": 1.2,
                "best_baseline_layout": "validation_swap_selected",
                "trace_minus_best_baseline": -0.2 if beats else 0.1,
                "trace_beats_best_baseline": beats,
                "baseline_count": 4,
                "paired_count": 3,
                "paired_win_count": 3,
                "paired_paired_t_p": 0.1,
                "paired_wilcoxon_p": 0.25,
                "evidence_source": "stage15_main",
            }
        ]
    )


def test_build_contract_rows_fail_closed_when_trace_does_not_beat_best_baseline(tmp_path):
    with pytest.raises(generator.ClaimContractError):
        generator.build_contract_rows(dominance_frame(beats=False), tmp_path / "dominance.csv")


def test_claim_contract_rows_include_caveats_and_provenance(tmp_path):
    dominance_path = tmp_path / "trace_biopt_best_baseline_delta.csv"
    paired_path = tmp_path / "gls_map_paired_delta_tests.csv"
    layout_path = tmp_path / "gls_map_layout_summary.csv"
    rows = generator.build_contract_rows(
        dominance_frame(beats=True),
        dominance_path,
        paired_source=paired_path,
        layout_summary_source=layout_path,
    )

    assert len(rows) == 1
    row = rows[0]
    assert row["claim_status"] == "supported_directional"
    assert row["evidence_strength"] == "directional_mean_dominance_all_observed_splits"
    assert "pre-registered non-BiOpt baselines" in row["allowed_wording"]
    assert "additional seeds" in row["required_caveat"]
    assert row["dominance_source"].endswith("trace_biopt_best_baseline_delta.csv")
    assert row["paired_source"].endswith("gls_map_paired_delta_tests.csv")
    assert row["layout_summary_source"].endswith("gls_map_layout_summary.csv")


def test_baseline_registry_excludes_trace_biopt():
    layout_summary = pd.DataFrame({"layout_type": ["trace_biopt", "random", "validation_swap_selected", "random"]})

    baselines = generator.build_baseline_registry(layout_summary)

    assert baselines == ["random", "validation_swap_selected"]


def test_write_outputs_creates_csv_json_and_markdown(tmp_path):
    rows = generator.build_contract_rows(dominance_frame(beats=True), tmp_path / "dominance.csv")
    aggregate = generator.aggregate_claim(rows, ["random", "validation_swap_selected"])

    generator.write_outputs(rows, aggregate, tmp_path)

    assert (tmp_path / "trace_biopt_claim_contract.csv").exists()
    assert (tmp_path / "trace_biopt_claim_contract.json").exists()
    markdown = (tmp_path / "trace_biopt_claim_contract.md").read_text(encoding="utf-8")
    assert "TRACE-BiOpt Claim Contract" in markdown
    assert "directional current evidence" in markdown


def test_stage16_replaceable_rows_emit_current_best_wording(tmp_path):
    frame = dominance_frame(beats=True)
    frame.loc[0, "evidence_source"] = "stage16_replaceable:unitnet_trainval"

    row = generator.build_contract_rows(frame, tmp_path / "dominance.csv")[0]

    assert "current-best evidence chain" in row["allowed_wording"]
    assert "replaceable Stage16 calibrated rerun" in row["allowed_wording"]
    assert "unitnet_trainval" in row["allowed_wording"]
