# -*- coding: utf-8 -*-
"""
mcm-judge / aggregate.py
把 papers.jsonl 汇总成按题号（A–F）分开的特征分布，并生成可读的 Markdown。
用法：python aggregate.py --jsonl data/papers.jsonl --outdir .
"""
import argparse, json, os, statistics as st
from collections import Counter, defaultdict

MIN_CHARS = 3000


def q(vals, p):
    if not vals:
        return None
    vals = sorted(vals)
    k = max(0, min(len(vals) - 1, int(round(p * (len(vals) - 1)))))
    return vals[k]


def band(n, d):
    return round(100.0 * n / d, 1) if d else 0.0


def tier(rate):
    if rate >= 95:
        return "floor"
    if rate >= 60:
        return "strong"
    if rate >= 40:
        return "weak"
    return "style"


def load(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        if r.get("kind") != "paper":
            continue
        if r.get("error") or r.get("chars", 0) < MIN_CHARS:
            continue
        rows.append(r)
    return rows


NUMS = [("pages", "pages"), ("fig_captions", "fig_captions"), ("tab_captions", "tab_captions"),
        ("fig_max_ref", "fig_max_ref"), ("tab_max_ref", "tab_max_ref"),
        ("abstract_words", "abstract_words"), ("ref_count", "ref_count"),
        ("words", "words")]


def describe(rows):
    d = {"n": len(rows)}
    for key, _ in NUMS:
        vals = [r.get(key, 0) for r in rows if isinstance(r.get(key), (int, float))]
        d[key] = {"median": q(vals, .5), "p25": q(vals, .25), "p75": q(vals, .75),
                  "min": min(vals) if vals else None, "max": max(vals) if vals else None}
    # 章节出现率
    secs = Counter()
    for r in rows:
        for k, v in r.get("sections", {}).items():
            if v:
                secs[k] += 1
    d["sections"] = {k: band(v, len(rows)) for k, v in secs.most_common()}
    # 关键词出现率（出现过即算）
    kwr = Counter()
    for r in rows:
        for k, v in r.get("kw", {}).items():
            if v > 0:
                kwr[k] += 1
    d["kw_presence"] = {k: band(v, len(rows)) for k, v in kwr.most_common()}
    # 关键词强度（中位数次数）
    d["kw_intensity"] = {}
    for k in kwr:
        vals = [r["kw"].get(k, 0) for r in rows]
        d["kw_intensity"][k] = q(vals, .5)
    # 摘要首句类型
    ft = Counter(r.get("abstract_first_type", "other") for r in rows)
    d["abstract_first_type"] = {k: band(v, len(rows)) for k, v in ft.most_common()}
    d["abstract_has_number"] = band(sum(1 for r in rows if r.get("abstract_has_number")), len(rows))
    d["abstract_words_ok"] = band(sum(1 for r in rows if 150 <= r.get("abstract_words", 0) <= 600), len(rows))
    return d


def load_content(path):
    if not path or not os.path.exists(path):
        return {}
    d = {}
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        if r.get("skip"):
            continue
        d[r["id"]] = r
    return d


def describe_content(rows):
    n = len(rows)
    if not n:
        return None
    mc = Counter()
    for r in rows:
        for m in r.get("models", []):
            mc[m] += 1
    out = {"n": n, "models": {k: band(v, n) for k, v in mc.most_common(14)}}
    for key, label in [("arg_attr", "归因式论证"), ("arg_compare", "对比式"), ("arg_lit", "文献式"),
                       ("arg_data", "数据驱动式"), ("param_sent", "参数来源句"),
                       ("valid_sent", "检验句"), ("decide_sent", "决策翻译句")]:
        vals = [r.get(key, 0) for r in rows]
        out[key] = {"cover": band(sum(1 for v in vals if v > 0), n),
                    "median": q(vals, .5), "p75": q(vals, .75)}
    a = [r.get("assume_sent", 0) for r in rows]
    j = [r.get("assume_justified", 0) for r in rows]
    out["assume"] = {"median": q(a, .5), "justified_cover": band(sum(1 for v in j if v > 0), n)}
    out["taskmark"] = q([r.get("taskmark", 0) for r in rows], .5)
    return out


def md_problem(prob, d, by_year, recent=None, content=None):
    L = []
    L.append("# Problem %s — O 奖论文特征分布（n=%d）\n" % (prob, d["n"]))
    L.append("> 数据来源：2017–2025 年 MCM/ICM Outstanding 论文，脚本抽取；"
             "只统计可解析文本的论文（字符数 ≥ %d）。\n" % MIN_CHARS)
    L.append("## 规模分布\n")
    L.append("| 指标 | 中位数 | P25 | P75 | 最小 | 最大 |")
    L.append("|---|---|---|---|---|---|")
    for key, label in [("pages", "总页数"), ("fig_captions", "图（题注数）"), ("tab_captions", "表（题注数）"),
                       ("abstract_words", "摘要词数"), ("ref_count", "参考文献数"), ("words", "正文词数")]:
        s = d[key]
        L.append("| %s | %s | %s | %s | %s | %s |" % (label, s["median"], s["p25"], s["p75"], s["min"], s["max"]))
    L.append("")
    L.append("## 章节出现率\n")
    L.append("| 章节 | 出现率 | 分级 |")
    L.append("|---|---|---|")
    order = {"floor": 0, "strong": 1, "weak": 2, "style": 3}
    for k, v in sorted(d["sections"].items(), key=lambda x: (-x[1], x[0])):
        L.append("| %s | %.1f%% | %s |" % (k, v, tier(v)))
    L.append("")
    L.append("## 建模与技术关键词出现率（出现在 ≥1 次即计）\n")
    L.append("| 关键词 | 出现率 | 中位次数 |")
    L.append("|---|---|---|")
    for k, v in d["kw_presence"].items():
        if v >= 20:
            L.append("| %s | %.1f%% | %s |" % (k, v, d["kw_intensity"].get(k)))
    L.append("")
    L.append("## 摘要形态\n")
    L.append("- 含数字结论：%.1f%%" % d["abstract_has_number"])
    L.append("- 词数落在 150–600：%.1f%%" % d["abstract_words_ok"])
    L.append("- 首句类型分布：%s" % ", ".join("%s=%.1f%%" % (k, v) for k, v in d["abstract_first_type"].items()))
    L.append("")
    L.append("## 逐年漂移（页数 / 图 / 摘要词数 中位数）\n")
    L.append("| 年份 | n | 页数 | 图 | 摘要词数 | AI 报告章† |")
    L.append("|---|---|---|---|---|---|")
    for y in sorted(by_year):
        e = by_year[y]
        L.append("| %s | %d | %s | %s | %s | %s%% |" % (y, e["n"], e["pages"], e["fig_captions"],
                                                       e["abstract_words"], e["ai_report"]))
    L.append("")
    L.append("† AI 报告章按标题正则检出，漏检严重（2024–2025 实为强制项，检出率仅 37–40%），"
             "不要用这个数字判断该不该写 AI 报告，只用于说明标题写法不统一。")
    if recent:
        L.append("## 近五年格式基线（2021–2025，n=%d）\n" % recent["n"])
        L.append("> 2021 年起 25 页上限成为实际约束，早年的页数与图数不可直接比较；格式类判断只用这一块。\n")
        L.append("| 指标 | 中位数 | P25 | P75 | 最小 | 最大 |")
        L.append("|---|---|---|---|---|---|")
        for key, label in [("pages", "总页数"), ("fig_captions", "图"), ("tab_captions", "表"),
                           ("abstract_words", "摘要词数"), ("ref_count", "参考文献数")]:
            s = recent[key]
            L.append("| %s | %s | %s | %s | %s | %s |" % (label, s["median"], s["p25"], s["p75"], s["min"], s["max"]))
        L.append("")
        L.append("地板/强倾向（近五年）：%s" % ", ".join(
            "%s=%.0f%%" % (k, v) for k, v in recent["sections"].items() if v >= 60))
        L.append("")
    if content:
        L.append("## 内容层：模型与建模过程（n=%d）\n" % content["n"])
        L.append("### 模型家族出现率\n")
        L.append("| 模型家族 | 出现率 |")
        L.append("|---|---|")
        for k, v in content["models"].items():
            L.append("| %s | %.1f%% |" % (k, v))
        L.append("")
        L.append("### 论证与过程交代\n")
        L.append("| 项目 | 覆盖率 | 中位句数 | P75 |")
        L.append("|---|---|---|---|")
        for key, label in [("arg_attr", "归因式论证"), ("arg_compare", "对比式"), ("arg_lit", "文献式"),
                           ("arg_data", "数据驱动式"), ("param_sent", "参数来源"), ("valid_sent", "检验"),
                           ("decide_sent", "决策翻译")]:
            e = content[key]
            L.append("| %s | %.1f%% | %s | %s |" % (label, e["cover"], e["median"], e["p75"]))
        L.append("")
        L.append("- 假设句：中位 %s 条；含理由的论文占 %.1f%%" % (
            content["assume"]["median"], content["assume"]["justified_cover"]))
        L.append("- 子问题标记（Task/Question N）：中位 %s 个" % content["taskmark"])
        L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jsonl", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--content", default=None, help="content.jsonl，用于内容层统计")
    a = ap.parse_args()
    rows = load(a.jsonl)
    cmap = load_content(a.content)
    if not rows:
        raise SystemExit("没有可用记录，检查 jsonl 路径与 MIN_CHARS")

    out = {"meta": {"n_total": len(rows), "min_chars": MIN_CHARS,
                    "years": sorted({r["year"] for r in rows}),
                    "source": os.path.basename(a.jsonl)}, "problems": {}}

    probdir = os.path.join(a.outdir, "references", "problems")
    os.makedirs(probdir, exist_ok=True)
    os.makedirs(os.path.join(a.outdir, "data"), exist_ok=True)

    for prob in "ABCDEF":
        sub = [r for r in rows if r["problem"] == prob]
        if not sub:
            continue
        d = describe(sub)
        by_year = {}
        for y in sorted({r["year"] for r in sub}):
            ys = [r for r in sub if r["year"] == y]
            dy = describe(ys)
            by_year[str(y)] = {"n": dy["n"], "pages": dy["pages"]["median"],
                               "fig_captions": dy["fig_captions"]["median"],
                               "abstract_words": dy["abstract_words"]["median"],
                               "ai_report": dy["sections"].get("ai_report", 0)}
        recent = describe([r for r in sub if r["year"] >= 2021])
        csub = [cmap[r["id"]] for r in sub if r["id"] in cmap]
        cdesc = describe_content(csub)
        out["problems"][prob] = {"summary": d, "by_year": by_year, "recent": recent, "content": cdesc}
        with open(os.path.join(probdir, "%s.md" % prob), "w", encoding="utf-8") as f:
            f.write(md_problem(prob, d, by_year, recent, cdesc))

    with open(os.path.join(a.outdir, "data", "features.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    # 总览
    L = ["# O 奖论文特征总览（n=%d，%s）\n" % (len(rows), ",".join(str(y) for y in out["meta"]["years"])),
         "| 题号 | n | 页数中位 | 图中位 | 表中位 | 摘要词数中位 | 有独立结论章 | 有检验章 |",
         "|---|---|---|---|---|---|---|---|"]
    for prob in "ABCDEF":
        if prob not in out["problems"]:
            continue
        s = out["problems"][prob]["summary"]
        L.append("| %s | %d | %s | %s | %s | %s | %.0f%% | %.0f%% |" % (
            prob, s["n"], s["pages"]["median"], s["fig_captions"]["median"], s["tab_captions"]["median"],
            s["abstract_words"]["median"], s["sections"].get("conclusion", 0), s["sections"].get("sensitivity", 0)))
    L.append("")
    if any(out["problems"][p].get("content") for p in out["problems"]):
        L.append("## 内容层：模型与建模过程\n")
        L.append("| 题号 | 首要模型家族 | 归因式论证 | 参数来源 | 检验 | 决策翻译 |")
        L.append("|---|---|---|---|---|---|")
        for prob in "ABCDEF":
            c = out["problems"].get(prob, {}).get("content")
            if not c:
                continue
            tops = ", ".join(list(c["models"])[:3])
            L.append("| %s | %s | %.0f%% | %.0f%% | %.0f%% | %.0f%% |" % (
                prob, tops, c["arg_attr"]["cover"], c["param_sent"]["cover"],
                c["valid_sent"]["cover"], c["decide_sent"]["cover"]))
        L.append("")
    with open(os.path.join(a.outdir, "references", "o-features.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    print("wrote features.json + references/problems/*.md + references/o-features.md")
    print("| 题 | n | 页 | 图 | 表 | 摘要词 | 结论章 | 检验章 |")
    for prob in "ABCDEF":
        if prob in out["problems"]:
            s = out["problems"][prob]["summary"]
            print("| %s | %d | %s | %s | %s | %s | %.0f%% | %.0f%% |" % (
                prob, s["n"], s["pages"]["median"], s["fig_captions"]["median"], s["tab_captions"]["median"],
                s["abstract_words"]["median"], s["sections"].get("conclusion", 0), s["sections"].get("sensitivity", 0)))


if __name__ == "__main__":
    main()
