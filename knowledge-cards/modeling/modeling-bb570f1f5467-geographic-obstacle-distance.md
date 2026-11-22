---
schema: mcm-card-v1
id: "modeling-bb570f1f5467-geographic-obstacle-distance"
type: modeling
title: "用地理障碍约束分区扩张或路径距离"
paper:
  title: "Applying Voronoi Diagrams to the Redistricting Problem"
  year: 2007
  problem: A
source:
  pdf: "2007/MCM-A/论文/Applying Voronoi Diagrams to the Redistricting Problem.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "bb570f1f5467ae8a97a8b81c3addf813edbf65aa1fb93eeaf2ef2e5430646679"
  pdf_pages: [18, 19]
tags: ["Voronoi", "地理分区", "人口栅格"]
score:
  total: 15
  max: 20
  tier: usable
---

# 用地理障碍约束分区扩张或路径距离

## 原题与基线

防止平面最近点导致不合理的跨障碍区形

## 建模机制与求解

在 Voronoi 扩张过程中将地理屏障保留，边界沿可达空间接触，城市密集区可先细分

## 验证与局限

图8示意验证，缺少跨屏障真实路径或通勤基线

## 迁移到新题

可迁移到岛屿、入河口和山谷服务区规划

## 证据定位

- PDF 第 18–19 页，第7节及图8。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 18–19 第7节及图8可对应假设、机制与结果。 |
| 机制解释力 | 3 | 在 Voronoi 扩张过程中将地理屏障保留，边界沿可达空间接触，城市密集区可先细分。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 图8示意验证，缺少跨屏障真实路径或通勤基线 |
| 可迁移性 | 3 | 可迁移到岛屿、入河口和山谷服务区规划 |

总分 **15/20** · 可借鉴
