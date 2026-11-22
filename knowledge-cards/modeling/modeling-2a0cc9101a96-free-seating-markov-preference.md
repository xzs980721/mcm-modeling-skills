---
schema: mcm-card-v1
id: "modeling-2a0cc9101a96-free-seating-markov-preference"
type: modeling
title: "把非指定座位的旅客偏好写进位置转移"
paper:
  title: "In the Zone: Novel Approaches to Airplane Boarding"
  year: 2007
  problem: B
source:
  pdf: "2007/MCM-B/论文/Novel Approaches to Airplane Boarding.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "2a0cc9101a96b60403d4843b6e081e5f55fd076d0438d938a9c05b6599244985"
  pdf_pages: [23, 24, 25, 26, 27, 34, 48, 49, 50]
tags: ["登机排序", "处理器模拟", "遗传优化"]
score:
  total: 16
  max: 20
  tier: usable
---

# 把非指定座位的旅客偏好写进位置转移

## 原题与基线

自由座位时不能直接用预先分配的排列

## 建模机制与求解

设座位选择偏好和通过/停留概率，构建 Markov 转移并计算稳态分布或选择行为

## 验证与局限

由偏好假设得出的图案可查，真实家庭同行及偏好需要校验

## 迁移到新题

适用于有位置选择的场馆与交通

## 证据定位

- PDF 第 23–27 页，第3.4节。
- PDF 第 34 页，图16。
- PDF 第 48–50 页，附录C。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 23–27 第3.4节、34 图16、48–50 附录C可对应假设、机制与结果。 |
| 机制解释力 | 4 | 设座位选择偏好和通过/停留概率，构建 Markov 转移并计算稳态分布或选择行为。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 由偏好假设得出的图案可查，真实家庭同行及偏好需要校验 |
| 可迁移性 | 3 | 适用于有位置选择的场馆与交通 |

总分 **16/20** · 可借鉴
