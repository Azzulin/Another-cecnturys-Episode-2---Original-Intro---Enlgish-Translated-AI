"""Map every story operation to all of its text: work/translation/operations.json.

  python tools/ace2/operations.py

An operation is never only its mission dialogue. Layers (resource numbering checked against the content):
  strategic   brief(63000 + op - 1)            operation briefing; row 1 = 'オペレーション NN'
  tactical    brief(63028 + (op-1)*5 + p - 1)  one per phase, shown before each phase (objective + dialogue)
  missions    m(6000 + op*10 + p)              in-mission dialogue (container 6### and its twin 42###)
  debrief     brief(63167 + op)                talk after the operation
  reports     brief(63196 + (op-1)*4 + k)      Preventer reports unlocked by the operation (k = 0..3)
Tables that belong to no operation (names, HUD, menus, other missions) are listed under "shared".
"""
import json, re, sys, unicodedata
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT

EN = ROOT / 'work' / 'translation' / 'en'
OUT = ROOT / 'work' / 'translation' / 'operations.json'
OPS = 28


def main():
    tables = {p.stem: json.loads(p.read_text(encoding='utf-8')) for p in EN.glob('*.json')}
    used, ops, problems = set(), [], []
    for op in range(1, OPS + 1):
        entry = {'op': op, 'strategic': None, 'tactical': [], 'missions': [], 'debrief': None, 'reports': []}
        s = 'brief%d' % (63000 + op - 1)
        head = unicodedata.normalize('NFKC', tables[s]['rows'][0]['jp']) if s in tables else ''
        if re.fullmatch(r'オペレーション\s*%02d' % op, head):
            entry['strategic'] = s
        else:
            problems.append('op %d: strategic %s header %r' % (op, s, head))
        for p in range(1, 6):
            t = 'brief%d' % (63028 + (op - 1) * 5 + p - 1)
            if t in tables:
                entry['tactical'].append(t)
            m = 'm%d' % (6000 + op * 10 + p)
            if m in tables:
                entry['missions'].append(m)
        d = 'brief%d' % (63167 + op)
        if d in tables and op < OPS:
            entry['debrief'] = d
        for k in range(4):
            r = 'brief%d' % (63196 + (op - 1) * 4 + k)
            if r in tables:
                entry['reports'].append(r)
        names = [entry['strategic'], entry['debrief']] + entry['tactical'] + entry['missions'] + entry['reports']
        entry['rows'] = sum(len(tables[n]['rows']) for n in names if n)
        used.update(n for n in names if n)
        ops.append(entry)
    shared = sorted(set(tables) - used)
    OUT.write_text(json.dumps({'operations': ops, 'shared': shared}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for e in ops:
        print('Op %02d  strategic %-10s tactical %-40s missions %-28s debrief %-10s reports %s  (%d rows)' % (
            e['op'], e['strategic'], ','.join(t[5:] for t in e['tactical']), ','.join(m[1:] for m in e['missions']),
            e['debrief'], ','.join(r[5:] for r in e['reports']), e['rows']))
    print('shared tables:', len(shared), ' '.join(shared))
    for p in problems:
        print('PROBLEM', p)


if __name__ == '__main__':
    main()
