"""Fill the three content sections and paper palette of the locked Image2 prompt."""

import argparse
import json
import re
import sys
from pathlib import Path


TEMPLATE = Path(__file__).resolve().parents[1] / "references" / "image2-template.txt"
SLOTS = ("WHAT", "HOW_TO_MODEL", "HOW_TO_SOLVE")
PLACEHOLDER = re.compile(r"\{\{([A-Z_]+)\}\}")
HEX_COLOR = re.compile(r"#[0-9A-Fa-f]{6}")
LEGACY_PALETTE = """Use this fixed palette and keep each color's meaning consistent throughout:

- Deep navy #193B69: shared system and primary structure.
- Steel blue #537FA3: primary model and baseline processes.
- Teal #007E78: resource or material flow and supply.
- Muted amber #B56815: alternative pathways and optimization results.
- Muted coral #B95F5C: disruptions, failures, and risk.
- Desaturated green #60836A: environmental analysis and validation.
- Light gray #E9EDF2: secondary information and assumptions."""


def format_palette(palette):
    if not isinstance(palette, dict) or not palette:
        raise ValueError("PALETTE must be a nonempty mapping of English color roles to #RRGGBB values")
    lines = ["Use the confirmed paper-wide palette and keep each color's meaning consistent throughout:", ""]
    for role, color in palette.items():
        if not isinstance(role, str) or not role.strip() or role.splitlines() != [role] or PLACEHOLDER.search(role):
            raise ValueError("Each PALETTE role must be a single line of text with no unresolved placeholders")
        if not isinstance(color, str) or not HEX_COLOR.fullmatch(color):
            raise ValueError(f"PALETTE color for {role!r} must use #RRGGBB format")
        lines.append(f"- {color.upper()}: {role.strip()}")
    return "\n".join(lines)


def render_prompt(content):
    required = set(SLOTS)
    if not isinstance(content, dict) or set(content) not in (required, required | {"PALETTE"}):
        raise ValueError(f"Content must have {', '.join(SLOTS)} and may include PALETTE")
    for slot in SLOTS:
        value = content[slot]
        if not isinstance(value, str) or not value.strip() or PLACEHOLDER.search(value):
            raise ValueError(f"{slot} must contain English text with no unresolved placeholders")
    palette = format_palette(content["PALETTE"]) if "PALETTE" in content else LEGACY_PALETTE
    replacements = {slot: content[slot].strip() for slot in SLOTS}
    replacements["PALETTE"] = palette
    template = TEMPLATE.read_text(encoding="utf-8")
    if tuple(PLACEHOLDER.findall(template)) != (*SLOTS, "PALETTE"):
        raise ValueError("The template must contain the three content placeholders and PALETTE once, in order")
    return PLACEHOLDER.sub(lambda match: replacements[match[1]], template)


def apply_edits(content, changes):
    if not isinstance(changes, list) or not changes:
        raise ValueError("Patch must be a nonempty list of individual line edits")

    revised = content.copy()
    for index, change in enumerate(changes, start=1):
        if not isinstance(change, dict) or set(change) != {"field", "before", "after"}:
            raise ValueError(f"Edit {index} must have field, before, and after")
        field = change["field"]
        before = change["before"]
        after = change["after"]
        if field not in SLOTS or not all(isinstance(value, str) and value.strip() for value in (before, after)):
            raise ValueError(f"Edit {index} must name one content field and provide nonblank text")
        if before.splitlines() != [before]:
            raise ValueError(f"Edit {index} must identify exactly one original line")
        lines = revised[field].splitlines(keepends=True)
        matches = [
            position for position, line in enumerate(lines) if line.rstrip("\r\n") == before
        ]
        if len(matches) != 1:
            raise ValueError(f"Edit {index} must match exactly one line in {field}")
        position = matches[0]
        ending = lines[position][len(before):]
        lines[position] = after.rstrip("\r\n") + ending
        revised[field] = "".join(lines)
    return revised


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("content", type=Path, help="UTF-8 JSON containing the three content fields and the paper palette")
    parser.add_argument("--patch", type=Path, help="JSON list of targeted edits to the original content")
    parser.add_argument("--save-content", type=Path, help="New JSON file for the revised content")
    args = parser.parse_args()
    if bool(args.patch) != bool(args.save_content):
        parser.error("--patch and --save-content must be provided together")
    try:
        content = json.loads(args.content.read_text(encoding="utf-8-sig"))
        prompt = render_prompt(content)
        if args.patch:
            changes = json.loads(args.patch.read_text(encoding="utf-8-sig"))
            revised = apply_edits(content, changes)
            prompt = render_prompt(revised)
            output = json.dumps(revised, ensure_ascii=False, indent=2) + "\n"
            with args.save_content.open("x", encoding="utf-8", newline="\n") as file:
                file.write(output)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{parser.prog}: {error}\n")
    sys.stdout.buffer.write(prompt.encode("utf-8"))


if __name__ == "__main__":
    main()
