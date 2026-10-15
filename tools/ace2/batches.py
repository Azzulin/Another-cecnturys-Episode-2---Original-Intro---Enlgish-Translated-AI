"""Work package for the external translator agent (same procedure as ACE1): work/translation/agent/.

  python tools/ace2/batches.py make [--ops 2-28] [--force]   write agent/batches/opNN_KK.json (+ examples/op01.json)
  python tools/ace2/batches.py status                         per batch: returned? validated? applied?
  python tools/ace2/batches.py hand op03_01                   record a batch as given to the agent

An operation is frozen as soon as one of its batches is handed (agent/handed.json) or returned: make never rewrites
its batches or auto rows again (without --force), because batch boundaries move when the translation memory grows.

The agent only translates: it copies batches/<LOTE>.json to returns/<LOTE>.json and fills "en", "notes" and "report".
It never runs tools, never touches the game, the tables, the fills or the docs. Validation and application are done
here by tools/ace2/validate_return.py (report in agent/validation/<LOTE>.md); review aid: tools/ace2/review_returns.py.

BASE_RULES: one batch = 80 consecutive rows of one operation, in play order (strategic briefing, then for each phase
the tactical briefing and the mission, then the debriefing and the Preventer reports). Every batch carries the rows
around it as read-only context and the glossary entries whose Japanese occurs in it (names.json wins; gender, role and
personality come from work/glossary/research). Rows whose Japanese is already translated elsewhere (exact same
string, tags included) are not sent ("tm"), and a row repeated inside the pending corpus is translated once ("repeat");
both are listed in work/translation/auto/opNN.json and filled by validate_return.py --apply.
"""
import argparse, datetime, json, re, sys, unicodedata
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT
from textdb import TOKEN

TR = ROOT / 'work' / 'translation'
EN = TR / 'en'
AGENT = TR / 'agent'
AUTO = TR / 'auto'
GL = ROOT / 'work' / 'glossary'
SIZE, CONTEXT = 80, 12
BRIEF_BASE, MISSION_BASE = 63028, 6000
KATAKANA_NAME = re.compile(r'[ァ-ヺー]+(?:[・･][ァ-ヺー]+)+')
PORTRAIT = re.compile(r'<op\((\d+),')
NAME_KINDS = {'character', 'unit', 'ship', 'place', 'faction'}


def norm(s):
    return unicodedata.normalize('NFKC', s or '').replace('･', '・').replace(' ', '').replace('　', '')


def table(name, cache={}):
    if name not in cache:
        cache[name] = json.loads((EN / (name + '.json')).read_text(encoding='utf-8'))
    return cache[name]


def fill_of(name):
    p = EN / '_fill' / (name + '.json')
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}


def parse_ops(text, last=28):
    if not text:
        return list(range(2, last + 1))
    out = []
    for part in text.split(','):
        a, _, b = part.partition('-')
        out += range(int(a), int(b or a) + 1)
    return out


def sequence(op):
    """[(table, layer, phase)] in play order."""
    e = json.loads((TR / 'operations.json').read_text(encoding='utf-8'))['operations'][op - 1]
    seq = [(e['strategic'], 'strategic briefing', None)]
    phases = {}
    for t in e['tactical']:
        phases.setdefault(int(t[5:]) - (BRIEF_BASE + (op - 1) * 5) + 1, []).append((t, 'tactical briefing'))
    for m in e['missions']:
        phases.setdefault(int(m[1:]) - MISSION_BASE - op * 10, []).append((m, 'mission dialogue'))
    for p in sorted(phases):
        seq += [(t, layer, p) for t, layer in phases[p]]
    if e['debrief']:
        seq.append((e['debrief'], 'debriefing', None))
    seq += [(r, 'Preventer report', None) for r in e['reports']]
    return [s for s in seq if s[0]]


