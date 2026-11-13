"""Verify preserved source bytes and generated navigation, using only stdlib."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads(
        (ROOT / 'docs/migration-manifest.json').read_text(encoding='utf-8')
    )
    records = manifest['records']
    failures = []
    destinations = set()
    origins = set()
    for row in records:
        key = (row['branch'], row['source'])
        if key in origins:
            failures.append('Duplicate source: ' + str(key))
        origins.add(key)
        path = ROOT / row['destination']
        try:
            path.resolve().relative_to(ROOT.resolve())
        except ValueError:
            failures.append('Unsafe destination: ' + row['destination'])
            continue
        if not path.is_file():
            failures.append('Missing: ' + row['destination'])
            continue
        data = path.read_bytes()
        sha256 = hashlib.sha256(data).hexdigest()
        blob = hashlib.sha1(
            b'blob ' + str(len(data)).encode('ascii') + b'\0' + data
        ).hexdigest()
        if (sha256 != row['sha256'] or blob != row['git_blob_sha1']
                or len(data) != row['size']):
            failures.append('Changed: ' + row['destination'])
        destinations.add(row['destination'])

    # Original documents retain their historical links; check only new guides.
    original_paths = {row['destination'] for row in records}
    guides = [p for p in ROOT.rglob('*.md')
              if '.git' not in p.parts
              and p.relative_to(ROOT).as_posix() not in original_paths]
    links = 0
    for path in guides:
        text = path.read_text(encoding='utf-8')
        for url in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'^[a-zA-Z]+:', url) or url.startswith('#'):
                continue
            target = unquote(url.split('#', 1)[0])
            links += 1
            if not (path.parent / target).exists():
                failures.append('Broken link: ' + str(path) + ' -> ' + url)

    print('Branches:', len({row['branch'] for row in records}))
    print('Source records:', len(records))
    print('Unique preserved files:', len(destinations))
    print('Consolidated duplicates:', len(records) - len(destinations))
    print('Generated Markdown documents:', len(guides))
    print('Checked local links:', links)
    for failure in failures:
        print('FAIL:', failure)
    print('PASS' if not failures else 'FAILED')
    return int(bool(failures))


if __name__ == '__main__':
    sys.exit(main())
