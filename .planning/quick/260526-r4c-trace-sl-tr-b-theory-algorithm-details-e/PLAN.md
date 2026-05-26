---
quick_id: 260526-r4c
slug: trace-sl-tr-b-theory-algorithm-details-e
status: in_progress
date: 2026-05-26
---

# TRACE-SL TR-B Paper Revision Plan

Task: revise the existing TRACE-SL paper draft using the reviewer-style feedback supplied by the user, focusing on TR-B methodological thickness rather than new experiments.

Scope:
- Strengthen title, abstract, introduction, conclusion, and claim boundaries.
- Expand related work from a short placeholder into transportation sensor placement, sparse traffic state estimation, OED, graph sampling, and traffic forecasting positioning.
- Replace theory sketch prose with formal definitions, algorithms, propositions, and proof sketches while preserving scoped non-claims.
- Rework the external evidence table so PeMS7_1026 and Seattle include baseline context and caveats.
- Expand experimental protocol, statistical testing, baseline definitions, data/code availability, and reproducibility notes.
- Compile the LaTeX PDF and update local pipeline summary artifacts.

Verification:
- Run LaTeX compilation from `paper/`.
- Run local paper-source/audit artifact generation if the edited source changes hashes.
- Check Git status and report files changed.
