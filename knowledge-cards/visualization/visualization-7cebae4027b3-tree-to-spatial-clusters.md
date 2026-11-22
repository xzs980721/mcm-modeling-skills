---
schema: mcm-card-v1
id: "visualization-7cebae4027b3-tree-to-spatial-clusters"
type: visualization
title: "把聚类树结果回写到空间坐标检查边界"
paper:
  title: "Centroids, Clusters, and Crime: Anchoring the Geographic Profiles of Serial Criminals"
  year: 2010
  problem: B
source:
  pdf: "2010/MCM-B/论文/Centroids, Clusters, and Crime.pdf"
  pdf_root: null
  sha256: "7cebae4027b3464cfdb45ebe7f0c7795c9515ca2be51b68a3ffd8edf045c52f6"
  pdf_pages: [12, 14]
tags: ["地理检验", "空间分析", "历史观测"]
score:
  total: 18
  max: 20
  tier: priority
---

# 把聚类树结果回写到空间坐标检查边界

## 入选理由

表达创新。聚类编号上图，识别由距离树切出的地理分组。

## 论证任务

图8将作者用轮廓系数选择的分组画回位置，便于观察中心、边缘和离群点。

## 图型与输入

平面位置和颜色编码不同聚类，图题说明虚拟竖线的分隔。

## 视觉编码

树本身给出聚合顺序，空间图补几何信息。

## 重绘与迁移

用同一颜色映射连接树叶与散点，抽查近边界点的归属。出现重叠区域时画边界不确定性，不把竖线当真实障碍。

## 证据定位

- PDF 第 12 页（印刷页 140），图7。
- PDF 第 14 页（印刷页 142），图8。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 可在 12 图7、14 图8 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 4 | 聚类编号上图，识别由距离树切出的地理分组。 |
| 重绘可行性 | 3 | 平面位置和颜色编码不同聚类，图题说明虚拟竖线的分隔。 逐点源数据未随图附出。 |
| 视觉可读性 | 3 | 原页主层次可辨，成文尺寸下仍需检查标注。 |
| 可迁移性 | 4 | 用同一颜色映射连接树叶与散点，抽查近边界点的归属。出现重叠区域时画边界不确定性，不把竖线当真实障碍。 |

总分 **18/20** · 优先借鉴
