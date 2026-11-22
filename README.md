# MathModelAgent for MCM/ICM

从 COMAP MCM/ICM 赛题与附件出发，交付可复现的求解代码、结果、图表和英文竞赛论文。这是一套独立维护的美赛技能，源于 [jihe520/MathModelAgent 的 Skills 工作流](https://github.com/jihe520/MathModelAgent#skills)。

## 相对上游的主要改动

| 方面 | 本仓库的改动 |
| --- | --- |
| **范围与仓库结构** | 将多赛事工作流收敛为 MCM/ICM 的英文论文流程，移出国赛等其他赛事模板、论文转会议稿和通用工具技能。Git 仓库集中维护技能、共享规范和英文模板；赛题、数据、计算结果与论文放在独立项目目录。 |
| **建模与选型** | 按题面明确要求的答案拆解任务，保留原有顺序和编号，也覆盖未编号问询。先确定统一基础，再为确有需要的小问增加模型结构、变量或约束，最后整合各问结果。候选先满足数据、硬约束和基本有效性门槛，再依次比较**可视化潜力、创新性、效果**。 |
| **图件方案参与选型** | 每个基础候选（含基线）提交机制图或系统工作图、关键证据图两份文字方案。两类图各 6 分，六项评分分别按 0、1、2 分给出可复核的理由。机制图方案说明创意如何让关键关系可见、构图为何有美感。求解后核对证据，第 4 阶段为入选模型比较两种不同的视觉构思。 |
| **数据图与概念图分工** | 将数据图提炼为独立技能，通过范文图表卡寻找表达方式，并用 `nature-figure` 从当前数据或结果生成可追溯的定量矢量图。原 `4drawio` 改为 `4concept-visual`，负责背景、总体解题路线图、机制图和系统工作图。总体路线图按锁定英文母版和全局色板装配，采用 Image2；机制阐释图及承担同类用途的系统工作图同样用 Image2 完成，保留生成稿。 |
| **全篇配色与图件下限** | 用户确认的全局 HEX 色值及语义写入 `plan.md`，可用 [ColorDrop](https://colordrop.io/palette/create) 从关键词生成候选。完整论文正文至少 **12 张图**，其中概念图至少 **4 张**、数据图至少 **5 张**，余量按论证需求分配。数据图至少含一张有独立表达价值的非常规图。每个正文页至少有一张相关、可读的图或表。 |
| **英文写作与验收** | 内置 Typst 和 XeLaTeX 英文美赛模板，锁定七个一级章节，并用脚本核对章节结构。`Solution and Results` 按题面逐问展开，技术选型记录留在内部报告。总体路线图置于引言的总体思路小节，最终验收检查图件来源、实际入稿数量、逐页可读性、风格一致性及论文数值。第六阶段由 `6verity` 更名为 `6verify`。 |
| **范文知识卡** | 新增单篇 PDF 的知识提取技能，分别输出建模方法卡和图表方法卡，逐项评分并标明原文物理页码。工作流按当前机制、约束或图件论证任务检索，并核对原文后迁移。 |

## 使用方式

将赛题 PDF 和附件放在独立的赛题目录，在能够读取本仓库技能的对话中，从 1start-mathmodel 启动完整流程。可以直接给出赛题路径、所用排版引擎和已有的中间成果。

```text
使用 $1start-mathmodel 完成本目录中的美赛赛题。读取题面和附件，先建立 plan.md 和 todo.md，交付可复现结果、图表和 XeLaTeX 英文论文。
```

| 阶段 | 核心交付 |
| --- | --- |
| [1start-mathmodel](1start-mathmodel/SKILL.md) | 建立 `plan.md` 和 `todo.md`，确定论文引擎、图表风格和各阶段任务。 |
| [2analysis-modeling](2analysis-modeling/SKILL.md) | `reports/ANALYSIS_MODELING_REPORT.md`，包含基础模型、逐问扩展、图件方案及验证设计。 |
| [3coding-visual](3coding-visual/SKILL.md) | `code/`、`results/`、数据图和 `reports/RESULTS_REPORT.md`。 |
| [4concept-visual](4concept-visual/SKILL.md) | 概念图成稿和 `reports/CONCEPT_FIGURES_REPORT.md`。 |
| [5writing](5writing/SKILL.md) | `paper/` 中的英文论文源码和编译 PDF。 |
| [6verify](6verify/SKILL.md) | `reports/VERIFY_REPORT.md`，记录论文一致性、编译、图表和版面验收结果。 |

### 独立任务

- 使用已有数据或结果生成、重绘和美化数据图。 [mcm-data-figure](mcm-data-figure/SKILL.md)
- 根据题面和模型成果装配可直接交给 Image2 的完整英文路线图提示词。 [mcm-solution-roadmap](mcm-solution-roadmap/SKILL.md)
- 从单篇论文 PDF 提取两类 Markdown 知识卡，分别写入用户指定目录的 `modeling/` 和 `visualization/`。 [mcm-paper-cards](mcm-paper-cards/SKILL.md)
- 判断"怎么做才可能拿奖"与"这篇稿子能到什么档"：动笔前出简报、交稿前出评分与改法。 [mcm-judge](mcm-judge/SKILL.md)

### 工具与参考

完整流程按任务使用 Python 或 R 求解和绘图，使用 Typst 或 XeLaTeX 编译论文，并使用环境中的 `nature-figure` 和内置 Image2 完成相应图件。

- [建模方法优化流程](_references/modeling-method-workflow.md)
- [图表工作流](_references/figure-workflow.md)
- [数学建模基本规范](_references/math_modeling_norms.md)
- [项目路线图](ROADMAP.md)

### 范文知识库

- [建模方法卡](knowledge-cards/modeling) 记录模型机制、求解、验证和迁移条件。
- [图表方法卡](knowledge-cards/visualization) 记录图表的论证任务、视觉编码和重绘思路。

`plan.md` 的默认知识卡根目录为 `knowledge-cards/`，相对于技能仓库根目录。原论文库路径默认待定，仓库内卡片以 `source.pdf_root: null` 表示待配置，`source.pdf` 保留论文在原资料库中的相对路径。配置原论文库后，将其根目录与 `source.pdf` 拼接，并依 `source.pdf_pages` 核对物理页码。原论文库待定时仍可检索卡片，原文核对状态记为待核。

上游技能与模板来自 MathModelAgent，科研绘图流程复用 nature-figure。 [MathModelAgent](https://github.com/jihe520/MathModelAgent) · [nature-skills](https://github.com/Yuan1z0825/nature-skills)

## 上游许可

MathModelAgent 的许可说明允许个人免费使用，并对商业用途、商业服务和闭源分发作出限制。使用本仓库中的上游材料时，请遵守原许可说明。 [MathModelAgent 许可原文](https://github.com/jihe520/MathModelAgent/blob/main/docs/md/License.md)
