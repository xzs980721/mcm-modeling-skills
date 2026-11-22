---
schema: mcm-card-v1
id: "visualization-a011d0e27f40-lane-neighbor-and-interchange-geometry"
type: visualization
title: "用小尺度换道与中尺度互通指向车辆位置"
paper:
  title: "The Effects of Self-Driving Cooperating Vehicles on Traffic Capacity of Highways"
  year: 2017
  problem: C
source:
  pdf: "2017/MCM-C/论文/55278.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "a011d0e27f40b59ab532e393ff2acd9f536defd604bf7e4b1593279329fd4788"
  pdf_pages: [11, 12]
tags: ["元胞自动机", "车型条件", "专用道"]
score:
  total: 18
  max: 20
  tier: priority
---

# 用小尺度换道与中尺度互通指向车辆位置

## 入选理由

表达创新或视觉张力。车道示意和道路结构说明同一模型两尺度的允许边。

## 论证任务

核对车距条件和互通入口去向。

## 图型与输入

网格和车辆符号标相邻车道距离，互通图以箭头、彩色路径及汇入线示流向。

## 视觉编码

网格和车辆符号标相邻车道距离，互通图以箭头、彩色路径及汇入线示流向。

## 重绘与迁移

统一箭头语义并验小实例换道及进出口守恒。

## 证据定位

- PDF 第 11 页，图2。
- PDF 第 12 页，图3。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 11 图2、12 图3给出图面、图题及正文语境。 |
| 论证表达 | 4 | 车道示意和道路结构说明同一模型两尺度的允许边。 |
| 重绘可行性 | 4 | 网格和车辆符号标相邻车道距离，互通图以箭头、彩色路径及汇入线示流向。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 统一箭头语义并验小实例换道及进出口守恒。 |

总分 **18/20** · 优先借鉴
