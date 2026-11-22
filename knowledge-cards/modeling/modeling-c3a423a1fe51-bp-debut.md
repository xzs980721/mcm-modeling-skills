---
schema: mcm-card-v1
id: "modeling-c3a423a1fe51-bp-debut"
type: modeling
title: "单独建二类网络判首次获奖"
paper:
  title: "Maximizing Medal Performance: Athlete and Event Potential Indices"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2510185.pdf"
  pdf_root: null
  sha256: "c3a423a1fe51e518a175d0cff007e31519b59a614bbfa97b62d22ccff23c020d"
  pdf_pages: [13, 14]
tags: ["运动员潜力", "随机森林", "项目重要性"]
score:
  total: 15
  max: 20
  tier: usable
---

# 单独建二类网络判首次获奖

## 原题与基线

获牌零值的形成机制不同于已有奖牌数量回归

## 建模机制与求解

从近年来首次获奖国家建正类，以参赛及历史字段训练分类，给候选概率

## 验证与局限

提供 ROC 和选例，无长期首次获奖概率校准

## 迁移到新题

先复核按届留出及稀有类采样偏差，再使用概率

## 证据定位

- PDF 第 13–14 页，图8、表9。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 13–14 图8、表9可对应假设、机制与结果。 |
| 机制解释力 | 3 | 从近年来首次获奖国家建正类，以参赛及历史字段训练分类，给候选概率。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 提供 ROC 和选例，无长期首次获奖概率校准 |
| 可迁移性 | 3 | 先复核按届留出及稀有类采样偏差，再使用概率 |

总分 **15/20** · 可借鉴
