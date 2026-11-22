---
schema: mcm-card-v1
id: "modeling-cbdc483b65b4-cluster-assisted-pseudo-label-cnn"
type: modeling
title: "借助聚类标签缓解图像监督样本不平衡"
paper:
  title: "Swarming with Data: Prioritizing Sightings of Vespa Mandarinia with Semi-Supervised Learning"
  year: 2021
  problem: C
source:
  pdf: "2021/MCM-C/论文/2107870.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "cbdc483b65b4f43c7a3c67ace5e5c4ff3ec278521c0adab7cb7bbbc9bf0cc2a8"
  pdf_pages: [8, 9, 10, 11, 12, 13, 20, 21]
tags: ["半监督分类", "概率融合", "分档复核"]
score:
  total: 18
  max: 20
  tier: priority
---

# 借助聚类标签缓解图像监督样本不平衡

## 原题与基线

少量已定标签难以单独训练稳定图像筛查器

## 建模机制与求解

先在图像表示上聚类并用已有标签解释聚类，再训练卷积分支

## 验证与局限

联合报告不同簇数的指标及三折混淆矩阵，伪标签噪声和源级泄漏仍需控制

## 迁移到新题

按图像来源分组留出，对无伪标签、不同簇数和类权重分别比较

## 证据定位

- PDF 第 8–12 页，图2–4及算法1–2。
- PDF 第 13 页，图5。
- PDF 第 20 页，图14。
- PDF 第 21 页，图15。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 8–12 图2–4及算法1–2、13 图5、20 图14、21 图15可对应假设、机制与结果。 |
| 机制解释力 | 4 | 先在图像表示上聚类并用已有标签解释聚类，再训练卷积分支。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 联合报告不同簇数的指标及三折混淆矩阵，伪标签噪声和源级泄漏仍需控制 |
| 可迁移性 | 4 | 按图像来源分组留出，对无伪标签、不同簇数和类权重分别比较 |

总分 **18/20** · 优先借鉴