def glossary():
    """{normalized ja: entry}: terms.json first (Op 01 usage), then names.json with details from research."""
    names = json.loads((GL / 'names.json').read_text(encoding='utf-8'))
    detail = {}
    for path in sorted((GL / 'research').glob('*.json')):
        for e in json.loads(path.read_text(encoding='utf-8'))['entries']:
            for k in (norm(e.get('ja')), norm(e.get('ja_short'))):
                if k:
                    detail.setdefault(k, e)
    out = {}
    for t in json.loads((GL / 'terms.json').read_text(encoding='utf-8'))['terms']:
        out[norm(t['ja'])] = dict(t, ja=norm(t['ja']))
    for part in ('full', 'short'):
        for k, v in names[part].items():
            if len(k) < 2:
                continue
            d = detail.get(k, {})
            entry = {'ja': k, 'en': v['en']}
            for f in ('kind', 'series', 'gender', 'role', 'personality'):
                if d.get(f):
                    entry[f] = d[f]
            if d and part == 'full' and d.get('en_short'):
                entry['en_short'] = d['en_short']
            if d and part == 'short' and d.get('en'):
                entry['full_name'] = d['en']
            out.setdefault(k, entry)
    return out


def translated_memory():
    """{jp: en} from every translated row (merged tables and fill files)."""
    tm = {}
    for p in EN.glob('*.json'):
        doc = json.loads(p.read_text(encoding='utf-8'))
        fill = fill_of(p.stem)
        for i, r in enumerate(doc['rows']):
            en = fill.get(str(i)) or r.get('en')
            if en:
                tm.setdefault(r['jp'], en)
    return tm


def font_hint():
    """Average px per character of English already in the game (Op 01), per font: turns px limits into a char guide."""
    from merge_fill import load_fonts, widths, FONT_OF_KIND, limit_for
    fonts = load_fonts()
    avg = {}
    for font in ('game', 'menu'):
        px = chars = 0
        for name in ('m6011', 'm6012') if font == 'game' else ('brief63000', 'brief63028', 'brief63029', 'brief63168'):
            for r in table(name)['rows']:
                if r.get('en'):
                    for line in re.sub(TOKEN, '', r['en']).split('\n'):
                        if line.strip():
                            px += max(widths(fonts[font], line)); chars += len(line)
        avg[font] = px / chars
    return avg, fonts, widths, FONT_OF_KIND, limit_for


