---
schema: mcm-card-v1
id: "visualization-64620e5ea09a-qq-empirical-error-check"
type: visualization
title: "用 Q–Q 图核查误差分布的尾部形态"
paper:
  title: "Forecasts for the Ecology and Fisheries Economy of Scottish herring and mackerel"
  year: 2020
  problem: A
source:
  pdf: "2020/MCM-A/论文/2001334.pdf"
  pdf_root: null
  sha256: "64620e5ea09a09f3db7f8057663ce1b094f1ff522eccf1d889378a1b412dab99"
  pdf_pages: [20]
tags: ["海温", "迁移轨迹", "破产风险"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用 Q–Q 图核查误差分布的尾部形态

## 入选理由

表达创新或视觉张力。点序与参照直线的偏离直接提示尾部失配

## 论证任务

辅助判断 RMSE 的模拟分布是否近似正态

## 图型与输入

横轴为标准正态分位，纵轴为经验 RMSE 分位。

## 视觉编码

横轴为标准正态分位，纵轴为经验 RMSE 分位

## 重绘与迁移

独立计算样本和理论分位，检查正值误差偏态并另做覆盖率检验

## 证据定位

- PDF 第 20 页，图16。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 3 | 20 图16给出图面、图题及正文语境。 |
| 论证表达 | 4 | 点序与参照直线的偏离直接提示尾部失配 |
| 重绘可行性 | 3 | 横轴为标准正态分位，纵轴为经验 RMSE 分位。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 独立计算样本和理论分位，检查正值误差偏态并另做覆盖率检验 |

总分 **16/20** · 可借鉴
