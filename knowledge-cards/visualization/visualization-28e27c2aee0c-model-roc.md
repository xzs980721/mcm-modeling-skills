---
schema: mcm-card-v1
id: "visualization-28e27c2aee0c-model-roc"
type: visualization
title: "以三面固定 ROC 参考对照分类器"
paper:
  title: "Revealing the Hidden Forces Shaping Olympic Success"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2516178.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "28e27c2aee0cfcda7dccb21061565665099698220e0ae2b39d82367764aa8f02"
  pdf_pages: [9]
tags: ["双阶段预测", "重采样", "DID"]
score:
  total: 17
  max: 20
  tier: priority
---

# 以三面固定 ROC 参考对照分类器

## 入选理由

表达创新或视觉张力。同类对角基线可见不同模型的偏离

## 论证任务

检查过滤级的分类效果

## 图型与输入

每面一种算法、相同 FPR 和 TPR 轴。

## 视觉编码

每面一种算法、相同 FPR 和 TPR 轴

## 重绘与迁移

统一折及基准率，标 AUC

## 证据定位

- PDF 第 9 页，图4。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 9 图4给出图面、图题及正文语境。 |
| 论证表达 | 4 | 同类对角基线可见不同模型的偏离 |
| 重绘可行性 | 3 | 每面一种算法、相同 FPR 和 TPR 轴。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 统一折及基准率，标 AUC |

总分 **17/20** · 优先借鉴
