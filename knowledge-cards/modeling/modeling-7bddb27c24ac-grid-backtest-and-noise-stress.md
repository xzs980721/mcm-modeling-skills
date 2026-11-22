---
schema: mcm-card-v1
id: "modeling-7bddb27c24ac-grid-backtest-and-noise-stress"
type: modeling
title: "在相同历史窗口比较成本及输入扰动"
paper:
  title: "Grid the profit: Adaptive Periodic Grid Model with ARIMA Prediction"
  year: 2022
  problem: C
source:
  pdf: "2022/MCM-C/论文/2200401.pdf"
  pdf_root: null
  sha256: "7bddb27c24ac00c33b76ef70c08f8d44a10b3f04f0822562d9dd19ad795a5b5c"
  pdf_pages: [15, 17, 18, 19]
tags: ["网格边界", "滚动校准", "回测对照"]
score:
  total: 17
  max: 20
  tier: priority
---

# 在相同历史窗口比较成本及输入扰动

## 原题与基线

回测结果可能依赖费用及输入波动假设

## 建模机制与求解

保持状态更新规则，以多边界、费用和数据噪声重跑

## 验证与局限

仅给历史及高斯噪声，未覆盖跳空及成交限制

## 迁移到新题

添加费率和缺交易日模型，用一致输入逐期对账

## 证据定位

- PDF 第 15 页，图7–8。
- PDF 第 17 页，图9–10。
- PDF 第 18 页，图11。
- PDF 第 19 页，图12。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 15 图7–8、17 图9–10、18 图11、19 图12可对应假设、机制与结果。 |
| 机制解释力 | 3 | 保持状态更新规则，以多边界、费用和数据噪声重跑。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 仅给历史及高斯噪声，未覆盖跳空及成交限制 |
| 可迁移性 | 4 | 添加费率和缺交易日模型，用一致输入逐期对账 |

总分 **17/20** · 优先借鉴
