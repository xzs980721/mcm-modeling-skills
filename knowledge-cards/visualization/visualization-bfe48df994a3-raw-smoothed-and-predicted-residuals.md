---
schema: mcm-card-v1
id: "visualization-bfe48df994a3-raw-smoothed-and-predicted-residuals"
type: visualization
title: "沿逐分横轴比较原始、平滑和预测残差"
paper:
  title: "\"Momentum\" Exists In Tennis Game As Residual Effect - A Dual-Temporal Bayesian Network Model"
  year: 2024
  problem: C
source:
  pdf: "2024/MCM-C/论文/2401298.pdf"
  pdf_root: null
  sha256: "bfe48df994a311d261217a6b597118ee42bda6906e200c3acf31a4a4d11f7422"
  pdf_pages: [17, 20]
tags: ["发球校正", "残差势头", "动态贝叶斯"]
score:
  total: 16
  max: 20
  tier: usable
---

# 沿逐分横轴比较原始、平滑和预测残差

## 入选理由

表达创新或视觉张力。可按时点分辨滤波增益及预测误差

## 论证任务

查看真实转向是否被提前或滞后

## 图型与输入

淡线与主拟合线同轴，不同比赛片段分图。

## 视觉编码

淡线与主拟合线同轴，不同比赛片段分图

## 重绘与迁移

列样本来源和窗宽，估计转折延时与留出残差

## 证据定位

- PDF 第 17 页，图11。
- PDF 第 20 页，图13。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 17 图11、20 图13给出图面、图题及正文语境。 |
| 论证表达 | 4 | 可按时点分辨滤波增益及预测误差 |
| 重绘可行性 | 3 | 淡线与主拟合线同轴，不同比赛片段分图。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 2 | 原图主结构可辨，细线、标注或水印影响缩印辨读。 |
| 可迁移性 | 3 | 列样本来源和窗宽，估计转折延时与留出残差 |

总分 **16/20** · 可借鉴
