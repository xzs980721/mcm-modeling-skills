---
schema: mcm-card-v1
id: "visualization-ea8e578d9fc6-random-policy-benchmark"
type: visualization
title: "把随机控制样本和基准水平画在一起"
paper:
  title: "Pseudo-Finite Jackson Networks and Simulation: A Roundabout Approach to Traffic Control"
  year: 2009
  problem: A
source:
  pdf: "2009/MCM-A/论文/Pseudo-Finite Jackson Networks and Simulation.pdf"
  pdf_root: null
  sha256: "ea8e578d9fc6436157a20cc75fff393b73f0b1af8b44a41da697b4cb761a9aa5"
  pdf_pages: [21]
tags: ["交通仿真", "排队", "控制策略"]
score:
  total: 17
  max: 20
  tier: priority
---

# 把随机控制样本和基准水平画在一起

## 入选理由

表达创新。在候选散点分布中显示已知控制规则的位置。

## 论证任务

100 次随机信号矩阵试验的平均通过时间用来判断让行是否只是偶然占优。

## 图型与输入

横轴试验序列，纵轴平均在系统时间。

## 视觉编码

散点对应随机样本，水平参照线标最小、平均和中位试验值。让行规则的时间由第 18 页正文另给，精确信号矩阵未附。

## 重绘与迁移

重画时保存每个方案的重复随机试验并明确一点评价口径，重复生成点检查相对参考线的次序。

## 证据定位

- PDF 第 21 页（印刷页 301），图7。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 可在 21 图7 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 3 | 在候选散点分布中显示已知控制规则的位置。 |
| 重绘可行性 | 3 | 横轴试验序列，纵轴平均在系统时间。 逐点源数据未随图附出。 |
| 视觉可读性 | 3 | 原页主层次可辨，成文尺寸下仍需检查标注。 |
| 可迁移性 | 4 | 重画时保存每个方案的重复随机试验并明确一点评价口径，重复生成点检查相对参考线的次序。 |

总分 **17/20** · 优先借鉴
