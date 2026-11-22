---
schema: mcm-card-v1
id: "modeling-7fd2005c3d91-topology-dynamics-centrality"
type: modeling
title: "并行检查食物网拓扑和动力学稳定性"
paper:
  title: "Forests and Agriculture in Harmony: How to Maintain Ecosystem Stability During the Transition to Organic Farming"
  year: 2025
  problem: E
source:
  pdf: "2025/ICM-E/论文/2502355.pdf"
  pdf_root: null
  sha256: "7fd2005c3d91b23a6451ad148cc1ec1b16c15ec7f6a264f1e49145ea096b22d8"
  pdf_pages: [15, 16, 17, 18, 19, 20]
tags: ["农业生态", "食物网", "动态干预"]
score:
  total: 17
  max: 20
  tier: priority
---

# 并行检查食物网拓扑和动力学稳定性

## 原题与基线

区分连边结构改变与平衡点附近的动态表现

## 建模机制与求解

新增物种时修改食物网及耦合方程，用结构中心性描述重排，用 Jacobian 特征值检查局部动态

## 验证与局限

中心性与稳定性含义分开，平衡点和边权扰动可补检

## 迁移到新题

可用于同一机制下不同生态配置的比较

## 证据定位

- PDF 第 15–20 页，第5节、表2至5、图10至13。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 15–20 第5节、表2至5、图10至13可对应假设、机制与结果。 |
| 机制解释力 | 4 | 新增物种时修改食物网及耦合方程，用结构中心性描述重排，用 Jacobian 特征值检查局部动态。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 中心性与稳定性含义分开，平衡点和边权扰动可补检 |
| 可迁移性 | 3 | 可用于同一机制下不同生态配置的比较 |

总分 **17/20** · 优先借鉴
