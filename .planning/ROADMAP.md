# Roadmap: TRACE-SL Transportation Research Part B Readiness

**Created:** 2026/05/21
**Last updated:** 2026/05/26

## Milestones

- [shipped] **v1.0 TRACE-SL Readiness** — Phases 1-6 shipped 2026-05-23 ([archive](milestones/v1.0-ROADMAP.md))
- [complete] **v1.1 TRACE-SL Transportation Science Paper Foundation** — Phases 7-10 complete; archived at `milestones/v1.1-ROADMAP.md`
- [active] **v1.2 TRACE-SL Transportation Research Part B Manuscript Drafting** — Phases 11-16 write, compile, improve, and submission-audit the TR Part B paper package

## Overview

v1.2 converts the frozen v1.1 paper foundation into a complete Transportation Research Part B manuscript. The milestone uses `$paper-writing` with `assurance: submission`, local `els-cas-templates/`, `NARRATIVE_REPORT.md`, and generated paper-source artifacts under `TRC-23-02333/trace_sl_results/paper_sources/`. Completion requires a compiled CAS-template PDF, two improvement-loop rounds, and green proof, claim, citation, and external audit-verifier gates.

## Phases

**Phase Numbering:**

- Phases 1-6: completed v1.0 readiness milestone work
- Phases 7-10: completed v1.1 paper-foundation milestone work
- Phases 11-16: active v1.2 TR Part B manuscript-writing milestone work
- Decimal phases: urgent insertions between planned phases if needed

<details>
<summary>v1.0 TRACE-SL Readiness (Phases 1-6) — SHIPPED 2026-05-23</summary>

See `.planning/milestones/v1.0-ROADMAP.md`.

</details>

<details>
<summary>v1.1 TRACE-SL Transportation Science Paper Foundation (Phases 7-10) — COMPLETE 2026-05-26</summary>

See `.planning/milestones/v1.1-ROADMAP.md`.

</details>

### v1.2 TRACE-SL Transportation Research Part B Manuscript Drafting

- [ ] **Phase 11: TR Part B Paper Plan and CAS Scaffold** - Create the paper plan, claim-evidence matrix, and Elsevier CAS source scaffold.
- [ ] **Phase 12: Figures, Tables, and Method Illustration** - Generate paper-visible figures/tables from committed result artifacts and create the method/workflow illustration.
- [ ] **Phase 13: Manuscript Writing** - Write complete English manuscript sections for a TR Part B audience.
- [ ] **Phase 14: CAS Compilation and Formatting** - Compile `paper/main.pdf`, fix LaTeX/template issues, and ensure references/figures resolve.
- [ ] **Phase 15: Improvement Loop** - Run two review/fix/recompile rounds and preserve comparison PDFs.
- [ ] **Phase 16: Submission Assurance Audits** - Run proof, claim, citation, and external verifier gates before declaring submission readiness.

## Phase Details

### Phase 11: TR Part B Paper Plan and CAS Scaffold

**Goal:** Author has a TR Part B-specific paper plan and an initialized CAS-template LaTeX source tree ready for figure generation and section writing.
**Depends on:** Phase 10
**Requirements:** PLAN-01, PLAN-02, PLAN-03, PLAN-04, TEX-01, TEX-03
**Success Criteria** (what must be TRUE):

1. `PAPER_PLAN.md` names Transportation Research Part B as the target and does not retain Transportation Science as the active venue.
2. The plan maps every central claim to `NARRATIVE_REPORT.md` and v1.1 paper-source artifacts.
3. The section plan covers all expected TR Part B manuscript sections and identifies which figures/tables each section needs.
4. Claim-boundary notes explicitly preserve multistart, multi-network, certificate-guided, and no-guarantee caveats.
5. `paper/` is scaffolded from local `els-cas-templates/` with metadata placeholders or completed fields.

**Plans:** 1 plan

- [ ] 11-01-PLAN.md — Run paper-plan setup and scaffold the CAS manuscript source.

### Phase 12: Figures, Tables, and Method Illustration

