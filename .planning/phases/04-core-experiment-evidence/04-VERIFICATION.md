---
phase: 04-core-experiment-evidence
verified: 2026-05-22T18:12:11Z
status: passed
score: 6/6 must-haves verified
overrides_applied: 0
residual_caveats:
  - requirement: EXP-02
    caveat: "PeMS7_1026 remains lower-power external evidence with 5 held-out GLS/MAP splits; this is allowed by the Phase 4 contract when explicitly framed with uncertainty/effect-size language."
  - requirement: EXP-03
    caveat: "Seattle remains supporting/conditional evidence with synchronized scripts/results/docs; it is not core claim evidence unless a stronger bundle is later generated and reviewed."
---

# Phase 4: Core Experiment Evidence Verification Report

**Phase Goal:** Produce the main held-out evidence package that supports the Transportation Science performance and certificate-guided claims.
**Verified:** 2026-05-22T18:12:11Z
**Status:** passed
**Re-verification:** No — initial verification

## Goal Achievement

Phase 4 goal is achieved. The codebase contains a curated held-out evidence package for EXP-01 through EXP-06, backed by machine-readable CSV/Markdown artifacts, launchers, a final validator, and claim-contract synchronization. The package does not rely on pending commands or raw dataset paths as evidence.

Note: `.planning/ROADMAP.md` marks Phase 4 as `mode: mvp`, but the recorded goal is not in the canonical user-story form. This verification therefore used the user's requested goal-backward contract and the roadmap/requirements success criteria rather than a user-flow table.

### Observable Truths

| # | Truth | Status | Evidence |
|---|---|---|---|
| 1 | EXP-01: PeMS7_228 10-split evidence is audited/regenerated for all final variants and core baselines. | VERIFIED | `python .planning/phases/04-core-experiment-evidence/validate_phase4_evidence.py` reports PASS. `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/combined_metrics.csv` has held-out GLS/MAP split count 10..10, budgets 0.10/0.20/0.30, and required labels: `validation_swap_selected`, `rcss_selected`, `multistart_swap_by_validation`, `greedy_a_trace`, `greedy_d_logdet`, `observability_proxy`, `graph_sampling_laplacian`, `qr_pod_modes`. |
| 2 | EXP-02: PeMS7_1026 is extended to 10 splits or explicitly framed as lower-power external evidence. | VERIFIED with caveat | Validator reports WARN allowed by D-06. `TRC-23-02333/trace_sl_results/pems7_1026_stage11_auto_weight/combined_metrics.csv` has held-out GLS/MAP split count 5..5; `.planning/phases/04-core-experiment-evidence/04-DATASET-CLAIM-STATUS.md` and `TRC-23-02333/trace_sl_results/README.md` frame it as lower-power external evidence. |
| 3 | EXP-03: Seattle evidence is curated into `trace_sl_results/` with synchronized documentation or removed from the core claim set. | VERIFIED with caveat | Validator reports WARN allowed by D-07. `TRC-23-02333/trace_sl_results/seattle_stage11_auto_weight_light/` contains synchronized result artifacts with held-out GLS/MAP split count 5..5; docs mark it supporting/conditional, not core. |
| 4 | EXP-04: Reported comparisons include paired deltas, intervals, effect sizes, and paired tests. | VERIFIED | `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/gls_map_paired_delta_tests.csv` has 99 rows and required columns `ci95_low`, `ci95_high`, `cohens_dz`, `paired_t_p`, `wilcoxon_p`, `count`; greedy A/D baseline comparison rows are present. Stage 13 paired tests also pass schema checks. |
| 5 | EXP-05: Certificate-error correlations are reported and interpreted as empirical support. | VERIFIED | Stage 12 and Stage 13 include `combined_certificate_correlations.csv`, `certificate_correlation_summary.csv`, and SUMMARY wording: “empirical support for certificate-guided selection, not formal optimality guarantees.” |
| 6 | EXP-06: Runtime and candidate-count sensitivity summaries exist for main claim settings. | VERIFIED | `TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/runtime_candidate_sensitivity.csv` has measured runtime for candidate counts 50 and 100 with nonnegative `runtime_seconds`; `candidate_sensitivity_summary.csv` and `combined_rcss_candidates.csv` exist. |

