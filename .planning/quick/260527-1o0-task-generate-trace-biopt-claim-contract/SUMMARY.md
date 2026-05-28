# Quick Summary: TRACE-BiOpt Claim Contract

## Completed

- Added `scripts/generate_trace_biopt_claim_contract.py`.
- Added `scripts/test_generate_trace_biopt_claim_contract.py`.
- Generated
  `TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_3seed_v2/combined/trace_biopt_claim_contract.csv`,
  `.json`, and `.md`.
- The contract contains nine supported directional Stage15 claim rows and one
  aggregate claim. It records the weakest margin as PeMS7_1026 at 30 percent
  budget against `validation_swap_selected`.
- Updated the Stage15 launcher so future runs generate the claim contract after
  dominance generation.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_claim_contract.py`
- `pytest -q scripts/test_generate_trace_biopt_claim_contract.py`
- Generated contract JSON reports schema `trace_biopt_claim_contract_v1` and
  `row_count=9`.

## Remaining

- Expand Stage15 beyond three seeds before final TR-B significance wording.
