---
schema: mcm-card-v1
id: "modeling-7c06f4a0a719-temperature-triggered-cell-move"
type: modeling
title: "在元胞邻域中按热胁迫决定留居或迁移"
paper:
  title: "Under Global Warming: Small Scottish Fishing Companies Business Strategies with Species Migration"
  year: 2020
  problem: A
source:
  pdf: "2020/MCM-A/论文/2007799.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "7c06f4a0a719b330374ea9f1aed1f86228fbb4be92f65e5857e40d1cf9a248f0"
  pdf_pages: [8, 9, 10, 28, 29]
tags: ["季节预测", "元胞模型", "成本收益"]
score:
  total: 16
  max: 20
  tier: usable
---

# 在元胞邻域中按热胁迫决定留居或迁移

## 原题与基线

局部升温时只按直线拟合无法显式表达格点迁移规则

## 建模机制与求解

将适生温差经 sigmoid 映射到移动判定，按邻域适宜程度更新鲱鱼和鲭鱼位置

## 验证与局限

位置分面可核对模拟演进，固定种群及温度主导缺跨地点外部检验

## 迁移到新题

用真实分布初始化，回测占据格重叠和海陆边界，检查敏感温度窗

## 证据定位

- PDF 第 8–10 页，图6、表2、图7。
- PDF 第 28–29 页，附录程序。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 8–10 图6、表2、图7、28–29 附录程序可对应假设、机制与结果。 |
| 机制解释力 | 3 | 将适生温差经 sigmoid 映射到移动判定，按邻域适宜程度更新鲱鱼和鲭鱼位置。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 2 | 位置分面可核对模拟演进，固定种群及温度主导缺跨地点外部检验 |
| 可迁移性 | 4 | 用真实分布初始化，回测占据格重叠和海陆边界，检查敏感温度窗 |

总分 **16/20** · 可借鉴
