我看了渲染后的 PDF，包括正文和后面附录里的图。结论很直接：**论文主线没问题，但图和浮动体版面现在还不能原样投 TR-B。** 问题主要不是结果，而是"可读性"和"投稿版式可信度"：有些图题、图例、旁注、panel title 互相压住；有些图还带着实验脚本里的 raw route label；还有一些 Section 6 的图被 LaTeX 浮动到 Appendix 后面，容易让 reviewer 以为正文图和附录图混在一起。你这篇稿件的核心 claim 很强，更要避免被这些图面问题拖累。

Elsevier/TR-B 的作者指南也明确要求图作为单独 artwork 提交、尽量减少图内文字、符号和缩写要解释清楚，矢量图应存为 EPS/PDF；表格也建议 sparingly 使用，避免和正文重复，Appendix 里的图表最好用 Fig. A.1、Table A.1 这样的编号。([科学直达][1]) 你现在最该做的是一次集中"figure hardening"。

## 必须先修的 P0 问题

**1. Section 6 的图被浮动到 Appendix 后面，顺序感不对。**
PDF 里 Figure 6–12 都出现在后面附录区域附近，而正文 Section 6 早就引用了这些图。这个会给 reviewer 一种感觉：正文图、附录图、审计图混在一起了。建议二选一：

第一种，真正属于正文的图用 `\FloatBarrier` 强制留在正文相应 section 里：

```latex
\usepackage{placeins}

... Section 6 text ...

\begin{figure}[t]
...
\end{figure}

\FloatBarrier
```

并在 `\appendix` 前加一次：

```latex
\clearpage
\appendix
```

第二种，更推荐：把 Figure 6、7、8、12 这类机制/指纹/完整热图全部明确移入 Appendix，并重命名为 Fig. A.1、Fig. A.2。正文只保留 3–4 张最强、最干净的图。

**2. PDF 页脚现在出现 "Page 25 of 24 / Page 42 of 24" 这类错误。**
这是投稿前必须修的。要么不要显示总页数，只显示 `Page \thepage`；要么用 `lastpage` 正确统计全稿页数：

```latex
\usepackage{lastpage}
Page \thepage\ of \pageref{LastPage}
```

如果用 Elsevier `cas-sc.cls`，更稳的是不要自定义 "of total pages"，交给 class 处理。

**3. Appendix 图表编号要改。**
现在 Appendix 后面还是 Table 1、Table 2……这种编号，会和主文表格混淆。建议：

```latex
\appendix
\setcounter{figure}{0}
\setcounter{table}{0}
\renewcommand{\thefigure}{A.\arabic{figure}}
\renewcommand{\thetable}{A.\arabic{table}}
```

如果多个 appendix，就用：

```latex
\renewcommand{\thefigure}{\thesection.\arabic{figure}}
\renewcommand{\thetable}{\thesection.\arabic{table}}
```

## 图像逐项处理建议

| 图           | 当前问题                                                                                         | 建议处理                                                                                                                                   |
| ----------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Figure 1    | 没有明显重叠，但像 raster/slide 图，不够 TR-B 正式                                                          | 重画成真正矢量图。用 TikZ、draw.io、Illustrator/Inkscape、PowerPoint 矢量 PDF 都行，不要用 Pillow/JPEG 嵌图。图内文字减少，标题交给 caption。                              |
| Figure 2    | 网络点和边太淡，视觉上偏虚                                                                                | 保留可以，但提高节点/边对比度；caption 明确 PeMS7_1026 是 distance-matrix embedding，visual kNN edges 只是可视化辅助，不是道路拓扑。                                     |
| Figure 3    | PeMS7_1026、PeMS7_228 panel 顶部曲线和红色标签接近裁切；label 贴边                                            | 主文可删或移附录，因为 Figure 4 已经更强。若保留，加 y-axis headroom，例如 `ax.set_ylim(ymin, ymax + 0.08*range)`，不要把 baseline 名直接贴在曲线端点。                      |
| Figure 4    | 这是最适合主文的结果图，但右侧 "Strongest challenger" header 和 title 重叠，底部 legend 也挤                        | 必须修。用 GridSpec 分成左侧 forest plot + 右侧 challenger-name text panel；不要把右侧标签画在同一 axes 里。legend 放到图下方或删掉，用 caption 解释 Stage15/Stage16。       |
| Figure 5    | 顶部 legend、Spearman rho、panel title 相互挤压                                                      | Spearman rho 放到每个 panel 内部左上/右上角，带白底；legend 移到图外上方，增加 top margin。或者直接移附录。                                                              |
| Figure 6    | 图里有 raw route label，如 `pems7_1026 10 20 posterior iter20`、`train val lowcert...`；`J=...` 没解释 | 如果保留，必须把 raw label 改成人话：`TRACE-BiOpt`、`Strongest challenger`、`Stage16 calibrated`。`J` 要么删掉，要么 caption 解释为 unique-node Jaccard overlap。 |
| Figure 7    | 指纹图视觉还可以，但 `uniq=...` 和 `J=...` 仍像 debug annotation；还要核对是否确实读的是 current-best layout          | 建议放 Appendix。若保留，caption 明确 `uniq` 和 `J`，并确认图源脚本按 current-best provenance 解析 Stage16 promoted rows。                                    |
| Figure 8    | 作为机制切片可以，但 panel 小、色条多、只代表 seed-25 10%                                                       | 放 Appendix，正文只保留一句总结。caption 已经说 representative slice，这点是对的。                                                                           |
| Figure 9/10 | 图例和 panel title 明显重叠；上下两张图堆在一页里太挤                                                            | 拆成两张 Appendix 图，或正文只留 Figure 9。legend 放图外；去掉 bar 上方那些很小的 `exchange-only / 0-ex` 文本，改到 caption 或表里。                                     |
| Figure 11   | 图本身基本可用                                                                                      | 可以保留 Appendix 或 mechanism section；如果进正文，x-label 建议简化成 `PeMS1026 10%` 等，legend 放图外。                                                     |
| Figure 12   | 22-method heatmap 太密，适合 Appendix，不适合主文                                                       | 主文如果需要 heatmap，做 compact version：TRACE-BiOpt + top 6–8 challengers；full 22-method 放 Appendix 或 supplement。                             |

