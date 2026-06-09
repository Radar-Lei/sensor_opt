# SPEC

## Goal

Prepare a goal-ready contract for the TRACE-BiOpt Transportation Research Part B submission cleanup. The executable work should make the manuscript and repository contracts read as a confident, bounded methodological contribution while preserving the current evidence chain and leaving Figure 1 unchanged.

## Scope

This is a P0 manuscript and contract synchronization task with a full current-best refresh used as final verification.

The goal covers:

- Synchronizing `TRACE_BIOPT_SPEC.md` and `TRACE_BIOPT_THEORY.md` with the implemented normalized full-state posterior trace certificate.
- Reframing Section 4 from defensive "scoped/narrow" language to positive theoretical properties.
- Reframing the main theory table as formal properties with assumptions and interpretation.
- Enforcing the empirical claim wording around 21 pre-registered non-BiOpt baselines in the tested dataset-budget regimes.
- Fixing Figure 4 spacing if needed without changing the scientific content.
- Running the full current-best paper refresh as final verification and accepting only directly relevant generated changes.

## Non-Goals

- Do not modify Figure 1 or its image file.
- Do not add any manuscript statement that Figure 1 is AI-generated.
- Do not rerun large Stage15/Stage16 experiments; the refresh script may regenerate artifacts from existing results only.
- Do not add a global optimality, approximation, universal robustness, or untested baseline-dominance theorem.
- Do not broaden claims beyond tested networks, budgets, seeds, estimator protocol, and the pre-registered comparison class.
- Do not refactor unrelated research code.

## Key Files

- `TRACE_BIOPT_SPEC.md`
- `TRACE_BIOPT_THEORY.md`
- `paper/sections/4_method_theory.tex`
- `paper/sections/3_problem.tex`
- `paper/sections/5_experiments.tex`
- `paper/sections/7_discussion.tex`
- `paper/sections/A_appendix.tex`
- `paper/tables/table_theory.tex`
- `figures/table_theory.tex`
- `figures/latex_includes.tex`
- `paper/main.tex`
- `SUBMISSION_EVIDENCE_INDEX.md`
- `scripts/refresh_current_best_trace_biopt_paper_chain.sh`

Discovery commands:

```bash
rg -n "scoped theory|Scoped theoretical|narrow claim|Non-claim boundary|all baselines|beats all|globally optimal|posterior_trace|hidden uncertainty|hidden-node risk|Bayes-risk|full-state" TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md paper figures -S
rg -n "fig1|Figure 1|fig1_trace_biopt_framework_v2" paper figures -S
```

## Required Framing

Use the following canonical posterior-certificate wording in contract/theory language:

> The implemented posterior certificate is the normalized full-state posterior trace, `|V|^{-1} tr(Sigma_post(S))`. Under the linear-Gaussian squared-error model, the full trace equals full-state Bayes squared reconstruction risk; the hidden-block identity follows by projection and is reported as a variant, not the audited objective.

Use the following canonical empirical claim shape:

> TRACE-BiOpt achieves the lowest mean held-out GLS/MAP MAE against 21 pre-registered non-BiOpt baselines across the tested dataset-budget regimes, and no pre-registered challenger remains tied or better after Holm-corrected paired tests.

## Scorecard

Primary checklist score: 7 required checks, pass threshold 7/7.

1. Contract synchronization: `TRACE_BIOPT_SPEC.md` and `TRACE_BIOPT_THEORY.md` describe normalized full-state posterior trace as the implemented certificate and hidden-block posterior trace only as a projected variant.
2. Section 4 tone: no defensive title or opening sentence using "scoped theory" or "narrow claim"; the section presents theoretical properties positively.
3. Theory table tone: main theory tables use a title like "Formal properties of TRACE-BiOpt" and columns like `Property`, `Guarantee`, and `Assumptions and interpretation`.
4. Claim wording: no unsupported naked "beats all baselines", "all baselines" as a standalone dominance claim, or "globally optimal" claim remains in main manuscript text outside explicit non-claim/limitation context.
5. Figure 1 protection: no tracked Figure 1 file or Figure 1 manuscript reference is changed except incidental build artifacts that do not alter the figure content or caption.
6. Fast checks: targeted `rg` checks and `python TRC-23-02333/test_transparent_estimator_eval.py` pass.
7. Final refresh: `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh` completes, or any failure is diagnosed and recorded with enough detail to decide whether it is environmental or manuscript-caused.

Regression checks:

- `git diff --name-only` must not include Figure 1 image assets.
- Changes to generated evidence/table artifacts must be traceable to the refresh script or manuscript wording changes.
- No claim wording should imply global optimality, untested baseline dominance, or universal cross-network generalization.

Stop condition: all 7 scorecard items pass, or the only failing item is a documented environmental failure in final refresh that is unrelated to the manuscript/contract changes.

## Feedback Loop

Fast check after each edit cluster, expected runtime under 1 minute:

```bash
rg -n "scoped theory|Scoped theoretical|narrow claim|Non-claim boundary|beats all baselines|globally optimal" TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md paper figures -S
rg -n "posterior_trace\\(S\\).*hidden|hidden uncertainty certificate|hidden-node risk identity|Bayes-risk certificate" TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md -S
git diff --name-only | rg "fig1|Figure1|trace_biopt_framework|\\.jpg$|\\.png$" || true
python TRC-23-02333/test_transparent_estimator_eval.py
```

Proxy validity: these checks directly target the requested wording, contract alignment, Figure 1 protection, and no-dataset test suite.

Final check, expected to be slower:

```bash
bash scripts/refresh_current_best_trace_biopt_paper_chain.sh
```

If the refresh produces broad generated artifact churn, inspect it before accepting it. Keep directly relevant generated table/figure/audit updates; do not widen into unrelated evidence work.

## Working Memory

Use `.planning/goals/trace-biopt-trb-p0/` for long-run state:

- `PLAN.md`: current phase checklist and active strategy.
- `ATTEMPTS.md`: commands run, results, failures, and next adjustment.
- `NOTES.md`: durable discoveries, especially wording decisions and refresh outcomes.
- `CONTROL.md`: compact control surface with protected files and resource gates.

Update `PLAN.md` at phase changes, `ATTEMPTS.md` after each edit/check cycle, and `NOTES.md` whenever a durable issue or decision is discovered.

## Human Control

The initial human control settings are:

- Primary priority: submission-quality wording and contract consistency.
- Secondary priority: preserve current evidence chain and avoid unnecessary artifact churn.
- Protected: Figure 1 image assets and Figure 1 manuscript/caption content.
- Expensive step allowed: full current-best refresh script.
- Require explicit approval for: changing Figure 1, adding new experiments, changing dependencies, claiming global optimality or approximation guarantees, or editing unrelated model/training code.

## Verification

Run, in order:

```bash
git status --short
rg -n "scoped theory|Scoped theoretical|narrow claim|Non-claim boundary|beats all baselines|globally optimal" TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md paper figures -S
rg -n "posterior_trace\\(S\\).*hidden|hidden uncertainty certificate|hidden-node risk identity|Bayes-risk certificate" TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md -S
python TRC-23-02333/test_transparent_estimator_eval.py
bash scripts/refresh_current_best_trace_biopt_paper_chain.sh
git diff --name-only
```

If a check fails, fix the cause when in scope. If out of scope or environmental, record it in `ATTEMPTS.md` and the final response.

## Acceptance Criteria

The user has approved:

- P0 manuscript and contract synchronization is the target.
- Full current-best refresh may run as final verification.
- Figure 1 remains unchanged and the manuscript should not discuss it as AI-generated.

This spec is ready to compile into `GOAL.md`.
