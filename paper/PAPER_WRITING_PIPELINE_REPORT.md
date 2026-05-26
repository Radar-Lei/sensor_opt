# Paper Writing Pipeline Report

**Input**: `NARRATIVE_REPORT.md`
**Venue**: Transportation Research Part B: Methodological
**Assurance**: submission
**Submission-ready**: yes by verifier exit code; see warning below
**Date**: 2026-05-26

## Pipeline Summary

| Phase | Status | Output |
|-------|--------|--------|
| 0. Assurance Setup | Complete | `paper/.aris/assurance.txt = submission` |
| 1. Paper Plan | Complete | `PAPER_PLAN.md` |
| 2. Figures | Complete | `figures/`, `paper/figures/`, `paper/tables/` |
| 3. LaTeX Writing | Complete | `paper/main.tex`, `paper/sections/*.tex`, `paper/references.bib` |
| 4. Compilation | Complete | `paper/main.pdf` (8 pages) |
| 5. Improvement | Complete | `main_round0_original.pdf`, `main_round1.pdf`, `main_round2.pdf` |
| 4.5 Proof Audit | WARN | `paper/PROOF_AUDIT.{md,json}` |
| 5.5 Paper Claim Audit | PASS | `paper/PAPER_CLAIM_AUDIT.{md,json}` |
| 5.8 Citation Audit | WARN | `paper/CITATION_AUDIT.{md,json}` |
| 6.0 Assurance Verifier | OK, exit 0 | `paper/.aris/audit-verifier-report.json` |

## Improvement Scores

| Round | Score | Key Changes |
|-------|-------|-------------|
| Round 0 | 5/10 | CAS draft compiled from v1.1 evidence foundation |
| Round 1 | 6/10 | Inserted TRACE-SL workflow figure into the problem section |
| Round 2 | 6.5/10 | Strengthened discussion of auditability and evidence routing |

## Deliverables

- `paper/main.pdf` -- final compiled draft
- `paper/main_round0_original.pdf` -- before improvement
- `paper/main_round1.pdf` -- after round 1
- `paper/main_round2.pdf` -- after round 2
- `paper/PAPER_IMPROVEMENT_LOG.md` -- review and edit log
- `paper/PROOF_AUDIT.{md,json}` -- proof-obligation warning audit
- `paper/PAPER_CLAIM_AUDIT.{md,json}` -- numerical claim audit
- `paper/CITATION_AUDIT.{md,json}` -- citation audit warning ledger
- `paper/KILL_ARGUMENT.{md,json}` -- verifier-required adversarial audit
- `paper/.aris/audit-verifier-report.json` -- external verifier report

## Warning

The ARIS verifier is green, but proof/citation/kill-argument audits were emitted as deterministic local audits because this Codex runtime did not spawn fresh reviewer agents. Treat the current PDF as a verifier-green manuscript draft, not as a final human-submission package.

## Next Steps

- [ ] Visually inspect `paper/main.pdf`.
- [ ] Run fresh external proof, citation, and adversarial reviews before real submission.
- [ ] Fill author metadata, affiliations, declarations, and any TR Part B portal-specific files.
