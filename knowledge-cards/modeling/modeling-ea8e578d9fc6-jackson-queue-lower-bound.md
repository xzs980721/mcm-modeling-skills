---
schema: mcm-card-v1
id: "modeling-ea8e578d9fc6-jackson-queue-lower-bound"
type: modeling
title: "用排队网络的稳态下界评估入口放行"
paper:
  title: "Pseudo-Finite Jackson Networks and Simulation: A Roundabout Approach to Traffic Control"
  year: 2009
  problem: A
source:
  pdf: "2009/MCM-A/论文/Pseudo-Finite Jackson Networks and Simulation.pdf"
  pdf_root: null
  sha256: "ea8e578d9fc6436157a20cc75fff393b73f0b1af8b44a41da697b4cb761a9aa5"
  pdf_pages: [1, 5, 6, 10, 11, 12]
tags: ["Jackson网络", "放行比例", "稳态下界"]
score:
  total: 18
  max: 20
  tier: priority
---

# 用排队网络的稳态下界评估入口放行

## 原题与基线

选择环岛入口让行或信号比例。解析基线把每条路当作单服务器入口队列，把环岛当作出口数对应的多服务器队列。

## 建模机制与求解

用绿灯时间比例 g 稀释入口服务，按路由矩阵求稳态流量，再求队列占用的乘积形式分布。对总车数相同的状态，用各项中最小的比值构造保守下界，检查 g 对小占用状态概率的影响。

## 验证与局限

第 10–11 页给出低占用域的推导，第 12 页同时画精确分布与下界。稳定条件和常流假设限制了让行结论的使用范围，图中的下界幅值与精确值有差别。

## 迁移到新题

替换节点服务率与转移频率。用两三个小队列枚举状态，核实下界逐点低于精确值并检查对 g 的排序一致性。排序改变时改用直接计算，排队发散时停用稳态比较。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 280 可得期刊印刷页。

- PDF 第 5–6 页，Description of Simple Queuing Network、Formulation of Stationary Distribution，流量方程
- PDF 第 10–12 页，稳态下界的推导和图 2，低占用范围

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 5–6、10–12 页有队列、级数、下界及图面对照。 |
| 机制解释力 | 4 | g 直接改变占用比值，结论只由小占用域的推导支持。 |
| 实现可复现性 | 3 | 流量方程与低状态界足以重做小实例。 |
| 验证质量 | 3 | 同时给解析推导和与精确概率的检查，大占用域证据较弱。 |
| 可迁移性 | 4 | 可用枚举检查逐点下界和策略排序。 |

总分 **18/20** · 优先借鉴
