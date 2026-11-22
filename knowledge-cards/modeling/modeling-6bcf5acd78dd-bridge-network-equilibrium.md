---
schema: mcm-card-v1
id: "modeling-6bcf5acd78dd-bridge-network-equilibrium"
type: modeling
title: "将断桥冲击投影到道路容量和用户均衡"
paper:
  title: "A Multi-Methodological Framework for Post-Disaster Traffic Optimization and Sustainable Mobility Planning in Baltimore"
  year: 2025
  problem: D
source:
  pdf: "2025/ICM-D/论文/2516219.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "6bcf5acd78dd6cff84bbbf52895464a07b02bff83554831f3051b279274a9a6c"
  pdf_pages: [8, 9, 10, 11, 12, 13, 14]
tags: ["灾后交通", "网络均衡", "公交规划"]
score:
  total: 17
  max: 20
  tier: priority
---

# 将断桥冲击投影到道路容量和用户均衡

## 原题与基线

分析失去桥梁后路网如何重新分配流量

## 建模机制与求解

以道路距离、等级、交通量及通行能力参数构建有向路网，将灾害作为容量情景，按 Wardrop 均衡分配需求并对照道路观测变化

## 验证与局限

文中道路数据提供前后参照，容量假定和事故时段外推仍需检验

## 迁移到新题

可迁移到隧道关闭和施工绕行，另报路段及通行方式

## 证据定位

- PDF 第 8–14 页，道路网络、交通分配和断桥情景。
- PDF 第 12 页，图5。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 8–14 道路网络、交通分配和断桥情景、12 图5可对应假设、机制与结果。 |
| 机制解释力 | 4 | 以道路距离、等级、交通量及通行能力参数构建有向路网，将灾害作为容量情景，按 Wardrop 均衡分配需求并对照道路观测变化。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 文中道路数据提供前后参照，容量假定和事故时段外推仍需检验 |
| 可迁移性 | 3 | 可迁移到隧道关闭和施工绕行，另报路段及通行方式 |

总分 **17/20** · 优先借鉴
