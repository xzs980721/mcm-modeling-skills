---
schema: mcm-card-v1
id: "visualization-bb570f1f5467-density-subdivision-story"
type: visualization
title: "从人口斑块到局部分区展示预分割"
paper:
  title: "Applying Voronoi Diagrams to the Redistricting Problem"
  year: 2007
  problem: A
source:
  pdf: "2007/MCM-A/论文/Applying Voronoi Diagrams to the Redistricting Problem.pdf"
  pdf_root: null
  sha256: "bb570f1f5467ae8a97a8b81c3addf813edbf65aa1fb93eeaf2ef2e5430646679"
  pdf_pages: [10, 13]
tags: ["Voronoi", "地理分区", "人口栅格"]
score:
  total: 17
  max: 20
  tier: priority
---

# 从人口斑块到局部分区展示预分割

## 入选理由

表达创新或视觉张力。可直接查看预细分前后的边界改变

## 论证任务

密度不均时先切大范围再生成小区有何作用？

## 图型与输入

三格保持人口斑块位置，叠加大边界和次级区，纽约地图给对应前后。

## 视觉编码

三格保持人口斑块位置，叠加大边界和次级区，纽约地图给对应前后

## 重绘与迁移

固定州范围和颜色复用，画出细分边界

## 证据定位

- PDF 第 10 页，图3 三面板。
- PDF 第 13 页，图5 a–b。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 10 图3 三面板、13 图5 a–b给出图面、图题及正文语境。 |
| 论证表达 | 4 | 可直接查看预细分前后的边界改变 |
| 重绘可行性 | 3 | 三格保持人口斑块位置，叠加大边界和次级区，纽约地图给对应前后。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 固定州范围和颜色复用，画出细分边界 |

总分 **17/20** · 优先借鉴
