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

- [ ] **THEORY-01**: The manuscript defines the sensor layout optimization problem with budgeted sensor set, hidden-node reconstruction, held-out loss, and transparent reconstruction model.
- [ ] **THEORY-02**: The manuscript defines the tractable TRACE-SL/RCSS surrogate objective, including validation loss, posterior trace, scenario CVaR trace, condition number, and coverage terms.
- [ ] **THEORY-03**: The manuscript provides a linear-Gaussian GLS/MAP posterior-error derivation connecting posterior covariance trace to expected hidden-state squared error.
- [ ] **THEORY-04**: The manuscript states when posterior variance can motivate MAE-oriented sensor selection and where real traffic data depart from the idealized assumptions.
- [ ] **THEORY-05**: The method section gives algorithmic complexity and local optimality conditions for fixed-candidate validation-aware swap refinement.
- [ ] **THEORY-06**: TR Part B optional material identifies what additional monotonicity, submodularity-like, approximation, or stability analysis would be needed for a more mathematical submission.

### Baselines and Method Portfolio

- [ ] **BASE-01**: The experiment suite includes observability-inspired or TSLP-style baselines, with clear explanation that their objective differs from reconstruction-error minimization.
- [ ] **BASE-02**: A-optimal and D-optimal design baselines are reported as independent baselines, not only candidate sources inside RCSS.
- [ ] **BASE-03**: Graph sampling or graph signal reconstruction baselines are included or explicitly justified as already represented by existing GSP-related comparisons.
- [ ] **BASE-04**: QR/SVD/POD sparse sensor placement baseline is implemented and evaluated where compatible with the traffic matrix representation.
- [ ] **BASE-05**: A simple learning-based reconstruction check is run or scoped with a documented reason if deferred.
- [ ] **BASE-06**: Multistart validation refinement is treated as a strong comparator or predeclared portfolio member, not ignored after observing the 10% budget result.

### Experiment Evidence

- [ ] **EXP-01**: PeMS7_228 10-split evidence is regenerated or audited for all core baselines and final method variants used in claims.
- [ ] **EXP-02**: PeMS7_1026 external validation is extended to at least 10 splits or clearly framed as lower-power external evidence.
- [ ] **EXP-03**: Seattle evidence is either curated into `trace_sl_results/` and synchronized with documentation, or removed from the core claim set.
- [ ] **EXP-04**: All reported method comparisons include paired deltas, confidence intervals or bootstrap intervals, effect sizes, and paired significance tests where appropriate.
- [ ] **EXP-05**: Certificate-error correlation results are reported with Spearman/Pearson-style summaries and interpreted as empirical validation unless formal theory is added.
- [ ] **EXP-06**: Runtime and candidate-count sensitivity are reported for the main datasets and budget levels.

### Robustness and Generality

- [ ] **ROBUST-01**: Sensor failure experiments evaluate random sensor drop rates such as 5%, 10%, and 20% after layout selection.
- [ ] **ROBUST-02**: Observation noise experiments perturb observed sensor readings and report reconstruction degradation.
- [ ] **ROBUST-03**: Missingness experiments simulate missing sensor readings or missing time blocks at validation/test time.
- [ ] **ROBUST-04**: Nonuniform sensor cost experiments evaluate budgeted placement where sensors have heterogeneous costs or a documented proxy.
- [ ] **ROBUST-05**: Temporal distribution shift experiments use time-blocked or month/week-style train-test splits when supported by dataset timestamps.
- [ ] **ROBUST-06**: Candidate-count sensitivity experiments compare performance and runtime across candidate pool sizes such as 50, 100, 200, and 500.

### Reproducibility and Paper Artifacts

- [ ] **REPRO-01**: Experiment scripts, configs, and summaries encode enough provenance to reproduce the paper tables, including seeds, budgets, candidate counts, and package versions where feasible.
- [ ] **REPRO-02**: Raw traffic datasets remain ignored and are not committed; paper-visible artifacts use summaries, checksums, or non-sensitive metadata only.
- [ ] **REPRO-03**: The repository documentation and paper narrative cite only curated, present, and reproducible result directories.
- [ ] **REPRO-04**: Paper-ready tables and figures are generated from committed result artifacts rather than manually copied numbers.
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
| CLAIM-01 | TBD | Pending |
| CLAIM-02 | TBD | Pending |
| CLAIM-03 | TBD | Pending |
| CLAIM-04 | TBD | Pending |
| CLAIM-05 | TBD | Pending |
| THEORY-01 | TBD | Pending |
| THEORY-02 | TBD | Pending |
| THEORY-03 | TBD | Pending |
| THEORY-04 | TBD | Pending |
| THEORY-05 | TBD | Pending |
| THEORY-06 | TBD | Pending |
| BASE-01 | TBD | Pending |
| BASE-02 | TBD | Pending |
| BASE-03 | TBD | Pending |
| BASE-04 | TBD | Pending |
| BASE-05 | TBD | Pending |
| BASE-06 | TBD | Pending |
| EXP-01 | TBD | Pending |
| EXP-02 | TBD | Pending |
| EXP-03 | TBD | Pending |
| EXP-04 | TBD | Pending |
| EXP-05 | TBD | Pending |
| EXP-06 | TBD | Pending |
| ROBUST-01 | TBD | Pending |
| ROBUST-02 | TBD | Pending |
| ROBUST-03 | TBD | Pending |
| ROBUST-04 | TBD | Pending |
| ROBUST-05 | TBD | Pending |
| ROBUST-06 | TBD | Pending |
| REPRO-01 | TBD | Pending |
| REPRO-02 | TBD | Pending |
| REPRO-03 | TBD | Pending |
| REPRO-04 | TBD | Pending |
| REPRO-05 | TBD | Pending |
| PAPER-01 | TBD | Pending |
| PAPER-02 | TBD | Pending |
| PAPER-03 | TBD | Pending |
| PAPER-04 | TBD | Pending |
| PAPER-05 | TBD | Pending |

**Coverage:**
- v1 requirements: 39 total
- Mapped to phases: 0
- Unmapped: 39 ⚠️

---
*Requirements defined: 2026/05/21*
*Last updated: 2026/05/21 after initial definition*
