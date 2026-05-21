# Phase 1: Claim-Evidence Contract - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-21
**Phase:** 1-Claim-Evidence Contract
**Areas discussed:** Claim set and main framing, Evidence mapping standard, Low-budget caveat policy, Certificate terminology, Positioning boundaries

---

## Claim Set and Main Framing

| Option | Description | Selected |
|--------|-------------|----------|
| Preserve strong method claim | Frame TRACE-SL as transparent reconstruction-aware sensor placement and strengthen it with evidence. | ✓ |
| Narrow to empirical heuristic | Present TRACE-SL mainly as candidate-pool tuning with modest empirical gains. | |
| Delay claim decisions | Leave contribution wording to the final manuscript phase. | |

**User's choice:** Auto-selected recommended default based on PROJECT.md and REQUIREMENTS.md.
**Notes:** Existing project context explicitly says strong claims should be preserved and evidence-backed rather than weakened.

---

## Evidence Mapping Standard

| Option | Description | Selected |
|--------|-------------|----------|
| Explicit claim-evidence matrix | Map each primary claim to held-out experiments, statistics, robustness, theory, artifacts, or limitation wording. | ✓ |
| Narrative-only checklist | Capture claim status in prose without structured routing. | |
| Evidence later | Defer evidence mapping until experiments complete. | |

**User's choice:** Auto-selected recommended default.
**Notes:** This is the central deliverable for CLAIM-02 and prevents later phases from producing disconnected evidence.

---

## Low-Budget Caveat Policy

| Option | Description | Selected |
|--------|-------------|----------|
| Predeclare comparator or bounded caveat | Represent the 10% multistart issue directly and avoid post-hoc best-method selection. | ✓ |
| Ignore caveat | Focus only on aggregate wins. | |
| Weaken all performance claims | Avoid strong performance language across all budgets. | |

**User's choice:** Auto-selected recommended default.
**Notes:** PROJECT.md and REQUIREMENTS.md identify the low-budget multistart issue as a key reviewer-risk item.

---

## Certificate Terminology

| Option | Description | Selected |
|--------|-------------|----------|
| Certificate-guided language | Use certificate-guided/posterior-certificate-aware wording unless formal theorem is added. | ✓ |
| Certified method branding | Use formal certified language immediately. | |
| Remove certificate language | Avoid discussing posterior diagnostics as part of the method. | |

**User's choice:** Auto-selected recommended default.
**Notes:** Current evidence supports empirical certificate-error alignment, not theorem-level certification.

---

## Positioning Boundaries

| Option | Description | Selected |
|--------|-------------|----------|
| Separate from TSLP and black-box imputation | Emphasize reconstruction-aware sensor-layout design with transparent models. | ✓ |
| Position as general TSLP | Treat TRACE-SL as a variant of deterministic observability/coverage planning. | |
| Position as imputation model | Center the contribution on traffic prediction/imputation quality. | |

**User's choice:** Auto-selected recommended default.
**Notes:** This directly covers CLAIM-05 and supports Transportation Science framing.

---

## Claude's Discretion

- Exact matrix format may be chosen during planning, provided it includes claim ID, claim wording, evidence required, current evidence source, caveat/limitation wording, and downstream phase owner.

## Deferred Ideas

- New baseline implementation belongs to Phase 3.
- Core experiment audit/regeneration belongs to Phase 4.
- Robustness and generality experiments belong to Phase 5.
- Final manuscript writing belongs to Phase 7.
