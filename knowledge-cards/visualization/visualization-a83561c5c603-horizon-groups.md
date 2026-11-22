---
schema: mcm-card-v1
id: "visualization-a83561c5c603-horizon-groups"
type: visualization
title: "按预测步长分组比较训练策略"
paper:
  title: "Command the Flow: Analysis and Prediction of Momentum in Tennis Matches"
  year: 2024
  problem: C
source:
  pdf: "2024/MCM-C/论文/2406324.pdf"
  pdf_root: null
  sha256: "a83561c5c6030213d72c2c295e21f78c68e9409e087abffbc0495ed325e9be94"
  pdf_pages: [18]
tags: ["网球", "滤波", "迁移"]
score:
  total: 16
  max: 20
  tier: usable
---

# 按预测步长分组比较训练策略

## 入选理由

表达创新或视觉张力。同一预测步长内可横向选策略

## 论证任务

看收益是否随预测跨度改变

## 图型与输入

分组柱对应步长，柱色对应训练方案。

## 视觉编码

分组柱对应步长，柱色对应训练方案

## 重绘与迁移

补共同测试集和误差定义

## 证据定位

- PDF 第 18 页，图14。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 3 | 18 图14给出图面、图题及正文语境。 |
| 论证表达 | 4 | 同一预测步长内可横向选策略 |
| 重绘可行性 | 3 | 分组柱对应步长，柱色对应训练方案。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 补共同测试集和误差定义 |

总分 **16/20** · 可借鉴
