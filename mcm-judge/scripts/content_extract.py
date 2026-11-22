# -*- coding: utf-8 -*-
"""
mcm-judge / content_extract.py
内容层抽取：从 data/text/*.txt 抽出「建模过程」与「模型」证据。
- 模型家族出现与否
- 论证方式（归因式／对比式／文献式／数据驱动式）
- 参数来源是否交代
- 检验方式
- 决策翻译
- 假设是否附理由
- 子问题标记数
用法：python content_extract.py --textdir data/text --out data/content.jsonl
"""
import argparse, glob, json, os, re
from collections import Counter

MODELS = [
    ("regression", r"\b(?:multiple |linear |logistic )?regression\b|geographically weighted|\bmgwr\b|\bgwr\b"),
    ("timeseries", r"\barima\b|\bsarima\b|exponential smoothing|holt[- ]winters"),
    ("tree_ml", r"random forest|xgboost|lightgbm|gradient boosting|decision tree|catboost"),
    ("neural_net", r"neural net|deep learning|\bcnn\b|\brnn\b|\blstm\b|\bgru\b|transformer"),
    ("svm", r"support vector"),
    ("clustering", r"k-?means|\bdbscan\b|hierarchical cluster|gaussian mixture"),
    ("dim_reduction", r"\bpca\b|principal component|\btsne\b|\bumap\b|factor analysis"),
    ("weighting", r"entropy weight|analytic hierarchy|\bahp\b|\bcritic\b|coefficient of variation"),
    ("mcdm_rank", r"\btopsis\b|grey relation|\bvikor\b|\belectre\b|\bpromethee\b|data envelopment|\bdea\b"),
    ("fuzzy", r"fuzzy (?:logic|set|comprehensive|evaluation|ahp|clustering)"),
    ("lp_milp", r"linear program|integer program|mixed[- ]integer|\bmilp\b|linear programming"),
    ("nonlinear_opt", r"nonlinear program|convex optimi|quadratic program"),
    ("multi_objective", r"multi-?objective|pareto|\bnsga\b|weighted sum method|epsilon[- ]constraint"),
    ("heuristic", r"genetic algorithm|simulated annealing|particle swarm|ant colony|tabu search|differential evolution"),
    ("graph", r"dijkstra|floyd|minimum spanning|shortest path|maximu?m flow|graph theory|network flow"),
    ("diff_eq", r"differential equation|\bode\b|\bpde\b|lotka|sir model|seir|\bcompartment"),
    ("cellular", r"cellular automat"),
    ("sys_dynamics", r"system dynamic"),
    ("queuing", r"queuing|queueing|m/m/\d"),
    ("game", r"game theor|nash|stackelberg|evolutionary game"),
    ("markov", r"markov"),
    ("monte_carlo", r"monte[ -]carlo"),
    ("simulation", r"discrete event simulation|agent[- ]based"),
    ("spatial", r"\bgis\b|spatial autocorrelation|moran"),
    ("stat_test", r"\bt-test\b|\banova\b|chi-square|\bks test\b|hypothesis test|p-value"),
    ("curve_fit", r"interpolation|curve fitting|least square|spline"),
    ("diffusion", r"\bepidemic\b|infection model|bass model|diffusion model"),
    ("risk", r"value at risk|expected shortfall|risk assessment|\bvar\b"),
    ("equilibrium", r"equilibrium|supply[- ]demand|market clearing"),
]

ARG_ATTR = re.compile(
    r"(?i)(because|since|due to|given (?:the|that)|considering|owing to|as a result of|in light of)"
    r"[^.]{0,160}?"
    r"(we (?:use|used|employ|employed|adopt|adopted|apply|applied|choose|chose|select|selected|build|built|establish|develop|developed)"
    r"|therefore|thus|hence|so that|which (?:allows|enables|makes))")
