"""Reviewer aid (as in ACE1): dump returns as JP/EN pairs with context and flag suspicious rows.

  python tools/ace2/review_returns.py [op02_01 ...]   -> work/translation/agent/review/<LOTE>.md

Each row shows ref, layer, speaker hint (portrait / new window), Japanese, English (reviewer fix applied, marked)
and the translator note. Flags: romanized honorifics or Japanese words, parentheses (notes inside the text), TODO/???,
English much shorter than the Japanese suggests (possible dropped clause), sentence closed where the Japanese row
continues in the next one.
"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT

AGENT = ROOT / 'work' / 'translation' / 'agent'
STRIP = re.compile(r'<[a-z]+\([^)]*\)>|#c\[[0-9A-Fa-f]{6}\]|#c|#i')
SUSPECT = re.compile(r"\b(san|sama|kun|chan|dono|baka|desu|nani|sensei|senpai|kancho|taicho)\b|\(.*?\)|TODO|\?\?\?", re.I)
CONTINUES = re.compile(r'[、の]\s*$|[をにがはでと]\s*$')


def flags(jp, en):
    out = []
    j, e = STRIP.sub('', jp), STRIP.sub('', en)
    if SUSPECT.search(e):
        out.append('suspeito: %s' % SUSPECT.search(e).group())
    jl = len(re.sub(r'[\s　…！？。、]', '', j))
    if jl >= 12 and len(e.split()) < jl / 6:
        out.append('inglês curto para o japonês (%d palavras / %d caracteres)' % (len(e.split()), jl))
    if CONTINUES.search(j.rstrip('\n')) and re.search(r'[.!?]["\']?\s*$', e.rstrip('\n')):
        out.append('o japonês continua na próxima linha, mas o inglês fecha a frase')
    return out


def main():
    fixes = json.loads((AGENT / 'reviewer_fixes.json').read_text(encoding='utf-8')) if (AGENT / 'reviewer_fixes.json').exists() else {}
    lotes = sys.argv[1:] or sorted(p.stem for p in (AGENT / 'returns').glob('*.json'))
    (AGENT / 'review').mkdir(exist_ok=True)
    for lote in lotes:
        d = json.loads((AGENT / 'returns' / (lote + '.json')).read_text(encoding='utf-8-sig'))
        fx = fixes.get(lote, {})
        out = ['# Revisão %s\n' % lote]
        n_flag = 0
        for r in d['rows']:
            en = fx.get(r['ref'], r.get('en', ''))
            hint = ('retrato %s' % r['portrait']) if 'portrait' in r else ('nova janela' if r.get('opens_new_window') else
                                                                          ('continua' if 'opens_new_window' in r else ''))
            out.append('- [%s | %s%s]' % (r['ref'], r['layer'], ' | ' + hint if hint else ''))
            out.append('    JP: %s' % STRIP.sub('', r['jp']).replace('\n', ' / '))
            out.append('    EN%s: %s' % (' (revisor)' if r['ref'] in fx else '', STRIP.sub('', en).replace('\n', ' / ')))
            if r.get('notes'):
                out.append('    nota: %s' % r['notes'])
            for f in flags(r['jp'], en):
                out.append('    **%s**' % f); n_flag += 1
        (AGENT / 'review' / (lote + '.md')).write_text('\n'.join(out) + '\n', encoding='utf-8')
        print('%s: %d rows, %d flags -> review/%s.md' % (lote, len(d['rows']), n_flag, lote))


if __name__ == '__main__':
    main()
