---
schema: mcm-card-v1
id: "visualization-dbfd662724df-space-time-vehicle-structure"
type: visualization
title: "用时空轨迹的连续性诊断拥堵"
paper:
  title: "Freeway Traffic Model Based on Cellular Automata and Monte-Carlo Method"
  year: 2014
  problem: A
source:
  pdf: "2014/MCM-A/论文/25142.pdf"
  pdf_root: null
  sha256: "dbfd662724dfb35cdc44fc60c2a555fcb811afbcd29dfc2a927b1fafb41c85fd"
  pdf_pages: [15]
tags: ["车流", "元胞自动机", "换道"]
score:
  total: 15
  max: 20
  tier: usable
---

# 用时空轨迹的连续性诊断拥堵

## 入选理由

表达创新或视觉张力。多辆车的斜轨迹把快慢和堵点同时呈现。

## 论证任务

说明微观模拟输出可直接按时空组织而不只给总体速度。

## 图型与输入

每条线是车辆位置的时序。

## 视觉编码

每条线是车辆位置的时序。迹线斜率随速度变化，颜色用于区分仿真中的轨迹。图中精确系列定义需与正文、代码核对。

## 重绘与迁移

任选一辆车两个时点重算坡度与单位。绘制跨车道比较时统一时空范围，并清楚标明车道与速度标签。

## 证据定位

- PDF 第 15 页，图3。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 15 图3给出图面、图题及正文语境。 |
| 论证表达 | 3 | 多辆车的斜轨迹把快慢和堵点同时呈现。 |
| 重绘可行性 | 3 | 每条线是车辆位置的时序。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 2 | 原图主结构可辨，细线、标注或水印影响缩印辨读。 |
| 可迁移性 | 3 | 任选一辆车两个时点重算坡度与单位。绘制跨车道比较时统一时空范围，并清楚标明车道与速度标签。 迁移时按上文检查条件和输入口径。 |

总分 **15/20** · 可借鉴
