---
schema: mcm-card-v1
id: "visualization-801e10daa2da-classifier-training-route-layout"
type: visualization
title: "复用编码器的分类及重建流程板"
paper:
  title: "Fight for Washington State: Can Artificial Intelligence Beat the Asian Giant Hornet?"
  year: 2021
  problem: C
source:
  pdf: "2021/MCM-C/论文/2101166.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "801e10daa2dab997a1389b9e26414c5c96b941046bc849d0deaed227352e0137"
  pdf_pages: [13]
tags: ["事件分类", "图像质量诊断", "时序监测"]
score:
  total: 18
  max: 20
  tier: priority
---

# 复用编码器的分类及重建流程板

## 入选理由

表达创新或视觉张力。同一结构上标明训练对象、重建目标和分类输出的关系

## 论证任务

查清损失施加在哪个支路及何时训练

## 图型与输入

按输入、共享编码和输出排列，各训练路径用不同连结。

## 视觉编码

按输入、共享编码和输出排列，各训练路径用不同连结

## 重绘与迁移

绘制只含可证实模块的分支并注明何处冻结或更新

## 证据定位

- PDF 第 13 页，图8。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 13 图8给出图面、图题及正文语境。 |
| 论证表达 | 4 | 同一结构上标明训练对象、重建目标和分类输出的关系 |
| 重绘可行性 | 3 | 按输入、共享编码和输出排列，各训练路径用不同连结。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 4 | 绘制只含可证实模块的分支并注明何处冻结或更新 |

总分 **18/20** · 优先借鉴
