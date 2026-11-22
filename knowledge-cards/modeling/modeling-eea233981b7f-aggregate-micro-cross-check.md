---
schema: mcm-card-v1
id: "modeling-eea233981b7f-aggregate-micro-cross-check"
type: modeling
title: "用同一场景交叉核对宏观流与个体仿真"
paper:
  title: "Three Steps to Make the Traffic Circle Go Round"
  year: 2009
  problem: A
source:
  pdf: "2009/MCM-A/论文/Three Steps to Make the Traffic Circle Go Round.pdf"
  pdf_root: null
  sha256: "eea233981b7ff452dc2317211d387904aa679fc2a57dcf0b4da5ce4fe3de0350"
  pdf_pages: [1, 4, 6, 7, 8]
tags: ["交通流", "多尺度", "交叉验证"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用同一场景交叉核对宏观流与个体仿真

## 原题与基线

环岛不同数据条件下需要比较控制配置。宏观分段模型以区段车辆数和路口流量为状态。

## 建模机制与求解

宏观模型按区段容量、入口分流和信号状态更新存量。微观模型保留单车速度、加减速、排队和局部让行规则，得到更细粒度输出。两者先用同一 Sheriffhall 来向去向流量与灯控设置，比对平均通过时间，然后决定哪些情景可用较省数据的模型。

## 验证与局限

第 8 页的共同场景中宏观 42.7 秒、微观 41.6 秒。表 2 还有参数扰动，而作者未在此处给出同口径实测通过时间。

## 迁移到新题

将同一到达和配时喂给两种粒度，统一是否计队列等待。另选高负荷情景复核策略排序。若差异集中在个体冲突或按车道输出，保留微观模型。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 260 可得期刊印刷页。

- PDF 第 4、6–7 页，Simulation Models 与表 1，宏观与微观状态以及共同场景输入
- PDF 第 8 页，Comparison and Sensitivity Analysis、表 2，通过时间和参数扰动

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 4、6–8 页给共同输入、模型细节及验证表。 |
| 机制解释力 | 4 | 宏观交换的比例流与微观加减速规则解释了信息需求差别。 |
| 实现可复现性 | 2 | 正文有两个模型规则，但复现需要完整信号和运行设置。 |
| 验证质量 | 3 | 共同场景定量对照并含扰动，缺同口径现场时间。 |
| 可迁移性 | 4 | 最小测试明确统一观测量，并以差异决定模型粒度。 |

总分 **17/20** · 优先借鉴
