---
schema: mcm-card-v1
id: "visualization-41b5e1c20a62-standby-accounting-table"
type: visualization
title: "并置覆盖率、待机功率和全国年耗电量"
paper:
  title: "Modeling Telephony Energy Consumption"
  year: 2009
  problem: B
source:
  pdf: "2009/MCM-B/论文/Modeling Telephony Energy Consumption.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "41b5e1c20a620ace39b44e1a5a01060e37df2b7847ff75f687886f00420412be"
  pdf_pages: [9, 10]
tags: ["设备用电", "参数核算", "表格"]
score:
  total: 17
  max: 20
  tier: priority
---

# 并置覆盖率、待机功率和全国年耗电量

## 入选理由

表达创新。同一行说明单机待机功率如何放大成全国用量。

## 论证任务

支持讨论哪些家电的待机损耗在总体最突出。

## 图型与输入

设备为行，列给待机比例或渗透率、设备 W 及全国待机 TWh/年。

## 视觉编码

时间占比的分母是设备运行时间口径需核对，功耗列原文写作 In use W。

## 重绘与迁移

重画时声明人口和时长分母，挑一项把 W、设备数和小时核成 TWh，缺项保留，不用零代替。

## 证据定位

- PDF 第 9,10 页，表6。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 可在 9,10 表6 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 3 | 同一行说明单机待机功率如何放大成全国用量。 |
| 重绘可行性 | 3 | 设备为行，列给待机比例或渗透率、设备 W 及全国待机 TWh/年。 核对时按原文定义相同统计口径。 |
| 视觉可读性 | 3 | 原页主层次可辨，成文尺寸下仍需检查标注。 |
| 可迁移性 | 4 | 重画时声明人口和时长分母，挑一项把 W、设备数和小时核成 TWh，缺项保留，不用零代替。 |

总分 **17/20** · 优先借鉴
