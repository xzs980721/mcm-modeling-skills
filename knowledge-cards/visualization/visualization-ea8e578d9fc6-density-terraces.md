---
schema: mcm-card-v1
id: "visualization-ea8e578d9fc6-density-terraces"
type: visualization
title: "按入口分层画时间密度与管制对照"
paper:
  title: "Pseudo-Finite Jackson Networks and Simulation: A Roundabout Approach to Traffic Control"
  year: 2009
  problem: A
source:
  pdf: "2009/MCM-A/论文/Pseudo-Finite Jackson Networks and Simulation.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "ea8e578d9fc6436157a20cc75fff393b73f0b1af8b44a41da697b4cb761a9aa5"
  pdf_pages: [19, 20]
tags: ["交通仿真", "排队", "控制策略"]
score:
  total: 17
  max: 20
  tier: priority
---

# 按入口分层画时间密度与管制对照

## 入选理由

表达创新。在同一视图中区分入口高峰与交通策略。

## 论证任务

图 5 较量同类流量下让行和非让行。图 6 改变有较大流量的支路数量，用同类图解释特定入口的积压。

## 图型与输入

每入口、时刻与车数构成一层沿时间走的图，配相同空间透视。

## 视觉编码

高度表达车数，前后层是不同队列，峰后衰退可对应高峰时段。跨图高度和遮挡须看刻度。

## 重绘与迁移

以二维共轴小多图作为缩印备选。先人工重建一个入口短窗，核对最高积压按同一车辆定义计数。

## 证据定位

- PDF 第 19 页（印刷页 299），图5。
- PDF 第 20 页（印刷页 300），图6。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 可在 19 图5、20 图6 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 4 | 在同一视图中区分入口高峰与交通策略。 |
| 重绘可行性 | 3 | 每入口、时刻与车数构成一层沿时间走的图，配相同空间透视。 逐点源数据未随图附出。 |
| 视觉可读性 | 2 | 小图例、细线或水印限制缩印，建议逐页放大。 |
| 可迁移性 | 4 | 以二维共轴小多图作为缩印备选。先人工重建一个入口短窗，核对最高积压按同一车辆定义计数。 |

总分 **17/20** · 优先借鉴
