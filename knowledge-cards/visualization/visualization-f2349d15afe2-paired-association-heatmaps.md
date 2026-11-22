---
schema: mcm-card-v1
id: "visualization-f2349d15afe2-paired-association-heatmaps"
type: visualization
title: "用相同对象次序并列两种相似度矩阵"
paper:
  title: "CAFE: Characterization, Analysis, Forecasting, and Evaluation of Energy Profile"
  year: 2018
  problem: C
source:
  pdf: "2018/MCM-C/论文/72969.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "f2349d15afe26f49d7183ab8cc7759d1eb9a275b69a6c6bdc51796cfae0b860a"
  pdf_pages: [12]
tags: ["能源画像", "混合预测", "目标协调"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用相同对象次序并列两种相似度矩阵

## 入选理由

表达创新或视觉张力。蓝、红矩阵视觉分开不同统计量，相同单元位置支持判断一致项。

## 论证任务

对照灰关联与秩相关得到的州际相似程度。

## 图型与输入

行列都是同一组州，单元格深浅表示 GRC 和 KRCC，色条分别解释数值。

## 视觉编码

行列都是同一组州，单元格深浅表示 GRC 和 KRCC，色条分别解释数值。

## 重绘与迁移

锁定州序并验证矩阵对称性，区分两统计量零点与尺度，再标差异单元。

## 证据定位

- PDF 第 12 页，图6。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 12 图6给出图面、图题及正文语境。 |
| 论证表达 | 4 | 蓝、红矩阵视觉分开不同统计量，相同单元位置支持判断一致项。 |
| 重绘可行性 | 3 | 行列都是同一组州，单元格深浅表示 GRC 和 KRCC，色条分别解释数值。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 锁定州序并验证矩阵对称性，区分两统计量零点与尺度，再标差异单元。 |

总分 **17/20** · 优先借鉴
