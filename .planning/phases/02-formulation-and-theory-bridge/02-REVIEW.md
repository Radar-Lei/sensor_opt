---
phase: 02-formulation-and-theory-bridge
reviewed: 2026-05-22T00:00:00Z
depth: standard
files_reviewed: 2
files_reviewed_list:
  - /home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md
  - /home/samuel/projects/sensor_opt/README.md
findings:
  critical: 2
  warning: 2
  info: 0
  total: 4
status: issues_found
---

# Phase 2: Code Review Report

## Summary

Reviewed `/home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md` and `/home/samuel/projects/sensor_opt/README.md` at standard depth. The main defects are paper-facing claim/evidence violations: formal “certified” branding without theorem-level support, promotion of non-curated ignored Seattle outputs as core cross-network evidence, and inconsistent/missing artifact references.

## Critical Issues

### CR-01: BLOCKER — “Robust Certified Sensor Search” overclaims formal certification

**File:** `/home/samuel/projects/sensor_opt/README.md:2`  
**File:** `/home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md:4,14`

**Issue:** Both reviewed files expand RCSS as “Robust Certified Sensor Search”. This violates the Phase 1 guardrail that certificate language must remain “certificate-guided”, “posterior-certificate-aware”, or diagnostic unless theorem-level guarantees exist. The Phase 2 bridge explicitly says posterior diagnostics do not become broad MAE or optimality guarantees.

**Fix:** Rename the expansion to avoid formal certification, e.g. `Robust Certificate-guided Sensor Search (RCSS)`, and reserve “certified” only for scoped theorem statements if later proven.

---

### CR-02: BLOCKER — Non-curated Seattle results are promoted as core cross-network evidence

**File:** `/home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md:171-193`  
**File:** `/home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md:205`

**Issue:** The narrative says Seattle “strengthens the cross-network claim” and cites Seattle certificate correlations as if they are core evidence. Phase 1 explicitly says Seattle must remain conditional/supporting-only unless Phase 4 curates repository-visible outputs. The cited Seattle result directory is currently ignored by `.gitignore`, so this is not a durable curated artifact.

**Fix:** Either remove Seattle from core claim language or rewrite it as conditional/supporting-only pending Phase 4 curation. If retained as core evidence, first unignore/curate the Seattle outputs, add reproducibility documentation, and audit consistency.

## Warnings

### WR-01: WARNING — Stage 11 selected-weight distribution is inconsistent with the 10-split section

**File:** `/home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md:112-143`

**Issue:** The section is labeled as “automatic weight selection, 10-split extension” and reports 10-split MAE, but the selected-weight table reports `5/5`, `3/5`, and `2/5` counts. That appears to describe the original five-split run, not the 10-split aggregate.

**Fix:** Either relabel the table as “original five-split selected weight distribution” or recompute/report the distribution over all 10 splits.

---

### WR-02: WARNING — Figure/table inventory references CSV files missing from the main 10-split aggregate

**File:** `/home/samuel/projects/sensor_opt/NARRATIVE_REPORT.md:227-239`

**Issue:** The inventory lists `validation_swap_delta_tests.csv` and `auto_weight_selection_summary.csv` as ready outputs, but these files are not present in the main 10-split aggregate directory `/home/samuel/projects/sensor_opt/TRC-23-02333/trace_sl_results/pems7_228_stage11_auto_weight_10split/`.

**Fix:** Replace these with existing aggregate artifacts such as `gls_map_paired_delta_tests.csv`, or add explicit directory-qualified references if those files only exist in older five-split outputs.
