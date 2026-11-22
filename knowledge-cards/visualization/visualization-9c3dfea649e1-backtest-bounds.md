---
schema: mcm-card-v1
id: "visualization-9c3dfea649e1-backtest-bounds"
type: visualization
title: "将逐国实际奖牌叠到预测上下范围"
paper:
  title: "Beyond Medals: A Predictive Model for Olympic Success and Identifying Opportunities"
  year: 2025
  problem: C
source:
  pdf: "2025/MCM-C/论文/2521556.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "9c3dfea649e18e012725e8669e69f6af4c9ca1a09a473057b75cab05a97f6354"
  pdf_pages: [11]
tags: ["TrueSkill", "奖牌分配", "残差断点"]
score:
  total: 16
  max: 20
  tier: usable
---

# 将逐国实际奖牌叠到预测上下范围

## 入选理由

表达创新或视觉张力。哪国落在区间外能直接看到

## 论证任务

查 2024 预测覆盖

## 图型与输入

按国排序，带或上下线与实值叠用。

## 视觉编码

按国排序，带或上下线与实值叠用

## 重绘与迁移

用点区间更适合离散国家轴，保存覆盖分母

## 证据定位

- PDF 第 11 页，图8。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 11 图8给出图面、图题及正文语境。 |
| 论证表达 | 4 | 哪国落在区间外能直接看到 |
| 重绘可行性 | 3 | 按国排序，带或上下线与实值叠用。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 2 | 原图主结构可辨，细线、标注或水印影响缩印辨读。 |
| 可迁移性 | 3 | 用点区间更适合离散国家轴，保存覆盖分母 |

总分 **16/20** · 可借鉴
