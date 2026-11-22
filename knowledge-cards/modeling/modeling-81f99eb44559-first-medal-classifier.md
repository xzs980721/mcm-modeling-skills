---
schema: mcm-card-v1
id: "modeling-81f99eb44559-first-medal-classifier"
type: modeling
title: "用二元 Logistic 预测零获牌国家首次突破"
paper:
  title: "Olympic Medals Unveiled: A Mathematical Exploration of Achievement Trends"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2507817.pdf"
  pdf_root: null
  sha256: "81f99eb4455949cdaab1ab385f40dc5a367e5cf4d094a15d67269354cfa8c842"
  pdf_pages: [13, 14, 15, 16]
tags: ["奥运", "预测区间", "稀疏回归"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用二元 Logistic 预测零获牌国家首次突破

## 原题与基线

稀疏首次奖牌难用计数回归校准

## 建模机制与求解

构造项目、参赛和历史指标并训练二元模型，比较 ROC 和混淆矩阵

## 验证与局限

给出分类指标与国家机会，甄别低先验类须同时核查精确率及概率校准

## 迁移到新题

按国家和届联合留出并核对未参赛与零牌的不同标签

## 证据定位

- PDF 第 13–16 页，图12–14、表9–11、式7–12。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 13–16 图12–14、表9–11、式7–12可对应假设、机制与结果。 |
| 机制解释力 | 4 | 构造项目、参赛和历史指标并训练二元模型，比较 ROC 和混淆矩阵。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 给出分类指标与国家机会，甄别低先验类须同时核查精确率及概率校准 |
| 可迁移性 | 3 | 按国家和届联合留出并核对未参赛与零牌的不同标签 |

总分 **16/20** · 可借鉴
