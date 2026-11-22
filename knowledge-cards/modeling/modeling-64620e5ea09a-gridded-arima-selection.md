---
schema: mcm-card-v1
id: "modeling-64620e5ea09a-gridded-arima-selection"
type: modeling
title: "以交叉验证在多个格点筛选海温预测阶数"
paper:
  title: "Forecasts for the Ecology and Fisheries Economy of Scottish herring and mackerel"
  year: 2020
  problem: A
source:
  pdf: "2020/MCM-A/论文/2001334.pdf"
  pdf_root: null
  sha256: "64620e5ea09a09f3db7f8057663ce1b094f1ff522eccf1d889378a1b412dab99"
  pdf_pages: [7, 8, 9, 10, 11, 26, 27, 28]
tags: ["海温", "迁移轨迹", "破产风险"]
score:
  total: 17
  max: 20
  tier: priority
---

# 以交叉验证在多个格点筛选海温预测阶数

## 原题与基线

水域各点的历史温度差异大，如何选择共同预测结构

## 建模机制与求解

按季预处理、填缺并将地理位置转为球面表示，比较候选 ARIMA 阶数在六折 RMSE 分布上的表现

## 验证与局限

论文给误差箱线和代码，长时域外推仍超过历史检验窗

## 迁移到新题

按时间块而非随机划分重跑，比较季节基线，检查高误差格点空间集中

## 证据定位

- PDF 第 7–11 页，图3–图7。
- PDF 第 26–28 页，附录ARIMA代码。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 7–11 图3–图7、26–28 附录ARIMA代码可对应假设、机制与结果。 |
| 机制解释力 | 3 | 按季预处理、填缺并将地理位置转为球面表示，比较候选 ARIMA 阶数在六折 RMSE 分布上的表现。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 论文给误差箱线和代码，长时域外推仍超过历史检验窗 |
| 可迁移性 | 4 | 按时间块而非随机划分重跑，比较季节基线，检查高误差格点空间集中 |

总分 **17/20** · 优先借鉴
