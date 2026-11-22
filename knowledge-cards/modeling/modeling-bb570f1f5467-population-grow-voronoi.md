---
schema: mcm-card-v1
id: "modeling-bb570f1f5467-population-grow-voronoi"
type: modeling
title: "以目标人口容量限制区域扩张"
paper:
  title: "Applying Voronoi Diagrams to the Redistricting Problem"
  year: 2007
  problem: A
source:
  pdf: "2007/MCM-A/论文/Applying Voronoi Diagrams to the Redistricting Problem.pdf"
  pdf_root: null
  sha256: "bb570f1f5467ae8a97a8b81c3addf813edbf65aa1fb93eeaf2ef2e5430646679"
  pdf_pages: [7, 8, 9, 10, 11, 14, 15, 16, 17]
tags: ["Voronoi", "地理分区", "人口栅格"]
score:
  total: 17
  max: 20
  tier: priority
---

# 以目标人口容量限制区域扩张

## 原题与基线

标准最近邻划分的面积均匀性并不保证人口均衡

## 建模机制与求解

由人口集中区挑生成点，逐步扩张并结合人口权重控制各区份额，比较不同距离；先为高密度范围分出子域再应用

## 验证与局限

真实州人口份额给数值复查，栅格人口估计、细分和边界相交需校验

## 迁移到新题

可用于容量受限的设施服务区划

## 证据定位

- PDF 第 7–11 页，第4节、图1–3。
- PDF 第 14–17 页，图6–7及表1。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 7–11 第4节、图1–3、14–17 图6–7及表1可对应假设、机制与结果。 |
| 机制解释力 | 4 | 由人口集中区挑生成点，逐步扩张并结合人口权重控制各区份额，比较不同距离；先为高密度范围分出子域再应用。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 真实州人口份额给数值复查，栅格人口估计、细分和边界相交需校验 |
| 可迁移性 | 3 | 可用于容量受限的设施服务区划 |

总分 **17/20** · 优先借鉴
