---
schema: mcm-card-v1
id: "visualization-20f6a4251d26-shape-search-to-surrogate-panels"
type: visualization
title: "用四面板展示几何优化从候选到简式近似"
paper:
  title: "A Half-Blood Half-Pipe, A Perfect Performance"
  year: 2011
  problem: A
source:
  pdf: "2011/MCM-A/论文/A Half-Blood Half-Pipe, A Perfect Performance.pdf"
  pdf_root: null
  sha256: "20f6a4251d26dfbfcb2caa3b66ff24340333d995d0c389f1d2ab46c299d6fd38"
  pdf_pages: [10, 11]
tags: ["多面板", "形状优化", "收敛诊断"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用四面板展示几何优化从候选到简式近似

## 论证任务

图 5 将候选形状、适应度、优化赛道和椭圆近似连续展示。

## 图型与输入

输入为初代及终代曲线控制点和适应度、最终几何采样点、二次曲线拟合结果。原页没有逐点数值。

## 视觉编码

上排由初代到终代，各含蓝色候选曲线和适应度小图。下排先给整体几何，再放大待拟合的过渡段，以局部曲线和完整椭圆形轨迹对照拟合关系。

## 重绘与迁移

用相同候选坐标范围比较初终代，给简式拟合加残差小图。抽取三个断面点比较近似误差，在栏宽预览标注和小图。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 108 可得期刊印刷页。

- PDF 第 10–11 页，Question 1 与图 5(a)–(d)，参数、候选形态、适应度和拟合的对应关系

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 11 页图 5 的四个面板与算法说明对应。 |
| 论证表达 | 4 | 读者能依序检查搜索前后、整体方案和局部近似。 |
| 重绘可行性 | 3 | 可用曲线与适应度重画，原搜索数据未附。 |
| 视觉可读性 | 2 | 缩印会影响适应度小图与坐标。 |
| 可迁移性 | 4 | 提供同尺度及残差检查的最小复绘。 |

总分 **17/20** · 优先借鉴