**Score:** 6/6 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|---|---|---|---|
| `.planning/phases/04-core-experiment-evidence/validate_phase4_evidence.py` | Final EXP-01..EXP-06 validator | VERIFIED | Exists, substantive, passes `py_compile`, has tests, and reads curated result artifacts only. |
| `.planning/phases/04-core-experiment-evidence/04-EVIDENCE-AUDIT.md` | Final evidence status/caveat table | VERIFIED | Maps EXP-01..EXP-06 to artifact paths, statuses, caveats, and claim implications. |
| `.planning/phases/04-core-experiment-evidence/04-DATASET-CLAIM-STATUS.md` | PeMS7_1026/Seattle caveat record | VERIFIED | Documents lower-power PeMS7_1026 and supporting/conditional Seattle without raw-data evidence. |
| `TRC-23-02333/summarize_trace_sl_rcss.py` | Main aggregation script with statistical and sensitivity outputs | VERIFIED | Emits paired intervals/effect sizes/tests, empirical certificate summaries, candidate sensitivity, and runtime sensitivity when timing data exist. |
| `scripts/run_stage12_pems7_228.sh` | Reproducible Stage 12 PeMS7_228 launcher | VERIFIED | Includes ten seeds, budgets, Phase 3 portfolio flags, DRY_RUN path, and summarizer call. |
| `scripts/run_stage12_pems7_1026.sh` | Optional external extension launcher | VERIFIED | Exists and passes shell syntax checks. |
| `scripts/run_stage12_seattle.sh` | Optional Seattle extension launcher | VERIFIED | Exists and passes shell syntax checks. |
| `scripts/run_stage13_candidate_sensitivity_pems7_228.sh` | Candidate/runtime sensitivity launcher | VERIFIED | Exists, passes shell syntax, has DRY_RUN path, writes timing CSV and aggregated Stage 13 outputs. |
| `TRC-23-02333/trace_sl_results/pems7_228_stage12_baseline_portfolio/` | Primary in-domain held-out evidence bundle | VERIFIED | Contains 10 seed metrics plus aggregate CSV/Markdown files and required final/baseline labels. |
| `TRC-23-02333/trace_sl_results/pems7_228_stage13_candidate_sensitivity/` | Runtime/candidate sensitivity bundle | VERIFIED | Contains aggregate metrics, candidate diagnostics, measured runtime table, and tractability/stability summary. |
| `.planning/phases/01-claim-evidence-contract/01-CLAIM-EVIDENCE-CONTRACT.md` | Claim contract synchronized with Phase 4 evidence | VERIFIED | C-01..C-05 cite curated Stage 12/13/external/supporting evidence and preserve caveats. |

### Key Link Verification

| From | To | Via | Status | Details |
|---|---|---|---|---|
| `validate_phase4_evidence.py` | `TRC-23-02333/trace_sl_results/` | Artifact schema/status validation | VERIFIED | GSD key-link check passed for Plan 04-06; validator executes and reads curated evidence paths. |
| `04-EVIDENCE-AUDIT.md` | `01-CLAIM-EVIDENCE-CONTRACT.md` | Claim status synchronization | VERIFIED | GSD key-link check passed for Plan 04-06; claim contract contains Phase 4 evidence/caveat references. |
| `scripts/run_stage12_pems7_228.sh` | `TRC-23-02333/transparent_estimator_eval.py` | Phase 3 portfolio flags | VERIFIED | GSD key-link check passed for Plan 04-03; launcher includes `--include-greedy`, `--include-baseline-portfolio`, observability, graph-sampling, and QR/POD flags. |
| `scripts/run_stage12_pems7_228.sh` | `TRC-23-02333/summarize_trace_sl_rcss.py` | Post-run aggregation | VERIFIED | GSD key-link check passed for Plan 04-03. |
| `summarize_trace_sl_rcss.py` | `gls_map_paired_delta_tests.csv` | Paired comparison CSV writer | VERIFIED | GSD key-link check passed for Plan 04-02; generated outputs contain required statistical columns. |
| `summarize_trace_sl_rcss.py` | `certificate_correlation_summary.csv` | Certificate correlation aggregation | VERIFIED | GSD key-link check passed for Plan 04-02; generated summaries use empirical wording. |
| `scripts/run_stage13_candidate_sensitivity_pems7_228.sh` | `pems7_228_stage13_candidate_sensitivity/` | Candidate-count sweep outputs | VERIFIED | GSD pattern check was overly literal, but manual inspection confirms the launcher writes `candidates_<N>/`, uses `--rcss-random-candidates` and `--rcss-quality-candidates`, records `stage13_timing.csv`, and Stage 13 aggregated evidence exists. |

### Data-Flow Trace (Level 4)

