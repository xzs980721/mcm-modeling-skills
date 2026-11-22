---
schema: mcm-card-v1
id: "visualization-84c1c7cfbe8a-normalized-range-bottleneck"
type: visualization
title: "在同一比例轴比较不同规模下的覆盖瓶颈"
paper:
  title: "Fewest Repeaters for a Circular Area: Iterative Extremal Optimization Based on Voronoi Diagrams"
  year: 2011
  problem: B
source:
  pdf: "2011/MCM-B/论文/Fewest Repeaters for a Circular Area.pdf"
  pdf_root: null
  sha256: "84c1c7cfbe8a7683afc9ecdfed98abc890aa42280ca7af9e97f3351a7364064f"
  pdf_pages: [15]
tags: ["设施布点", "区域覆盖", "网络图"]
score:
  total: 18
  max: 20
  tier: priority
---

# 在同一比例轴比较不同规模下的覆盖瓶颈

## 入选理由

表达创新。同轴展示一组下降和一组几乎平坦的无量纲响应。

## 论证任务

用于说明需求量升高后，改善覆盖半径可能不再减少设施需求。

## 图型与输入

横轴用户通信半径，纵轴为每组设施数除以该组最大值。

## 视觉编码

图注把两颜色的 N 写成同一数，图例和正文区分 1000 与 10000。

## 重绘与迁移

重绘同时保留归一化分母和原始设施数，在短长半径两点对算比例。图题与图例统一。

## 证据定位

- PDF 第 15 页（印刷页 145），图10。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 可在 15 图10 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 4 | 同轴展示一组下降和一组几乎平坦的无量纲响应。 |
| 重绘可行性 | 3 | 横轴用户通信半径，纵轴为每组设施数除以该组最大值。 逐点源数据未随图附出。 |
| 视觉可读性 | 3 | 原页主层次可辨，成文尺寸下仍需检查标注。 |
| 可迁移性 | 4 | 重绘同时保留归一化分母和原始设施数，在短长半径两点对算比例。图题与图例统一。 |

总分 **18/20** · 优先借鉴
