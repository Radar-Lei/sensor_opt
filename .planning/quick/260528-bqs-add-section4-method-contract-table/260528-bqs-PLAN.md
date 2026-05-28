# Quick Plan — 260528-bqs

## Goal

Add a Section 4 reviewer-facing method contract that makes TRACE-BiOpt's one-method identity explicit in the method section itself rather than only in front matter and discussion tables.

## Scope

- Create an automatic `TRACE-BiOpt method contract` generator.
- Insert the generated table into `paper/sections/4_method_theory.tex`.
- Wire the new generator into the current-best refresh chain.
- Extend the machine claim audit so the new method-contract table is required, not decorative.
- Revalidate the full paper chain and check that `paper/main.log` remains clean.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_method_contract_table.py scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`
- `rg -n -e 'Underfull' -e 'Overfull' -e 'Extra alignment' -e 'Misplaced \\\\noalign' -e 'undefined' paper/main.log`
