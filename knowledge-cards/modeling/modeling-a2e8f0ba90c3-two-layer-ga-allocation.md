---
schema: mcm-card-v1
id: "modeling-a2e8f0ba90c3-two-layer-ga-allocation"
type: modeling
title: "以双层规划分开效率目标和运输约束"
paper:
  title: "A Two-Stage Water Resource Optimal Operation Model Based on Genetic Algorithm"
  year: 2022
  problem: B
source:
  pdf: "2022/MCM-B/论文/2228168.pdf"
  pdf_root: null
  sha256: "a2e8f0ba90c3a1d5f49eda10401c8bc6fdc7dfa7def56d5906c1f50c1dda5e7c"
  pdf_pages: [14, 15, 16, 17, 18, 19, 20, 21]
tags: ["双层规划", "水位阈值", "遗传算法"]
score:
  total: 18
  max: 20
  tier: priority
---

# 以双层规划分开效率目标和运输约束

## 原题与基线

地方使用收益与上层调配成本的分母和约束不同

## 建模机制与求解

遗传搜索处理下层收益，所得用水需求连到上层分配并复算短缺场景

## 验证与局限

两情景展示目标收敛和解表，不能据此证明全局最优

## 迁移到新题

以小问题枚举和多种子比较并验证可行性

## 证据定位

- PDF 第 14–18 页，图8及表5–7。
- PDF 第 19–21 页，图9和表8–10。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 14–18 图8及表5–7、19–21 图9和表8–10可对应假设、机制与结果。 |
| 机制解释力 | 4 | 遗传搜索处理下层收益，所得用水需求连到上层分配并复算短缺场景。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 两情景展示目标收敛和解表，不能据此证明全局最优 |
| 可迁移性 | 4 | 以小问题枚举和多种子比较并验证可行性 |

总分 **18/20** · 优先借鉴
