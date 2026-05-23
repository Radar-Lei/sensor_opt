# Phase 7: Claim and Main Table Contract - Pattern Map

**Mapped:** 2026-05-23
**Files analyzed:** 8 planned new/modified files
**Analogs found:** 8 / 8

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `scripts/generate_trace_sl_claim_contracts.py` | utility / artifact generator | file-I/O, batch, transform | `scripts/generate_trace_sl_paper_sources.py` | exact |
| `scripts/test_generate_trace_sl_claim_contracts.py` | test / validation script | file-I/O, validation | `scripts/test_generate_trace_sl_paper_sources.py` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv` | research artifact / contract table | batch, transform | `.planning/REQUIREMENTS.md`; `TRC-23-02333/trace_sl_results/README.md` | role-match |
| `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json` | research artifact / machine-readable policy | file-I/O, batch | `TRC-23-02333/trace_sl_results/reproducibility_manifest.json`; `scripts/generate_trace_sl_repro_manifest.py` | role-match |
| `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.md` | Markdown summary | file-I/O, transform | `TRC-23-02333/trace_sl_results/paper_sources/README.md`; `TRC-23-02333/trace_sl_results/README.md` | role-match |
| `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv` | research artifact / table contract | batch, transform | `TRC-23-02333/trace_sl_results/paper_sources/core_performance_table.csv`; `paired_delta_table.csv` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.md` | Markdown table summary | file-I/O, transform | `TRC-23-02333/trace_sl_results/paper_sources/core_performance_table.md` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/README.md` | documentation / artifact index | file-I/O, request-response to readers | `TRC-23-02333/trace_sl_results/paper_sources/README.md` | modify-existing |

## Pattern Assignments

### `scripts/generate_trace_sl_claim_contracts.py` (utility, file-I/O/batch/transform)

**Analog:** `scripts/generate_trace_sl_paper_sources.py`

**Imports pattern** (`scripts/generate_trace_sl_paper_sources.py` lines 0-10):
```python
#!/usr/bin/env python3
"""Generate deterministic TRACE-SL paper-source tables from committed aggregates."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from typing import Iterable, Sequence

import pandas as pd
```

**Constant/source-root pattern** (lines 13-30):
```python
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
```

**Apply to Phase 7:** keep `TRACE_RESULTS_ROOT`; use Stage12 PeMS7_228 as the main in-domain evidence source; add explicit Phase 7 label sets for claim status, forbidden wording, baseline portfolio, and caveat tags. Extend the table contract labels beyond current `CORE_LAYOUT_LABELS` to include `random`, `best_random_by_validation`, and `top_variance` because Phase 7 requires reviewer-facing main-table rows.

**Source metadata + fail-fast CSV loading pattern** (lines 55-69):
```python
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
```

**Core table row builder pattern** (lines 90-105):
```python
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
```

**Paired-delta contract pattern** (lines 108-120):
```python
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
```

**Write CSV first, Markdown second pattern** (lines 210-225):
```python
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
```

**Tracked-source guard pattern** (lines 227-239):
```python
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
```

**Orchestration pattern** (lines 247-299):
```python
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
```

**Apply to Phase 7:** build one deterministic function returning at least `claim_contract`, `main_table_contract`, and optional `claim_policy` rows. Verify all source CSVs are under `TRC-23-02333/trace_sl_results/` and tracked. Do not read raw datasets.

**CLI pattern** (lines 323-358):
```python
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
```

---

### `scripts/test_generate_trace_sl_claim_contracts.py` (test, file-I/O/validation)

**Analog:** `scripts/test_generate_trace_sl_paper_sources.py`

**Imports + dynamic import pattern** (`scripts/test_generate_trace_sl_paper_sources.py` lines 0-23):
```python
#!/usr/bin/env python3
"""Regression tests for TRACE-SL paper-source generation."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = PROJECT_ROOT / "scripts" / "generate_trace_sl_paper_sources.py"


