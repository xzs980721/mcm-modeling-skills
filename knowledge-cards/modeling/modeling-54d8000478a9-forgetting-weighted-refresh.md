---
schema: mcm-card-v1
id: "modeling-54d8000478a9-forgetting-weighted-refresh"
type: modeling
title: "以遗忘权重分批更新事件判别模型"
paper:
  title: "Strategies to Analyze the Invasion of the Vespa Mandarinia: A Comprehensive Three-dimensional Model"
  year: 2021
  problem: C
source:
  pdf: "2021/MCM-C/论文/2107815.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "54d8000478a91f6570553566e8ed2f5a809be0d5c07a11ffefdc13a7845b6d52"
  pdf_pages: [18, 19, 20]
tags: ["多模态评分", "增量更新", "事件优先级"]
score:
  total: 18
  max: 20
  tier: priority
---

# 以遗忘权重分批更新事件判别模型

## 原题与基线

新事件进入后，旧报告对当前判断的贡献可能过时

## 建模机制与求解

按更新时间及事件条件计算遗忘量，并增量更新文本、图像和综合标签

## 验证与局限

用刷新前后拟合与地点分布核对，缺少多时点独立对照

## 迁移到新题

用滚动留出比较恒定权重、遗忘更新和完全重训

## 证据定位

- PDF 第 18–20 页，图6-1–6-2及表6-1–6-4。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 18–20 图6-1–6-2及表6-1–6-4可对应假设、机制与结果。 |
| 机制解释力 | 4 | 按更新时间及事件条件计算遗忘量，并增量更新文本、图像和综合标签。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 用刷新前后拟合与地点分布核对，缺少多时点独立对照 |
| 可迁移性 | 4 | 用滚动留出比较恒定权重、遗忘更新和完全重训 |

总分 **18/20** · 优先借鉴
