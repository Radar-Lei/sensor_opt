# Quick Summary — 260528-c1m

This quick task added a Section 3 problem contract so the paper now states, inside the formal problem definition, how TRACE-BiOpt should be read as a deployment-time transportation network-design problem.

## What changed

- Added a new generator:
  - `scripts/generate_trace_biopt_problem_contract_table.py`
- Added a new current-best artifact:
  - `TRC-23-02333/trace_sl_results/current_best_trace_biopt_evidence/trace_biopt_problem_contract.csv`
- Added a new paper table:
  - `paper/tables/table_trace_biopt_problem_contract.tex`
- Inserted the problem-contract table into:
  - `paper/sections/3_problem.tex`
- Wired the generator into:
  - `scripts/refresh_current_best_trace_biopt_paper_chain.sh`
- Extended:
  - `scripts/audit_trace_biopt_claims.py`
  so the new Section 3 table is machine-audited.

## What the new table makes explicit

- one long-lived deployment-time fixed-infrastructure decision
- one hidden-state recoverability target rather than coverage or visibility
- one transparent inverse problem inside one bilevel stochastic design formulation
- one train/validation/test split discipline aligned with deployment-time evaluation
- one external audited comparison class with `21` baselines across `11` families and no surviving challenger after `189/189` corrected paired wins
- explicit scope boundaries around exactness, observability, and untested baselines

## Verification outcome

- `python -m py_compile ...`: PASS
- `python scripts/generate_trace_biopt_problem_contract_table.py`: PASS
- `python scripts/audit_trace_biopt_claims.py`: PASS (`1632` checks)
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`: PASS
- `paper-claim-audit`: PASS (`1632` checks)
- `proof-checker`: PASS (`52` obligations)
- `citation-audit`: PASS
- `kill-argument`: PASS
- submission verifier: all four gates `OK / PASS / stale=false`
- `paper/main.pdf`: rebuilt successfully at 54 pages
- `paper/main.log`: no `Underfull`, `Overfull`, `Extra alignment`, `Misplaced \noalign`, or unresolved `undefined` messages
