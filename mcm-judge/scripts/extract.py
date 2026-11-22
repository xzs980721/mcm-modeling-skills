# -*- coding: utf-8 -*-
"""
mcm-judge / extract.py
把一批 O 奖论文 PDF 抽成同一张字段卡（JSONL）。
用法：python extract.py --root <论文根目录> --out <jsonl>
"""
import argparse, hashlib, json, os, re, sys, traceback

# ---------- 章节词表 ----------
SEC = [
    ("introduction",  r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?introduction\b"),
    ("restatement",   r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(problem[ \t]+(?:re-?statement|description|analysis|background)|re-?statement of the problem)"),
    ("related_work",  r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(related[ \t]+works?|literature[ \t]+review|background and related)"),
    ("assumptions",   r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(assumptions?|model assumptions|basic assumptions|general assumptions)"),
    ("notation",      r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(notations?|nomenclature|list of (?:symbols|notation)|symbols? (?:and|&) (?:description|definitions?)|definitions? of symbols)"),
    ("model",         r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(model (?:construction|establishment|building|design|formulation|development)|mathematical model|the [a-z\- ]{2,30}model\b|modeling)"),
    ("solution",      r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(solutions?|results?|solving|numerical (?:results?|simulations?)|model (?:solving|solution))"),
    ("sensitivity",   r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(sensitivity|robustness|stability|error analysis|uncertainty analysis|sensitivity analysis)"),
    ("strengths",     r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(strengths?|advantages?)"),
    ("weaknesses",    r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(weakness(?:es)?|disadvantages?|limitations?|shortcomings?)"),
    ("conclusion",    r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(conclusions?|concluding remarks|summary and conclusions|conclusions? and (?:future|outlook))"),
    ("references",    r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(references?|bibliography)\b"),
    ("appendix",      r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(appendi(?:x|ces))\b"),
    ("ai_report",     r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(report on (?:the )?use of ai|use of ai|ai (?:use|utilization|usage)|ai[- ]assisted|ai statement)"),
    ("toc",           r"(?im)^[ \t]*(?:table of )?contents\b"),
    ("letter",        r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(a )?letter to\b"),
    ("memo",          r"(?im)^[ \t]*(?:\d+\.?[ \t]*)?(memorandum|memo)\b"),
]

KW = {
    "sensitivity": r"sensitiv",
    "robust": r"robust",
    "ablation": r"ablation",
    "uncertainty": r"uncertaint",
    "validation": r"validat",
    "error": r"error",
    "assumption": r"assumption",
    "limitation": r"limitation",
    "weakness": r"weakness",
    "strength": r"strength",
    "comparison": r"compar",
    "baseline": r"\bbaseline",
    "optimization": r"optimi[sz]",
    "simulation": r"simulat",
    "monte_carlo": r"monte[ -]carlo",
    "trade_off": r"trade[ -]?off",
    "regression": r"regression",
    "classifier": r"classif",
    "clustering": r"cluster",
    "game_theory": r"game[ -]theor",
    "ode_pde": r"\b(?:ode|pde|differential equation)",
    "network": r"networ",
    "agent_based": r"agent[ -]based",
    "ahp": r"\bahp\b|analytic hierarchy",
    "entropy_weight": r"entropy weight",
    "topsis": r"\btopsis\b",
    "grey_relation": r"grey (?:relation|correlation)",
    "markov": r"markov",
    "random_forest": r"random forest",
    "neural_net": r"neural net",
    "lstm": r"\blstm\b",
    "arima": r"\barima\b",
    "pca": r"\bpca\b|principal component",
    "kmeans": r"k-?means",
    "integer_programming": r"integer program",
    "linear_programming": r"linear program",
    "genetic_algo": r"genetic algorithm",
    "simulated_annealing": r"simulated annealing",
    "particle_swarm": r"particle swarm",
    "cellular_automata": r"cellular automat",
    "system_dynamics": r"system dynamic",
    "queuing": r"queue|queuing",
    "dijkstra": r"dijkstra|shortest path",
}

COMMENTARY_RE = re.compile(
    r"(?i)(com[-_][a-f]\b|judges?_?com|authors?_?com|expert_?com|umap|tips|_summary\.|problems?)")

NUM_RE = re.compile(r"\d+(?:\.\d+)?")
FIG_REF = re.compile(r"(?i)\b(?:figure|fig\.)\s*(\d{1,2})\b")
TAB_REF = re.compile(r"(?i)\btable\s*(\d{1,2})\b")
FIG_CAP = re.compile(r"(?im)^[ \t]*(?:figure|fig\.)\s*\d+")
TAB_CAP = re.compile(r"(?im)^[ \t]*table\s*\d+")
CJK = re.compile(r"[\u4e00-\u9fff]")


def first_sentence(text, limit=400):
    t = re.sub(r"\s+", " ", text).strip()
    m = re.search(r"[.!?](?:\s|$)", t)
    return t[: m.end()] if m and m.end() <= limit else t[:limit]


def split_first_sentence(s):
    """摘要首句类型：background / result / method / problem"""
    s = s.lower()
    if re.search(r"\b(we (?:propose|develop|build|establish|present|introduce|construct)|this paper (?:proposes|develops|presents)|our (?:model|approach|framework))", s):
        return "method"
    if re.search(r"\b(in this (?:paper|study)|herein|this study)\b", s):
        return "method"
    if re.search(r"\d", s) and re.search(r"%|increase|decrease|optimal|reduc|improv|yield|predicted", s):
        return "result"
    if re.search(r"\b(is|are|has|have|poses?|becomes?|faces?|plays?)\b", s):
        return "background"
    return "other"


def analyse(path, year, problem, fname):
    out = {"id": "%s/%s/%s" % (year, problem, os.path.splitext(fname)[0]),
           "year": int(year), "problem": problem, "file": path}
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    out["sha256"] = h.hexdigest()
    try:
        from pypdf import PdfReader
        r = PdfReader(path)
        pages = len(r.pages)
        texts = []
        for p in r.pages:
            try:
                texts.append(p.extract_text() or "")
            except Exception:
                texts.append("")
        text = "\n".join(texts)
    except Exception as e:
        out.update({"error": "%s: %s" % (type(e).__name__, e), "pages": 0, "chars": 0})
        return out

    out["pages"] = pages
    out["chars"] = len(text)
    out["words"] = len(re.findall(r"[A-Za-z][A-Za-z'\-]+", text))
    out["scanned"] = len(text) < 2000
    out["cjk_ratio"] = round(len(CJK.findall(text)) / max(1, len(text)), 4)

    sec = {}
    for name, pat in SEC:
        m = re.search(pat, text)
        sec[name] = bool(m)
    out["sections"] = sec

    fig_nums = {int(x) for x in FIG_REF.findall(text)}
    tab_nums = {int(x) for x in TAB_REF.findall(text)}
    out["fig_max_ref"] = max(fig_nums) if fig_nums else 0
    out["tab_max_ref"] = max(tab_nums) if tab_nums else 0
    out["fig_captions"] = len(FIG_CAP.findall(text))
    out["tab_captions"] = len(TAB_CAP.findall(text))

    low = text.lower()
    out["kw"] = {k: len(re.findall(p, low)) for k, p in KW.items()}

    # 摘要 = 第 1 页（COMAP 摘要页），去掉页眉两行
    p1 = texts[0] if texts else ""
    lines = [l for l in p1.splitlines() if l.strip()]
    ab = "\n".join(lines[2:]) if len(lines) > 4 else p1
    ab_clean = re.sub(r"\s+", " ", ab).strip()
    out["abstract_words"] = len(re.findall(r"[A-Za-z][A-Za-z'\-]+", ab_clean))
    out["abstract_has_number"] = bool(re.search(r"\d", ab_clean))
    out["abstract_first_sentence"] = first_sentence(ab_clean)
    out["abstract_first_type"] = split_first_sentence(out["abstract_first_sentence"])
    # 摘要里是否覆盖到分问题编号（如 "Task 1"/"(1)"/"question 2"）
    out["abstract_task_markers"] = len(re.findall(r"(?i)\b(task|question|part|problem|scenario)\s*[1-9]\b", ab_clean))

    # 引用计数：参考文献区里的 [n] 或 年份
    m = re.search(r"(?im)^[ \t]*(?:references?|bibliography)\b", text)
    if m:
        ref_sec = text[m.end(): m.end() + 20000]
        out["ref_count"] = len(re.findall(r"\[\d{1,3}\]", ref_sec)) or len(re.findall(r"\((?:19|20)\d\d\)", ref_sec))
    else:
        out["ref_count"] = 0
    out["cite_inline"] = len(re.findall(r"\[\d{1,3}\]", text))

    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--commentary-out", default=None)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--shard", type=int, default=0)
    ap.add_argument("--shards", type=int, default=1)
    a = ap.parse_args()

    jobs = []
    for year in sorted(os.listdir(a.root)):
        ydir = os.path.join(a.root, year)
        if not re.fullmatch(r"\d{4}", year) or not os.path.isdir(ydir):
            continue
        for prob in "ABCDEF":
            pdir = os.path.join(ydir, prob)
            if not os.path.isdir(pdir):
                continue
            for f in sorted(os.listdir(pdir)):
                if f.lower().endswith(".pdf"):
                    jobs.append((os.path.join(pdir, f), year, prob, f))
    if a.limit:
        jobs = jobs[: a.limit]
    if a.shards > 1:
        jobs = [j for i, j in enumerate(jobs) if i % a.shards == a.shard]

    com_out = a.commentary_out or (os.path.splitext(a.out)[0] + ".commentary.jsonl")

    def emit(rec, fo, fc, state):
        is_com = bool(COMMENTARY_RE.search(rec.get("_file", "")))
        rec.pop("_file", None)
        rec["kind"] = "commentary" if is_com else "paper"
        if is_com:
            fc.write(json.dumps(rec, ensure_ascii=False) + "\n"); fc.flush(); state["com"] += 1
        else:
            fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); fo.flush(); state["ok"] += 1

    ok = com = 0
    with open(a.out, "w", encoding="utf-8") as fo, open(com_out, "w", encoding="utf-8") as fc:
        state = {"ok": 0, "com": 0}
        if a.workers > 1:
            from concurrent.futures import ProcessPoolExecutor, as_completed
            with ProcessPoolExecutor(max_workers=a.workers) as ex:
                fut = {ex.submit(analyse, p, y, pr, f): f for (p, y, pr, f) in jobs}
                done = 0
                for fu in as_completed(fut):
                    fname = fut[fu]
                    try:
                        rec = fu.result()
                    except Exception:
                        rec = {"id": fname, "error": traceback.format_exc(limit=1)}
                    rec["_file"] = fname
                    emit(rec, fo, fc, state)
                    done += 1
                    if done % 20 == 0 or done == len(jobs):
                        print("[%d/%d] paper=%d commentary=%d" % (done, len(jobs), state["ok"], state["com"]), flush=True)
            ok, com = state["ok"], state["com"]
        else:
            for i, (path, year, prob, f) in enumerate(jobs, 1):
                try:
                    rec = analyse(path, year, prob, f)
                except Exception:
                    rec = {"id": "%s/%s/%s" % (year, prob, f), "error": traceback.format_exc(limit=1)}
                rec["_file"] = f
                emit(rec, fo, fc, state)
                if i % 20 == 0 or i == len(jobs):
                    print("[%d/%d] %s paper=%d commentary=%d" % (i, len(jobs), rec.get("id"), state["ok"], state["com"]), flush=True)
            ok, com = state["ok"], state["com"]
    print("DONE total=%d paper=%d commentary=%d" % (len(jobs), ok, com), flush=True)


if __name__ == "__main__":
    main()
