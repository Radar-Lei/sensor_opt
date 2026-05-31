我又看了一轮新的 `main1.pdf` 渲染版，也按你的要求用 **GitHub 工具连接器**看了仓库里的 LaTeX、理论 contract 和源码实现。结论先说清楚：

**主线和大部分数学理论没有看到"致命错误"；但现在确实还有几处数学符号/实现/论文公式不完全一致的问题，投稿前必须修。排版方面也还没完全到 TR-B 投稿稿质感，主要集中在 Figure 1、Figure 4、Figure A.2/A.7/A.8。**

## 1. 排版：这版比前一版好，但仍有几个 P0/P1 问题

**Figure 1 仍然建议换。** PDF 第 6 页的框架图视觉上已经能读，但它还是"JPG 插入"的流程图，不是真正的矢量图。LaTeX 里现在明确插的是 `figures/fig1_trace_biopt_framework_v2.jpg`。 我用 PDF 工具看了对象，page 6 是 JPEG image object，不是纯 vector。作为第一张方法图，这个最好还是重画成矢量版，或者至少用高质量 PDF/SVG 导出版本。现在这张可以作为内部稿，但正式投稿版建议不要保留这种 raster/JPEG 主框架图。

**Figure 3 现在基本可以。** 第 12 页的 paired margin forest plot 已经把符号方向改对了：横轴是 strongest non-BiOpt baseline MAE − TRACE-BiOpt MAE，正值代表 TRACE-BiOpt 更好。图面目前能支撑主 claim，右侧 strongest challenger 列也没有前一版那么挤。

**Figure 4 还有挤压。** 第 16 页的 Figure 4 只有 objective descent 三个 panel，方向对；但图和 caption 的距离偏紧，x-axis label 贴得太近，整体像从脚本图硬塞进正文。建议把图高度稍微加大，或者主文只保留更简洁的三条曲线版，把 accepted-step mix 彻底留在 Appendix。

**Figure A.2 还需要修。** 第 38 页的 strongest-challenger envelope 图，顶部 legend 和 panel title 靠得很近，红色 challenger label 有贴边/接近裁切的问题。这个图已经在 Appendix，问题不致命，但最好加 y-axis headroom，并把 legend 放到图下或 caption 里。

**Appendix maps 明显好多了。** 第 42–43 页的 Figure A.5/A.6 已经没有 raw debug label，caption 也解释了 dotted edges 只是 visual aids，不代表完整道路拓扑，这个处理是对的。

## 2. 理论公式：大方向没错，但有 5 个需要修的"不一致点"

### 2.1 `M_S` 的符号必须统一

现在论文里 `M_S` 有时像"矩形选择矩阵"，有时又像"对角 mask"。比如 lower-level 里写 `M_s(z-x_t)`，posterior term 又写 `(I-M_S)\Sigma(I-M_S)`。如果 `M_S` 是 (k×n) 的选择矩阵，`I-M_S` 就没有维度意义；如果它是 (n×n) 的 diagonal mask，那 lower-level 写法成立，但需要明确说明。

仓库理论 contract 里写的是 "diagonal/selection observation operator"，这说明你们自己也知道这里有歧义。 论文正文最好改成两个符号：

$$
D_S=\operatorname{diag}(\mathbf{1}_{i\in S}),\qquad D_H=I-D_S.
$$

然后 lower-level 写成：

$$
\frac12|D_S(z-x_t)|_{R^{-1}}^2
$$

posterior hidden trace 写成：

$$
\operatorname{tr}(D_H\Sigma_{\mathrm{post}}(S)D_H).
$$

这样不会被审稿人抓维度错误。

### 2.2 posterior trace：论文写 hidden trace，但源码算的是 full trace

这是我这次检查里最重要的理论/实现不一致。

论文 Section 4 里 posterior term 写的是 hidden-state uncertainty：

$$
\Phi_{\mathrm{post}}(S)=\operatorname{tr}((I-M_S)\Sigma_{\mathrm{post}}(S)(I-M_S)).
$$

LaTeX 源码也是这么写的。 但 GitHub 源码里的 `posterior_trace_for_layout` 实际返回的是 **full posterior trace**，也就是整个 posterior inverse 的 trace，没有把 hidden complement 单独取出来。 scenario CVaR trace 也是对这些 full traces 做 upper-tail average。

