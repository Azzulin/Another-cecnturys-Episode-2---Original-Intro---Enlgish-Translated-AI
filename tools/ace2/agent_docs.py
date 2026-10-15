"""Write the translator's glossary view: work/translation/agent/GLOSSARIO.md (same role as ACE1's GLOSSARIO.md).

  python tools/ace2/agent_docs.py

Only names that occur in the game's Japanese text are listed, grouped by category and series, with the short form,
gender, role and personality from the research (work/glossary/research, ACE3 glossary). The English always comes from
work/glossary/names.json (glossary.py), so this page never disagrees with the batches or with validate_return.py.
"""
import collections, json, re, sys, unicodedata
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT
from glossary import NOT_IN_ACE2

GL = ROOT / 'work' / 'glossary'
EN = ROOT / 'work' / 'translation' / 'en'
OUT = ROOT / 'work' / 'translation' / 'agent' / 'GLOSSARIO.md'
ACE3 = Path(r'D:\Ace 1\ACE-3-0.9.3\ACE-3-0.9.3\work\glossary')
SERIES = [  # (match in the research "series" text, canonical name), first match wins
    ('0083', 'Mobile Suit Gundam 0083: Stardust Memory'),
    ("Char's Counterattack", "Mobile Suit Gundam: Char's Counterattack"),
    ('Zeta', 'Mobile Suit Zeta Gundam'),
    ('G Gundam', 'Mobile Fighter G Gundam'),
    ('Wing', 'Mobile Suit Gundam Wing / Endless Waltz'),
    ('Universal Century', 'Gundam (Universal Century, geral)'),
    ('Mobile Suit Gundam', 'Gundam (Universal Century, geral)'),
    ('Macross', 'Super Dimension Fortress Macross: Do You Remember Love?'),
    ('Rean', 'Aura Battler Dunbine / The Wings of Rean'),
    ('Dunbine', 'Aura Battler Dunbine / The Wings of Rean'),
    ('L-Gaim', 'Heavy Metal L-Gaim'),
    ('Layzner', 'Blue Comet SPT Layzner'),
    ('Brain Powerd', 'Brain Powerd'),
    ('Nadesico', 'Martian Successor Nadesico (TV / Prince of Darkness)'),
    ('Dragonar', 'Metal Armor Dragonar'),
    ('Another Century', "Another Century's Episode (original)"),
]
UNIT_SERIES = [  # units that the research gives without a series: by English name
    (('VF-1', 'Valkyrie', 'Queadluun'), 'Super Dimension Fortress Macross: Do You Remember Love?'),
    (('Nu Gundam', 'Re-GZ'), "Mobile Suit Gundam: Char's Counterattack"),
    (('Aestivalis', 'Alstroemeria', 'Black Sarena', 'Nanajin'), 'Martian Successor Nadesico (TV / Prince of Darkness)'),
    (('Dragonar',), 'Metal Armor Dragonar'), (('Billbine', 'Oukaou'), 'Aura Battler Dunbine / The Wings of Rean'),
    (('Nelly Brain',), 'Brain Powerd'), (('Falguen',), 'Heavy Metal L-Gaim'), (('UNKNOWN',), "Another Century's Episode (original)"),
]
CATS = [('character', 'Personagens'), ('unit', 'Unidades (mechas)'), ('ship', 'Naves'),
        ('faction', 'Facções e organizações'), ('place', 'Lugares'), ('term', 'Termos da série'),
        ('generic', 'Termos genéricos (soldados, operadores, tipos de unidade)')]


def norm(s):
    return unicodedata.normalize('NFKC', s or '').replace('･', '・').replace(' ', '').replace('　', '')


def canon(series):
    for key, name in SERIES:
        if series and key in series:
            return name
    return 'Série não identificada'


def cut(text, n=110):
    text = (text or '').replace('|', '/').replace('\n', ' ')
    return text if len(text) <= n else text[:n - 3].rstrip() + '...'


def details():
    out = {}
    for e in json.loads((GL / 'decisions.json').read_text(encoding='utf-8'))['entries']:
        for k in (norm(e.get('ja')), norm(e.get('ja_short'))):
            if k and e.get('series'):
                out.setdefault(k, e)
    for path in sorted((GL / 'research').glob('*.json')):
        for e in json.loads(path.read_text(encoding='utf-8'))['entries']:
            for k in (norm(e.get('ja')), norm(e.get('ja_short'))):
                if k:
                    out.setdefault(k, e)
    for e in json.loads((ACE3 / 'character_names_021.json').read_text(encoding='utf-8'))['entries']:
        if any(x in (e.get('series') or '') for x in NOT_IN_ACE2):
            continue
        d = {'kind': 'character', 'series': e.get('series'), 'gender': e.get('gender'), 'role': e.get('role'),
             'personality': e.get('personality'), 'ja': e.get('ja_full'), 'ja_short': e.get('ja_short'),
             'en_short': e.get('en_short')}
        for k in (norm(e.get('ja_full')), norm(e.get('ja_short'))):
            if k:
                out.setdefault(k, d)
    for f in ('unit_names_014_a', 'unit_names_014_b'):
        for e in json.loads((ACE3 / (f + '.json')).read_text(encoding='utf-8'))['entries']:
            if e.get('ja'):
                out.setdefault(norm(e['ja']), {'kind': 'unit'})
    return out


class Corpus:
    """Occurrences counted like validate_return.present: a key inside a longer katakana word does not count."""
    def __init__(self):
        self.rows = [norm(r['jp']) for p in EN.glob('*.json') for r in json.loads(p.read_text(encoding='utf-8'))['rows']]
        self.text = '\n'.join(self.rows)

    def count(self, key):
        from validate_return import present
        return sum(1 for r in self.rows if key in r and present(r, key)) if key in self.text else 0


