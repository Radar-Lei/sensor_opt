对，你这个判断是对的。**如果主方法被写成“一个 pool，里面有很多候选，然后从中挑最优”，TR-B reviewer 可能会觉得它更像 portfolio / AutoML selector，而不是一个原创、统一、可分析的交通网络设计方法。** 这会削弱 contribution。

你想要的是：

> **一个唯一的方法，一个统一目标，一个确定性优化过程；它不是从 baselines 里挑，而是直接优化一个 reconstruction-aware traffic sensor design problem，并且在实验上打败所有预先定义的 baselines。**

我建议下一步不要继续强化 “candidate pool story”，而是把论文升级成：

> **TRACE-BiOpt / TRACE-Opt：a robust bilevel reconstruction-aware sensor layout optimization method**

也就是把 TRACE-SL 从 portfolio framework 改成 **单一 bilevel stochastic network design method**。

---

## 1. 为什么现在的 pool 思路不适合你想要的强 claim

当前论文 Section 4 其实还是说 TRACE-SL 有多个 candidate generators：posterior A-trace、D-logdet、scenario risk、top variance、degree、graph sampling、QR/POD、random 等，然后用 validation-calibrated selection 和 swap refinement。

这个在工程上有效，但从论文贡献看有三个问题。

**第一，它像 meta-selector，而不是新方法。**
审稿人可能会问：你的方法到底是新的 sensor placement principle，还是把很多已有 baselines 放一起再挑？

**第二，它难以 claim “打败所有 baselines”。**
如果你把 baseline 放进 pool，最后赢了，别人会说你只是选择了 baseline；如果没放进 pool，强 baseline 又可能打败你。这个逻辑很尴尬。

**第三，理论很难强。**
当前 finite-candidate validation bound 只能说“在有限候选集内选择不会太差”。这不是 TR-B 最想要的那种强 network design / optimization result。

所以我建议换叙事：**不要再把 pool 作为主方法。**

---

## 2. 新方法应该是什么：一个统一的 bilevel reconstruction-risk optimization

把方法定义成一个唯一的优化问题：

[
\min_{s\in{0,1}^n}
\quad
J(s)
\qquad
\text{s.t.}
\quad
\mathbf 1^\top s=k,
]

其中 (s_i=1) 表示第 (i) 个位置安装 sensor。

核心是 (J(s)) 不是 coverage、variance、trace 这种代理目标，而是直接面向 hidden-network reconstruction：

[
J(s)
====

\underbrace{
\frac{1}{|\mathcal T_v|}
\sum_{t\in\mathcal T_v}
\frac{1}{n-k}
\sum_{i=1}^n
(1-s_i)
\rho_\delta
\left(x_{ti}-\hat x_{ti}(s)\right)
}*{\text{validation hidden reconstruction loss}}
+
\beta
\underbrace{
\operatorname{tr}
\left[
(I-M_s)\Sigma*{\mathrm{post}}(s)(I-M_s)
\right]
}*{\text{posterior uncertainty}}
+
\gamma
\underbrace{
\operatorname{CVaR}*{\alpha}
\left(
\ell_t(s)
\right)
}*{\text{tail-risk robustness}}
+
\eta
\underbrace{
\Omega*{\mathrm{spatial}}(s)
}_{\text{redundancy / deployment regularization}}.
]

这里：

* (\rho_\delta) 是 Huber / smooth-L1 loss，比 MAE 更容易优化，也比 squared loss 更 robust；
* (\hat x_t(s)) 是在 sensor set (s) 下由透明 MAP/GLS estimator 重构出的 full network state；
* posterior trace 是理论 certificate；
* CVaR 是 robust transportation network design 的味道；
* spatial regularization 防止 sensors 全堆在局部区域；
* 但所有东西都在 **一个 objective** 里面，不是 pool 选择。

这个方法的 lower-level reconstruction 可以写成：

[
\hat x_t(s)
===========

\arg\min_z
\left{
\frac{1}{2}
|M_s(z-x_t)|_{R^{-1}}^2
+
\frac{\lambda_Q}{2}
(z-\mu)^\top Q(z-\mu)
+
\frac{\lambda_L}{2}
z^\top Lz
\right}.
]

这就是一个 convex quadratic MAP reconstruction problem。给定 (s)，它有闭式解：

[
\hat x_t(s)
===========

A(s)^{-1}b_t(s),
]

其中：

[
A(s)=M_s^\top R^{-1}M_s+\lambda_Q Q+\lambda_L L.
]

于是 sensor layout 是 upper-level discrete optimization，reconstruction 是 lower-level convex optimization。这个就很像 TR-B 会认可的 **bilevel network design / stochastic optimization / traffic system design**。

---

## 3. 这个方法怎么命名和定位

