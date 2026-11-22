---
schema: mcm-card-v1
id: "visualization-48864c6d196c-nested-optimization-stopping-branched-flow"
type: visualization
title: "用内外两层收敛判定展示带约束求解器"
paper:
  title: "The Optimal Investment Strategy Based on the Large-scale Non-linear Constraint Optimization Methods"
  year: 2016
  problem: C
source:
  pdf: "2016/MCM-C/论文/47823.pdf"
  pdf_root: "美赛范文_2006-2025"
  sha256: "48864c6d196cb0aaf536bd376cf50c3a31d909085d9ba1103cb8050897be74e7"
  pdf_pages: [15]
tags: ["教育投资", "增广拉格朗日", "粒子群"]
score:
  total: 18
  max: 20
  tier: priority
---

# 用内外两层收敛判定展示带约束求解器

## 入选理由

表达创新或视觉张力。内层粒子群和外层乘子更新各自有停止与回线。

## 论证任务

便于检查什么时候重新找粒子，什么时候返回结果。

## 图型与输入

流程由框和决策菱形展开，主线输出目标和解，旁线回到迭代入口。

## 视觉编码

流程由框和决策菱形展开，主线输出目标和解，旁线回到迭代入口。

## 重绘与迁移

让每节点和附录的步骤对应，用不等式残差和测试目标核验退出。

## 证据定位

- PDF 第 15 页，图4。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 15 图4给出图面、图题及正文语境。 |
| 论证表达 | 4 | 内层粒子群和外层乘子更新各自有停止与回线。 |
| 重绘可行性 | 4 | 流程由框和决策菱形展开，主线输出目标和解，旁线回到迭代入口。 |
| 视觉可读性 | 3 | 原图对照结构可辨，缩小后应复核图例和字重。 |
| 可迁移性 | 3 | 让每节点和附录的步骤对应，用不等式残差和测试目标核验退出。 |

总分 **18/20** · 优先借鉴
