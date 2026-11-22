---
schema: mcm-card-v1
id: "visualization-c4b4c7532831-decompose-total-baseline"
type: visualization
title: "同轴展示两种设备分量、总能源与反事实"
paper:
  title: "Mobile to Mobil: The Primary Energy Costs for Cellular and Landline Telephones"
  year: 2009
  problem: B
source:
  pdf: "2009/MCM-B/论文/Mobile to Mobil.pdf"
  pdf_root: null
  sha256: "c4b4c75328314b9f8f4a9638aa060b399315fd6b598218e6478ae8c0448af856"
  pdf_pages: [7]
tags: ["一次能源", "存量模型", "策略参照"]
score:
  total: 18
  max: 20
  tier: priority
---

# 同轴展示两种设备分量、总能源与反事实

## 入选理由

表达创新。分量变化、总量峰值和基线交叉一图可见。

## 论证任务

把源自替代模型的设备量换成能耗后，检验双持过渡何时超过无手机替代基线。

## 图型与输入

年份对一次能源 GWh/日，移动、固话、总计和基线对应四条系列。

## 视觉编码

基线单独编码，分量并非堆叠。

## 重绘与迁移

抽三年核对两分量之和等于总线，基线不参与加总。纵轴一致并在交叉处放简短标注。

## 证据定位

- PDF 第 7 页（印刷页 319），图3。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 可在 7 图3 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 4 | 分量变化、总量峰值和基线交叉一图可见。 |
| 重绘可行性 | 3 | 年份对一次能源 GWh/日，移动、固话、总计和基线对应四条系列。 逐点源数据未随图附出。 |
| 视觉可读性 | 3 | 原页主层次可辨，成文尺寸下仍需检查标注。 |
| 可迁移性 | 4 | 抽三年核对两分量之和等于总线，基线不参与加总。纵轴一致并在交叉处放简短标注。 |

总分 **18/20** · 优先借鉴
