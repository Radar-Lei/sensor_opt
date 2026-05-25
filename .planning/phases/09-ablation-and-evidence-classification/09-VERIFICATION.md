---
phase: 09-ablation-and-evidence-classification
verified: 2026-05-25
status: passed
score: 5/5 must-haves verified
overrides_applied: 0
---

# Phase 09: Ablation and Evidence Classification Verification Report

**Phase Goal:** Freeze the ablation logic and classify every dataset by evidence strength for TRACE-SL paper-source artifacts, while preserving fail-closed EVID-03/EVID-04 boundaries.
**Verified:** 2026-05-25
**Status:** passed

## Goal Achievement

| # | Truth | Status | Evidence |
|---|---|---|---|
| 1 | Phase 9 produces ablation contracts covering the required row families. | VERIFIED | `ablation_contract.csv/json` contain 36 rows including random, validation-selected random, certificate-only greedy, RCSS-selected, validation-swap-selected, and multistart validation-swap variants. |
| 2 | The ablation contract exposes component-layer explanations without using validation MAE as held-out evidence. | VERIFIED | Rows include `component_layer`, `supported_question`, `comparison_target`, `claim_route`, and `evidence_basis=held_out_test_aggregate`; tests reject `validation_mae` as held-out evidence. |
| 3 | Dataset evidence classification is generated as CSV/JSON-first paper-source data. | VERIFIED | `dataset_evidence_classification.csv/json` contain PeMS7_228, PeMS7_1026, Seattle, and robustness stress-test rows. |
| 4 | PeMS7_1026 and Seattle remain non-completing unless committed ten-split Stage12 aggregate evidence exists. | VERIFIED | `external_evidence_gate.json` remains fail-closed; generated rows have `requirement_complete=false` and `core_claim_eligible=false` for PeMS7_1026 and Seattle. |
| 5 | Code review fail-closed findings are closed. | VERIFIED | Final re-review confirmed CR-01, CR-02, CR-03, WR-01, WR-02, and WR-03 resolved. |

**Score:** 5/5 must-haves verified

## Required Artifacts

| Artifact | Expected | Status |
|---|---|---|
| `scripts/generate_trace_sl_ablation_evidence_contracts.py` | Fail-closed generator | VERIFIED |
| `scripts/test_generate_trace_sl_ablation_evidence_contracts.py` | Regression tests for generator policy | VERIFIED |
| `TRC-23-02333/trace_sl_results/paper_sources/ablation_contract.csv` | Ablation contract table | VERIFIED |
| `TRC-23-02333/trace_sl_results/paper_sources/ablation_contract.json` | Ablation contract JSON with metadata | VERIFIED |
| `TRC-23-02333/trace_sl_results/paper_sources/dataset_evidence_classification.csv` | Dataset evidence classification table | VERIFIED |
| `TRC-23-02333/trace_sl_results/paper_sources/dataset_evidence_classification.json` | Dataset classification JSON with metadata | VERIFIED |
| `TRC-23-02333/trace_sl_results/paper_sources/README.md` | Regeneration block | VERIFIED |

## Requirement Coverage

| Requirement | Status | Evidence |
|---|---|---|
| ABLT-01 | SATISFIED | Required ablation variants are present in `ablation_contract.csv/json`. |
| ABLT-02 | SATISFIED | Certificate-only rows are represented with certificate candidate-generation metadata. |
| ABLT-03 | SATISFIED | Validation selection and validation-aware swap layers are represented separately. |
| ABLT-04 | SATISFIED | RCSS is classified by certificate, validation, and local-refinement layers rather than kitchen-sink prose. |
| EVID-05 | SATISFIED | Dataset rows classify PeMS7_228, PeMS7_1026, Seattle, and robustness stress tests by evidence lane. |
| EVID-03 | NON-COMPLETING | PeMS7_1026 remains blocked/conditional until committed ten-split Stage12 aggregate evidence exists. |
| EVID-04 | NON-COMPLETING | Seattle remains blocked from core claims until committed ten-split Stage12 aggregate evidence exists. |

## Verification Commands

| Command | Result |
|---|---|
| `python scripts/test_generate_trace_sl_ablation_evidence_contracts.py` | 14 tests passed |
| `python -m py_compile scripts/generate_trace_sl_ablation_evidence_contracts.py scripts/test_generate_trace_sl_ablation_evidence_contracts.py` | passed |
| `python scripts/generate_trace_sl_ablation_evidence_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources` | regenerated 36 ablation rows and 4 dataset rows |
| Inline JSON integrity check | passed; external gate snapshot remains fail-closed and metadata `source_artifacts` contain no semicolon pseudo-paths |

## Review Closure

Final review confirmed:

- CR-01 resolved: committed evidence paths must exist in `HEAD` and have no dirty diff.
- CR-02 resolved: external completion requires gate boolean, split counts, committed clean aggregate CSVs, real aggregate split count, layout summary completeness, and paired evidence completeness.
- CR-03 resolved: ablation rows require actual split count to equal required split count.
- WR-01 resolved: gate booleans require JSON boolean values.
- WR-02 resolved: duplicate layout and paired keys fail closed.
- WR-03 resolved: metadata `source_artifacts` are normalized to real paths.

## Final Verdict

Phase 9 is passed. The phase artifacts are ready for Phase 10 paper writing support, while EVID-03 and EVID-04 correctly remain pending until committed ten-split external Stage12 evidence exists.
