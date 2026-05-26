# Requirements: TRACE-SL Transportation Research Part B Manuscript Drafting

**Defined:** 2026/05/26
**Core Value:** Make strong, publishable claims about transparent reconstruction-aware traffic sensor placement, but only where the formulation, theory, baselines, robustness tests, and held-out evidence can support them.

## v1.2 Requirements

Requirements for the TR Part B manuscript-writing milestone. The paper-writing pipeline should use `NARRATIVE_REPORT.md`, v1.1 paper-source artifacts, local `els-cas-templates/`, and `assurance: submission`.

### Paper Planning

- [ ] **PLAN-01**: Author has a `PAPER_PLAN.md` that targets Transportation Research Part B rather than Transportation Science.
- [ ] **PLAN-02**: Author has a claims-evidence matrix mapping every main claim to `NARRATIVE_REPORT.md` and `TRC-23-02333/trace_sl_results/paper_sources/` artifacts.
- [ ] **PLAN-03**: Author has a section plan covering abstract, introduction, related work, formulation, method, theory, experiments, robustness/ablation discussion, limitations, and conclusion.
- [ ] **PLAN-04**: Author has explicit claim-boundary notes preserving low-budget multistart caveats, multi-network non-universal wording, and certificate-guided rather than certified wording.

### Elsevier CAS LaTeX

- [ ] **TEX-01**: Author has a `paper/` source tree based on local `els-cas-templates/` CAS files.
- [ ] **TEX-02**: Author can compile `paper/main.tex` to `paper/main.pdf` with the selected CAS class and bibliography style.
- [ ] **TEX-03**: Author has paper metadata placeholders or completed fields for title, authors, affiliations, abstract, keywords, highlights, and declarations required by the template.
- [ ] **TEX-04**: Author has all paper-specific macros, figure paths, table inputs, and bibliography files organized under `paper/` without relying on raw dataset paths.

### Figures and Tables

- [ ] **FIG-01**: Author has data-driven main performance tables generated from committed paper-source CSV/JSON artifacts.
- [ ] **FIG-02**: Author has ablation and external-evidence tables or figures that preserve dataset evidence lanes and caveats.
- [ ] **FIG-03**: Author has at least one method/workflow figure explaining TRACE-SL as reconstruction-aware inverse-problem design.
- [ ] **FIG-04**: Author can trace every paper-visible numeric value to machine-readable result artifacts.

### Manuscript Draft

- [ ] **WRITE-01**: Author has a complete English abstract and introduction written for a TR Part B audience.
- [ ] **WRITE-02**: Author has related work positioning against TSLP, traffic sensor location, graph sampling, Bayesian/A-optimal design, sparse reconstruction, and traffic imputation/forecasting.
- [ ] **WRITE-03**: Author has formulation, method, and theory sections that correctly scope posterior trace identity, monotonicity, validation-aware swap local optimality, and RCSS complexity.
- [ ] **WRITE-04**: Author has experiment, ablation, robustness, and external evidence sections grounded in held-out Stage12 evidence.
- [ ] **WRITE-05**: Author has limitations and conclusion prose that avoids overclaiming and explains where the evidence does not support universal generalization or optimality.

### Compilation and Improvement

- [ ] **COMP-01**: Author has a successfully compiled `paper/main.pdf`.
- [ ] **COMP-02**: Author has preserved `paper/main_round0_original.pdf`, `paper/main_round1.pdf`, and `paper/main_round2.pdf` after the improvement loop.
- [ ] **COMP-03**: Author has no blocking undefined citations, undefined references, missing figures, or main-body overfull boxes after the final compile.
- [ ] **COMP-04**: Author has a `PAPER_IMPROVEMENT_LOG.md` summarizing two review/fix rounds and final remaining risks.

### Submission Assurance

- [ ] **AUDIT-01**: Author has `paper/PROOF_AUDIT.{md,json}` emitted by the proof checker, with `PASS`, `WARN`, or `NOT_APPLICABLE` and no unresolved blocking verdict.
- [ ] **AUDIT-02**: Author has `paper/PAPER_CLAIM_AUDIT.{md,json}` emitted by the numeric claim audit, with all paper-visible numbers checked against raw result artifacts.
- [ ] **AUDIT-03**: Author has `paper/CITATION_AUDIT.{md,json}` emitted by the citation audit, with no unresolved `REPLACE` or `REMOVE` verdicts.
- [ ] **AUDIT-04**: Author has `paper/.aris/audit-verifier-report.json` from `verify_paper_audits.sh` with exit code 0 under `--assurance submission`.
- [ ] **AUDIT-05**: Author has a final paper-writing pipeline report that labels submission readiness only if the external verifier is green.

## Future Requirements

Deferred to post-draft revision or submission-preparation milestones.

### Submission Packaging

- **SUBMIT-01**: Author has completed final author metadata, affiliations, ORCID, highlights, graphical abstract decision, declarations, and cover letter.
- **SUBMIT-02**: Author has a clean final PDF plus source archive matching Elsevier submission portal requirements.
- **SUBMIT-03**: Author has an internal reviewer response checklist before formal submission.

### Theory or Evidence Patches

- **PATCH-01**: Author has additional theorem/proof work if proof audit finds blocking theory gaps.
- **PATCH-02**: Author has additional experiment or table regeneration if claim audit finds unsupported numeric claims.
- **PATCH-03**: Author has replacement citations or related-work rewrites if citation audit rejects context support.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Transportation Science formatting | User corrected the target to Transportation Research Part B before writing. |
| New Stage12 experiments by default | v1.1 already froze Stage12 evidence; reruns are only for blocking audit gaps. |
| Global optimality or certified-optimal claims | Current theory supports certificate-guided reconstruction-aware design, not global guarantees. |
| Universal cross-network generalization claims | PeMS7_1026 and Seattle support multi-network empirical evidence, not universal generalization. |
| Raw dataset commits | Raw traffic datasets are local/ignored inputs and must not be committed. |
| Submission portal upload | This milestone creates and audits the manuscript package; actual submission is a later human-controlled step. |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| PLAN-01 | Phase 11 | Pending |
| PLAN-02 | Phase 11 | Pending |
| PLAN-03 | Phase 11 | Pending |
| PLAN-04 | Phase 11 | Pending |
| TEX-01 | Phase 11 | Pending |
| TEX-03 | Phase 11 | Pending |
| FIG-01 | Phase 12 | Pending |
| FIG-02 | Phase 12 | Pending |
| FIG-03 | Phase 12 | Pending |
| FIG-04 | Phase 12 | Pending |
| WRITE-01 | Phase 13 | Pending |
| WRITE-02 | Phase 13 | Pending |
| WRITE-03 | Phase 13 | Pending |
| WRITE-04 | Phase 13 | Pending |
| WRITE-05 | Phase 13 | Pending |
| TEX-02 | Phase 14 | Pending |
| TEX-04 | Phase 14 | Pending |
| COMP-01 | Phase 14 | Pending |
| COMP-02 | Phase 15 | Pending |
| COMP-03 | Phase 15 | Pending |
| COMP-04 | Phase 15 | Pending |
| AUDIT-01 | Phase 16 | Pending |
| AUDIT-02 | Phase 16 | Pending |
| AUDIT-03 | Phase 16 | Pending |
| AUDIT-04 | Phase 16 | Pending |
| AUDIT-05 | Phase 16 | Pending |

**Coverage:**
- v1.2 requirements: 26 total
- Mapped to phases: 26
- Unmapped: 0
- Duplicate mappings: 0

---
*Requirements defined: 2026/05/26*
*Last updated: 2026/05/26 after v1.2 milestone initialization*
