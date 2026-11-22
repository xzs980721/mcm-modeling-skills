# -*- coding: utf-8 -*-
"""
mcm-judge / dump_text.py
把论文 PDF 的正文文本导出到 data/text/<year>-<problem>-<id>.txt，供内容层抽取与摘录用。
已存在则跳过。用法：
  python dump_text.py --root <论文根目录> --outdir data/text --shards 5 --shard 0
"""
import argparse, os, re, sys

SKIP = re.compile(r"(?i)(com[-_][a-f]\b|judges?_?com|authors?_?com|expert_?com|umap|tips|_summary\.|problems?)")


def dump(path, dst):
    from pypdf import PdfReader
    r = PdfReader(path)
    parts = []
    for i, p in enumerate(r.pages, 1):
        try:
            t = p.extract_text() or ""
        except Exception:
            t = ""
        parts.append("\n\n===== PAGE %d =====\n%s" % (i, t))
    text = "".join(parts)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8", errors="ignore") as f:
        f.write(text)
    return len(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--shards", type=int, default=1)
    ap.add_argument("--shard", type=int, default=0)
    ap.add_argument("--min-year", type=int, default=0)
    a = ap.parse_args()

    jobs = []
    for year in sorted(os.listdir(a.root)):
        ydir = os.path.join(a.root, year)
        if not re.fullmatch(r"\d{4}", year) or not os.path.isdir(ydir):
            continue
        if int(year) < a.min_year:
            continue
        for prob in "ABCDEF":
            pdir = os.path.join(ydir, prob)
            if not os.path.isdir(pdir):
                continue
            for f in sorted(os.listdir(pdir)):
                if f.lower().endswith(".pdf") and not SKIP.search(f):
                    jobs.append((os.path.join(pdir, f), year, prob, f))
    if a.shards > 1:
        jobs = [j for i, j in enumerate(jobs) if i % a.shards == a.shard]

    done = skip = 0
    for path, year, prob, f in jobs:
        stem = os.path.splitext(f)[0]
        dst = os.path.join(a.outdir, "%s-%s-%s.txt" % (year, prob, stem))
        if os.path.exists(dst) and os.path.getsize(dst) > 2000:
            skip += 1
            continue
        try:
            n = dump(path, dst)
        except Exception as e:
            print("ERR %s %s" % (f, e), flush=True)
            continue
        done += 1
        if done % 10 == 0:
            print("[%d] %s-%s-%s chars=%d" % (done, year, prob, stem, n), flush=True)
    print("DONE done=%d skip=%d total=%d" % (done, skip, len(jobs)), flush=True)


if __name__ == "__main__":
    main()