def import_generator():
    spec = importlib.util.spec_from_file_location("generate_trace_sl_paper_sources", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not import generator from {GENERATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
```

**Temp CSV fixture pattern** (lines 26-36):
```python
class PaperSourceGenerationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def write_csv(self, relative_path: str, rows: list[dict[str, object]]) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(rows).to_csv(path, index=False)
        return path
```

**Provenance-preservation assertion pattern** (lines 38-65):
```python
def test_core_rows_filter_labels_and_preserve_provenance(self) -> None:
    generator = import_generator()
    source_csv = self.write_csv(
        "TRC-23-02333/trace_sl_results/stage12/gls_map_layout_summary.csv",
        [
            {"budget": 0.1, "layout_type": "validation_swap_selected", "mean": 1.2, "count": 2},
            {"budget": 0.1, "layout_type": "rcss_selected", "mean": 1.4, "count": 2},
            {"budget": 0.1, "layout_type": "unused_layout", "mean": 9.9, "count": 2},
        ],
    )

    frame = generator.load_csv(source_csv)
    rows = generator.build_core_performance_rows(
        frame,
        source_stage="stage12",
        source_dir=source_csv.parent,
        source_csv=source_csv,
        layout_labels=("validation_swap_selected", "rcss_selected"),
    )

    self.assertEqual([row["layout_type"] for row in rows], ["validation_swap_selected", "rcss_selected"])
    self.assertEqual({row["budget"] for row in rows}, {0.1})
    for row in rows:
        self.assertEqual(row["source_stage"], "stage12")
        self.assertEqual(row["source_dir"], "TRC-23-02333/trace_sl_results/stage12")
        self.assertEqual(row["source_csv"], "gls_map_layout_summary.csv")
        self.assertIn("mean", row)
```

**Fail-closed missing-label pattern** (lines 97-113):
```python
def test_missing_required_core_layout_label_fails_closed(self) -> None:
    generator = import_generator()
    source_csv = self.write_csv(
        "TRC-23-02333/trace_sl_results/stage12/gls_map_layout_summary.csv",
        [
            {"budget": 0.1, "layout_type": "validation_swap_selected", "mean": 1.2},
        ],
    )

    with self.assertRaisesRegex(ValueError, "missing required layout_type"):
        generator.build_core_performance_rows(
            generator.load_csv(source_csv),
            source_stage="stage12",
            source_dir=source_csv.parent,
            source_csv=source_csv,
            layout_labels=("validation_swap_selected", "rcss_selected"),
        )
```

**Deterministic Markdown test pattern** (lines 115-130):
```python
def test_markdown_rendering_is_deterministic_and_csv_backed(self) -> None:
    generator = import_generator()
    rows = [
        {"budget": 0.1, "layout_type": "validation_swap_selected", "mean": 1.234567, "source_stage": "stage12"},
        {"budget": 0.2, "layout_type": "rcss_selected", "mean": 2.0, "source_stage": "stage12"},
    ]
    columns = ["budget", "layout_type", "mean", "source_stage"]

    first = generator.markdown_table(rows, columns)
    second = generator.markdown_table(rows, columns)

    self.assertEqual(first, second)
    self.assertIn("| budget | layout_type | mean | source_stage |", first)
    self.assertIn("| 0.1 | validation_swap_selected | 1.234567 | stage12 |", first)
    self.assertNotIn("unused_layout", first)
    self.assertNotIn("not available", first.lower())
```

**Apply to Phase 7:** add tests for (1) forbidden wording list exists, (2) low-budget caveat is attached to every claim/table artifact row that discusses main-table dominance, (3) PeMS7_1026/Seattle are routed outside core claims, (4) main table rows include Stage12 provenance and paired statistics, and (5) empty/missing required evidence fails closed.

---

### `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv` (research artifact, batch/transform)

**Analogs:** `.planning/REQUIREMENTS.md`; `TRC-23-02333/trace_sl_results/README.md`; `scripts/generate_trace_sl_paper_sources.py`

**Claim requirements pattern** (`.planning/REQUIREMENTS.md` lines 9-23):
```markdown
### Claim Foundation

- [ ] **CLAIM-01**: Author can state the paper-level contribution as transparent reconstruction-aware sparse sensor layout design, not as a heuristic improvement story.
- [ ] **CLAIM-02**: Author can distinguish Transportation Science-ready claims from TR Part B-level claims that need stronger mathematical theory.
- [ ] **CLAIM-03**: Author has an explicit forbidden-wording list covering optimal, certified, globally robust, guaranteed MAE improvement, and generalizes across networks.
- [ ] **CLAIM-04**: Author can preserve the PeMS7_228 low-budget multistart caveat in all claim-facing artifacts.

### Main Evidence

- [ ] **EVID-01**: Author can use Stage12 PeMS7_228 baseline portfolio as the frozen main in-domain result table.
- [ ] **EVID-02**: Author has paired delta and p-value summaries for TRACE-SL against validation-selected random, random mean, top variance, greedy A-trace, graph sampling, observability, and QR/POD-style baselines where available.
- [ ] **EVID-03**: Author has completed PeMS7_1026 Stage12 10-split evidence using the same budgets and reviewer-facing baseline portfolio.
- [ ] **EVID-04**: Author has completed Seattle Stage12 10-split external/transfer-style evidence before Seattle appears in any core claim.
- [ ] **EVID-05**: Author can classify each dataset as core, external, supporting, conditional, or appendix-only based on evidence strength.
```

**Forbidden/out-of-scope wording pattern** (`.planning/REQUIREMENTS.md` lines 64-73):
```markdown
## Out of Scope

| Feature | Reason |
|---------|--------|
| Manuscript prose drafting | v1.1 only prepares the foundation; prose belongs to the next writing milestone. |
| Optimal or certified optimal placement claims | Current theory supports certificate-guided design, not global optimality or formal certification. |
| Guaranteed MAE improvement claims | Held-out empirical gains are statistical evidence, not universal guarantees. |
| Globally robust claims | Current robustness is stress-test evidence unless multi-seed perturbation evidence is added. |
| Strong cross-network generalization claims | PeMS7_1026 and Seattle need Stage12 10-split evidence before stronger external claims. |
| Raw dataset commits | Raw traffic datasets are local/ignored inputs and must not be committed. |
```

**Evidence-routing pattern** (`TRC-23-02333/trace_sl_results/README.md` lines 49-55):
```markdown
## Reading the results

Use `validation_swap_selected` as the current main method label. Use `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/` and `pems7_228_stage11_auto_weight_10split/` for the main in-domain evidence, preserving the documented 10% multistart caveat. Use `TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/` as the core PeMS7_228 robustness/generalization stress-test path with `combined_metrics.csv`, `gls_map_layout_summary.csv`, `gls_map_paired_delta_tests.csv`, and `SUMMARY.md`; interpret it as evaluated perturbation evidence, not a universal deployment proof. Use `TRC-23-02333/trace_sl_results/pems7_228_stage14_candidate_sensitivity/` for 50/100/200/500 candidate-count performance/runtime evidence with `combined_metrics.csv`, `candidate_sensitivity_summary.csv`, `runtime_candidate_sensitivity.csv`, `stage14_timing.csv`, and `SUMMARY.md`; if present, `candidate_sensitivity_caveat.json` is the only allowed ROBUST-06 limited-tractability exception. Use `TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/` as predecessor candidate-count sensitivity and measured runtime/tractability evidence, not as a broad scalability guarantee. Use `pems7_1026_stage11_auto_weight/` only as lower-power external supporting/optional evidence unless regenerated with a ten-split Stage 12 extension. Use `seattle_stage11_auto_weight_light/` only as supporting/conditional evidence; it is synchronized with scripts and summaries, but it is not part of the core claim set.

Stage 14 artifacts are stress-test evidence for usefulness under the specified perturbations and candidate budgets. External robustness remains supporting/optional unless a synchronized stronger bundle is generated and reviewed.

See `.planning/phases/04-core-experiment-evidence/04-DATASET-CLAIM-STATUS.md` for the PeMS7_1026 and Seattle claim-status decision record.
```

**Recommended CSV columns:** `claim_id`, `claim_lane`, `claim_status`, `allowed_wording`, `forbidden_wording`, `evidence_source`, `evidence_artifact`, `required_metric_basis`, `required_caveat_tag`, `phase_scope`, `notes`.

**Must copy:** all rows must include provenance columns equivalent to `source_stage`, `source_dir`, `source_csv` when derived from result artifacts.

---

### `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json` (research artifact, JSON machine-readable policy)

**Analog:** `scripts/generate_trace_sl_repro_manifest.py`

**Manifest constants and curated-stage pattern** (`scripts/generate_trace_sl_repro_manifest.py` lines 15-33):
```python
RAW_DATASET_PREFIX = "TRC-23-02333/dataset/"
RESULT_ROOT = Path("TRC-23-02333/trace_sl_results")

CURATED_STAGE_ENTRIES = [
    {
        "stage": "12",
        "directory": "pems7_228_stage12_baseline_portfolio",
        "claim_status": "core in-domain baseline-portfolio evidence",
        "launcher": "scripts/run_stage12_pems7_228.sh",
        "required_artifacts": [
            "SUMMARY.md",
            "combined_metrics.csv",
            "gls_map_layout_summary.csv",
            "gls_map_delta_summary.csv",
            "gls_map_paired_delta_tests.csv",
            "gls_map_win_counts.csv",
            "rcss_selected_sources.csv",
        ],
    },
```

**Raw-data hygiene + artifact inventory pattern** (lines 184-219):
```python
def is_evidence_path(path: Path) -> bool:
    """Return whether a path is allowed to appear as an evidence artifact."""
    return not path.as_posix().startswith(RAW_DATASET_PREFIX)


def inventory_result_dir(project_root: Path | str, result_dir: Path | str) -> dict[str, object]:
    """Inventory non-sensitive CSV/JSON/Markdown artifacts for a curated result directory."""
    root = Path(project_root).resolve()
    directory = Path(result_dir)
    if not directory.is_absolute():
        directory = root / directory
    directory_exists = directory.exists()
    artifacts: list[dict[str, object]] = []
    if directory_exists:
        for path in sorted(directory.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in {".csv", ".json", ".md"}:
                continue
            relative = relpath(root, path)
            if not is_evidence_path(Path(relative)):
                continue
            artifacts.append(
                {
                    "path": relative,
                    "size_bytes": path.stat().st_size,
                    "exists": True,
                    "is_evidence_artifact": True,
                }
            )
```

**JSON writer pattern** (lines 391-393):
```python
def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
```

**Deterministic payload pattern** (lines 373-388):
```python
return {
    "manifest_schema": "trace-sl-reproducibility-provenance-v1",
    "generated_at_utc": "1970-01-01T00:00:00Z",
    "generated_at_utc_note": "fixed deterministic timestamp; regenerate command provenance is captured by git commit/status",
    "generated_by": "scripts/generate_trace_sl_repro_manifest.py",
    "project_root_name": project_root.name,
    "policy": {
        "raw_dataset_prefix": RAW_DATASET_PREFIX,
        "raw_dataset_disposition": "protected local input only; never listed as evidence artifact",
        "experiment_rerun_disposition": "not run by this generator",
        "dependency_disposition": "standard library only for generator; package metadata queried via importlib.metadata",
    },
    "environment": collect_environment(),
    "git": collect_git_provenance(project_root),
    "curated_result_stages": stages,
}
```

**Apply to Phase 7:** create a deterministic `claim_contract_schema` value; keep `generated_at_utc` deterministic if the project wants stable diffs; include `forbidden_wording`, `bounded_allowed_wording`, `claim_lanes`, `evidence_routing`, and `caveat_tags`. Do not inventory or embed raw dataset files.

---

### `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv` (research artifact, batch/transform)

**Analogs:** `core_performance_table.csv`, `paired_delta_table.csv`, Stage12 aggregate CSVs.

**Provenance-first core-performance row shape** (`paper_sources/core_performance_table.csv` lines 0-9):
```csv
source_stage,source_dir,source_csv,budget,layout_type,mean,std,count
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_layout_summary.csv,0.1,validation_swap_selected,3.590056043088187,0.3072595267030528,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_layout_summary.csv,0.1,rcss_selected,3.6049820225763862,0.2932859626734715,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_layout_summary.csv,0.1,multistart_swap_by_validation,3.594525269120191,0.3248353991653851,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_layout_summary.csv,0.1,greedy_a_trace,3.6859786731065136,0.3434359269391557,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_layout_summary.csv,0.1,greedy_d_logdet,4.555444548458214,0.6117382334215894,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_layout_summary.csv,0.1,observability_proxy,4.0013402743381805,0.3219379858477312,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_layout_summary.csv,0.1,graph_sampling_laplacian,4.132875023482333,0.5062326927518931,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_layout_summary.csv,0.1,qr_pod_modes,3.9769370021338704,0.3358968053634518,10
```

**Stage12 full portfolio source includes random/top variance/best-random rows** (`pems7_228_stage12_baseline_portfolio/gls_map_layout_summary.csv` lines 1-21):
```csv
0.1,validation_swap_selected,3.590056043088187,0.3072595267030528,10
0.1,multistart_swap_by_validation,3.594525269120191,0.3248353991653851,10
0.1,rcss_selected,3.6049820225763867,0.29328596267347157,10
0.1,swap_from_scenario_average,3.6060833523296187,0.30167030141924295,10
0.1,swap_from_best_random_trace,3.614188982667156,0.28140066807907577,10
0.1,swap_from_greedy_a_trace,3.618488979571088,0.3011667312692168,10
0.1,swap_from_scenario_cvar,3.642753707582314,0.274517080693317,10
0.1,greedy_a_trace,3.6859786731065136,0.34343592693915576,10
0.1,best_random_by_validation,3.713109957542167,0.32397787926475097,10
0.1,top_variance,3.730412411309768,0.3412403302997051,10
0.1,robust_coverage_cvar,3.7357101485159547,0.2786812990910196,10
0.1,best_random_by_trace,3.7551446726357027,0.2850110627913955,10
0.1,scenario_average_a_trace,3.7712088509547015,0.3371247192612363,10
0.1,scenario_cvar_a_trace,3.788435444627004,0.3634043910368006,10
0.1,random,3.8331133641113926,0.3262458388220748,500
0.1,coverage,3.917373872743505,0.34293875306004784,10
0.1,qr_pod_modes,3.9769370021338704,0.33589680536345184,10
0.1,observability_proxy,4.0013402743381805,0.3219379858477312,10
0.1,graph_sampling_laplacian,4.132875023482333,0.5062326927518931,10
0.1,degree,4.146553304242128,0.29950659458184203,10
0.1,greedy_d_logdet,4.555444548458214,0.6117382334215894,10
```

**Paired-stat row shape with multistart caveat evidence** (`paper_sources/paired_delta_table.csv` lines 0-11):
```csv
source_stage,source_dir,source_csv,budget,layout,baseline,delta_mean,delta_std,delta_sem,ci95_low,ci95_high,cohens_dz,paired_t_p,wilcoxon_p,win_count,count
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,best_random_by_validation,-0.1230539144539801,0.0580018394246732,0.0183417921061317,-0.1645459308454217,-0.0815618980625386,-2.1215519313622777,8.764091420559418e-05,0.001953125,10,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,graph_sampling_laplacian,-0.5428189803941462,0.2657894274777081,0.0840499968821699,-0.7329532828743138,-0.3526846779139786,-2.0422895882104743,0.0001170030887827,0.001953125,10,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,greedy_a_trace,-0.0959226300183267,0.0737198373555399,0.023312259478067,-0.1486586247776464,-0.0431866352590071,-1.3011779930509897,0.0026186262226825,0.001953125,10,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,greedy_d_logdet,-0.9653885053700264,0.3461656927783362,0.1094672036989643,-1.2130205243091283,-0.717756486430924,-2.788804683739134,1.0078913825655343e-05,0.001953125,10,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,multistart_swap_by_validation,-0.0044692260320039,0.057732178584021,0.0182565178609101,-0.0457683386788151,0.0368298866148072,-0.0774130847236189,0.8121002073006562,0.76953125,5,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,observability_proxy,-0.4112842312499939,0.0785031573792612,0.024824878083312,-0.4674420070217504,-0.3551264554782374,-5.2390788470203065,4.7450703710452247e-08,0.001953125,10,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,qr_pod_modes,-0.3868809590456831,0.0953783634581701,0.0301612868027191,-0.4551105300256652,-0.318651388065701,-4.056275920642698,4.355815657618506e-07,0.001953125,10,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,random,-0.2430573210232056,0.0502251127599089,0.0158825752060097,-0.2789862022891618,-0.2071284397572493,-4.839358393978968,9.479071085037625e-08,0.001953125,10,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,scenario_cvar_a_trace,-0.1983794015388168,0.1003771833783279,0.0317420524587911,-0.2701849128703876,-0.1265738902072461,-1.976339590951784,0.0001496818051828,0.001953125,10,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,swap_from_scenario_cvar,-0.0526976644941268,0.0718038922164286,0.022706384426915,-0.1040630746667223,-0.0013322543215313,-0.7339109742865675,0.045424021780702,0.130859375,7,10
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,top_variance,-0.1403563682215808,0.0819354986592046,0.0259102796984759,-0.1989694930315929,-0.0817432434115686,-1.7130104840804932,0.0004234854226279,0.001953125,10,10
```

**Recommended CSV columns:** `budget`, `method_label`, `layout_type`, `table_role`, `test_mae_mean`, `test_mae_std`, `test_rmse_mean`, `test_mape_mean`, `paired_baseline`, `delta_mean`, `ci95_low`, `ci95_high`, `paired_t_p`, `wilcoxon_p`, `win_count`, `split_count`, `caveat_tag`, `claim_lane`, `source_stage`, `source_dir`, `source_csv`.

**Must copy:** preserve `source_stage/source_dir/source_csv` first; attach a `caveat_tag` to 10% rows and all dominance-sensitive rows involving `multistart_swap_by_validation`.

---

### `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.md` (Markdown summary, file-I/O/transform)

**Analog:** `TRC-23-02333/trace_sl_results/paper_sources/core_performance_table.md`

**Markdown table pattern** (`core_performance_table.md` lines 0-9):
```markdown
| source_stage | source_dir | source_csv | budget | layout_type | mean | std | count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stage12_baseline_portfolio | TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio | gls_map_layout_summary.csv | 0.1 | validation_swap_selected | 3.590056043088187 | 0.3072595267030528 | 10 |
| stage12_baseline_portfolio | TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio | gls_map_layout_summary.csv | 0.1 | rcss_selected | 3.6049820225763862 | 0.2932859626734715 | 10 |
| stage12_baseline_portfolio | TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio | gls_map_layout_summary.csv | 0.1 | multistart_swap_by_validation | 3.594525269120191 | 0.3248353991653851 | 10 |
| stage12_baseline_portfolio | TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio | gls_map_layout_summary.csv | 0.1 | greedy_a_trace | 3.6859786731065136 | 0.3434359269391557 | 10 |
| stage12_baseline_portfolio | TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio | gls_map_layout_summary.csv | 0.1 | greedy_d_logdet | 4.555444548458214 | 0.6117382334215894 | 10 |
| stage12_baseline_portfolio | TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio | gls_map_layout_summary.csv | 0.1 | observability_proxy | 4.0013402743381805 | 0.3219379858477312 | 10 |
| stage12_baseline_portfolio | TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio | gls_map_layout_summary.csv | 0.1 | graph_sampling_laplacian | 4.132875023482333 | 0.5062326927518931 | 10 |
```

**Markdown renderer to copy** (`scripts/generate_trace_sl_paper_sources.py` lines 184-198):
```python
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
```

**Apply to Phase 7:** Markdown is a generated view of the CSV contract, not the source of truth. Include a short caveat note above or below the table only if generated from row fields; do not hand-write paper prose.

---

### `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.md` (Markdown summary, file-I/O/transform)

**Analogs:** `paper_sources/README.md`; `trace_sl_results/README.md`; `summarize_trace_sl_rcss.py`

**Human-readable generated-file index pattern** (`paper_sources/README.md` lines 0-18):
```markdown
# TRACE-SL paper source tables

This directory contains deterministic manuscript-facing CSV and Markdown sources generated from committed aggregate result artifacts under `TRC-23-02333/trace_sl_results/`. They are inputs for later manuscript table/figure rendering, not manually copied paper values.

Regenerate from the repository root with:

```bash
python scripts/generate_trace_sl_paper_sources.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources
```

## Generated files

- `core_performance_table.csv` / `core_performance_table.md`: Stage 12 GLS/MAP core method and comparator performance by budget.
- `paired_delta_table.csv`: Stage 12 paired deltas/tests for `validation_swap_selected` against available baselines.
- `robustness_condition_table.csv`: Stage 14 condition-preserving robustness performance rows.
- `candidate_runtime_table.csv`: Stage 14 candidate-count runtime and candidate diagnostic sensitivity rows.
- `certificate_correlation_table.csv`: Stage 12/13 empirical certificate-error correlation summaries.

Every generated row includes `source_stage`, `source_dir`, and `source_csv` provenance columns. The generator verifies that source CSVs are tracked by git and reads only committed aggregate CSVs, not raw traffic datasets.
```

**Summary wording pattern with bounded caveat** (`TRC-23-02333/summarize_trace_sl_rcss.py` lines 127-137):
```python
def certificate_summary_lines(corr_summary):
    return [
        "## Empirical certificate-error correlation summary",
        "",
        "These correlations are empirical support for certificate-guided selection, not formal optimality guarantees.",
        "",
        "```",
        corr_summary.to_string(),
        "```",
        "",
    ]
```

**Apply to Phase 7:** use short generated sections like `Transportation Science-ready`, `TR Part B-level extension`, `Forbidden wording`, `Evidence routing`, and `Caveat tags`. Keep it contract-like and avoid manuscript prose.

---

### `TRC-23-02333/trace_sl_results/paper_sources/README.md` (documentation/artifact index, file-I/O)

**Analog:** same file, modify-existing.

**Existing convention to preserve** (`paper_sources/README.md` lines 0-18):
```markdown
# TRACE-SL paper source tables

This directory contains deterministic manuscript-facing CSV and Markdown sources generated from committed aggregate result artifacts under `TRC-23-02333/trace_sl_results/`. They are inputs for later manuscript table/figure rendering, not manually copied paper values.

Regenerate from the repository root with:

```bash
python scripts/generate_trace_sl_paper_sources.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources
```

## Generated files

- `core_performance_table.csv` / `core_performance_table.md`: Stage 12 GLS/MAP core method and comparator performance by budget.
- `paired_delta_table.csv`: Stage 12 paired deltas/tests for `validation_swap_selected` against available baselines.
- `robustness_condition_table.csv`: Stage 14 condition-preserving robustness performance rows.
- `candidate_runtime_table.csv`: Stage 14 candidate-count runtime and candidate diagnostic sensitivity rows.
- `certificate_correlation_table.csv`: Stage 12/13 empirical certificate-error correlation summaries.

Every generated row includes `source_stage`, `source_dir`, and `source_csv` provenance columns. The generator verifies that source CSVs are tracked by git and reads only committed aggregate CSVs, not raw traffic datasets.
```

**Apply to Phase 7:** add new generated files to the existing bullet list; keep the regenerate command; if a new generator script is used, either update command or add an additional command. Preserve the final provenance/raw-data sentence.

## Shared Patterns

### CSV/JSON first, Markdown second
**Source:** `scripts/generate_trace_sl_paper_sources.py` lines 210-225; `scripts/generate_trace_sl_repro_manifest.py` lines 391-393 and 476-478.
**Apply to:** all Phase 7 artifacts.

Copy the pattern: machine-readable payload first; Markdown generated from same rows/payload; fail if rows are empty.

### Provenance columns on every paper-source row
**Source:** `scripts/generate_trace_sl_paper_sources.py` lines 55-87; `paper_sources/core_performance_table.csv` lines 0-9.
**Apply to:** `claim_contract.csv`, `main_table_contract.csv`, Markdown summaries.

Required fields: `source_stage`, `source_dir`, `source_csv` for evidence-derived rows; for policy rows, use `source_stage=phase7_claim_contract` and point `source_dir/source_csv` to the governing artifact when applicable.

### Fail-fast validation
**Source:** `scripts/generate_trace_sl_paper_sources.py` lines 63-69, 97-104, 114-118, 216-218; `scripts/test_generate_trace_sl_paper_sources.py` lines 97-113.
**Apply to:** generator and tests.

Missing required source CSVs, missing required columns, missing required layout/baseline labels, empty outputs, absent forbidden-wording rows, or absent caveat tags should raise `FileNotFoundError` or `ValueError`, not silently generate partial contracts.

### Evidence routing and claim guardrails
**Source:** `.planning/REQUIREMENTS.md` lines 9-23 and 64-73; `TRC-23-02333/trace_sl_results/README.md` lines 49-55.
**Apply to:** `claim_contract.csv`, `claim_contract.json`, `claim_contract.md`, README.

Mandatory routing:
- PeMS7_228 Stage12 baseline portfolio is main in-domain evidence.
- `validation_swap_selected` is the main method label.
- PeMS7_1026 and Seattle stay supporting/conditional until Phase 8 completes Stage12 10-split evidence.
- Robustness remains stress-test/appendix lane unless stronger evidence is added later.
- Forbidden wording: `optimal`, `certified`, `globally robust`, `guaranteed MAE improvement`, `generalizes across networks`.
- Allowed bounded wording: `certificate-guided`, `posterior-certificate-aware`, `stress-tested`, `improves in the tested setting`, `external evidence` when supported.

### Low-budget multistart caveat
**Source:** `paper_sources/paired_delta_table.csv` lines 5 and 16; `pems7_228_stage12_baseline_portfolio/gls_map_paired_delta_tests.csv` lines 10, 43, 76.
**Apply to:** all claim-facing files and main-table rows.

Copy the evidence logic: at 10% budget, `validation_swap_selected` vs `multistart_swap_by_validation` has `paired_t_p=0.8121002073006562`, `wilcoxon_p=0.76953125`, and `win_count=5/10`; therefore any dominance claim or main table at budget `0.1` must carry an explicit low-budget caveat tag.

### Raw dataset hygiene
**Source:** `scripts/generate_trace_sl_repro_manifest.py` lines 15-17 and 184-219; `paper_sources/README.md` line 18.
**Apply to:** generator, JSON payload, README.

Do not read, list as evidence, commit, or delete files under `TRC-23-02333/dataset/`. Phase 7 should use committed aggregate outputs under `TRC-23-02333/trace_sl_results/` only.

## No Analog Found

| File | Role | Data Flow | Reason |
|------|------|-----------|--------|
| Dedicated claim-contract artifact schema | research artifact | policy/contract transform | No existing dedicated `claim_contract.*` artifact exists; use `.planning/REQUIREMENTS.md`, `trace_sl_results/README.md`, and reproducibility manifest patterns. |

## Metadata

**Analog search scope:** `/home/samuel/projects/sensor_opt/scripts`, `/home/samuel/projects/sensor_opt/TRC-23-02333`, `/home/samuel/projects/sensor_opt/TRC-23-02333/trace_sl_results`, `/home/samuel/projects/sensor_opt/.planning`
**Files scanned:** 40+ script/planning/artifact files, with 10 strong analogs inspected
**Pattern extraction date:** 2026-05-23
