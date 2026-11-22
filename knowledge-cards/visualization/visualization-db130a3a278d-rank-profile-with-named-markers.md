---
schema: mcm-card-v1
id: "visualization-db130a3a278d-rank-profile-with-named-markers"
type: visualization
title: "在连续排序曲线上加少量重点样本标记"
paper:
  title: "Finding Conspirators in the Network via Machine Learning"
  year: 2012
  problem: C
source:
  pdf: "2012/ICM-C/论文/Finding Conspirators in the Network via Machine Learning.pdf"
  pdf_root: null
  sha256: "db130a3a278dd6f4a998e2a6bd812b3925dee31d27ef42a74df9d99d3bc9e86a"
  pdf_pages: [8, 9]
tags: ["网络分析", "小样本", "稳定性"]
score:
  total: 17
  max: 20
  tier: priority
---

# 在连续排序曲线上加少量重点样本标记

## 入选理由

表达创新或视觉张力。将数值表与打分长尾连起来，保留特定样本位置。

## 论证任务

显示排序集中度及示例点相对于其余节点的位置。

## 图型与输入

横轴优先级名次，纵轴模型分数。

## 视觉编码

横轴优先级名次，纵轴模型分数。折线沿排序，符号区分需说明的样本，表给排名领先的一小组。

## 重绘与迁移

用匿名 ID，标出并列处理。抽查两个名次及其相邻分数，勿将断点误读成真实概率界。

## 证据定位

- PDF 第 8 页，表2。
- PDF 第 9 页，图3。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 8 表2、9 图3给出图面、图题及正文语境。 |
| 论证表达 | 4 | 将数值表与打分长尾连起来，保留特定样本位置。 |
| 重绘可行性 | 3 | 横轴优先级名次，纵轴模型分数。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 用匿名 ID，标出并列处理。抽查两个名次及其相邻分数，勿将断点误读成真实概率界。 迁移时按上文检查条件和输入口径。 |

总分 **17/20** · 优先借鉴
