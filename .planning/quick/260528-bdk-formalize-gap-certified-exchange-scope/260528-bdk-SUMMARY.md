# Quick Summary — 260528-bdk

## Outcome

Formalized the TRACE-BiOpt exchange-certificate story into a gap-certified
proposition, upgraded the Section 6 reading and exchange-certificate table to
use `G_1` / `G^{search}_1` language, and revalidated the full 52-page
submission chain.

## What changed

- Updated:
  - `paper/sections/4_method_theory.tex`
  - `paper/sections/6_ablation_robustness.tex`
  - `scripts/generate_trace_biopt_exchange_certificate_table.py`
  - `scripts/audit_trace_biopt_claims.py`
- Added a formal proposition that distinguishes:
  - complete one-exchange certificates with `G_1(\hat{\calS})=0`
  - searched-active-set certificates with only
    `G^{search}_1(\hat{\calS})=0`
  - budget-limited rows with no zero-gap certificate
- Updated the Section 6 mechanism discussion so PeMS7_228 10\%, Seattle
  30\%, and the budget-limited PeMS7_1026 rows are described using the same
  gap-certified language.
- Updated the exchange-certificate table caption/footnote so the row-level
  certificate scopes now map directly to the theorem-facing gap notation.
- Extended the claim audit to machine-check the new proposition, Section 6
  wording, and table footnote.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_exchange_certificate_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/generate_trace_biopt_exchange_certificate_table.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`
- `rg -n -e 'Underfull' -e 'Overfull' -e 'Extra alignment' -e 'Misplaced \\\\noalign' -e 'undefined' paper/main.log`

Final status:

- `paper-claim-audit`: `PASS` (`1595` checks)
- `proof-checker`: `PASS` (`52` obligations)
- `citation-audit`: `PASS`
- `kill-argument`: `PASS`
- submission verifier: `OK / PASS / stale=false` on all four gates
- `paper/main.pdf`: rebuilt successfully (`52` pages)
- `paper/main.log`: no `Underfull`, `Overfull`, `Extra alignment`,
  `Misplaced \noalign`, or unresolved `undefined` messages
