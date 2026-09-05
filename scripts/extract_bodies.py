#!/usr/bin/env python3
"""
Extract the body content from each standalone HTML lesson.
Strips the outer <div class="wrap"> wrapper (the layout provides it).
Saves to /workspace/extract-tmp/ for use in building Astro pages.
"""
import re
from pathlib import Path

SOURCES = {
    '01-syntax':              '/workspace/kotlin-syntax/index.html',
    '02-classes-null-safety': '/workspace/kotlin-classes-null-safety/index.html',
    '03-data-modeling':       '/workspace/kotlin-data-modeling/index.html',
    '04-scope-functions':     '/workspace/kotlin-scope-functions/index.html',
    '05-functional':          '/workspace/kotlin-functional/index.html',
}

OUT = Path('/workspace/extract-tmp')
OUT.mkdir(parents=True, exist_ok=True)

for slug, path in SOURCES.items():
    text = Path(path).read_text(encoding='utf-8')
    m = re.search(r'<body>(.*?)</body>', text, re.DOTALL)
    if not m:
        print(f'!! no body in {path}')
        continue
    body = m.group(1).strip()
    body = re.sub(r'^<div class="wrap">\s*', '', body, count=1)
    body = re.sub(r'\s*</div>\s*$', '', body, count=1)
    out_path = OUT / f'{slug}.body.html'
    out_path.write_text(body, encoding='utf-8')
    print(f'wrote {out_path} ({len(body):,} chars, {body.count(chr(10))} lines)')
