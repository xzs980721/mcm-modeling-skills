---
schema: mcm-card-v1
id: "visualization-801e10daa2da-image-model-architecture-tensors"
type: visualization
title: "用几何层块标记分类与重建架构"
paper:
  title: "Fight for Washington State: Can Artificial Intelligence Beat the Asian Giant Hornet?"
  year: 2021
  problem: C
source:
  pdf: "2021/MCM-C/论文/2101166.pdf"
  pdf_root: null
  sha256: "801e10daa2dab997a1389b9e26414c5c96b941046bc849d0deaed227352e0137"
  pdf_pages: [9, 10, 25]
tags: ["事件分类", "图像质量诊断", "时序监测"]
score:
  total: 19
  max: 20
  tier: priority
---

# 用几何层块标记分类与重建架构

## 入选理由

表达创新或视觉张力。图区分张量尺寸变化和两类输出路径

## 论证任务

定位编码后如何分流和恢复表征

## 图型与输入

网络层以相连的几何框表示，依序标记空间尺度及输出角色。

## 视觉编码

网络层以相连的几何框表示，依序标记空间尺度及输出角色

## 重绘与迁移

从网络定义导出实际输入输出形状，把公共编码器与分支口分别标清

## 证据定位

- PDF 第 9 页，图4。
- PDF 第 10 页，图5。
- PDF 第 25 页，备忘录架构简图。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 9 图4、10 图5、25 备忘录架构简图给出图面、图题及正文语境。 |
| 论证表达 | 4 | 图区分张量尺寸变化和两类输出路径 |
| 重绘可行性 | 4 | 网络层以相连的几何框表示，依序标记空间尺度及输出角色。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 4 | 从网络定义导出实际输入输出形状，把公共编码器与分支口分别标清 |

总分 **19/20** · 优先借鉴
