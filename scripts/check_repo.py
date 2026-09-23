#!/usr/bin/env python3
"""Offline repository hygiene checks; Python standard library only."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def fail(message):
    errors.append(message)

raw = subprocess.check_output(
    ['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=ROOT)
paths = sorted({p.decode() for p in raw.split(b'\0') if p})
paths = [p for p in paths if (ROOT / p).is_file()]
for rel in paths:
    p = ROOT / rel
    if p.name in {'.DS_Store', '.gitkeep', '.env'} or p.suffix in {'.patch', '.pyc', '.tmp', '.swp'}:
        fail(f'Unwanted repository file: {rel}')
    if p.suffix == '.md':
        text = p.read_text()
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)\)', text):
            if re.match(r'^[a-zA-Z][\w+.-]*:', target) or target.startswith('#'):
                continue
            target = target.split('#')[0]
            if target and not (p.parent / target).exists():
                fail(f'Broken relative link in {rel}: {target}')

bib = (ROOT / 'literature/references.bib').read_text()
keys = re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,', bib)
if len(keys) != len(set(keys)):
    fail('Duplicate BibTeX keys')
if re.search(r'^\s*file\s*=', bib, re.M) or '/Users/' in bib:
    fail('Machine-local attachment paths in bibliography')
# Balanced BibTeX braces (escaped literal braces do not delimit groups).
depth = 0
for c in re.sub(r'\\[{}]', '', bib):
    depth += (c == '{') - (c == '}')
    if depth < 0:
        fail('Unbalanced BibTeX braces')
        break
if depth:
    fail('Unbalanced BibTeX braces')
index = (ROOT / 'literature/references.md').read_text()
index_keys = set(re.findall(r'^\| `([^`]+)` \|', index, re.M))
if index_keys != set(keys):
    fail(f'Index/BibTeX mismatch: {sorted(index_keys.symmetric_difference(keys))}')
index_ids = set(re.findall(r'https://arxiv.org/abs/(\d{4}\.\d{4,5})', index))
bib_ids = re.findall(r'eprint\s*=\s*\{([^}]+)\}', bib)
if len(bib_ids) != len(set(bib_ids)) or set(bib_ids) != index_ids:
    fail('Duplicate or mismatched arXiv identifiers')
for rel in ['README.md', 'STATUS.md', 'AGENTS.md', 'proposal/research-design.md', 'literature/positioning-note.md']:
    if re.search(r'supervisor (?:agreement|approval) (?:remains |is )?pending|pending supervisor', (ROOT / rel).read_text(), re.I):
        fail(f'Stale supervisor approval status: {rel}')
if errors:
    print('\n'.join('ERROR: ' + e for e in errors))
    sys.exit(1)
print(f'OK: {len(paths)} repository files; {len(keys)} bibliography records; links and hygiene checked.')
print('This does not verify scientific claims, remote URLs, data licenses or Zotero synchronization.')
