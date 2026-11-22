---
schema: mcm-card-v1
id: "modeling-7fd2005c3d91-entropy-ahp-interventions"
type: modeling
title: "联合多层指标给备选农事组合评分"
paper:
  title: "Forests and Agriculture in Harmony: How to Maintain Ecosystem Stability During the Transition to Organic Farming"
  year: 2025
  problem: E
source:
  pdf: "2025/ICM-E/论文/2502355.pdf"
  pdf_root: null
  sha256: "7fd2005c3d91b23a6451ad148cc1ec1b16c15ec7f6a264f1e49145ea096b22d8"
  pdf_pages: [21, 22, 23]
tags: ["农业生态", "食物网", "动态干预"]
score:
  total: 16
  max: 20
  tier: usable
---

# 联合多层指标给备选农事组合评分

## 原题与基线

把生态、经营等不可直接相比的目标纳入决策

## 建模机制与求解

为每个措施组合构造多维指标并归一，结合层级与熵权组织综合评分

## 验证与局限

报告配置和指标，可补权重扰动与未量化损失

## 迁移到新题

适用于兼顾收益及生态稳定性的方案筛选

## 证据定位

- PDF 第 21–23 页，第6节、图14与表6、式34–35。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 21–23 第6节、图14与表6、式34–35可对应假设、机制与结果。 |
| 机制解释力 | 4 | 为每个措施组合构造多维指标并归一，结合层级与熵权组织综合评分。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 报告配置和指标，可补权重扰动与未量化损失 |
| 可迁移性 | 3 | 适用于兼顾收益及生态稳定性的方案筛选 |

总分 **16/20** · 可借鉴
