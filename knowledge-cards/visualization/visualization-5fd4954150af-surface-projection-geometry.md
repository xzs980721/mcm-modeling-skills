---
schema: mcm-card-v1
id: "visualization-5fd4954150af-surface-projection-geometry"
type: visualization
title: "用剖面示意标清漂浮曲面如何变成受光面积"
paper:
  title: "Shedding Light on Marine Pollution"
  year: 2010
  problem: C
source:
  pdf: "2010/ICM-C/论文/Shedding Light on Marine Pollution.pdf"
  pdf_root: null
  sha256: "5fd4954150afd8ce8026d2e748979395af60fe2a424b87804a808b47786a5fcd"
  pdf_pages: [5, 6, 7]
tags: ["剖面图", "有效投影", "浮力"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用剖面示意标清漂浮曲面如何变成受光面积

## 论证任务

图 2 配合低透光推导解释球体浸入水面时，投影计算依赖露出部分。

## 图型与输入

需要球壳半径、水线及照射方向。推导先求有效太阳半径，再对圆形投影面积积分。

## 视觉编码

在同一图里画球壳剖面、水面位置与辅助半径，上方画等效投影圆。线标较细，水线和圆形投影要结合公式辨识。

## 重绘与迁移

画两个不同浸没比例的几何算例，验证满浸投影趋零以及对称条件。用高对比标注区分水线、剖面与积分区，在栏宽检查角度符号。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 164 可得期刊印刷页。

- PDF 第 5 页，Low-Transmittance Model，使用投影的理由
- PDF 第 6 页，图 2 和有效半径式，水线、投影圆和角度
- PDF 第 7 页，面积积分，图面变量怎样进入质量变化

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 5–7 页从投影假设、标注和积分检查。 |
| 论证表达 | 4 | 图面定位水面截线与用于积分的圆。 |
| 重绘可行性 | 3 | 几何关系和变量足够复画同类剖面。 |
| 视觉可读性 | 2 | 水面、虚线投影能辨，标注略小。 |
| 可迁移性 | 4 | 可用满浸退化和对称几何核验。 |

总分 **17/20** · 优先借鉴
