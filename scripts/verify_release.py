"""Verify release files without reading local input directories."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {'.git', '.venv', '__pycache__', '.pytest_cache', 'inputs', 'local_data', 'outputs'}

def main():
    expected = json.loads((ROOT/'MANIFEST_SHA256.json').read_text())
    actual = {}
    for path in ROOT.rglob('*'):
        rel = path.relative_to(ROOT)
        if any(part in SKIP for part in rel.parts):
            continue
        assert not path.is_symlink(), f'Symlink not allowed: {rel}'
        if not path.is_file() or str(rel) == 'MANIFEST_SHA256.json':
            continue
        actual[str(rel)] = hashlib.sha256(path.read_bytes()).hexdigest()
    assert actual == expected, 'Release files differ from manifest'
    print(json.dumps({'status': 'PASS', 'manifest_files': len(expected)}))

if __name__ == '__main__':
    main()
