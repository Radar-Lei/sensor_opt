# Project Retrospective

*A living document updated after each milestone. Lessons feed forward into future planning.*

## Milestone: v1.0 — TRACE-SL Readiness

**Shipped:** 2026-05-23
**Phases:** 6 | **Plans:** 17 | **Sessions:** 1 milestone cycle

### What Was Built

- Claim-evidence contract, formal method framing, baseline portfolio, core evidence, robustness evidence, and reproducibility handoff for TRACE-SL.
- Curated manuscript-facing evidence artifacts under `TRC-23-02333/trace_sl_results/`, including reproducibility manifests and generated paper-source tables.
- Validator-backed closure for EXP, ROBUST, and REPRO requirements without committing raw traffic datasets.

### What Worked

- Keeping claims strong but evidence-bound gave the milestone a clear quality bar.
- Fail-closed validators made Phase 4–6 completion auditable instead of relying on narrative confidence.
- Generated paper-source tables reduced the risk of manual number drift in the manuscript.

### What Was Inefficient

- Requirement checkboxes drifted from phase verification state and had to be synchronized at milestone close.
- One summary extractor produced a review-finding line instead of a useful accomplishment, so milestone summaries should be curated before final archiving.
- The audit file name did not match the CLI's expected `v1.0-MILESTONE-AUDIT.md` pattern and required manual archival.

### Patterns Established

- Treat validation MAE as selection evidence and held-out aggregate rows as paper-visible performance evidence.
- Keep low-power or conditional datasets visible as bounded evidence rather than hiding caveats.
- Use deterministic manifest and source-table generation as the paper handoff boundary.

### Key Lessons

1. Milestone closure should re-check requirement status against verification reports before archival.
2. Paper-writing phases should consume curated `paper_sources/` artifacts, not raw experiment directories or manually copied values.
3. Dataset caveats should remain in claim routing and limitations until new evidence explicitly removes them.

### Cost Observations

- Model mix: not tracked in repository artifacts.
- Sessions: one GSD milestone cycle from 2026-05-21 to 2026-05-23.
- Notable: local reduced robustness/candidate runs were sufficient for bounded claims while preserving raw-data hygiene.

---

## Cross-Milestone Trends

### Process Evolution

| Milestone | Sessions | Phases | Key Change |
|-----------|----------|--------|------------|
| v1.0 | 1 cycle | 6 | Prototype evidence was converted into an auditable Transportation Science readiness package. |

### Cumulative Quality

| Milestone | Validators | Coverage | Zero-Dep Additions |
|-----------|------------|----------|-------------------|
| v1.0 | Phase 4, Phase 5, Phase 6 validators plus tests | 34/34 readiness requirements | Not tracked |

### Top Lessons (Verified Across Milestones)

1. Keep paper claims tied to generated, committed evidence artifacts.
2. Preserve caveats as explicit claim boundaries instead of resolving them through wording alone.
