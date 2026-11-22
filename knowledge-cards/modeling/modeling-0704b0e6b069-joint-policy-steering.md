---
schema: mcm-card-v1
id: "modeling-0704b0e6b069-joint-policy-steering"
type: modeling
title: "按双变量敏感性和阶段反应选择税收分配"
paper:
  title: "The Triangular Balance of Environment, Economy, and Society: A System Dynamics-Based Model for Sustainable Tourism Management"
  year: 2025
  problem: B
source:
  pdf: "2025/MCM-B/论文/2509557.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "0704b0e6b0695b9ec421c4a9f14c7ee4e9d7fd527c9ef5d854d742633b59e77a"
  pdf_pages: [16, 17, 18, 19, 20, 21, 22]
tags: ["旅游", "状态反馈", "联合灵敏度"]
score:
  total: 17
  max: 20
  tier: priority
---

# 按双变量敏感性和阶段反应选择税收分配

## 原题与基线

单变量分析无法识别税率与环保支出配比的联合作用

## 建模机制与求解

扫描政策组合，比较游客、环境、满意度和设施约束，并在另一地重设初值和占比

## 验证与局限

有两地情景及数值热图，未提供实施后的结果

## 迁移到新题

套用同单位约束和目标，并保留基准、单改及联合改三类对照

## 证据定位

- PDF 第 16–22 页，图8–14、算法1。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 16–22 图8–14、算法1可对应假设、机制与结果。 |
| 机制解释力 | 4 | 扫描政策组合，比较游客、环境、满意度和设施约束，并在另一地重设初值和占比。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 有两地情景及数值热图，未提供实施后的结果 |
| 可迁移性 | 3 | 套用同单位约束和目标，并保留基准、单改及联合改三类对照 |

总分 **17/20** · 优先借鉴
