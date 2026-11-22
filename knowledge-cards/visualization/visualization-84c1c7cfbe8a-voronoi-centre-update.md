---
schema: mcm-card-v1
id: "visualization-84c1c7cfbe8a-voronoi-centre-update"
type: visualization
title: "用运动箭头和两层几何显示迭代更新"
paper:
  title: "Fewest Repeaters for a Circular Area: Iterative Extremal Optimization Based on Voronoi Diagrams"
  year: 2011
  problem: B
source:
  pdf: "2011/MCM-B/论文/Fewest Repeaters for a Circular Area.pdf"
  pdf_root: null
  sha256: "84c1c7cfbe8a7683afc9ecdfed98abc890aa42280ca7af9e97f3351a7364064f"
  pdf_pages: [11]
tags: ["设施布点", "区域覆盖", "网络图"]
score:
  total: 18
  max: 20
  tier: priority
---

# 用运动箭头和两层几何显示迭代更新

## 入选理由

表达创新。把中心更新和可行性区域同时显示。

## 论证任务

解释为何站点会从起始位置移向对应包围圆中心。

## 图型与输入

原点用加号，新点用星号，箭头表示一次定位方向。

## 视觉编码

边界为红实线，包围圆用绿虚线，圆心另编码。

## 重绘与迁移

选一个 Voronoi 区重算包围圆并检查更新方向。图区需用同等比例，否则距离关系易误读。

## 证据定位

- PDF 第 11 页（印刷页 141），图3。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 可在 11 图3 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 4 | 把中心更新和可行性区域同时显示。 |
| 重绘可行性 | 3 | 原点用加号，新点用星号，箭头表示一次定位方向。 逐点源数据未随图附出。 |
| 视觉可读性 | 3 | 原页主层次可辨，成文尺寸下仍需检查标注。 |
| 可迁移性 | 4 | 选一个 Voronoi 区重算包围圆并检查更新方向。图区需用同等比例，否则距离关系易误读。 |

总分 **18/20** · 优先借鉴
