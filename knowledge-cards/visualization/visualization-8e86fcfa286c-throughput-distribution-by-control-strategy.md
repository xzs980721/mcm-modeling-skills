---
schema: mcm-card-v1
id: "visualization-8e86fcfa286c-throughput-distribution-by-control-strategy"
type: visualization
title: "用同轴箱图呈现不同策略的离散性"
paper:
  title: "Control Time Model: Wait One Second and Start Your Journey"
  year: 2017
  problem: B
source:
  pdf: "2017/MCM-B/论文/70545.pdf"
  pdf_root: null
  sha256: "8e86fcfa286c46c3d8bddc3ef1ab64b376abe7e07c86827adc811b6c086d9954"
  pdf_pages: [12, 13]
tags: ["交替放行", "冲突代理", "敏感性"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用同轴箱图呈现不同策略的离散性

## 入选理由

表达创新或视觉张力。箱须对照平均结果很接近时仍给波动差。

## 论证任务

在同模拟长度对比三种控制方案。

## 图型与输入

横轴策略，纵轴吞吐，颜色区分箱形，另外给测试统计数。

## 视觉编码

横轴策略，纵轴吞吐，颜色区分箱形，另外给测试统计数。

## 重绘与迁移

明确每组重复次数和异常规则，给转译到实际吞吐的区间。

## 证据定位

- PDF 第 12 页，图7。
- PDF 第 13 页，表1。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 12 图7、13 表1给出图面、图题及正文语境。 |
| 论证表达 | 4 | 箱须对照平均结果很接近时仍给波动差。 |
| 重绘可行性 | 3 | 横轴策略，纵轴吞吐，颜色区分箱形，另外给测试统计数。 可据给出的字段重绘，逐点数据或参数仍需补齐。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 明确每组重复次数和异常规则，给转译到实际吞吐的区间。 |

总分 **17/20** · 优先借鉴
