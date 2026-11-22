---
schema: mcm-card-v1
id: "visualization-115a256c8128-parameter-model-dependency-map"
type: visualization
title: "把可估参数和子模型依赖放在同一流程图"
paper:
  title: "Fungal Decomposition Modeling via Stochastic Gradient Descent and Cellular Automata"
  year: 2021
  problem: A
source:
  pdf: "2021/MCM-A/论文/2122025.pdf"
  pdf_root: null
  sha256: "115a256c81280c6b6e6bfa5340ff534f34e42aad3505389327deed42f10068ce"
  pdf_pages: [17]
tags: ["参数拟合", "元胞状态", "空间分解"]
score:
  total: 16
  max: 20
  tier: usable
---

# 把可估参数和子模型依赖放在同一流程图

## 入选理由

表达创新或视觉张力。多阶段的计算依赖能够逐节点查询

## 论证任务

说明参数从何处进入及输出如何重用

## 图型与输入

用各列色块和箭头连接输入、子模型与结果。

## 视觉编码

用各列色块和箭头连接输入、子模型与结果

## 重绘与迁移

在箭头写传递对象，标过程和数据的区别并查循环依赖

## 证据定位

- PDF 第 17 页，图5。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 3 | 17 图5给出图面、图题及正文语境。 |
| 论证表达 | 4 | 多阶段的计算依赖能够逐节点查询 |
| 重绘可行性 | 3 | 用各列色块和箭头连接输入、子模型与结果。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 在箭头写传递对象，标过程和数据的区别并查循环依赖 |

总分 **16/20** · 可借鉴
