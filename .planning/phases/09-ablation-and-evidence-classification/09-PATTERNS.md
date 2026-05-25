# Phase 09: Ablation and Evidence Classification - Pattern Map

**Mapped:** 2026-05-25
**Files analyzed:** 14
**Analogs found:** 14 / 14

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `scripts/generate_trace_sl_ablation_evidence_contracts.py` | utility / generator | batch transform + file-I/O | `scripts/generate_trace_sl_external_evidence_contracts.py`; `scripts/generate_trace_sl_claim_contracts.py`; `TRC-23-02333/summarize_trace_sl_rcss.py` | exact |
| `scripts/test_generate_trace_sl_ablation_evidence_contracts.py` | test | batch validation + file-I/O | `scripts/test_generate_trace_sl_external_evidence_contracts.py`; `scripts/test_generate_trace_sl_paper_sources.py` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/ablation_contract.csv` | generated contract artifact | batch transform + file-I/O | `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv`; `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_contract.csv` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/ablation_contract.json` | generated contract artifact | batch transform + file-I/O | `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.json`; `scripts/generate_trace_sl_claim_contracts.py` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/ablation_contract.md` | generated view | batch transform + file-I/O | `scripts/generate_trace_sl_external_evidence_contracts.py` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/dataset_evidence_classification.csv` | generated contract artifact | batch transform + file-I/O | `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_contract.csv` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/dataset_evidence_classification.json` | generated gate / policy artifact | batch transform + file-I/O | `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.json` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/dataset_evidence_classification.md` | generated view | batch transform + file-I/O | `scripts/generate_trace_sl_external_evidence_contracts.py` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.json` | generated gate artifact | fail-closed batch validation | `scripts/generate_trace_sl_external_evidence_contracts.py`; existing `external_evidence_gate.json` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.md` | generated gate view | batch transform + file-I/O | `scripts/generate_trace_sl_external_evidence_contracts.py` | exact |
| `TRC-23-02333/trace_sl_results/paper_sources/README.md` | generated index | batch file-I/O | `scripts/generate_trace_sl_external_evidence_contracts.py`; existing paper source `README.md` | exact |
| `.planning/REQUIREMENTS.md` | planning config | request-response documentation update | `.planning/REQUIREMENTS.md` existing traceability format | exact |
| `.planning/ROADMAP.md` | planning config | request-response documentation update | `.planning/ROADMAP.md` Phase 9 section | exact |
| `.planning/STATE.md` | planning state | event-driven status update | `.planning/STATE.md` accumulated decisions/blockers format | exact |

## Pattern Assignments

### `scripts/generate_trace_sl_ablation_evidence_contracts.py` (utility/generator, batch transform + file-I/O)

**Primary analogs:**
- `scripts/generate_trace_sl_external_evidence_contracts.py`
- `scripts/generate_trace_sl_claim_contracts.py`
- `TRC-23-02333/summarize_trace_sl_rcss.py`

**Imports and constants pattern** — copy simple standalone CLI style from `scripts/generate_trace_sl_external_evidence_contracts.py` lines 0-31:
```python
#!/usr/bin/env python3
"""Generate TRACE-SL external Stage12 evidence contracts and gates."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Iterable, Sequence

import pandas as pd


TRACE_RESULTS_ROOT = Path("TRC-23-02333/trace_sl_results")
RAW_DATASET_PREFIX = "TRC-23-02333/dataset/"
REQUIRED_SPLIT_COUNT = 10
REQUIRED_BUDGETS = ("0.10", "0.20", "0.30")
```

**Contract column pattern** — use explicit ordered columns like `scripts/generate_trace_sl_external_evidence_contracts.py` lines 75-102:
```python
EXTERNAL_EVIDENCE_COLUMNS = (
    "dataset",
    "source_stage",
    "source_dir",
    "source_csv",
    "budget",
    "method_label",
    "layout_type",
    "table_role",
    "test_mae_mean",
    "test_mae_std",
    "test_rmse_mean",
    "test_mape_mean",
    "paired_baseline",
    "paired_evidence_status",
    "delta_mean",
    "ci95_low",
    "ci95_high",
    "paired_t_p",
    "wilcoxon_p",
    "win_count",
    "actual_split_count",
    "required_split_count",
    "evidence_status",
    "claim_lane",
    "core_claim_eligible",
    "blocker_reason",
)
```

