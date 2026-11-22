---
schema: mcm-card-v1
id: "visualization-f0c04548e5d6-forecast-ablation-overlay"
type: visualization
title: "将时序结果和分类误差表联读"
paper:
  title: "Data-Driven Policy Effectiveness Evaluation and Country-Specific Characteristic Based Cybercrime Prediction"
  year: 2025
  problem: F
source:
  pdf: "2025/ICM-F/论文/2517199.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "f0c04548e5d6bb282178e3f99aa7b570a11f34459fe41d03a3e6c19b044c9968"
  pdf_pages: [22]
tags: ["网络安全政策", "面板统计", "时间预测"]
score:
  total: 17
  max: 20
  tier: priority
---

# 将时序结果和分类误差表联读

## 入选理由

表达创新或视觉张力。轨迹与汇总指标互补验证外生特征的作用

## 论证任务

加入外生量后，模型在哪些日期更接近实测？

## 图型与输入

原序列和两个预测版本共轴，竖线给预测分界，表另报 MAE 和 MSE。

## 视觉编码

原序列和两个预测版本共轴，竖线给预测分界，表另报 MAE 和 MSE

## 重绘与迁移

标训练范围及预测单位，图旁加逐期绝对误差

## 证据定位

- PDF 第 22 页，图14及表VII。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 22 图14及表VII给出图面、图题及正文语境。 |
| 论证表达 | 4 | 轨迹与汇总指标互补验证外生特征的作用 |
| 重绘可行性 | 3 | 原序列和两个预测版本共轴，竖线给预测分界，表另报 MAE 和 MSE。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 标训练范围及预测单位，图旁加逐期绝对误差 |

总分 **17/20** · 优先借鉴
