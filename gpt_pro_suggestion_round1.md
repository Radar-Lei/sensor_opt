我看了 9923023 这一版的 LaTeX、表格、作图脚本、current-best evidence CSV，以及几个图文件的元信息。**结论是：论文主线和结果现在基本没有大问题，可以冲 Transportation Research Part B；但我不建议现在立刻投，因为图里面确实还有几个“真实问题”，不是纯审美问题。** 这也和前一轮判断一致：现在重点已经不是继续发明方法，而是投稿硬化、修图、删噪和统一 claim。

## 1. 论文版本总体判断

**方法叙事现在是对的。** 最新稿件已经把问题写成 recoverability-driven bilevel transportation network design，而不是旧的 candidate-pool selector。摘要也已经明确说 TRACE-BiOpt 是一个 bilevel stochastic design method，lower level 是 GLS/MAP reconstruction，upper level 组合 Huber reconstruction loss、posterior uncertainty、CVaR tail risk 和 spatial redundancy；同时明确 baseline 不进入方法候选池。 这和 TR-B 的 methodological scope 是匹配的；TR-B 官方 scope 本身强调 mathematical analysis、optimization、network design/analysis 和交通系统方法论。([科学直达][1])

**实验 claim 现在也基本站得住。** 主表显示 9 个 dataset-budget rows 上 TRACE-BiOpt 都低于 row-wise strongest challenger，且都是 10/10 paired wins。 current-best evidence CSV 也显示所有 `trace_minus_best_baseline` 都是负数，即 TRACE-BiOpt MAE 更低。 另外，evidence index 已经把 claim、source CSV、生成脚本、Stage15/Stage16 来源和 Seattle 10% fail-closed 解释串起来了，这是加分项。

**投稿材料还差最后封口。** `PAPER_WRITING_PIPELINE_REPORT.md` 现在写的是 submission-ready yes，并且 LaTeX、pytest、claim audit、citation audit 都通过；但它仍然列出 author metadata、affiliations、declarations、portal-specific files 需要补齐，且 manuscript 只有 18 页。 这些不是科学问题，但投稿前必须处理。

## 2. 图里面最需要马上修的 3 个问题

**第一，margin forest 图的正负号说明错了。**
现在论文 caption 写的是 “Positive values indicate that TRACE-BiOpt has lower error”。 但脚本实际画的是 `paired_delta_mean = TRACE-BiOpt MAE - strongest baseline MAE`，而且脚本自己的 note 写的是 “Negative values favor TRACE-BiOpt”。 CSV 也证明所有优势都是负数。

这个必须修。最简单做法是把 caption 改成：

> Negative values indicate lower held-out GLS/MAP MAE for TRACE-BiOpt.

更好的做法是改脚本，把横轴改成：

[
\text{Strongest challenger MAE} - \text{TRACE-BiOpt MAE}
]

这样正数就表示 TRACE-BiOpt 更好，和读者直觉一致。

**第二，layout fingerprint 图不是 current-best。**
`generate_trace_biopt_layout_fingerprint_figure.py` 的 `collect_frequency()` 直接从 Stage15 目录读 layouts，没有解析 Stage16 promoted rows。 但正文却把这个图说成 “Current-best low-budget layout fingerprints”。 这会被审稿人抓住：PeMS7_1026 10% 和 PeMS7_228 10% 当前是 Stage16 current-best，但图可能画的是 Stage15 旧布局。

这个图要么重写脚本，复用 sensor map 脚本里的 `resolve_trace_layout_path()` 逻辑；要么把图改名为 historical Stage15 fingerprint，并移到附录。前者更好。

**第三，框架图是 raster PDF，不是干净的 vector 图。**
`fig1_trace_biopt_framework_v2.pdf` 的文件头显示它是 Pillow 生成的 PDF，里面嵌了 JPEG image XObject，而不是矢量图。 作为主文 Figure 1，这不理想。TR-B/Elsevier 对 artwork 有明确要求，线图最好用 EPS/PDF 等矢量格式，并注意字体、分辨率和可读性。([科学直达][1])

