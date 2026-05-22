from pathlib import Path


CHECKER = Path(__file__).with_name("check_phase4_evidence_coverage.py")


def test_checker_source_contract():
    text = CHECKER.read_text(encoding="utf-8")
    assert "def main()" in text
    assert "TRC-23-02333/trace_sl_results" in text
    assert "TRC-23-02333/dataset" in text
    assert text.count("TRC-23-02333/dataset") == 1
    assert "EXP-01" in text
    assert "EXP-06" in text
    assert "greedy_a_trace" in text
    assert "greedy_d_logdet" in text
    assert "observability_proxy" in text
    assert "graph_sampling_laplacian" in text
    assert "qr_pod_modes" in text
    assert "--include-greedy" in text


if __name__ == "__main__":
    test_checker_source_contract()
    print("checker-source-contract-ok")
