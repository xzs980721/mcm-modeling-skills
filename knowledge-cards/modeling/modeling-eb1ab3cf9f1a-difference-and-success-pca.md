---
schema: mcm-card-v1
id: "modeling-eb1ab3cf9f1a-difference-and-success-pca"
type: modeling
title: "差分预测五指标后用主成分构建成功指数"
paper:
  title: "Strategies to Online Sales: A Review-tracking System Combined with Deep Learning and Difference Equation Model"
  year: 2020
  problem: C
source:
  pdf: "2020/MCM-C/论文/2007707.pdf"
  pdf_root: null
  sha256: "eb1ab3cf9f1a49a9a49c171e77a0d808b12109066b68957e7348a6bde93b7fc4"
  pdf_pages: [16, 17, 18, 19, 20, 21, 22, 30, 31, 32]
tags: ["文本评分", "差分方程", "成功指数"]
score:
  total: 16
  max: 20
  tier: usable
---

# 差分预测五指标后用主成分构建成功指数

## 原题与基线

不同指标时序互动、量纲与权重不一致

## 建模机制与求解

用 ACF/PACF 及相关表选择滞后项，拟合指标差分，然后按标准化主成分贡献合成指数

## 验证与局限

按销量代理分组及删减期限做核查，等级受代理和期数影响

## 迁移到新题

复核平稳性，估计只用训练窗，留出检验指数排序和预测增益

## 证据定位

- PDF 第 16–22 页，图16–图18、表3–表8。
- PDF 第 30–32 页，附录C–G。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 16–22 图16–图18、表3–表8、30–32 附录C–G可对应假设、机制与结果。 |
| 机制解释力 | 3 | 用 ACF/PACF 及相关表选择滞后项，拟合指标差分，然后按标准化主成分贡献合成指数。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 按销量代理分组及删减期限做核查，等级受代理和期数影响 |
| 可迁移性 | 4 | 复核平稳性，估计只用训练窗，留出检验指数排序和预测增益 |

总分 **16/20** · 可借鉴
