---
phase: 07-claim-and-main-table-contract
reviewed: 2026-05-23T12:17:01Z
depth: standard
files_reviewed: 6
files_reviewed_list:
  - scripts/generate_trace_sl_claim_contracts.py
  - scripts/test_generate_trace_sl_claim_contracts.py
  - TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv
  - TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json
  - TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv
  - TRC-23-02333/trace_sl_results/paper_sources/README.md
findings:
  critical: 2
  warning: 1
  info: 0
  total: 3
status: issues_found
---

# Phase 07: Code Review Report

**Reviewed:** 2026-05-23T12:17:01Z
**Depth:** standard
**Files Reviewed:** 6
**Status:** issues_found

## Summary

Reviewed the Phase 7 claim-contract generator, its regression tests, and the generated CSV/JSON/README paper-source artifacts for evidence routing, raw-dataset leakage, schema consistency, and reproducibility defects. No raw dataset file contents were exposed in the reviewed artifacts, but the contract currently ships with incorrect or unverifiable evidence provenance and one JSON/CSV schema mismatch that can misroute manuscript evidence.

## Narrative Findings (AI reviewer)

## Critical Issues

### CR-01: BLOCKER - Ignored/untracked Seattle evidence is published in the claim contract without fail-closed validation

**File:** `scripts/generate_trace_sl_claim_contracts.py:301-328`, `scripts/generate_trace_sl_claim_contracts.py:555-566`, `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv:4-5`, `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json:63-71`, `TRC-23-02333/trace_sl_results/paper_sources/README.md:21`

**Issue:** `build_all_contracts()` only calls `assert_source_is_tracked()` for the two Stage 12 PeMS7_228 CSVs before generating every contract row. The generator then hardcodes additional evidence artifacts for PeMS7_1026, Seattle, Stage14 robustness, and `.planning/REQUIREMENTS.md` without checking that those artifacts exist, are tracked, or are allowed curated sources. The generated contract includes `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light`, but that directory is ignored by `.gitignore` and is not returned by `git ls-files`, so the manuscript-facing JSON/CSV can route evidence to a local-only artifact while the README claims the generators verify committed aggregate sources.

**Fix:** Validate every non-empty `evidence_artifact` before writing the CSV/JSON, and either unignore/track the Seattle evidence artifact or keep Seattle out of the Phase 7 contract until it is committed. For example:

```python
def assert_evidence_artifact_is_tracked(project_root: Path, artifact: str) -> None:
    if artifact.startswith("TRC-23-02333/dataset/"):
        raise ValueError(f"Evidence artifact references raw dataset path: {artifact}")
    if artifact.startswith(TRACE_RESULTS_ROOT.as_posix() + "/"):
        assert_source_is_tracked(project_root, project_root / artifact)
        return
    result = subprocess.run(
        ["git", "-C", str(project_root), "ls-files", "--error-unmatch", artifact],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode != 0:
        raise ValueError(f"Evidence artifact is not committed/tracked by git: {artifact}")

# after claim_rows are built and before writing outputs
for row in claim_rows:
    assert_evidence_artifact_is_tracked(project_root, str(row["evidence_artifact"]))
```

### CR-02: BLOCKER - Claim rows misattribute non-Stage12 evidence to the PeMS7_228 Stage12 layout CSV

**File:** `scripts/generate_trace_sl_claim_contracts.py:254-256`, `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv:2-12`

**Issue:** `build_claim_contract_rows()` creates one metadata block from `stage12_dir` and `layout_csv`, then reuses that same `source_stage`, `source_dir`, and `source_csv` for theory, external-evidence, robustness, and wording-policy rows. As a result, rows whose actual `evidence_artifact` is `.planning/REQUIREMENTS.md`, `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight`, `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light`, or Stage14 robustness files still claim `source_dir=TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio` and `source_csv=gls_map_layout_summary.csv`. Downstream table/rendering code that trusts the provenance columns can cite or audit the wrong source, defeating the Phase 7 evidence-routing contract.

**Fix:** Populate provenance from the row's actual evidence source, or rename the columns if they are intended to describe the generator seed rather than evidence provenance. A minimal fix is to build metadata per row:

```python
def evidence_metadata(source_stage: str, artifact: str) -> dict[str, str]:
    artifact_path = Path(artifact)
    return {
        "source_stage": source_stage,
        "source_dir": artifact_path.parent.as_posix(),
        "source_csv": artifact_path.name,
    }

# Example for robustness row:
_claim_row(
    evidence_metadata(
        "stage14_robustness",
        "TRC-23-02333/trace_sl_results/pems7_228_stage14_robustness/gls_map_layout_summary.csv",
    ),
    ...
)
```

If directory-level artifacts remain allowed, add explicit `source_artifact_type` or use a tracked summary CSV/Markdown file instead of overloading `source_csv`.

## Warnings

### WR-01: WARNING - JSON policy omits `greedy_d_logdet` even though the CSV main-table contract includes it

**File:** `scripts/generate_trace_sl_claim_contracts.py:440-448`, `scripts/generate_trace_sl_claim_contracts.py:537-540`, `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv:11`, `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv:22`, `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv:33`, `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json:46-57`

**Issue:** `build_main_table_contract_rows()` appends the optional `greedy_d_logdet` baseline when it is present in the Stage12 layout summary, and the generated CSV contains three `greedy_d_logdet` rows. However, `build_claim_contract_policy()` serializes `main_table_layout_labels` from the fixed `MAIN_TABLE_LAYOUT_LABELS` tuple, which excludes that optional label. The JSON policy therefore does not fully describe the generated CSV contract, so downstream consumers using the JSON as the schema/allow-list can silently drop or reject valid rows.

**Fix:** Derive the JSON labels from the generated `main_rows`, preserving the canonical order and appending present optional labels:

```python
def main_table_labels_in_rows(main_rows: Sequence[dict[str, object]]) -> list[str]:
    ordered = list(MAIN_TABLE_LAYOUT_LABELS) + [SECONDARY_CERTIFICATE_BASELINE]
    present = {str(row["layout_type"]) for row in main_rows}
    return [label for label in ordered if label in present]

# in build_claim_contract_policy()
"main_table_layout_labels": main_table_labels_in_rows(main_rows),
```

Also add a regression assertion that `set(policy["main_table_layout_labels"]) == {row["layout_type"] for row in main_rows}`.

---

_Reviewed: 2026-05-23T12:17:01Z_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
