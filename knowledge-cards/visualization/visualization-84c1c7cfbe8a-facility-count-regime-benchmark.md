---
schema: mcm-card-v1
id: "visualization-84c1c7cfbe8a-facility-count-regime-benchmark"
type: visualization
title: "用方法与基线叠点显示设施数量的约束切换"
paper:
  title: "Fewest Repeaters for a Circular Area: Iterative Extremal Optimization Based on Voronoi Diagrams"
  year: 2011
  problem: B
source:
  pdf: "2011/MCM-B/论文/Fewest Repeaters for a Circular Area.pdf"
  pdf_root: null
  sha256: "84c1c7cfbe8a7683afc9ecdfed98abc890aa42280ca7af9e97f3351a7364064f"
  pdf_pages: [13, 14]
tags: ["基线比较", "离散计数", "约束切换"]
score:
  total: 18
  max: 20
  tier: priority
---

# 用方法与基线叠点显示设施数量的约束切换

## 论证任务

图 9 对比规则布点与优化方法，并结合正文说明用户数增大时瓶颈由通信范围转向容量。

## 图型与输入

每个点包含区域固定参数、用户总数、算法标识、有效设施数。涉及两种基线的中心定位。

## 视觉编码

横轴是用户数，纵轴是最少设施数，黑方块表示优化法，红圆点及蓝三角对应两种规则基线。三套点在某些位置很接近。

## 重绘与迁移

在同一空间参数下生成点列，标明容量下界和预计转折。任选小、中、大三个用户规模核查是否满足覆盖和容量，在栏宽保留可分辨的点形。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 130 可得期刊印刷页。

- PDF 第 13 页，不同规模的布点结果，比较量的产生
- PDF 第 14 页，图 9 与 Sensitivity of Parameters，系列映射和转折

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 图 9 的三方法图例、轴与第 14 页趋势段对应。 |
| 论证表达 | 4 | 可以比较点数差距和增速变化。 |
| 重绘可行性 | 3 | 字段和控制场景可用，原始序列未汇总。 |
| 视觉可读性 | 3 | 点线与图例清楚，部分低数量点相近。 |
| 可迁移性 | 4 | 明确大小实例的约束检查。 |

总分 **18/20** · 优先借鉴
