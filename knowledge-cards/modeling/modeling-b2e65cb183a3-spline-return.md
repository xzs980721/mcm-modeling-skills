---
schema: mcm-card-v1
id: "modeling-b2e65cb183a3-spline-return"
type: modeling
title: "将累计分转为发球基准下的瞬时偏差"
paper:
  title: "Momentum Prediction and Core Feature Extraction Based on GRU with Integrated Gradients"
  year: 2024
  problem: C
source:
  pdf: "2024/MCM-C/论文/2409961.pdf"
  pdf_root: null
  sha256: "b2e65cb183a336844825205dea990a883d2605a682725dff39a733680cf829d5"
  pdf_pages: [7, 8, 9, 10, 11]
tags: ["网球", "GRU", "积分梯度"]
score:
  total: 16
  max: 20
  tier: usable
---

# 将累计分转为发球基准下的瞬时偏差

## 原题与基线

需要从累积分数获得可比较的局部表现

## 建模机制与求解

先对离散分数做三次平滑并求导，再条件化发接角色后计算偏差

## 验证与局限

文中展示角色散点及标准化前后分布，平滑在实时部署需检查未来信息

## 迁移到新题

适合不连续累积计数的速率比较

## 证据定位

- PDF 第 7–11 页，图2–7。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 7–11 图2–7可对应假设、机制与结果。 |
| 机制解释力 | 4 | 先对离散分数做三次平滑并求导，再条件化发接角色后计算偏差。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 文中展示角色散点及标准化前后分布，平滑在实时部署需检查未来信息 |
| 可迁移性 | 3 | 适合不连续累积计数的速率比较 |

总分 **16/20** · 可借鉴
