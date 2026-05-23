# Roadmap: TRACE-SL Transportation Science Readiness

**Created:** 2026/05/21
**Last updated:** 2026/05/23

## Milestones

- [shipped] **v1.0 TRACE-SL Readiness** — Phases 1–6 shipped 2026-05-23 ([archive](milestones/v1.0-ROADMAP.md))
- [active] **v1.1 TRACE-SL Transportation Science Paper Foundation** — Phases 7–10 planned

## Overview

v1.1 freezes the Transportation Science paper foundation before manuscript drafting. The milestone turns the v1.0 readiness package into a claim-evidence-theory-experiment contract with frozen main evidence, mandatory external Stage12 evidence for PeMS7_1026 and Seattle, ablation logic, dataset evidence classification, theory-ready statements, and reproducibility-safe handoff artifacts. It does not generate introduction, related work, method, results, limitations, abstract, conclusion, or other manuscript prose.

## Phases

**Phase Numbering:**

- Phases 1–6: completed v1.0 milestone work
- Phases 7–10: v1.1 paper-foundation milestone work
- Decimal phases: urgent insertions between planned phases if needed

<details>
<summary>v1.0 TRACE-SL Readiness (Phases 1–6) — SHIPPED 2026-05-23</summary>

- [x] **Phase 1: Claim-Evidence Contract** - Established evidence-backed claim routing and overclaim guardrails.
- [x] **Phase 2: Formulation and Theory Bridge** - Formalized the optimization problem, surrogate, and posterior-error bridge.
- [x] **Phase 3: Baseline Portfolio** - Built the reviewer-facing comparator portfolio.
- [x] **Phase 4: Core Experiment Evidence** - Curated core held-out evidence, statistics, runtime, and sensitivity summaries.
- [x] **Phase 5: Robustness and Generality** - Produced bounded robustness and generality stress-test artifacts.
- [x] **Phase 6: Reproducibility and Artifact Curation** - Completed deterministic reproducibility and paper-source artifact handoff.

</details>

### v1.1 TRACE-SL Transportation Science Paper Foundation

- [x] **Phase 7: Claim and Main Table Contract** - Freeze the Transportation Science claim boundary, PeMS7_228 main table contract, caveats, and robustness routing.
- [ ] **Phase 8: External Stage12 Evidence** - Complete mandatory PeMS7_1026 and Seattle Stage12 10-split external evidence before external claims are elevated.
- [ ] **Phase 9: Ablation and Evidence Classification** - Freeze the ablation logic and classify every dataset by evidence strength.
- [ ] **Phase 10: Theory and Handoff Package** - Prepare theory-ready statements and reproducibility-safe paper-foundation handoff artifacts without manuscript prose.

## Phase Details

<details>
<summary>v1.0 TRACE-SL Readiness details are archived</summary>

See `.planning/milestones/v1.0-ROADMAP.md` for full Phase 1–6 details.

</details>

### Phase 7: Claim and Main Table Contract

**Goal**: Author has a frozen Transportation Science claim contract and main PeMS7_228 result-table contract that preserve the low-budget multistart caveat and keep robustness evidence in its supported lane.
**Depends on**: Phase 6
**Requirements**: CLAIM-01, CLAIM-02, CLAIM-03, CLAIM-04, EVID-01, EVID-02, HAND-01
**Success Criteria** (what must be TRUE):

  1. Author can point to a claim contract that frames TRACE-SL as transparent reconstruction-aware sparse sensor layout design rather than a toy-project or heuristic-improvement story.
  2. Author can identify which claims are Transportation Science-ready and which are TR Part B-level extensions requiring stronger theory.
  3. Author can inspect a frozen Stage12 PeMS7_228 main-table contract with the reviewer-facing baseline portfolio, paired deltas, and p-value summaries where available.
  4. Author can verify that forbidden wording and the PeMS7_228 low-budget multistart caveat are present in all claim-facing artifacts.
  5. Author can verify that robustness evidence is routed only as stress-test or appendix evidence unless multi-seed perturbation evidence is later added.

**Plans**: 2 plans
Plans:
**Wave 1**

- [x] 07-01-PLAN.md — Create tested fail-fast generator for claim and main-table contracts.

**Wave 2** *(blocked on Wave 1 completion)*

- [x] 07-02-PLAN.md — Generate frozen CSV/JSON-first contract artifacts and update paper-source index.

### Phase 8: External Stage12 Evidence

**Goal**: Author has mandatory Stage12 10-split external evidence for both PeMS7_1026 and Seattle, with Seattle blocked from core claims unless this phase succeeds.
**Depends on**: Phase 7
**Requirements**: EVID-03, EVID-04
**Success Criteria** (what must be TRUE):

  1. Author can inspect completed PeMS7_1026 Stage12 10-split evidence using the same budgets and reviewer-facing baseline portfolio as the main PeMS7_228 evidence.
  2. Author can inspect completed Seattle Stage12 10-split external/transfer-style evidence before Seattle appears in any core claim artifact.
  3. Author can trace each external-evidence result to committed summaries, generated tables, scripts, or manifests without relying on committed raw traffic datasets.
  4. Author can see an explicit milestone-completion gate that prevents v1.1 completion if Seattle Stage12 10-split evidence is missing or excluded from core claims.

