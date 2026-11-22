---
schema: mcm-card-v1
id: "visualization-c2ee18e8369d-geographic-zoom-and-bathymetry"
type: visualization
title: "三维海底色面与区域图框选对应"
paper:
  title: "Time is Life: Precise Localization and Faster Search"
  year: 2024
  problem: B
source:
  pdf: "2024/MCM-B/论文/2419984.pdf"
  pdf_root: null
  sha256: "c2ee18e8369d3eaf05c941094e6e9e02d26ffd12404e4c180ddca7f73ed0b4a9"
  pdf_pages: [6, 8, 21]
tags: ["运动仿真", "贝叶斯搜救", "空间概率"]
score:
  total: 15
  max: 20
  tier: usable
---

# 三维海底色面与区域图框选对应

## 入选理由

表达创新或视觉张力。两个区域的形状与本地海流视窗都可查

## 论证任务

定位哪片海域影响轨迹

## 图型与输入

三维地形用色条标高程，海流地图靠圈选及红框。

## 视觉编码

三维地形用色条标高程，海流地图靠圈选及红框

## 重绘与迁移

声明色标和深度正向，核对同范围纬经坐标

## 证据定位

- PDF 第 6 页，图3。
- PDF 第 8 页，图5。
- PDF 第 21 页，图14。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 3 | 6 图3、8 图5、21 图14给出图面、图题及正文语境。 |
| 论证表达 | 4 | 两个区域的形状与本地海流视窗都可查 |
| 重绘可行性 | 3 | 三维地形用色条标高程，海流地图靠圈选及红框。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 2 | 原图主结构可辨，细线、标注或水印影响缩印辨读。 |
| 可迁移性 | 3 | 声明色标和深度正向，核对同范围纬经坐标 |

总分 **15/20** · 可借鉴
