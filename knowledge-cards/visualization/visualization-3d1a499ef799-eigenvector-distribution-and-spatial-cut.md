---
schema: mcm-card-v1
id: "visualization-3d1a499ef799-eigenvector-distribution-and-spatial-cut"
type: visualization
title: "用分布、排序折线和三维布局对照谱划分"
paper:
  title: "Getting a Move On When the Louvre’s Bombed"
  year: 2019
  problem: D
source:
  pdf: "2019/ICM-D/论文/1908810.pdf"
  pdf_root: null
  sha256: "3d1a499ef799692e6b66b7c6fdfe82a0659edd9ff2d204c7ceb81cb33cf1aa40"
  pdf_pages: [7]
tags: ["谱划分", "人群排队", "拥堵模拟"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用分布、排序折线和三维布局对照谱划分

## 入选理由

表达创新或视觉张力。零阈值可在排序值上查看，再对应到地图里的两群。

## 论证任务

检查少割边的分区依据。

## 图型与输入

图2为Fiedler向量直方图和排序，图3以点大小区分分区。

## 视觉编码

图2为Fiedler向量直方图和排序，图3以点大小区分分区。

## 重绘与迁移

从数值数组和非敏感几何生成三个视图，用同一键传递节点颜色或大小。

## 证据定位

- PDF 第 7 页，图2和图3。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 7 图2和图3给出图面、图题及正文语境。 |
| 论证表达 | 4 | 零阈值可在排序值上查看，再对应到地图里的两群。 |
| 重绘可行性 | 3 | 图2为Fiedler向量直方图和排序，图3以点大小区分分区。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 从数值数组和非敏感几何生成三个视图，用同一键传递节点颜色或大小。 |

总分 **17/20** · 优先借鉴
