---
schema: mcm-card-v1
id: "modeling-115a256c8128-gradient-descent-decay-calibration"
type: modeling
title: "用双轴收敛诊断辅助分解率参数估计"
paper:
  title: "Fungal Decomposition Modeling via Stochastic Gradient Descent and Cellular Automata"
  year: 2021
  problem: A
source:
  pdf: "2021/MCM-A/论文/2122025.pdf"
  pdf_root: null
  sha256: "115a256c81280c6b6e6bfa5340ff534f34e42aad3505389327deed42f10068ce"
  pdf_pages: [7, 8, 9, 10, 11]
tags: ["参数拟合", "元胞状态", "空间分解"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用双轴收敛诊断辅助分解率参数估计

## 原题与基线

损失下降和参数收敛速度不必一致

## 建模机制与求解

从性状与环境构建拟合函数，按损失迭代更新参数并观察总误差与单一参数轨迹

## 验证与局限

有拟合诊断和算法表，缺外部数据验证

## 迁移到新题

用独立环境样本检验拟合，比较多初始化和简单回归基线

## 证据定位

- PDF 第 7–11 页，图1、图2、表2、表3和式1–14。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 7–11 图1、图2、表2、表3和式1–14可对应假设、机制与结果。 |
| 机制解释力 | 3 | 从性状与环境构建拟合函数，按损失迭代更新参数并观察总误差与单一参数轨迹。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 有拟合诊断和算法表，缺外部数据验证 |
| 可迁移性 | 4 | 用独立环境样本检验拟合，比较多初始化和简单回归基线 |

总分 **16/20** · 可借鉴
