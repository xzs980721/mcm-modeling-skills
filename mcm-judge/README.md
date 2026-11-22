# mcm-judge — 美赛评奖标准

本技能回答两个问题：**动笔前该怎么做才可能拿 Outstanding**，以及**这篇稿子现在能到什么档、怎么改**。

它不生成论文、不写代码、不画图、不编译。它只做判断，并给出可追溯的依据。

## 数据从哪来

| 项目 | 内容 |
|---|---|
| 语料 | 2017、2019–2025 年 MCM/ICM **Outstanding** 论文 |
| 论文数 | **295 篇**（可解析文本者；原始 296 篇中 1 篇为扫描件被剔除） |
| 分布 | A 49 / B 39 / C 73 / D 42 / E 51 / F 41 |
| 附加 | 11 份**评委评语**（`data/commentary.jsonl`），用于校准负面判断 |
| 字段 | `data/papers.jsonl`（每篇一份字段卡，含 SHA-256，可与 `mcm-paper-cards` 的卡片 join） |
| 全文 | `data/text/`（296 篇纯文本，按 `年-题-控制号.txt`，供内容层抽取与摘录用） |
| 内容层 | `data/content.jsonl`（模型家族、论证方式、参数来源、检验、决策翻译，均按篇） |
| 汇总 | `data/features.json`（按题号分开，含格式层与内容层） |

脚本：`extract.py`（PDF → 字段卡）、`dump_text.py`（PDF → 纯文本）、`content_extract.py`（文本 → 内容层特征）、`aggregate.py`（字段卡 → 分布）、`mutate.py` + `calibrate.py`（定向退化与校准）。

**依赖**：`pypdf`。`data/papers.jsonl` 已生成，除新增论文外不需要重跑。

```bash
pip install pypdf
python scripts/extract.py  --root <论文根目录> --out data/papers.jsonl --shards 5 --shard 0   # 分片跑，避开多进程
python scripts/aggregate.py --jsonl data/papers.jsonl --outdir .
```

## 读数顺序

1. `references/findings.md` — **16 条带数据的判断**，这是蒸馏的结论，先读这份。
2. `references/problems/<题号>.md` — 你那道题的规模区间、章节出现率、逐年漂移。
3. `references/rubric.md` — 六维评分卡（事前当动作清单，事后当判据）。
4. `references/judge-questions.md` — 评委预设怀疑清单。
5. `references/anti-patterns.md` — 扣分点与别学清单。
6. `references/contract.md` — 与管线交接的两份文件格式。

## 与本仓库管线的接口

| 时点 | 调用 | 产出 | 谁读 |
|---|---|---|---|
| 写 `plan.md` 之前 | brief | `reports/AWARD_BRIEF.md` | `1start-mathmodel`、`2analysis-modeling` |
| 提交之前 | review | `reports/JUDGE_REVIEW.md` | `5writing`（改稿）、`6verify`（gate） |

本技能**只读不写**：不修改 `paper/`、`code/`、`results/`。

## 尚未完成的部分（不要当成已完成）

1. **校准只做了 pilot。** 3 篇 × 4 个定向退化的结果见 `references/calibration.md`：摘要维灵敏且特异，建模过程部分灵敏，**检验维的句级计数代理失效**（删掉整节只掉 1–4 句）。完整校准需每题 2 篇、共 48 次评分。
2. **摘录只覆盖 1 篇。** `exemplars.md` 目前只来自 2024-ICM-E，计划扩到每题 2–3 篇。
3. **语义字段未人工校核。** 论证类型、摘要首句类型由规则抽取，存在误判。
4. **档位阈值（85/65）未校准。** 现在只能给方向，不能当承诺。

## 已知的数据不可靠处

- AI 使用报告章的检出率（10–23%）是正则漏检，不是事实；2024 起该报告是强制项。
- 摘要词数按"第 1 页去掉两行页眉"估算，约 10% 样本首页是封面，会得到异常小值。
- 章节存在性靠标题正则，双栏排版或标题不折行时会漏。
- 图表数取图注行计数，图注折行会少计 1–2 张。