这不是说方法错了，但论文公式必须和实现一致。现在有两个选择：

**推荐的低风险选择：不重跑实验，改论文表述。**
把 posterior/cvar 项写成 normalized full-state posterior uncertainty certificate：

$$
\Phi_{\mathrm{post}}^{\mathrm{full}}(S)=\frac{1}{n}\operatorname{tr}(\Sigma_{\mathrm{post}}(S)).
$$

Theorem 2 可以写成 full-state Bayes risk identity：

$$
\mathbb{E}|x-\mathbb{E}[x\mid y_S]|_2^2=\operatorname{tr}(\Sigma_{\mathrm{post}}(S)),
$$

然后补一句：hidden-block version follows by replacing $x$ with $x_H$ and $\Sigma_{\mathrm{post}}$ with its hidden block. 这样和源码、证据链一致，不需要重跑。

**如果坚持 hidden posterior trace，就必须改源码并重跑 current-best evidence。**
否则论文声称优化 hidden trace，但实际 evidence 是 full trace objective 跑出来的，会有审稿风险。

### 2.3 Section 3 和 Section 4 的 trace normalization 不一致

Section 3 里 upper-level objective 写了：

$$
\beta \frac{\mathrm{posterior\_trace}(S)}{|V|}+\gamma \frac{\mathrm{CVaR}_{\alpha}(\mathrm{scenario\_trace}(S))}{|V|}.
$$

这个和源码一致：`trace_biopt_objective` 里 posterior trace 和 scenario CVaR 都除以 `n_nodes`。 但 Section 4 里定义：

$$
J(S)=\hat R_v^{Huber}(S)+\beta\Phi_{post}(S)+\gamma\Phi_{tail}(S)+\cdots
$$

随后 $\Phi_{post}$ 没有除以 $|V|$。

建议直接改成：

$$
\Phi_{\mathrm{post}}(S)=\frac{1}{|\mathcal V|}\operatorname{tr}(\Sigma_{\mathrm{post}}(S)),
$$

或者 hidden 版本：

$$
\Phi_{\mathrm{post}}(S)=\frac{1}{|\mathcal V|}\operatorname{tr}(D_H\Sigma_{\mathrm{post}}(S)D_H).
$$

同理，tail term 也加 $/|\mathcal V|$。这样 Section 3、Section 4、源码三者一致。

### 2.4 Huber loss 需要明确定义，避免标准 Huber 缩放歧义

源码的 `smooth_l1_mean` 实际实现是：

$$
\rho_\delta(e)=\begin{cases}\frac{e^2}{2\delta}, & |e|\le \delta,\\|e|-\frac{\delta}{2}, & |e|>\delta.\end{cases}
$$

代码里对应的是 `0.5 * quadratic**2 / delta + linear`。 hidden Huber 的实现也是同一形式。

这个是常见的 smooth-L1 / Huberized absolute loss，没有问题。但论文现在只说 "Huber penalty"，没有公式。建议在 Section 4.2 加一句定义，否则有审稿人会默认标准 Huber：

$$
\rho_\delta(e)=\frac12 e^2 \quad (|e|\le\delta),\quad\delta(|e|-\delta/2) \quad (|e|>\delta),
$$

那就和源码缩放不一致。

### 2.5 CVaR 的 $\alpha$ 和源码里的 `tail_fraction` 要对齐

理论里 CVaR epigraph 写成：

$$
\tau+\frac{1}{(1-\alpha)|\mathcal T_v|}\sum_t(\ell_t(S)-\tau)_+.
$$

这个公式本身是对的。 但源码实际用的是 `cvar_tail_fraction`，即直接取 largest tail fraction 的平均。

所以论文需要明确：

$$
q = 1-\alpha,
$$

其中 $q$ 是 implementation 中的 `cvar_tail_fraction`。例如 `tail_fraction=0.1` 对应的是 $\mathrm{CVaR}_{0.9}$，不是 $\mathrm{CVaR}_{0.1}$。

## 3. Lower-level MAP / GLS 这块基本是对的

这部分我比较放心。论文里的 closed form：

