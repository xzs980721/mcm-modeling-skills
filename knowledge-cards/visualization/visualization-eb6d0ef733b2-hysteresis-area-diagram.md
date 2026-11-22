---
schema: mcm-card-v1
id: "visualization-eb6d0ef733b2-hysteresis-area-diagram"
type: visualization
title: "用加载与卸载双曲线说明一次冲击的耗能"
paper:
  title: "The Sweet Spot: A Wave Model of Baseball Bats"
  year: 2010
  problem: A
source:
  pdf: "2010/MCM-A/论文/The Sweet Spot - A Wave Model of Baseball Bats.pdf"
  pdf_root: null
  sha256: "eb6d0ef733b22659cf91061b52c50ed725662876221e5f4f0a03449dd8d9773d"
  pdf_pages: [9, 10, 11]
tags: ["滞回", "力位移曲线", "接触"]
score:
  total: 18
  max: 20
  tier: priority
---

# 用加载与卸载双曲线说明一次冲击的耗能

## 论证任务

图 3 在接触力模型处解释两条分支间的面积为何代表能量损失。

## 图型与输入

输入为力–变形加载与卸载样本、最大压缩位置和零力条件。图注给最大压缩量 1.5 cm。

## 视觉编码

两条曲线共用力（kN）与压缩长度（cm）坐标。正文指定压缩走较高分支，膨胀走较低分支。阅读方向靠文字推断，图中没有显著流程箭头。

## 重绘与迁移

新数据按加载阶段区分点，标识分支方向并对两支做数值积分。在零耗散试验中核对曲线重合与面积趋零，再在栏宽内确认双线可区分。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 104 可得期刊印刷页。

- PDF 第 10 页，图 3，力和压缩量、两条分支与积分解释
- PDF 第 11 页，Simulation Results，接触时程中的压缩与回弹差异

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 10 页图注、单位和接触力说明相互对应。 |
| 论证表达 | 4 | 双支之间的面积直接解释能量损失。 |
| 重绘可行性 | 3 | 两支定义与最大变形已知，逐点原始数据未附。 |
| 视觉可读性 | 3 | 双支清楚，方向需配合正文。 |
| 可迁移性 | 4 | 用零耗散退化算例和面积积分核验重绘。 |

总分 **18/20** · 优先借鉴
