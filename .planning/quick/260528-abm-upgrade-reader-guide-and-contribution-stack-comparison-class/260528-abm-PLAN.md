# Quick Plan — 260528-abm

## Intent

Upgrade the front-page reviewer guide and contribution stack so they explicitly
absorb the stronger `21 baselines / 11 families` comparison-class fact instead
of staying at the older `21 baselines` level.

## Steps

1. Extend the reader-guide generator so its first-screen method and evidence
   answers mention the 11 audited baseline families.
2. Extend the contribution-stack generator so the evidence layer states that
   the current-best chain spans 21 baselines across 11 families.
3. Update `scripts/audit_trace_biopt_claims.py` to machine-check those stronger
   table-level comparison-class statements.
4. Re-run the full current-best chain and confirm the 51-page PDF plus all
   submission gates remain green.

## Guardrails

- Keep the stronger comparison-class wording tied to the audited registry, not
  to untested future baselines.
- Preserve the existing strongest empirical facts: `9/9` paired rows,
  `189/189` corrected wins, and zero surviving tied-or-better challenger.
- Treat the table upgrade as front-screen compression of existing evidence, not
  a new empirical lane.
