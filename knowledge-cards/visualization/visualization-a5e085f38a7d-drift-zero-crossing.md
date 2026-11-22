---
schema: mcm-card-v1
id: "visualization-a5e085f38a7d-drift-zero-crossing"
type: visualization
title: "用存量漂移的过零点辨认稳定平衡"
paper:
  title: "One Ring to Rule Them All: The Optimization of Traffic Circles"
  year: 2009
  problem: A
source:
  pdf: "2009/MCM-A/论文/One Ring to Rule Them All.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "a5e085f38a7d0ca2082301592f7d48d5fdc6aff5348c2c0a268af8ad4d129b22"
  pdf_pages: [7, 8]
tags: ["稳态", "漂移曲线", "容量"]
score:
  total: 18
  max: 20
  tier: priority
---

# 用存量漂移的过零点辨认稳定平衡

## 论证任务

图 3 比较不同在环车辆数下的净流量，支持正文对两个数学根的稳定性判断。

## 图型与输入

图中横轴 C 为环内车辆数，纵轴为 dC/dt，数据可按图注固定入口、离开和容量参数计算。

## 视觉编码

用一条曲线画净增速，并保留水平零线。容量 30 辆只在图注给出。较高的根超出所设容量范围时须在图注标记。

## 重绘与迁移

对新系统在两个数值根附近代入扰动点，核对漂移方向，同时把物理可行区和数学延长区清楚标出。缩印后确认零线能和曲线分辨。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 246 可得期刊印刷页。

- PDF 第 7 页，Analyzing the Models，从固定服务率到占用反馈
- PDF 第 8 页，图 3 和紧随其后的稳定性解释，参数、坐标与过零点

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 8 页曲线、参数图注与根的推导相互补充。 |
| 论证表达 | 4 | 过零与符号能读出两根稳定性。 |
| 重绘可行性 | 3 | 给了坐标单位和示例参数，可重算主要曲线。 |
| 视觉可读性 | 3 | 主线和零线可辨，但原图跨出可行占用域。 |
| 可迁移性 | 4 | 可用两个根附近的符号与物理范围测试复绘。 |

总分 **18/20** · 优先借鉴
