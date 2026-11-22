---
schema: mcm-card-v1
id: "visualization-f2349d15afe2-forecast-window-handoff"
type: visualization
title: "把滑窗和预测重心变化画在同一时间线上"
paper:
  title: "CAFE: Characterization, Analysis, Forecasting, and Evaluation of Energy Profile"
  year: 2018
  problem: C
source:
  pdf: "2018/MCM-C/论文/72969.pdf"
  pdf_root: null
  sha256: "f2349d15afe26f49d7183ab8cc7759d1eb9a275b69a6c6bdc51796cfae0b860a"
  pdf_pages: [16]
tags: ["能源画像", "混合预测", "目标协调"]
score:
  total: 18
  max: 20
  tier: priority
---

# 把滑窗和预测重心变化画在同一时间线上

## 入选理由

表达创新或视觉张力。窗口单元格和跨阶段箭头显示近期采用局部模型、远期逐步交给全局模型。

## 论证任务

说明发生递推和预测切换的时间关系。

## 图型与输入

横向为历史至未来，矩形标窗，红/黄区区分短与长预测，蓝箭头示 ARMA，绿线标 GPR。

## 视觉编码

横向为历史至未来，矩形标窗，红/黄区区分短与长预测，蓝箭头示 ARMA，绿线标 GPR。

## 重绘与迁移

复刻为可按预测步数检查的窗口图，给一组手算以排除未来数据泄漏。

## 证据定位

- PDF 第 16 页，图9。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 16 图9给出图面、图题及正文语境。 |
| 论证表达 | 4 | 窗口单元格和跨阶段箭头显示近期采用局部模型、远期逐步交给全局模型。 |
| 重绘可行性 | 4 | 横向为历史至未来，矩形标窗，红/黄区区分短与长预测，蓝箭头示 ARMA，绿线标 GPR。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 复刻为可按预测步数检查的窗口图，给一组手算以排除未来数据泄漏。 |

总分 **18/20** · 优先借鉴
