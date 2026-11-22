---
schema: mcm-card-v1
id: "modeling-d77e804d8263-grf-archard"
type: modeling
title: "用方向性反力积分修正磨损量"
paper:
  title: "Step Chronicles: A Multiscale Model Linking Wear Patterns and Temporal Use in Ancient Staircases"
  year: 2025
  problem: A
source:
  pdf: "2025/MCM-A/论文/2501567.pdf"
  pdf_root: null
  sha256: "d77e804d8263a4a2425a2b66afb09a71b14fa2c24afa9c6ec94ad058c7bda040"
  pdf_pages: [6, 7, 8, 9, 10, 11, 12]
tags: ["Archard 磨损", "混合分布", "寿命"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用方向性反力积分修正磨损量

## 原题与基线

单一载荷难区分材料和上下行脚步

## 建模机制与求解

以 Archard 体积损失为基线，加入材料硬度、温度和足底反力积分，再由三维扫描校验与反演使用频率

## 验证与局限

论文报告花岗岩估计与实测偏差，反力参数用于其他石材时不可照搬

## 迁移到新题

给定足底数据、硬度及有效滑动距离后换算；在已知频次阶梯做偏差校验

## 证据定位

- PDF 第 6–12 页，图2–6、表2–3、式1–10。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 6–12 图2–6、表2–3、式1–10可对应假设、机制与结果。 |
| 机制解释力 | 4 | 以 Archard 体积损失为基线，加入材料硬度、温度和足底反力积分，再由三维扫描校验与反演使用频率。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 论文报告花岗岩估计与实测偏差，反力参数用于其他石材时不可照搬 |
| 可迁移性 | 3 | 给定足底数据、硬度及有效滑动距离后换算；在已知频次阶梯做偏差校验 |

总分 **17/20** · 优先借鉴
