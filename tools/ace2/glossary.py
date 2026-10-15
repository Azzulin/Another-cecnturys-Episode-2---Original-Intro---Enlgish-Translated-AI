"""Merge the name research into work/glossary/names.json and fill the name tables from it.

  python tools/ace2/glossary.py            report only (coverage, conflicts, missing names)
  python tools/ace2/glossary.py --write    also writes names.json and _fill/{menu3014,hud3021,unit_names}.json

Sources, in priority order (BASE_RULES: one spelling for the whole series; the wiki wins):
  1. work/glossary/decisions.json   project-owner decisions (override everything)
  2. ACE3 0.9.3 researched glossary (character_names_021, unit_names_014_a/b) - keeps ACE2 consistent with ACE3
  3. work/glossary/research/*.json  ACE2 research (one file per franchise group, every entry with its source URL)
A name found in both 2 and 3 with different English is reported as a conflict (2 is used until a decision exists).
Name tables: menu3014 = full names (briefing speaker labels), hud3021 = short speaker labels, unit_names = lock-on.
"""
import argparse, json, sys, unicodedata
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT

GL = ROOT / 'work' / 'glossary'
EN = ROOT / 'work' / 'translation' / 'en'
ACE3 = Path(r'D:\Ace 1\ACE-3-0.9.3\ACE-3-0.9.3\work\glossary')
# ACE3 characters from series that are not in ACE2: their names (short ones above all, e.g. レイ = Ray of Eureka Seven)
# would collide with ACE2 text (アムロ・レイ, Layzner's computer レイ), so they never enter the ACE2 glossary.
NOT_IN_ACE2 = ('Eureka Seven', 'Gundam X', 'King Gainer', 'Getter Robo', 'Turn A', 'SEED', 'Macross Plus', 'Plamo-Kyoshiro',
               'ACE3 original')


def norm(s):
    return unicodedata.normalize('NFKC', s or '').replace('･', '・').replace(' ', '').replace('　', '')


def load_sources():
    entries = []   # (priority, source, entry with ja/ja_short/en/en_short/kind)
    decisions = GL / 'decisions.json'
    if decisions.exists():
        for e in json.loads(decisions.read_text(encoding='utf-8'))['entries']:
            entries.append((1, 'decision', e))
    for e in json.loads((ACE3 / 'character_names_021.json').read_text(encoding='utf-8'))['entries']:
        if any(x in (e.get('series') or '') for x in NOT_IN_ACE2):
            continue
        entries.append((2, 'ACE3 character_names_021', {'ja': e.get('ja_full'), 'ja_short': e.get('ja_short'), 'en': e.get('en_full'),
                                                        'en_short': e.get('en_short'), 'kind': 'character', 'sources': e.get('sources', [])}))
    for f in ('unit_names_014_a', 'unit_names_014_b'):
        for e in json.loads((ACE3 / (f + '.json')).read_text(encoding='utf-8'))['entries']:
            entries.append((2, 'ACE3 ' + f, {'ja': e.get('ja'), 'en': e.get('en'), 'kind': 'unit', 'sources': e.get('sources', [])}))
    for path in sorted((GL / 'research').glob('*.json')):
        for e in json.loads(path.read_text(encoding='utf-8'))['entries']:
            entries.append((3, path.name, e))
    return entries


def index(entries):
    """{normalized ja: (en, source)} for full names and {normalized ja_short: (en_short, source)}; plus conflicts."""
    full, short, conflicts = {}, {}, []
    for pri, src, e in sorted(entries, key=lambda x: x[0]):
        for key, en, table in ((norm(e.get('ja')), e.get('en'), full), (norm(e.get('ja_short')), e.get('en_short'), short)):
            if not key or not en:
                continue
            if key in table:
                if table[key][0] != en and table[key][2] != pri:
                    conflicts.append((key, table[key][0], table[key][1], en, src))
                continue
            table[key] = (en, src, pri)
    return full, short, conflicts


def fill_table(name, lookup, fallback=None):
    rows = json.loads((EN / (name + '.json')).read_text(encoding='utf-8'))['rows']
    fill, missing = {}, []
    for i, r in enumerate(rows):
        hit = lookup.get(norm(r['jp'])) or (fallback.get(norm(r['jp'])) if fallback else None)
        if hit:
            fill[str(i)] = hit[0]
        else:
            missing.append(r['jp'])
    return fill, missing, len(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()
    entries = load_sources()
    full, short, conflicts = index(entries)
    print('glossary: %d full names, %d short labels from %d entries' % (len(full), len(short), len(entries)))
    for key, a, sa, b, sb in conflicts:
        print('CONFLICT %s: %r (%s) vs %r (%s)' % (key, a, sa, b, sb))
    jobs = {'menu3014': (full, None), 'hud3021': (short, full), 'unit_names': (full, None)}
    for name, (lookup, fallback) in jobs.items():
        fill, missing, total = fill_table(name, lookup, fallback)
        print('%-10s %3d/%3d named; missing: %s' % (name, len(fill), total, ' | '.join(missing) or '-'))
        if args.write:
            (EN / '_fill' / (name + '.json')).write_text(json.dumps(fill, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if args.write:
        out = {'note': 'Generated by tools/ace2/glossary.py; edit the sources, not this file.',
               'full': {k: {'en': v[0], 'source': v[1]} for k, v in sorted(full.items())},
               'short': {k: {'en': v[0], 'source': v[1]} for k, v in sorted(short.items())},
               'conflicts': [{'ja': k, 'used': a, 'used_source': sa, 'other': b, 'other_source': sb} for k, a, sa, b, sb in conflicts]}
        (GL / 'names.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