**Goal:** Author has reproducible data-driven paper tables/figures and a clear method/workflow illustration without relying on raw dataset paths.
**Depends on:** Phase 11
**Requirements:** FIG-01, FIG-02, FIG-03, FIG-04
**Success Criteria** (what must be TRUE):

1. Main performance, paired-delta, external-evidence, and ablation tables are generated from committed CSV/JSON paper-source artifacts.
2. Dataset evidence lanes and claim caveats are visible in generated table captions or table notes.
3. A TRACE-SL workflow/method figure explains reconstruction-aware inverse-problem design rather than a black-box heuristic.
4. Every numeric value intended for manuscript use traces to machine-readable evidence.

**Plans:** 1 plan

- [ ] 12-01-PLAN.md — Generate paper figures/tables and method illustration assets.

### Phase 13: Manuscript Writing

**Goal:** Author has complete English LaTeX manuscript prose grounded in v1.1 evidence and theory.
**Depends on:** Phase 12
**Requirements:** WRITE-01, WRITE-02, WRITE-03, WRITE-04, WRITE-05
**Success Criteria** (what must be TRUE):

1. Abstract and introduction make a TR Part B contribution claim about reconstruction-aware network design.
2. Related work positions TRACE-SL against sensor location, graph sampling, Bayesian/A-optimal design, sparse reconstruction, and traffic imputation/forecasting.
3. Formulation, method, and theory sections accurately scope posterior trace identity, monotonicity, local optimality, and complexity.
4. Results, ablation, robustness, and external evidence sections use held-out Stage12 evidence and bounded wording.
5. Limitations and conclusion avoid global optimality, universal generalization, and guaranteed MAE improvement claims.

**Plans:** 1 plan

- [ ] 13-01-PLAN.md — Write all manuscript sections from `PAPER_PLAN.md`.

### Phase 14: CAS Compilation and Formatting

**Goal:** Author has a compiled CAS-template PDF with resolved figures, citations, references, and template-specific requirements.
**Depends on:** Phase 13
**Requirements:** TEX-02, TEX-04, COMP-01
**Success Criteria** (what must be TRUE):

1. `paper/main.tex` compiles to `paper/main.pdf`.
2. CAS class/style files, bibliography, macros, figure paths, and table inputs are organized under `paper/`.
3. No blocking undefined citations, undefined references, or missing figures remain after compilation.
4. Template-specific metadata and declarations are present or explicitly marked for human completion.

**Plans:** 1 plan

- [ ] 14-01-PLAN.md — Compile the CAS manuscript and fix LaTeX/template errors.

### Phase 15: Improvement Loop

**Goal:** Author has a reviewed and improved manuscript with preserved round0/round1/round2 PDFs and a clear improvement log.
**Depends on:** Phase 14
**Requirements:** COMP-02, COMP-03, COMP-04
**Success Criteria** (what must be TRUE):

1. `paper/main_round0_original.pdf`, `paper/main_round1.pdf`, and `paper/main_round2.pdf` exist.
2. The final PDF has no blocking main-body overfull boxes or unresolved formatting issues.
3. `PAPER_IMPROVEMENT_LOG.md` records review scores, major fixes, and remaining risks.
4. The manuscript has been recompiled after each improvement round.

**Plans:** 1 plan

- [ ] 15-01-PLAN.md — Run two improvement rounds and preserve comparison PDFs.

### Phase 16: Submission Assurance Audits

**Goal:** Author has submission-level audit artifacts and a verifier-green final pipeline report before any submission-ready claim.
**Depends on:** Phase 15
**Requirements:** AUDIT-01, AUDIT-02, AUDIT-03, AUDIT-04, AUDIT-05
**Success Criteria** (what must be TRUE):

1. `paper/PROOF_AUDIT.{md,json}` exists and has no unresolved blocking verdict.
2. `paper/PAPER_CLAIM_AUDIT.{md,json}` exists and paper-visible numbers are checked against result artifacts.
3. `paper/CITATION_AUDIT.{md,json}` exists and has no unresolved `REPLACE` or `REMOVE` verdicts.
4. `verify_paper_audits.sh` runs with `paper/ --assurance submission` and exits 0.
5. The final report says `Submission-ready: yes` only if the external verifier is green.

