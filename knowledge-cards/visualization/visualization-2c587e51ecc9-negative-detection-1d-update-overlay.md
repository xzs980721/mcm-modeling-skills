---
schema: mcm-card-v1
id: "visualization-2c587e51ecc9-negative-detection-1d-update-overlay"
type: visualization
title: "用一维切片直观证明未检出如何改写概率"
paper:
  title: "Into the Void: A Probabilistic Approach to the Search for Missing Aircraft"
  year: 2015
  problem: B
source:
  pdf: "2015/MCM-B/论文/32879.pdf"
  pdf_root: null
  sha256: "2c587e51ecc9209b9e7553cb1ade060b1a6b5581a54773a57fdbb5eb56dd6c54"
  pdf_pages: [12]
tags: ["贝叶斯更新", "搜索救援", "路径比较"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用一维切片直观证明未检出如何改写概率

## 入选理由

表达创新或视觉张力。在同一函数上显示局部搜索区突降，有解释力。

## 论证任务

阐释对未发现证据进行条件化。

## 图型与输入

横轴为一维位置，纵轴概率量，叠初始与更新曲线，中间搜索段压低。

## 视觉编码

横轴为一维位置，纵轴概率量，叠初始与更新曲线，中间搜索段压低。

## 重绘与迁移

标被搜索区间、探测概率及归一规则，以最小例验离散积分。

## 证据定位

- PDF 第 12 页，图6。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 3 | 12 图6可定位主要细节，评分按这些明确来源。 |
| 论证表达 | 4 | 在同一函数上显示局部搜索区突降，有解释力。 |
| 重绘可行性 | 4 | 横轴为一维位置，纵轴概率量，叠初始与更新曲线，中间搜索段压低。 |
| 视觉可读性 | 3 | 关键图式及标签可辨，缩印下需要复核局部颜色、比例或字重。 |
| 可迁移性 | 3 | 标被搜索区间、探测概率及归一规则，以最小例验离散积分。 迁移时按上文检查条件和输入口径。 |

总分 **17/20** · 优先借鉴
