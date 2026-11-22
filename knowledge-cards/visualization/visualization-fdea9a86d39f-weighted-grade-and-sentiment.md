---
schema: mcm-card-v1
id: "visualization-fdea9a86d39f-weighted-grade-and-sentiment"
type: visualization
title: "对照原值与加权值的星级统计"
paper:
  title: "Beat The Market: Comprehensive Exploration of Amazon Reviews and Ratings"
  year: 2020
  problem: C
source:
  pdf: "2020/MCM-C/论文/2003717.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "fdea9a86d39f65f6fb78db23457eb9997d577b1ce29a319da04ccd243deef937"
  pdf_pages: [9, 10]
tags: ["LDA", "声誉窗口", "评分文本一致性"]
score:
  total: 17
  max: 20
  tier: priority
---

# 对照原值与加权值的星级统计

## 入选理由

表达创新或视觉张力。保留平均与离散程度，能核查权重是否推动趋势差异

## 论证任务

比较品类的加权评分占比和文本情感

## 图型与输入

图8按星级排条，图9成对画平均与标准差，颜色复用品类。

## 视觉编码

图8按星级排条，图9成对画平均与标准差，颜色复用品类

## 重绘与迁移

注明有用度处理和总权重，对照未加权分布，核对同星级样本数

## 证据定位

- PDF 第 9 页，图8。
- PDF 第 10 页，图9。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 9 图8、10 图9给出图面、图题及正文语境。 |
| 论证表达 | 4 | 保留平均与离散程度，能核查权重是否推动趋势差异 |
| 重绘可行性 | 3 | 图8按星级排条，图9成对画平均与标准差，颜色复用品类。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 注明有用度处理和总权重，对照未加权分布，核对同星级样本数 |

总分 **17/20** · 优先借鉴
