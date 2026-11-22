---
schema: mcm-card-v1
id: "modeling-23751fe4d6a0-shell-topsis-selection"
type: modeling
title: "用网络层级和多指标距离划定候选工程"
paper:
  title: "Navigating Baltimore’s Growth: A Multi-Layer Network Approach to Urban Transportation Optimization"
  year: 2025
  problem: D
source:
  pdf: "2025/ICM-D/论文/2519935.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "23751fe4d6a0c8075a79839cee87363037f06c5757e398f24391b11414c53e6e"
  pdf_pages: [13, 14, 15, 16]
tags: ["交通网络", "路网韧性", "轨道选线"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用网络层级和多指标距离划定候选工程

## 原题与基线

缩减改造候选并比较方案

## 建模机制与求解

使用加权网络指标识别层级，再将多指标标准化与赋权后作 TOPSIS 排序；将候选与既有服务位置叠合

## 验证与局限

排名依赖标准化及权重，宜报告阈值和排名扰动

## 迁移到新题

用于道路或轨道的分阶段选址

## 证据定位

- PDF 第 13–16 页，第6节及表5、图12至16。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 13–16 第6节及表5、图12至16可对应假设、机制与结果。 |
| 机制解释力 | 4 | 使用加权网络指标识别层级，再将多指标标准化与赋权后作 TOPSIS 排序；将候选与既有服务位置叠合。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 排名依赖标准化及权重，宜报告阈值和排名扰动 |
| 可迁移性 | 3 | 用于道路或轨道的分阶段选址 |

总分 **16/20** · 可借鉴
