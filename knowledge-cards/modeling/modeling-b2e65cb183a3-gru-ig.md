---
schema: mcm-card-v1
id: "modeling-b2e65cb183a3-gru-ig"
type: modeling
title: "用分组特征和球员嵌入预测并归因"
paper:
  title: "Momentum Prediction and Core Feature Extraction Based on GRU with Integrated Gradients"
  year: 2024
  problem: C
source:
  pdf: "2024/MCM-C/论文/2409961.pdf"
  pdf_root: null
  sha256: "b2e65cb183a336844825205dea990a883d2605a682725dff39a733680cf829d5"
  pdf_pages: [12, 13, 14, 15, 16, 17, 18, 19]
tags: ["网球", "GRU", "积分梯度"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用分组特征和球员嵌入预测并归因

## 原题与基线

势头预测须兼顾场内时序和运动员差异

## 建模机制与求解

将历史变量和球员嵌入送入 GRU，再以积分梯度分析预测影响

## 验证与局限

提供验证损失、分组误差与异项案例，归因对参照输入敏感

## 迁移到新题

可换为其他带个人差异的连续事件流

## 证据定位

- PDF 第 12–19 页，图8–15、表2–3。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 12–19 图8–15、表2–3可对应假设、机制与结果。 |
| 机制解释力 | 4 | 将历史变量和球员嵌入送入 GRU，再以积分梯度分析预测影响。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 提供验证损失、分组误差与异项案例，归因对参照输入敏感 |
| 可迁移性 | 3 | 可换为其他带个人差异的连续事件流 |

总分 **17/20** · 优先借鉴
