---
schema: mcm-card-v1
id: "visualization-00c7420c324b-class-error-matrix"
type: visualization
title: "灰阶混淆矩阵呈现多类别误分位置"
paper:
  title: "Fighting the Horde: a Comprehensive Model for Monitoring and Controlling Hornet Invasions"
  year: 2021
  problem: C
source:
  pdf: "2021/MCM-C/论文/2101587.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "00c7420c324bc69c8b9783f018babc06eed8c36035a3159e2e35dca88ae3cc0e"
  pdf_pages: [13]
tags: ["事件筛查", "图像裁剪", "优先级"]
score:
  total: 17
  max: 20
  tier: priority
---

# 灰阶混淆矩阵呈现多类别误分位置

## 入选理由

表达创新或视觉张力。让严重误分在网格中有可定位坐标

## 论证任务

分辨错误集中在哪些真实与预测标签

## 图型与输入

按真实和预测轴组织灰阶单元，旁列连续色标。

## 视觉编码

按真实和预测轴组织灰阶单元，旁列连续色标

## 重绘与迁移

核实矩阵归一方向及标签顺序，补充原始样本数

## 证据定位

- PDF 第 13 页，图8。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 13 图8给出图面、图题及正文语境。 |
| 论证表达 | 3 | 让严重误分在网格中有可定位坐标 |
| 重绘可行性 | 3 | 按真实和预测轴组织灰阶单元，旁列连续色标。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 4 | 核实矩阵归一方向及标签顺序，补充原始样本数 |

总分 **17/20** · 优先借鉴
