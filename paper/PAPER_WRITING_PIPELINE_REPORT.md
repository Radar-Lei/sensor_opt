# Paper Writing Pipeline Report

**Input**: `NARRATIVE_REPORT.md` plus user-supplied TR-B review notes
**Venue**: Transportation Research Part B: Methodological
**Assurance**: draft
**Submission-ready**: no
**Date**: 2026-05-26

## Pipeline Summary

| Phase | Status | Output |
|-------|--------|--------|
| 0. Assurance Setup | Complete | `paper/.aris/assurance.txt = draft` |
| 1. Paper Plan | Reused | `PAPER_PLAN.md` plus targeted TR-B revision scope |
| 2. Figures | Reused | Existing workflow and MAE figures retained |
| 3. LaTeX Writing | Complete | Theory, algorithms, related work, experiments, tables, appendix revised |
| 4. Compilation | Complete | `paper/main.pdf` (12 pages) |
| 4.5 Proof Audit | WARN | `paper/PROOF_AUDIT.{md,json}`; formal environments detected, local audit only |
| 5.5 Paper Claim Audit | PASS | `paper/PAPER_CLAIM_AUDIT.{md,json}` |
| 5.8 Citation Audit | WARN | `paper/CITATION_AUDIT.{md,json}`; metadata locally checked, fresh web audit still needed |
| 6.0 Assurance Verifier | OK in draft mode | `paper/.aris/audit-verifier-report.json` |

## Key Revisions

| Area | Change |
|------|--------|
| Title/abstract | Reframed the paper around recoverability-driven sensor design and made low-budget caveats visible. |
| Theory | Added a formal design definition, two algorithm tables, four propositions with proofs, and a complexity/non-claim remark. |
| External evidence | Replaced TRACE-SL-only external table with PeMS7_1026/Seattle baseline comparison rows and boundary notes. |
| Experiments | Expanded dataset, split, metric, baseline, and statistical-testing protocol prose. |
| Related work | Expanded transportation sensor location, sparse TSE, OED, graph sampling/POD, and forecasting positioning; bibliography now has 16 entries. |
| Reproducibility | Strengthened data/code availability and appendix evidence-contract routing. |

## Verification

- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` succeeded.
- `paper/main.pdf` is 12 pages.
- Draft audit verifier passed with `paper-claim-audit=PASS`, `proof-checker=WARN`, `citation-audit=WARN`, and `kill-argument=WARN`.
- Remaining LaTeX issue: one `cas-sc` front-matter overfull hbox at `\maketitle`; no undefined references or citations remain.

## Remaining Issues

- Run fresh external proof and citation audits before real TR-B submission.
- Visually inspect `paper/main.pdf` for float placement, front-matter spacing, and table readability.
- Fill author metadata, affiliations, declarations, and portal-specific files before submission.
