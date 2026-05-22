---
phase: 02-formulation-and-theory-bridge
verified: 2026-05-22T02:28:41Z
status: passed
score: 20/20 must-haves verified
overrides_applied: 0
gaps: []
deferred: []
human_verification: []
---

# Phase 2: Formulation and Theory Bridge Verification Report

**Phase Goal:** Provide the formal optimization formulation, surrogate objective, posterior-error derivation, and algorithm analysis needed to make TRACE-SL read as a method.
**Verified:** 2026-05-22T02:28:41Z
**Status:** passed
**Re-verification:** No — initial verification

## MVP Mode Note

ROADMAP marks Phase 2 as `mode: mvp`, but the phase goal is not in the canonical user-story format. The automated user-story validator returned `false`. Because this phase is a documentation/theory phase and the user explicitly requested must-have verification against actual files, this report verifies the phase through goal-backward method/theory artifact checks rather than user-flow coverage.

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|---|---|---|
| 1 | Roadmap SC1: budgeted sensor-set formulation with hidden-node reconstruction loss and transparent reconstruction model exists. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` contains `Notation`, `Budgeted Reconstruction-Aware Sensor-Set Problem`, `|S| <= k`, hidden complement `H`, reconstruction map, held-out loss, and transparent GLS/MAP/GSP model framing. |
| 2 | Roadmap SC2: TRACE-SL/RCSS is defined as tractable surrogate with validation loss, posterior trace, scenario CVaR trace, condition number, and coverage terms. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` section `TRACE-SL/RCSS Surrogate Objective` names all five terms and ties them to `make_rcss_row` / `rcss_candidate_scores`; implementation confirms fields at `transparent_estimator_eval.py` lines 425-466. |
| 3 | Roadmap SC3: linear-Gaussian GLS/MAP derivation connects posterior covariance trace to expected hidden-state squared error. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` section `Linear-Gaussian GLS/MAP Posterior-Error Bridge` states posterior precision/covariance and the expected hidden-state squared-error trace identity. |
| 4 | Roadmap SC4: posterior variance is framed as MAE-oriented empirical motivation with approximation caveats. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` `MAE-Oriented Interpretation and Caveats` explicitly says the bridge is empirical, not a broad guarantee; `NARRATIVE_REPORT.md` repeats the MAE caveat. |
| 5 | Roadmap SC5: validation-aware swap has stated complexity and fixed-candidate local-optimality conditions. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` `Validation-Aware Swap Analysis` gives `O(B I k (U-k) C_solve(n,T_val))`, dense-solver limitation, and fixed-candidate one-swap local optimality. Implementation confirms validation-swap behavior at `transparent_estimator_eval.py` lines 513-559 and candidate union at lines 935-962. |
| 6 | THEORY-06: optional TR Part B material identifies monotonicity, submodularity-like, approximation, stability, and stochastic/bilevel theory gaps. | VERIFIED | `02-TR-PART-B-THEORY-GAP-NOTE.md` includes `THEORY-06`, `D-13`, `D-14`, and bullets for monotonicity, approximate submodularity, approximation guarantees, stability under covariance perturbation, and stochastic/bilevel analysis. |
| 7 | D-01: TRACE-SL is budgeted sparse sensor-set design for hidden-node reconstruction, not candidate-pool tuning. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` formal problem; `NARRATIVE_REPORT.md` formulation subsection; `README.md` public method pointer. |
| 8 | D-02: train-derived ingredients, validation selection, and held-out test evaluation are separated. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` `Protocol Separation`; `NARRATIVE_REPORT.md` lines 31-37; implementation uses validation selection before test evaluation at `transparent_estimator_eval.py` lines 897-982. |
| 9 | D-03: traffic-network notation includes graph, S, H, x, y_S, reconstruction map, budget k. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` `Notation` contains all required symbols and budget constraint. |
| 10 | D-04: RCSS is predeclared surrogate/portfolio with validation loss, posterior trace, scenario CVaR trace, condition number, coverage. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` names all diagnostics; implementation fields verified in `make_rcss_row`. |
| 11 | D-05: auto weights are inner-validation model selection over fixed grid with selector/tuner splits. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` `Auto-Weight Selection`; implementation confirms `split_validation_for_tuning`, `parse_weight_grid`, and `select_auto_rcss_weights` at `transparent_estimator_eval.py` lines 402-504. |
| 12 | D-06: validation-aware swap uses fixed add-node universe from OR-guided candidate pool and accepts only validation GLS/MAP loss improvements. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` lines 127-135 describe fixed universe and acceptance rule; implementation confirms candidate union and `validation_mae` improvement filter. |
| 13 | D-07: posterior trace is connected to expected hidden-state squared error under linear-Gaussian assumptions. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` posterior bridge states the trace identity. |
| 14 | D-08: assumptions are explicit and no formal MAE guarantee is claimed. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` lists Gaussian/linear model, train-derived prior, regularization, fixed observations, and squared-error scope. |
| 15 | D-09: posterior variance is empirical MAE-oriented guide, not MAE theorem. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` and `NARRATIVE_REPORT.md` both state MAE mismatch and caveats. |
| 16 | D-10: swap complexity names candidate universe size, budget k, validation samples, solve cost, starts, iterations, dense-solver limitation. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` complexity subsection includes all required factors and dense solver limitation. |
| 17 | D-11: fixed-candidate local optimality is scoped to one-swap validation objective and implemented acceptance rule. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md` fixed-candidate local optimality statement is scoped and excludes global optimality. |
| 18 | D-12: certificate terminology remains certificate-guided/posterior-certificate-aware; no broad formal certification overclaim. | VERIFIED | `02-FORMULATION-THEORY-BRIDGE.md`, `02-TR-PART-B-THEORY-GAP-NOTE.md`, `NARRATIVE_REPORT.md`, and `README.md` use scoped terminology. The phrase `certified optimization` appears only in a negated sentence: `not evidence of broad certified optimization`. |
| 19 | D-13: TR Part B extension needs are findable without being current deliverables. | VERIFIED | `02-TR-PART-B-THEORY-GAP-NOTE.md` separates Transportation Science framing from TR Part B needs and marks them as additional material. |
| 20 | D-14: broad approximation/submodularity/stability proofs are deferred v2 unless future narrow theorem is scoped. | VERIFIED | `02-TR-PART-B-THEORY-GAP-NOTE.md` `Deferred v2` section explicitly marks broad proofs as future work. |

