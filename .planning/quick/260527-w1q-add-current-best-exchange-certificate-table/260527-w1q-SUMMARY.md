# Quick Task 260527-w1q Summary

## Outcome

Added a reviewer-facing current-best exchange-certificate table:
`paper/tables/table_trace_biopt_exchange_certificate.tex` with backing CSV
`current_best_trace_biopt_evidence/trace_biopt_exchange_certificate_summary.csv`.

The new table lifts Theorem T4 out of the theory section and binds it to the
actual current-best rows. It now makes three practically different certificate
regimes explicit:

- `PeMS7_228 10%` is the cleanest row: a complete one-exchange certificate,
  because all ten runs searched the full one-exchange neighborhood and stopped
  only after no improving swap remained.
- `Seattle 30%` is a searched active-set certificate: every run ends with no
  improving searched swap, but the searched neighborhood is still a strict
  subset of the full `k(n-k)` swap set.
- The promoted `PeMS7_1026 20/30%` rows are budget-limited certificates:
  search coverage stays below 1.5% and the runs exhaust the declared exchange
  budget before a no-improving searched-swap stop appears.

This gives the manuscript a clearer optimization-scope posture. The paper no
longer relies on readers inferring certificate strength from scattered stop
counts or coverage columns; it states the row-level solver guarantee class
directly next to the mechanism analysis.

The audit layer was extended at the same time. `scripts/audit_trace_biopt_claims.py`
now checks the new table inclusion, the nine-row backing CSV, the unique
complete-certificate row, the budget-limited PeMS7_1026 rows, the Seattle 30%
searched active-set row, and the surrounding reviewer-facing wording in
Section 6.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_exchange_certificate_table.py scripts/audit_trace_biopt_claims.py`
- `python scripts/generate_trace_biopt_exchange_certificate_table.py`
- `python scripts/audit_trace_biopt_claims.py`
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The refreshed current-best paper chain stayed fully green. `paper-claim-audit`
expanded to 943 checks, `proof-checker`, `citation-audit`, and
`kill-argument` all remained `PASS`, the submission verifier stayed
`OK / PASS / stale=false` on all four audits, and `paper/main.pdf` rebuilt
cleanly at 36 pages.
