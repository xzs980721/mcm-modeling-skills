---
name: 1start-mathmodel
description: 从 COMAP 美赛（MCM/ICM）题面与附件生成完整英文竞赛论文。用户要求解答美赛赛题、执行题面到论文的完整建模工作流，或显式调用本阶段时使用。
---

# 美赛建模工作流

## 启动与计划

1. 读取题面、附件和当届提交要求。确认题号、需要交付的各问与附加材料，记录缺失数据和关键歧义。
2. 沿用用户已指定的 Typst 或 LaTeX。选择会影响交付且尚未明确时询问。按美赛英文论文组织内容。
3. 在本次赛题项目中创建 `plan.md`，记录排版引擎、题目及任务数、模型方向、各阶段的负责人、输入和产物，以及关键假设或风险的检查方式。
4. 创建 `todo.md`。按下表逐阶段列出带 skill 名称的任务，完成且产物就绪后更新状态。

## 顺序与交接

| 阶段 | 调用 | 产物 |
| --- | --- | --- |
| 赛题分析与建模设计 | `2analysis-modeling` | `reports/ANALYSIS_MODELING_REPORT.md` |
| 求解、实验与数据可视化 | `3coding-visual` | `code/`、`results/`、数据图和 `reports/RESULTS_REPORT.md` |
| 背景、机制与流程图 | `4drawio` | 按题目需要生成图源和 PDF，并记录于 `reports/DRAWIO_REPORT.md` |
| 美赛论文写作与排版 | `5writing` | 美赛模板下的 `paper/` 源码和 PDF |
| 提交前验收 | `6verity` | `reports/VERIFY_REPORT.md` |

按表顺序读取各阶段的 `SKILL.md`。图表集中存放在 `figures/`，数据图从计算结果生成，概念图解释场景、模型结构或流程。论文的表格数值、图和定量结论应能追溯到计算结果。需要补充领域规范时，查看 `../_references/math_modeling_norms.md`。
