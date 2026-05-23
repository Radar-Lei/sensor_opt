#!/usr/bin/env python3
"""Generate deterministic TRACE-SL paper-source tables from committed aggregates."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from typing import Iterable, Sequence

import pandas as pd


TRACE_RESULTS_ROOT = Path("TRC-23-02333/trace_sl_results")
STAGE12_DIR = TRACE_RESULTS_ROOT / "pems7_228_stage12_baseline_portfolio"
STAGE13_DIR = TRACE_RESULTS_ROOT / "pems7_228_stage13_candidate_sensitivity"
STAGE14_ROBUSTNESS_DIR = TRACE_RESULTS_ROOT / "pems7_228_stage14_robustness"
STAGE14_CANDIDATE_DIR = TRACE_RESULTS_ROOT / "pems7_228_stage14_candidate_sensitivity"

CORE_LAYOUT_LABELS = (
    "validation_swap_selected",
    "rcss_selected",
    "multistart_swap_by_validation",
    "greedy_a_trace",
    "greedy_d_logdet",
    "observability_proxy",
    "graph_sampling_laplacian",
    "qr_pod_modes",
)

SOURCE_COLUMNS = ("source_stage", "source_dir", "source_csv")


def project_relative(path: Path, project_root: Path | None = None) -> str:
    resolved = path.resolve()
    if project_root is None:
        project_root = Path.cwd()
    try:
        return resolved.relative_to(project_root.resolve()).as_posix()
    except ValueError:
        parts = resolved.parts
        if "TRC-23-02333" in parts:
            start = parts.index("TRC-23-02333")
            return Path(*parts[start:]).as_posix()
        return path.as_posix()

def order_by_values(frame: pd.DataFrame, column: str, values: Sequence[str]) -> pd.DataFrame:
    order = {value: index for index, value in enumerate(values)}
    ordered = frame.copy()
    ordered["__paper_source_order"] = ordered[column].map(order)
    sort_columns = [column for column in ("budget", "robustness_condition", "__paper_source_order") if column in ordered.columns]
    ordered = ordered.sort_values(sort_columns, kind="mergesort").drop(columns=["__paper_source_order"])
    return ordered


def source_metadata(source_stage: str, source_dir: Path, source_csv: Path) -> dict[str, str]:
    return {
        "source_stage": source_stage,
        "source_dir": project_relative(source_dir),
        "source_csv": source_csv.name,
    }


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Expected aggregate CSV not found: {path}")
    frame = pd.read_csv(path)
    if frame.empty:
        raise ValueError(f"Expected nonempty aggregate CSV: {path}")
    return frame


def rows_from_frame(
    frame: pd.DataFrame,
    source_stage: str,
    source_dir: Path,
    source_csv: Path,
    columns: Sequence[str] | None = None,
) -> list[dict[str, object]]:
    if columns is None:
        columns = [column for column in frame.columns if column not in SOURCE_COLUMNS]
    metadata = source_metadata(source_stage, source_dir, source_csv)
    rows: list[dict[str, object]] = []
    for raw_row in frame.loc[:, list(columns)].to_dict(orient="records"):
        row = dict(metadata)
        row.update(raw_row)
        rows.append(row)
    return rows


def build_core_performance_rows(
    frame: pd.DataFrame,
    source_stage: str,
    source_dir: Path,
    source_csv: Path,
    layout_labels: Iterable[str] = CORE_LAYOUT_LABELS,
) -> list[dict[str, object]]:
    if "layout_type" not in frame.columns:
        raise ValueError("Core performance source must include layout_type")
    labels = tuple(layout_labels)
    selected = frame[frame["layout_type"].isin(labels)].copy()
    missing = sorted(set(labels) - set(selected["layout_type"].dropna().astype(str)))
    if missing:
        raise ValueError(f"Core performance source missing required layout_type rows: {missing}")
    selected = order_by_values(selected, "layout_type", labels)
    return rows_from_frame(selected, source_stage, source_dir, source_csv)


def build_paired_delta_rows(
    frame: pd.DataFrame,
    source_stage: str,
    source_dir: Path,
    source_csv: Path,
) -> list[dict[str, object]]:
    required = {"budget", "layout", "baseline"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Paired delta source missing columns: {sorted(missing)}")
    selected = frame[frame["layout"].eq("validation_swap_selected")].copy()
    selected = selected.sort_values(["budget", "layout", "baseline"], kind="mergesort")
    return rows_from_frame(selected, source_stage, source_dir, source_csv)


def build_robustness_condition_rows(
    frame: pd.DataFrame,
    source_stage: str,
    source_dir: Path,
    source_csv: Path,
    layout_labels: Iterable[str] = CORE_LAYOUT_LABELS,
) -> list[dict[str, object]]:
    required = {"budget", "robustness_condition", "layout_type"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Robustness source missing columns: {sorted(missing)}")
    labels = tuple(layout_labels)
    selected = frame[frame["layout_type"].isin(labels)].copy()
    missing = sorted(set(labels) - set(selected["layout_type"].dropna().astype(str)))
    if missing:
        raise ValueError(f"Robustness source missing required layout_type rows: {missing}")
    selected = order_by_values(selected, "layout_type", labels)
    return rows_from_frame(selected, source_stage, source_dir, source_csv)


def build_candidate_runtime_rows(
    runtime_frame: pd.DataFrame,
    candidate_frame: pd.DataFrame,
    runtime_source: Path,
    candidate_source: Path,
) -> list[dict[str, object]]:
    if "candidate_count" not in runtime_frame.columns:
        raise ValueError("Runtime source must include candidate_count")
    runtime = runtime_frame.sort_values(["candidate_count"], kind="mergesort")
    runtime_rows = rows_from_frame(
        runtime,
        "stage14_candidate_runtime",
        runtime_source.parent,
        runtime_source,
    )

    if "candidate_count" not in candidate_frame.columns:
        raise ValueError("Candidate sensitivity source must include candidate_count")
    candidate = candidate_frame.copy()
    sort_columns = [column for column in ("candidate_count", "budget", "source") if column in candidate.columns]
    candidate = candidate.sort_values(sort_columns, kind="mergesort")
    candidate_rows = rows_from_frame(
        candidate,
        "stage14_candidate_sensitivity",
        candidate_source.parent,
        candidate_source,
    )
    return runtime_rows + candidate_rows


def build_certificate_correlation_rows(sources: Sequence[tuple[str, Path]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for source_stage, source_csv in sources:
        frame = load_csv(source_csv)
        sort_columns = [column for column in ("method", "certificate") if column in frame.columns]
        if sort_columns:
            frame = frame.sort_values(sort_columns, kind="mergesort")
        rows.extend(rows_from_frame(frame, source_stage, source_csv.parent, source_csv))
    return rows


def format_markdown_value(value: object) -> str:
    if pd.isna(value):
        return ""
    return str(value)


def markdown_table(rows: Sequence[dict[str, object]], columns: Sequence[str]) -> str:
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in rows:
        values = [format_markdown_value(row.get(column, "")) for column in columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines) + "\n"


def ordered_columns(rows: Sequence[dict[str, object]]) -> list[str]:
    columns: list[str] = list(SOURCE_COLUMNS)
    for row in rows:
        for column in row:
            if column not in columns:
                columns.append(column)
    return columns


def write_table_outputs(
    rows: Sequence[dict[str, object]],
    output_csv: Path,
    markdown_csv: Path | None = None,
    columns: Sequence[str] | None = None,
) -> None:
    if not rows:
        raise ValueError(f"Refusing to write empty paper source table: {output_csv}")
    if columns is None:
        columns = ordered_columns(rows)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows).loc[:, list(columns)]
    frame.to_csv(output_csv, index=False)
    if markdown_csv is not None:
        markdown_csv.write_text(markdown_table(frame.to_dict(orient="records"), columns), encoding="utf-8")


def assert_source_is_tracked(project_root: Path, source: Path) -> None:
    relative = project_relative(source, project_root)
    if not relative.startswith(TRACE_RESULTS_ROOT.as_posix() + "/"):
        raise ValueError(f"Source is outside curated trace_sl_results: {relative}")
    result = subprocess.run(
        ["git", "-C", str(project_root), "ls-files", "--error-unmatch", relative],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode != 0:
        raise ValueError(f"Source CSV is not committed/tracked by git: {relative}")


def resolve_output_dir(project_root: Path, output_dir: Path) -> Path:
    if output_dir.is_absolute():
        return output_dir
    return project_root / output_dir


def build_all_tables(project_root: Path, output_dir: Path) -> dict[str, list[dict[str, object]]]:
    stage12_layout = project_root / STAGE12_DIR / "gls_map_layout_summary.csv"
    stage12_paired = project_root / STAGE12_DIR / "gls_map_paired_delta_tests.csv"
    stage12_cert = project_root / STAGE12_DIR / "certificate_correlation_summary.csv"
    stage13_cert = project_root / STAGE13_DIR / "certificate_correlation_summary.csv"
    stage14_robustness = project_root / STAGE14_ROBUSTNESS_DIR / "gls_map_layout_summary.csv"
    stage14_runtime = project_root / STAGE14_CANDIDATE_DIR / "runtime_candidate_sensitivity.csv"
    stage14_candidate = project_root / STAGE14_CANDIDATE_DIR / "candidate_sensitivity_summary.csv"

    sources = [
        stage12_layout,
        stage12_paired,
        stage12_cert,
        stage13_cert,
        stage14_robustness,
        stage14_runtime,
        stage14_candidate,
    ]
    for source in sources:
        assert_source_is_tracked(project_root, source)

    return {
        "core_performance": build_core_performance_rows(
            load_csv(stage12_layout),
            "stage12_baseline_portfolio",
            stage12_layout.parent,
            stage12_layout,
        ),
        "paired_delta": build_paired_delta_rows(
            load_csv(stage12_paired),
            "stage12_baseline_portfolio",
            stage12_paired.parent,
            stage12_paired,
        ),
        "robustness_condition": build_robustness_condition_rows(
            load_csv(stage14_robustness),
            "stage14_robustness",
            stage14_robustness.parent,
            stage14_robustness,
        ),
        "candidate_runtime": build_candidate_runtime_rows(
            load_csv(stage14_runtime),
            load_csv(stage14_candidate),
            stage14_runtime,
            stage14_candidate,
        ),
        "certificate_correlation": build_certificate_correlation_rows(
            (
                ("stage12_baseline_portfolio", stage12_cert),
                ("stage13_candidate_sensitivity", stage13_cert),
            )
        ),
    }


def write_readme(output_dir: Path) -> None:
    readme = output_dir / "README.md"
    readme.write_text(
        "# TRACE-SL paper source tables\n\n"
        "This directory contains deterministic manuscript-facing CSV and Markdown sources generated from committed aggregate result artifacts under `TRC-23-02333/trace_sl_results/`. "
        "They are inputs for later manuscript table/figure rendering, not manually copied paper values.\n\n"
        "Regenerate from the repository root with:\n\n"
        "```bash\n"
        "python scripts/generate_trace_sl_paper_sources.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources\n"
        "```\n\n"
        "## Generated files\n\n"
        "- `core_performance_table.csv` / `core_performance_table.md`: Stage 12 GLS/MAP core method and comparator performance by budget.\n"
        "- `paired_delta_table.csv`: Stage 12 paired deltas/tests for `validation_swap_selected` against available baselines.\n"
        "- `robustness_condition_table.csv`: Stage 14 condition-preserving robustness performance rows.\n"
        "- `candidate_runtime_table.csv`: Stage 14 candidate-count runtime and candidate diagnostic sensitivity rows.\n"
        "- `certificate_correlation_table.csv`: Stage 12/13 empirical certificate-error correlation summaries.\n\n"
        "Every generated row includes `source_stage`, `source_dir`, and `source_csv` provenance columns. The generator verifies that source CSVs are tracked by git and reads only committed aggregate CSVs, not raw traffic datasets.\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=TRACE_RESULTS_ROOT / "paper_sources",
        help="Output directory, relative to project root unless absolute.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    project_root = args.project_root.resolve()
    output_dir = resolve_output_dir(project_root, args.output_dir)
    tables = build_all_tables(project_root, output_dir)

    write_table_outputs(
        tables["core_performance"],
        output_dir / "core_performance_table.csv",
        output_dir / "core_performance_table.md",
    )
    write_table_outputs(tables["paired_delta"], output_dir / "paired_delta_table.csv")
    write_table_outputs(tables["robustness_condition"], output_dir / "robustness_condition_table.csv")
    write_table_outputs(tables["candidate_runtime"], output_dir / "candidate_runtime_table.csv")
    write_table_outputs(tables["certificate_correlation"], output_dir / "certificate_correlation_table.csv")
    write_readme(output_dir)

    for name, rows in tables.items():
        print(f"wrote {name}: {len(rows)} rows")
    print(f"paper sources: {project_relative(output_dir, project_root)}")


if __name__ == "__main__":
    main()
