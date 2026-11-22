---
schema: mcm-card-v1
id: "modeling-0704b0e6b069-logistic-feedback"
type: modeling
title: "在游客增长率中引入基础设施、生态和满意度反馈"
paper:
  title: "The Triangular Balance of Environment, Economy, and Society: A System Dynamics-Based Model for Sustainable Tourism Management"
  year: 2025
  problem: B
source:
  pdf: "2025/MCM-B/论文/2509557.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "0704b0e6b0695b9ec421c4a9f14c7ee4e9d7fd527c9ef5d854d742633b59e77a"
  pdf_pages: [6, 7, 11, 12, 13, 14, 15, 16, 17]
tags: ["旅游", "状态反馈", "联合灵敏度"]
score:
  total: 16
  max: 20
  tier: usable
---

# 在游客增长率中引入基础设施、生态和满意度反馈

## 原题与基线

静态游客容量不表达环境和设施的累积变化

## 建模机制与求解

用改写的 Logistic 游客式联立环境、基础设施和居民满意度状态，按税收及费额分配调制后用数值法仿真

## 验证与局限

有地区数据与参数表，政策效应与结构假设相耦合

## 迁移到新题

更换承载、恢复及折旧参数，在稳态和历史窗口分别校验

## 证据定位

- PDF 第 6–7 页，图3–6。
- PDF 第 11–17 页，式1–6、图7–8、表1–3、算法1。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 6–7 图3–6、11–17 式1–6、图7–8、表1–3、算法1可对应假设、机制与结果。 |
| 机制解释力 | 4 | 用改写的 Logistic 游客式联立环境、基础设施和居民满意度状态，按税收及费额分配调制后用数值法仿真。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 有地区数据与参数表，政策效应与结构假设相耦合 |
| 可迁移性 | 3 | 更换承载、恢复及折旧参数，在稳态和历史窗口分别校验 |

总分 **16/20** · 可借鉴
