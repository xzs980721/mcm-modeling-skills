---
schema: mcm-card-v1
id: "modeling-3cc9456cbe89-separate-rating-sentiment-arima"
type: modeling
title: "分别预测星级与评论情绪并展示预测区间"
paper:
  title: "Market data tracking measurement based on sentiment analysis model and ARIMA model"
  year: 2020
  problem: C
source:
  pdf: "2020/MCM-C/论文/2009116.pdf"
  pdf_root: null
  sha256: "3cc9456cbe89f8cd28cd62b55f0b60a5ac49acafa1ab6323118955cbe7044199"
  pdf_pages: [16, 17, 18, 19]
tags: ["情感测度", "主成分", "时间预测"]
score:
  total: 16
  max: 20
  tier: usable
---

# 分别预测星级与评论情绪并展示预测区间

## 原题与基线

不同评论信号趋势和可靠区间不同

## 建模机制与求解

按时间构造星级与情绪序列，经平稳及 ACF/PACF 诊断选阶，用 ARIMA 给短期外推

## 验证与局限

给数值预测而缺同口径留出对照，评论早段稀疏

## 迁移到新题

按时间拆分并与季节持平比较，使用覆盖率及平均误差验收

## 证据定位

- PDF 第 16–19 页，图3–图7、表6和第4.2节。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 16–19 图3–图7、表6和第4.2节可对应假设、机制与结果。 |
| 机制解释力 | 3 | 按时间构造星级与情绪序列，经平稳及 ACF/PACF 诊断选阶，用 ARIMA 给短期外推。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 给数值预测而缺同口径留出对照，评论早段稀疏 |
| 可迁移性 | 4 | 按时间拆分并与季节持平比较，使用覆盖率及平均误差验收 |

总分 **16/20** · 可借鉴
