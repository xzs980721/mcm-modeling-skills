---
schema: mcm-card-v1
id: "visualization-054d7c394a43-rank-deviation-parameter-line"
type: visualization
title: "以多步扰动下的相对偏差走势检查尖峰"
paper:
  title: "Methods of Measuring Influence Using Network Model"
  year: 2014
  problem: C
source:
  pdf: "2014/ICM-C/论文/28747.pdf"
  pdf_root: null
  sha256: "054d7c394a43f4c3c1714fded14fc1a40d8a623901f276672b76578864d5d4d1"
  pdf_pages: [20]
tags: ["节点删除", "PageRank", "带符号排名差"]
score:
  total: 15
  max: 20
  tier: usable
---

# 以多步扰动下的相对偏差走势检查尖峰

## 入选理由

表达创新或视觉张力。峰谷提示结果对不同扰动水平非平滑。

## 论证任务

查选定 u 的模型输出偏差。

## 图型与输入

横轴扰动参数 u，纵轴 Deviation Degree，以折线连接离散样本。

## 视觉编码

横轴扰动参数 u，纵轴 Deviation Degree，以折线连接离散样本。

## 重绘与迁移

增加未扰动基线并复算同一度量，至少多种扰动重复。

## 证据定位

- PDF 第 20 页，图7。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 3 | 20 图7可定位主要细节，评分按这些明确来源。 |
| 论证表达 | 4 | 峰谷提示结果对不同扰动水平非平滑。 |
| 重绘可行性 | 3 | 主要字段、尺度及面板关系可据上文重绘。 |
| 视觉可读性 | 2 | 主结构可辨，缩印时的细线、标注、水印或拥挤会妨碍读值。 |
| 可迁移性 | 3 | 增加未扰动基线并复算同一度量，至少多种扰动重复。 迁移时按上文检查条件和输入口径。 |

总分 **15/20** · 可借鉴
