---
schema: mcm-card-v1
id: "modeling-32dd29c8ce49-pareto-scenic-allocation"
type: modeling
title: "以约束优化同时确定总量与景区分配"
paper:
  title: "Overload Alarm: Pareto Optimization of the Economic-Social-Environmental Triangle"
  year: 2025
  problem: B
source:
  pdf: "2025/MCM-B/论文/2502617.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "32dd29c8ce49b9cb80cc53668dfce0e335b835419195829fc79ffd009f43487b"
  pdf_pages: [14, 15, 16, 17, 18, 19, 20, 22]
tags: ["旅游权衡", "边际效应", "SLSQP"]
score:
  total: 17
  max: 20
  tier: priority
---

# 以约束优化同时确定总量与景区分配

## 原题与基线

不同景区和分目标冲突使单目标最大化不稳

## 建模机制与求解

按权重组合收益并用 SLSQP 搜索，在不同客流和消费水平下比较各类可行性与结果

## 验证与局限

展示三种权衡及跨地区算例和灵敏度，有限起点的 SLSQP 结果不能证明全局非支配

## 迁移到新题

用多起点与少量显式网格检查边界，地区变化时重估需求与容量

## 证据定位

- PDF 第 14–20 页，图7–14。
- PDF 第 22 页，表3。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 14–20 图7–14、22 表3可对应假设、机制与结果。 |
| 机制解释力 | 4 | 按权重组合收益并用 SLSQP 搜索，在不同客流和消费水平下比较各类可行性与结果。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 展示三种权衡及跨地区算例和灵敏度，有限起点的 SLSQP 结果不能证明全局非支配 |
| 可迁移性 | 3 | 用多起点与少量显式网格检查边界，地区变化时重估需求与容量 |

总分 **17/20** · 优先借鉴
