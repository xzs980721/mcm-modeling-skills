---
schema: mcm-card-v1
id: "modeling-9c3dfea649e1-bottom-up-skill"
type: modeling
title: "传统项按能力预测，新设项用独立模型后合并"
paper:
  title: "Beyond Medals: A Predictive Model for Olympic Success and Identifying Opportunities"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2521556.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "9c3dfea649e18e012725e8669e69f6af4c9ca1a09a473057b75cab05a97f6354"
  pdf_pages: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
tags: ["TrueSkill", "奖牌分配", "残差断点"]
score:
  total: 17
  max: 20
  tier: priority
---

# 传统项按能力预测，新设项用独立模型后合并

## 原题与基线

统一历史计数忽略新增项目没有足够同类样本

## 建模机制与求解

TrueSkill 更新运动员和国家表现；传统项 SARIMAX 预测能力并估方差，新项目用随机森林，逐项汇总奖牌

## 验证与局限

有 2024 预测区间对照与 MAE，队伍组成和新项目转移样本还需核查

## 迁移到新题

换能力先验和赛制，检查每项可发奖牌数与未来届误差

## 证据定位

- PDF 第 6–12 页，图3–9、表2、式1–12。
- PDF 第 13–15 页，图10–14。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 6–12 图3–9、表2、式1–12、13–15 图10–14可对应假设、机制与结果。 |
| 机制解释力 | 4 | TrueSkill 更新运动员和国家表现；传统项 SARIMAX 预测能力并估方差，新项目用随机森林，逐项汇总奖牌。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 有 2024 预测区间对照与 MAE，队伍组成和新项目转移样本还需核查 |
| 可迁移性 | 3 | 换能力先验和赛制，检查每项可发奖牌数与未来届误差 |

总分 **17/20** · 优先借鉴
