---
schema: mcm-card-v1
id: "modeling-8742ccd808cc-weighted-k-means-balance"
type: modeling
title: "迭代校正聚类权重平衡区划人口"
paper:
  title: "Why Weight? A Cluster-Theoretic Approach to Political Districting"
  year: 2007
  problem: A
source:
  pdf: "2007/MCM-A/论文/A Cluster-Theoretic Approach to Political Districting.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "8742ccd808cc8f275928817c581ebd36562b3eb4664e7ee8464cc8b6d6d5b3d2"
  pdf_pages: [7, 8, 9, 11, 12, 13, 16, 17]
tags: ["地理区划", "加权聚类", "空间紧致"]
score:
  total: 17
  max: 20
  tier: priority
---

# 迭代校正聚类权重平衡区划人口

## 原题与基线

普通 K-means 得到紧致的空间簇，人口总量可相差较大

## 建模机制与求解

按人口单元作加权分配、更新质心和拥挤惩罚，对人口超过目标的簇调权，再重复直到进容差

## 验证与局限

案例检查紧致程度和人口误差，飞地与种子波动仍应单独测试

## 迁移到新题

可用于学校分区和服务辖区，硬性连通需另验证

## 证据定位

- PDF 第 7–9 页，第3节。
- PDF 第 11–13 页，图4–6。
- PDF 第 16–17 页，附录B。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 7–9 第3节、11–13 图4–6、16–17 附录B可对应假设、机制与结果。 |
| 机制解释力 | 4 | 按人口单元作加权分配、更新质心和拥挤惩罚，对人口超过目标的簇调权，再重复直到进容差。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 案例检查紧致程度和人口误差，飞地与种子波动仍应单独测试 |
| 可迁移性 | 3 | 可用于学校分区和服务辖区，硬性连通需另验证 |

总分 **17/20** · 优先借鉴
