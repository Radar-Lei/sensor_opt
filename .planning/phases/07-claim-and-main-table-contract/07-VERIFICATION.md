---
phase: 07-claim-and-main-table-contract
verified: 2026-05-23T12:43:58Z
status: passed
score: 5/5 must-haves verified
overrides_applied: 0
---

# Phase 7: Claim and Main Table Contract Verification Report

**Phase Goal:** Author has a frozen Transportation Science claim contract and main PeMS7_228 result-table contract that preserve the low-budget multistart caveat and keep robustness evidence in its supported lane.
**Verified:** 2026-05-23T12:43:58Z
**Status:** passed
**Re-verification:** No — initial verification

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | Author can point to a claim contract that frames TRACE-SL as transparent reconstruction-aware sparse sensor layout design rather than a toy-project or heuristic-improvement story. | VERIFIED | `claim_contract.csv` row `CLAIM-01` is `core_in_domain` / `transportation_science_ready` and its notes say `transparent reconstruction-aware sparse sensor layout design with validation-swap-selected main method`; generator constant/function path exists in `scripts/generate_trace_sl_claim_contracts.py`. |
| 2 | Author can identify which claims are Transportation Science-ready and which are TR Part B-level extensions requiring stronger theory. | VERIFIED | `claim_contract.csv` separates `CLAIM-01` and `EVID-01` as `transportation_science_ready` from `CLAIM-02` as `tr_part_b_extension` / `requires_stronger_theory`; `claim_contract.json` lists both statuses and lanes. |
| 3 | Author can inspect a frozen Stage12 PeMS7_228 main-table contract with the reviewer-facing baseline portfolio, paired deltas, and p-value summaries where available. | VERIFIED | `main_table_contract.csv` has 33 rows from `pems7_228_stage12_baseline_portfolio`, includes the required reviewer-facing baselines, has 27 `paired_stats_available` rows with `delta_mean`, `paired_t_p`, and `wilcoxon_p`, and keeps 6 `descriptive_only` rows with blank paired-test fields. |
| 4 | Author can verify that forbidden wording and the PeMS7_228 low-budget multistart caveat are present in all claim-facing artifacts. | VERIFIED | `claim_contract.csv`, `claim_contract.json`, and `claim_contract.md` include all forbidden terms: `optimal`, `certified`, `globally robust`, `guaranteed MAE improvement`, and `generalizes across networks`; claim/table artifacts contain `pems7_228_low_budget_multistart_not_dominant` on claim rows, all 10% table rows, and all multistart comparison rows. |
| 5 | Author can verify that robustness evidence is routed only as stress-test or appendix evidence unless multi-seed perturbation evidence is later added. | VERIFIED | `claim_contract.csv` rows `HAND-01-STRESS` and `HAND-01-APPENDIX` use `stress_test` and `appendix`; `claim_contract.json` says robustness is `stress_test or appendix unless source row declares multi-seed perturbation evidence`; tests enforce lane violations fail closed. |

**Score:** 5/5 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|---|---|---|---|
| `scripts/generate_trace_sl_claim_contracts.py` | Deterministic claim/table contract generator | VERIFIED | Exists and substantive; exports the planned builder/validator functions and constants; `build_all_contracts()` reads tracked Stage12 PeMS7_228 aggregate CSVs and writes CSV/JSON/Markdown outputs. |
| `scripts/test_generate_trace_sl_claim_contracts.py` | Regression tests for guardrails | VERIFIED | Exists and substantive; `ClaimContractGenerationTests` covers forbidden wording, external/core routing, robustness lanes, descriptive-only paired evidence, source tracking, and caveat tags. |
| `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.csv` | CSV claim boundary contract | VERIFIED | Nonempty, schema-present, 11 rows; includes claim lanes/statuses, forbidden wording, evidence artifact pointers, and caveat tag fields. |
| `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.json` | Machine-readable claim policy | VERIFIED | Nonempty; contains `trace_sl_claim_contract_v1`, forbidden wording list, routing policy, caveat tags, source artifacts, row counts, and main-table labels. |
| `TRC-23-02333/trace_sl_results/paper_sources/claim_contract.md` | Generated Markdown claim-contract view | VERIFIED | Nonempty generated table with `forbidden_wording` column and all forbidden terms. Note: `gsd-sdk verify.artifacts` flagged missing exact text `Forbidden wording`, but direct content inspection verifies the list is present as generated snake_case table schema, not prose. |
| `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.csv` | Frozen PeMS7_228 main-table result contract | VERIFIED | Nonempty, 33 rows; includes `validation_swap_selected`, required baselines, provenance, caveats, paired-stat status, deltas, and p-values where available. |
| `TRC-23-02333/trace_sl_results/paper_sources/main_table_contract.md` | Generated Markdown main-table view | VERIFIED | Nonempty generated table containing `pems7_228_low_budget_multistart_not_dominant` and paired/descriptive status fields. |
| `TRC-23-02333/trace_sl_results/paper_sources/README.md` | Paper-source artifact index | VERIFIED | Lists Phase 7 contract files, regeneration command, provenance columns, and raw-data hygiene sentence; no manuscript-section headings found. |

### Key Link Verification

