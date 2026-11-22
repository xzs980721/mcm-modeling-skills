---
schema: mcm-card-v1
id: "visualization-fdea9a86d39f-window-sensitive-reputation-panels"
type: visualization
title: "以两种窗口对比声誉波动并标预测续段"
paper:
  title: "Beat The Market: Comprehensive Exploration of Amazon Reviews and Ratings"
  year: 2020
  problem: C
source:
  pdf: "2020/MCM-C/论文/2003717.pdf"
  pdf_root: null
  sha256: "fdea9a86d39f65f6fb78db23457eb9997d577b1ce29a319da04ccd243deef937"
  pdf_pages: [13, 16]
tags: ["LDA", "声誉窗口", "评分文本一致性"]
score:
  total: 17
  max: 20
  tier: priority
---

# 以两种窗口对比声誉波动并标预测续段

## 入选理由

表达创新或视觉张力。同一三产品可比较平滑和预测方向

## 论证任务

判断窗口扩大后波动是否稳定，以及未来段是否偏离

## 图型与输入

每行并列三产品，一组改变窗大小，预测图蓝色与红色切分历史和未来。

## 视觉编码

每行并列三产品，一组改变窗大小，预测图蓝色与红色切分历史和未来

## 重绘与迁移

标明窗口是评论数或时间，保持同日期尺度并单列未来误差

## 证据定位

- PDF 第 13 页，图10、图11。
- PDF 第 16 页，图13。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 13 图10、图11、16 图13给出图面、图题及正文语境。 |
| 论证表达 | 4 | 同一三产品可比较平滑和预测方向 |
| 重绘可行性 | 3 | 每行并列三产品，一组改变窗大小，预测图蓝色与红色切分历史和未来。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 标明窗口是评论数或时间，保持同日期尺度并单列未来误差 |

总分 **17/20** · 优先借鉴
