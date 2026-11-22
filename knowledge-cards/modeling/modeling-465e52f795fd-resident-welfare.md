---
schema: mcm-card-v1
id: "modeling-465e52f795fd-resident-welfare"
type: modeling
title: "把人口收入趋势和游客感受合成社会福利代理"
paper:
  title: "Economy, Ecology, and Social Welfare:A Win-Win Approach for Sustainable Tourism in Juneau"
  year: 2025
  problem: B
source:
  pdf: "2025/MCM-B/论文/2501687.pdf"
  pdf_root: null
  sha256: "465e52f795fd36f31df25b2a6592b11b0a1286b0a11e2424b6727973128d27fe"
  pdf_pages: [12, 13, 14, 15]
tags: ["旅游限流", "福利量化", "非线性优化"]
score:
  total: 16
  max: 20
  tier: usable
---

# 把人口收入趋势和游客感受合成社会福利代理

## 原题与基线

旅游收入与居民满意度可能方向不同

## 建模机制与求解

以回归预测人口和收入，用 ARIMA 检查失业变化，再以调查赋权估算不利影响

## 验证与局限

文中有拟合及调查比例，关联和政策因果不可混用

## 迁移到新题

换同题调查和就业类别，核查比例分母和预测历史外留

## 证据定位

- PDF 第 12–15 页，图6–9。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 12–15 图6–9可对应假设、机制与结果。 |
| 机制解释力 | 4 | 以回归预测人口和收入，用 ARIMA 检查失业变化，再以调查赋权估算不利影响。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 文中有拟合及调查比例，关联和政策因果不可混用 |
| 可迁移性 | 3 | 换同题调查和就业类别，核查比例分母和预测历史外留 |

总分 **16/20** · 可借鉴
