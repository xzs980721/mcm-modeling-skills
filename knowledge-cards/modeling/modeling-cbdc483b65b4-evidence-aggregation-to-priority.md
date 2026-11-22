---
schema: mcm-card-v1
id: "modeling-cbdc483b65b4-evidence-aggregation-to-priority"
type: modeling
title: "合成多路报告证据并校准复核分档"
paper:
  title: "Swarming with Data: Prioritizing Sightings of Vespa Mandarinia with Semi-Supervised Learning"
  year: 2021
  problem: C
source:
  pdf: "2021/MCM-C/论文/2107870.pdf"
  pdf_root: null
  sha256: "cbdc483b65b4f43c7a3c67ace5e5c4ff3ec278521c0adab7cb7bbbc9bf0cc2a8"
  pdf_pages: [4, 13, 14, 15, 16, 17, 18, 24]
tags: ["半监督分类", "概率融合", "分档复核"]
score:
  total: 18
  max: 20
  tier: priority
---

# 合成多路报告证据并校准复核分档

## 原题与基线

有限人力需据图像、文字和地点的混合证据识别高优先队列

## 建模机制与求解

各支路产生错分相关分数，联合得到筛查分数并定义复核区间

## 验证与局限

按已知标签对比分布，备忘录给出分档；区间的队列成本及样本外表现缺少量化

## 迁移到新题

先明确分数方向，用独立已核数据测量各分档召回和队列规模

## 证据定位

- PDF 第 4 页，图1。
- PDF 第 13–17 页，图5–9。
- PDF 第 18 页，图10–12。
- PDF 第 24 页，图16。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 4 图1、13–17 图5–9、18 图10–12、24 图16可对应假设、机制与结果。 |
| 机制解释力 | 4 | 各支路产生错分相关分数，联合得到筛查分数并定义复核区间。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 按已知标签对比分布，备忘录给出分档；区间的队列成本及样本外表现缺少量化 |
| 可迁移性 | 4 | 先明确分数方向，用独立已核数据测量各分档召回和队列规模 |

总分 **18/20** · 优先借鉴
