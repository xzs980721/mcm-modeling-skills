---
schema: mcm-card-v1
id: "visualization-4cbde897bb3a-temporal-heatmap-stack"
type: visualization
title: "把相邻时刻概率层沿时间叠放"
paper:
  title: "Save the Submersible: An Combined Method of Computational Fluid Dynamics and Kalman Filter"
  year: 2024
  problem: B
source:
  pdf: "2024/MCM-B/论文/2425792.pdf"
  pdf_root: null
  sha256: "4cbde897bb3a881ab0d29ee4b1cb1abc31b03e72b1acf52d941d1d17850adc82"
  pdf_pages: [17]
tags: ["轨迹状态", "协方差", "搜救地图"]
score:
  total: 16
  max: 20
  tier: usable
---

# 把相邻时刻概率层沿时间叠放

## 入选理由

表达创新或视觉张力。在相同地图位置对照概率峰如何漂移

## 论证任务

查看最高概率带在何时移动

## 图型与输入

等规格透视层以色度给概率、高度序列表达时间。

## 视觉编码

等规格透视层以色度给概率、高度序列表达时间

## 重绘与迁移

标每层时间和同色标，补平面切片避免遮挡

## 证据定位

- PDF 第 17 页，图13。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 3 | 17 图13给出图面、图题及正文语境。 |
| 论证表达 | 4 | 在相同地图位置对照概率峰如何漂移 |
| 重绘可行性 | 3 | 等规格透视层以色度给概率、高度序列表达时间。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 标每层时间和同色标，补平面切片避免遮挡 |

总分 **16/20** · 可借鉴
