---
schema: mcm-card-v1
id: "visualization-278f2f6812f3-simulation-view-with-enlarged-local-mechanism"
type: visualization
title: "从整体帧上标出需放大的车队互动"
paper:
  title: "Highway Traffic Flow Model with Self-Driving Vehicles Based on Cellular Automata"
  year: 2017
  problem: C
source:
  pdf: "2017/MCM-C/论文/55585.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "278f2f6812f35e7cb88c8d5006ab37eaf45f59a61ce62ee4c7079db4adeffe53"
  pdf_pages: [15, 17]
tags: ["混合车辆", "状态规则", "多维交通表现"]
score:
  total: 17
  max: 20
  tier: priority
---

# 从整体帧上标出需放大的车队互动

## 入选理由

表达创新或视觉张力。放大区域凸显总体视觉难看清的车距与局部换道。

## 论证任务

确认模型输出是否展示所设跟随或换道规则。

## 图型与输入

底层为仿真车道全景，圈标签及插框突出局部，图15按状态并列剖示。

## 视觉编码

底层为仿真车道全景，圈标签及插框突出局部，图15按状态并列剖示。

## 重绘与迁移

让每个放大框与帧上坐标关联，冻结同一步核对车辆和速度。

## 证据定位

- PDF 第 15 页，图11。
- PDF 第 17 页，图15。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 15 图11、17 图15给出图面、图题及正文语境。 |
| 论证表达 | 4 | 放大区域凸显总体视觉难看清的车距与局部换道。 |
| 重绘可行性 | 3 | 底层为仿真车道全景，圈标签及插框突出局部，图15按状态并列剖示。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 让每个放大框与帧上坐标关联，冻结同一步核对车辆和速度。 |

总分 **17/20** · 优先借鉴
