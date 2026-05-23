# Roadmap: TRACE-SL Transportation Science Readiness

**Created:** 2026/05/21
**Mode:** Vertical MVP
**Granularity:** Standard

## Objective

Turn TRACE-SL from a strong experimental prototype into a Transportation Science-ready methodology paper while preserving strong claims and making every claim evidence-backed.

## Phase Overview

| # | Phase | Goal | Requirements |
|---|-------|------|--------------|
| 1 | 1/1 | Complete   | 2026-05-21 |
| 2 | 2/2 | Complete   | 2026-05-22 |
| 3 | 1/1 | Complete   | 2026-05-22 |
| 4 | 6/6 | Complete   | 2026-05-22 |
| 5 | 4/4 | Complete   | 2026-05-23 |
| 6 | 3/3 | Complete   | 2026-05-23 |

## Phases

### Phase 1: Claim-Evidence Contract
**Goal:** Define the strongest defensible TRACE-SL claim set and the exact evidence required for each claim before adding experiments or writing.

**Requirements:** CLAIM-01, CLAIM-02, CLAIM-03, CLAIM-04, CLAIM-05

**Success Criteria:**
1. A claim-evidence matrix exists that maps each primary claim to required experiment, theory, statistical support, or limitation wording.
2. The main contribution statement frames TRACE-SL as transparent reconstruction-aware sensor placement rather than candidate-pool tuning.
3. The 10% PeMS7_228 multistart caveat is represented as either a predeclared portfolio/comparator issue or a bounded low-budget caveat.
4. Terminology is constrained to “certificate-guided” or equivalent unless later theory justifies stronger certification language.
5. The positioning separates TRACE-SL from deterministic full-observability TSLP and black-box imputation/forecasting.

**Dependencies:** Existing README, NARRATIVE_REPORT, Stage 11 summaries, and codebase map.

### Phase 2: Formulation and Theory Bridge
**Goal:** Provide the formal optimization formulation, surrogate objective, posterior-error derivation, and algorithm analysis needed to make TRACE-SL read as a method.
**Mode:** mvp

**Requirements:** THEORY-01, THEORY-02, THEORY-03, THEORY-04, THEORY-05, THEORY-06

**Success Criteria:**
1. The manuscript has a budgeted sensor-set formulation with hidden-node reconstruction loss and a transparent reconstruction model.
2. TRACE-SL/RCSS is defined as a tractable surrogate with validation loss, posterior trace, scenario CVaR trace, condition number, and coverage terms.
3. A linear-Gaussian GLS/MAP derivation connects posterior covariance trace to expected hidden-state squared error.
4. The method section explains how posterior variance motivates MAE-oriented selection and where assumptions are empirical approximations.
5. Validation-aware swap has stated complexity and fixed-candidate local-optimality conditions.

**Dependencies:** Phase 1 claim-evidence contract.

### Phase 3: Baseline Portfolio
**Goal:** Build a reviewer-resistant baseline set so the strong claim is supported against OR, graph sampling, sparse reconstruction, and learning-style alternatives.
**Mode:** mvp

**Requirements:** BASE-01, BASE-02, BASE-03, BASE-04, BASE-05, BASE-06

**Success Criteria:**
1. Observability-inspired/TSLP-style baselines are implemented or documented with a comparable reconstruction-evaluation adaptation.
2. A-optimal and D-optimal design baselines appear as independent reported baselines, not only as RCSS candidate sources.
3. Graph sampling/GSP baseline coverage is either implemented or explicitly tied to existing GSP evaluator evidence.
4. QR/SVD/POD sparse sensor placement is implemented where compatible with the traffic matrix representation.
5. A simple learning-based reconstruction check is run or a defensible deferral is documented.
6. Multistart validation refinement is a predeclared comparator or portfolio member, preventing post-hoc selection criticism.

**Dependencies:** Phase 2 method definition.

