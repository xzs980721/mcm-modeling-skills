"""Compare the main sections of a Typst or XeLaTeX paper with its template."""

import argparse
import os
from pathlib import Path
import re
import sys


TYPST_EVENTS = re.compile(
    r'#include(?:\s+|\s*\(\s*)"(?P<input>[^"\r\n]+)"'
    r'|^[ \t]*=[ \t]+(?P<title>[^\r\n]+)'
    r'|#heading(?:\s*\[|\(\s*level:\s*1\s*(?=[,)]))',
    re.MULTILINE,
)
LATEX_EVENTS = re.compile(
    r"\\(?:input|include)\s*\{(?P<input>[^}]+)\}"
    r"|\\section(?P<star>\*)?\s*(?:\[(?P<short>[^\]]*)\]\s*)?\{(?P<title>[^}]*)\}"
    r"|(?P<appendix>\\appendix\b)",
)


def source_events(path, is_typst):
    source = path.read_text(encoding="utf-8-sig")
    if is_typst:
        source = re.sub(r"(?ms)^[ \t]*\x60{3,}[^\n]*\n.*?^[ \t]*\x60{3,}[ \t]*$", "", source)
        source = re.sub(r"(?s)/\*.*?\*/", "", source)
        source = re.sub(r"(?m)^[ \t]*//[^\n]*", "", source)
        return TYPST_EVENTS.finditer(source)

    source = re.sub(r"(?m)(?<!\\)%[^\n]*", "", source)
    source = re.sub(r"(?s)\\begin\{(verbatim\*?|lstlisting|minted)\}.*?\\end\{\1\}", "", source)
    return LATEX_EVENTS.finditer(source)


def included_file(base, name, is_typst):
    name = name.strip()
    if not is_typst and not name.endswith(".tex"):
        name += ".tex"
    return (base / name).resolve()


def direct_inputs(main, is_typst):
    return [
        included_file(main.parent, match["input"], is_typst)
        for match in source_events(main, is_typst)
        if match["input"] is not None
    ]


def expanded_events(path, main_dir, is_typst, parents=()):
    if path in parents:
        raise ValueError(f"circular input: {path}")
    for match in source_events(path, is_typst):
        if match["input"] is None:
            yield path, match.groupdict()
        else:
            base = path.parent if is_typst else main_dir
            target = included_file(base, match["input"], is_typst)
            yield from expanded_events(target, main_dir, is_typst, (*parents, path))


def outline(main, core_files, is_typst):
    headings = []
    in_appendix = False
    for path, event in expanded_events(main, main.parent, is_typst):
        if event.get("appendix"):
            in_appendix = True
            continue
        relative = Path(os.path.relpath(path, main.parent)).as_posix()
        if relative not in core_files and (in_appendix or event.get("star")):
            continue
        if in_appendix and relative in core_files:
            raise ValueError(f"main chapter is inside the appendix: {relative}")
        raw_title = event["title"] if event["title"] is not None else "#heading(level: 1, ...)"
        title = " ".join(raw_title.split())
        short_title = event.get("short")
        if short_title is not None and " ".join(short_title.split()) != title:
            title += f" [contents: {short_title}]"
        if event.get("star"):
            title += " [unnumbered]"
        headings.append((relative, title))
    return headings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper_main", type=Path)
    parser.add_argument("template_main", type=Path)
    args = parser.parse_args()
    paper = args.paper_main.resolve()
    template = args.template_main.resolve()
    if template.suffix not in {".typ", ".tex"} or paper.suffix != template.suffix:
        parser.error("paper and template must use the same .typ or .tex format")
    is_typst = template.suffix == ".typ"

    try:
        template_inputs = direct_inputs(template, is_typst)
        core_files = [
            path.relative_to(template.parent).as_posix()
            for path in template_inputs
            if path.parent == template.parent / "sections" and re.match(r"^\d+_", path.name)
        ]
        if len(core_files) != 7 or len(set(core_files)) != 7:
            raise ValueError("template must include its seven distinct main chapters")

        expected = outline(template, core_files, is_typst)
        if [path for path, _ in expected] != core_files:
            raise ValueError("template must have exactly one level-1 heading per main chapter")

        paper_inputs = direct_inputs(paper, is_typst)
        paper_core = [paper.parent / path for path in core_files]
        if [path for path in paper_inputs if path in paper_core] != paper_core:
            raise ValueError("main entry must include all seven template chapter files once and in order")

        actual = outline(paper, core_files, is_typst)
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    if actual != expected:
        print("FAIL: level-1 headings differ from the template", file=sys.stderr)
        for label, entries in (("Expected", expected), ("Found", actual)):
            print(f"{label}:", file=sys.stderr)
            for path, title in entries:
                print(f"  {path}: {title}", file=sys.stderr)
        return 1

    print("PASS: main chapter paths, titles, and order match the template")
    return 0


if __name__ == "__main__":
    sys.exit(main())
