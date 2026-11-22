---
schema: mcm-card-v1
id: "visualization-a294c5876130-semilog-market-crossover"
type: visualization
title: "用对数纵轴同时保留早期小份额与替代交叉"
paper:
  title: "Electric Cars as a Widespread Means of Transportation"
  year: 2011
  problem: C
source:
  pdf: "2011/ICM-C/论文/Electric Cars as a Widespread Means of Transportation.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "a294c587613025525ea652c6ddb7c603ef7fba355dda2c98f4c92d8720ea0323"
  pdf_pages: [7, 8, 9]
tags: ["半对数图", "替代技术", "交叉"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用对数纵轴同时保留早期小份额与替代交叉

## 论证任务

图 2 在组合政策情景下展示多个数量级的车型轨迹，读者可以同时看到初期存量及其交叉。

## 图型与输入

输入为各年份汽油车、BEV、PHEV 与总车辆数，纵轴量以百万辆计，所有可绘制存量应大于零。

## 视觉编码

横轴为模拟年，纵轴为十进对数间距，曲线及图例标记各类。线条灰度相近，交叉处需要配合图例追踪。

## 重绘与迁移

将车型与总量分别指派线型，标出交叉年份，使用普通坐标或份额小图核对绝对差。遇到零存量留断点并说明，不以未经披露的正数替代。

## 证据定位

本卡使用单篇 PDF 物理页码，引用页加 164 可得期刊印刷页。

- PDF 第 7 页，图 1 与 Population Model Results，基准情景及半对数选择
- PDF 第 8–9 页，组合情景段与图 2，车型图例、轴和轨迹交叉

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 第 7 页解释半对数选择，第 9 页图例与交叉点对应。 |
| 论证表达 | 4 | 同时表现小初值和规模跨越，支持交叉比较。 |
| 重绘可行性 | 3 | 字段、单位和变换齐全，无法逐点复录。 |
| 视觉可读性 | 2 | 灰度多线有叠靠，同图图例可辅助。 |
| 可迁移性 | 4 | 规定零值处理及交叉与普通尺度的对照。 |

总分 **17/20** · 优先借鉴
