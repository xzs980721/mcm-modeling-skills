---
schema: mcm-card-v1
id: "modeling-d77e804d8263-gmm-traffic"
type: modeling
title: "以固定脚印结构的混合分布反推并行人数"
paper:
  title: "Step Chronicles: A Multiscale Model Linking Wear Patterns and Temporal Use in Ancient Staircases"
  year: 2025
  problem: A
source:
  pdf: "2025/MCM-A/论文/2501567.pdf"
  pdf_root: null
  sha256: "d77e804d8263a4a2425a2b66afb09a71b14fa2c24afa9c6ec94ad058c7bda040"
  pdf_pages: [12, 13, 14, 15, 16, 17]
tags: ["Archard 磨损", "混合分布", "寿命"]
score:
  total: 16
  max: 20
  tier: usable
---

# 以固定脚印结构的混合分布反推并行人数

## 原题与基线

来自不同通行者和左右脚的磨损峰互相重叠

## 建模机制与求解

将踩踏位置假定为双维混合正态，以 EM 拟合分布，并用 BIC 及脚数结构挑分量数

## 验证与局限

有一、二人 BIC 曲线和拟合，需警惕双向流、修补或材质不均造成伪峰

## 迁移到新题

保留模型选择，换网格及脚印先验并用已知并排行走数据检验

## 证据定位

- PDF 第 12–17 页，图7–10、式11–29。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 12–17 图7–10、式11–29可对应假设、机制与结果。 |
| 机制解释力 | 4 | 将踩踏位置假定为双维混合正态，以 EM 拟合分布，并用 BIC 及脚数结构挑分量数。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 有一、二人 BIC 曲线和拟合，需警惕双向流、修补或材质不均造成伪峰 |
| 可迁移性 | 3 | 保留模型选择，换网格及脚印先验并用已知并排行走数据检验 |

总分 **16/20** · 可借鉴