ARG_COMPARE = re.compile(r"(?i)compared (?:with|to)|in contrast|unlike|instead of|rather than|outperform|superior to")
ARG_LIT = re.compile(r"(?i)following (?:the )?(?:method|approach|work)|proposed by|as (?:in|described in) \[?\d|based on the (?:method|model|framework) (?:of|proposed)")
ARG_DATA = re.compile(r"(?i)given the (?:high )?(?:dimensionality|complexity|scarcity)|with only \d+|comprising \d+|consists? of \d+|due to the (?:limited|large|sparse|missing|small)")

PARAM = re.compile(
    r"(?i)calibrat|estimated (?:from|by|using|as)|obtained from|taken from|set to|assumed (?:as|to be)|"
    r"according to (?:the )?literature|fitted|tuned|optimi[sz]ed (?:by|using)|from \[?\d")
VALID = re.compile(
    r"(?i)sensitivit|sensitivity analysis|robustness|stability|ablation|cross[- ]validation|hold[- ]out|"
    r"leave[- ]one[- ]out|monte[ -]carlo|bootstrap|error analysis|residual|back[- ]testing|out[- ]of[- ]sample")
DECIDE = re.compile(
    r"(?i)decision[- ]maker|policymaker|policy maker|recommend|suggest|\bguideline|implication|"
    r"for (?:the )?(?:company|companies|government|community|owner|owners|investor|residents|policymakers)")
ASSUME = re.compile(r"(?i)\bassum")
JUSTIF = re.compile(r"(?i)because|since|due to|reasonable|justif|as the|in practice")
TASKMARK = re.compile(r"(?i)\b(?:task|question|part|problem)\s*([1-9])\b")


def sentences(text):
    return re.split(r"(?<=[.!?])\s+", text)


def analyse(path):
    stem = os.path.splitext(os.path.basename(path))[0]   # year-prob-id
    try:
        year, prob, pid = stem.split("-", 2)
    except ValueError:
        year, prob, pid = "", "", stem
    text = open(path, encoding="utf-8", errors="replace").read()
    low = text
    # 正文指标排除摘要页：摘要句子若计入正文，会虚高归因/参数/检验的覆盖
    m2 = re.search(r"(?s)^.*?===== PAGE 2 =====", text)
    body = text[m2.end():] if m2 else text
    out = {"id": "%s/%s/%s" % (year, prob, pid), "year": int(year) if year.isdigit() else 0,
           "problem": prob, "chars": len(text)}
    if len(text) < 2000:
        out["skip"] = True
    m = Counter()
    for name, pat in MODELS:
        if re.search(pat, low, re.I):
            m[name] += 1
    out["models"] = sorted(m)
    out["n_models"] = len(m)

    sents = [s for s in sentences(body) if 20 < len(s) < 600]
    out["n_sent"] = len(sents)
    out["arg_attr"] = sum(1 for s in sents if ARG_ATTR.search(s))
    out["arg_compare"] = sum(1 for s in sents if ARG_COMPARE.search(s))
    out["arg_lit"] = sum(1 for s in sents if ARG_LIT.search(s))
    out["arg_data"] = sum(1 for s in sents if ARG_DATA.search(s))

    # 参数来源：以句子为单位统计
    out["param_sent"] = sum(1 for s in sents if PARAM.search(s))
    out["valid_sent"] = sum(1 for s in sents if VALID.search(s))
    out["decide_sent"] = sum(1 for s in sents if DECIDE.search(s))
    asum = [s for s in sents if ASSUME.search(s)]
    out["assume_sent"] = len(asum)
    out["assume_justified"] = sum(1 for s in asum if JUSTIF.search(s))
    out["taskmark"] = len({int(x) for x in TASKMARK.findall(text)})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--textdir", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    files = sorted(glob.glob(os.path.join(a.textdir, "*.txt")))
    with open(a.out, "w", encoding="utf-8") as fo:
        for i, f in enumerate(files, 1):
            rec = analyse(f)
            fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if i % 50 == 0:
                print("[%d/%d]" % (i, len(files)), flush=True)
    print("DONE %d" % len(files), flush=True)


if __name__ == "__main__":
    main()
