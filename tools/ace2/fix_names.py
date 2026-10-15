"""Apply name/term fixes from work/glossary/name_fixes.json to every English text (fills and merged tables).

  python tools/ace2/fix_names.py            dry run: prints every change it would make
  python tools/ace2/fix_names.py --write    applies them

BASE_RULES: names are fixed by script, after agent fixes, and a fixed name goes on the agents' do-not-touch list.
Each rule is a literal replacement ('from') or a regular expression ('regex'), case-sensitive, with an optional "only_if_jp" substring that the Japanese
source must contain, so a generic word is not rewritten in unrelated rows.
"""
import argparse, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT

EN = ROOT / 'work' / 'translation' / 'en'
RULES = ROOT / 'work' / 'glossary' / 'name_fixes.json'


def apply(text, jp, rules):
    for r in rules:
        if r.get('only_if_jp') and r['only_if_jp'] not in jp:
            continue
        text = re.sub(r['regex'], r['to'], text) if 'regex' in r else text.replace(r['from'], r['to'])
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()
    rules = json.loads(RULES.read_text(encoding='utf-8'))['rules']
    changes = 0
    for table_path in sorted(EN.glob('*.json')):
        doc = json.loads(table_path.read_text(encoding='utf-8'))
        fill_path = EN / '_fill' / table_path.name
        fill = json.loads(fill_path.read_text(encoding='utf-8')) if fill_path.exists() else None
        dirty_doc = dirty_fill = False
        for i, row in enumerate(doc['rows']):
            for source, key in ((row, 'en'), (fill, str(i))):
                if source is None or not source.get(key):
                    continue
                new = apply(source[key], row['jp'], rules)
                if new != source[key]:
                    print('%s[%d]%s\n   - %r\n   + %r' % (doc['table'], i, ' (fill)' if source is fill else '', source[key], new))
                    source[key] = new; changes += 1
                    dirty_fill |= source is fill; dirty_doc |= source is row
        if args.write and dirty_doc:
            table_path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        if args.write and dirty_fill:
            fill_path.write_text(json.dumps(fill, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%d changes%s' % (changes, '' if args.write else ' (dry run)'))


if __name__ == '__main__':
    main()
