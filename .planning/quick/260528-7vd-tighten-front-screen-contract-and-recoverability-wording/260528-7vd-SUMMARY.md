# Quick Summary — 260528-7vd

## What changed

- Tightened the compiled abstract in `paper/main.tex` and the source abstract in
  `paper/sections/0_abstract.tex` so the front-screen summary now reads:
  one long-lived infrastructure decision, one transparent inverse problem, one
  scoped theory package, and one strongest-baseline evidence contract.
- Added the same front-screen contract explicitly to
  `paper/sections/1_introduction.tex`, `paper/sections/2_related_work.tex`, and
  `paper/sections/8_conclusion.tex` so the first screen, comparison class, and
  closing paragraph no longer drift.
- Updated `scripts/generate_trace_biopt_reader_guide_table.py` and
  `scripts/generate_trace_biopt_novelty_identity_table.py` so the generated
  current-best tables no longer call TRACE-BiOpt `reconstruction-aware`; they
  now use the manuscript's `recoverability-driven` method identity.
- Refreshed `TRACE_BIOPT_SPEC.md` so its method identity and current evidence
  state match the current-best chain: 8/9 Stage16-promoted rows, with only
  Seattle 10\% intentionally retained on the Stage15 path.
- Extended `scripts/audit_trace_biopt_claims.py` to machine-check the new
  front-screen contract across front matter, introduction, related work, and
  conclusion.

## Verification

- `python -m py_compile scripts/generate_trace_biopt_reader_guide_table.py scripts/generate_trace_biopt_novelty_identity_table.py scripts/audit_trace_biopt_claims.py` — PASS
- `bash scripts/refresh_current_best_trace_biopt_paper_chain.sh` — PASS
  - `paper-claim-audit`: PASS (`1448` checks)
  - `proof-checker`: PASS
  - `citation-audit`: PASS
  - `kill-argument`: PASS
  - submission verifier: all `OK / PASS / stale=false`
  - `paper/main.pdf`: rebuilt at `48` pages

## Result

The paper now repeats the same TR-B-facing contract from the title page through
the closing section, and the current-best front-screen tables no longer lag the
manuscript's recoverability-driven method identity.
