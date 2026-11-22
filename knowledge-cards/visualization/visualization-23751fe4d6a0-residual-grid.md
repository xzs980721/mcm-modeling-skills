---
schema: mcm-card-v1
id: "visualization-23751fe4d6a0-residual-grid"
type: visualization
title: "把实际密度与带符号残差放在相邻矩阵"
paper:
  title: "Navigating Baltimore’s Growth: A Multi-Layer Network Approach to Urban Transportation Optimization"
  year: 2025
  problem: D
source:
  pdf: "2025/ICM-D/论文/2519935.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "23751fe4d6a0c8075a79839cee87363037f06c5757e398f24391b11414c53e6e"
  pdf_pages: [21]
tags: ["交通网络", "路网韧性", "轨道选线"]
score:
  total: 17
  max: 20
  tier: priority
---

# 把实际密度与带符号残差放在相邻矩阵

## 入选理由

表达创新或视觉张力。区分低密度与模型低估的位置

## 论证任务

模型在哪些格点低估或高估实测密度？

## 图型与输入

将实际量和实际减预测按相同格位排列。

## 视觉编码

将实际量和实际减预测按相同格位排列

## 重绘与迁移

残差色标取零中心，加绝对误差单位

## 证据定位

- PDF 第 21 页，图23。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 21 图23给出图面、图题及正文语境。 |
| 论证表达 | 4 | 区分低密度与模型低估的位置 |
| 重绘可行性 | 3 | 将实际量和实际减预测按相同格位排列。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 残差色标取零中心，加绝对误差单位 |

总分 **17/20** · 优先借鉴
