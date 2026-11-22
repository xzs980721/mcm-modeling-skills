---
schema: mcm-card-v1
id: "visualization-fdea9a86d39f-embedding-to-stacked-memory"
type: visualization
title: "用架构图和输入字典对齐双层记忆单元"
paper:
  title: "Beat The Market: Comprehensive Exploration of Amazon Reviews and Ratings"
  year: 2020
  problem: C
source:
  pdf: "2020/MCM-C/论文/2003717.pdf"
  pdf_root: null
  sha256: "fdea9a86d39f65f6fb78db23457eb9997d577b1ce29a319da04ccd243deef937"
  pdf_pages: [14, 15]
tags: ["LDA", "声誉窗口", "评分文本一致性"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用架构图和输入字典对齐双层记忆单元

## 入选理由

表达创新或视觉张力。模型输入何时合并、何处变成预测值可直接核对

## 论证任务

说明文本和结构化特征的融入点

## 图型与输入

分区画输入、双层循环单元及输出，旁表列向量分量及维度。

## 视觉编码

分区画输入、双层循环单元及输出，旁表列向量分量及维度

## 重绘与迁移

标张量形状和时间步，逐层核验维度及归一化口径

## 证据定位

- PDF 第 14 页，图12、表3。
- PDF 第 15 页，表4。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 14 图12、表3、15 表4给出图面、图题及正文语境。 |
| 论证表达 | 4 | 模型输入何时合并、何处变成预测值可直接核对 |
| 重绘可行性 | 3 | 分区画输入、双层循环单元及输出，旁表列向量分量及维度。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 标张量形状和时间步，逐层核验维度及归一化口径 |

总分 **17/20** · 优先借鉴
