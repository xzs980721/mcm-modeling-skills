---
schema: mcm-card-v1
id: "visualization-ae27bceb5fe0-roc-baseline-to-fusion"
type: visualization
title: "用相同坐标解释单模态与融合 ROC"
paper:
  title: "Trace the Buzz: A Comprehensive Study on the Reports About Hornets"
  year: 2021
  problem: C
source:
  pdf: "2021/MCM-C/论文/2123823.pdf"
  pdf_root: null
  sha256: "ae27bceb5fe06483285012a99b7485c963b2c3afaa663f8dea8eb22e43aac55e"
  pdf_pages: [11, 15]
tags: ["组合预测", "伪标签", "纵向模型"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用相同坐标解释单模态与融合 ROC

## 入选理由

表达创新或视觉张力。将增益放在明确假阳性区间

## 论证任务

识别可接受误报下的收益

## 图型与输入

用曲线和随机基准呈现两阶段分数。

## 视觉编码

用曲线和随机基准呈现两阶段分数

## 重绘与迁移

重绘时用相同验证集和正类，给出区间

## 证据定位

- PDF 第 11 页，图4.10。
- PDF 第 15 页，图4.17。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 11 图4.10、15 图4.17给出图面、图题及正文语境。 |
| 论证表达 | 3 | 将增益放在明确假阳性区间 |
| 重绘可行性 | 3 | 用曲线和随机基准呈现两阶段分数。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 4 | 重绘时用相同验证集和正类，给出区间 |

总分 **17/20** · 优先借鉴
