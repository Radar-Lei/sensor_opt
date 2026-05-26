---
quick_id: 260526-r4c
slug: trace-sl-tr-b-theory-algorithm-details-e
status: complete
date: 2026-05-26
---

# TRACE-SL TR-B Paper Revision Summary

Completed a targeted `$paper-writing` revision of the existing TRACE-SL manuscript using the supplied TR-B review notes.

Changed:
- Reframed title and abstract around recoverability-driven sensor design.
- Expanded related work and bibliography from a short placeholder to 16 entries spanning transportation sensor location, sparse TSE, OED, graph sampling/POD, and forecasting.
- Added formal problem definition, Algorithm 1, Algorithm 2, four propositions with proofs, and a complexity/non-claim remark.
- Replaced the external TRACE-SL-only table with PeMS7_1026 and Seattle baseline comparison rows.
- Expanded experiment protocol, metrics, baselines, statistical testing, ablation interpretation, data availability, and reproducibility appendix.
- Regenerated local audit artifacts and compiled `paper/main.pdf`.

Verification:
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` succeeded from `paper/`.
- `paper/main.pdf` has 12 pages.
- ARIS audit verifier passed in draft mode.
- Remaining warning: one `cas-sc` front-matter overfull hbox at `\maketitle`; no unresolved citations or references.