**Path hygiene + fail-closed loading pattern** — copy from `scripts/generate_trace_sl_external_evidence_contracts.py` lines 129-170:
```python
def assert_no_raw_dataset_path(value: str | Path, label: str) -> None:
    rendered = Path(value).as_posix() if isinstance(value, Path) else str(value)
    if RAW_DATASET_PREFIX in rendered:
        raise ValueError(f"{label} references raw dataset path: {rendered}")


def require_trace_results_path(path: Path, project_root: Path, label: str) -> str:
    relative = project_relative(path, project_root)
    assert_no_raw_dataset_path(relative, label)
    if not relative.startswith(TRACE_RESULTS_ROOT.as_posix() + "/"):
        raise ValueError(f"{label} is outside curated trace_sl_results: {relative}")
    return relative
...
def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Expected aggregate CSV not found: {path}")
    frame = pd.read_csv(path)
    if frame.empty:
        raise ValueError(f"Expected nonempty aggregate CSV: {path}")
    return frame
```

**CSV/JSON/Markdown writer pattern** — copy from `scripts/generate_trace_sl_external_evidence_contracts.py` lines 196-215:
```python
def write_table_outputs(
    rows: Sequence[dict[str, object]],
    output_csv: Path,
    markdown_csv: Path | None = None,
    columns: Sequence[str] | None = None,
) -> None:
    if not rows:
        raise ValueError(f"Refusing to write empty contract table: {output_csv}")
    if columns is None:
        columns = list(rows[0].keys())
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows).loc[:, list(columns)]
    frame.to_csv(output_csv, index=False)
    if markdown_csv is not None:
        markdown_csv.write_text(markdown_table(frame.to_dict(orient="records"), columns), encoding="utf-8")


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
```

**Ablation source aggregation pattern** — copy result-summary conventions from `TRC-23-02333/summarize_trace_sl_rcss.py` lines 408-423 and 439-447:
```python
ablation_layouts = [
    "best_random_by_validation",
    "top_variance",
    "observability_proxy",
    "greedy_a_trace",
    "greedy_d_logdet",
    "graph_sampling_laplacian",
    "qr_pod_modes",
    "scenario_cvar_a_trace",
    "multistart_swap_by_validation",
    "rcss_selected",
    "validation_swap_selected",
]
ablation_summary = layout_summary[layout_summary["layout_type"].isin(ablation_layouts)].copy()
ablation_summary.to_csv(output_dir / "gls_map_ablation_summary.csv", index=False)
...
if rcss_candidates:
    rcss = pd.concat(rcss_candidates, ignore_index=True)
    rcss.to_csv(output_dir / "combined_rcss_candidates.csv", index=False)
    selected = rcss[selected_candidate_mask(rcss)]
    selected_source_cols = [*condition_group_columns(selected), "source"]
    selected.groupby(selected_source_cols).size().reset_index(name="selected_count").to_csv(output_dir / "rcss_selected_sources.csv", index=False)
    candidate_summary = build_candidate_sensitivity_summary(rcss)
    candidate_summary.to_csv(output_dir / "candidate_sensitivity_summary.csv", index=False)
```

