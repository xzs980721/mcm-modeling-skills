---
schema: mcm-card-v1
id: "modeling-9c3dfea649e1-coach-residual-scad"
type: modeling
title: "先定位残差异常再用 SCAD 筛教练解释"
paper:
  title: "Beyond Medals: A Predictive Model for Olympic Success and Identifying Opportunities"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2521556.pdf"
  pdf_root: null
  sha256: "9c3dfea649e18e012725e8669e69f6af4c9ca1a09a473057b75cab05a97f6354"
  pdf_pages: [16, 17, 18, 19, 20]
tags: ["TrueSkill", "奖牌分配", "残差断点"]
score:
  total: 16
  max: 20
  tier: usable
---

# 先定位残差异常再用 SCAD 筛教练解释

## 原题与基线

赛果突变仅是线索，非教练唯一解释

## 建模机制与求解

拟合过去表现、人数及项目变量，以标准残差和累计和找变点，SCAD 稀疏回归估教练变量关联

## 验证与局限

个案异常和项目预测支持筛选，难排除队员更替等同期因素

## 迁移到新题

在有任教记录和基线的项目验证，并做未任教伪时点对照

## 证据定位

- PDF 第 16–20 页，图15–18、式18–22。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 16–20 图15–18、式18–22可对应假设、机制与结果。 |
| 机制解释力 | 4 | 拟合过去表现、人数及项目变量，以标准残差和累计和找变点，SCAD 稀疏回归估教练变量关联。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 个案异常和项目预测支持筛选，难排除队员更替等同期因素 |
| 可迁移性 | 3 | 在有任教记录和基线的项目验证，并做未任教伪时点对照 |

总分 **16/20** · 可借鉴
