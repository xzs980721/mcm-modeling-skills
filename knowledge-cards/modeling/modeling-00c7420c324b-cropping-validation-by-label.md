---
schema: mcm-card-v1
id: "modeling-00c7420c324b-cropping-validation-by-label"
type: modeling
title: "用图像裁剪和标签粒度诊断分类泛化"
paper:
  title: "Fighting the Horde: a Comprehensive Model for Monitoring and Controlling Hornet Invasions"
  year: 2021
  problem: C
source:
  pdf: "2021/MCM-C/论文/2101587.pdf"
  pdf_root: null
  sha256: "00c7420c324bc69c8b9783f018babc06eed8c36035a3159e2e35dca88ae3cc0e"
  pdf_pages: [11, 12, 13, 23, 24, 25]
tags: ["事件筛查", "图像裁剪", "优先级"]
score:
  total: 18
  max: 20
  tier: priority
---

# 用图像裁剪和标签粒度诊断分类泛化

## 原题与基线

训练图片和公众报告图的取景不同会造成域偏移

## 建模机制与求解

比较不同 ResNet 和裁剪后的结果，再分别检验细类分类和二类任务

## 验证与局限

表4–6及混淆矩阵支持误差分析，手动裁剪与小样本限制外推

## 迁移到新题

固定分组数据和对照裁剪规则，并同时报告两种标签粒度的结果

## 证据定位

- PDF 第 11–13 页，图6–8及表4–6。
- PDF 第 23–25 页，附录 A。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 11–13 图6–8及表4–6、23–25 附录 A可对应假设、机制与结果。 |
| 机制解释力 | 4 | 比较不同 ResNet 和裁剪后的结果，再分别检验细类分类和二类任务。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 表4–6及混淆矩阵支持误差分析，手动裁剪与小样本限制外推 |
| 可迁移性 | 4 | 固定分组数据和对照裁剪规则，并同时报告两种标签粒度的结果 |

总分 **18/20** · 优先借鉴
