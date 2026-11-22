---
schema: mcm-card-v1
id: "modeling-84c1c7cfbe8a-voronoi-cover-and-capacity"
type: modeling
title: "用最远点与负荷上界联合检查设施布点"
paper:
  title: "Fewest Repeaters for a Circular Area: Iterative Extremal Optimization Based on Voronoi Diagrams"
  year: 2011
  problem: B
source:
  pdf: "2011/MCM-B/论文/Fewest Repeaters for a Circular Area.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "84c1c7cfbe8a7683afc9ecdfed98abc890aa42280ca7af9e97f3351a7364064f"
  pdf_pages: [1, 8, 10, 13, 14, 15]
tags: ["Voronoi", "覆盖", "容量约束"]
score:
  total: 19
  max: 20
  tier: priority
---

# 用最远点与负荷上界联合检查设施布点

## 原题与基线

在圆域内用最少中继点覆盖用户。论文先用规则六边形布点给可解析计数的基线。

## 建模机制与求解

从数量下界起步，将地理点划给最近中继，按各区最小包围圆中心迭代移动站点。收敛后校验最远距离和面积×密度的需求上界。局部改动用于摆脱停滞。

## 验证与局限

第 13 页给 1000 用户时的 11 点布置和 10 点不可覆盖的几何界。该证明依赖圆域和覆盖半径，均匀密度是容量推导的条件。

## 迁移到新题

新题用地形可达距离和空间需求权重代替均匀圆域。小实例枚举并核查最远点、热点安全余量和已知数量界。若负荷非均匀使按面积检查失真，改用分区积分。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 130 可得期刊印刷页。

- PDF 第 8 页，规则布点基线
- PDF 第 10 页，Algorithm for Repeater Locations，Voronoi 与收敛
- PDF 第 13–15 页，图 7–10、覆盖界和敏感性分析

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 10、13–15 页算法、覆盖证明、布点图和敏感性互证。 |
| 机制解释力 | 4 | 最远点覆盖与按面积负荷共同限制可行布点。 |
| 实现可复现性 | 3 | 规则和算例可重做核心检验，极值扰动实现不全。 |
| 验证质量 | 4 | 单实例有几何下界，另做数量、范围和密度波动分析。 |
| 可迁移性 | 4 | 枚举小实例和热点容量测试给出停用判据。 |

总分 **19/20** · 优先借鉴
