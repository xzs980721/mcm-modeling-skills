---
schema: mcm-card-v1
id: "visualization-86e7a4f375f7-score-bands"
type: visualization
title: "时间线叠加得分色带和动量"
paper:
  title: "Uncovering the Hidden Momentum: A Data-Science Exploration of Tennis Match Dynamics"
  year: 2024
  problem: C
source:
  pdf: "2024/MCM-C/论文/2403774.pdf"
  pdf_root: null
  sha256: "86e7a4f375f7e1be1a13c0c9d29154cf60a201f86de9974ac083a611f30231e9"
  pdf_pages: [13, 21]
tags: ["网球", "异常处理", "因果卷积"]
score:
  total: 17
  max: 20
  tier: priority
---

# 时间线叠加得分色带和动量

## 入选理由

表达创新或视觉张力。逐分条带保留局部事件，平滑走势提供全局节奏

## 论证任务

同时看短期交替和长期势头

## 图型与输入

底层按点绘制垂直窄带，上层叠连续指标线。

## 视觉编码

底层按点绘制垂直窄带，上层叠连续指标线

## 重绘与迁移

用低饱和彩色或纹理压低背景干扰

## 证据定位

- PDF 第 13 页，图7。
- PDF 第 21 页，图17。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 13 图7、21 图17给出图面、图题及正文语境。 |
| 论证表达 | 4 | 逐分条带保留局部事件，平滑走势提供全局节奏 |
| 重绘可行性 | 3 | 底层按点绘制垂直窄带，上层叠连续指标线。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 用低饱和彩色或纹理压低背景干扰 |

总分 **17/20** · 优先借鉴
