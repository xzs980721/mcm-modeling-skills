---
schema: mcm-card-v1
id: "visualization-81f99eb44559-prediction-sweeps"
type: visualization
title: "相同布局下观察输入加减后的台阶响应"
paper:
  title: "Olympic Medals Unveiled: A Mathematical Exploration of Achievement Trends"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2507817.pdf"
  pdf_root: null
  sha256: "81f99eb4455949cdaab1ab385f40dc5a367e5cf4d094a15d67269354cfa8c842"
  pdf_pages: [24]
tags: ["奥运", "预测区间", "稀疏回归"]
score:
  total: 17
  max: 20
  tier: priority
---

# 相同布局下观察输入加减后的台阶响应

## 入选理由

表达创新或视觉张力。可识别树模型不连续的跳变点

## 论证任务

判断赛事数和运动员数扰动的预测敏感段

## 图型与输入

固定其它输入，分别按变量扫描并绘输出变化。

## 视觉编码

固定其它输入，分别按变量扫描并绘输出变化

## 重绘与迁移

标 baseline 和切换位置及整数步长

## 证据定位

- PDF 第 24 页，图23 a–b。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 24 图23 a–b给出图面、图题及正文语境。 |
| 论证表达 | 4 | 可识别树模型不连续的跳变点 |
| 重绘可行性 | 3 | 固定其它输入，分别按变量扫描并绘输出变化。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 标 baseline 和切换位置及整数步长 |

总分 **17/20** · 优先借鉴
