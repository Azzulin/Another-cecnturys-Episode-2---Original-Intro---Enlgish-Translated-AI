"""Export the Japanese text of the base disc to work/translation/en/<table>.json (one row per distinct source).

  python tools/ace2/export_text.py

Every text table is discovered automatically (see textdb.py) and grouped into logical tables:
  m####        mission dialogue (container 6### and its twin 42###, whose rows are identical)
  unit_names   enemy names shown on the lock-on HUD (one-row sub-tables of every mission container)
  brief#####   briefing tables 63###
  menu####     menu tables (inner id) in the menu bundles 62050-62057
  hud####      gameplay tables (inner id) in the gameplay bundles 38000-38006
  common       system windows 8031 (+ copies 8033, 60000)
  partnerNNN   battle chatter of partner NNN (chunk PMS of model package 2NNN and its packed copy 36300+NNN)
  partner_names  partner pilot names (chunks PPN1/PPN2 of the same packages)
  r...         anything else, named after its location
Only rows that contain Japanese or fullwidth letters are exported; the rest (numbers, '%d', '---') stay as they are.
Existing "en" values are kept, so the export can be re-run safely. work/translation/inventory.json gets the counts;
work/translation/partners.json says who speaks each partnerNNN table (pilot and unit, in Japanese).
"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT, BASE, Disc, TextTable, vmd_chunks
from textdb import discover, group, JPC

OUT = ROOT / 'work' / 'translation' / 'en'
INVENTORY = ROOT / 'work' / 'translation' / 'inventory.json'
PARTNERS = ROOT / 'work' / 'translation' / 'partners.json'
FULLWIDTH = re.compile(r'[Ａ-Ｚａ-ｚ]')


def kind(name):
    if name == 'partner_names':
        return 'unit_names'
    for prefix in ('unit_names', 'brief', 'menu', 'hud', 'common'):
        if name.startswith(prefix):
            return prefix
    # partnerNNN: the partner's battle chatter, shown in the mission dialogue window
    return 'mission' if re.fullmatch(r'm\d{4}|partner\d{3}', name) else 'other'


def partners(disc):
    """{partnerNNN: {'pilot': [names], 'unit': name}} from the PPN1/PPN2 and FNM chunks of each partner package, so the
    translator knows who speaks each line of partnerNNN."""
    out = {}
    for rid in range(2000, 2300):
        chunks = vmd_chunks(disc.get(rid)) if rid in disc.index.by_id else None
        if not chunks:
            continue
        data = disc.get(rid)
        found = {m: TextTable(data[a + 16:a + s]) for a, m, s in chunks if m in (b'PMS\0', b'PPN1', b'PPN2', b'FNM\0')}
        if b'PMS\0' in found:
            out['partner%03d' % (rid - 2000)] = {
                'pilot': [t.rows[min(t.rows)] for m, t in sorted(found.items()) if m.startswith(b'PPN') and t.rows],
                'unit': next(iter(found[b'FNM\0'].rows.values()), '') if b'FNM\0' in found else ''}
    return out


def wanted(text):
    return bool(JPC.search(text) or FULLWIDTH.search(text))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    disc = Disc(BASE)
    groups = group(discover(disc))
    inventory = {'tables': {}, 'totals': {}}
    for name, members in sorted(groups.items()):
        rows = {}
        for loc, t in members:
            for tid, jp in t.rows.items():
                if wanted(jp):
                    rows.setdefault(jp, set()).add(tid)
        if not rows:
            continue
        path = OUT / (name + '.json')
        old = {}
        if path.exists():
            old = {r['jp']: r.get('en', '') for r in json.loads(path.read_text(encoding='utf-8'))['rows']}
        doc = {'table': name, 'kind': kind(name), 'copies': sorted({loc for loc, _ in members}),
               'rows': [{'ids': sorted(ids), 'jp': jp, 'en': old.get(jp, '')}
                        for jp, ids in sorted(rows.items(), key=lambda kv: (min(kv[1]), kv[0]))]}
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        done = sum(1 for r in doc['rows'] if r['en'])
        inventory['tables'][name] = {'kind': doc['kind'], 'rows': len(doc['rows']), 'chars': sum(len(r['jp']) for r in doc['rows']),
                                     'translated': done, 'copies': len(doc['copies'])}
    for t in inventory['tables'].values():
        k = inventory['totals'].setdefault(t['kind'], {'tables': 0, 'rows': 0, 'chars': 0, 'translated': 0})
        k['tables'] += 1; k['rows'] += t['rows']; k['chars'] += t['chars']; k['translated'] += t['translated']
    INVENTORY.write_text(json.dumps(inventory, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    PARTNERS.write_text(json.dumps(partners(disc), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for k, v in sorted(inventory['totals'].items()):
        print('%-11s tables=%4d rows=%6d chars=%7d translated=%d' % (k, v['tables'], v['rows'], v['chars'], v['translated']))
    print('files ->', OUT)


if __name__ == '__main__':
    main()
