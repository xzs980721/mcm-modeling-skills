---
schema: mcm-card-v1
id: "visualization-bfe48df994a3-repeated-bayes-block-with-temporal-links"
type: visualization
title: "重用单层网络并用跨层箭头画时间依赖"
paper:
  title: "\"Momentum\" Exists In Tennis Game As Residual Effect - A Dual-Temporal Bayesian Network Model"
  year: 2024
  problem: C
source:
  pdf: "2024/MCM-C/论文/2401298.pdf"
  pdf_root: null
  sha256: "bfe48df994a311d261217a6b597118ee42bda6906e200c3acf31a4a4d11f7422"
  pdf_pages: [16, 21]
tags: ["发球校正", "残差势头", "动态贝叶斯"]
score:
  total: 17
  max: 20
  tier: priority
---

# 重用单层网络并用跨层箭头画时间依赖

## 入选理由

表达创新或视觉张力。复制模块后，新增跨层关系在相同位置容易找到

## 论证任务

区分单点特征和两层时间信息

## 图型与输入

单层框保持节点类别，跨层线另编码。

## 视觉编码

单层框保持节点类别，跨层线另编码

## 重绘与迁移

明确时间下标，以无跨层设定检查模型是否退化

## 证据定位

- PDF 第 16 页，图9–10。
- PDF 第 21 页，图15。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 16 图9–10、21 图15给出图面、图题及正文语境。 |
| 论证表达 | 4 | 复制模块后，新增跨层关系在相同位置容易找到 |
| 重绘可行性 | 4 | 单层框保持节点类别，跨层线另编码。 |
| 视觉可读性 | 2 | 原图主结构可辨，细线、标注或水印影响缩印辨读。 |
| 可迁移性 | 3 | 明确时间下标，以无跨层设定检查模型是否退化 |

总分 **17/20** · 优先借鉴
