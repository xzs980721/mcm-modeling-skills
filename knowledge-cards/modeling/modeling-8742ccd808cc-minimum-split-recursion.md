---
schema: mcm-card-v1
id: "modeling-8742ccd808cc-minimum-split-recursion"
type: modeling
title: "按需求份额递归选短切线生成连通分区"
paper:
  title: "Why Weight? A Cluster-Theoretic Approach to Political Districting"
  year: 2007
  problem: A
source:
  pdf: "2007/MCM-A/论文/A Cluster-Theoretic Approach to Political Districting.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "8742ccd808cc8f275928817c581ebd36562b3eb4664e7ee8464cc8b6d6d5b3d2"
  pdf_pages: [9, 10, 13, 16, 17]
tags: ["地理区划", "加权聚类", "空间紧致"]
score:
  total: 17
  max: 20
  tier: priority
---

# 按需求份额递归选短切线生成连通分区

## 原题与基线

给聚类输出一个易复核的几何基线

## 建模机制与求解

先按计划两侧区数设人口比例，再选最短可行切线，递归直到单区

## 验证与局限

可比较纽约两模型的紧致及人口误差，边界栅格误差和断连约束要核查

## 迁移到新题

适用于将连续地理范围按服务量逐次分割

## 证据定位

- PDF 第 9–10 页，第4节、图3。
- PDF 第 13 页，图6。
- PDF 第 16–17 页，附录B。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 9–10 第4节、图3、13 图6、16–17 附录B可对应假设、机制与结果。 |
| 机制解释力 | 4 | 先按计划两侧区数设人口比例，再选最短可行切线，递归直到单区。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 可比较纽约两模型的紧致及人口误差，边界栅格误差和断连约束要核查 |
| 可迁移性 | 3 | 适用于将连续地理范围按服务量逐次分割 |

总分 **17/20** · 优先借鉴