**Score:** 20/20 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|---|---|---|---|
| `.planning/phases/02-formulation-and-theory-bridge/02-FORMULATION-THEORY-BRIDGE.md` | Core formulation, surrogate, posterior-error bridge, MAE caveats, validation-swap analysis | VERIFIED | Exists; substantive 190-line artifact; `gsd-sdk query verify.artifacts` passed; terms and implementation anchors verified. |
| `.planning/phases/02-formulation-and-theory-bridge/02-TR-PART-B-THEORY-GAP-NOTE.md` | THEORY-06 TR Part B gap note | VERIFIED | Exists; substantive 69-line artifact; contains `THEORY-06`, `D-13`, `D-14`, named advanced theory gaps, and deferred-v2 boundary. |
| `NARRATIVE_REPORT.md` | Narrative method/theory bridge for manuscript handoff | VERIFIED | Contains `Formulation and theory bridge`, validation/test separation, posterior covariance trace, expected squared hidden-state error, and Phase 2 artifact links. |
| `README.md` | Public-facing pointer to formal method framing | VERIFIED | Contains reconstruction-aware sensor-set design pointer and links to both Phase 2 artifacts while preserving Stage 11 reproduction commands. |

### Key Link Verification

| From | To | Via | Status | Details |
|---|---|---|---|---|
| `02-FORMULATION-THEORY-BRIDGE.md` | `TRC-23-02333/transparent_estimator_eval.py` | Named implementation identifiers | VERIFIED | `gsd-sdk verify.key-links` passed; grep/read confirmed `solve_quadratic`, `certificate`, `rcss_candidate_scores`, `select_auto_rcss_weights`, `validation_swap_search`, and evaluation wiring. |
| `02-FORMULATION-THEORY-BRIDGE.md` | `01-CLAIM-EVIDENCE-CONTRACT.md` | Certificate terminology and validation/test guardrails | VERIFIED | Key-link check passed; contract contains validation MAE as selection evidence and certificate terminology boundaries. |
| `NARRATIVE_REPORT.md` | `02-FORMULATION-THEORY-BRIDGE.md` | Method/theory bridge reference | VERIFIED | Key-link check passed and file path appears in the narrative bridge subsection. |
| `README.md` | `02-FORMULATION-THEORY-BRIDGE.md` | Repository layout / method formulation link | VERIFIED | Key-link check passed and file path appears in current claim plus repository layout. |

### Data-Flow Trace (Level 4)

