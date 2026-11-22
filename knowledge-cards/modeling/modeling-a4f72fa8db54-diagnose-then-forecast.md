---
schema: mcm-card-v1
id: "modeling-a4f72fa8db54-diagnose-then-forecast"
type: modeling
title: "由平稳性和残差检查选择滚动 ARIMA"
paper:
  title: "Trading Strategy Model Based on Dynamic Programming"
  year: 2022
  problem: C
source:
  pdf: "2022/MCM-C/论文/2203120.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "a4f72fa8db5498d784f1e51cb4bfb7307e15b3b9bf5b7930b7cae0f5028eb403"
  pdf_pages: [6, 7, 8]
tags: ["ARIMA 诊断", "动态规划", "成本敏感性"]
score:
  total: 18
  max: 20
  tier: priority
---

# 由平稳性和残差检查选择滚动 ARIMA

## 原题与基线

两种时序的平稳性及可预测性不同

## 建模机制与求解

差分与滞后诊断选型，通过白噪声检查再生成短周期预测

## 验证与局限

原文有检验与对比轨迹，留出规则和预测区间仍需明确

## 迁移到新题

按时点滚动拟合，保留不差分和持平预测的对照

## 证据定位

- PDF 第 6–7 页，图3、表2–3。
- PDF 第 8 页，图4–5。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 6–7 图3、表2–3、8 图4–5可对应假设、机制与结果。 |
| 机制解释力 | 4 | 差分与滞后诊断选型，通过白噪声检查再生成短周期预测。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 原文有检验与对比轨迹，留出规则和预测区间仍需明确 |
| 可迁移性 | 4 | 按时点滚动拟合，保留不差分和持平预测的对照 |

总分 **18/20** · 优先借鉴
