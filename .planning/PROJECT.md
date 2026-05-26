# TRACE-SL Transportation Research Part B Readiness

## Current State

TRACE-SL v1.0 shipped on 2026/05/23. The completed foundation milestones turn the prior experimental prototype into a Transportation Research Part B paper package for transparent reconstruction-aware sparse traffic sensor placement.

The repository now has:

- A claim-evidence contract constraining TRACE-SL claims to explicit theory, held-out evidence, robustness evidence, statistical comparisons, or limitations.
- A formal budgeted sensor-set formulation, RCSS surrogate, GLS/MAP posterior-error bridge, and validation-aware swap analysis.
- A reviewer-facing baseline portfolio covering observability/TSLP-style baselines, A/D-optimal design, graph/GSP connections, QR/SVD/POD sparse placement, learning-check framing, and multistart comparators.
- Curated PeMS7_228, PeMS7_1026, Seattle, candidate-count, runtime, and certificate-error evidence with paired statistics and bounded caveats.
- Robustness artifacts for sensor failure, observation noise, missingness, nonuniform costs, temporal shift, and candidate-count sensitivity.
- A reproducibility handoff with deterministic manifests, generated paper-source tables, launcher smoke checks, aggregate validators, and raw-data hygiene boundaries.

## Current Milestone: v1.2 TRACE-SL Transportation Research Part B Manuscript Drafting

**Goal:** Produce a complete English Transportation Research Part B manuscript package from the frozen v1.1 paper foundation using `els-cas-templates`, then bring it through submission-level proof, claim, citation, and audit-verifier gates.

**Target features:**
- Run `$paper-writing` from `NARRATIVE_REPORT.md` and the v1.1 handoff artifacts, with `assurance: submission`.
- Use local `els-cas-templates/` as the LaTeX template basis, targeting a TR Part B / Elsevier journal manuscript rather than Transportation Science.
- Generate a claim-evidence-aware `PAPER_PLAN.md` that routes every major contribution, theorem/proposition, table, and figure to v1.1 source artifacts.
- Generate publication figures and tables from `TRC-23-02333/trace_sl_results/paper_sources/` without committing raw traffic datasets.
- Write complete manuscript prose: abstract, introduction, related work, formulation, method, theory, experiments, robustness/ablation discussion, limitations, and conclusion.
- Compile `paper/main.pdf` under the CAS template and preserve round0/round1/round2 PDFs from the improvement loop.
- Run mandatory submission audits: proof-checker, paper-claim-audit, citation-audit, and `verify_paper_audits.sh`.
- Keep claim wording bounded: certificate-guided, posterior-certificate-aware, empirically supported in tested networks; no global optimality, universal generalization, or guaranteed MAE improvement.

**Explicit non-goal:** This milestone does not add new experiments unless the writing or audits uncover a blocking evidence gap. It does not change raw datasets, rerun Stage12 by default, or target Transportation Science formatting.

## Core Value

Make strong, publishable claims about transparent reconstruction-aware traffic sensor placement, but only where the formulation, theory, baselines, robustness tests, and held-out evidence can support them.

## Requirements

### Validated

