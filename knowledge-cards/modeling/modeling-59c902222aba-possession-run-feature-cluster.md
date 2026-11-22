---
schema: mcm-card-v1
id: "modeling-59c902222aba-possession-run-feature-cluster"
type: modeling
title: "从连续传球片段提特征并聚类协作结构"
paper:
  title: "Analysis Cooperation Structure of Network and Making Teaming Strategies ——based on Sliding Window Model"
  year: 2020
  problem: D
source:
  pdf: "2020/ICM-D/论文/2013245.pdf"
  pdf_root: null
  sha256: "59c902222abadb7cb14f3d2162ac3efc76f96154a917216dd141900a84c66dda"
  pdf_pages: [4, 5, 6, 7, 8, 9, 10, 11, 25, 26, 27, 28]
tags: ["层次聚类", "滑动窗口", "传球"]
score:
  total: 16
  max: 20
  tier: usable
---

# 从连续传球片段提特征并聚类协作结构

## 原题与基线

全赛网络会抹掉局部配合的时空差异

## 建模机制与求解

提超过阈值的连续序列，编码中心位置、距离、人数、次数及时间，按平均链层次聚类，以 PCA 辅助解释

## 验证与局限

回投到对应片段和完整样例，缺不同阈值下群稳定性检验

## 迁移到新题

更换比赛阈值和特征标准化，抽样核查分组重现及战术可解释性

## 证据定位

- PDF 第 4–11 页，图1–图6及样例。
- PDF 第 25–28 页，聚类代码。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 4–11 图1–图6及样例、25–28 聚类代码可对应假设、机制与结果。 |
| 机制解释力 | 3 | 提超过阈值的连续序列，编码中心位置、距离、人数、次数及时间，按平均链层次聚类，以 PCA 辅助解释。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 回投到对应片段和完整样例，缺不同阈值下群稳定性检验 |
| 可迁移性 | 4 | 更换比赛阈值和特征标准化，抽样核查分组重现及战术可解释性 |

总分 **16/20** · 可借鉴
