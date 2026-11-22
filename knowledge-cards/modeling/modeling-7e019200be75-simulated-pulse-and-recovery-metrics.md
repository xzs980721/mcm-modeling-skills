---
schema: mcm-card-v1
id: "modeling-7e019200be75-simulated-pulse-and-recovery-metrics"
type: modeling
title: "用一致脉冲测群落恢复差距"
paper:
  title: "Population analysis of lampreys: a discrete population dynamics model based on age grouping"
  year: 2024
  problem: A
source:
  pdf: "2024/MCM-A/论文/2425397.pdf"
  pdf_root: null
  sha256: "7e019200be75a4f5a7df506bc4faadfd2da10690d4ed7d4a7b78d91c46044f56"
  pdf_pages: [18, 19, 20, 23, 24]
tags: ["龄级离散", "相轨道", "冲击恢复"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用一致脉冲测群落恢复差距

## 原题与基线

不同对象遭受压力时，末态相近也可能恢复时间不同

## 建模机制与求解

分别在同一时点改变模型输入，统计最大偏离幅度及恢复所需时间

## 验证与局限

有两类压力结果表和参数例，未报告多轮独立随机检验

## 迁移到新题

用受扰与未扰两个重复轨迹计算差值，报告无恢复情景而非硬设时长

## 证据定位

- PDF 第 18 页，图18。
- PDF 第 19 页，图19及表5。
- PDF 第 20 页，图20及表6。
- PDF 第 23–24 页，图23–24。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 18 图18、19 图19及表5、20 图20及表6、23–24 图23–24可对应假设、机制与结果。 |
| 机制解释力 | 4 | 分别在同一时点改变模型输入，统计最大偏离幅度及恢复所需时间。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 有两类压力结果表和参数例，未报告多轮独立随机检验 |
| 可迁移性 | 3 | 用受扰与未扰两个重复轨迹计算差值，报告无恢复情景而非硬设时长 |

总分 **16/20** · 可借鉴
