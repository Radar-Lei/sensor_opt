# Requirements: TRACE-SL Transportation Science Paper Foundation

**Defined:** 2026/05/23
**Core Value:** Make strong, publishable claims about transparent reconstruction-aware traffic sensor placement, but only where the formulation, theory, baselines, robustness tests, and held-out evidence can support them.

## v1.1 Requirements

Requirements for the TRACE-SL Transportation Science paper-foundation milestone. This milestone does not start manuscript prose.

### Claim Foundation

- [ ] **CLAIM-01**: Author can state the paper-level contribution as transparent reconstruction-aware sparse sensor layout design, not as a heuristic improvement story.
- [ ] **CLAIM-02**: Author can distinguish Transportation Science-ready claims from TR Part B-level claims that need stronger mathematical theory.
- [ ] **CLAIM-03**: Author has an explicit forbidden-wording list covering optimal, certified, globally robust, guaranteed MAE improvement, and generalizes across networks.
- [ ] **CLAIM-04**: Author can preserve the PeMS7_228 low-budget multistart caveat in all claim-facing artifacts.

### Main Evidence

- [ ] **EVID-01**: Author can use Stage12 PeMS7_228 baseline portfolio as the frozen main in-domain result table.
- [ ] **EVID-02**: Author has paired delta and p-value summaries for TRACE-SL against validation-selected random, random mean, top variance, greedy A-trace, graph sampling, observability, and QR/POD-style baselines where available.
- [ ] **EVID-03**: Author has completed PeMS7_1026 Stage12 10-split evidence using the same budgets and reviewer-facing baseline portfolio.
- [ ] **EVID-04**: Author has completed Seattle Stage12 10-split external/transfer-style evidence before Seattle appears in any core claim.
- [ ] **EVID-05**: Author can classify each dataset as core, external, supporting, conditional, or appendix-only based on evidence strength.

### Ablation Logic

- [ ] **ABLT-01**: Author can compare random mean, validation-selected random, certificate-only greedy, RCSS-selected, validation-swap-selected, and multistart validation-swap variants.
- [ ] **ABLT-02**: Author can answer whether certificate candidate pools improve over random candidate pools.
- [ ] **ABLT-03**: Author can answer whether validation selection and validation-aware swap each add measurable value.
- [ ] **ABLT-04**: Author can explain RCSS as certificate layer, validation layer, and local refinement layer rather than a kitchen-sink heuristic.

### Theory Foundation

- [ ] **THEORY-01**: Author has a clean budgeted hidden-network reconstruction formulation with train/validation/test separation.
- [ ] **THEORY-02**: Author has a posterior trace identity for the linear-Gaussian squared-error setting.
- [ ] **THEORY-03**: Author has a monotonicity proposition showing additional sensors do not increase posterior covariance or posterior trace under the stated Gaussian linear model.
- [ ] **THEORY-04**: Author has a validation-aware swap local-optimality statement over the one-swap neighborhood.
- [ ] **THEORY-05**: Author has a complexity statement for the RCSS candidate/search/evaluation process.

### Robustness and Handoff

- [ ] **HAND-01**: Author can keep robustness evidence as stress-test or appendix evidence unless multi-seed perturbation evidence is added.
- [ ] **HAND-02**: Author has paper-foundation artifacts that a later writing milestone can consume without generating manuscript prose now.
- [ ] **HAND-03**: Author has reproducibility-safe pointers from every paper-foundation claim/table to committed summaries, generated tables, scripts, or manifests without committing raw datasets.

## Future Requirements

Deferred to future writing or theory milestones.

### Manuscript Drafting

- **PAPER-01**: Author has a full Transportation Science introduction draft.
- **PAPER-02**: Author has a related work section positioning TRACE-SL against TSLP, graph sampling, Bayesian design, and traffic reconstruction.
- **PAPER-03**: Author has a method section written from the frozen claim/evidence/theory foundation.
- **PAPER-04**: Author has a results section written from frozen tables, ablations, and external evidence.
- **PAPER-05**: Author has limitations and discussion prose aligned with evidence boundaries.

### TR Part B Theory Extension

- **TRB-01**: Author has an approximate submodularity or weak-submodularity analysis where valid.
- **TRB-02**: Author has a covariance perturbation or stability bound.
- **TRB-03**: Author has a sample-splitting or validation-selection generalization argument.
- **TRB-04**: Author has a stochastic or bilevel optimization interpretation with suitable convergence or consistency discussion.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Manuscript prose drafting | v1.1 only prepares the foundation; prose belongs to the next writing milestone. |
| Optimal or certified optimal placement claims | Current theory supports certificate-guided design, not global optimality or formal certification. |
| Guaranteed MAE improvement claims | Held-out empirical gains are statistical evidence, not universal guarantees. |
| Globally robust claims | Current robustness is stress-test evidence unless multi-seed perturbation evidence is added. |
| Strong cross-network generalization claims | PeMS7_1026 and Seattle need Stage12 10-split evidence before stronger external claims. |
| Raw dataset commits | Raw traffic datasets are local/ignored inputs and must not be committed. |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| CLAIM-01 | TBD | Pending |
| CLAIM-02 | TBD | Pending |
| CLAIM-03 | TBD | Pending |
| CLAIM-04 | TBD | Pending |
| EVID-01 | TBD | Pending |
| EVID-02 | TBD | Pending |
| EVID-03 | TBD | Pending |
| EVID-04 | TBD | Pending |
| EVID-05 | TBD | Pending |
| ABLT-01 | TBD | Pending |
| ABLT-02 | TBD | Pending |
| ABLT-03 | TBD | Pending |
| ABLT-04 | TBD | Pending |
| THEORY-01 | TBD | Pending |
| THEORY-02 | TBD | Pending |
| THEORY-03 | TBD | Pending |
| THEORY-04 | TBD | Pending |
| THEORY-05 | TBD | Pending |
| HAND-01 | TBD | Pending |
| HAND-02 | TBD | Pending |
| HAND-03 | TBD | Pending |

**Coverage:**
- v1.1 requirements: 21 total
- Mapped to phases: 0
- Unmapped: 21 ⚠

---
*Requirements defined: 2026/05/23*
*Last updated: 2026/05/23 after v1.1 requirements definition*
