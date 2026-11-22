---
schema: mcm-card-v1
id: "visualization-7cebae4027b3-merge-distance-dendrogram"
type: visualization
title: "用合并高度树图交代多个空间中心如何产生"
paper:
  title: "Centroids, Clusters, and Crime: Anchoring the Geographic Profiles of Serial Criminals"
  year: 2010
  problem: B
source:
  pdf: "2010/MCM-B/论文/Centroids, Clusters, and Crime.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "7cebae4027b3464cfdb45ebe7f0c7795c9515ca2be51b68a3ffd8edf045c52f6"
  pdf_pages: [12, 13]
tags: ["树状图", "聚类距离", "轮廓系数"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用合并高度树图交代多个空间中心如何产生

## 论证任务

图 7 展示样本由单点逐步聚成簇，正文用它解释多中心不是事先指定的点。

## 图型与输入

每个样本需要匿名 ID 和坐标，依正文用质心距离汇总合并。图中纵轴为网格距离，精确原始坐标未单列。

## 视觉编码

底部是样本 ID，纵向横杠高度对应合并距离，蓝线连接合并路径。没有明确标出选择簇数的切线。

## 重绘与迁移

重画时标记候选切法并配轮廓系数。挑一条枝验证合并距离来自同一空间单位。缩印检查 ID 和候选切线，勿把叶序理解成真实空间顺序。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 128 可得期刊印刷页。

- PDF 第 12 页，图 7，网格距离和样本编号
- PDF 第 13 页，式 (1) 和合并规则，树分支与所选组数

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 12–13 页树图、合并规则和簇数选择过程同页相邻。 |
| 论证表达 | 3 | 能读出合并层次，仍需正文判断切法。 |
| 重绘可行性 | 2 | 有距离和链接方法，缺逐点原始坐标。 |
| 视觉可读性 | 3 | 枝条和刻度大体明确，水印跨部分图面。 |
| 可迁移性 | 4 | 可核查单次合并距离并显示实际切分。 |

总分 **16/20** · 可借鉴
