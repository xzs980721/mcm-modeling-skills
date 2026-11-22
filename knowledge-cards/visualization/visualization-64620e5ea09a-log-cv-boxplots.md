---
schema: mcm-card-v1
id: "visualization-64620e5ea09a-log-cv-boxplots"
type: visualization
title: "用对数箱线图比较候选阶数的验证误差"
paper:
  title: "Forecasts for the Ecology and Fisheries Economy of Scottish herring and mackerel"
  year: 2020
  problem: A
source:
  pdf: "2020/MCM-A/论文/2001334.pdf"
  pdf_root: null
  sha256: "64620e5ea09a09f3db7f8057663ce1b094f1ff522eccf1d889378a1b412dab99"
  pdf_pages: [10]
tags: ["海温", "迁移轨迹", "破产风险"]
score:
  total: 18
  max: 20
  tier: priority
---

# 用对数箱线图比较候选阶数的验证误差

## 入选理由

表达创新或视觉张力。同图呈现中位数、离群和数量级跨度

## 论证任务

选择误差稳定的 ARIMA 阶数

## 图型与输入

横轴四种参数配对，纵轴对数显示六折验证 RMSE，红点标离群。

## 视觉编码

横轴四种参数配对，纵轴对数显示六折验证 RMSE，红点标离群

## 重绘与迁移

同折同格计算误差，保留每个模型样本数，注明对数轴不能显示零

## 证据定位

- PDF 第 10 页，图6。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 10 图6给出图面、图题及正文语境。 |
| 论证表达 | 4 | 同图呈现中位数、离群和数量级跨度 |
| 重绘可行性 | 3 | 横轴四种参数配对，纵轴对数显示六折验证 RMSE，红点标离群。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 4 | 同折同格计算误差，保留每个模型样本数，注明对数轴不能显示零 |

总分 **18/20** · 优先借鉴
