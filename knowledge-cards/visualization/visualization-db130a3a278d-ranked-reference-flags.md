---
schema: mcm-card-v1
id: "visualization-db130a3a278d-ranked-reference-flags"
type: visualization
title: "用颜色和符号标注排序表中的已知样例"
paper:
  title: "Finding Conspirators in the Network via Machine Learning"
  year: 2012
  problem: C
source:
  pdf: "2012/ICM-C/论文/Finding Conspirators in the Network via Machine Learning.pdf"
  pdf_root: null
  sha256: "db130a3a278dd6f4a998e2a6bd812b3925dee31d27ef42a74df9d99d3bc9e86a"
  pdf_pages: [12]
tags: ["网络分析", "小样本", "稳定性"]
score:
  total: 18
  max: 20
  tier: priority
---

# 用颜色和符号标注排序表中的已知样例

## 入选理由

在排序结果中以颜色和星号重复标记已知样例，检查命中位置时仍能直接查原分值。

## 论证任务

比较已知样例的位置与其他条目的相似度名次。

## 图型与输入

每行为排名、主题编号与相似度，已知类别有独立的标记字段。完整输入相似度需由作者计算流程或原始表追回。

## 视觉编码

表按相似度降序，已知样例在编号旁加星号并用蓝色突出，零分并列放在同一行。

## 重绘与迁移

迁移到信息检索结果表，校验排名与并列规则，检查灰度打印时星号仍可识别。

## 证据定位

- PDF 第 12 页，表1（该页独立排序表）。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 12 页表1的图注解释星号和蓝色。 |
| 论证表达 | 4 | 同列编码便于核查参考样例排位与分数。 |
| 重绘可行性 | 4 | 表内绘制所需字段可逐行读取。 |
| 视觉可读性 | 3 | 水印压过部分行，但颜色与符号仍可辨。 |
| 可迁移性 | 3 | 适合有已知样例的排序，重绘须明确并列规则。 |

总分 **18/20** · 优先借鉴
