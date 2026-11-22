---
schema: mcm-card-v1
id: "modeling-a2e8f0ba90c3-transport-water-level-state"
type: modeling
title: "从运输优化到多月水库可运行期"
paper:
  title: "A Two-Stage Water Resource Optimal Operation Model Based on Genetic Algorithm"
  year: 2022
  problem: B
source:
  pdf: "2022/MCM-B/论文/2228168.pdf"
  pdf_root: null
  sha256: "a2e8f0ba90c3a1d5f49eda10401c8bc6fdc7dfa7def56d5906c1f50c1dda5e7c"
  pdf_pages: [7, 8, 9, 10, 12, 13, 14]
tags: ["双层规划", "水位阈值", "遗传算法"]
score:
  total: 18
  max: 20
  tier: priority
---

# 从运输优化到多月水库可运行期

## 原题与基线

区域供给约束和库水降至阈值可能同时触发

## 建模机制与求解

以输水距离约束调配并逐期更新库容和发电能力

## 验证与局限

调度时序对照阈值行为，持续期需验证入流变化

## 迁移到新题

设置已知来水和需求的两库小例，核对首次不可行时点

## 证据定位

- PDF 第 7–8 页，表1–2及图2–3。
- PDF 第 9–10 页，图4–5。
- PDF 第 12–14 页，图6–7及表3–4。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 7–8 表1–2及图2–3、9–10 图4–5、12–14 图6–7及表3–4可对应假设、机制与结果。 |
| 机制解释力 | 4 | 以输水距离约束调配并逐期更新库容和发电能力。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 调度时序对照阈值行为，持续期需验证入流变化 |
| 可迁移性 | 4 | 设置已知来水和需求的两库小例，核对首次不可行时点 |

总分 **18/20** · 优先借鉴
