---
schema: mcm-card-v1
id: "visualization-00c7420c324b-image-shape-through-cnn"
type: visualization
title: "以特征块与线网表示卷积网络"
paper:
  title: "Fighting the Horde: a Comprehensive Model for Monitoring and Controlling Hornet Invasions"
  year: 2021
  problem: C
source:
  pdf: "2021/MCM-C/论文/2101587.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "00c7420c324bc69c8b9783f018babc06eed8c36035a3159e2e35dca88ae3cc0e"
  pdf_pages: [11]
tags: ["事件筛查", "图像裁剪", "优先级"]
score:
  total: 18
  max: 20
  tier: priority
---

# 以特征块与线网表示卷积网络

## 入选理由

表达创新或视觉张力。图层厚度和空间缩减直观展示表征变换

## 论证任务

检查图像到类别的形状路径

## 图型与输入

用特征图组、连接和输出节点标示卷积、汇聚及分类。

## 视觉编码

用特征图组、连接和输出节点标示卷积、汇聚及分类

## 重绘与迁移

用实际张量形状绘制图层，确认会改变维度的算子清楚可读

## 证据定位

- PDF 第 11 页，图6。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 11 图6给出图面、图题及正文语境。 |
| 论证表达 | 4 | 图层厚度和空间缩减直观展示表征变换 |
| 重绘可行性 | 3 | 用特征图组、连接和输出节点标示卷积、汇聚及分类。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 4 | 用实际张量形状绘制图层，确认会改变维度的算子清楚可读 |

总分 **18/20** · 优先借鉴
