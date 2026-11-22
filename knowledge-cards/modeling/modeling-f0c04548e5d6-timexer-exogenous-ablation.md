---
schema: mcm-card-v1
id: "modeling-f0c04548e5d6-timexer-exogenous-ablation"
type: modeling
title: "以外生宏观信息有无对照时间预测"
paper:
  title: "Data-Driven Policy Effectiveness Evaluation and Country-Specific Characteristic Based Cybercrime Prediction"
  year: 2025
  problem: F
source:
  pdf: "2025/ICM-F/论文/2517199.pdf"
  pdf_root: null
  sha256: "f0c04548e5d6bb282178e3f99aa7b570a11f34459fe41d03a3e6c19b044c9968"
  pdf_pages: [13, 14, 15, 16, 17, 18, 22]
tags: ["网络安全政策", "面板统计", "时间预测"]
score:
  total: 17
  max: 20
  tier: priority
---

# 以外生宏观信息有无对照时间预测

## 原题与基线

识别宏观特征是否改善未来事件数预测

## 建模机制与求解

检查异常、对比三类相关系数筛变量，以 TimeXer 接入宏观量，并与纯时序版本作样本比较

## 验证与局限

给了真实与两种预测、MAE 和 MSE；需核查训练与预测的时间划分、可用的外生输入和误差单位

## 迁移到新题

适用于多外生特征的防御容量或事件监测预测

## 证据定位

- PDF 第 13–18 页，第3.3节、表III至VI及图8–10。
- PDF 第 22 页，图14和表VII。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 13–18 第3.3节、表III至VI及图8–10、22 图14和表VII可对应假设、机制与结果。 |
| 机制解释力 | 4 | 检查异常、对比三类相关系数筛变量，以 TimeXer 接入宏观量，并与纯时序版本作样本比较。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 给了真实与两种预测、MAE 和 MSE；需核查训练与预测的时间划分、可用的外生输入和误差单位 |
| 可迁移性 | 3 | 适用于多外生特征的防御容量或事件监测预测 |

总分 **17/20** · 优先借鉴
