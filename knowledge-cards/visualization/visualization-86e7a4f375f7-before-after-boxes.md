---
schema: mcm-card-v1
id: "visualization-86e7a4f375f7-before-after-boxes"
type: visualization
title: "同轴箱线图排查异常修整"
paper:
  title: "Uncovering the Hidden Momentum: A Data-Science Exploration of Tennis Match Dynamics"
  year: 2024
  problem: C
source:
  pdf: "2024/MCM-C/论文/2403774.pdf"
  pdf_root: null
  sha256: "86e7a4f375f7e1be1a13c0c9d29154cf60a201f86de9974ac083a611f30231e9"
  pdf_pages: [5]
tags: ["网球", "异常处理", "因果卷积"]
score:
  total: 17
  max: 20
  tier: priority
---

# 同轴箱线图排查异常修整

## 入选理由

表达创新或视觉张力。并列处理前后让缩尾或去除的效果可查

## 论证任务

定位哪些变量变化明显

## 图型与输入

按变量画水平箱线，在相同尺度比较两个版本。

## 视觉编码

按变量画水平箱线，在相同尺度比较两个版本

## 重绘与迁移

标明处理阈值和异常点是否从样本删除

## 证据定位

- PDF 第 5 页，图1、图2。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 5 图1、图2给出图面、图题及正文语境。 |
| 论证表达 | 4 | 并列处理前后让缩尾或去除的效果可查 |
| 重绘可行性 | 3 | 按变量画水平箱线，在相同尺度比较两个版本。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 标明处理阈值和异常点是否从样本删除 |

总分 **17/20** · 优先借鉴
