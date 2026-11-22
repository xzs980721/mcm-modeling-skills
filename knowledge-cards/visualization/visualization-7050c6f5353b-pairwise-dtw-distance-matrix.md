---
schema: mcm-card-v1
id: "visualization-7050c6f5353b-pairwise-dtw-distance-matrix"
type: visualization
title: "用成对距离热图核验多套排序的一致性"
paper:
  title: "Riddle of Sphinx: Cracking the Secret of Amazon’s Ratings and Reviews"
  year: 2020
  problem: C
source:
  pdf: "2020/MCM-C/论文/2002116.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "7050c6f5353b68e4339fcc261cc0377886372f98ae875cdd0310f1b53a8e1b0e"
  pdf_pages: [12]
tags: ["情感评分", "评论信息量", "声誉预测"]
score:
  total: 18
  max: 20
  tier: priority
---

# 用成对距离热图核验多套排序的一致性

## 入选理由

表达创新或视觉张力。色阶和数值让最接近及偏离较大的配置可见

## 论证任务

定量检查筛选权重改变后排序是否类似

## 图型与输入

双轴排列相同参数组合，方格显示 DTW 距离。

## 视觉编码

双轴排列相同参数组合，方格显示 DTW 距离

## 重绘与迁移

按固定顺序排序，校验矩阵对称、对角线零值和尺度

## 证据定位

- PDF 第 12 页，图5。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 12 图5给出图面、图题及正文语境。 |
| 论证表达 | 4 | 色阶和数值让最接近及偏离较大的配置可见 |
| 重绘可行性 | 3 | 双轴排列相同参数组合，方格显示 DTW 距离。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 4 | 按固定顺序排序，校验矩阵对称、对角线零值和尺度 |

总分 **18/20** · 优先借鉴
