---
schema: mcm-card-v1
id: "modeling-d77e804d8263-fatigue-and-progression"
type: modeling
title: "将日常磨损进程与集中载荷疲劳分别估算"
paper:
  title: "Step Chronicles: A Multiscale Model Linking Wear Patterns and Temporal Use in Ancient Staircases"
  year: 2025
  problem: A
source:
  pdf: "2025/MCM-A/论文/2501567.pdf"
  pdf_root: null
  sha256: "d77e804d8263a4a2425a2b66afb09a71b14fa2c24afa9c6ec94ad058c7bda040"
  pdf_pages: [18, 19, 20, 21, 22, 23]
tags: ["Archard 磨损", "混合分布", "寿命"]
score:
  total: 16
  max: 20
  tier: usable
---

# 将日常磨损进程与集中载荷疲劳分别估算

## 原题与基线

同样的踩踏次数分时或集中，对机械损伤影响可能不同

## 建模机制与求解

用蒙特卡洛采样行走特点并累计空间磨损，另以 Chaboche 模型比较不同载荷时间分布

## 验证与局限

报告若干年模拟及应力响应，无不同流量情景的实际长期观测

## 迁移到新题

换入试验材料的循环参数及监测边界，先复算单载荷状态再批量模拟

## 证据定位

- PDF 第 18–23 页，算法1、图11–12、式30–36。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 18–23 算法1、图11–12、式30–36可对应假设、机制与结果。 |
| 机制解释力 | 4 | 用蒙特卡洛采样行走特点并累计空间磨损，另以 Chaboche 模型比较不同载荷时间分布。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 报告若干年模拟及应力响应，无不同流量情景的实际长期观测 |
| 可迁移性 | 3 | 换入试验材料的循环参数及监测边界，先复算单载荷状态再批量模拟 |

总分 **16/20** · 可借鉴