| Artifact | Data Variable | Source | Produces Real Data | Status |
|---|---|---|---|---|
| `02-FORMULATION-THEORY-BRIDGE.md` | Method/theory content | Planning requirements, Phase 1 guardrails, implementation anchors | Not a dynamic data renderer | N/A — documentation artifact |
| `NARRATIVE_REPORT.md` | Narrative claims | Curated result paths and Phase 2 bridge | Not a dynamic data renderer | N/A — documentation artifact |
| `README.md` | Public method pointer | Phase 2 bridge artifacts | Not a dynamic data renderer | N/A — documentation artifact |

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|---|---|---|---|
| Requirement terms are present across Phase 2 artifacts | Python term scan over bridge, TR note, narrative, README | THEORY-01..05 terms present in bridge; THEORY-06 terms present in TR note | PASS |
| Implementation anchors exist in actual evaluator | grep/read `transparent_estimator_eval.py` for named functions | All named anchors found; relevant selection/evaluation code read | PASS |
| Guardrail wording avoids broad certification overclaim | grep for `formally certified`, `certified optimization`, `guarantee` | No broad positive claim found; only negated `not evidence of broad certified optimization` | PASS |
| Raw dataset contents not used as evidence | file reads and scans avoided dataset files; grep counted only README placement paths | No raw dataset files were read; bridge/TR/narrative do not cite dataset paths as evidence. README has existing data-placement instructions only. | PASS |

### Probe Execution

| Probe | Command | Result | Status |
|---|---|---|---|
| Conventional probe discovery | `find scripts -path '*/tests/probe-*.sh' -type f` | No probe scripts found | SKIPPED |
| Phase-declared probe search | grep phase plans/summaries for probe paths | No probe declarations found | SKIPPED |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|---|---|---|---|---|
| THEORY-01 | 02-01, 02-02 | Budgeted sensor-set formulation with hidden-node reconstruction, held-out loss, transparent model | SATISFIED | `02-FORMULATION-THEORY-BRIDGE.md` notation/problem/protocol sections; `NARRATIVE_REPORT.md` and `README.md` expose the framing. |
| THEORY-02 | 02-01, 02-02 | TRACE-SL/RCSS surrogate objective with validation loss, posterior trace, scenario CVaR, condition, coverage | SATISFIED | Bridge surrogate section and implementation fields at `make_rcss_row` / `rcss_candidate_scores`. |
| THEORY-03 | 02-01, 02-02 | Linear-Gaussian GLS/MAP posterior-error derivation | SATISFIED | Bridge posterior-error section states posterior covariance trace to expected hidden-state squared error. |
| THEORY-04 | 02-01, 02-02 | MAE-oriented posterior variance caveats | SATISFIED | Bridge and narrative state MAE vs squared-error mismatch and empirical approximation boundary. |
| THEORY-05 | 02-01, 02-02 | Validation-aware swap complexity and local optimality | SATISFIED | Bridge swap analysis plus implementation confirmation in `validation_swap_search`. |
| THEORY-06 | 02-02 | Optional TR Part B theory-gap note | SATISFIED | `02-TR-PART-B-THEORY-GAP-NOTE.md` covers monotonicity, approximate submodularity, approximation, stability, stochastic/bilevel analysis, deferred v2. |

No orphaned Phase 2 requirements were found: `.planning/REQUIREMENTS.md` maps THEORY-01..THEORY-06 to Phase 2, and both plans collectively declare all six IDs.

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|---|---:|---|---|---|
| `02-FORMULATION-THEORY-BRIDGE.md` | 149 | `certified optimization` | Info | Appears only in the negated phrase `not evidence of broad certified optimization`; this honors D-12 rather than overclaiming. |
| `README.md` | 51-54 | `TRC-23-02333/dataset/...` | Info | Existing data-placement instructions, not cited as evidence. No raw dataset contents were read. |

No TODO/FIXME/XXX/TBD blockers, placeholders, or empty implementation stubs were found in the checked modified documentation files.

### Human Verification Required

None. This phase produced documentation/theory artifacts, not a visual/user-flow feature. Automated artifact, link, requirement, and guardrail checks were sufficient for the phase goal.

### Gaps Summary

No blocking gaps found. The phase goal is achieved in actual files: the formal formulation, RCSS surrogate, posterior-error bridge, MAE caveats, validation-swap analysis, TR Part B theory-gap note, narrative handoff, and README pointer all exist, are substantive, and are wired to implementation/guardrail sources.

---

_Verified: 2026-05-22T02:28:41Z_
_Verifier: Claude (gsd-verifier)_
