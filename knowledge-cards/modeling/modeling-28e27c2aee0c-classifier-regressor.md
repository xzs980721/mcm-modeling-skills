---
schema: mcm-card-v1
id: "modeling-28e27c2aee0c-classifier-regressor"
type: modeling
title: "先判获牌再回归数量以吸收零膨胀"
paper:
  title: "Revealing the Hidden Forces Shaping Olympic Success"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2516178.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "28e27c2aee0cfcda7dccb21061565665099698220e0ae2b39d82367764aa8f02"
  pdf_pages: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
tags: ["双阶段预测", "重采样", "DID"]
score:
  total: 17
  max: 20
  tier: priority
---

# 先判获牌再回归数量以吸收零膨胀

## 原题与基线

相当多零奖牌，单回归不区分有无获奖

## 建模机制与求解

XGBoost 分类过滤可能获牌者，再做调参回归并用非参数 Bootstrap 得区间

## 验证与局限

有两届回测及覆盖率，低牌样本和强国覆盖差要分别报告

## 迁移到新题

按整届前训后验，另监控阈值漏判及覆盖率

## 证据定位

- PDF 第 6–15 页，图3–8、表2–5、式1–12。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 6–15 图3–8、表2–5、式1–12可对应假设、机制与结果。 |
| 机制解释力 | 4 | XGBoost 分类过滤可能获牌者，再做调参回归并用非参数 Bootstrap 得区间。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 有两届回测及覆盖率，低牌样本和强国覆盖差要分别报告 |
| 可迁移性 | 3 | 按整届前训后验，另监控阈值漏判及覆盖率 |

总分 **17/20** · 优先借鉴
