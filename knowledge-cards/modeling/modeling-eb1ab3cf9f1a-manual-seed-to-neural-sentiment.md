---
schema: mcm-card-v1
id: "modeling-eb1ab3cf9f1a-manual-seed-to-neural-sentiment"
type: modeling
title: "以人工修订词典分和上下文嵌入训练情感估计"
paper:
  title: "Strategies to Online Sales: A Review-tracking System Combined with Deep Learning and Difference Equation Model"
  year: 2020
  problem: C
source:
  pdf: "2020/MCM-C/论文/2007707.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "eb1ab3cf9f1a49a9a49c171e77a0d808b12109066b68957e7348a6bde93b7fc4"
  pdf_pages: [10, 11, 12, 13, 14, 15, 21, 26, 27, 28, 29]
tags: ["文本评分", "差分方程", "成功指数"]
score:
  total: 16
  max: 20
  tier: usable
---

# 以人工修订词典分和上下文嵌入训练情感估计

## 原题与基线

词典逐词累加会误判语境

## 建模机制与求解

用 TF-IDF 摘关键词，经 one-hot 和 CBOW 得向量，修正少量词典分作监督拟合

## 验证与局限

用删去部分人工校正的实验做敏感性，人工评分主观且训练分布偏

## 迁移到新题

建立独立标注样本和纯词典基线，分品类报告留出误差

## 证据定位

- PDF 第 10–15 页，表2、图9–图15。
- PDF 第 21 页，图18、表7。
- PDF 第 26–29 页，附录词表。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 10–15 表2、图9–图15、21 图18、表7、26–29 附录词表可对应假设、机制与结果。 |
| 机制解释力 | 3 | 用 TF-IDF 摘关键词，经 one-hot 和 CBOW 得向量，修正少量词典分作监督拟合。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 用删去部分人工校正的实验做敏感性，人工评分主观且训练分布偏 |
| 可迁移性 | 4 | 建立独立标注样本和纯词典基线，分品类报告留出误差 |

总分 **16/20** · 可借鉴
