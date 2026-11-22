---
schema: mcm-card-v1
id: "visualization-042b56884fce-stacking-lanes"
type: visualization
title: "基模型预测分支汇集到元模型"
paper:
  title: "2028 Olympic Medal Predictions: Multi-Effect Analysis and Strategic Insights"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2510862.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "042b56884fcebe1928a7ccc60853390f4c140b1210d033ece9087a1ec0fd6bda"
  pdf_pages: [7]
tags: ["堆叠集成", "SHAP", "匹配双重差分"]
score:
  total: 17
  max: 20
  tier: priority
---

# 基模型预测分支汇集到元模型

## 入选理由

表达创新或视觉张力。训练及预测路径能区分，利于查泄漏

## 论证任务

理解输出怎样进入整合

## 图型与输入

分支框分别为各基学习器，箭头注入元学习器。

## 视觉编码

分支框分别为各基学习器，箭头注入元学习器

## 重绘与迁移

标折外预测和最终重训的两条路径

## 证据定位

- PDF 第 7 页，图3。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 7 图3给出图面、图题及正文语境。 |
| 论证表达 | 4 | 训练及预测路径能区分，利于查泄漏 |
| 重绘可行性 | 3 | 分支框分别为各基学习器，箭头注入元学习器。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 标折外预测和最终重训的两条路径 |

总分 **17/20** · 优先借鉴
