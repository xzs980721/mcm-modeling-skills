---
schema: mcm-card-v1
id: "visualization-115a256c8128-convergence-loss-and-parameter"
type: visualization
title: "用双轴并排对应同一次迭代的损失和参数"
paper:
  title: "Fungal Decomposition Modeling via Stochastic Gradient Descent and Cellular Automata"
  year: 2021
  problem: A
source:
  pdf: "2021/MCM-A/论文/2122025.pdf"
  pdf_root: null
  sha256: "115a256c81280c6b6e6bfa5340ff534f34e42aad3505389327deed42f10068ce"
  pdf_pages: [10, 11]
tags: ["参数拟合", "元胞状态", "空间分解"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用双轴并排对应同一次迭代的损失和参数

## 入选理由

表达创新或视觉张力。单看平稳参数可能掩盖有噪损失

## 论证任务

检验优化是否趋稳

## 图型与输入

共同迭代号，左右轴分别为蓝色损失与橙色参数。

## 视觉编码

共同迭代号，左右轴分别为蓝色损失与橙色参数

## 重绘与迁移

匹配颜色与轴标签，增加滑动中位数，复验随机批次

## 证据定位

- PDF 第 10 页，表3。
- PDF 第 11 页，图2。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 10 表3、11 图2给出图面、图题及正文语境。 |
| 论证表达 | 4 | 单看平稳参数可能掩盖有噪损失 |
| 重绘可行性 | 3 | 共同迭代号，左右轴分别为蓝色损失与橙色参数。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 匹配颜色与轴标签，增加滑动中位数，复验随机批次 |

总分 **17/20** · 优先借鉴
