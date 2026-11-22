---
schema: mcm-card-v1
id: "modeling-7cebae4027b3-multi-centroid-spatial-validation"
type: modeling
title: "用逐步聚类检验单中心空间假设的适用性"
paper:
  title: "Centroids, Clusters, and Crime: Anchoring the Geographic Profiles of Serial Criminals"
  year: 2010
  problem: B
source:
  pdf: "2010/MCM-B/论文/Centroids, Clusters, and Crime.pdf"
  pdf_root: null
  sha256: "7cebae4027b3464cfdb45ebe7f0c7795c9515ca2be51b68a3ffd8edf045c52f6"
  pdf_pages: [1, 7, 10, 11, 12, 13, 14, 16]
tags: ["层次聚类", "多中心", "时序留出"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用逐步聚类检验单中心空间假设的适用性

## 原题与基线

论文对历史空间事件序列做回顾检验，先以全体历史点的单质心代表中心。

## 建模机制与求解

用欧氏距离和质心链接生成层次树，以平均轮廓系数选择候选组数。每组重新估中心并组合结果。检验以早期事件建模并对照末次事件，观察单中心是否被少数离群记录拉偏。

## 验证与局限

三个案例中聚类能区分局部簇和离群点。有些原始位置由发表图回读，样本少且无跨地区外部验证，结论依赖平面距离和人为指定组数范围。

## 迁移到新题

迁移到历史服务报修或地理生态观察记录，选时间分界点并比较单中心与聚类在留出期的误差。按区域尺度更换距离，若少量扰动导致簇不稳定或无预测改进，保留简单基线。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 128 可得期刊印刷页。

- PDF 第 7、10–11 页，Single Anchor Point 与结果分析，单中心对照与留出过程
- PDF 第 12–14 页，Multiple Anchor Points、图 7–8 和式 (1)，聚类、轮廓系数以及比较
- PDF 第 16 页，结果与讨论，个案差异

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 7、11–14 页有基线、聚类步骤、系数与不同案例。 |
| 机制解释力 | 4 | 多个中心绕开单中心受跨簇点拉偏的问题。 |
| 实现可复现性 | 2 | 部分数据来自图回读且精度受限。 |
| 验证质量 | 2 | 留出末次事件有实证逻辑，三案例不足以支持跨区结论。 |
| 可迁移性 | 4 | 可用匿名服务数据留时段比较稳定性与误差。 |

总分 **16/20** · 可借鉴
