# Paper Improvement Log

## Round 0

Baseline CAS draft generated from `NARRATIVE_REPORT.md`, v1.1 paper-source artifacts, and local `els-cas-templates/`. The first successful compile produced an 8-page PDF.

## Round 1

Issue: the generated workflow figure existed but was not referenced in the manuscript body.

Fix: inserted Figure 1 into Section 3 so readers see the train/validation/test separation and TRACE-SL layout pipeline before the method details.

Output: `paper/main_round1.pdf`.

## Round 2

Issue: the discussion did not explicitly connect the manuscript source package to auditability and evidence routing.

Fix: added a paragraph explaining that paper-visible numbers come from machine-readable Stage12 artifacts and that claim, ablation, and external-evidence contracts localize future review questions.

Output: `paper/main_round2.pdf`.

## Residual Risks

- The draft is concise for a full TR Part B submission and should be expanded before actual submission.
- Proof, citation, and adversarial audits are local deterministic artifacts in this run; run fresh external reviews before submission.
