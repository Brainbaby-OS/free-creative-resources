"""Verify original resource bytes and the public example without external calls."""
from pathlib import Path
import csv
import hashlib
import json
import re
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree
import zipfile

root = Path(__file__).resolve().parents[1]
seen = set()
for manifest in ['resource-manifest.json', 'presentation-example-manifest.json']:
    for item in json.loads((root / manifest).read_text())['files']:
        path = (root / item['path']).resolve()
        assert path.is_relative_to(root) and path.is_file(), item['path']
        assert item['path'] not in seen, item['path']
        seen.add(item['path'])
        data = path.read_bytes()
        assert len(data) == item['bytes'], item['path']
        assert hashlib.sha256(data).hexdigest() == item['sha256'], item['path']

for file in root.rglob('*.md'):
    if '.git' in file.parts:
        continue
    for href in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', file.read_text()):
        target = urlsplit(href)
        if target.scheme or target.netloc or not target.path or target.path.startswith('/'):
            continue
        path = (file.parent / unquote(target.path)).resolve()
        assert path.is_relative_to(root) and path.exists(), (str(file.relative_to(root)), href)

with (root / 'resources/en/presentation-tool-scorecard.csv').open(newline='') as file:
    rows = list(csv.reader(file))
assert len(rows) == 4 and len(rows[0]) == 20
assert all(len(row) == 20 and all(not cell for cell in row) for row in rows[1:])

with (root / 'resources/tr/mobil-uygulama-ekran-plani.csv').open(newline='') as file:
    mobile_rows = list(csv.reader(file))
assert len(mobile_rows) == 13 and all(len(row) == 8 for row in mobile_rows)
assert all(not any(row[4:]) for row in mobile_rows[1:]), 'Mobile result fields must stay blank'
mobile_svg = ElementTree.fromstring((root / 'resources/tr/mobil-uygulama-tasarimi.svg').read_bytes())
assert mobile_svg.attrib.get('viewBox') == '0 0 1200 740'
assert not any(node.tag.rsplit('}', 1)[-1] in {'script', 'foreignObject'} for node in mobile_svg.iter())

folder = root / 'examples/presentations/community-garden'
pdf = (folder / 'community-garden.pdf').read_bytes()
assert pdf.startswith(b'%PDF-') and b'%%EOF' in pdf[-1024:]
with zipfile.ZipFile(folder / 'community-garden.pptx') as file:
    assert not any('vba' in name.lower() for name in file.namelist())
    slides = [name for name in file.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', name)]
    assert len(slides) == 4
    for name in slides:
        slide = ElementTree.fromstring(file.read(name))
        assert slide.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/main}t'), name
    for name in file.namelist():
        if name.endswith('.rels'):
            assert b'TargetMode="External"' not in file.read(name), name

print(f'Verified {len(seen)} manifest files, local Markdown links, a blank scorecard and the four-slide PDF/PPTX sample. No AI or payment requests were made.')
