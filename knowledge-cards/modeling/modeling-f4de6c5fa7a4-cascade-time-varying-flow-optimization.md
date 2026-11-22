---
schema: mcm-card-v1
id: "modeling-f4de6c5fa7a4-cascade-time-varying-flow-optimization"
type: modeling
title: "将水位状态和输水输电网络联合求解"
paper:
  title: "A Model for Better Use of Water Resources Based on Marginal Utility and Auction Theory"
  year: 2022
  problem: B
source:
  pdf: "2022/MCM-B/论文/2200084.pdf"
  pdf_root: null
  sha256: "f4de6c5fa7a435c4b3e7d9083f39d4908d496cb9ee52671ac84cf83880794ae4"
  pdf_pages: [6, 7, 8, 9, 10, 11, 12]
tags: ["级联水库", "分配网络", "竞拍边际效用"]
score:
  total: 18
  max: 20
  tier: priority
---

# 将水位状态和输水输电网络联合求解

## 原题与基线

水量和水电共用水库且存在最低水位

## 建模机制与求解

以串联系统传播库水状态，再分日更新线性网络并核查可行性

## 验证与局限

输出跨日水位和各州分流，线性化及外部来水场景需要验证

## 迁移到新题

在两库小网络核对跨期质量守恒和停供约束

## 证据定位

- PDF 第 6 页，图3–4。
- PDF 第 7 页，图5。
- PDF 第 8–10 页，方程、算法1及表2。
- PDF 第 11–12 页，图6–10。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 6 图3–4、7 图5、8–10 方程、算法1及表2、11–12 图6–10可对应假设、机制与结果。 |
| 机制解释力 | 4 | 以串联系统传播库水状态，再分日更新线性网络并核查可行性。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 输出跨日水位和各州分流，线性化及外部来水场景需要验证 |
| 可迁移性 | 4 | 在两库小网络核对跨期质量守恒和停供约束 |

总分 **18/20** · 优先借鉴
