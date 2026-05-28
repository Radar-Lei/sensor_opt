# Quick Task 260527-ply Summary

## Outcome

Added an appendix provenance table for the current-best TRACE-BiOpt dominance
chain. The table shows, row by row, whether the main result currently comes
from Stage15 or from a replaceable Stage16 calibrated rerun, along with the
paired-evidence status.

## Verification

- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh`

## Result

The appendix now makes the hybrid evidence policy explicit instead of leaving it
implicit in file paths and surrounding prose.
