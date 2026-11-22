---
schema: mcm-card-v1
id: "modeling-6bcf5acd78dd-construction-bayesian"
type: modeling
title: "把施工期通行能力折减纳入政策比较"
paper:
  title: "A Multi-Methodological Framework for Post-Disaster Traffic Optimization and Sustainable Mobility Planning in Baltimore"
  year: 2025
  problem: D
source:
  pdf: "2025/ICM-D/论文/2516219.pdf"
  pdf_root: null
  sha256: "6bcf5acd78dd6cff84bbbf52895464a07b02bff83554831f3051b279274a9a6c"
  pdf_pages: [20, 21, 22, 23]
tags: ["灾后交通", "网络均衡", "公交规划"]
score:
  total: 16
  max: 20
  tier: usable
---

# 把施工期通行能力折减纳入政策比较

## 原题与基线

解释建设期成本与长期收益的衔接

## 建模机制与求解

分阶段模拟施工造成的容量下降，按居民、商业及政府定义收益或支出，并用贝叶斯参数估计表征部分弹性

## 验证与局限

后验与一条轨迹仅提供局部诊断，可报告多链和预测检验

## 迁移到新题

适用于带临时服务损失的基础设施改造

## 证据定位

- PDF 第 20–23 页，第8节、式35–44、图11至13。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 20–23 第8节、式35–44、图11至13可对应假设、机制与结果。 |
| 机制解释力 | 4 | 分阶段模拟施工造成的容量下降，按居民、商业及政府定义收益或支出，并用贝叶斯参数估计表征部分弹性。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 后验与一条轨迹仅提供局部诊断，可报告多链和预测检验 |
| 可迁移性 | 3 | 适用于带临时服务损失的基础设施改造 |

总分 **16/20** · 可借鉴
