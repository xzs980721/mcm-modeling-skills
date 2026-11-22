---
schema: mcm-card-v1
id: "visualization-84c1c7cfbe8a-reachable-sets-network"
type: visualization
title: "以两类覆盖距离和有向连边说明可达定义"
paper:
  title: "Fewest Repeaters for a Circular Area: Iterative Extremal Optimization Based on Voronoi Diagrams"
  year: 2011
  problem: B
source:
  pdf: "2011/MCM-B/论文/Fewest Repeaters for a Circular Area.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "84c1c7cfbe8a7683afc9ecdfed98abc890aa42280ca7af9e97f3351a7364064f"
  pdf_pages: [4]
tags: ["设施布点", "区域覆盖", "网络图"]
score:
  total: 16
  max: 20
  tier: usable
---

# 以两类覆盖距离和有向连边说明可达定义

## 入选理由

表达创新。局部实例把用户直达与经由中转区分。

## 论证任务

为可达率试验定义图中哪些中继可由给定用户使用。

## 图型与输入

以用户点为中心画半径 r 的圆，用标记画站点和连接方向。

## 视觉编码

其他边由站点之间距离与路由关系决定，不能从线长推断功率。

## 重绘与迁移

给新图两个边界算例，用节点/边表核对直接边与经中转路径是否区分。

## 证据定位

- PDF 第 4 页（印刷页 134），图1。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 3 | 可在 4 图1 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 3 | 局部实例把用户直达与经由中转区分。 |
| 重绘可行性 | 3 | 以用户点为中心画半径 r 的圆，用标记画站点和连接方向。 逐点源数据未随图附出。 |
| 视觉可读性 | 3 | 原页主层次可辨，成文尺寸下仍需检查标注。 |
| 可迁移性 | 4 | 给新图两个边界算例，用节点/边表核对直接边与经中转路径是否区分。 |

总分 **16/20** · 可借鉴
