---
schema: mcm-card-v1
id: "visualization-86e7a4f375f7-perturb-error"
type: visualization
title: "带误差量的扰动对比柱图"
paper:
  title: "Uncovering the Hidden Momentum: A Data-Science Exploration of Tennis Match Dynamics"
  year: 2024
  problem: C
source:
  pdf: "2024/MCM-C/论文/2403774.pdf"
  pdf_root: null
  sha256: "86e7a4f375f7e1be1a13c0c9d29154cf60a201f86de9974ac083a611f30231e9"
  pdf_pages: [22]
tags: ["网球", "异常处理", "因果卷积"]
score:
  total: 16
  max: 20
  tier: usable
---

# 带误差量的扰动对比柱图

## 入选理由

表达创新或视觉张力。扰动组和基准有共同刻度和误差表示

## 论证任务

定位参数变化时误差是否放大

## 图型与输入

条件作分组柱，误差线采用原始统计口径。

## 视觉编码

条件作分组柱，误差线采用原始统计口径

## 重绘与迁移

使用相同样本和计量单位

## 证据定位

- PDF 第 22 页，图18。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 3 | 22 图18给出图面、图题及正文语境。 |
| 论证表达 | 4 | 扰动组和基准有共同刻度和误差表示 |
| 重绘可行性 | 3 | 条件作分组柱，误差线采用原始统计口径。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 使用相同样本和计量单位 |

总分 **16/20** · 可借鉴
