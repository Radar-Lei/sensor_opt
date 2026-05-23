# Requirements: TRACE-SL Transportation Science Readiness

**Defined:** 2026/05/21
**Core Value:** Make strong, publishable claims about transparent reconstruction-aware traffic sensor placement, but only where the formulation, theory, baselines, robustness tests, and held-out evidence can support them.

## v1 Requirements

Requirements for turning the current TRACE-SL prototype into a Transportation Science-ready research package.

### Claim and Framing

- [ ] **CLAIM-01**: The paper states TRACE-SL as a transparent reconstruction-aware sensor placement problem, not as an ad hoc candidate-pool heuristic.
- [ ] **CLAIM-02**: Every primary contribution claim maps to explicit evidence: held-out experiment, robustness result, statistical comparison, theorem/derivation, or limitation note.
- [ ] **CLAIM-03**: The main performance claim avoids “best at all budgets” wording and correctly handles the 10% PeMS7_228 multistart-vs-RCSS caveat.
- [ ] **CLAIM-04**: The paper uses “certificate-guided” or equivalent wording unless a formal certificate theorem is added.
- [ ] **CLAIM-05**: The positioning distinguishes TRACE-SL from deterministic full-observability TSLP and from black-box traffic imputation/forecasting.

### Formulation and Theory

- [x] **THEORY-01**: The manuscript defines the sensor layout optimization problem with budgeted sensor set, hidden-node reconstruction, held-out loss, and transparent reconstruction model.
- [x] **THEORY-02**: The manuscript defines the tractable TRACE-SL/RCSS surrogate objective, including validation loss, posterior trace, scenario CVaR trace, condition number, and coverage terms.
- [x] **THEORY-03**: The manuscript provides a linear-Gaussian GLS/MAP posterior-error derivation connecting posterior covariance trace to expected hidden-state squared error.
- [x] **THEORY-04**: The manuscript states when posterior variance can motivate MAE-oriented sensor selection and where real traffic data depart from the idealized assumptions.
- [x] **THEORY-05**: The method section gives algorithmic complexity and local optimality conditions for fixed-candidate validation-aware swap refinement.
- [x] **THEORY-06**: TR Part B optional material identifies what additional monotonicity, submodularity-like, approximation, or stability analysis would be needed for a more mathematical submission.

### Baselines and Method Portfolio

- [ ] **BASE-01**: The experiment suite includes observability-inspired or TSLP-style baselines, with clear explanation that their objective differs from reconstruction-error minimization.
- [ ] **BASE-02**: A-optimal and D-optimal design baselines are reported as independent baselines, not only candidate sources inside RCSS.
- [ ] **BASE-03**: Graph sampling or graph signal reconstruction baselines are included or explicitly justified as already represented by existing GSP-related comparisons.
- [ ] **BASE-04**: QR/SVD/POD sparse sensor placement baseline is implemented and evaluated where compatible with the traffic matrix representation.
- [ ] **BASE-05**: A simple learning-based reconstruction check is run or scoped with a documented reason if deferred.
- [ ] **BASE-06**: Multistart validation refinement is treated as a strong comparator or predeclared portfolio member, not ignored after observing the 10% budget result.

### Experiment Evidence

- [x] **EXP-01**: PeMS7_228 10-split evidence is regenerated or audited for all core baselines and final method variants used in claims.
- [x] **EXP-02**: PeMS7_1026 external validation is extended to at least 10 splits or clearly framed as lower-power external evidence.
- [x] **EXP-03**: Seattle evidence is either curated into `trace_sl_results/` and synchronized with documentation, or removed from the core claim set.
- [x] **EXP-04**: All reported method comparisons include paired deltas, confidence intervals or bootstrap intervals, effect sizes, and paired significance tests where appropriate.
- [x] **EXP-05**: Certificate-error correlation results are reported with Spearman/Pearson-style summaries and interpreted as empirical validation unless formal theory is added.
- [x] **EXP-06**: Runtime and candidate-count sensitivity are reported for the main datasets and budget levels.

### Robustness and Generality

- [x] **ROBUST-01**: Sensor failure experiments evaluate random sensor drop rates such as 5%, 10%, and 20% after layout selection.
- [x] **ROBUST-02**: Observation noise experiments perturb observed sensor readings and report reconstruction degradation.
- [x] **ROBUST-03**: Missingness experiments simulate missing sensor readings or missing time blocks at validation/test time.
- [x] **ROBUST-04**: Nonuniform sensor cost experiments evaluate budgeted placement where sensors have heterogeneous costs or a documented proxy.
- [x] **ROBUST-05**: Temporal distribution shift experiments use time-blocked or month/week-style train-test splits when supported by dataset timestamps.
- [x] **ROBUST-06**: Candidate-count sensitivity experiments compare performance and runtime across candidate pool sizes such as 50, 100, 200, and 500.

### Reproducibility and Paper Artifacts