**Dataset gate pattern** — copy fail-closed dataset contract logic from `scripts/generate_trace_sl_external_evidence_contracts.py` lines 398-475. Keep Stage11 and one-seed feasibility as blocked/conditional, not complete evidence:
```python
def build_dataset_contract(project_root: Path, spec: dict[str, object]) -> dict[str, object]:
    dataset = str(spec["dataset"])
    source_stage = str(spec["source_stage"])
    required_split_count = int(spec["required_split_count"])
    result_dir = Path(spec["result_dir"])
...
    if "stage11" in source_dir_relative.lower():
        blocker = "Stage11 directory cannot satisfy Stage12 10 split completion"
        row = build_blocked_row(dataset, source_stage, source_dir_relative, required_split_count, 0, "blocked", blocker)
        return {"rows": [row], "summary": dataset_summary(dataset, source_dir_relative, 0, required_split_count, "blocked", False, blocker, [])}
...
    if actual_count != required_split_count:
        evidence_status = "blocked"
        complete = False
        blocker = f"expected {required_split_count} split Stage12 evidence, found {actual_count} split evidence"
    elif untracked:
        evidence_status = "pending_tracking"
        complete = False
        blocker = "required aggregate CSVs/artifacts exist but are not git-tracked: " + ", ".join(untracked)
    else:
        evidence_status = "completed"
        complete = True
        blocker = ""
```

**CLI main pattern** — copy from `scripts/generate_trace_sl_external_evidence_contracts.py` lines 616-632:
```python
def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    project_root = args.project_root.resolve()
    output_dir = resolve_output_dir(project_root, args.output_dir)
    contracts = build_all_contracts(project_root, output_dir)
    write_table_outputs(
        contracts["external_evidence_contract"],
        output_dir / "external_evidence_contract.csv",
        output_dir / "external_evidence_contract.md",
        EXTERNAL_EVIDENCE_COLUMNS,
    )
    write_json(output_dir / "external_evidence_contract.json", {"external_evidence_contract": contracts["external_evidence_contract"]})
    write_json(output_dir / "external_evidence_gate.json", contracts["external_evidence_gate"])
    (output_dir / "external_evidence_gate.md").write_text(render_gate_markdown(contracts["external_evidence_gate"]), encoding="utf-8")
    write_readme(output_dir)
    print(f"wrote external_evidence_contract: {len(contracts['external_evidence_contract'])} rows")
    print(f"paper sources: {project_relative(output_dir, project_root)}")
```

---

### `scripts/test_generate_trace_sl_ablation_evidence_contracts.py` (test, batch validation + file-I/O)

**Analog:** `scripts/test_generate_trace_sl_external_evidence_contracts.py`

**Dynamic import + temporary git repo pattern** — copy lines 15-49:
```python
PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = PROJECT_ROOT / "scripts" / "generate_trace_sl_external_evidence_contracts.py"


def import_generator():
    spec = importlib.util.spec_from_file_location("generate_trace_sl_external_evidence_contracts", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not import generator from {GENERATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ExternalEvidenceContractGenerationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        subprocess.run(["git", "init", "--quiet"], cwd=self.root, check=True)

    def write_csv(self, relative_path: str, rows: list[dict[str, object]]) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(rows).to_csv(path, index=False)
        return path
...
    def track(self, *relative_paths: str) -> None:
        subprocess.run(["git", "add", *relative_paths], cwd=self.root, check=True)
```

**Fail-closed evidence tests** — adapt these from `scripts/test_generate_trace_sl_external_evidence_contracts.py` lines 169-202 and 253-266:
```python
def test_untracked_aggregate_sources_are_pending_tracking_not_complete(self) -> None:
    generator = import_generator()
    self.make_stage12_sources("pems7_1026_stage12_baseline_portfolio", tracked=False)
    self.make_stage12_sources("seattle_stage12_baseline_portfolio", tracked=False)

    contracts = generator.build_all_contracts(self.root)
    gate = contracts["external_evidence_gate"]

    self.assertFalse(gate["pems7_1026_stage12_complete"])
    self.assertFalse(gate["seattle_stage12_complete"])
    self.assertFalse(gate["v1_1_completion_allowed"])
...
def test_stage11_directory_is_rejected_as_stage12_completion(self) -> None:
    generator = import_generator()
    stage11_dir = self.make_stage12_sources("pems7_1026_stage11_auto_weight")
    spec = dict(generator.DATASET_SPECS[0], result_dir=stage11_dir.relative_to(self.root))

    dataset = generator.build_dataset_contract(self.root, spec)

    self.assertEqual(dataset["summary"]["evidence_status"], "blocked")
    self.assertFalse(dataset["summary"]["stage12_complete"])
    self.assertIn("Stage11", dataset["summary"]["blocker_reason"])
...
def test_seattle_core_eligibility_fails_closed_without_ten_splits(self) -> None:
    generator = import_generator()
    self.make_stage12_sources("pems7_1026_stage12_baseline_portfolio")
    self.make_stage12_sources("seattle_stage12_baseline_portfolio", split_count=9, status_payload={"status": "completed"})

    contracts = generator.build_all_contracts(self.root)
    gate = contracts["external_evidence_gate"]
    seattle = gate["datasets"]["Seattle"]

    self.assertFalse(gate["seattle_stage12_complete"])
    self.assertTrue(gate["seattle_core_claim_blocked"])
    self.assertFalse(seattle["core_claim_eligible"])
    self.assertEqual(seattle["actual_split_count"], 9)
    self.assertIn("10 split", seattle["blocker_reason"])
```

