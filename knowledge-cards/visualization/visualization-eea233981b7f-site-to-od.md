---
schema: mcm-card-v1
id: "visualization-eea233981b7f-site-to-od"
type: visualization
title: "把现场环岛与定向流量矩阵相邻呈现"
paper:
  title: "Three Steps to Make the Traffic Circle Go Round"
  year: 2009
  problem: A
source:
  pdf: "2009/MCM-A/论文/Three Steps to Make the Traffic Circle Go Round.pdf"
  pdf_root: null
  sha256: "eea233981b7ff452dc2317211d387904aa679fc2a57dcf0b4da5ce4fe3de0350"
  pdf_pages: [3, 4]
tags: ["环岛", "情景比较", "交通调度"]
score:
  total: 18
  max: 20
  tier: priority
---

# 把现场环岛与定向流量矩阵相邻呈现

## 入选理由

表达创新。由俯视形状转入来向与去向。

## 论证任务

明确真实几何中存在六个路口，再把同一对象转成可计算的车辆流量。

## 图型与输入

图中环岛居中，场景照片给空间方位。

## 视觉编码

表以起讫路口构成行列，数值单位为辆/小时，方向从行列标题读取。

## 重绘与迁移

给现场图和矩阵复用同一编号，抽查一对非对称起讫的取值与方向，再核对行列和。

## 证据定位

- PDF 第 3 页（印刷页 263），图1。
- PDF 第 4 页（印刷页 264），表1。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 可在 3 图1、4 表1 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 4 | 由俯视形状转入来向与去向。 |
| 重绘可行性 | 3 | 图中环岛居中，场景照片给空间方位。 核对时按原文定义相同统计口径。 |
| 视觉可读性 | 3 | 原页主层次可辨，成文尺寸下仍需检查标注。 |
| 可迁移性 | 4 | 给现场图和矩阵复用同一编号，抽查一对非对称起讫的取值与方向，再核对行列和。 |

总分 **18/20** · 优先借鉴
