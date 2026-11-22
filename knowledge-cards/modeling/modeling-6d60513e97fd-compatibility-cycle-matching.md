---
schema: mcm-card-v1
id: "modeling-6d60513e97fd-compatibility-cycle-matching"
type: modeling
title: "用相容图的循环形成双人或多人配对"
paper:
  title: "Analysis of Kidney Transplant System Using Markov Process Models"
  year: 2007
  problem: C
source:
  pdf: "2007/ICM-C/论文/Analysis of Kidney Transplant System Using Markov Process Models.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "6d60513e97fd54ddc6d511381e6baed589468cc928fb6b11c837b829aee6742b"
  pdf_pages: [8, 9, 10]
tags: ["等候系统", "马尔可夫过程", "配对交换"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用相容图的循环形成双人或多人配对

## 原题与基线

同对供者不匹配时寻找跨对的可行组合

## 建模机制与求解

把供受两类个体以相容边接起，先处理管理成本较低的短交换圈，再纳入较长圈，统计从队列扣除的量

## 验证与局限

模拟表给配对量，临床流程与公平性不由这个简化匹配直接决定

## 迁移到新题

可迁移到兼容关系明确的交换网络

## 证据定位

- PDF 第 8–10 页，图4–5、表5。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 8–10 图4–5、表5可对应假设、机制与结果。 |
| 机制解释力 | 4 | 把供受两类个体以相容边接起，先处理管理成本较低的短交换圈，再纳入较长圈，统计从队列扣除的量。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 模拟表给配对量，临床流程与公平性不由这个简化匹配直接决定 |
| 可迁移性 | 3 | 可迁移到兼容关系明确的交换网络 |

总分 **17/20** · 优先借鉴
