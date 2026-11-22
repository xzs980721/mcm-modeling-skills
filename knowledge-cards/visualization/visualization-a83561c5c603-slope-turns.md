---
schema: mcm-card-v1
id: "visualization-a83561c5c603-slope-turns"
type: visualization
title: "导数与关键时间竖线对照"
paper:
  title: "Command the Flow: Analysis and Prediction of Momentum in Tennis Matches"
  year: 2024
  problem: C
source:
  pdf: "2024/MCM-C/论文/2406324.pdf"
  pdf_root: null
  sha256: "a83561c5c6030213d72c2c295e21f78c68e9409e087abffbc0495ed325e9be94"
  pdf_pages: [11]
tags: ["网球", "滤波", "迁移"]
score:
  total: 17
  max: 20
  tier: priority
---

# 导数与关键时间竖线对照

## 入选理由

表达创新或视觉张力。把波形层的转折显示成可检验局部信号

## 论证任务

定位斜率换符号或峰值时刻

## 图型与输入

画势头斜率和零线，以标记指向候选点。

## 视觉编码

画势头斜率和零线，以标记指向候选点

## 重绘与迁移

补充导数的差分窗口和阈值

## 证据定位

- PDF 第 11 页，图8。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 11 图8给出图面、图题及正文语境。 |
| 论证表达 | 4 | 把波形层的转折显示成可检验局部信号 |
| 重绘可行性 | 3 | 画势头斜率和零线，以标记指向候选点。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 补充导数的差分窗口和阈值 |

总分 **17/20** · 优先借鉴