- [x] **REPRO-01**: Experiment scripts, configs, and summaries encode enough provenance to reproduce the paper tables, including seeds, budgets, candidate counts, and package versions where feasible.
- [x] **REPRO-02**: Raw traffic datasets remain ignored and are not committed; paper-visible artifacts use summaries, checksums, or non-sensitive metadata only.
- [x] **REPRO-03**: The repository documentation and paper narrative cite only curated, present, and reproducible result directories.
- [x] **REPRO-04**: Paper-ready tables and figures are generated from committed result artifacts rather than manually copied numbers.
- [ ] **REPRO-05**: Smoke tests or validation scripts check that key experiment commands still run and that aggregate summaries contain required layout/method rows.

### Manuscript Readiness

- [ ] **PAPER-01**: The manuscript has a Transportation Science-oriented introduction focused on planning/design value, transparent reconstruction, and sparse network monitoring.
- [ ] **PAPER-02**: The related work section positions TRACE-SL against traffic sensor location, observability, graph sampling, sparse reconstruction, experimental design, and traffic imputation.
- [ ] **PAPER-03**: The method section defines TRACE-SL/RCSS as a predeclared algorithmic portfolio with fixed selection rules before test evaluation.
- [ ] **PAPER-04**: The results section supports strong claims with the full claim-evidence matrix, including low-budget caveats.
- [ ] **PAPER-05**: The limitations section honestly states empirical-certificate assumptions, dataset scope, dense-solver scaling limits, and remaining TR Part B theory gaps.

## v2 Requirements

Deferred to a later milestone or a TR Part B-focused extension.

### Advanced Theory

- **V2-THEORY-01**: Prove stronger surrogate-error bounds beyond the linear-Gaussian posterior trace identity.
- **V2-THEORY-02**: Establish monotonicity, approximate submodularity, stability, or approximation-style guarantees for a restricted TRACE-SL objective.
- **V2-THEORY-03**: Develop a bilevel or stochastic programming formulation with a stronger optimization-theory contribution.

### Scaling and Engineering

- **V2-SCALE-01**: Replace dense posterior inversions with Cholesky/rank-update/sparse or low-rank solvers for larger transportation networks.
- **V2-SCALE-02**: Refactor the monolithic evaluator into importable modules with automated unit/regression tests.
- **V2-SCALE-03**: Add a larger non-PeMS network if data access and runtime allow.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Weakening the core claim into a purely incremental heuristic paper | User explicitly wants to preserve strong claims while adding evidence support |
| Post-hoc choosing the best method per budget without predeclared rule | Would invite cherry-picking criticism and undermine methodology credibility |
| Formal “certified” branding without theorem-level support | Current certificate evidence is empirical and model-based, not formal certification |
| Full TR Part B rewrite before Transportation Science readiness | TR Part B requires more mathematical analysis than the current immediate target |
| Committing raw datasets | Dataset files are local/ignored and may be large or license-constrained |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| CLAIM-01 | Phase 1 | Pending |
| CLAIM-02 | Phase 1 | Pending |
| CLAIM-03 | Phase 1 | Pending |
| CLAIM-04 | Phase 1 | Pending |
| CLAIM-05 | Phase 1 | Pending |
| THEORY-01 | Phase 2 | Complete |
| THEORY-02 | Phase 2 | Complete |
| THEORY-03 | Phase 2 | Complete |
| THEORY-04 | Phase 2 | Complete |
| THEORY-05 | Phase 2 | Complete |
| THEORY-06 | Phase 2 | Complete |
| BASE-01 | Phase 3 | Pending |
| BASE-02 | Phase 3 | Pending |
| BASE-03 | Phase 3 | Pending |
| BASE-04 | Phase 3 | Pending |
| BASE-05 | Phase 3 | Pending |
| BASE-06 | Phase 3 | Pending |
| EXP-01 | Phase 4 | Complete |
| EXP-02 | Phase 4 | Complete |
| EXP-03 | Phase 4 | Complete |
| EXP-04 | Phase 4 | Complete |
| EXP-05 | Phase 4 | Complete |
| EXP-06 | Phase 4 | Complete |
| ROBUST-01 | Phase 5 | Complete |
| ROBUST-02 | Phase 5 | Complete |
| ROBUST-03 | Phase 5 | Complete |
| ROBUST-04 | Phase 5 | Complete |
| ROBUST-05 | Phase 5 | Complete |
| ROBUST-06 | Phase 5 | Complete |
| REPRO-01 | Phase 6 | Complete |
| REPRO-02 | Phase 6 | Complete |
| REPRO-03 | Phase 6 | Complete |
| REPRO-04 | Phase 6 | Complete |
| REPRO-05 | Phase 6 | Pending |
| PAPER-01 | Phase 7 | Pending |
| PAPER-02 | Phase 7 | Pending |
| PAPER-03 | Phase 7 | Pending |
| PAPER-04 | Phase 7 | Pending |
| PAPER-05 | Phase 7 | Pending |

**Coverage:**
- v1 requirements: 39 total
- Mapped to phases: 39
- Unmapped: 0 ✓

---
*Requirements defined: 2026/05/21*
*Last updated: 2026/05/21 after initial definition*