### Phase 4: Core Experiment Evidence
**Goal:** Produce the main held-out evidence package that supports the Transportation Science performance and certificate-guided claims.
**Mode:** mvp

**Requirements:** EXP-01, EXP-02, EXP-03, EXP-04, EXP-05, EXP-06

**Success Criteria:**
1. PeMS7_228 10-split evidence is audited or regenerated for all final method variants and core baselines.
2. PeMS7_1026 is either extended to at least 10 splits or explicitly presented as lower-power external evidence.
3. Seattle evidence is either curated into `trace_sl_results/` with synchronized documentation or removed from the core claim set.
4. Reported comparisons include paired deltas, confidence/bootstrap intervals, effect sizes, and suitable paired tests.
5. Certificate-error correlations are reported and interpreted as empirical support unless a formal theorem is added.
6. Runtime and candidate-count sensitivity summaries exist for the main claim settings.

**Dependencies:** Phase 3 baseline portfolio.

### Phase 5: Robustness and Generality
**Goal:** Show TRACE-SL remains useful under realistic sensing failures, noisy observations, missing data, heterogeneous costs, temporal shift, and candidate-pool changes.
**Mode:** mvp

**Requirements:** ROBUST-01, ROBUST-02, ROBUST-03, ROBUST-04, ROBUST-05, ROBUST-06

**Success Criteria:**
1. Sensor-failure experiments report degradation at 5%, 10%, and 20% random sensor drops after layout selection.
2. Observation-noise experiments quantify reconstruction degradation under perturbed sensor readings.
3. Missingness experiments cover missing sensor readings or missing time blocks at validation/test time.
4. Nonuniform sensor-cost experiments or a documented proxy evaluate heterogeneous installation-budget effects.
5. Temporal distribution-shift experiments use time-blocked splits when dataset timestamps support them.
6. Candidate-count sensitivity compares performance and runtime across 50/100/200/500-style candidate budgets.

**Dependencies:** Phase 4 core experiment harness and final baseline/method labels.

### Phase 6: Reproducibility and Artifact Curation
**Goal:** Make every paper-visible number traceable to curated scripts, summaries, and non-sensitive artifacts while keeping raw datasets local.
**Mode:** mvp

**Requirements:** REPRO-01, REPRO-02, REPRO-03, REPRO-04, REPRO-05

**Success Criteria:**
1. Scripts/configs record seeds, budgets, candidate counts, package versions where feasible, and enough provenance for table regeneration.
2. Raw traffic datasets remain ignored and are not committed.
3. Repository documentation and manuscript references point only to curated, present, reproducible result directories.
4. Paper tables and figures are generated from committed result artifacts rather than manually copied values.
5. Smoke or validation scripts check key commands and required aggregate layout/method rows.

**Dependencies:** Phases 4 and 5 evidence outputs.


## Requirement Coverage

| Phase | Requirements Covered | Count |
|-------|----------------------|-------|
| Phase 1 | CLAIM-01, CLAIM-02, CLAIM-03, CLAIM-04, CLAIM-05 | 5 |
| Phase 2 | THEORY-01, THEORY-02, THEORY-03, THEORY-04, THEORY-05, THEORY-06 | 6 |
| Phase 3 | BASE-01, BASE-02, BASE-03, BASE-04, BASE-05, BASE-06 | 6 |
| Phase 4 | EXP-01, EXP-02, EXP-03, EXP-04, EXP-05, EXP-06 | 6 |
| Phase 5 | ROBUST-01, ROBUST-02, ROBUST-03, ROBUST-04, ROBUST-05, ROBUST-06 | 6 |
| Phase 6 | REPRO-01, REPRO-02, REPRO-03, REPRO-04, REPRO-05 | 5 |

**Coverage:** 34 / 34 v1 requirements mapped.

## Next Step

Start with `/gsd:discuss-phase 1` to turn the claim-evidence contract into a concrete execution plan.
