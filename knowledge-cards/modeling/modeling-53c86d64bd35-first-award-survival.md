---
schema: mcm-card-v1
id: "modeling-53c86d64bd35-first-award-survival"
type: modeling
title: "用 Cox 风险和蒙特卡洛估首次获奖"
paper:
  title: "Golden Dynamics: Bayesian-AI Olympic Forecasting with Geopolitics & Coaching"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2516695.pdf"
  pdf_root: null
  sha256: "53c86d64bd350c52b989574acb6693009a2448905664ac4fd9e0d0a65e19549f"
  pdf_pages: [11, 12]
tags: ["动态贝叶斯", "风险与干预", "全球灵敏度"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用 Cox 风险和蒙特卡洛估首次获奖

## 原题与基线

无首牌的国家在观测期末只是删失

## 建模机制与求解

将多维参赛特征送入 Cox，结合抽样模拟未来概率及不确定

## 验证与局限

给候选敏感性及结果，缺独立比例风险与长期校准检验

## 迁移到新题

分清参赛起点和删失，用已知后届校验风险排序

## 证据定位

- PDF 第 11–12 页，图8、表6、算法2。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 11–12 图8、表6、算法2可对应假设、机制与结果。 |
| 机制解释力 | 4 | 将多维参赛特征送入 Cox，结合抽样模拟未来概率及不确定。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 给候选敏感性及结果，缺独立比例风险与长期校准检验 |
| 可迁移性 | 3 | 分清参赛起点和删失，用已知后届校验风险排序 |

总分 **16/20** · 可借鉴
