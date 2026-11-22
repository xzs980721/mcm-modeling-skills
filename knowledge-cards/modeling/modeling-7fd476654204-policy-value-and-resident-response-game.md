---
schema: mcm-card-v1
id: "modeling-7fd476654204-policy-value-and-resident-response-game"
type: modeling
title: "把经营价值差异接到居民响应演化"
paper:
  title: "Letting \"Carbon\" Stay: Forest Management for Ecological-Economic Balance in the Perspective of Carbon Sequestration"
  year: 2022
  problem: E
source:
  pdf: "2022/ICM-E/论文/2223495.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "7fd4766542049753f5ade37080731eb6e3c971b069580c0dd0bebf1b5187cf79"
  pdf_pages: [11, 12, 13, 14, 15, 19, 20, 21]
tags: ["龄级 ODE", "生态经济权衡", "演化博弈"]
score:
  total: 15
  max: 20
  tier: usable
---

# 把经营价值差异接到居民响应演化

## 原题与基线

政策带来的社会支持会反馈经营选择

## 建模机制与求解

用双方选择的期望收益和响应趋势构建演化博弈，区别可行与首选策略

## 验证与局限

仿真图及支付矩阵缺失，当前仅支持机制级卡

## 迁移到新题

在合成收益矩阵核对稳定点，不能从当前文件复算案例结果

## 证据定位

- PDF 第 11–15 页，TEV 目标和退火。
- PDF 第 19 页，支付矩阵位置与期望收益。
- PDF 第 20–21 页，演化文字。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 11–15 TEV 目标和退火、19 支付矩阵位置与期望收益、20–21 演化文字可对应假设、机制与结果。 |
| 机制解释力 | 3 | 用双方选择的期望收益和响应趋势构建演化博弈，区别可行与首选策略。 |
| 实现可复现性 | 2 | 主要输入和操作可从建模步骤回查。还有影响复算的源参数需补齐。 |
| 验证质量 | 2 | 仿真图及支付矩阵缺失，当前仅支持机制级卡 |
| 可迁移性 | 4 | 在合成收益矩阵核对稳定点，不能从当前文件复算案例结果 |

总分 **15/20** · 可借鉴
