---
schema: mcm-card-v1
id: "visualization-2a0cc9101a96-passenger-simulator-branches"
type: visualization
title: "以判定框展开每个时步的乘客动作"
paper:
  title: "In the Zone: Novel Approaches to Airplane Boarding"
  year: 2007
  problem: B
source:
  pdf: "2007/MCM-B/论文/Novel Approaches to Airplane Boarding.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "2a0cc9101a96b60403d4843b6e081e5f55fd076d0438d938a9c05b6599244985"
  pdf_pages: [12]
tags: ["登机排序", "处理器模拟", "遗传优化"]
score:
  total: 17
  max: 20
  tier: priority
---

# 以判定框展开每个时步的乘客动作

## 入选理由

表达创新或视觉张力。可核查等待、前进或入座之间的状态触发

## 论证任务

处理器什么情况下推进时间或切换乘客状态？

## 图型与输入

圆角起止和菱形判定配回环箭头，不同结果收敛到操作节点。

## 视觉编码

圆角起止和菱形判定配回环箭头，不同结果收敛到操作节点

## 重绘与迁移

给关键分支补变量和逻辑条件

## 证据定位

- PDF 第 12 页，图2。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 12 图2给出图面、图题及正文语境。 |
| 论证表达 | 4 | 可核查等待、前进或入座之间的状态触发 |
| 重绘可行性 | 3 | 圆角起止和菱形判定配回环箭头，不同结果收敛到操作节点。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 给关键分支补变量和逻辑条件 |

总分 **17/20** · 优先借鉴
