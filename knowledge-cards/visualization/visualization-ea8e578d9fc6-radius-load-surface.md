---
schema: mcm-card-v1
id: "visualization-ea8e578d9fc6-radius-load-surface"
type: visualization
title: "用二维输入网格显示设施规模在过载区的作用"
paper:
  title: "Pseudo-Finite Jackson Networks and Simulation: A Roundabout Approach to Traffic Control"
  year: 2009
  problem: A
source:
  pdf: "2009/MCM-A/论文/Pseudo-Finite Jackson Networks and Simulation.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "ea8e578d9fc6436157a20cc75fff393b73f0b1af8b44a41da697b4cb761a9aa5"
  pdf_pages: [22]
tags: ["交通仿真", "排队", "控制策略"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用二维输入网格显示设施规模在过载区的作用

## 入选理由

表达创新与视觉张力。半径和总到达量并排进入一个响应曲面。

## 论证任务

比较规模对平均在系统时间的影响为何随负荷改变。

## 图型与输入

横向两个变量为总输入（辆/小时）和半径（米），竖向为平均在系统时间。正文以秒讨论该指标。

## 视觉编码

网格面和标出的点让读者对照低负荷平区与高负荷抬升。正文指出在约 3000 辆/小时以上，半径与平均时间的关系变得不规则。

## 重绘与迁移

在新图增加等值线或平面切片，抽两种需求水平检查半径变化方向，注明服务水平和重复抽样误差。

## 证据定位

- PDF 第 22 页（印刷页 302），图8。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 可在 22 图8 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 4 | 半径和总到达量并排进入一个响应曲面。 |
| 重绘可行性 | 3 | 横向两个变量为总输入（辆/小时）和半径（米），竖向为平均在系统时间。正文以秒讨论该指标。 逐点源数据未随图附出。 |
| 视觉可读性 | 2 | 小图例、细线或水印限制缩印，建议逐页放大。 |
| 可迁移性 | 4 | 在新图增加等值线或平面切片，抽两种需求水平检查半径变化方向，注明服务水平和重复抽样误差。 |

总分 **17/20** · 优先借鉴
