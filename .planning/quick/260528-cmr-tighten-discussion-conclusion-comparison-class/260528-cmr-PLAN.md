# Quick Plan — 260528-cmr

## Goal

Tighten the manuscript's discussion, conclusion, and method-spec wording so the paper no longer falls back to a weaker `strongest-baseline` shorthand where the stronger `external audited comparison-class contract` is now the real paper-facing evidence lane.

## Scope

- Update `paper/sections/7_discussion.tex` so the boundary and deployment-readout prose explicitly references the 21-baseline / 11-family / 189-corrected all-baseline screen.
- Update `paper/sections/8_conclusion.tex` so the compressed TR-B claim and closing evidence sentence use the stronger comparison-class contract wording.
- Update `TRACE_BIOPT_SPEC.md` to align the method-identity contract with the same comparison-class wording.
- Regenerate the discussion-boundary table and extend the claim audit so the new wording is required.
- Revalidate the full paper chain and check that `paper/main.log` stays clean.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_discussion_boundary_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`
- `rg -n -e 'Underfull' -e 'Overfull' -e 'Extra alignment' -e 'Misplaced \\\\noalign' -e 'undefined' paper/main.log`