def example_op01():
    """Operation 01 as translated and tested in 0.0.2: the reference for tone, layout and tag handling."""
    rows = []
    for name, layer, phase in sequence(1):
        for i, r in enumerate(table(name)['rows']):
            en = fill_of(name).get(str(i)) or r.get('en')
            if en:
                rows.append({'ref': '%s#%d' % (name, i), 'layer': layer, 'phase': phase, 'jp': r['jp'], 'en': en})
    (AGENT / 'examples').mkdir(parents=True, exist_ok=True)
    (AGENT / 'examples' / 'op01.json').write_text(json.dumps({
        'note': 'Operation 01, translated and checked in game (build 0.0.2). Read it for tone and tag handling; '
                'do not copy its lines into other rows.', 'rows': rows}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def line_caps():
    """Most lines the game ever shows in a dialogue window of each text kind (briefing 3, mission 2)."""
    caps = {}
    for p in EN.glob('*.json'):
        doc = json.loads(p.read_text(encoding='utf-8'))
        for r in doc['rows']:
            if '<sp(' in r['jp']:
                caps[doc['kind']] = max(caps.get(doc['kind'], 1), r['jp'].count('\n') + 1)
    return caps


def max_lines(kind, jp, caps):
    """Dialogue may take one line more than the Japanese, never more than the window shows; other text keeps its lines."""
    n = jp.count('\n') + 1
    return min(n + 1, caps[kind]) if '<sp(' in jp and kind in caps else n


# Text outside the 28 operations, translated after them in the same format (ESTUDO 8.6). Mission tables keep the
# mission-dialogue layer (speech windows); menus are the UI text of one screen each.
EXTRA_GROUPS = [
    ('xa', 'Extra missions (Nadesico B, Ra Cailum, White Fang...)', ['m6005', 'm6006', 'm6007', 'm6008', 'm6009', 'm6010']),
    ('xb', 'In-game tutorial / manual', ['m6302', 'm6303']),
    ('xc', 'Flashbacks Tak x Marina (054-057)', ['m6320', 'm6321', 'm6322', 'm6323', 'm6324', 'm6325']),
    ('xd', 'Short and system missions', ['m6340', 'm6341', 'm6342', 'm6350', 'm6351', 'm6352', 'm6353', 'm6354', 'm6355',
                                         'm6356', 'm6357', 'm6358', 'm6359', 'm6360', 'm6361', 'm6900', 'm6901', 'm6903',
                                         'm6905', 'm6998']),
]
EXTRA_LABELS = {k: label for k, label, _ in EXTRA_GROUPS}


def units(ops, extras):
    """[(key, operation number or None, [(table, layer, phase)])]: the operations, then (with --extras) the extra groups
    and one group per menu table that still has untranslated rows."""
    out = [('op%02d' % op, op, sequence(op)) for op in ops]
    if extras:
        for key, label, tables in EXTRA_GROUPS:
            out.append((key, None, [(t, 'mission dialogue', None) for t in tables if (EN / (t + '.json')).exists()]))
        for p in sorted(EN.glob('menu*.json')):
            doc = table(p.stem)
            fill = fill_of(p.stem)
            if any(not (r.get('en') or fill.get(str(i))) for i, r in enumerate(doc['rows'])):
                key = 'xm_' + p.stem
                EXTRA_LABELS[key] = 'Menu screen %s' % p.stem
                out.append((key, None, [(p.stem, 'menu', None)]))
    return out


def handed():
    p = AGENT / 'handed.json'
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}


def started(key):
    """An operation (op05) or extra group (xa, xm_menu3019) is frozen once any of its batches was handed or returned."""
    tag = key + '_' if isinstance(key, str) else 'op%02d_' % key
    return any(k.startswith(tag) for k in handed()) or any((AGENT / 'returns').glob(tag + '*.json'))


def hand(args):
    """Record that a batch was given to the agent (freezes its operation's batches)."""
    log = handed()
    for lote in args.lotes:
        if not (AGENT / 'batches' / (lote + '.json')).exists():
            raise SystemExit('no batch ' + lote)
        log[lote] = datetime.date.today().isoformat()
    (AGENT / 'handed.json').write_text(json.dumps(dict(sorted(log.items())), indent=1) + '\n', encoding='utf-8')
    print('handed:', ' '.join(args.lotes))


def make(args):
    ops = parse_ops(args.ops)
    caps = line_caps()
    gl = glossary()
    tm = translated_memory()
    avg, fonts, widths, FONT_OF_KIND, limit_for = font_hint()
    rules = json.loads((GL / 'name_fixes.json').read_text(encoding='utf-8'))['rules']
    do_not_touch = sorted({r['to'].strip() for r in rules if not re.search(r'[?!]', r['to'])})
    portraits = json.loads((GL / 'portraits.json').read_text(encoding='utf-8'))['portraits']
    example_op01()
    from validate_return import present, longer_keys
    longer = longer_keys(gl.keys())
    (AGENT / 'batches').mkdir(parents=True, exist_ok=True)
    AUTO.mkdir(parents=True, exist_ok=True)
    first_seen, unknown, listing = {}, {}, []
    total = {'send': 0, 'tm': 0, 'repeat': 0}
    for key, op, seq in units(ops, args.extras):
        rows = []
        for name, layer, phase in seq:
            doc = table(name)
            fm = FONT_OF_KIND.get(doc['kind'], 'menu')
            jp_max = max(max(widths(fonts[fm], r['jp'])) for r in doc['rows'])
            limit = limit_for(doc['kind'], jp_max)
            for i, r in enumerate(doc['rows']):
                ref = '%s#%d' % (name, i)
                row = {'ref': ref, 'layer': layer, 'phase': phase, 'jp': r['jp']}
                if r['jp'] in tm:
                    row['skip'] = ('tm', tm[r['jp']]); total['tm'] += 1
                elif r['jp'] in first_seen:
                    row['skip'] = ('repeat', first_seen[r['jp']]); total['repeat'] += 1
                else:
                    first_seen[r['jp']] = ref; total['send'] += 1
                px = max(limit, max(widths(fonts[fm], r['jp'])))
                row.update(font=fm, max_line_px=px, max_line_chars_approx=int(px / avg[fm]), jp_lines=r['jp'].count('\n') + 1,
                           max_lines=max_lines(doc['kind'], r['jp'], caps))
                m = PORTRAIT.match(r['jp'])
                if m:
                    row['portrait'] = int(m.group(1))
                if layer == 'mission dialogue' and '<sp(' in r['jp']:
                    row['opens_new_window'] = r['jp'].startswith(('<op(', '<on('))
                rows.append(row)
        send = [r for r in rows if 'skip' not in r]
        batches = [send[k:k + SIZE] for k in range(0, len(send), SIZE)]
        if started(key) and not args.force:
            # batch boundaries move when the translation memory grows: an operation already handed to the agent
            # keeps its batches and auto rows exactly as they were (its rows still count for the repeats above)
            print('%s: handed to the agent, batches kept (--force to rewrite)' % key)
            continue
        (AUTO / (key + '.json')).write_text(json.dumps({
            'note': 'Rows not sent to the agent. tm = exact Japanese already translated (value = English); '
                    'repeat = same Japanese as another row of the pending corpus (value = that ref). '
                    'Filled by validate_return.py --apply.',
            'rows': {r['ref']: {'mode': r['skip'][0], 'value': r['skip'][1]} for r in rows if 'skip' in r}},
            ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        pos = {r['ref']: k for k, r in enumerate(rows)}
        for n, chunk in enumerate(batches, 1):
            lote = '%s_%02d' % (key, n)
            path = AGENT / 'batches' / (lote + '.json')
            listing.append({'batch': lote, 'operation': op if op else key, 'rows': len(chunk),
                            'first': chunk[0]['ref'], 'last': chunk[-1]['ref'],
                            'layers': sorted({r['layer'] for r in chunk})})
            a, b = pos[chunk[0]['ref']], pos[chunk[-1]['ref']]
            ctx = lambda rs: [{'ref': r['ref'], 'layer': r['layer'], 'jp': r['jp'],
                               'en': r['skip'][1] if 'skip' in r and r['skip'][0] == 'tm' else ''} for r in rs]
            text = norm(''.join(r['jp'] for r in chunk))
            # same word-boundary rule as the validator: レイ must not match inside リクレイマー or ドレイク
            # and not inside a longer glossary name: レイ in アムロ・レイ is Amuro, not Layzner's computer
            terms = sorted((v for k, v in gl.items()
                            if k in text and any(present(r['jp'], k, longer.get(k, ())) for r in chunk)),
                           key=lambda v: (-len(v['ja']), v['ja']))
            terms = [v for v in terms if not any(v['ja'] in w['ja'] and v['ja'] != w['ja'] and w['ja'] in text
                                                 and text.count(v['ja']) == text.count(w['ja']) for w in terms)]
            for nm in set(KATAKANA_NAME.findall(text)):
                if nm not in gl:
                    unknown.setdefault(nm, []).append(lote)
            used = sorted({r['portrait'] for r in chunk if 'portrait' in r})
            doc = {
                'batch': lote, 'operation': op, 'group': key, 'group_label': EXTRA_LABELS.get(key, 'Operation %s' % op),
                'previous_batch': '%s_%02d' % (key, n - 1) if n > 1 else None,
                'next_batch': '%s_%02d' % (key, n + 1) if n < len(batches) else None,
                'rows_in_slice': len(chunk),
                'do_not_touch_names': do_not_touch,
                'glossary': terms,
                'known_portraits': {k: v for k, v in portraits.items() if int(k) in used},
                'unknown_portraits': [p for p in used if str(p) not in portraits],
                'context_before': ctx(rows[max(0, a - CONTEXT):a]),
                'rows': [{'ref': r['ref'], 'layer': r['layer'], 'phase': r['phase'],
                          **({'portrait': r['portrait']} if 'portrait' in r else {}),
                          **({'opens_new_window': r['opens_new_window']} if 'opens_new_window' in r else {}),
                          'tokens': TOKEN.findall(r['jp']),
                          'jp_lines': r['jp_lines'], 'max_lines': r['max_lines'],
                          'max_line_px': r['max_line_px'], 'max_line_chars_approx': r['max_line_chars_approx'],
                          'jp': r['jp'], 'en': '', 'notes': ''} for r in chunk],
                'context_after': ctx(rows[b + 1:b + 1 + CONTEXT]),
                'report': {'translator_summary': '', 'rows_examined': '', 'rows_examined_count': 0,
                           'uncertainties': [], 'glossary_proposals': [], 'portrait_speakers': {}},
            }
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('%-14s %4d rows, %4d to translate in %d batches' % (key, len(rows), len(send), len(batches)))
    lst = AGENT / 'LOTES.md'
    old = {}
    if lst.exists():
        for line in lst.read_text(encoding='utf-8').splitlines():
            m = re.match(r'\| `([a-z0-9_]+_\d\d)` \| (.*)$', line)
            if m:
                old[m.group(1)] = line
    for it in listing:
        old['%s' % it['batch']] = '| `%s` | %s | %d | %s | `%s` ... `%s` |' % (
            it['batch'], it['operation'], it['rows'], ', '.join(it['layers']), it['first'], it['last'])
    lst.write_text('# Lotes\n\nOrdem de trabalho: um lote por vez, nesta ordem.\n\n'
                   '| Lote | Op / grupo | Linhas | Camadas | Primeira ... última linha |\n|---|---|---|---|---|\n'
                   + '\n'.join(old[k] for k in sorted(old, key=lambda k: (not k.startswith('op'), k))) + '\n',
                   encoding='utf-8')
    print('sent %(send)d, tm %(tm)d, repeat %(repeat)d' % total)
    print('px per char:', {k: round(v, 2) for k, v in avg.items()})
    if unknown:
        print('names (with ・) not in the glossary: %d' % len(unknown))
        for nm, where in sorted(unknown.items(), key=lambda kv: -len(kv[1])):
            print('  %s  (%d batches: %s)' % (nm, len(where), ' '.join(sorted(set(where))[:4])))


def status(args):
    applied = json.loads((AGENT / 'applied.json').read_text(encoding='utf-8')) if (AGENT / 'applied.json').exists() else {}
    for p in sorted((AGENT / 'batches').glob('*.json'), key=lambda p: (not p.stem.startswith('op'), p.stem)):
        if p.stem.startswith('op') and int(p.stem[2:4]) not in parse_ops(args.ops):
            continue
        if not p.stem.startswith('op') and args.ops:
            continue
        ret = (AGENT / 'returns' / p.name).exists()
        val = AGENT / 'validation' / (p.stem + '.md')
        verdict = re.search(r'\*\*(APROVADO|REJEITADO)\*\*', val.read_text(encoding='utf-8')).group(1) if val.exists() else '-'
        print('%s  entregue=%-3s  validação=%-9s  aplicado=%s' % (p.stem, 'sim' if ret else 'não', verdict,
                                                                  applied.get(p.stem, {}).get('date', 'não')))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=('make', 'status', 'hand'))
    ap.add_argument('lotes', nargs='*')
    ap.add_argument('--ops')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--extras', action='store_true', help='also the text outside the 28 operations (ESTUDO 8.6)')
    args = ap.parse_args()
    {'make': make, 'status': status, 'hand': hand}[args.cmd](args)


if __name__ == '__main__':
    main()
