---
schema: mcm-card-v1
id: "modeling-869782f09ab9-joint-fatigue-and-storage-state"
type: modeling
title: "区分肌肉输出上限和能量库存"
paper:
  title: "Optimal Cycling Solution Based on Physiology, Newtonian Mechanics and Dynamic Programming"
  year: 2022
  problem: A
source:
  pdf: "2022/MCM-A/论文/2216547.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "869782f09ab98e3ec43d62a2f94f7ff8fc003a06a923072a796cbfec8b0ba261"
  pdf_pages: [6, 7, 8, 9, 10]
tags: ["肌肉疲劳", "离散求解", "状态诊断"]
score:
  total: 18
  max: 20
  tier: priority
---

# 区分肌肉输出上限和能量库存

## 原题与基线

疲劳可逆变化与累计能耗具有不同轨迹

## 建模机制与求解

分别建立疲劳恢复和资源库存方程，取当前可行功率上限推进状态

## 验证与局限

不同初值和骑手曲线能检查行为，独立个体校准有限

## 迁移到新题

验证静息和极短满功率两边界，再拟合长短时观测

## 证据定位

- PDF 第 6–8 页，图1–3。
- PDF 第 9 页，图4及表1。
- PDF 第 10 页，图5及算法1。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 6–8 图1–3、9 图4及表1、10 图5及算法1可对应假设、机制与结果。 |
| 机制解释力 | 4 | 分别建立疲劳恢复和资源库存方程，取当前可行功率上限推进状态。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 不同初值和骑手曲线能检查行为，独立个体校准有限 |
| 可迁移性 | 4 | 验证静息和极短满功率两边界，再拟合长短时观测 |

总分 **18/20** · 优先借鉴