**Missing-row fail-closed test** — copy structure from `scripts/test_generate_trace_sl_paper_sources.py` lines 97-113:
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

---

### Generated ablation artifacts

**Files:**
- `TRC-23-02333/trace_sl_results/paper_sources/ablation_contract.csv`
- `TRC-23-02333/trace_sl_results/paper_sources/ablation_contract.json`
- `TRC-23-02333/trace_sl_results/paper_sources/ablation_contract.md`

**Analog:** `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv`

**CSV contract row pattern** — follow provenance-first, method/layout, evidence-status columns from `main_table_contract.csv` lines 0-5:
```csv
source_stage,source_dir,source_csv,budget,method_label,layout_type,table_role,test_mae_mean,test_mae_std,test_rmse_mean,test_mape_mean,paired_baseline,paired_evidence_status,delta_mean,ci95_low,ci95_high,paired_t_p,wilcoxon_p,win_count,split_count,caveat_tag,claim_lane
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_layout_summary.csv,0.1,validation_swap_selected,validation_swap_selected,main_method,3.590056043088187,0.3072595267030528,,,,descriptive_only,,,,,,,10,pems7_228_low_budget_multistart_not_dominant,core_in_domain
stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio,gls_map_layout_summary.csv;gls_map_paired_delta_tests.csv,0.1,validation_swap_selected,multistart_swap_by_validation,reviewer_baseline,3.594525269120191,0.3248353991653851,,,multistart_swap_by_validation,paired_stats_available,-0.0044692260320039,-0.0457683386788151,0.0368298866148072,0.8121002073006562,0.76953125,5,10,pems7_228_low_budget_multistart_not_dominant,core_in_domain
```

**Required ablation rows:** include at least `random`, `best_random_by_validation`, `greedy_a_trace` / `greedy_d_logdet` as certificate-only greedy rows, `rcss_selected`, `validation_swap_selected`, and `multistart_swap_by_validation`. Add machine-checkable fields such as `component_layer`, `supported_question`, `comparison_target`, `evidence_status`, `claim_route`, `caveat_tag`, and `provenance`.

**JSON policy pattern:** write JSON with schema marker, deterministic timestamp, `generated_by`, source artifacts, row counts, and status vocabulary like `scripts/generate_trace_sl_claim_contracts.py` lines 568-605.

**Markdown view pattern:** render from generated rows only, using `markdown_table()` from `scripts/generate_trace_sl_external_evidence_contracts.py` lines 185-193; do not manually draft manuscript prose.

---

### Generated dataset classification artifacts

**Files:**
- `TRC-23-02333/trace_sl_results/paper_sources/dataset_evidence_classification.csv`
- `TRC-23-02333/trace_sl_results/paper_sources/dataset_evidence_classification.json`
- `TRC-23-02333/trace_sl_results/paper_sources/dataset_evidence_classification.md`

**Analog:** `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_contract.csv` and `external_evidence_gate.json`