def main():
    names = json.loads((GL / 'names.json').read_text(encoding='utf-8'))
    det, text = details(), Corpus()
    short_en = names['short']
    rows = collections.defaultdict(lambda: collections.defaultdict(list))
    seen_short = set()
    for k, v in names['full'].items():
        n = text.count(k)
        if not n:
            continue
        d = det.get(k, {})
        kind = d.get('kind') or 'unit'
        ks = norm(d.get('ja_short'))
        short = ''
        if ks and ks != k and ks in short_en:
            short = '%s = %s' % (d.get('ja_short'), short_en[ks]['en'])
            seen_short.add(ks)
        series = canon(d.get('series'))
        if series == 'Série não identificada':
            series = next((name for keys, name in UNIT_SERIES if any(x in v['en'] for x in keys)), series)
        rows[kind if kind in dict(CATS) else 'term'][series].append(
            (k, v['en'], short, d.get('gender') or '', cut(d.get('role')), cut(d.get('personality'), 90), n))
    for k, v in short_en.items():
        if k in seen_short or k in names['full'] or not text.count(k):
            continue
        d = det.get(k, {})
        rows['character'][canon(d.get('series'))].append((k, v['en'], '(forma curta)', d.get('gender') or '',
                                                          cut(d.get('role')), cut(d.get('personality'), 90), text.count(k)))
    terms = json.loads((GL / 'terms.json').read_text(encoding='utf-8'))['terms']
    fixes = json.loads((GL / 'name_fixes.json').read_text(encoding='utf-8'))['rules']
    decisions = json.loads((GL / 'decisions.json').read_text(encoding='utf-8'))['entries']
    portraits = json.loads((GL / 'portraits.json').read_text(encoding='utf-8'))['portraits']
    md = ['# Glossário (ACE2)', '',
          'Gerado por `tools/ace2/agent_docs.py` a partir de `work/glossary/` (fonte da verdade: `names.json`). '
          'Só aparecem nomes que existem no texto do jogo; "ocorr." é quantas vezes o japonês aparece.', '',
          '- **Obrigatório:** todo nome desta página que aparece no japonês de uma linha deve aparecer em inglês exatamente '
          'assim. O validador rejeita a linha se o nome de personagem, unidade, nave, facção ou lugar faltar.',
          '- Na fala, use a forma curta quando o japonês usa a forma curta (ex.: シナプス → Sinapus).',
          '- **Gênero:** use a coluna; quando ela estiver vazia, não deduza pelo nome.',
          '- Nome que não está aqui nem no `glossary` do lote: translitere, marque em `notes` e proponha em '
          '`report.glossary_proposals` com a fonte (título da página na wiki da série).', '']
    md += ['## Grafias fixadas pelo projeto (não "corrija")', '', '| Use | Nunca | Por quê |', '|---|---|---|']
    for r in fixes:
        if not re.search(r'[?!]', r['to']):
            md.append('| %s | %s | %s |' % (r['to'].strip(), r.get('from', r.get('regex', '')).replace('\\b', '').replace('|', '/'), cut(r['why'], 120)))
    md += ['', '## Tratamentos e termos recorrentes (como na Operação 01)', '', '| Japonês | Inglês | Nota |', '|---|---|---|']
    md += ['| %s | %s%s | %s |' % (t['ja'], t['en'], (' (' + t['en_short'] + ')') if t.get('en_short') else '', t.get('note', ''))
           for t in terms]
    md += ['', '## Retratos do briefing (`<op(N,1)>`)', '', '| N | Quem fala | Gênero | Papel | Confiança |', '|---|---|---|---|---|']
    md += ['| %s | %s | %s | %s | %s |' % (k, v['speaker'], v['gender'], v['role'], v['confidence']) for k, v in
           sorted(portraits.items(), key=lambda kv: int(kv[0]))]
    md += ['', 'Retratos que não estão na tabela: descubra pelo contexto e informe em `report.portrait_speakers`.', '']
    order = [name for _, name in SERIES]
    for kind, title in CATS:
        if not rows[kind]:
            continue
        md += ['## %s' % title, '']
        for series in sorted(rows[kind], key=lambda s: (order.index(s) if s in order else 99, s)):
            md += ['### %s' % series, '']
            if kind == 'character':
                md += ['| Japonês | Inglês | Forma curta | Gênero | Papel | Personalidade (voz) | Ocorr. |', '|---|---|---|---|---|---|---|']
                md += ['| %s | %s | %s | %s | %s | %s | %d |' % r for r in sorted(rows[kind][series], key=lambda r: -r[6])]
            else:
                md += ['| Japonês | Inglês | Descrição | Ocorr. |', '|---|---|---|---|']
                md += ['| %s | %s | %s | %d |' % (r[0], r[1], r[4], r[6]) for r in sorted(rows[kind][series], key=lambda r: -r[6])]
            md.append('')
    pending = [d for d in decisions if d.get('by') != 'owner']
    if pending:
        md += ['## Decisões provisórias (use como estão)', '', '| Japonês | Inglês | Motivo |', '|---|---|---|']
        md += ['| %s | %s | %s |' % (d['ja'], d['en'], cut(d['why'], 140)) for d in pending]
    OUT.write_text('\n'.join(md) + '\n', encoding='utf-8')
    total = sum(len(v) for c in rows.values() for v in c.values())
    print('%d names in the game text -> %s' % (total, OUT.relative_to(ROOT)))
    for kind, title in CATS:
        print('  %-10s %s' % (kind, {s: len(v) for s, v in rows[kind].items()}))


if __name__ == '__main__':
    main()
