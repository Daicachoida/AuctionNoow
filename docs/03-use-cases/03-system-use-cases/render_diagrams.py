"""Render the System Use Case Mermaid sources as standalone SVG summaries.

The SVG uses the same actor-by-use-case matrix convention as the existing BUC
diagram. The Mermaid source remains the editable relationship model.
"""

from __future__ import annotations

import html
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCES = sorted(HERE.glob("system-use-case-*.mmd"))
ACTOR_RE = re.compile(r'^\s*(\w+)\["(.+)"\]\s*$')
CASE_RE = re.compile(r'^\s*(U\d{4}|G\d)\(\["(.+)"\]\)\s*$')
GROUP_RE = re.compile(r'^\s*subgraph\s+(\w+)\["(.+)"\]\s*$')
EDGE_RE = re.compile(r'^\s*(\w+)\s+---\s+(\w+)\s*$')


def esc(value: str) -> str:
    return html.escape(value.replace("<br/>", " / "), quote=False)


def parse(source: Path):
    actors: list[tuple[str, str]] = []
    cases: list[tuple[str, str, str]] = []
    edges: set[tuple[str, str]] = set()
    group = ""
    inside_system = False
    for line in source.read_text(encoding="utf-8").splitlines():
        if match := GROUP_RE.match(line):
            if match.group(1) == "AN":
                inside_system = True
            else:
                group = match.group(2)
            continue
        if match := CASE_RE.match(line):
            cases.append((match.group(1), match.group(2), group))
            continue
        if match := EDGE_RE.match(line):
            edges.add((match.group(1), match.group(2)))
            continue
        if not inside_system and (match := ACTOR_RE.match(line)):
            actors.append((match.group(1), match.group(2)))
    return actors, cases, edges


def render(source: Path) -> Path:
    actors, cases, edges = parse(source)
    actor_col = 137
    left = 45
    case_x = left + len(actors) * actor_col + 26
    width = case_x + 850
    y = 186
    group_height = 35
    row_height = 61
    positions: list[tuple[int, str, str, str]] = []
    group_positions: list[tuple[int, str]] = []
    last_group = None
    for case_id, label, group in cases:
        if group and group != last_group:
            group_positions.append((y, group))
            y += group_height
        positions.append((y, case_id, label, group))
        y += row_height
        last_group = group
    height = y + 65

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{esc(source.stem.replace("-", " "))}</title>',
        '<desc id="desc">Mỗi hàng là một use case; chấm tròn cho biết tác nhân tham gia. Nhãn A, B thể hiện tầng áp dụng.</desc>',
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
        f'<text x="{left}" y="60" font-family="Arial,sans-serif" font-size="30" font-weight="700" fill="#172b43">AuctionNoow · System Use Case</text>',
        f'<text x="{left}" y="92" font-family="Arial,sans-serif" font-size="17" fill="#526579">{esc(source.stem)} · {len(cases)} nhóm/use case</text>',
        f'<line x1="{left}" y1="112" x2="{width-left}" y2="112" stroke="#cbd5e1" stroke-width="2"/>',
        f'<text x="{left}" y="139" font-family="Arial,sans-serif" font-size="16" font-weight="700" fill="#334155">Tác nhân tham gia</text>',
        f'<text x="{case_x+12}" y="139" font-family="Arial,sans-serif" font-size="16" font-weight="700" fill="#334155">Use case trong hệ thống</text>',
    ]

    for index, (_, label) in enumerate(actors):
        x = left + index * actor_col + actor_col / 2
        words = label.replace(" · ", " / ").split()
        lines = []
        current = ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if len(candidate) > 16 and current:
                lines.append(current)
                current = word
            else:
                current = candidate
        if current:
            lines.append(current)
        for line_index, text in enumerate(lines[:2]):
            parts.append(f'<text x="{x:.0f}" y="{157+line_index*17}" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#334155">{esc(text)}</text>')
        parts.append(f'<line x1="{x:.0f}" y1="{184}" x2="{x:.0f}" y2="{height-52}" stroke="#e2e8f0"/>')

    for group_y, group in group_positions:
        parts.extend([
            f'<rect x="{left}" y="{group_y}" width="{width-2*left}" height="31" rx="6" fill="#e8eef6"/>',
            f'<text x="{left+12}" y="{group_y+21}" font-family="Arial,sans-serif" font-size="15" font-weight="700" fill="#27415c">{esc(group)}</text>',
        ])

    for row_y, case_id, label, _ in positions:
        center = row_y + 25
        tier = ""
        for suffix in (" · Ngoài MVP", " · A,B", " · A", " · B"):
            if label.endswith(suffix):
                tier = suffix[3:]
                label = label[: -len(suffix)]
                break
        color = "#eef2f7"
        border = "#9aa9b9"
        if tier == "A":
            color, border = "#e8f7ed", "#25a45a"
        elif tier == "B":
            color, border = "#e8f0ff", "#3b75d9"
        elif tier == "Ngoài MVP":
            color, border = "#f3f4f6", "#a5acb4"
        parts.extend([
            f'<line x1="{left}" y1="{row_y+52}" x2="{width-left}" y2="{row_y+52}" stroke="#e8edf2"/>',
            f'<rect x="{case_x}" y="{row_y+2}" width="810" height="45" rx="22" fill="{color}" stroke="{border}" stroke-width="1.5"/>',
            f'<text x="{case_x+17}" y="{center+5}" font-family="Arial,sans-serif" font-size="15" fill="#20354a">{esc(label)}</text>',
        ])
        if tier:
            parts.append(f'<text x="{case_x+790}" y="{center+5}" text-anchor="end" font-family="Arial,sans-serif" font-size="13" font-weight="700" fill="#415d78">{esc(tier)}</text>')
        for index, (actor_id, _) in enumerate(actors):
            if (actor_id, case_id) in edges:
                x = left + index * actor_col + actor_col / 2
                parts.append(f'<circle cx="{x:.0f}" cy="{center}" r="8" fill="#2482b9"/>')

    parts.append(f'<text x="{left}" y="{height-24}" font-family="Arial,sans-serif" font-size="14" fill="#526579">Chấm tròn = tác nhân tham gia · A = giao dịch ngoài nền tảng · B = thanh toán qua đối tác</text>')
    parts.append("</svg>")
    target = source.with_suffix(".svg")
    target.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return target


if __name__ == "__main__":
    for source in SOURCES:
        print(render(source).name)