**Blocked/conditional CSV row pattern** — copy evidence-status fields from `external_evidence_contract.csv` lines 0-2:
```csv
dataset,source_stage,source_dir,source_csv,budget,method_label,layout_type,table_role,test_mae_mean,test_mae_std,test_rmse_mean,test_mape_mean,paired_baseline,paired_evidence_status,delta_mean,ci95_low,ci95_high,paired_t_p,wilcoxon_p,win_count,actual_split_count,required_split_count,evidence_status,claim_lane,core_claim_eligible,blocker_reason
PeMS7_1026,external_stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/pems7_1026_stage12_baseline_portfolio,,,validation_swap_selected,,dataset_gate,,,,,,descriptive_only,,,,,,,0,10,blocked,external_evidence,False,"missing required aggregate artifacts: ..."
Seattle,external_stage12_baseline_portfolio,TRC-23-02333/trace_sl_results/seattle_stage12_baseline_portfolio,,,validation_swap_selected,,dataset_gate,,,,,,descriptive_only,,,,,,,0,10,blocked,external_evidence,False,Seattle Stage12 real run was started ... EVID-04 remains incomplete ...
```

**Gate JSON pattern** — copy fail-closed booleans/policy from `external_evidence_gate.json` lines 61-77:
```json
{
  "gate_schema": "trace_sl_external_evidence_gate_v1",
  "generated_at_utc": "1970-01-01T00:00:00Z",
  "generated_at_utc_note": "fixed deterministic timestamp; regenerate command provenance is captured by git commit/status",
  "generated_by": "scripts/generate_trace_sl_external_evidence_contracts.py",
  "pems7_1026_stage12_complete": false,
  "policy": {
    "pending_tracking_disposition": "aggregate evidence exists but remains incomplete until required sources are git-tracked",
    "raw_dataset_disposition": "protected local input only; never listed as evidence artifact",
    "raw_dataset_prefix": "TRC-23-02333/dataset/",
    "seattle_core_policy": "Seattle core eligibility requires complete tracked ten-split Stage12 evidence and completed stage12_status.json when present",
    "stage11_disposition": "blocked for Stage12 completion"
  },
  "required_split_count": 10,
  "seattle_core_claim_blocked": true,
  "seattle_stage12_complete": false,
  "v1_1_completion_allowed": false
}
```

**Classification rows should preserve these decisions:**
- `PeMS7_228`: `core` where Stage12/10-split or committed core aggregate rows support it.
- `PeMS7_1026`: `external`, `supporting`, or `conditional`; Stage11 and one-seed Stage12 feasibility are not EVID-03 completion.
- `Seattle`: `conditional` / blocked from core while Stage12 ten-split gate is incomplete.
- Robustness/stress rows: `appendix-only` or `supporting`, not global robustness.

---

### `TRC-23-02333/trace_sl_results/paper_sources/external_evidence_gate.json` and `.md` (generated gate artifact/view)

**Analog:** `scripts/generate_trace_sl_external_evidence_contracts.py`

**Gate builder pattern** — copy from lines 501-524 and extend only if needed to reference dataset classification status; keep existing fail-closed booleans unchanged unless ten-split evidence is actually complete:
```python
def build_external_evidence_gate(dataset_summaries: Sequence[dict[str, object]]) -> dict[str, object]:
    by_dataset = {str(summary["dataset"]): summary for summary in dataset_summaries}
    pems_complete = bool(by_dataset.get("PeMS7_1026", {}).get("stage12_complete", False))
    seattle_complete = bool(by_dataset.get("Seattle", {}).get("stage12_complete", False))
    seattle_blocked = not seattle_complete
    return {
        "gate_schema": "trace_sl_external_evidence_gate_v1",
        "generated_at_utc": "1970-01-01T00:00:00Z",
        "generated_at_utc_note": "fixed deterministic timestamp; regenerate command provenance is captured by git commit/status",
        "generated_by": "scripts/generate_trace_sl_external_evidence_contracts.py",
        "required_split_count": REQUIRED_SPLIT_COUNT,
        "pems7_1026_stage12_complete": pems_complete,
        "seattle_stage12_complete": seattle_complete,
        "seattle_core_claim_blocked": seattle_blocked,
        "v1_1_completion_allowed": pems_complete and seattle_complete,
        "datasets": by_dataset,
        "policy": {
            "raw_dataset_prefix": RAW_DATASET_PREFIX,
            "raw_dataset_disposition": "protected local input only; never listed as evidence artifact",
            "stage11_disposition": "blocked for Stage12 completion",
            "pending_tracking_disposition": "aggregate evidence exists but remains incomplete until required sources are git-tracked",
            "seattle_core_policy": "Seattle core eligibility requires complete tracked ten-split Stage12 evidence and completed stage12_status.json when present",
        },
    }
```

