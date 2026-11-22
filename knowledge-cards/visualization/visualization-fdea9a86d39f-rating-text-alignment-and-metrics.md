---
schema: mcm-card-v1
id: "visualization-fdea9a86d39f-rating-text-alignment-and-metrics"
type: visualization
title: "用混淆式热图和评价曲线诊断两路评级一致性"
paper:
  title: "Beat The Market: Comprehensive Exploration of Amazon Reviews and Ratings"
  year: 2020
  problem: C
source:
  pdf: "2020/MCM-C/论文/2003717.pdf"
  pdf_root: null
  sha256: "fdea9a86d39f65f6fb78db23457eb9997d577b1ce29a319da04ccd243deef937"
  pdf_pages: [20]
tags: ["LDA", "声誉窗口", "评分文本一致性"]
score:
  total: 19
  max: 20
  tier: priority
---

# 用混淆式热图和评价曲线诊断两路评级一致性

## 入选理由

表达创新或视觉张力。热图显示偏差发生在哪些等级，曲线对照总体指标

## 论证任务

识别哪个品类的星级与文本一致性较高

## 图型与输入

三面板五乘五矩阵着色标格值，第四面板比较精确、召回及宏 F1。

## 视觉编码

三面板五乘五矩阵着色标格值，第四面板比较精确、召回及宏 F1

## 重绘与迁移

冻结色尺，说明归一方式，指标从同矩阵重算并查类别样本不足

## 证据定位

- PDF 第 20 页，图16(a)–(d)、表6。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 20 图16(a)–(d)、表6给出图面、图题及正文语境。 |
| 论证表达 | 4 | 热图显示偏差发生在哪些等级，曲线对照总体指标 |
| 重绘可行性 | 4 | 三面板五乘五矩阵着色标格值，第四面板比较精确、召回及宏 F1。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 4 | 冻结色尺，说明归一方式，指标从同矩阵重算并查类别样本不足 |

总分 **19/20** · 优先借鉴
