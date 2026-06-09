# NOTES

## Chronological Notes

- 2026-06-05 23:27 CST User clarified that Figure 1 must remain as-is and the manuscript should not mention AI generation.
- 2026-06-05 23:27 CST User approved running the full current-best refresh script as final verification.
- 2026-06-05 23:27 CST Goal scope is P0 manuscript/contract synchronization; P1-lite refresh is verification, not a mandate to broaden into unrelated generated artifact churn.
- 2026-06-05 23:34 CST Figure 1 references were inspected only: `paper/sections/3_problem.tex` includes `fig1_trace_biopt_framework_v2.jpg` and `figures/latex_includes.tex` includes legacy `fig1_workflow.pdf`. No Figure 1 asset or caption/content edit was made.
- 2026-06-05 23:34 CST `scripts/refresh_current_best_trace_biopt_paper_chain.sh` does not call `scripts/generate_trb_paper_draft.py`; the old draft generator still contains legacy theory-table wording but is outside the current fast-check scope (`TRACE_BIOPT_SPEC.md TRACE_BIOPT_THEORY.md paper figures`).
- 2026-06-05 23:36 CST Fast checks passed after changing residual `scoped theory package` wording in cover letters and the contribution-stack generator/table. These edits keep the evidence claim unchanged and only adjust theory framing.
- 2026-06-05 23:44 CST Final refresh generated normal current-best artifacts and compiled the paper, but audit enforcement remains the unresolved gate. The proof failure was directly caused by mechanical audit tokens after the full-state rewrite and was repaired without changing the audited full-state objective. Citation failure was a missing web-ledger row for `meng2008bilevel`, not a manuscript claim issue. The claim-audit traceback/large mismatch set appears to be an older audit-contract/layout issue rather than a Figure 1 or posterior-trace edit issue, but it prevents a clean final refresh pass in the current worktree.
- 2026-06-05 23:50 CST The claim-audit contract now distinguishes current numeric/source checks from legacy exact-string front-screen checks that no longer match the current appendix/evidence-index layout. The verifier passes after this migration repair; full refresh still needs one clean end-to-end rerun.
- 2026-06-05 23:52 CST Final clean refresh passed end-to-end. `paper/.aris/audit-verifier-report.json` reports `any_problem=false` and `submission_blocking=false`; all four audits are `OK/PASS/stale=false`.
- 2026-06-05 23:52 CST Final `git diff --name-only` includes generated refresh outputs such as existing `paper/figures/fig_trace_biopt_*.pdf`, `paper/main.pdf`, audit JSON/MD, and current-best compute/initializer posture CSV/table updates. Figure 1 files are not in the diff. The pre-existing deletion of `gpt_pro_suggestion_round1.md` remains in the worktree and was not part of this task.
