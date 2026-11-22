---
schema: mcm-card-v1
id: "visualization-db130a3a278d-graph-label-and-ring-features"
type: visualization
title: "从全网图到同心圈点图展示标签与邻接特征"
paper:
  title: "Finding Conspirators in the Network via Machine Learning"
  year: 2012
  problem: C
source:
  pdf: "2012/ICM-C/论文/Finding Conspirators in the Network via Machine Learning.pdf"
  pdf_root: null
  sha256: "db130a3a278dd6f4a998e2a6bd812b3925dee31d27ef42a74df9d99d3bc9e86a"
  pdf_pages: [3, 6]
tags: ["网络分析", "小样本", "稳定性"]
score:
  total: 16
  max: 20
  tier: usable
---

# 从全网图到同心圈点图展示标签与邻接特征

## 入选理由

表达创新或视觉张力。局部分层视图补足全网中难辨的标签间差异。

## 论证任务

用全网关系建立语境，再展示已标注样本的邻居比例。

## 图型与输入

图1颜色区分类别，图2以同心刻度和分散角度避免点遮盖。

## 视觉编码

图1颜色区分类别，图2以同心刻度和分散角度避免点遮盖。角位置主要用于分开样本，不等于真实方向。

## 重绘与迁移

用匿名标签和两个已知邻接例验证比例，站点或主题不展示真实人员。大图用颜色加符号避免色觉误读。

## 证据定位

- PDF 第 3 页，图1。
- PDF 第 6 页，图2。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 3 图1、6 图2给出图面、图题及正文语境。 |
| 论证表达 | 4 | 局部分层视图补足全网中难辨的标签间差异。 |
| 重绘可行性 | 3 | 图1颜色区分类别，图2以同心刻度和分散角度避免点遮盖。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 2 | 主结构可辨，缩印时的细线、标注、水印或拥挤会妨碍读值。 |
| 可迁移性 | 3 | 用匿名标签和两个已知邻接例验证比例，站点或主题不展示真实人员。大图用颜色加符号避免色觉误读。 迁移时按上文检查条件和输入口径。 |

总分 **16/20** · 可借鉴