- ✓ TRACE-SL has a runnable experiment pipeline for PeMS7_228, PeMS7_1026, and Seattle-style inputs — existing
- ✓ The repository evaluates transparent reconstruction methods including historical mean, neighbor average, GSP, and GLS/MAP — existing
- ✓ Stage 12 outputs show validation-swap RCSS improves over random, validation-selected random, and reviewer-facing baselines on PeMS7_228 while preserving the low-budget multistart caveat — v1.1
- ✓ PeMS7_228, PeMS7_1026, and Seattle have tracked 10-split Stage12 aggregate evidence — v1.1
- ✓ The method emits posterior trace, condition number, logdet, scenario CVaR trace, coverage, and validation diagnostics — existing
- ✓ TRACE-SL is framed as transparent reconstruction-aware sensor placement rather than an empirical candidate-pool heuristic — v1.0
- ✓ Primary claims are mapped to explicit evidence or bounded limitation wording — v1.0
- ✓ The 10% PeMS7_228 multistart caveat is preserved in the claim/evidence routing — v1.0
- ✓ The method uses certificate-guided wording unless formal certification is proved — v1.0
- ✓ TRACE-SL is positioned against deterministic full-observability TSLP and black-box traffic imputation/forecasting — v1.0
- ✓ The optimization objective, tractable surrogate, RCSS process, and validation-aware refinement are formalized — v1.0
- ✓ The GLS/MAP posterior covariance bridge to expected hidden-state squared error is documented — v1.0
- ✓ Reviewer-resistant baselines are implemented or bounded, including observability, A/D-optimal, graph/GSP, QR/SVD/POD, learning-check, and multistart comparisons — v1.0
- ✓ Core held-out evidence includes paired deltas, intervals, effect sizes, certificate-error correlations, runtime, and candidate-count sensitivity — v1.0
- ✓ Robustness evidence covers sensor failure, observation noise, missingness, heterogeneous costs, temporal shift, and candidate-pool size — v1.0
- ✓ Reproducibility artifacts trace paper-visible numbers to curated scripts, summaries, manifests, and generated tables without committing raw datasets — v1.0
- ✓ The full v1.1 paper foundation is frozen: claim/table contracts, Stage12 external evidence, ablation contracts, dataset classification, theory statements, and handoff manifest — v1.1

### Active

- [ ] Produce a complete TR Part B manuscript plan from `NARRATIVE_REPORT.md` and v1.1 paper-source artifacts.
- [ ] Generate data-driven figures and tables from committed paper-source CSV/JSON artifacts.
- [ ] Write an English CAS-template LaTeX manuscript for TR Part B.
- [ ] Compile `paper/main.pdf` and preserve all improvement-loop PDFs.
- [ ] Run two improvement rounds and update source until compilation and formatting checks pass.
- [ ] Pass submission-level proof, numeric-claim, citation, and external audit-verifier gates.

### Out of Scope

- Claiming TRACE-SL is best at every budget and against every strong baseline — current 10% PeMS7_228 evidence does not support that wording.
- Calling the method formally “certified” without a theorem or bound — current evidence supports certificate-guided or posterior-certificate-aware wording.
- Claiming optimal sensor placement, guaranteed MAE improvement, global robustness, or generalization across networks without the required evidence and theory.
- Treating validation MAE as final test evidence — final claims must use held-out test evaluation and paired comparisons.
- Re-targeting to Transportation Science formatting in this milestone — the user corrected the target to Transportation Research Part B.
- Running new Stage12 or robustness experiments by default — only do this if audits reveal a blocking evidence gap.
- Deleting or committing raw traffic datasets — datasets are local inputs and must remain protected unless explicitly approved.

## Next Milestone Goals

After v1.2, the next milestone should handle post-draft submission polishing: author metadata, cover letter, response to internal review, final Elsevier checklist, and any experiment/theory patch required by audit findings.

## Context

The research direction is strong because it connects sparse traffic sensor layout decisions directly to full-network reconstruction quality. The intended distinction from classical traffic sensor location problems is that TRACE-SL does not pursue deterministic full observability or minimum counting-point coverage; it optimizes partial-observation reconstruction quality, uncertainty, robustness, and validation performance under limited budgets.

Known evidence caveats for v1.2 writing:

- PeMS7_228 supports strong improvements against reviewer-facing baselines, while low-budget claims must preserve the multistart validation refinement caveat.
- PeMS7_1026 and Seattle have complete Stage12 10-split evidence and may support multi-network empirical discussion.
- Multi-network evidence must not be phrased as universal cross-network generalization.
- Robustness is bounded to the tested perturbations and reduced PeMS7_228 settings.
- Raw datasets remain local/ignored and must not be committed.

## Constraints

