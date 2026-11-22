---
schema: mcm-card-v1
id: "modeling-6bcf5acd78dd-brt-access-equity"
type: modeling
title: "用旅行成本和公平指标评价公交改造"
paper:
  title: "A Multi-Methodological Framework for Post-Disaster Traffic Optimization and Sustainable Mobility Planning in Baltimore"
  year: 2025
  problem: D
source:
  pdf: "2025/ICM-D/论文/2516219.pdf"
  pdf_root: null
  sha256: "6bcf5acd78dd6cff84bbbf52895464a07b02bff83554831f3051b279274a9a6c"
  pdf_pages: [15, 16, 17, 18, 19, 20]
tags: ["灾后交通", "网络均衡", "公交规划"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用旅行成本和公平指标评价公交改造

## 原题与基线

评估道路空间重配的代价和群体差异

## 建模机制与求解

接上公交站点、车道及步行设施，模拟出行方式与出行成本，将可达性 Gini、污染与等待纳入比较

## 验证与局限

表4为情景输出，实施后的实测效应、误差范围仍应补充

## 迁移到新题

适用于公交优先与慢行组合项目

## 证据定位

- PDF 第 15–20 页，多模式方案和受益方分析。
- PDF 第 18 页，图8及表4。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 15–20 多模式方案和受益方分析、18 图8及表4可对应假设、机制与结果。 |
| 机制解释力 | 4 | 接上公交站点、车道及步行设施，模拟出行方式与出行成本，将可达性 Gini、污染与等待纳入比较。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 表4为情景输出，实施后的实测效应、误差范围仍应补充 |
| 可迁移性 | 3 | 适用于公交优先与慢行组合项目 |

总分 **16/20** · 可借鉴
