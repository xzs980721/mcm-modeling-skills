---
schema: mcm-card-v1
id: "modeling-53a5244d887c-first-medal-count"
type: modeling
title: "对不同国家首次获牌概率做异质伯努利汇总"
paper:
  title: "Olympic Medal Prediction Model Based on Regression and Machine Learning"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2503389.pdf"
  pdf_root: null
  sha256: "53a5244d887c0dac699f9926c9a30969112d6528a6b33573f86efa386e10fee3"
  pdf_pages: [12, 13, 14]
tags: ["奥运", "模型融合", "首牌模拟"]
score:
  total: 16
  max: 20
  tier: usable
---

# 对不同国家首次获牌概率做异质伯努利汇总

## 原题与基线

各国概率不同，不能用同成功率二项近似代替

## 建模机制与求解

先用 Logistic 与随机森林估各国首次获牌概率，按 Poisson 二项和随机抽样汇总数量

## 验证与局限

有交叉验证和模拟分布，没有后届概率校准数据

## 迁移到新题

换候选地区和赛事，先在往届检查分布覆盖及同届相关

## 证据定位

- PDF 第 12–14 页，图7–9、表6。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 12–14 图7–9、表6可对应假设、机制与结果。 |
| 机制解释力 | 4 | 先用 Logistic 与随机森林估各国首次获牌概率，按 Poisson 二项和随机抽样汇总数量。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 有交叉验证和模拟分布，没有后届概率校准数据 |
| 可迁移性 | 3 | 换候选地区和赛事，先在往届检查分布覆盖及同届相关 |

总分 **16/20** · 可借鉴
