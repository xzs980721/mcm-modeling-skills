---
schema: mcm-card-v1
id: "visualization-b82608352dbb-bearing-to-coordinate-discretization"
type: visualization
title: "由角度误差示意逐步落到可定位的网格"
paper:
  title: "Searching for a Lost Plane: A Probabilistic, Neighborhood-Based Model for Locating Transoceanic Flights"
  year: 2015
  problem: B
source:
  pdf: "2015/MCM-B/论文/39173.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "b82608352dbbe043cd7092dabcaea179ff110677e0a4598d1f78ad33f956b813"
  pdf_pages: [6, 7, 8]
tags: ["搜索救援", "邻域约束", "漏检更新"]
score:
  total: 18
  max: 20
  tier: priority
---

# 由角度误差示意逐步落到可定位的网格

## 入选理由

表达创新或视觉张力。连续坐标、标准差和分区编号各在一步内解释。

## 论证任务

把从航路点定义的候选范围变成可编号区。

## 图型与输入

角度示意突出中心轴和散开距离；格网按横纵坐标和相对原点示意。

## 视觉编码

角度示意突出中心轴和散开距离；格网按横纵坐标和相对原点示意。

## 重绘与迁移

在测试中转回经纬度，检查反算网格位置和索引闭开区间。

## 证据定位

- PDF 第 6 页，图1。
- PDF 第 7 页，图2。
- PDF 第 8 页，图3。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 6 图1、7 图2、8 图3给出图面、图题及正文语境。 |
| 论证表达 | 4 | 连续坐标、标准差和分区编号各在一步内解释。 |
| 重绘可行性 | 4 | 角度示意突出中心轴和散开距离；格网按横纵坐标和相对原点示意。 |
| 视觉可读性 | 3 | 关键图式及标签可辨，缩印下需要复核局部颜色、比例或字重。 |
| 可迁移性 | 3 | 在测试中转回经纬度，检查反算网格位置和索引闭开区间。 迁移时按上文检查条件和输入口径。 |

总分 **18/20** · 优先借鉴
