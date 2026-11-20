---
name: 5writing
description: 将 COMAP 美赛（MCM/ICM）的建模报告、求解结果和图表写成英文竞赛论文。支持内置 Typst 和 XeLaTeX 模板，也用于从已有美赛模型成果继续撰写与排版。
---

# 美赛英文论文写作

## 选择并复制模板

沿用 `plan.md` 或用户明确选择的引擎。选择尚未明确时询问，用户跳过时用 XeLaTeX。

| 引擎 | 内置模板 | 在 `paper/` 内运行 |
| --- | --- | --- |
| Typst | `templates/en/mcm/` | `typst compile main.typ` |
| XeLaTeX | `templates/en/mcm-latex/` | `xelatex -interaction=nonstopmode -halt-on-error main.tex`，运行两次 |

将对应模板目录完整复制到本次工作区的 `paper/`，以其入口文件为底稿，填写赛题、年份、标题、摘要及队号。未给出队号时标为待填写，向验收阶段记录。保留模板的 Summary Sheet、导航、页眉和分章入口，并根据题面与当届规则调整目录、页码、页数限制和附加材料。将模板来源记入 `plan.md` 或验收报告。对照当前题目的官方要求检查格式。

## 从证据撰写论文

1. 读取 `reports/ANALYSIS_MODELING_REPORT.md`、`reports/RESULTS_REPORT.md`、图表及可用的图示报告。按题目任务安排章节，保留模板的引言、假设、模型、求解、灵敏度、模型评估和结论结构。
2. 使用实际输出替换模板示例。解释赛题机制、基线局限、新增方法及可复现的对照结果。根据证据说明最终方法的取舍、有效条件和局限。
3. 按 `plan.md` 的图表清单嵌入定稿。背景图帮助读者理解问题，方法图解释机制，数据图支撑结果。配英文图题和正文引用，按 [图表工作流](../_references/figure-workflow.md) 检查编译后的字号、布局和跨章节风格。
4. 参考文献写入模板的 `references.typ` 或 `references.tex`。只引用可核实的资料。根据当届题面及政策加入需要的建议信、备忘录、附录及 AI 使用报告。
5. 完成正文后写一页 Summary Sheet。覆盖各问的方法、核心结果和结论。正文和摘要的数值、单位和舍入与结果文件对齐。
6. 编译 PDF，核对图表路径和交叉引用，确认模板示例均已替换，将论文源码、PDF 和未解决的格式问题交给 `6verity`。

写作和图表的通用规范见 `../_references/math_modeling_norms.md` 中的论文写作、图表与美赛专节。
