---
phase: 07-claim-and-main-table-contract
reviewed: 2026-05-23T00:00:00Z
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
  critical: 0
  warning: 1
  info: 0
  total: 1
status: issues_found
---

# Phase 07: Code Review Report

**Reviewed:** 2026-05-23T00:00:00Z
**Depth:** standard
**Files Reviewed:** 6
**Status:** issues_found

## Summary

Re-reviewed the Phase 7 claim/main-table contract generator, regression tests, and generated CSV/JSON/README artifacts after the CR-01, CR-02, and WR-01 fixes. The prior blocking evidence-routing defects are resolved: Seattle is no longer published in the Phase 7 contract, every nonempty claim evidence artifact is fail-closed against git tracking, claim-row provenance now matches each evidence artifact, and the JSON policy includes the optional `greedy_d_logdet` label present in `main_table_contract.csv`. One remaining evidence-routing robustness issue remains in the main-table contract path.

## Narrative Findings (AI reviewer)

## Warnings

### WR-01: WARNING - Main-table comparator rows can ship without paired-stat evidence while still being routed through the paired-test source

**File:** `scripts/generate_trace_sl_claim_contracts.py:481-502`, `scripts/generate_trace_sl_claim_contracts.py:512-534`, `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv:4`, `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv:15`, `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv:26`

**Issue:** `build_main_table_contract_rows()` silently emits blank `delta_mean`, confidence interval, p-value, and `win_count` fields whenever `_paired_lookup()` has no `(budget, layout_type)` row. `validate_main_table_contract_rows()` only checks required labels and caveats, so the generated contract currently includes `rcss_selected` reviewer-baseline rows with `paired_baseline=rcss_selected` but empty paired statistics while the row provenance still lists `gls_map_paired_delta_tests.csv`. Downstream manuscript/table code can therefore route these rows as paired-stat-supported evidence even though no paired comparison exists for that comparator-budget pair.

**Fix:** Fail closed for reviewer-baseline rows unless paired statistics are present, or add an explicit evidence status column that marks such rows as descriptive-only and prevents paired-comparison claims. For a fail-closed contract, add a validation check similar to:

```python
paired_stat_columns = ("delta_mean", "ci95_low", "ci95_high", "paired_t_p", "wilcoxon_p", "win_count")
for row in rows:
    if row["table_role"] == "reviewer_baseline":
        missing = [column for column in paired_stat_columns if row[column] == "" or pd.isna(row[column])]
        if missing:
            raise ValueError(
                f"missing paired statistics for {row['layout_type']} at budget {row['budget']}: {missing}"
            )
```

Alternatively, if `rcss_selected` is intentionally descriptive only, add a column such as `paired_evidence_status=descriptive_only`, remove `gls_map_paired_delta_tests.csv` from those rows' provenance, and ensure manuscript rendering never treats those rows as paired-test evidence.

---

_Reviewed: 2026-05-23T00:00:00Z_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
