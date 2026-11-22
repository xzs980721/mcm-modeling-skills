---
schema: mcm-card-v1
id: "visualization-f877d0a02e33-diurnal-traffic-volume-by-sensor-series"
type: visualization
title: "用日内叠线检查多个站点的双峰规律"
paper:
  title: "Driving Towards the Future: Modeling the Impact of Driverless Vehicles on Traffic Patterns"
  year: 2017
  problem: C
source:
  pdf: "2017/MCM-C/论文/55261.pdf"
  pdf_root: null
  sha256: "f877d0a02e332e8c2a991e49398896de946c8618f5c1d4c6764eeb73772c9d13"
  pdf_pages: [4]
tags: ["交通基本图", "驾驶协作", "传感器核验"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用日内叠线检查多个站点的双峰规律

## 入选理由

表达创新或视觉张力。诊断原始实测输入的时段共性和不同峰幅。

## 论证任务

为模型的交通条件和验证时段取样。

## 图型与输入

横轴一天小时，纵轴流量，传感器或方向用彩线区分。

## 视觉编码

横轴一天小时，纵轴流量，传感器或方向用彩线区分。

## 重绘与迁移

同星期和日窗口复算，标交换时区和离群事件。

## 证据定位

- PDF 第 4 页，图1。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 3 | 4 图1给出图面、图题及正文语境。 |
| 论证表达 | 4 | 诊断原始实测输入的时段共性和不同峰幅。 |
| 重绘可行性 | 3 | 横轴一天小时，纵轴流量，传感器或方向用彩线区分。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 同星期和日窗口复算，标交换时区和离群事件。 |

总分 **16/20** · 可借鉴