**Plans**: 5 plans
Plans:
**Wave 1**

- [x] 08-01-PLAN.md — Prepare ten-split Stage12 external launchers and fail-closed evidence/gate generator.

**Wave 2** *(blocked on Wave 1 completion)*

- [ ] 08-02-PLAN.md — Generate and validate real PeMS7_1026 Stage12 ten-split aggregate evidence.
- [ ] 08-03-PLAN.md — Generate and validate real Seattle Stage12 ten-split aggregate evidence or preserve the Seattle blocker.

**Wave 3** *(blocked on Wave 2 completion)*

- [ ] 08-04-PLAN.md — Generate external evidence contract, Seattle gate, and provenance indexes.

**Wave 4** *(blocked on Wave 3 completion)*

- [ ] 08-05-PLAN.md — Synchronize roadmap, requirements, and state with gate truth.

### Phase 9: Ablation and Evidence Classification

**Goal**: Author has the ablation and dataset-classification evidence needed to explain why each TRACE-SL layer matters and where each dataset may be used.
**Depends on**: Phase 8
**Requirements**: ABLT-01, ABLT-02, ABLT-03, ABLT-04, EVID-05
**Success Criteria** (what must be TRUE):

  1. Author can compare random mean, validation-selected random, certificate-only greedy, RCSS-selected, validation-swap-selected, and multistart validation-swap variants in one ablation contract.
  2. Author can answer whether certificate candidate pools improve over random candidate pools using curated ablation evidence.
  3. Author can answer whether validation selection and validation-aware swap each add measurable value using curated ablation evidence.
  4. Author can classify every dataset as core, external, supporting, conditional, or appendix-only based on evidence strength.
  5. Author can describe RCSS as certificate layer, validation layer, and local refinement layer without presenting it as a kitchen-sink heuristic.

**Plans**: TBD

### Phase 10: Theory and Handoff Package

**Goal**: Author has a theory-ready and reproducibility-safe paper-foundation package that a later writing milestone can consume without drafting manuscript prose now.
**Depends on**: Phase 9
**Requirements**: THEORY-01, THEORY-02, THEORY-03, THEORY-04, THEORY-05, HAND-02, HAND-03
**Success Criteria** (what must be TRUE):

  1. Author can inspect a clean budgeted hidden-network reconstruction formulation with explicit train/validation/test separation.
  2. Author can inspect theory-ready statements for the posterior trace identity and monotonicity under the stated linear-Gaussian model.
  3. Author can inspect theory-ready statements for validation-aware one-swap local optimality and RCSS candidate/search/evaluation complexity.
  4. Author can open a paper-foundation handoff package that links each claim and table to committed summaries, generated tables, scripts, or manifests.
  5. Author can verify that the handoff contains no introduction, related work, method, results, limitations, abstract, conclusion, or other manuscript prose, and no committed raw traffic datasets.

**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 7 → 8 → 9 → 10

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. Claim-Evidence Contract | v1.0 | 1/1 | Complete | 2026-05-21 |
| 2. Formulation and Theory Bridge | v1.0 | 2/2 | Complete | 2026-05-22 |
| 3. Baseline Portfolio | v1.0 | 1/1 | Complete | 2026-05-22 |
| 4. Core Experiment Evidence | v1.0 | 6/6 | Complete | 2026-05-22 |
| 5. Robustness and Generality | v1.0 | 4/4 | Complete | 2026-05-23 |
| 6. Reproducibility and Artifact Curation | v1.0 | 3/3 | Complete | 2026-05-23 |
| 7. Claim and Main Table Contract | v1.1 | 2/2 | Complete   | 2026-05-23 |
| 8. External Stage12 Evidence | v1.1 | 1/5 | In Progress|  |
| 9. Ablation and Evidence Classification | v1.1 | 0/TBD | Not started | - |
| 10. Theory and Handoff Package | v1.1 | 0/TBD | Not started | - |

## Coverage

| Requirement | Phase |
|-------------|-------|
| CLAIM-01 | Phase 7 |
| CLAIM-02 | Phase 7 |
| CLAIM-03 | Phase 7 |
| CLAIM-04 | Phase 7 |
| EVID-01 | Phase 7 |
| EVID-02 | Phase 7 |
| EVID-03 | Phase 8 |
| EVID-04 | Phase 8 |
| EVID-05 | Phase 9 |
| ABLT-01 | Phase 9 |
| ABLT-02 | Phase 9 |
| ABLT-03 | Phase 9 |
| ABLT-04 | Phase 9 |
| THEORY-01 | Phase 10 |
| THEORY-02 | Phase 10 |
| THEORY-03 | Phase 10 |
| THEORY-04 | Phase 10 |
| THEORY-05 | Phase 10 |
| HAND-01 | Phase 7 |
| HAND-02 | Phase 10 |
| HAND-03 | Phase 10 |

**Coverage:** 21/21 v1.1 requirements mapped exactly once.

## Archived Artifacts

- [v1.0 roadmap archive](milestones/v1.0-ROADMAP.md)
- [v1.0 requirements archive](milestones/v1.0-REQUIREMENTS.md)
- [v1.0 milestone audit](milestones/v1.0-MILESTONE-AUDIT.md)
