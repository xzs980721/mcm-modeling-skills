---
schema: mcm-card-v1
id: "visualization-db130a3a278d-rank-stability-and-score-parity"
type: visualization
title: "用并列扰动曲线与评分等值散点交代稳定性"
paper:
  title: "Finding Conspirators in the Network via Machine Learning"
  year: 2012
  problem: C
source:
  pdf: "2012/ICM-C/论文/Finding Conspirators in the Network via Machine Learning.pdf"
  pdf_root: null
  sha256: "db130a3a278dd6f4a998e2a6bd812b3925dee31d27ef42a74df9d99d3bc9e86a"
  pdf_pages: [15, 16, 17]
tags: ["网络分析", "小样本", "稳定性"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用并列扰动曲线与评分等值散点交代稳定性

## 入选理由

表达创新或视觉张力。排名整体变化和个体分数变化用不同的图。

## 论证任务

比较错误标签下排序相关值，以及规则改变前后的各点偏离。

## 图型与输入

图6用颜色比较两类误标，横轴概率、纵轴 Kendall τ。

## 视觉编码

图6用颜色比较两类误标，横轴概率、纵轴 Kendall τ。图7同尺度横纵轴为变更前后模型分数，斜线为不变参照。

## 重绘与迁移

读取一个高相关但分数偏移的案例，验证两图不会被解释成同一稳健性指标。

## 证据定位

- PDF 第 15–16 页，图6及扰动说明。
- PDF 第 17 页，图7。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 15–16 图6及扰动说明、17 图7给出图面、图题及正文语境。 |
| 论证表达 | 4 | 排名整体变化和个体分数变化用不同的图。 |
| 重绘可行性 | 3 | 图6用颜色比较两类误标，横轴概率、纵轴 Kendall τ。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 读取一个高相关但分数偏移的案例，验证两图不会被解释成同一稳健性指标。 迁移时按上文检查条件和输入口径。 |

总分 **17/20** · 优先借鉴
