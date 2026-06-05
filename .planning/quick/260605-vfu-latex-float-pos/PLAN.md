---
status: in_progress
quick_id: 260605-vfu
slug: latex-float-pos
created: 2026-06-05
---

# Quick Task: LaTeX float `pos=` cleanup

## Goal

检查 `paper/` 和生成片段中的 LaTeX 图表 float 位置参数，把 CAS 模板图表环境从裸 `[t]` / `[p]` 等形式改为显式 `[pos=...]`，并重新编译 `paper/main.pdf`。

## Tasks

1. 扫描 `figure`、`figure*`、`table`、`table*` 的可选位置参数。
2. 将图表统一改为正文优先的 CAS key-value 语法 `[pos=htbp]`，避免 `[p]` 或过窄 `[t]` 导致图表堆到文末。
3. 重新编译论文并确认没有遗留裸图表位置参数。
