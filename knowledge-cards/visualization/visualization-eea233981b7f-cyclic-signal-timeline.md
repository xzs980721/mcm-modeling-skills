---
schema: mcm-card-v1
id: "visualization-eea233981b7f-cyclic-signal-timeline"
type: visualization
title: "在循环时间轴标注跨路口的通行窗口"
paper:
  title: "Three Steps to Make the Traffic Circle Go Round"
  year: 2009
  problem: A
source:
  pdf: "2009/MCM-A/论文/Three Steps to Make the Traffic Circle Go Round.pdf"
  pdf_root: null
  sha256: "eea233981b7ff452dc2317211d387904aa679fc2a57dcf0b4da5ce4fe3de0350"
  pdf_pages: [14]
tags: ["配时", "时间带", "协调通行"]
score:
  total: 16
  max: 20
  tier: usable
---

# 在循环时间轴标注跨路口的通行窗口

## 论证任务

图 8 解释来流为原设定 1.8 倍时，六路口配时如何保留特定路口之间的直达窗口。

## 图型与输入

行是六个路口，时间以秒计，周期 68 秒。需各路口的放行区间、相位和要突出显示的协调路径。

## 视觉编码

同一时间方向下用红绿条带表示相位，斜向条带标出车辆沿路口行进时可利用的配时窗口。图下注明流量倍率和周期。

## 重绘与迁移

把新方案的相位表展开一个周期，逐段核验沿路径的到达时刻是否落入可放行区间。用带纹理的红绿替代纯色，确保缩印及灰度下可区分。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 260 可得期刊印刷页。

- PDF 第 14 页，Sheriffhall Roundabout with 1.8 × Original Inflow、图 8，周期和放行窗口

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 3 | 第 14 页的图注、相位条和正文能定位主要解释。 |
| 论证表达 | 4 | 能追踪配时窗和跨多路口关系。 |
| 重绘可行性 | 3 | 已知行、周期和颜色含义，可用新相位表重画。 |
| 视觉可读性 | 2 | 原图拥挤，细小刻度和红绿依赖限制可读性。 |
| 可迁移性 | 4 | 逐站校验到达时刻与放行窗有明确判据。 |

总分 **16/20** · 可借鉴
