---
schema: mcm-card-v1
id: "visualization-ea8e578d9fc6-arrival-pulse"
type: visualization
title: "用双峰时间轮廓交代非平稳仿真的输入"
paper:
  title: "Pseudo-Finite Jackson Networks and Simulation: A Roundabout Approach to Traffic Control"
  year: 2009
  problem: A
source:
  pdf: "2009/MCM-A/论文/Pseudo-Finite Jackson Networks and Simulation.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "ea8e578d9fc6436157a20cc75fff393b73f0b1af8b44a41da697b4cb761a9aa5"
  pdf_pages: [15]
tags: ["交通仿真", "排队", "控制策略"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用双峰时间轮廓交代非平稳仿真的输入

## 入选理由

表达创新。把早晚高峰直接编码进到达强度。

## 论证任务

曲线解释稳定网络假设放宽后，如何将不同时间的入口到达缩放。

## 图型与输入

横轴为一天内时间（秒），纵轴为到达率乘子，两个窄峰对应 8 时和 17 时附近。

## 视觉编码

精确采样表未附。

## 重绘与迁移

先核对峰中心、持续区间和全天积分是否和输入总量一致，再与排队输出图共享时区与轴范围。

## 证据定位

- PDF 第 15 页（印刷页 295），图4。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 可在 15 图4 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 3 | 把早晚高峰直接编码进到达强度。 |
| 重绘可行性 | 3 | 横轴为一天内时间（秒），纵轴为到达率乘子，两个窄峰对应 8 时和 17 时附近。 逐点源数据未随图附出。 |
| 视觉可读性 | 3 | 原页主层次可辨，成文尺寸下仍需检查标注。 |
| 可迁移性 | 4 | 先核对峰中心、持续区间和全天积分是否和输入总量一致，再与排队输出图共享时区与轴范围。 |

总分 **17/20** · 优先借鉴