- **Target venue:** Transportation Research Part B is the primary submission target for v1.2.
- **Template:** Use the local `els-cas-templates/` CAS template files for the paper source.
- **Claim strategy:** Strong claims should be preserved and strengthened with evidence rather than narrowed prematurely.
- **Evidence standard:** Core claims must be supported by held-out test results, paired comparisons, statistical uncertainty, robustness checks, and reproducible artifacts.
- **External evidence:** PeMS7_1026 and Seattle have complete Stage12 10-split evidence; use them as external empirical evidence, not as universal generalization proof.
- **Execution concurrency:** Completed Stage12 external evidence closure used max jobs set to 1. Future reruns should preserve this constraint unless the compute environment changes.
- **Reproducibility:** Raw datasets stay local and ignored; curated result summaries, scripts, and non-sensitive artifacts should remain synchronized with paper claims.
- **Submission assurance:** `$paper-writing` must run with `assurance: submission`; final completion requires proof, claim, citation, and verifier artifacts.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Retarget v1.2 manuscript to Transportation Research Part B | User corrected the submission target before manuscript drafting; the existing theory and evidence foundation should now be written for TR Part B expectations | — Pending |
| Use `els-cas-templates` for manuscript source | TR Part B is an Elsevier journal and the user provided the local template directory | — Pending |
| Run `$paper-writing` with submission assurance | The requested deliverable is a submission-gated paper package, not only a draft PDF | — Pending |
| Target Transportation Science first | This was the previous v1.0/v1.1 planning assumption and is now superseded for v1.2 writing | ⚠ Revisit |
| Keep strong claims, but require evidence-backed wording | The research has real promise; the right response is to add evidence and sharpen claims, not dilute the contribution | ✓ Good |
| Frame v1.1 as paper foundation, not manuscript drafting | The claim, external evidence, ablation logic, and theory layer needed to be frozen before writing begins | ✓ Good |
| Require PeMS7_1026 Stage12 10-split evidence before stronger external PeMS claims | The earlier PeMS7_1026 evidence was promising but lower-power | ✓ Done |
| Require Seattle Stage12 10-split evidence before core-claim use | Seattle should not remain conditional if it is used as external/transfer-style evidence | ✓ Done |
| Limit remaining Stage12 closure execution to max_jobs=1 | User-confirmed compute constraint; parallel split/seed/dataset jobs risk overrunning the available environment | ✓ Done |
| Use “certificate-guided” unless formal certification is proved | Current posterior diagnostics correlate with MAE but are not formal certificates | ✓ Good |
| Treat multistart validation refinement as a serious comparator or portfolio member | At 10% budget it can outperform validation-swap RCSS, so ignoring it would invite reviewer criticism | ✓ Good |
| Use generated paper-source tables as the manuscript handoff | This keeps paper-visible numbers tied to committed aggregate evidence and provenance | ✓ Good |
| Use DRY_RUN launcher smoke checks for final reproducibility validation | Full experiment reruns are expensive; smoke checks validate command surfaces without raw-data exposure | ✓ Good |

## Archived Milestones

<details>
<summary>v1.1 TRACE-SL Transportation Science Paper Foundation — complete 2026/05/26</summary>

Archived files:

- `.planning/milestones/v1.1-ROADMAP.md`
- `.planning/milestones/v1.1-REQUIREMENTS.md`
- `.planning/v1.1-MILESTONE-AUDIT.md`

</details>

<details>
<summary>v1.0 TRACE-SL Readiness — shipped 2026/05/23</summary>

Archived files:

- `.planning/milestones/v1.0-ROADMAP.md`
- `.planning/milestones/v1.0-REQUIREMENTS.md`
- `.planning/milestones/v1.0-MILESTONE-AUDIT.md`

</details>

## Evolution

This document evolves at phase transitions and milestone boundaries.

---
*Last updated: 2026/05/26 after starting v1.2 TR Part B manuscript drafting*
