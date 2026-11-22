---
schema: mcm-card-v1
id: "modeling-869782f09ab9-bellman-distance-sliced-pacing"
type: modeling
title: "把离散道路和库存状态组合成 Bellman 规划"
paper:
  title: "Optimal Cycling Solution Based on Physiology, Newtonian Mechanics and Dynamic Programming"
  year: 2022
  problem: A
source:
  pdf: "2022/MCM-A/论文/2216547.pdf"
  pdf_root: null
  sha256: "869782f09ab98e3ec43d62a2f94f7ff8fc003a06a923072a796cbfec8b0ba261"
  pdf_pages: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
tags: ["肌肉疲劳", "离散求解", "状态诊断"]
score:
  total: 18
  max: 20
  tier: priority
---

# 把离散道路和库存状态组合成 Bellman 规划

## 原题与基线

沿程选择功率受可行状态和终点时间约束

## 建模机制与求解

将路段坡弯几何转成动力约束，按阶段传播速度与资源并优化总时

## 验证与局限

搜索路线图及多条件轨迹支持核查，距离或状态网格收敛需补证

## 迁移到新题

给短路枚举基准，再比较不同离散尺度的速度和时间

## 证据定位

- PDF 第 11–13 页，图6–10。
- PDF 第 14–16 页，方程及图11。
- PDF 第 17–21 页，图12–19。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 11–13 图6–10、14–16 方程及图11、17–21 图12–19可对应假设、机制与结果。 |
| 机制解释力 | 4 | 将路段坡弯几何转成动力约束，按阶段传播速度与资源并优化总时。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 搜索路线图及多条件轨迹支持核查，距离或状态网格收敛需补证 |
| 可迁移性 | 4 | 给短路枚举基准，再比较不同离散尺度的速度和时间 |

总分 **18/20** · 优先借鉴
