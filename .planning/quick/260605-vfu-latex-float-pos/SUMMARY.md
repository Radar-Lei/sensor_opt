---
status: complete
quick_id: 260605-vfu
slug: latex-float-pos
completed: 2026-06-05
---

# Quick Task Summary: LaTeX float `pos=` cleanup

## Completed

- Converted all `figure`, `figure*`, `table`, and `table*` placement options in `paper/`, `figures/`, and relevant table-generation scripts from bare `[t]` / `[p]` style to CAS key-value `[pos=htbp]`.
- Added local `\FloatBarrier` calls around main-text table insertions and before references so main-body floats do not flush after the bibliography.
- Recompiled `paper/main.pdf` successfully.

## Verification

- `rg --pcre2 -n '\\begin\{(?:figure\*?|table\*?)\}\[(?!pos=)' paper figures scripts -g '*.tex' -g '*.py'` found no remaining non-`pos=` figure/table options.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` completed successfully in `paper/`.
- `pdfinfo paper/main.pdf` reports 49 pages.
- `pdftotext` check shows Table 1--6 before References, with appendix content after References.
