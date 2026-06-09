<goal>
Bring the TRACE-BiOpt TR-B submission into P0-ready manuscript and repository-contract alignment: make the method/theory framing confident rather than defensive, synchronize posterior-trace contract language with the implemented normalized full-state objective, preserve the current evidence chain, leave Figure 1 unchanged, and verify the result with the full current-best refresh pipeline.
</goal>

<context>
Read these files first:

- `SPEC.md`
- `TRACE_BIOPT_SPEC.md`
- `TRACE_BIOPT_THEORY.md`
- `paper/sections/3_problem.tex`
- `paper/sections/4_method_theory.tex`
- `paper/sections/5_experiments.tex`
- `paper/sections/7_discussion.tex`
- `paper/sections/A_appendix.tex`
- `paper/tables/table_theory.tex`
- `figures/table_theory.tex`
- `SUBMISSION_EVIDENCE_INDEX.md`
- `README.md`

Use these discovery commands before editing:

```bash
git status --short
rg -n "scoped theory|Scoped theoretical|narrow claim|Non-claim boundary|all baselines|beats all|globally optimal|posterior_trace|hidden uncertainty|hidden-node risk|Bayes-risk|full-state" TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md paper figures -S
rg -n "fig1|Figure 1|fig1_trace_biopt_framework_v2|trace_biopt_framework" paper figures -S
```

The current implementation and audited evidence use the normalized full-state posterior trace. Hidden-block posterior trace is only a projected variant, not the audited objective.
</context>

<constraints>
Do not modify Figure 1, its image asset, or its manuscript/caption content.

Do not add any manuscript statement that Figure 1 is AI-generated.

Do not run new large experiments. It is allowed to run `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh` because it regenerates the current-best paper chain from existing Stage15/Stage16 artifacts.

Do not claim global optimality, global approximation guarantees, universal cross-network generalization, universal MAE improvement, untested baseline dominance, or robustness outside the stated perturbation screens.

Do not turn the method back into a candidate-pool selector narrative. TRACE-BiOpt should remain one recoverability-driven bilevel network-design method with an external pre-registered non-BiOpt comparison class.

Do not widen scope into dependency management, estimator rewrites, experiment reruns, or unrelated model/training code.

Generated table/figure/audit changes from the refresh script may be kept only when they are directly relevant to the edited manuscript/contract or are normal deterministic refresh outputs. Inspect broad artifact churn before accepting it.
</constraints>

<scorecard>
Primary score: a 7-item checklist. Passing threshold: 7/7, unless the only failure is a documented environmental failure in the final refresh that is unrelated to the manuscript/contract edits.

1. Contract synchronization passes: `TRACE_BIOPT_SPEC.md` and `TRACE_BIOPT_THEORY.md` describe the implemented posterior certificate as `|V|^{-1} tr(Sigma_post(S))`; hidden-block posterior trace is a projected variant, not the audited objective.
2. Section 4 tone passes: `paper/sections/4_method_theory.tex` no longer uses a defensive title or opening such as "scoped theory" or "The narrow claim"; it presents theoretical properties positively.
3. Theory table tone passes: `paper/tables/table_theory.tex` and `figures/table_theory.tex` use a positive title such as "Formal properties of TRACE-BiOpt" and columns like `Property`, `Guarantee`, and `Assumptions and interpretation`.
4. Claim wording passes: unsupported naked "beats all baselines", "all baselines" dominance phrasing, and "globally optimal" claims do not appear in main manuscript text outside explicit non-claim/limitation context. The canonical claim shape is "against 21 pre-registered non-BiOpt baselines across the tested dataset-budget regimes".
5. Figure 1 protection passes: `git diff --name-only` does not include Figure 1 image assets, and Figure 1 content/caption references are not substantively changed.
6. Fast checks pass: targeted `rg` checks and `python TRC-23-02333/test_transparent_estimator_eval.py` pass.
7. Final refresh passes: `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh` completes, or a failure is diagnosed and recorded as environmental rather than caused by the edits.