建议保留 TRACE 品牌，但换成更强的主方法名：

### 方案 A：TRACE-BiOpt

**Transparent Reconstruction-Aware Bilevel Optimization for Sensor Layout**

优点：一听就是 bilevel optimization，不像 heuristic。

### 方案 B：TRACE-RBO

**Transparent Reconstruction-Aware Robust Bilevel Optimization**

优点：强调 CVaR / robust network design。

### 方案 C：TRACE-Opt

**Transparent Reconstruction-Aware Sensor Layout Optimization**

最简单，适合论文标题。

我更建议：

> **TRACE-BiOpt: A Recoverability-Driven Bilevel Optimization Method for Sparse Traffic Sensor Layout**

然后把当前 TRACE-SL portfolio 改成 old version / ablation / candidate heuristic，不再作为最终主方法。

---

## 4. 这个唯一方法怎么优化，才能真的打败 baselines

你不能只定义一个漂亮 objective，还要让它在实验上强。我的建议是：

### 4.1 连续松弛 + 投影优化 + 离散修复

把 (s\in{0,1}^n) 松弛成：

[
s\in[0,1]^n,\qquad \mathbf 1^\top s=k.
]

然后优化 (J(s))。因为 lower MAP solution (\hat x_t(s)) 对 (s) 可微，可以用 projected gradient / Frank-Wolfe / mirror descent。

最后取 top-(k) rounding：

[
S_0=\operatorname{TopK}(s).
]

### 4.2 确定性 exchange refinement，不是 pool

rounding 后做 deterministic local improvement：