**Plans:** 1 plan

- [ ] 16-01-PLAN.md — Run mandatory submission audits and final verifier.

## Progress

**Execution Order:**
Phases execute in numeric order: 11 -> 12 -> 13 -> 14 -> 15 -> 16

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. Claim-Evidence Contract | v1.0 | 1/1 | Complete | 2026-05-21 |
| 2. Formulation and Theory Bridge | v1.0 | 2/2 | Complete | 2026-05-22 |
| 3. Baseline Portfolio | v1.0 | 1/1 | Complete | 2026-05-22 |
| 4. Core Experiment Evidence | v1.0 | 6/6 | Complete | 2026-05-22 |
| 5. Robustness and Generality | v1.0 | 4/4 | Complete | 2026-05-23 |
| 6. Reproducibility and Artifact Curation | v1.0 | 3/3 | Complete | 2026-05-23 |
| 7. Claim and Main Table Contract | v1.1 | 2/2 | Complete | 2026-05-23 |
| 8. External Stage12 Evidence | v1.1 | 5/5 | Complete | 2026-05-25 |
| 8.5. Stage12 Performance Unblock | v1.1 | 4/4 | Complete | 2026-05-25 |
| 9. Ablation and Evidence Classification | v1.1 | 3/3 | Complete | 2026-05-25 |
| 10. Theory and Handoff Package | v1.1 | 1/1 | Complete | 2026-05-25 |
| 11. TR Part B Paper Plan and CAS Scaffold | v1.2 | 0/1 | Pending | — |
| 12. Figures, Tables, and Method Illustration | v1.2 | 0/1 | Pending | — |
| 13. Manuscript Writing | v1.2 | 0/1 | Pending | — |
| 14. CAS Compilation and Formatting | v1.2 | 0/1 | Pending | — |
| 15. Improvement Loop | v1.2 | 0/1 | Pending | — |
| 16. Submission Assurance Audits | v1.2 | 0/1 | Pending | — |

## Coverage

| Requirement | Phase |
|-------------|-------|
| PLAN-01 | Phase 11 |
| PLAN-02 | Phase 11 |
| PLAN-03 | Phase 11 |
| PLAN-04 | Phase 11 |
| TEX-01 | Phase 11 |
| TEX-03 | Phase 11 |
| FIG-01 | Phase 12 |
| FIG-02 | Phase 12 |
| FIG-03 | Phase 12 |
| FIG-04 | Phase 12 |
| WRITE-01 | Phase 13 |
| WRITE-02 | Phase 13 |
| WRITE-03 | Phase 13 |
| WRITE-04 | Phase 13 |
| WRITE-05 | Phase 13 |
| TEX-02 | Phase 14 |
| TEX-04 | Phase 14 |
| COMP-01 | Phase 14 |
| COMP-02 | Phase 15 |
| COMP-03 | Phase 15 |
| COMP-04 | Phase 15 |
| AUDIT-01 | Phase 16 |
| AUDIT-02 | Phase 16 |
| AUDIT-03 | Phase 16 |
| AUDIT-04 | Phase 16 |
| AUDIT-05 | Phase 16 |

**Coverage:** 26/26 v1.2 requirements mapped exactly once.

## Archived Artifacts

- [v1.0 roadmap archive](milestones/v1.0-ROADMAP.md)
- [v1.0 requirements archive](milestones/v1.0-REQUIREMENTS.md)
- [v1.0 milestone audit](milestones/v1.0-MILESTONE-AUDIT.md)
- [v1.1 roadmap archive](milestones/v1.1-ROADMAP.md)
- [v1.1 requirements archive](milestones/v1.1-REQUIREMENTS.md)
- [v1.1 milestone audit](v1.1-MILESTONE-AUDIT.md)
