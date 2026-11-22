---
schema: mcm-card-v1
id: "visualization-8f072f334633-cost-surface-with-colorbar"
type: visualization
title: "两个费用轴共同进入收益曲面"
paper:
  title: "PADRRI: Prediction And Decision Models For Best Return And Risk With High Interpretability"
  year: 2022
  problem: C
source:
  pdf: "2022/MCM-C/论文/2200688.pdf"
  pdf_root: null
  sha256: "8f072f3346333a2c59786c46ab623501d9366b484aa5f995bf522e5a3aa50554"
  pdf_pages: [20]
tags: ["分解预测", "滑动窗口", "交易成本"]
score:
  total: 19
  max: 20
  tier: priority
---

# 两个费用轴共同进入收益曲面

## 入选理由

表达创新或视觉张力。一图展示双费用扰动与阈值面

## 论证任务

定位陡降区和相对平缓区

## 图型与输入

交易费各为一底面坐标，高度和颜色都映射同一结果。

## 视觉编码

交易费各为一底面坐标，高度和颜色都映射同一结果

## 重绘与迁移

由二维参数网格重绘，标费率单位并配平面截面验证

## 证据定位

- PDF 第 20 页，图12。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 20 图12给出图面、图题及正文语境。 |
| 论证表达 | 4 | 一图展示双费用扰动与阈值面 |
| 重绘可行性 | 4 | 交易费各为一底面坐标，高度和颜色都映射同一结果。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 4 | 由二维参数网格重绘，标费率单位并配平面截面验证 |

总分 **19/20** · 优先借鉴