**Markdown gate view pattern** — copy `render_gate_markdown()` from `scripts/generate_trace_sl_external_evidence_contracts.py` lines 541-581. Keep it a generated mirror: “This generated view mirrors `external_evidence_gate.json`; it is not manuscript prose.”

---

### `TRC-23-02333/trace_sl_results/paper_sources/README.md` (generated index)

**Analog:** existing `paper_sources/README.md` and `write_readme()` functions.

**Existing index style** — append a concise generated-files block like `README.md` lines 23-36:
```markdown
## External Stage12 Evidence Sources

Regenerate external evidence contracts from the repository root with:

```bash
python scripts/generate_trace_sl_external_evidence_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources
```

Generated files:

- `external_evidence_contract.csv` / `external_evidence_contract.json` / `external_evidence_contract.md`: Phase 8 external Stage12 evidence rows with split counts, tracking provenance, paired-stat honesty, and blocker status.
- `external_evidence_gate.json` / `external_evidence_gate.md`: machine-checkable PeMS7_1026 and Seattle Stage12 completion gate; Seattle remains blocked from core claims unless complete tracked ten-split Stage12 evidence is present.

Raw traffic datasets under `TRC-23-02333/dataset/` are protected local inputs and are not evidence artifacts.
```

**Implementation note:** update via generator `write_readme()`, not manual table editing. Use marker-splitting pattern from `scripts/generate_trace_sl_external_evidence_contracts.py` lines 584-601 to avoid duplicate blocks.

---

### `.planning/REQUIREMENTS.md`, `.planning/ROADMAP.md`, `.planning/STATE.md` (planning config/state updates)

**Analogs:** existing planning files.

**Requirements update pattern** — mark only ABLT-01 through ABLT-04 and EVID-05 complete if generated artifacts support them; preserve EVID-03/EVID-04 as pending. Use `.planning/REQUIREMENTS.md` lines 16-22 and 31-36 as the source format:
```markdown
### Main Evidence

- [x] **EVID-01**: Author can use Stage12 PeMS7_228 baseline portfolio as the frozen main in-domain result table.
- [x] **EVID-02**: Author has paired delta and p-value summaries for TRACE-SL against validation-selected random, random mean, top variance, greedy A-trace, graph sampling, observability, and QR/POD-style baselines where available.
- [ ] **EVID-03**: Author has completed PeMS7_1026 Stage12 10-split evidence using the same budgets and reviewer-facing baseline portfolio.
- [ ] **EVID-04**: Author has completed Seattle Stage12 10-split external/transfer-style evidence before Seattle appears in any core claim.
- [ ] **EVID-05**: Author can classify each dataset as core, external, supporting, conditional, or appendix-only based on evidence strength.
...
### Ablation Logic

- [ ] **ABLT-01**: Author can compare random mean, validation-selected random, certificate-only greedy, RCSS-selected, validation-swap-selected, and multistart validation-swap variants.
```

**Roadmap Phase 9 completion pattern** — update the Phase 9 section in `.planning/ROADMAP.md` lines 140-153 and the progress table lines 183-187 only after artifacts are generated/validated:
```markdown
### Phase 9: Ablation and Evidence Classification

**Goal**: Author has the ablation and dataset-classification evidence needed to explain why each TRACE-SL layer matters and where each dataset may be used.
**Depends on**: Phase 8.5
**Requirements**: ABLT-01, ABLT-02, ABLT-03, ABLT-04, EVID-05
**Success Criteria** (what must be TRUE):

  1. Author can compare random mean, validation-selected random, certificate-only greedy, RCSS-selected, validation-swap-selected, and multistart validation-swap variants in one ablation contract.
```

