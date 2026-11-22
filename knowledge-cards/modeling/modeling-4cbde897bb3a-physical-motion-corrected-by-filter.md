---
schema: mcm-card-v1
id: "modeling-4cbde897bb3a-physical-motion-corrected-by-filter"
type: modeling
title: "将力学状态外推和观测校正构成闭环"
paper:
  title: "Save the Submersible: An Combined Method of Computational Fluid Dynamics and Kalman Filter"
  year: 2024
  problem: B
source:
  pdf: "2024/MCM-B/论文/2425792.pdf"
  pdf_root: null
  sha256: "4cbde897bb3a881ab0d29ee4b1cb1abc31b03e72b1acf52d941d1d17850adc82"
  pdf_pages: [8, 9, 10, 11, 12, 15, 16, 21]
tags: ["轨迹状态", "协方差", "搜救地图"]
score:
  total: 16
  max: 20
  tier: usable
---

# 将力学状态外推和观测校正构成闭环

## 原题与基线

失联前观测有噪声，失联后只能外推

## 建模机制与求解

力学量进入预测状态，观测更新均值与协方差，进而构造候选区域

## 验证与局限

仿真扰动及误差表可查，协方差覆盖需实测核准

## 迁移到新题

用合成同方差观测验证无观测时方差增长及覆盖率

## 证据定位

- PDF 第 8–10 页，图5–6及矩阵。
- PDF 第 11–12 页，图7–9。
- PDF 第 15–16 页，图11。
- PDF 第 21 页，表4及图19。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 8–10 图5–6及矩阵、11–12 图7–9、15–16 图11、21 表4及图19可对应假设、机制与结果。 |
| 机制解释力 | 4 | 力学量进入预测状态，观测更新均值与协方差，进而构造候选区域。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 仿真扰动及误差表可查，协方差覆盖需实测核准 |
| 可迁移性 | 3 | 用合成同方差观测验证无观测时方差增长及覆盖率 |

总分 **16/20** · 可借鉴
