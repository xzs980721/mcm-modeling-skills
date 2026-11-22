---
schema: mcm-card-v1
id: "visualization-eb1ab3cf9f1a-label-quality-ablation-panels"
type: visualization
title: "用平行时间曲线展示去掉不同份额人工校正的影响"
paper:
  title: "Strategies to Online Sales: A Review-tracking System Combined with Deep Learning and Difference Equation Model"
  year: 2020
  problem: C
source:
  pdf: "2020/MCM-C/论文/2007707.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "eb1ab3cf9f1a49a9a49c171e77a0d808b12109066b68957e7348a6bde93b7fc4"
  pdf_pages: [21, 22]
tags: ["文本评分", "差分方程", "成功指数"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用平行时间曲线展示去掉不同份额人工校正的影响

## 入选理由

表达创新或视觉张力。同构图的尖峰可比较，表量化标签和数据扰动

## 论证任务

检查模型对人工校正比例和观测数量的敏感性

## 图型与输入

并列正常、减少5%与10%校正，表给变更幅度。

## 视觉编码

并列正常、减少5%与10%校正，表给变更幅度

## 重绘与迁移

固定重抽样种子和测试例，按多次重复报告误差

## 证据定位

- PDF 第 21 页，图18、表7。
- PDF 第 22 页，表8。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 21 图18、表7、22 表8给出图面、图题及正文语境。 |
| 论证表达 | 4 | 同构图的尖峰可比较，表量化标签和数据扰动 |
| 重绘可行性 | 3 | 并列正常、减少5%与10%校正，表给变更幅度。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 固定重抽样种子和测试例，按多次重复报告误差 |

总分 **17/20** · 优先借鉴
