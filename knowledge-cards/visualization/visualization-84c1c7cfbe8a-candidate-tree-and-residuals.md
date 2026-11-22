---
schema: mcm-card-v1
id: "visualization-84c1c7cfbe8a-candidate-tree-and-residuals"
type: visualization
title: "把可行边、抽取树和保留边组织成对照序列"
paper:
  title: "Fewest Repeaters for a Circular Area: Iterative Extremal Optimization Based on Voronoi Diagrams"
  year: 2011
  problem: B
source:
  pdf: "2011/MCM-B/论文/Fewest Repeaters for a Circular Area.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "84c1c7cfbe8a7683afc9ecdfed98abc890aa42280ca7af9e97f3351a7364064f"
  pdf_pages: [11, 12]
tags: ["设施布点", "区域覆盖", "网络图"]
score:
  total: 18
  max: 20
  tier: priority
---

# 把可行边、抽取树和保留边组织成对照序列

## 入选理由

表达创新。同一站点布局只改变连边编码。

## 论证任务

依序说明原始可连通网络、最大/最小生成树及去掉树边后的网络。

## 图型与输入

节点坐标固定，候选边、树边和保留边用颜色和线型分开。

## 视觉编码

图6蓝粗实线与红虚线分别表示保留和移除，左右继承图5树类型。

## 重绘与迁移

用边 ID 验证选中和保留边均来自原网。缩印时淡化未选边并检查色弱时线型仍可区分。

## 证据定位

- PDF 第 11 页（印刷页 141），图4/图5。
- PDF 第 12 页（印刷页 142），图6。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 可在 11 图4/图5、12 图6 回查。图题和相邻正文支持其论证关系。 |
| 论证表达 | 4 | 同一站点布局只改变连边编码。 |
| 重绘可行性 | 3 | 节点坐标固定，候选边、树边和保留边用颜色和线型分开。 逐点源数据未随图附出。 |
| 视觉可读性 | 3 | 原页主层次可辨，成文尺寸下仍需检查标注。 |
| 可迁移性 | 4 | 用边 ID 验证选中和保留边均来自原网。缩印时淡化未选边并检查色弱时线型仍可区分。 |

总分 **18/20** · 优先借鉴
