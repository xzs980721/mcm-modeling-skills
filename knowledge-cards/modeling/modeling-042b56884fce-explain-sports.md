---
schema: mcm-card-v1
id: "modeling-042b56884fce-explain-sports"
type: modeling
title: "以项目相关及 SHAP 双层解释奖牌来源"
paper:
  title: "2028 Olympic Medal Predictions: Multi-Effect Analysis and Strategic Insights"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2510862.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "042b56884fcebe1928a7ccc60853390f4c140b1210d033ece9087a1ec0fd6bda"
  pdf_pages: [15, 16, 17, 18]
tags: ["堆叠集成", "SHAP", "匹配双重差分"]
score:
  total: 16
  max: 20
  tier: usable
---

# 以项目相关及 SHAP 双层解释奖牌来源

## 原题与基线

相关强度和模型贡献并不相同

## 建模机制与求解

先算跨牌型 Pearson，再对不同国家模型输出做 SHAP，按运动类别比较

## 验证与局限

给出若干国家分面，相关的参赛规模变量可能分摊贡献

## 迁移到新题

换入参与和奖牌统计，关联组特征时检查归因是否稳定

## 证据定位

- PDF 第 15–18 页，图11–13、式11–12。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 15–18 图11–13、式11–12可对应假设、机制与结果。 |
| 机制解释力 | 4 | 先算跨牌型 Pearson，再对不同国家模型输出做 SHAP，按运动类别比较。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 给出若干国家分面，相关的参赛规模变量可能分摊贡献 |
| 可迁移性 | 3 | 换入参与和奖牌统计，关联组特征时检查归因是否稳定 |

总分 **16/20** · 可借鉴
