# -*- coding: utf-8 -*-
"""
mcm-judge / calibrate.py
证据级校准：把评分卡里可自动测量的维度实现成谓词，对「原文 vs 定向退化」逐版打分，
输出灵敏度（该降的维度降了没）与特异度（不该动的维度动没动）。

可测维度：建模过程、模型、检验、摘要。内容与图表两维依赖人工判断，此处不出分。
用法：python calibrate.py --dir data/mutations/<id> --out data/calibration.json
"""
import argparse, glob, json, os, re, statistics as st

ARG_ATTR = re.compile(
    r"(?i)(because|since|due to|given (?:the|that)|considering|owing to)[^.]{0,160}?"
    r"(we (?:use|used|employ|employed|adopt|adopted|apply|applied|choose|chose|select|selected|build|built|establish|developed)"
    r"|therefore|thus|hence|so that|which (?:allows|enables|makes))")
PARAM = re.compile(
    r"(?i)calibrat|estimated (?:from|by|using|as)|obtained from|taken from|set to|assumed (?:as|to be)|"
    r"according to (?:the )?literature|fitted|tuned|optimi[sz]ed (?:by|using)")
VALID = re.compile(
    r"(?i)sensitivit|sensitivity analysis|robustness|stability|ablation|cross[- ]validation|"
    r"hold[- ]out|leave[- ]one[- ]out|monte[ -]carlo|bootstrap|error analysis|residual|back[- ]testing")
MODELNAME = re.compile(
    r"(?i)regression|arima|lstm|neural net|random forest|xgboost|pca|principal component|"
    r"entropy weight|topsis|ahp|analytic hierarchy|linear program|integer program|multi-?objective|"
    r"pareto|nsga|genetic algorithm|simulated annealing|particle swarm|dijkstra|graph theory|"
    r"differential equation|sir model|cellular automat|markov|monte[ -]carlo|game theor|fuzzy|k-?means|"
    r"cluster|factor analysis|supply[- ]demand|equilibrium")


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", text) if 20 < len(s) < 600]


def abstract_of(text):
    m = re.search(r"(?s)^(.*?)(?:===== PAGE 2 =====|$)", text)
    head = m.group(1) if m else text[:4000]
    lines = [l for l in head.splitlines() if l.strip()]
    return "\n".join(lines[2:]) if len(lines) > 4 else head


def score(text):
    m2 = re.search(r"(?s)^.*?===== PAGE 2 =====", text)
    body = text[m2.end():] if m2 else text
    s = sentences(body)
    ab = abstract_of(text)
    abw = len(re.findall(r"[A-Za-z][A-Za-z'\-]+", ab))
    abnum = bool(re.search(r"\d", ab))
    abmethod = bool(re.search(r"(?i)we (?:use|employ|adopt|apply|build|establish|develop|propose)", ab))

    n_attr = sum(1 for x in s if ARG_ATTR.search(x))
    n_param = sum(1 for x in s if PARAM.search(x))
    n_valid = sum(1 for x in s if VALID.search(x))
    models = {m.group(0).lower() for m in MODELNAME.finditer(text)}
    n_model = len(models)

    # 建模过程 0-10
    p = 4
    if n_attr >= 1: p = 6
    if n_attr >= 3: p = 7
    if n_attr >= 5: p = 8
    if n_attr >= 8: p = 9
    if n_param == 0: p = min(p, 4)
    # 模型 0-10
    mo = 2 if n_model == 0 else 5 if n_model == 1 else 6 if n_model == 2 else 7 if n_model == 3 else 6
    # 检验 0-10
    va = 0 if n_valid == 0 else 4 if n_valid <= 3 else 7 if n_valid <= 9 else 9
    # 摘要 0-10
    su = 3
    if abmethod: su += 2
    if abnum: su += 2
    if 350 <= abw <= 560: su += 2
    if abmethod and abnum and 350 <= abw <= 560: su += 1
    su = min(10, su)
    return {"建模过程": p, "模型": mo, "检验": va, "摘要": su,
            "ev": {"arg_attr": n_attr, "param": n_param, "valid": n_valid,
                   "n_model": n_model, "abw": abw, "abnum": abnum, "abmethod": abmethod}}


TARGET = {"M1_abstract_restate": "摘要", "M2_no_validation": "检验",
          "M3_no_param_source": "建模过程", "M4_vague_sw": None}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    files = sorted(glob.glob(os.path.join(a.dir, "*.txt")))
    res = {}
    for f in files:
        base = os.path.basename(f)[:-4]
        variant = base.split("__")[-1]
        txt = open(f, encoding="utf-8", errors="ignore").read()
        res[variant] = score(txt)
    report = {"scores": res, "delta": {}, "target": {}}
    if "base" in res:
        for v, sc in res.items():
            if v == "base":
                continue
            tgt = TARGET.get(v)
            report["target"][v] = tgt
            report["delta"][v] = {k: sc[k] - res["base"][k] for k in ("建模过程", "模型", "检验", "摘要")}
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)

    for v, sc in res.items():
        print("%-22s 建模%d 模型%d 检验%d 摘要%d   (attr=%d param=%d valid=%d models=%d abw=%d)" % (
            v, sc["建模过程"], sc["模型"], sc["检验"], sc["摘要"],
            sc["ev"]["arg_attr"], sc["ev"]["param"], sc["ev"]["valid"], sc["ev"]["n_model"], sc["ev"]["abw"]))
    for v, d in report["delta"].items():
        print("delta %-20s -> %s" % (v, d))


if __name__ == "__main__":
    main()
