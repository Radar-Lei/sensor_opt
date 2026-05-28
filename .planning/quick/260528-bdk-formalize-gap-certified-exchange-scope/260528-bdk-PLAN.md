# Quick Plan — 260528-bdk

## Intent

Strengthen the TRACE-BiOpt exchange theory so the paper does not stop at a
generic searched-neighborhood certificate, but explicitly states when the
solver supports a full one-exchange zero-gap claim, when it only supports a
searched-active-set zero-gap claim, and when no zero-gap certificate is
available because the exchange budget is exhausted.

## Steps

1. Add a formal gap-certified proposition to Section 4 that distinguishes
   `G_1(\hat{\calS})=0`, `G^{search}_1(\hat{\calS})=0`, and budget-limited
   cases.
2. Upgrade the Section 6 exchange-certificate interpretation and generated
   table footnote to use the same gap-based language.
3. Extend the claim audit, rebuild the full current-best chain, and confirm
   the PDF, verifier, and LaTeX log stay clean.

## Guardrails

- Keep the theorem scoped: no full-network global optimality claim and no
  zero-gap certificate when the exchange budget is exhausted.
- Preserve compatibility with the existing row-level certificate table and
  current-best solver diagnostics.
- Treat this as a theory-to-evidence bridge strengthening, not as a new
  empirical claim lane.
