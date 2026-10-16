"""Check the publication snapshot and usable RFCXML contribution structure."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

folder = Path(__file__).resolve().parent
name = 'draft-li-pearg-fhe-use-cases'
record = json.loads((folder / 'source-verification.json').read_text(encoding='utf-8'))
snapshot = folder / (name + '-00.xml')
assert hashlib.sha256(snapshot.read_bytes()).hexdigest() == record['source_sha256']
assert record['source_sha256'] == record['ietf_published_sha256']
assert record['byte_identical_to_published_xml'] is True
assert ET.parse(snapshot).getroot().get('docName') == name + '-00'

fragment = ET.parse(folder / 'templates/use-case-template.xml').getroot()
assert fragment.tag == 'section'
assert fragment.findtext('name').startswith('UCx:')
fragment_text = ' '.join(fragment.itertext())
for heading in ['Scenario:', '(1) Example Flows:', '(2) Post-conditions:',
                '(3) Existing Non-HE Solutions Covering the Use-Case Functionality:',
                '(4) Potential New Requirements Needed to Support the Use Case:']:
    assert heading in fragment_text, heading

editor = folder.parent / (name + '.xml')
if editor.exists():
    root = ET.parse(editor).getroot()
    assert root.get('docName') == name + '-latest'
    assert root.find('front/seriesInfo').get('value') == name + '-latest'
    assert root.findtext('front/title') == ET.parse(snapshot).findtext('front/title')
    targets = {element.get('anchor') for element in root.iter() if element.get('anchor')}
    missing = sorted({element.get('target') for element in root.iter('xref')} - targets)
    assert not missing, missing
    assert root.find('.//section[@anchor="uc-details"]') is not None

print('PASS: published XML hash, RFCXML template structure, and editor metadata/references')