## 还有两个表格/版面问题要一起修

**Table 17 和 Table 18 旁边有孤立的 "Calibrated-risk paired"。**
这在 PDF 第 36–37 页非常突兀，像是一个跑出表格边界的残留 label。建议把它移到 table note 里：

```latex
\begin{threeparttable}
\caption{...}
\begin{tabularx}{\linewidth}{...}
...
\end{tabularx}
\begin{tablenotes}
\footnotesize
\item Calibrated-risk paired tests compare the rerun with the seed-matched best baseline.
\end{tablenotes}
\end{threeparttable}
```

不要让任何说明文字漂在表格右侧。

**Table 21 太小。**
如果 stress frontier 只是 bounded stress evidence，不要挤在正文。放 Appendix 或 supplement。正文用一段话总结即可。

## 我建议的最终主文图结构

主文不要放太多图。保守、干净、最像 TR-B 的组合是：

1. **Figure 1：TRACE-BiOpt workflow**
   重画矢量版，保留方法直觉。

2. **Figure 2：network cases**
   可以保留，但增强对比度，少放文字。

3. **Figure 3：paired margin forest plot**
   也就是现在 Figure 4，修掉右侧标签重叠后作为主结果图。它比 MAE 曲线更有说服力，因为直接显示 row-wise strongest challenger margin。

4. **Figure 4：one solver/mechanism diagnostic**
   可以选 objective descent 或 objective composition，二选一即可。不要把 Figure 9 和 10 都堆在正文。

其余的 sensor maps、layout fingerprints、hidden-error heatmaps、full baseline heatmap、full solver diagnostics，全部放 Appendix，并按 Fig. A.1、Fig. A.2 编号。

## 作图脚本层面的统一修法

建议新建一个统一的 plotting style 文件，比如 `paper_plot_style.py`，所有图都走同一套尺寸、字体和导出规则：

```python
import matplotlib.pyplot as plt

def set_paper_style():
    plt.rcParams.update({
        "font.size": 8,
        "axes.titlesize": 9,
        "axes.labelsize": 8,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "axes.spines.top": False,
        "axes.spines.right": False,
    })

def savefig(fig, path):
    fig.savefig(path, bbox_inches="tight", pad_inches=0.03)
```

但注意：`bbox_inches="tight"` 只能防止裁切，**不能自动解决文字互相重叠**。Figure 4、5、9、10 这种图，必须调整 layout 结构。

Figure 4 的右侧 challenger labels 最好不要画在主 axes 里，改成双列 GridSpec：

```python
fig = plt.figure(figsize=(7.2, 4.8), constrained_layout=True)
gs = fig.add_gridspec(1, 2, width_ratios=[4.2, 1.2])

ax = fig.add_subplot(gs[0, 0])
ax_lab = fig.add_subplot(gs[0, 1], sharey=ax)
ax_lab.axis("off")

# left: forest plot
ax.errorbar(margins, ypos, xerr=ci, fmt="o")

# right: challenger names
for y, name in zip(ypos, challengers):
    ax_lab.text(0.0, y, name, va="center", ha="left")

ax_lab.set_title("Strongest\nchallenger", fontsize=8)
```

Figure 5 的 Spearman rho 不要放在图外顶部，放进 axes：

```python
ax.text(
    0.03, 0.95,
    r"Spearman $\rho=0.540$",
    transform=ax.transAxes,
    va="top",
    ha="left",
    fontsize=7,
    bbox=dict(facecolor="white", edgecolor="none", alpha=0.8),
)
```

Figure 9/10 建议拆开。如果非要合并，一定要把 legend 放在全图下方：

```python
fig.legend(
    handles, labels,
    loc="lower center",
    ncol=3,
    frameon=False,
    bbox_to_anchor=(0.5, -0.02),
)
```

## 最小投前修复清单

按优先级来，不要再扩实验：

1. 修 Figure 4 的 title/right labels/legend 重叠。
2. 修 Figure 5 顶部 legend 和 Spearman annotation 重叠。
3. 修 Figure 9/10 的 legend-panel title 重叠，最好拆图。
4. 修 Table 17/18 右侧孤立文字。
5. Figure 1 重画为 vector PDF。
6. Figure 6/7 去掉 raw debug labels，解释或删除 `J`、`uniq`。
7. Figure 3 增加 y-margin 或移入 Appendix。
8. Figure 12 移 Appendix，主文不要放 full 22-method heatmap。
9. `\clearpage` 后再 `\appendix`，避免正文图漂到 Appendix 后面。
10. Appendix 图表编号改成 Fig. A.x / Table A.x，页脚总页数修正。

修完这十项后，图面风险会降很多。现在最不划算的是继续加新图；最划算的是把现有图"少而干净"，让 reviewer 第一眼看到的是一个严肃的 TR-B 方法论文，而不是一个实验审计包。

[1]: https://www.sciencedirect.com/journal/transportation-research-part-b-methodological/publish/guide-for-authors "Guide for authors - Transportation Research Part B: Methodological - ISSN 0191-2615 | ScienceDirect.com by Elsevier"