Regression checks:

- Inspect `git diff --name-only` before finalizing.
- Inspect any generated table/figure/audit changes from the refresh script.
- Re-run targeted wording `rg` checks after generated table refresh, because generated tables may reintroduce old captions/columns.

Stop condition: the scorecard reaches passing threshold and final artifacts are summarized in the final response.
</scorecard>

<done_when>
The goal is complete when all of the following are true:

- `TRACE_BIOPT_SPEC.md` contains full-state normalized posterior trace contract wording and no longer defines `posterior_trace(S)` as an average hidden uncertainty certificate.
- `TRACE_BIOPT_THEORY.md` states that full-state posterior trace equals full-state Bayes squared reconstruction risk under the linear-Gaussian squared-error model, and treats hidden-block risk as a projection/variant rather than the audited objective.
- `paper/sections/4_method_theory.tex` has title `TRACE-BiOpt method and theoretical properties` or an equivalent positive title, and no opening "narrow claim" sentence.
- `paper/tables/table_theory.tex` and `figures/table_theory.tex` have positive formal-properties framing and no `Non-claim boundary` column in the main theory summary.
- Targeted `rg` checks show no remaining defensive/unsupported wording in the in-scope files, except accepted limitation/non-claim contexts.
- `python TRC-23-02333/test_transparent_estimator_eval.py` passes.
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh` is run as final verification, with outcome recorded in `.planning/goals/trace-biopt-trb-p0/ATTEMPTS.md`.
- `git diff --name-only` confirms Figure 1 image assets were not modified.
</done_when>

<feedback_loop>
Fast representative check, expected runtime under 1 minute, run after each edit cluster:

```bash
rg -n "scoped theory|Scoped theoretical|narrow claim|Non-claim boundary|beats all baselines|globally optimal" TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md paper figures -S
rg -n "posterior_trace\\(S\\).*hidden|hidden uncertainty certificate|hidden-node risk identity|Bayes-risk certificate" TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md -S
git diff --name-only | rg "fig1|Figure1|trace_biopt_framework|\\.jpg$|\\.png$" || true
python TRC-23-02333/test_transparent_estimator_eval.py
```

Why this proxy is representative: it directly checks the requested language changes, the posterior-certificate contract, Figure 1 protection, and the repo's no-dataset unit test path.

Slower final check:

```bash
bash scripts/refresh_current_best_trace_biopt_paper_chain.sh
```

Run the slower check after the text/contract changes are stable. If it regenerates tables that reintroduce old phrasing, patch the source generator or generated table as appropriate, then rerun targeted checks.
</feedback_loop>

<workflow>
1. Initialize working memory in `.planning/goals/trace-biopt-trb-p0/` and record the approved scope: P0 sync, full refresh as final verification, Figure 1 unchanged.
2. Inspect git status and read the context files. Use parallel reads where supported.
3. Run the discovery `rg` commands and classify each hit as in-scope required edit, acceptable limitation context, generated table source, or protected Figure 1 reference.
4. Edit contract files first: synchronize `TRACE_BIOPT_SPEC.md` and `TRACE_BIOPT_THEORY.md` around normalized full-state posterior trace and projected hidden-block variant.
5. Edit manuscript tone: update Section 4 title/opening and any nearby defensive wording without weakening formal assumptions or limitations.
6. Edit theory tables: change title/columns to formal properties, guarantees, assumptions and interpretation. Preserve caveats but do not foreground "non-claim boundary" in the main table.
7. Run the fast feedback loop. Update `ATTEMPTS.md` with pass/fail results.
8. Fix any remaining in-scope wording issues. Do not change Figure 1.
9. Run the full refresh script. Inspect generated changes and rerun targeted `rg` checks.
10. Run final status/diff review, update working memory, and prepare a concise final report with changed files and verification outcomes.
</workflow>

<working_memory>
Create and maintain these files:

- `.planning/goals/trace-biopt-trb-p0/PLAN.md`
- `.planning/goals/trace-biopt-trb-p0/ATTEMPTS.md`
- `.planning/goals/trace-biopt-trb-p0/NOTES.md`
- `.planning/goals/trace-biopt-trb-p0/CONTROL.md`

Update `PLAN.md` when the phase or strategy changes.

Update `ATTEMPTS.md` after each meaningful edit/check cycle, including command output summaries and next adjustment.

Update `NOTES.md` for durable discoveries, wording decisions, protected-file observations, and refresh outcomes.

Before final refresh and before any strategic pivot, reread `CONTROL.md`.
</working_memory>

<human_control_surface>
Create `.planning/goals/trace-biopt-trb-p0/CONTROL.md` as the compact operator panel.

Initial settings:

- status_file: `.planning/goals/trace-biopt-trb-p0/PLAN.md`
- attempt_log: `.planning/goals/trace-biopt-trb-p0/ATTEMPTS.md`
- durable_notes: `.planning/goals/trace-biopt-trb-p0/NOTES.md`
- primary_priority: submission-quality wording and contract consistency
- secondary_priority: preserve evidence chain and avoid unnecessary artifact churn
- protected_files: Figure 1 image assets and Figure 1 manuscript/caption content
- expensive_step_allowed: `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`
- require_approval_for: Figure 1 changes, new experiments, dependency changes, global optimality/approximation claims, unrelated model/training-code edits, scope expansion

`CONTROL.md` may narrow priorities or pause expensive steps, but it cannot silently weaken the `done_when` criteria or scorecard.
</human_control_surface>

<verification_loop>
Run these checks in order:

```bash
git status --short
rg -n "scoped theory|Scoped theoretical|narrow claim|Non-claim boundary|beats all baselines|globally optimal" TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md paper figures -S
rg -n "posterior_trace\\(S\\).*hidden|hidden uncertainty certificate|hidden-node risk identity|Bayes-risk certificate" TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md -S
python TRC-23-02333/test_transparent_estimator_eval.py
bash scripts/refresh_current_best_trace_biopt_paper_chain.sh
git diff --name-only
```

If a check fails, fix it when in scope and record the attempt. If the full refresh fails for an environmental reason, record the failing command, relevant error lines, and why the manuscript/contract edits are or are not implicated.
</verification_loop>

<execution_rules>
- Always reply to the user in Simplified Chinese.
- Check git status before edits.
- Preserve unrelated user changes.
- Prefer `rg` over `grep` when available.
- Use `apply_patch` for manual edits.
- Read context files before implementation.
- Batch independent file reads in parallel when the runtime supports it.
- Keep the scorecard current: know the primary metric, passing threshold, regression checks, scoring method, and stop condition.
- Use the fastest representative feedback check while iterating; reserve the full refresh for final verification.
- Maintain `.planning/goals/trace-biopt-trb-p0/PLAN.md`, `ATTEMPTS.md`, `NOTES.md`, and `CONTROL.md`.
- Update `ATTEMPTS.md` after each meaningful approach so future iterations do not repeat work without new evidence.
- Run focused tests before broad tests.
- Do not paper over failures.
- Do not widen scope.
- Do not modify Figure 1 or add AI-generated-image disclosure language.
- Keep the final answer concise and include verification outcomes.
</execution_rules>

<output_contract>
Final artifacts:

- Updated in-scope manuscript/contract files.
- Maintained working-memory files under `.planning/goals/trace-biopt-trb-p0/`.
- Final refresh/test outcomes recorded in `ATTEMPTS.md`.

Final response:

- Summarize the changed files and the framing changes.
- State whether Figure 1 was untouched.
- State the exact verification commands run and whether they passed.
- Call out any generated artifact churn or unresolved failures.
</output_contract>
