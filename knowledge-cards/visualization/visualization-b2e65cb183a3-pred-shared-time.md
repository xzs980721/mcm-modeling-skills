---
schema: mcm-card-v1
id: "visualization-b2e65cb183a3-pred-shared-time"
type: visualization
title: "真实状态与预测概率上下对齐"
paper:
  title: "Momentum Prediction and Core Feature Extraction Based on GRU with Integrated Gradients"
  year: 2024
  problem: C
source:
  pdf: "2024/MCM-C/论文/2409961.pdf"
  pdf_root: null
  sha256: "b2e65cb183a336844825205dea990a883d2605a682725dff39a733680cf829d5"
  pdf_pages: [18, 19]
tags: ["网球", "GRU", "积分梯度"]
score:
  total: 17
  max: 20
  tier: priority
---

# 真实状态与预测概率上下对齐

## 入选理由

表达创新或视觉张力。将形态和预测误差定位到同一比赛节点

## 论证任务

检查状态识别跨项目转移

## 图型与输入

上层画状态区域，下层按共同时间尺度叠预测和参照。

## 视觉编码

上层画状态区域，下层按共同时间尺度叠预测和参照

## 重绘与迁移

标不同系统的事件尺度

## 证据定位

- PDF 第 18 页，图13。
- PDF 第 19 页，图15。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 18 图13、19 图15给出图面、图题及正文语境。 |
| 论证表达 | 4 | 将形态和预测误差定位到同一比赛节点 |
| 重绘可行性 | 3 | 上层画状态区域，下层按共同时间尺度叠预测和参照。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 标不同系统的事件尺度 |

总分 **17/20** · 优先借鉴
