# -*- coding: utf-8 -*-
"""
mcm-judge / mutate.py
对一篇论文的纯文本做定向退化，生成负例，用于校准评分卡。
四个变异各打一个维度：
  M1 abstract  -> 摘要
  M2 nolint    -> 检验与稳健性
  M3 noparam   -> 建模过程
  M4 novague   -> 内容与结构（优劣势替换为免责声明）
用法：python mutate.py --text <文件> --outdir <目录>
"""
import argparse, os, re

HEAD = re.compile(r"(?im)^[ \t]*(?:\d+\.?\d*[ \t]*)?([A-Z][A-Za-z ,'\-]{2,60})[ \t]*$")
VALID = re.compile(r"(?i)(sensitiv|robust|stabilit|ablation|error analysis|model validation|discussion)")
SW = re.compile(r"(?i)(strengths?|weakness|advantages?|limitation)")
PARAM = re.compile(
    r"(?i)calibrat|estimated (?:from|by|using|as)|obtained from|taken from|set to|assumed (?:as|to be)|"
    r"according to (?:the )?literature|fitted|tuned|optimi[sz]ed (?:by|using)")

BOILER_SUMMARY = (
    "This paper studies the problem described in the task. We build a model to analyze the situation "
    "and solve the proposed questions. The model is reasonable and the results are obtained by "
    "computation. In this paper, the background, assumptions, model construction, solution and "
    "conclusion are presented in order. The results show that our approach is effective.\n"
)
BOILER_SW = (
    "Strengths and Weaknesses\n"
    "Our model has some strengths. It is reasonable and effective. Due to time constraints, "
    "some further analysis has not been carried out, which can be improved in future work.\n"
)


def blocks(text):
    """按疑似标题行切块，返回 [(start, end, title)]"""
    lines = text.splitlines()
    idx, out = [], []
    for i, ln in enumerate(lines):
        if 3 < len(ln.strip()) < 70 and HEAD.match(ln) and not ln.strip().endswith("."):
            idx.append(i)
    for k, i in enumerate(idx):
        j = idx[k + 1] if k + 1 < len(idx) else len(lines)
        out.append((i, j, lines[i].strip()))
    return lines, out


def cut_block(text, pattern, max_extra=250):
    """切掉匹配 pattern 的章节：在所有命中行里选「块最大」的那个，避免删到目录或列表项。
    返回 (新文本, 是否切到)。"""
    lines = text.splitlines()
    n = len(lines)
    cand = [i for i, l in enumerate(lines)
            if pattern.search(l) and 3 < len(l.strip()) < 90
            and not re.search(r"\.{3,}\s*\d*$", l)]
    if not cand:
        return text, False

    def block(i):
        j = n
        for k in range(i + 1, min(n, i + max_extra)):
            s = lines[k].strip()
            if 3 < len(s) < 70 and HEAD.match(lines[k]) and not s.endswith("."):
                j = k
                break
        return i, j

    best = max((block(i) for i in cand), key=lambda ij: ij[1] - ij[0])
    i, j = best
    if j - i < 3:                      # 太小，说明没找到真段落
        return text, False
    return "\n".join(lines[:i] + lines[j:]), True


def strip_sentences(text, pattern):
    parts = re.split(r"(?<=[.!?])\s+", text)
    kept = [p for p in parts if not pattern.search(p)]
    return " ".join(kept)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True)
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    t = open(a.text, encoding="utf-8", errors="replace").read()
    os.makedirs(a.outdir, exist_ok=True)
    base = os.path.splitext(os.path.basename(a.text))[0]
    variants = {"base": t}

    m1 = re.sub(r"(?s)^.*?(?====== PAGE 2 =====)", BOILER_SUMMARY + "\n", t, count=1)
    variants["M1_abstract_restate"] = m1
    m2, ok2 = cut_block(t, VALID)
    variants["M2_no_validation"] = m2
    variants["M3_no_param_source"] = strip_sentences(t, PARAM)
    m4, ok4 = cut_block(t, SW)
    variants["M4_vague_sw"] = m4.rstrip() + "\n\n" + BOILER_SW
    print("cut validation section: %s (%d chars removed)" % (ok2, len(t) - len(m2)))
    print("cut strengths section : %s (%d chars removed)" % (ok4, len(t) - len(m4)))

    for k, v in variants.items():
        p = os.path.join(a.outdir, "%s__%s.txt" % (base, k))
        open(p, "w", encoding="utf-8").write(v)
        print("%-22s %6d chars" % (k, len(v)))


if __name__ == "__main__":
    main()