建议重新做 Figure 1：用 TikZ、draw.io、PowerPoint 矢量导出、Illustrator/Inkscape 或 Matplotlib vector PDF，不要用 Pillow/JPEG 嵌图。尤其你之前也担心“AI 图标感”，那主框架图更应该走干净的学术流程图风格。

## 3. 其他图的处理建议

**full baseline heatmap 不建议放主文。** 它确实能证明 22-method matrix 中 TRACE-BiOpt rank 1，但主文里 22 行 × 3 dataset panels 太密。脚本本身也已经提供 compact heatmap，并说明 full matrix 应该放 appendix 或 repository。 Elsevier 也提醒 tables/figures 要 sparingly 使用，不要过度堆叠。([科学直达][1]) 我的建议是：主文保留 margin forest；full heatmap 放附录。

**performance curve 要改名。** 现在它画的是“row-specific strongest baseline”，不同 budget 的 challenger 可能不是同一个方法；脚本也在每个点旁标注不同 baseline。 所以不要叫普通 “best baseline curve”，应叫 **strongest-challenger envelope**，否则看起来像同一个 baseline 方法随 budget 变化。

**network/budget panels 要防误导。** 脚本用 kNN visual edges，只是为了防止图像像孤立点云，不是实际道路拓扑。 如果这些图进论文，caption 必须写清楚 “edges are visual aids only”。另外脚本默认在找不到 TRACE layout 时会 fallback 到 deterministic random mask，除非加 `--strict`。 投稿图必须用 `--strict` 生成，避免误把 random fallback 当成 TRACE-BiOpt layout。

**sensor maps 可以保留，但 caption 要解释 J。** 图里右下角有 `J=...`，脚本中这是 overlap/union 的 unique-node Jaccard overlap。 但 caption 没解释 J。 要么 caption 加一句 “J denotes unique-node Jaccard overlap between TRACE-BiOpt and the strongest baseline layouts”，要么删掉图中的 J。

**hidden error heatmap 只能放附录。** 它是 representative seed-25、10% budget、common-hidden nodes 的机制切片，不是全量 dominance evidence。脚本明确固定 `REPRESENTATIVE_BUDGET=0.1`、`REPRESENTATIVE_SEED=25`。 正文现在已经说它是 bounded mechanism slice，不是 dominance row，这个表述是对的。

## 4. 文字上还有几个小修

`table_external` 是旧 Stage12 TRACE-SL 表，现在放在主文会让 reviewer 分心。它显示的是旧 TRACE-SL，而不是 current TRACE-BiOpt。 我建议移到附录，主文只保留一句 “older Stage12 results motivated the pivot”。

Conclusion 里有一句把 “27/27 exact hits” 和 “searched-neighborhood stationarity certificate” 放在一起，容易让人误解为 exact subnetwork benchmark 提供了 full-network stationarity certificate。 建议拆开：exact hits 是 bounded small-subnetwork evidence；exchange certificate 是 solver diagnostic/theory 的证据。

另外 `PAPER_WRITING_PIPELINE_REPORT.md` 仍有一些旧 Stage15 语言，例如输入写 Stage15 evidence、若干 probe “without replacing Stage15 main table”，但现在 8/9 rows 已经 Stage16 promoted。 这个报告最好刷新一下，避免 co-author 或 reviewer 看仓库时觉得版本没同步。

## 5. 最终判断

**可以投 TR-B，但要先修图。** 现在不是“论文方法有大问题”，而是“图和 caption 还有几个会损害可信度的问题”。我认为最小修复清单是：

1. 修 margin forest 正负号；
2. 修 layout fingerprint 的 current-best 数据源；
3. 重做 Figure 1 为真正矢量图；
4. full heatmap 移到附录，主文用 margin forest；
5. performance curve 改成 strongest-challenger envelope；
6. network/budget panels 加 visual-edge 和 `--strict` 说明；
7. 刷新 pipeline report 和 conclusion 那句 exact/certificate 表述。

修完这些后，我会认为这个版本已经可以作为 TR-B 投稿稿进入最后格式检查。

[1]: https://www.sciencedirect.com/journal/transportation-research-part-b-methodological/publish/guide-for-authors "Guide for authors - Transportation Research Part B: Methodological - ISSN 0191-2615 | ScienceDirect.com by Elsevier"