[
S^{(m+1)}
=========

\arg\min_{S'\in\mathcal N_1(S^{(m)})}
J(S'),
]

其中 (\mathcal N_1(S)) 是 one-swap neighborhood。

这里的 swap refinement 是 **这个单一优化算法的一部分**，不是从 candidate pool 里挑。区别很重要。

### 4.3 可以做 two-swap / beam，但仍然是一个方法

为了打败所有 baselines，one-swap 可能不够。可以用：

* one-swap until convergence；
* top candidates 进入 limited two-swap；
* beam width (q)；
* deterministic stopping rule；
* objective 永远是同一个 (J(S))。

这仍然是一个唯一方法，因为它不是多个 methods 之间选择，而是同一个 objective 的 solver。

### 4.4 不要再把 baselines 放进方法里

Baselines 只用于比较，不进入主方法。

这符合你的要求：

> 我们的方法不是 pool，不是从 baselines 中选择。我们的方法是直接求解一个 reconstruction-aware bilevel sensor layout objective。

---

## 5. 理论应该怎么大幅加强

现在论文已有 posterior trace identity、fixed-target monotonicity、validation bound、swap local optimality。 这些可以保留，但要升级成更强的理论体系。

我建议理论 section 改成四个核心 theorem。

---

### Theorem 1：MAP reconstruction closed form and stability

给定 sensor vector (s)，lower-level MAP problem 是 strongly convex，存在唯一解：

[
\hat x_t(s)=A(s)^{-1}b_t(s).
]

如果 (Q+\lambda_L L\succ 0)，则 (A(s)\succ 0)，并且 reconstruction map 对 observation 和 sensor relaxation 是 Lipschitz stable。

这个 theorem 的作用是：说明方法不是黑箱 estimator，而是一个稳定、透明、可分析的 inverse problem。

---

### Theorem 2：posterior trace equals Bayes squared reconstruction risk

当前 Proposition 1 可以升级成 theorem。它说明在线性 Gaussian model 下：

[
\mathbb E
\left[
|x_H-\mathbb E[x_H\mid y_S]|_2^2
\right]
=======

\operatorname{tr}(\Sigma_{H|S}).
]

这个证明 posterior trace 不是随便加的 proxy，而是有 Bayes risk 意义。

当前论文已经写了这个方向。 但下一版要写得更正式，放在 theorem 环境，不要只是 proposition sketch。

---

### Theorem 3：uniform generalization over all size-(k) layouts

这个是最关键的。不要再只对 finite candidate pool 给 bound，而是对 **所有可能的 size-(k) sensor layouts** 给 uniform bound。

令：

[
\mathcal S_k={S\subseteq\mathcal V: |S|=k}.
]

因为：

[
|\mathcal S_k|=\binom{n}{k}
\le
\left(\frac{en}{k}\right)^k,
]

如果 loss bounded in ([0,B])，则以概率至少 (1-\delta)：

[
\sup_{S\in\mathcal S_k}
|R(S)-\hat R_v(S)|
\le
B\sqrt{
\frac{
k\log(en/k)+\log(2/\delta)
}{
2n_v
}
}.
]

如果 (\hat S) 是 empirical objective 的 (\epsilon_{\mathrm{opt}})-近似解：

[
\hat R_v(\hat S)
\le
\min_{|S|=k}\hat R_v(S)+\epsilon_{\mathrm{opt}},
]

那么：

[
R(\hat S)
\le
\min_{|S|=k}R(S)
+
2B\sqrt{
\frac{
k\log(en/k)+\log(2/\delta)
}{
2n_v
}
}
+
\epsilon_{\mathrm{opt}}.
]

这个理论很强。它说：

> TRACE-BiOpt 不只是和一个候选池比较，而是在所有 budget-feasible layouts 上有 finite-sample near-optimality bound，误差来自 validation sample size 和 optimization gap。

这会比当前 finite-candidate bound 强很多，也更像 TR-B。

注意交通时间序列不一定 IID，所以要加 block/effective sample size 版本：

[
n_v \rightarrow n_{\mathrm{eff}}.
]

写成：

> For temporally dependent traffic data, the same expression should be interpreted using independent validation blocks or an effective sample size under mixing assumptions.

---

### Theorem 4：exchange local optimality with computable optimality gap

现在论文有 one-swap local optimality。 可以加强成：

定义 exchange gap：

[
G_1(S)
======

J(S)-
\min_{i\in S, j\notin S}
J(S\setminus{i}\cup{j}).
]

如果 algorithm 停止时 (G_1(S)=0)，则 (S) 是 one-exchange stationary point。

如果做 (p)-swap：

[
G_p(S)=0,
]

则是 (p)-exchange local optimum。

再进一步，如果你愿意引入 approximate submodularity / weak submodularity condition，可以给 approximation bound：

[
J(S)-J(S^\star)
\le
C(\alpha,p)\cdot G_p(S)
]

或者在 benefit function 近似 submodular时给近似保证。这个需要小心，如果暂时不好证明，可以先只给 exchange certificate。

---

## 6. 新论文的理论贡献会变成什么

这样改后，你的 theory 不再是“posterior trace 有点合理”，而是：

1. **透明 MAP reconstruction 有唯一解和稳定性；**
2. **posterior trace 在 Gaussian model 下等于 Bayes squared reconstruction risk；**
3. **TRACE-BiOpt 在所有 size-(k) layouts 上有 uniform validation generalization bound；**
4. **solver 有明确 exchange local optimality certificate；**
5. **CVaR term 提供 robust risk-sensitive design interpretation。**

这个理论厚度就明显更像 TR-B。

---

## 7. 实验上怎么实现“打败所有 baselines”

你需要重新跑实验，不是只改论文。

目标应该是：

> **TRACE-BiOpt beats every pre-registered baseline on mean MAE across all dataset-budget pairs, and no baseline significantly outperforms TRACE-BiOpt under paired tests.**

更强版本：

> **TRACE-BiOpt significantly outperforms the best standalone baseline in most dataset-budget regimes and dominates all standard baselines in every tested regime.**

### 7.1 先锁定 baseline list

建议预注册这些 baseline：

* random mean；
* best random by validation；
* top variance；
* degree；
* coverage；
* observability proxy；
* graph sampling；
* QR/POD；
* greedy A-trace；
* greedy D-logdet；
* scenario average trace；
* scenario CVaR trace；
* RCSS old method；
* old validation-swap TRACE-SL；
* multistart swap；
* swap-from-greedy-A；
* cost-aware / robust coverage baseline, if included.

### 7.2 主表直接比较 best baseline

最重要的表不是列所有数字，而是：

| Dataset | Budget | TRACE-BiOpt | Best baseline | Best baseline name | Delta | p-value | Win count |
| ------- | -----: | ----------: | ------------: | ------------------ | ----: | ------: | --------: |

如果这张表每一行 TRACE-BiOpt 都赢，你就可以很强地写：

> TRACE-BiOpt achieves the lowest mean hidden-state reconstruction MAE among all pre-registered baselines across all tested networks and budgets.

注意是 **pre-registered baselines**，不是世界上所有可能 baselines。

### 7.3 专门攻当前两个薄弱点

当前 external table 暴露了两个问题：

* PeMS7_1026 10%：greedy A 比当前 TRACE-SL 稍好；
* Seattle 10%：TRACE-SL 和 RCSS / multistart 基本 tied。

新方法最先要验证这两个点。
如果 TRACE-BiOpt 在这两个点赢了，论文气质会完全不一样。

### 7.4 加 optimization diagnostics

为了证明不是调参偶然，要加：

* objective descent curve；
* exchange gap curve；
* validation vs test correlation；
* selected sensors map；
* hidden error heatmap；
* posterior trace / CVaR / MAE relation；
* runtime and convergence table；
* sensitivity to (\beta,\gamma,\eta)。

这样“研究内容”会明显增加。

---

## 8. 论文结构应该扩成这样

现在 12 页太短。最终 TR-B draft 建议扩到 22–30 页左右，包括 appendix。

### Section 1 Introduction

强讲：

> sparse traffic sensing is a recoverability-driven network design problem.

贡献写成：

1. bilevel reconstruction-aware sensor layout formulation；
2. transparent MAP reconstruction and robust risk objective；
3. TRACE-BiOpt optimization algorithm；
4. finite-sample layout generalization and exchange optimality theory；
5. multi-network experiments beating all pre-registered baselines。

### Section 2 Literature

扩到 30–45 references。重点放交通 sensor location / observability / OD / sparse TSE，而不是只放 ML。

### Section 3 Bilevel reconstruction-aware layout problem

正式定义：

[
\min_{S:|S|=k} R(S)
]

以及 lower MAP problem。

### Section 4 TRACE-BiOpt method

给：

* objective；
* lower-level closed form；
* continuous relaxation；
* projected optimization；
* rounding；
* exchange refinement；
* convergence / stopping criterion。

### Section 5 Theory

放 theorem：

* MAP uniqueness / stability；
* posterior trace Bayes risk；
* uniform generalization over all layouts；
* approximate optimality with optimization gap；
* exchange local optimality；
* CVaR interpretation。

### Section 6 Experiments

三网络、三预算、全部 baselines。

### Section 7 Results

主表：best baseline comparison。
次表：full baseline matrix。
图：performance curves。

### Section 8 Mechanism analysis

* sensor maps；
* validation-test calibration；
* posterior trace vs MAE；
* why low-budget design works；
* ablations。

### Section 9 Robustness / cost / failure

放 stress tests。

### Section 10 Discussion

边界：

* not universal all possible baselines；
* not global exact MIP unless solved exactly；
* theory depends on bounded/block assumptions；
* but it is a principled bilevel network design method.

---

## 9. 你现在应该怎么安排下一步

我建议下一步不是继续修当前论文，而是先开一个 **v2 method branch**：

### Step 1：定义新唯一方法

写一个 `TRACE_BIOPT_SPEC.md`：

* objective (J(S))；
* lower MAP estimator；
* hyperparameters；
* solver；
* stopping rule；
* no pool, no baseline selection。

### Step 2：实现 TRACE-BiOpt

新增脚本：

* `trace_biopt.py`
* `run_stage15_biopt.py`
* `evaluate_biopt_all_baselines.py`

### Step 3：先跑 current weak points

先只跑：

* PeMS7_1026 10%；
* Seattle 10%；
* PeMS7_228 10%。

如果这些点能赢当前最强 baseline，再扩到全量。

### Step 4：全量 Stage15

跑：

* PeMS7_228；
* PeMS7_1026；
* Seattle；
* 10/20/30%；
* 10 splits；
* all pre-registered baselines。

### Step 5：生成 dominance report

生成：

* `stage15_all_baseline_dominance.csv`
* `best_baseline_delta_table.csv`
* `biopt_theory_contract.md`
* `biopt_claim_contract.md`

### Step 6：重写论文

把 current TRACE-SL pool 方法降级为：

* previous version；
* ablation；
* baseline portfolio；
* supplementary.

主文只讲 TRACE-BiOpt。

---

## 10. 关键提醒：强 claim 应该怎么说

如果新方法真的跑赢所有预注册 baselines，可以写：

> **TRACE-BiOpt achieves the lowest mean held-out hidden-network reconstruction MAE among all pre-registered baselines across all evaluated datasets and budgets.**

如果多数显著，但少数只是 tied，可以写：

> **TRACE-BiOpt is never significantly outperformed by any pre-registered baseline and achieves the best mean MAE in all evaluated dataset-budget regimes.**

如果某个地方没赢，就不要硬说 all。那时可以说：

> **TRACE-BiOpt dominates all standard reviewer-facing baselines and is competitive with the strongest internal exchange-search comparator.**

但你的目标应该是第一种。

---

## 11. 最核心建议

**不要再把主方法写成 pool。**
改成：

> **一个 bilevel robust reconstruction-risk minimization problem + 一个 deterministic solver + 一组 formal generalization / optimality theorems。**

这才像 TR-B。

我会把最终方法定义为：

[
\boxed{
\textbf{TRACE-BiOpt}
====================

\text{Bilevel MAP reconstruction}
+
\text{Huber hidden-state validation risk}
+
\text{posterior uncertainty}
+
\text{CVaR tail risk}
+
\text{projected continuous optimization}
+
\text{deterministic exchange refinement}
}
]

这就是一个唯一方法，不是 pool。
它在理论上可以讲得很强，在实验上也更有机会真正打败所有 baselines。