**State truth pattern** — preserve blockers from `.planning/STATE.md` lines 104-109 until ten-split evidence exists:
```markdown
### Blockers/Concerns

- Phase 8 gate blocks v1.1 completion: PeMS7_1026 Stage12 aggregate artifacts are missing, so EVID-03 remains incomplete.
- Phase 8 gate blocks Seattle core claims: Seattle Stage12 `stage12_status.json` reports blocked, so EVID-04 remains incomplete.
- Phase 8.5 no longer blocks Phase 9 planning: one full Stage12-compatible seed for PeMS7_1026 and Seattle completed, but Phase 8 ten-split external evidence remains incomplete.
- All phases: do not draft manuscript prose in this milestone.
```

## Shared Patterns

### CSV/JSON first; Markdown is generated view
**Source:** `scripts/generate_trace_sl_paper_sources.py` lines 210-224 and `scripts/generate_trace_sl_external_evidence_contracts.py` lines 196-215.
**Apply to:** all Phase 9 paper-source artifacts.

### Provenance-first rows
**Source:** `scripts/generate_trace_sl_paper_sources.py` lines 55-87.
**Apply to:** ablation and dataset classification CSV rows.
```python
def source_metadata(source_stage: str, source_dir: Path, source_csv: Path) -> dict[str, str]:
    return {
        "source_stage": source_stage,
        "source_dir": project_relative(source_dir),
        "source_csv": source_csv.name,
    }
...
for raw_row in frame.loc[:, list(columns)].to_dict(orient="records"):
    row = dict(metadata)
    row.update(raw_row)
    rows.append(row)
```

### Tracked-source enforcement
**Source:** `scripts/generate_trace_sl_paper_sources.py` lines 227-239 and `scripts/generate_trace_sl_external_evidence_contracts.py` lines 143-161.
**Apply to:** committed aggregate evidence sources. For generated blockers, use explicit `blocked`/`pending_tracking` rather than silently ignoring missing artifacts.

### Paired-stat honesty
**Source:** `scripts/generate_trace_sl_external_evidence_contracts.py` lines 369-395 and `scripts/generate_trace_sl_claim_contracts.py` lines 522-555.
**Apply to:** ablation rows comparing validation-swap against baselines. Rows with no paired statistics must be `descriptive_only`, with paired fields blank.

### Stage11 / one-seed feasibility is non-evidence for ten-split claims
**Source:** `scripts/generate_trace_sl_external_evidence_contracts.py` lines 398-412; `external_evidence_gate.json` lines 65-77.
**Apply to:** dataset classification and any PeMS7_1026/Seattle feasibility rows.

### Existing result-summary conventions
**Source:** `TRC-23-02333/summarize_trace_sl_rcss.py` lines 360-383 and 509-531.
**Apply to:** any aggregate summary consumption and generated output lists.
```python
parser = argparse.ArgumentParser(description="Summarize TRACE-SL multi-split RCSS results")
parser.add_argument("--input-root", required=True, nargs="+")
parser.add_argument("--seed-dir", nargs="*", default=[])
parser.add_argument("--runtime-root", nargs="*", default=[])
parser.add_argument("--output-dir", required=True)
...
combined = pd.concat(metrics, ignore_index=True)
combined.to_csv(output_dir / "combined_metrics.csv", index=False)
```

## No Analog Found

None. All expected Phase 9 files have close analogs in existing generator, contract, gate, result-summary, test, and planning-state patterns.

## Metadata

**Analog search scope:** `scripts/`, `TRC-23-02333/`, `TRC-23-02333/trace_sl_results/paper_sources/`, `.planning/`
**Files scanned:** 19 strong candidates after repository search
**Pattern extraction date:** 2026-05-25
