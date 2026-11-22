---
schema: mcm-card-v1
id: "modeling-7fd476654204-age-cohort-carbon-and-product-decay"
type: modeling
title: "用林龄队列和木产品折旧分别传播碳库"
paper:
  title: "Letting \"Carbon\" Stay: Forest Management for Ecological-Economic Balance in the Perspective of Carbon Sequestration"
  year: 2022
  problem: E
source:
  pdf: "2022/ICM-E/论文/2223495.pdf"
  pdf_root: null
  sha256: "7fd4766542049753f5ade37080731eb6e3c971b069580c0dd0bebf1b5187cf79"
  pdf_pages: [6, 7, 8, 9, 10, 11, 25]
tags: ["龄级 ODE", "生态经济权衡", "演化博弈"]
score:
  total: 17
  max: 20
  tier: priority
---

# 用林龄队列和木产品折旧分别传播碳库

## 原题与基线

活林与产品的寿命和周转不同

## 建模机制与求解

将树龄阶段更新耦合产品储留及释放，用分期状态求稳态或有限时间轨迹

## 验证与局限

正文演算和附录片段可读，图体及部分参数表缺失

## 迁移到新题

分别校验增长和死亡或产物流转，再合并守恒核对

## 证据定位

- PDF 第 6–8 页，林龄状态与产品定义。
- PDF 第 9–11 页，动态方程与案例说明。
- PDF 第 25 页，附录程序。

## 评分

| 维度 | 分数（0–4） | 依据或缺口 |
| --- | --- | --- |
| 证据可追溯性 | 4 | 6–8 林龄状态与产品定义、9–11 动态方程与案例说明、25 附录程序可对应假设、机制与结果。 |
| 机制解释力 | 3 | 将树龄阶段更新耦合产品储留及释放，用分期状态求稳态或有限时间轨迹。 |
| 实现可复现性 | 3 | 主要输入和操作可从建模步骤回查。源数据或求解器设置限制完整复算。 |
| 验证质量 | 3 | 正文演算和附录片段可读，图体及部分参数表缺失 |
| 可迁移性 | 4 | 分别校验增长和死亡或产物流转，再合并守恒核对 |

总分 **17/20** · 优先借鉴
