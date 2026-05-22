#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
FILES = {
    "evaluator": ROOT / "TRC-23-02333" / "transparent_estimator_eval.py",
    "summarizer": ROOT / "TRC-23-02333" / "summarize_trace_sl_rcss.py",
    "launcher": ROOT / "scripts" / "run_stage12_pems7_228.sh",
    "inventory": ROOT / ".planning" / "phases" / "03-baseline-portfolio" / "03-BASELINE-INVENTORY.md",
}
DATASET_PART = ("TRC-23-02333", "dataset")


def read_text(label):
    path = FILES[label]
    if DATASET_PART[0] in path.parts and DATASET_PART[1] in path.parts:
        raise AssertionError(f"Refusing to read raw dataset path: {path}")
    return path.read_text(encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise AssertionError(f"Missing {needle!r} in {label}")


def require_any(texts, needle, labels):
    if not any(needle in text for text in texts):
        raise AssertionError(f"Missing {needle!r} in any of {', '.join(labels)}")


def require_order(text, first, second, label):
    first_pos = text.find(first)
    second_pos = text.rfind(second)
    if first_pos < 0 or second_pos < 0 or first_pos >= second_pos:
        raise AssertionError(f"Expected {first!r} before final {second!r} in {label}")


def main():
    texts = {label: read_text(label) for label in FILES}
    evaluator = texts["evaluator"]
    summarizer = texts["summarizer"]
    launcher = texts["launcher"]
    inventory = texts["inventory"]

    for flag in [
        "--include-baseline-portfolio",
        "--include-observability-proxy",
        "--include-graph-sampling-baseline",
        "--include-qr-pod-baseline",
    ]:
        require(evaluator, flag, "evaluator")

    for layout_type in [
        "observability_proxy",
        "greedy_a_trace",
        "greedy_d_logdet",
        "qr_pod_modes",
        "multistart_swap_by_validation",
    ]:
        require(evaluator, layout_type, "evaluator")

    if "graph_sampling_laplacian" not in evaluator:
        if "graph_sampling_laplacian" not in inventory or "already represented" not in inventory:
            raise AssertionError("BASE-03 must be implemented as graph_sampling_laplacian or documented as already represented")

    for helper in [
        "def observability_proxy_layout",
        "def graph_sampling_laplacian_layout",
        "def qr_pod_layout",
    ]:
        require(evaluator, helper, "evaluator")

    require(evaluator, "layouts.append", "evaluator")
    require_order(evaluator, "observability_proxy", "evaluate_layout(test", "evaluator")
    require_order(evaluator, "qr_pod_modes", "evaluate_layout(test", "evaluator")

    for layout_type in [
        "observability_proxy",
        "greedy_a_trace",
        "greedy_d_logdet",
        "graph_sampling_laplacian",
        "qr_pod_modes",
        "multistart_swap_by_validation",
    ]:
        require_any([summarizer, inventory], layout_type, ["summarizer", "inventory"])

    for flag in ["--include-baseline-portfolio", "--include-validation-swap", "--include-greedy"]:
        require(launcher, flag, "launcher")

    for requirement in ["BASE-01", "BASE-02", "BASE-03", "BASE-04", "BASE-05", "BASE-06"]:
        require(inventory, requirement, "inventory")

    if "TRC-23-02333/dataset/" in inventory and "does not open" not in inventory:
        raise AssertionError("Inventory may mention dataset guardrails only with no-raw-data wording")

    print("Phase 3 baseline wiring check passed without reading raw datasets.")


if __name__ == "__main__":
    main()