| From | To | Via | Status | Details |
|---|---|---|---|---|
| `scripts/generate_trace_sl_claim_contracts.py` | `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/gls_map_layout_summary.csv` | `STAGE12_DIR` plus `build_all_contracts()` source load | VERIFIED | Manual inspection confirms `STAGE12_DIR` is `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio` and `build_all_contracts()` loads `gls_map_layout_summary.csv` after `assert_source_is_tracked()`. |
| `scripts/generate_trace_sl_claim_contracts.py` | `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/gls_map_paired_delta_tests.csv` | `STAGE12_DIR` plus `build_all_contracts()` source load | VERIFIED | Manual inspection confirms the paired CSV is loaded and joined via `_paired_lookup()` for `validation_swap_selected`. |
| `scripts/test_generate_trace_sl_claim_contracts.py` | `scripts/generate_trace_sl_claim_contracts.py` | Dynamic import | VERIFIED | Uses `GENERATOR_PATH = PROJECT_ROOT / "scripts" / "generate_trace_sl_claim_contracts.py"` and `spec_from_file_location`. |
| `main_table_contract.csv` | Stage12 layout and paired-stat source CSVs | Provenance columns and paired-stat fields | VERIFIED | `source_dir/source_csv` columns point to `pems7_228_stage12_baseline_portfolio`; paired rows include `gls_map_paired_delta_tests.csv`, descriptive-only rows do not. |
| `README.md` | `scripts/generate_trace_sl_claim_contracts.py` | Regeneration command | VERIFIED | README contains `python scripts/generate_trace_sl_claim_contracts.py --project-root /home/samuel/projects/sensor_opt --output-dir TRC-23-02333/trace_sl_results/paper_sources`. |

### Data-Flow Trace (Level 4)

| Artifact | Data Variable | Source | Produces Real Data | Status |
|---|---|---|---|---|
| `main_table_contract.csv` | `main_rows` | `gls_map_layout_summary.csv` plus `gls_map_paired_delta_tests.csv` loaded by `build_all_contracts()` | Yes | FLOWING — source CSVs are tracked curated aggregate files, rows are nonempty, and generated contract has 33 rows. |
| `claim_contract.csv` / `claim_contract.json` | `claim_rows` and policy metadata | Generator constants plus tracked evidence artifacts validated by `assert_evidence_artifact_is_tracked()` | Yes | FLOWING — claim rows point to committed `.planning` and `trace_sl_results` artifacts; raw dataset paths are rejected. |

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|---|---|---|---|
| Contract regression tests pass | `python /home/samuel/projects/sensor_opt/scripts/test_generate_trace_sl_claim_contracts.py` | `Ran 8 tests ... OK` | PASS |
| Contract invariants hold | Inline Python parser over `claim_contract.*`, `main_table_contract.*`, and README | `claim_rows 11`, `main_rows 33`, `paired_rows 27`, `descriptive_rows 6`, raw dataset paths absent, manuscript headings absent | PASS |

### Probe Execution

| Probe | Command | Result | Status |
|---|---|---|---|
| No declared or conventional Phase 7 probes | Search of phase plans/summaries and `scripts/*/tests/probe-*.sh` | No probe files found | SKIPPED |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|---|---|---|---|---|
| CLAIM-01 | 07-01, 07-02 | Paper-level contribution is transparent reconstruction-aware sparse sensor layout design, not heuristic improvement story. | SATISFIED | `CLAIM-01` row in `claim_contract.csv` states the framing in notes and is marked TS-ready/core-in-domain. |
| CLAIM-02 | 07-01, 07-02 | Distinguish Transportation Science-ready claims from TR Part B-level claims needing stronger theory. | SATISFIED | `CLAIM-02` row is `tr_part_b_extension` / `requires_stronger_theory`; TS-ready rows are separately marked. |
| CLAIM-03 | 07-01, 07-02 | Explicit forbidden wording list covers required terms. | SATISFIED | CSV/JSON/Markdown contain all five required forbidden terms; tests assert exact tuple. |
| CLAIM-04 | 07-01, 07-02 | Preserve PeMS7_228 low-budget multistart caveat in claim-facing artifacts. | SATISFIED | `pems7_228_low_budget_multistart_not_dominant` is in claim policy/artifacts and on all 10% table rows and multistart comparison rows. |
| EVID-01 | 07-01, 07-02 | Stage12 PeMS7_228 baseline portfolio is frozen main in-domain result table. | SATISFIED | `main_table_contract.csv` uses `source_stage=stage12_baseline_portfolio` and `source_dir=.../pems7_228_stage12_baseline_portfolio`. |
| EVID-02 | 07-01, 07-02 | Paired delta and p-value summaries exist against reviewer-facing baselines where available. | SATISFIED | Required baselines are present; paired rows include `delta_mean`, `paired_t_p`, `wilcoxon_p`; unavailable rows are marked `descriptive_only`. |
| HAND-01 | 07-01, 07-02 | Robustness evidence remains stress-test or appendix unless multi-seed perturbation evidence is added. | SATISFIED | `HAND-01-STRESS` and `HAND-01-APPENDIX` rows use only `stress_test`/`appendix`; tests reject unsupported core robustness lanes. |

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|---|---:|---|---|---|
| None |  |  |  | Debt/stub scan over modified Phase 7 files found no `TBD`, `FIXME`, `XXX`, TODO/HACK/PLACEHOLDER, placeholder prose, empty implementations, or console-only implementations. |

### Human Verification Required

None. The deliverable is machine-readable/generated research contracts and all Phase 7 goal truths were verifiable through source inspection, parsed artifact checks, and the regression test command.

### Gaps Summary

No blocking gaps found. The phase goal is achieved: the frozen claim contract and PeMS7_228 main-table contract exist, are generated from tracked curated aggregate evidence, preserve the low-budget multistart caveat, separate TS-ready and TR Part B-level claims, keep PeMS7_1026/Seattle out of core claims, keep robustness in stress-test/appendix lanes, avoid raw dataset paths, and avoid manuscript prose.

---

_Verified: 2026-05-23T12:43:58Z_
_Verifier: Claude (gsd-verifier)_
