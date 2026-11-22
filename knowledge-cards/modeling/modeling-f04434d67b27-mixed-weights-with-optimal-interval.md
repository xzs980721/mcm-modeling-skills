---
schema: mcm-card-v1
id: "modeling-f04434d67b27-mixed-weights-with-optimal-interval"
type: modeling
title: "把适度区间指标纳入组合赋权 TOPSIS"
paper:
  title: "Will Asteroid Mining Affect Global Equity? Mathematical Modelling Based on Data from 32 Countries"
  year: 2022
  problem: F
source:
  pdf: "2022/ICM-F/论文/2218577.pdf"
  pdf_root: null
  sha256: "f04434d67b2764a3c4668c903a33b5eb55c26183a7fbb50bb07bc2e326b4f3c2"
  pdf_pages: [7, 8, 9, 10, 11, 12, 13, 24]
tags: ["TOPSIS", "部门分工", "情景分布"]
score:
  total: 16
  max: 20
  tier: usable
---

# 把适度区间指标纳入组合赋权 TOPSIS

## 原题与基线

多项公平指标并非一律越高越好，且部分缺值

## 建模机制与求解

按成本、收益及适度类型缩放，合用熵权和变异权，经正负理想距离生成名次

## 验证与局限

表和地图可核验，图14检验权重偏好。外部排名对照及缺测处理须复算

## 迁移到新题

用最优区间内外的合成值验证单调，按地区轮流留出并重算名次

## 证据定位

- PDF 第 7 页，表1。
- PDF 第 8–10 页，指标变换、两路权重及图2。
- PDF 第 11–13 页，表2与图3–5。
- PDF 第 24 页，图14。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 7 表1、8–10 指标变换、两路权重及图2、11–13 表2与图3–5、24 图14可对应假设、机制与结果。 |
| 机制解释力 | 4 | 按成本、收益及适度类型缩放，合用熵权和变异权，经正负理想距离生成名次。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 表和地图可核验，图14检验权重偏好。外部排名对照及缺测处理须复算 |
| 可迁移性 | 3 | 用最优区间内外的合成值验证单调，按地区轮流留出并重算名次 |

总分 **16/20** · 可借鉴
