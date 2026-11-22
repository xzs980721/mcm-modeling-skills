# MathModelAgent for MCM/ICM

本仓库维护从 COMAP MCM/ICM 题面及附件到可复现结果和英文竞赛论文的工作流。

- 完整任务从 [1start-mathmodel](1start-mathmodel/SKILL.md) 开始。单独执行阶段时读取相应的 `SKILL.md`，沿用已有输入。
- 单独制作或重绘数据图时使用 [mcm-data-figure](mcm-data-figure/SKILL.md)。单独制作或重绘总体解题路线图时使用 [mcm-solution-roadmap](mcm-solution-roadmap/SKILL.md)。
- 从单篇范文 PDF 提炼建模方法卡与图表方法卡时，使用 [mcm-paper-cards](mcm-paper-cards/SKILL.md)。
- 判断"这样写能不能拿奖"时使用 [mcm-judge](mcm-judge/SKILL.md)：动笔前调用 brief 模式产出 `reports/AWARD_BRIEF.md`，交付前调用 review 模式产出 `reports/JUDGE_REVIEW.md`。评奖标准以 `mcm-judge` 为准，执行与版式以本仓库管线为准。
- 资源路径以引用它的说明文件为基准。赛题、数据、运行结果和论文成稿放在独立的赛题目录。
- 项目目标与对照验证见 [ROADMAP.md](ROADMAP.md)。