| Artifact | Data Variable | Source | Produces Real Data | Status |
|---|---|---|---|---|
| `validate_phase4_evidence.py` | EXP status rows | Curated CSV/Markdown under `TRC-23-02333/trace_sl_results/` plus phase docs | Yes | VERIFIED |
| `summarize_trace_sl_rcss.py` | paired/certificate/candidate/runtime summaries | Seed-level `metrics.csv`, `certificate_correlations.csv`, `rcss_candidates.csv`, and Stage 13 timing/runtime CSVs | Yes | VERIFIED |
| Stage 12 evidence bundle | held-out GLS/MAP metrics | Ten seed `metrics.csv` files aggregated into `combined_metrics.csv` | Yes | VERIFIED |
| Stage 13 sensitivity bundle | runtime/candidate sensitivity | `stage13_timing.csv` and candidate-count run artifacts aggregated into runtime/candidate CSVs | Yes | VERIFIED |

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|---|---|---|---|
| Final Phase 4 validator reports EXP-01..EXP-06 status and raw-data hygiene | `python /home/samuel/projects/sensor_opt/.planning/phases/04-core-experiment-evidence/validate_phase4_evidence.py` | Exit 0; EXP-01/04/05/06 PASS, EXP-02/03 WARN allowed, RAW-DATA PASS | PASS |
| Validator/checker/summarizer compile and tests pass | `python -m py_compile ... && python .../test_summarize_trace_sl_rcss.py && python .../test_validate_phase4_evidence.py && python .../test_check_phase4_evidence_coverage.py` | Exit 0; 9 summarizer tests, 3 validator tests, checker source contract OK | PASS |
| Stage 12/13/external launchers are syntactically runnable | `bash -n scripts/run_stage12_pems7_228.sh && bash -n scripts/run_stage12_pems7_1026.sh && bash -n scripts/run_stage12_seattle.sh && bash -n scripts/run_stage13_candidate_sensitivity_pems7_228.sh` | Exit 0 | PASS |
| Evidence artifacts contain expected split counts, labels, statistical columns, and runtime rows | Python CSV inspection command | Stage 12 split range 10..10; required labels present; paired columns present; Stage 13 candidate counts [50, 100], min runtime 69.0 seconds | PASS |

### Probe Execution

No conventional `scripts/**/tests/probe-*.sh` probes or phase-declared probe scripts were found. Step 7c skipped.

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|---|---|---|---|---|
| EXP-01 | 04-01, 04-03, 04-06 | PeMS7_228 10-split evidence regenerated/audited for final variants and baselines | SATISFIED | Stage 12 PASS with 10 seed metrics and required final/portfolio labels. |
| EXP-02 | 04-01, 04-04, 04-06 | PeMS7_1026 ten-split or lower-power external framing | SATISFIED WITH CAVEAT | Five-split evidence documented as lower-power external in status/audit/README. |
| EXP-03 | 04-01, 04-04, 04-06 | Seattle curated or removed from core claims | SATISFIED WITH CAVEAT | Seattle result/scripts/docs synchronized as supporting/conditional, not core. |
| EXP-04 | 04-01, 04-02, 04-03, 04-06 | Paired deltas, intervals, effect sizes, paired tests | SATISFIED | Stage 12/13 paired CSVs include interval/effect/test/count columns. |
| EXP-05 | 04-01, 04-02, 04-06 | Certificate-error correlations reported as empirical validation | SATISFIED | Stage 12/13 certificate summaries and empirical/non-formal wording present. |
| EXP-06 | 04-01, 04-05, 04-06 | Runtime and candidate-count sensitivity reported | SATISFIED | Stage 13 runtime/candidate sensitivity CSVs and summary exist. |

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|---|---:|---|---|---|
| — | — | — | None | Scanned modified Phase 4 scripts/docs for TODO/FIXME/XXX/TBD, placeholder/incomplete wording, and obvious empty implementations; no blocker/warning anti-patterns found. |

### Human Verification Required

None. Verification is artifact/schema/command based; no visual, UX, external service, or subjective behavior requires human UAT for this phase.

### Residual Caveats

- PeMS7_1026 is not ten-split core-equivalent evidence. It is correctly framed as lower-power external evidence.
- Seattle is synchronized as supporting/conditional evidence, not core evidence.
- Stage 13 supports practical runtime/candidate-count tractability and selection-stability language only; it is not a broad scalability guarantee.
- The PeMS7_228 10% multistart caveat remains visible and should not be hidden by post-hoc best-method-per-budget selection.

### Gaps Summary

No blocking gaps found. All Phase 4 roadmap requirements EXP-01..EXP-06 are satisfied by codebase artifacts, with allowed caveats for EXP-02 and EXP-03.

---

_Verified: 2026-05-22T18:12:11Z_
_Verifier: Claude (gsd-verifier)_
