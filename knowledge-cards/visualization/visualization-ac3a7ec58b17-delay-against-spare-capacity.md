---
schema: mcm-card-v1
id: "visualization-ac3a7ec58b17-delay-against-spare-capacity"
type: visualization
title: "用剩余通行能力作横轴显示接近饱和时的延误"
paper:
  title: "A Simulation-Based Assessment of Traffic Circle Control"
  year: 2009
  problem: A
source:
  pdf: "2009/MCM-A/论文/A Simulation-Based Assessment of Traffic Circle Control.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "ac3a7ec58b173547decb985dea7ee81627b91ebfcb5eecf61ae3edd3e6af0c02"
  pdf_pages: [5, 6, 9]
tags: ["容量核对", "散点图", "剩余通行能力", "排队延误"]
score:
  total: 16
  max: 20
  tier: usable
---

# 用剩余通行能力作横轴显示接近饱和时的延误

## 论证任务

图 2 在 Validation Against Existing Empirical Models 中展示入口车辆让行策略的仿真结果。图要回答的是，当系统离最大通行能力越来越近时，车辆平均总时间如何变化。作者将观察到的反向关系与 Kimber–Hollis 延误关系作定性核对。

## 图型与输入

图中每个点需要一个平均通行率和平均总时间。用同一口径下的最大通行率减去当前平均通行率，得到剩余通行能力，单位为辆/时间步。平均总时间包含入口队列等待，单位为时间步。原文给出指标定义及相减关系，当前 PDF 未见逐点数据、运行重复数及用于计算「最大通行率」的具体取值过程。

## 视觉编码

横轴位置表示剩余通行能力，越靠左越接近饱和。纵轴位置表示平均总时间，越高表示越慢。原图使用黑点、线性坐标及明确的轴单位，未叠画经验公式。低余量附近多点聚集，原页水印覆盖部分散点，读图宜着眼于总体形态。

## 重绘与迁移

按同一场景记录 `capacity, mean_throughput, mean_total_time, completion_rate`，用统一的估算方法求 `capacity`，计算余量后画散点。先用三个已知负荷点手算横坐标，检查越饱和是否越靠左，再在低余量区域加密。若容量估计的波动足以改变余量的正负，标示不确定性并避免把拥堵起点读成精确阈值。若未完成率不可忽略，及早显示完成率和统计窗口，避免已完成样本的延误掩盖积压。缩印时核对零点位置与轴单位。

## 证据定位

- PDF 第 5–6 页，Control System Evaluation（印刷页 231–232） · 通行率和含排队总时间的定义。
- PDF 第 9 页，图 2 及解释（印刷页 235） · 横轴变换、点图、轴单位及经验关系核对。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 5–6 页指标定义与第 9 页图、轴和解释交叉对应，容量缺口已标出。 |
| 论证表达 | 4 | 余量坐标直接突出接近饱和时延误陡升的关系。 |
| 重绘可行性 | 2 | 已知变换和单位，缺逐点值与最大通行率的具体估算设置。 |
| 视觉可读性 | 2 | 轴带单位且趋势清晰，低余量点聚集并受水印影响。 |
| 可迁移性 | 4 | 包含余量手算检查、不确定性判据及积压条件。 |

总分 **16/20** · 可借鉴
