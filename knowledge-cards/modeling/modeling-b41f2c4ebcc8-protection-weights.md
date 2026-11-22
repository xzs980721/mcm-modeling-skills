---
schema: mcm-card-v1
id: "modeling-b41f2c4ebcc8-protection-weights"
type: modeling
title: "以层级判断矩阵联结文保指标和措施等级"
paper:
  title: "In Face of Increasingly Severe Extreme Weather: Sustainable Property Insurance under Risk"
  year: 2024
  problem: E
source:
  pdf: "2024/ICM-E/论文/2401102.pdf"
  pdf_root: null
  sha256: "b41f2c4ebcc818585ade672724ceb0a858fd609924bfdc931dd64a181e23b9c5"
  pdf_pages: [19, 20, 21, 22, 23]
tags: ["灾害预测", "需求风险优化", "文保"]
score:
  total: 16
  max: 20
  tier: usable
---

# 以层级判断矩阵联结文保指标和措施等级

## 原题与基线

多类文化及社区价值缺共同量纲

## 建模机制与求解

以 AHP 和一致性检验赋权，对不同单位的次指标归一化并按综合分划保护等级

## 验证与局限

给出文庙单案例保护前后估计，效果并无实际随访

## 迁移到新题

保留层级与一致性检验，用地方文保记录替换代理变量并检查等级边界

## 证据定位

- PDF 第 19–23 页，图12–13、表4–9。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 19–23 图12–13、表4–9可对应假设、机制与结果。 |
| 机制解释力 | 4 | 以 AHP 和一致性检验赋权，对不同单位的次指标归一化并按综合分划保护等级。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 给出文庙单案例保护前后估计，效果并无实际随访 |
| 可迁移性 | 3 | 保留层级与一致性检验，用地方文保记录替换代理变量并检查等级边界 |

总分 **16/20** · 可借鉴