$$
A(S)=M_S^\top R^{-1}M_S+\lambda_QQ+\lambda_LL+\epsilon I,\quad b_t(S)=M_S^\top R^{-1}M_Sx_t+\lambda_QQ\mu_t
$$

和理论 contract 是一致的。 LaTeX 里也对应这个写法。 源码 `solve_quadratic` 实际求的是：

$$
(\text{matrix}+\operatorname{diag}(\text{selector}))z=\text{matrix}\cdot\mu + \text{selector}\odot y,
$$

代码里表现为 `lhs = matrix + np.diag(selector)`，以及 `rhs[:, sensors] += selector[sensors] * observed_z[:, sensors]`。 这和"prior precision + observed sensor quadratic term"的 MAP/GLS 结构一致。

这里唯一需要注意的是：论文写了 $\lambda_QQ+\lambda_LL+\epsilon I$，而当前实现主要通过 `gls_matrix`/precision matrix 进入；如果当前 evidence 里 $\lambda_L=0$ 或 Laplacian 已被并入 matrix，就没问题。但最好在论文里说"the implemented GLS/MAP precision may instantiate this regularizer through the fitted precision and/or graph penalty"，避免让人以为源码里一定显式加了 $L$。

## 4. 理论 theorem 本身有没有明显错？

我没看到定理层面的硬错，但建议按下面方式收紧：

Theorem 1 的 closed form / stability 是成立的，前提是 $R\succ0$ 且 prior-plus-ridge precision 正定。理论 contract 也明确有这个条件。

Theorem 2 的 posterior trace Bayes risk identity 是成立的，但要把"full trace vs hidden trace vs implementation full trace"说清楚。现在源码 evidence 用 full trace，所以论文最好不要把 objective 写成 hidden posterior trace，除非重跑。

Theorem 3 的 uniform validation generalization bound 形式是对的：Hoeffding + union bound over $\binom{n}{k}$，得到 $k\log(en/k)$ 这一项。论文 proof 也正是这么写的，并且加了 temporal dependence 下要用 independent blocks/effective sample size 的 caveat。 这个没问题。

Theorem 4 的 exchange certificate 是对的，而且源码也确实是 deterministic one-swap exchange：初始化后每轮枚举 searched add/remove active sets，接受严格更优 swap，否则 stop。 论文已经说明它只证明 searched-neighborhood stationarity，不证明 global optimality。 这个边界写得对。

## 5. 我建议你现在马上改的最小清单

**数学/理论 P0：**

1. 引入 $D_S$ 和 $D_H$，不要继续让 `M_S` 同时扮演 rectangular selector 和 diagonal mask。
2. 决定 posterior/cvar trace 到底按源码写 full trace，还是改源码重跑 hidden trace。我的建议是不重跑，论文改成 full trace certificate。
3. Section 4 的 $\Phi_{\mathrm{post}}$、$\Phi_{\mathrm{tail}}$ 加 $/|\mathcal V|$，和 Section 3、源码一致。
4. 明确定义 smooth-L1/Huber $\rho_\delta$，匹配源码。
5. CVaR 里写清楚 `tail_fraction = 1-\alpha`。
6. Continuous relaxation 那段把 "gradient" 改成 "finite-difference projected update over a deterministic active pool"，因为源码确实是有限差分 active-pool 更新。

**排版 P0/P1：**

1. Figure 1 换成正式矢量版，不要用当前 JPG 主框架图。
2. Figure 4 增加图和 caption 间距；或者主文只留 objective descent，step mix 留 Appendix。
3. Figure A.2 重画，处理 legend/title/red labels 的贴边问题。
4. Appendix 的 A.7/A.8 作为诊断图可以留，但最好拆得更松一些。
5. Full heatmap 留 Appendix，不要搬回正文。

## 6. 最终判断

**这版不是"理论错了"，但也还不能说数学已经完全封口。** 最关键的问题是：论文公式现在说 hidden posterior trace，而源码 evidence 实际是 full posterior trace。这个必须统一。统一之后，MAP closed form、Bayes risk identity、uniform generalization、exchange certificate 这些理论大体是稳的。

我建议下一轮不要再大改实验；直接做一次 **math-consistency patch + figure hardening**。修完上面这几个点后，我会更放心地把它视为 TR-B 投稿前最终稿。
