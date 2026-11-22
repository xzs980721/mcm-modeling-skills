---
schema: mcm-card-v1
id: "visualization-ea8e578d9fc6-exact-bound-surfaces"
type: visualization
title: "以双面板对照精确概率面与解析下界"
paper:
  title: "Pseudo-Finite Jackson Networks and Simulation: A Roundabout Approach to Traffic Control"
  year: 2009
  problem: A
source:
  pdf: "2009/MCM-A/论文/Pseudo-Finite Jackson Networks and Simulation.pdf"
  pdf_root: null
  sha256: "ea8e578d9fc6436157a20cc75fff393b73f0b1af8b44a41da697b4cb761a9aa5"
  pdf_pages: [10, 11, 12]
tags: ["概率曲面", "下界", "诊断"]
score:
  total: 16
  max: 20
  tier: usable
---

# 以双面板对照精确概率面与解析下界

## 论证任务

图 2 的任务是让读者比较真实稳态分布与下界在不等入口流量下的形状。

## 图型与输入

两幅 3D 网格面用总车数和放行参数 g 作输入，输出概率或下界，按同一个参数设置计算。

## 视觉编码

上图是精确值，下图是下界，同一组方向和网格呈现趋势。两个竖轴尺度不同，曲面视觉高度不能直接当作误差。上图竖轴也印成下界，以分图题 (a) Actual value 和正文为准。

## 重绘与迁移

生成相同输入网格，统一竖轴或增列差值图。用一个已知状态检查下界不越上界，再在单栏尺寸检查轴符号和各面板标题。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 280 可得期刊印刷页。

- PDF 第 10–11 页，下界推导，需保持一致的总车数状态定义
- PDF 第 12 页，图 2(a)–(b)，两个曲面的输入和不同纵轴

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 10–12 页提供下界公式、图注说明及坐标标签矛盾。 |
| 论证表达 | 3 | 曲面支持查看趋势，但上下图幅值仍需读轴。 |
| 重绘可行性 | 3 | 主要输入与示例入口流量可定位。 |
| 视觉可读性 | 2 | 两面板轴小、范围差异大，顶部纵轴标签易误导。 |
| 可迁移性 | 4 | 可统一尺度并逐点检查差值方向。 |

总分 **16/20** · 可借鉴
