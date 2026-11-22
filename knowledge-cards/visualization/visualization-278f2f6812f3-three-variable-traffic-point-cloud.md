---
schema: mcm-card-v1
id: "visualization-278f2f6812f3-three-variable-traffic-point-cloud"
type: visualization
title: "以三维点云呈现流量、速度和车辆占比的联合关系"
paper:
  title: "Highway Traffic Flow Model with Self-Driving Vehicles Based on Cellular Automata"
  year: 2017
  problem: C
source:
  pdf: "2017/MCM-C/论文/55585.pdf"
  pdf_root: null
  sha256: "278f2f6812f35e7cb88c8d5006ab37eaf45f59a61ce62ee4c7079db4adeffe53"
  pdf_pages: [16]
tags: ["混合车辆", "状态规则", "多维交通表现"]
score:
  total: 17
  max: 20
  tier: priority
---

# 以三维点云呈现流量、速度和车辆占比的联合关系

## 入选理由

表达创新或视觉张力。三变量联动的整体形状直观，便于定位不均匀的折面变化。

## 论证任务

先探索混合比条件下的流量—速度范围。

## 图型与输入

三轴为车流量、比例和平均速度，点云以颜色显示相应连续量，配色条。

## 视觉编码

三轴为车流量、比例和平均速度，点云以颜色显示相应连续量，配色条。

## 重绘与迁移

各轴明确单位和色映射，添加关键比率切片验证三维遮挡。

## 证据定位

- PDF 第 16 页，图12。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 16 图12给出图面、图题及正文语境。 |
| 论证表达 | 4 | 三变量联动的整体形状直观，便于定位不均匀的折面变化。 |
| 重绘可行性 | 3 | 三轴为车流量、比例和平均速度，点云以颜色显示相应连续量，配色条。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 各轴明确单位和色映射，添加关键比率切片验证三维遮挡。 |

总分 **17/20** · 优先借鉴
