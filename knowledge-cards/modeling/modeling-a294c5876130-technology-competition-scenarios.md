---
schema: mcm-card-v1
id: "modeling-a294c5876130-technology-competition-scenarios"
type: modeling
title: "把技术替代情景映射到竞争方程的不同参数"
paper:
  title: "Electric Cars as a Widespread Means of Transportation"
  year: 2011
  problem: C
source:
  pdf: "2011/ICM-C/论文/Electric Cars as a Widespread Means of Transportation.pdf"
  pdf_root: null
  sha256: "a294c587613025525ea652c6ddb7c603ef7fba355dda2c98f4c92d8720ea0323"
  pdf_pages: [1, 3, 4, 7, 8, 9]
tags: ["技术扩散", "Lotka–Volterra", "情景分析"]
score:
  total: 17
  max: 20
  tier: priority
---

# 把技术替代情景映射到竞争方程的不同参数

## 原题与基线

预测燃油、插混和纯电车型的保有量，使用表 1 的市场竞争参数构建基准情景。

## 建模机制与求解

三个增长方程各设自身增长率、容量和其他类型占用容量的竞争系数。用登记数据初始化，数值积分后求纯电与燃油曲线相等的年份。基础设施提前改变初值，电价变化改变纯电增长率，油价变化则改竞争项。

## 验证与局限

第 7–9 页报告基准 2035、电价情景 2042 等交叉年份。这是带假定的情景对比，尚未给出演进期样本外检验或需求价格弹性估计。

## 迁移到新题

在扩散历史足以识别竞争参数时使用，留出末段并对照独立 Logistic 外推。检查数值积分对步长不敏感且非负。若交叉年排序取决于先验选值，报告区间。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 164 可得期刊印刷页。

- PDF 第 3–4 页，Methodology、式 (1)–(3)，初始化与数值解
- PDF 第 7–9 页，Population Model Results、图 1–2，情景参数及交叉年

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 4 页方程与第 7–9 页交叉年结果相互支撑。 |
| 机制解释力 | 4 | 不同情景改初值、增长或竞争项，给出排名变化的原因。 |
| 实现可复现性 | 3 | 方程、初始化、求解器与参数支持核心计算。 |
| 验证质量 | 2 | 有定量场景，参数缺弹性验证。 |
| 可迁移性 | 4 | 留出法、步长检验和敏感判据可执行。 |

总分 **17/20** · 优先借鉴
