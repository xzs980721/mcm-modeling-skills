---
schema: mcm-card-v1
id: "visualization-db130a3a278d-seed-keyword-topic-bridges"
type: visualization
title: "分三列画主题权重跨关键词往返"
paper:
  title: "Finding Conspirators in the Network via Machine Learning"
  year: 2012
  problem: C
source:
  pdf: "2012/ICM-C/论文/Finding Conspirators in the Network via Machine Learning.pdf"
  pdf_root: null
  sha256: "db130a3a278dd6f4a998e2a6bd812b3925dee31d27ef42a74df9d99d3bc9e86a"
  pdf_pages: [6, 10, 11]
tags: ["网络分析", "小样本", "稳定性"]
score:
  total: 17
  max: 20
  tier: priority
---

# 分三列画主题权重跨关键词往返

## 入选理由

表达创新或视觉张力。左右同为主题而中列为词，使两步扩散方向可见。

## 论证任务

区分已知起点、字典词与有新权重的候选主题。

## 图型与输入

左列为输入主题，中央为共享字典词，右列为更新后的主题。

## 视觉编码

左列为输入主题，中央为共享字典词，右列为更新后的主题。曲线边说明连接，标记展示决定的数据来源。

## 重绘与迁移

用不同颜色与线型区分来回，画少量真实共享词并手算一个两度节点的权重。

## 证据定位

- PDF 第 6 页，表1。
- PDF 第 10 页，图4。
- PDF 第 11 页，式11–13。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 6 表1、10 图4、11 式11–13给出图面、图题及正文语境。 |
| 论证表达 | 4 | 左右同为主题而中列为词，使两步扩散方向可见。 |
| 重绘可行性 | 3 | 左列为输入主题，中央为共享字典词，右列为更新后的主题。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 用不同颜色与线型区分来回，画少量真实共享词并手算一个两度节点的权重。 迁移时按上文检查条件和输入口径。 |

总分 **17/20** · 优先借鉴
