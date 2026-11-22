# 真实摘录（exemplars）

从语料里摘出的真实句子，用来给"长这样"的样例。**摘录的作用是校准语气和结构，不是模板**——照抄句式会变成另一种套路，评委看得出来。

目前样本：2024-ICM-E（控制号 2413552）、2024-C-2406176、2021-B-2104673、2022-A-2207343、2023-B-2300136。**待扩充到每题 2–3 篇。**

---

## E1｜归因式论证（问题特性 → 模型特性）

> "The model results indicate that **considering spatial heterogeneity** allows for **more accurate predictions** of insurance claim amounts, offering insurance companies a scientific risk assessment tool."

**结构**：因为题里有某个结构特点 → 所以需要某类方法 → 这个方法带来什么。

**可套用**：
- 因为〔本题的结构特点〕，〔某类方法〕才能〔解决的具体困难〕。
- 若忽略〔该特点〕，〔会出的错：偏差方向或结论翻转〕。

**这类句子是"建模过程"维度拿 7 分以上的关键**，一句话顶三段方法介绍。

---

## E2｜数据驱动的归因（用数据特征说话）

> "**Given the high dimensionality of our climatic dataset, comprising 96 variables**, we employed Principal Component Analysis (PCA) to distill this complexity into a more manageable form. The goal was to **reduce these variables to four principal components**, capturing the most significant variance in the dataset."

**结构**：数据的客观特征（96 维）→ 方法（PCA）→ 目标（降到 4 个成分）→ 保留什么（most significant variance）。

**为什么有效**：数字锚定了必要性。不说"数据复杂"，说"96 个变量"。

---

## E3｜摘要开头（背景式，不是结论式）

> "In the context of global climate change, the increasing frequency of extreme weather events poses significant challenges to the property insurance industry. This study presents a comprehensive analytical framework addressing the sustainability of the property insurance sector under extreme weather conditions."

**结构**：背景一句 → 本文做什么（一句）。

**注意**：这是 O 奖摘要的常见开头——**先立场景，不先甩结论**。近五年摘要首句是背景式的占 39–56%，结果式只有 5–6%。所以"第一句必须给结论"是错的。

---

## E4｜检验段（诚实交代 + 结论稳定）

> "In this section, we conduct a robustness check of our model. **Given that our model involves relatively few parameters**, with only some hyperparameters manually adjusted in the entropy weighting method, we perform an ablation study on these parameters. … We observe that **despite changes in the model's parameters, the trend of losses … continues to fluctuate and rise**. Moreover, the beneficial impact of community interventions consistently exceeds that of individual property owners. **This indicates that our model is sufficiently robust**, demonstrating consistent performance under different parameter settings."

**结构**：交代模型有几个参数（诚实）→ 扰动哪些 → 观察到什么（趋势不变）→ 结论（足够稳健）。

**关键**：全部只用一段 + 一张图。**检验的分量在"界定范围"，不在篇幅。**

---

## E5｜优劣势写法（具体到机制）

> "**Spatial Heterogeneity Consideration:** The model incorporates spatial heterogeneity through the MGWR …, **enhancing the precision of predictions** and **providing insurance companies with a scientific tool for risk assessment**."

**结构**：黑体标签（做对了什么）→ 机制 → 带来什么好处（对谁有用）。

**反例对照**：不要写"模型准确性较高"。要写"通过 X 机制，在 Y 方面更准，对 Z 有用"。

---

## E6｜"数据缺什么"也能当选择理由（2021-B-2104673）

> "**Considering the lack of spatial distribution data** of fire field, we use **cellular automata model** to sim-…"

**结构**：先承认数据缺口 → 缺口决定了方法（元胞自动机不需要连续空间数据）。这类论证在 B 题很常见：**不是"这个方法好"，而是"只有这类方法能用现有数据做"**。

---

## E7｜用指标可得性做替代论证（2023-B-2300136）

> "When considering wildlife numbers and biodiversity, **we use the number/diversity of mammals as an indicator** for all wildlife. Data on large mammals…"

**结构**：目标量不可直接观测 → 选一个可观测的代理指标 → 说明数据来源。这是假设章里最该出现的一种论证：**承认替代，并交代替代的依据**。

---

## E8｜把维度问题说成选择理由（2024-C-2406176）

> "**Given the multitude of performance indicators** for a player, we use a **Factor Analysis Model** to distill key factors that better represent the player's technic-…"

**结构**：指标太多 → 降维 → 目的是"更能代表"。这是 C 题的典型归因：**用数据的规模特征逼出方法**。

---

## E9｜用场地条件筛样本（2022-A-2207343）

> "**Due to the small undulating terrain in this area**, we selected 9 road sections with **slope angles below 1°**…"

**结构**：物理条件 → 筛选标准 → 具体数字（9 段、≤1°）。**注意它把筛选阈值写成了数**——评委能复核，这就是"可复现"的具体样子。

---

## 反面句式（合成示例，非语料原句）

> "Due to time constraints, some further analysis has not been carried out, which can be improved in future work."

这类句子在 O 奖论文里几乎见不到，但它是最常见的失败写法：把局限写成免责声明，读者得不到任何信息。**替代写法**：指出具体是哪一项没做、它会让哪条结论不可靠、如果要做需要什么数据。判断标准是"换一个团队能不能照着补上"。

---

## 使用方式

| 场景 | 怎么用 |
|---|---|
| brief 模式 | 把 E1、E3 作为"论证句"和"摘要开头"的示例贴进 `AWARD_BRIEF.md` |
| review 模式 | 指出某段缺归因时，附 E1 作为"应该有的样子" |
| 反例 | 不要把 E4 当成"检验只要一段就够"——它够是因为它界定了范围，不是因为短 |

## 待补

- 每题各选 2–3 篇代表（A 题机理、B 题优化、C 题数据、D 题网络、E 题评价、F 题政策），各摘 2 句。
- 全文文本现已导出（`data/text/`），补摘录直接从中挑句，不需要再解析 PDF。
