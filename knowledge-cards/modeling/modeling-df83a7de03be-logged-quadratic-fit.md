---
schema: mcm-card-v1
id: "modeling-df83a7de03be-logged-quadratic-fit"
type: modeling
title: "以相关筛选和含对数二次项的回归解释事件统计"
paper:
  title: "The Global Cybersecurity Chessboard: Decoding Crime Distribution and Policy Effectiveness"
  year: 2025
  problem: F
source:
  pdf: "2025/ICM-F/论文/2521039.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "df83a7de03bea0afc64a216c4dd04c4bb8701e98e9c8ba41f0ff62c1bf6df36e"
  pdf_pages: [19, 20, 21]
tags: ["网络安全治理", "政策评估", "非线性回归"]
score:
  total: 17
  max: 20
  tier: priority
---

# 以相关筛选和含对数二次项的回归解释事件统计

## 原题与基线

对宏观指标的非线性提供明确模型

## 建模机制与求解

以 Spearman 及散点探索关系，先线性拟合，再比较模型准则选择对数与二次项，固定其他变量画条件反应

## 验证与局限

有实测预测图可辨误差，需独立检验与影响点分析

## 迁移到新题

可用于治理预测，不把条件曲线直接视为因果

## 证据定位

- PDF 第 19–21 页，第6节、图14至17。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 19–21 第6节、图14至17可对应假设、机制与结果。 |
| 机制解释力 | 4 | 以 Spearman 及散点探索关系，先线性拟合，再比较模型准则选择对数与二次项，固定其他变量画条件反应。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 有实测预测图可辨误差，需独立检验与影响点分析 |
| 可迁移性 | 3 | 可用于治理预测，不把条件曲线直接视为因果 |

总分 **17/20** · 优先借鉴
