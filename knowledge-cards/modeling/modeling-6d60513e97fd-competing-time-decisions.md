---
schema: mcm-card-v1
id: "modeling-6d60513e97fd-competing-time-decisions"
type: modeling
title: "用状态转移比较接受、等待及配对选项"
paper:
  title: "Analysis of Kidney Transplant System Using Markov Process Models"
  year: 2007
  problem: C
source:
  pdf: "2007/ICM-C/论文/Analysis of Kidney Transplant System Using Markov Process Models.pdf"
  pdf_root: null
  sha256: "6d60513e97fd54ddc6d511381e6baed589468cc928fb6b11c837b829aee6742b"
  pdf_pages: [10, 11, 12, 15, 16, 17, 18]
tags: ["等候系统", "马尔可夫过程", "配对交换"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用状态转移比较接受、等待及配对选项

## 原题与基线

不同选项需要在等待时风险与后续结果间取舍

## 建模机制与求解

用竞争事件和生存模型计算期望，再匹配分人群及有无配对交换的选项

## 验证与局限

是历史建模示例，指数风险和少量群组压缩限制外推

## 迁移到新题

方法可迁移到任意竞争等待时间的抽象决策分析

## 证据定位

- PDF 第 10–12 页，图6至8和表6。
- PDF 第 15–18 页，供体模型。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 10–12 图6至8和表6、15–18 供体模型可对应假设、机制与结果。 |
| 机制解释力 | 4 | 用竞争事件和生存模型计算期望，再匹配分人群及有无配对交换的选项。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 是历史建模示例，指数风险和少量群组压缩限制外推 |
| 可迁移性 | 3 | 方法可迁移到任意竞争等待时间的抽象决策分析 |

总分 **16/20** · 可借鉴
