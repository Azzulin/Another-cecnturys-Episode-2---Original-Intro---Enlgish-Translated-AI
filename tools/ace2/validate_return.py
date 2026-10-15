"""Validate a translator return against its batch, write a report, and (with --apply) put it in the build input.

  python tools/ace2/validate_return.py op02_01            -> work/translation/agent/validation/op02_01.md
  python tools/ace2/validate_return.py op02_01 --apply    -> also writes work/translation/en/_fill/<table>.json
  python tools/ace2/validate_return.py --all              every return that has no report yet (or changed)
  python tools/ace2/validate_return.py --auto             re-apply the automatic rows of every group

Same procedure as ACE1: the agent only translates; this script (run by the reviewer) is the only way a translation
reaches the game. Reviewer corrections live in work/translation/agent/reviewer_fixes.json ({lote: {ref: english}}),
are applied on top of the return before validation and are listed in the report; the return itself is never edited.

Blocking errors: structure/identity changes (rows added, removed, reordered, frozen fields edited, Japanese that no
longer matches the table), empty rows, control tokens (validate.check_row), forbidden characters, double/trailing
spaces, too many lines, a line too wide that an automatic re-wrap cannot fix, a glossary name missing, an old
spelling that name_fixes.json replaces. Warnings: line re-wrapped automatically, glossary term (rank/title/term)
missing, translator notes, empty report.
"""
import argparse, datetime, hashlib, json, re, sys, unicodedata
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT
from validate import check_row as check_tokens
from textdb import TOKEN
from build import RARE

TR = ROOT / 'work' / 'translation'
EN = TR / 'en'
AGENT = TR / 'agent'
AUTO = TR / 'auto'
GL = ROOT / 'work' / 'glossary'
FROZEN = ('ref', 'layer', 'phase', 'portrait', 'opens_new_window', 'tokens', 'jp_lines', 'max_lines', 'max_line_px',
          'max_line_chars_approx', 'jp')
STRIP = re.compile(r'<[a-z]+\([^)]*\)>|#c\[[0-9A-Fa-f]{6}\]|#c|#i')  # #i...#i: pilot rank names (menu3001)
ICONS = set('○×△□㊤㊦㊧㊨㍉㌢㌔㍍％　') | {chr(c) for c in range(0x2460, 0x2474)}
KATA = re.compile(r'[ァ-ヺー･・]')
NAME_KINDS = {'character', 'unit', 'ship', 'place', 'faction', None}


def norm(s):
    return unicodedata.normalize('NFKC', s or '').replace('･', '・')


def longer_keys(keys):
    """{key: [longer glossary keys that contain it]} (レイ -> アムロ・レイ, ...)."""
    keys = sorted(set(keys), key=len)
    return {k: [K for K in keys if len(K) > len(k) and k in K] for k in keys}


def present(jp, term, longer=()):
    """Occurrence of a glossary key not embedded in a longer katakana word, nor inside a longer glossary name
    (レイ inside アムロ・レイ is Amuro's name, not Layzner's computer)."""
    jp = norm(jp).replace(' ', '').replace('　', '')
    for K in longer:
        jp = jp.replace(K, '〓' * len(K))
    for m in re.finditer(re.escape(term), jp):
        before = jp[m.start() - 1] if m.start() else ' '
        after = jp[m.end()] if m.end() < len(jp) else ' '
        if KATA.match(term[0]) and ((KATA.match(before) and before not in '・') or (KATA.match(after) and after not in '・')):
            continue
        return True
    return False


def accepted_forms(entry):
    forms = {entry['en'], entry.get('en_short'), entry.get('full_name')}
    forms |= {w for f in list(forms) if f for w in re.split(r'[\s/]+', f) if len(w) >= 4}
    return {f.lower() for f in forms if f}


def old_spelling(en, jp, rules):
    for r in rules:
        if r.get('only_if_jp') and r['only_if_jp'] not in jp:
            continue
        if ('regex' in r and re.search(r['regex'], en)) or ('from' in r and r['from'] in en):
            return '%s -> %s' % (r.get('regex', r.get('from')), r['to'])
    return None


def check_row(rr, rb, ctx, neighbors='', fixed=False):
    errors, warns = [], []
    for k in FROZEN:
        if (k in rb or k in rr) and rr.get(k) != rb.get(k):
            # a row the reviewer rewrote takes nothing from the return but its ref: the batch fields stand
            (warns if fixed else errors).append('campo "%s" foi alterado' % k + (' (ignorado: linha reescrita pelo revisor)' if fixed else ''))
    name, _, idx = rb['ref'].partition('#')
    doc = ctx['table'](name)
    if doc['rows'][int(idx)]['jp'] != rb['jp']:
        errors.append('o japonês do lote não confere mais com a tabela %s (lote desatualizado)' % rb['ref'])
    en = rr.get('en', '')
    if not isinstance(en, str) or not en.strip():
        return errors + ['tradução vazia'], warns
    jp = rb['jp']
    errors += check_tokens(jp, en)
    visible = STRIP.sub('', en)
    bad = sorted({c for c in visible if not (c == '\n' or 32 <= ord(c) < 127 or (c in ICONS and c in jp))})
    if bad:
        errors.append('caracteres proibidos: %s' % ' '.join(repr(c) for c in bad))
    if '%' in TOKEN.sub('', en):
        # a lone ASCII % is a printf conversion start: the Japanese writes a literal full-width ％, keep that
        errors.append('"%" solto (fora de %d/%s): use o ％ largo do japonês')
    rare = sorted({c for c in visible if c in RARE})
    if rare:
        errors.append('caracteres ausentes em algumas fontes: %s' % ' '.join(rare))
    for line in visible.split('\n'):
        if '　' in line:
            continue  # report signature aligned with ideographic spaces, as in the Japanese
        if '  ' in line:
            errors.append('espaço duplo: %r' % line)
        if line != line.strip():
            errors.append('espaço no início/fim da linha: %r' % line)
    n_lines = en.count('\n') + 1
    if n_lines > rb['max_lines']:
        errors.append('%d linhas; máximo %d' % (n_lines, rb['max_lines']))
    fm = ctx['fonts'][ctx['font_of'].get(doc['kind'], 'menu')]
    ws = ctx['widths'](fm, en)
    if max(ws) > rb['max_line_px']:
        body = en.rstrip('\n')
        tail = en[len(body):]  # trailing breaks (blank lines after a report paragraph) are layout, kept as they are
        wrapped = ctx['wrap'](fm, body, rb['max_line_px'], rb['max_lines'] - tail.count('\n'))
        wrapped = wrapped + tail if wrapped else None
        if wrapped:
            rr['en_final'] = wrapped  # what --apply writes: the layout that passed this check
            warns.append('linha com %d px > %d px; a quebra automática resolve: %r' % (max(ws), rb['max_line_px'], wrapped))
        elif rb['ref'] in ctx.get('waivers', {}):
            # a provisional menu limit that no faithful English can meet (agent/width_waivers.json, with the reason)
            warns.append('linha com %d px > %d px: dispensa de largura (%s)' % (max(ws), rb['max_line_px'], ctx['waivers'][rb['ref']]))
        else:
            errors.append('linha com %d px > %d px e não cabe em %d linhas: encurte (sem cortar o sentido)'
                          % (max(ws), rb['max_line_px'], rb['max_lines']))
    low = en.lower()
    for g in ctx['glossary']:
        if not present(jp, g['ja'], ctx['longer'].get(g['ja'], ())):
            continue
        if not any(f in low for f in accepted_forms(g)):
            msg = 'glossário: "%s" deve aparecer como "%s"' % (g['ja'], g['en'])
            # a sentence split over two rows may carry the name in the neighbouring row
            near = any(f in neighbors.lower() for f in accepted_forms(g))
            (errors if g.get('kind') in NAME_KINDS and not near else warns).append(msg + (' (está na linha vizinha)' if near else ''))
    old = old_spelling(en, jp, ctx['rules'])
    if old:
        errors.append('grafia substituída pelo projeto: %s' % old)
    if rr.get('notes'):
        warns.append('nota do tradutor: ' + rr['notes'])
    return errors, warns


def context():
    from merge_fill import load_fonts, widths, FONT_OF_KIND
    from rewrap import wrap
    cache = {}

    def table(name):
        if name not in cache:
            cache[name] = json.loads((EN / (name + '.json')).read_text(encoding='utf-8'))
        return cache[name]
    from batches import glossary
    return {'fonts': load_fonts(), 'widths': widths, 'font_of': FONT_OF_KIND, 'wrap': wrap, 'table': table,
            'rules': json.loads((GL / 'name_fixes.json').read_text(encoding='utf-8'))['rules'],
            'longer': longer_keys(glossary().keys()),
            'waivers': json.loads((AGENT / 'width_waivers.json').read_text(encoding='utf-8'))['rows']
            if (AGENT / 'width_waivers.json').exists() else {}}


def validate(lote, ctx, apply=False):
    before = json.loads((AGENT / 'batches' / (lote + '.json')).read_text(encoding='utf-8'))
    ret_path = AGENT / 'returns' / (lote + '.json')
    report = ['# Validação do lote %s' % lote, '']
    out = AGENT / 'validation' / (lote + '.md')
    out.parent.mkdir(exist_ok=True)
    try:
        raw = ret_path.read_bytes()
        ret = json.loads(raw.decode('utf-8-sig'))
    except (OSError, ValueError) as e:
        report += ['**REJEITADO**: arquivo ausente ou JSON inválido: %s' % e]
        out.write_text('\n'.join(report) + '\n', encoding='utf-8'); print('\n'.join(report)); return False
    fixes = {}
    fp = AGENT / 'reviewer_fixes.json'
    if fp.exists():
        fixes = json.loads(fp.read_text(encoding='utf-8')).get(lote, {})
    ctx['glossary'] = before['glossary']
    struct = []
    if ret.get('batch') != lote:
        struct.append('campo "batch" alterado')
    rows_b, rows_r = before['rows'], ret.get('rows', [])
    if [r.get('ref') for r in rows_r] != [r['ref'] for r in rows_b]:
        struct.append('linhas acrescentadas, removidas ou reordenadas (%d no lote, %d na entrega)' % (len(rows_b), len(rows_r)))
    body, n_err, n_warn, applied_fixes = [], len(struct), 0, []
    final = {}
    if not struct:
        ens = [fixes.get(rb['ref'], rr.get('en', '')) for rb, rr in zip(rows_b, rows_r)]
        for k, (rb, rr) in enumerate(zip(rows_b, rows_r)):
            rr = dict(rr)
            if rb['ref'] in fixes:
                applied_fixes.append((rb['ref'], rr.get('en', ''), fixes[rb['ref']]))
                rr['en'] = fixes[rb['ref']]
            errors, warns = check_row(rr, rb, ctx, ' '.join(ens[max(0, k - 1):k] + ens[k + 1:k + 2]), rb['ref'] in fixes)
            n_err += len(errors); n_warn += len(warns)
            final[rb['ref']] = rr.get('en_final', rr.get('en', ''))
            if errors or warns:
                body.append('### `%s` (%s)' % (rb['ref'], rb['layer']))
                body.append('- JP: `%s`' % rb['jp'].replace('\n', '\\n'))
                body.append('- EN: `%s`' % str(rr.get('en', '')).replace('\n', '\\n'))
                body += ['- **ERRO**: ' + e for e in errors] + ['- aviso: ' + w for w in warns] + ['']
    rep = ret.get('report', {})
    if not rep.get('rows_examined'):
        n_warn += 1; body.insert(0, '- aviso: report.rows_examined vazio\n')
    status = 'APROVADO' if not n_err else 'REJEITADO'
    report += ['**%s**: %d erros, %d avisos.' % (status, n_err, n_warn), '',
               'Entrega: `returns/%s.json`, sha256 `%s`.' % (lote, hashlib.sha256(raw).hexdigest()[:16]), '']
    if rep.get('translator_summary'):
        report += ['Resumo do tradutor: ' + rep['translator_summary'], '']
    report += ['Linhas examinadas pelo tradutor: %s (%s)' % (rep.get('rows_examined') or '-', rep.get('rows_examined_count', 0)), '']
    for key, title in (('uncertainties', 'Incertezas do tradutor'), ('glossary_proposals', 'Propostas de glossário'),
                       ('rows_left_untranslated', 'Linhas deixadas sem tradução')):
        if rep.get(key):
            report.append('## %s\n' % title)
            report += ['- %s' % (json.dumps(u, ensure_ascii=False) if not isinstance(u, str) else u) for u in rep[key]] + ['']
    if rep.get('portrait_speakers'):
        report += ['## Retratos identificados pelo tradutor\n'] + ['- %s: %s' % (k, json.dumps(v, ensure_ascii=False))
                                                                   for k, v in rep['portrait_speakers'].items()] + ['']
    if applied_fixes:
        report.append('## Correções do revisor (reviewer_fixes.json)\n')
        for ref, a, b in applied_fixes:
            report += ['- `%s`' % ref, '  - antes: `%s`' % a.replace('\n', '\\n'), '  - depois: `%s`' % b.replace('\n', '\\n')]
        report.append('')
    report += ['- **ERRO estrutural**: ' + e for e in struct] + ([''] if struct else []) + ['## Linhas\n'] + body
    out.write_text('\n'.join(report) + '\n', encoding='utf-8')
    print('%s %s: %d errors, %d warnings -> %s' % (lote, status, n_err, n_warn, out.relative_to(ROOT)))
    if apply:
        if n_err:
            print('Not applied: fix the errors first.'); return False
        merge(lote, before['operation'], final, hashlib.sha256(raw).hexdigest(), ctx)
    return not n_err


def merge(lote, op, final, sha, ctx):
    fills = {}
    for ref, en in final.items():
        name, _, idx = ref.partition('#')
        fills.setdefault(name, {})[idx] = en
    # automatic rows of the batch's group: op05_02 -> auto/op05.json, xm_menu3019_01 -> auto/xm_menu3019.json
    auto = json.loads((AUTO / (lote.rsplit('_', 1)[0] + '.json')).read_text(encoding='utf-8'))['rows']
    def have(ref):
        if final.get(ref):
            return final[ref]
        name, _, idx = ref.partition('#')
        p = EN / '_fill' / (name + '.json')
        return json.loads(p.read_text(encoding='utf-8')).get(idx) if p.exists() else None
    # an automatic copy is right only when the row stands on its own; a fragment of a split objective
    # (掃討する after ...を) needs its own English, kept in auto/overrides.json ({ref: english})
    op_path = AUTO / 'overrides.json'
    overrides = json.loads(op_path.read_text(encoding='utf-8'))['rows'] if op_path.exists() else {}
    n_auto = 0
    for ref, a in auto.items():
        en = overrides.get(ref) or (a['value'] if a['mode'] == 'tm' else have(a['value']))
        if en:
            name, _, idx = ref.partition('#')
            fills.setdefault(name, {})[idx] = en; n_auto += 1
    for name, values in fills.items():
        p = EN / '_fill' / (name + '.json')
        cur = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        cur.update(values)
        p.write_text(json.dumps(dict(sorted(cur.items(), key=lambda kv: int(kv[0]))), ensure_ascii=False, indent=1) + '\n',
                     encoding='utf-8')
    ap = AGENT / 'applied.json'
    log = json.loads(ap.read_text(encoding='utf-8')) if ap.exists() else {}
    log[lote] = {'date': datetime.date.today().isoformat(), 'sha256': sha, 'rows': len(final), 'auto_rows': n_auto}
    ap.write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied %s: %d rows + %d automatic -> _fill/ (%s)' % (lote, len(final), n_auto, ', '.join(sorted(fills))))


def apply_auto():
    """Re-apply the automatic rows of every group (auto/<group>.json) until nothing changes. Needed for groups with
    no batch of their own (menu3023, menu3074) and for copies of rows that were filled after their group was applied."""
    op_path = AUTO / 'overrides.json'
    overrides = json.loads(op_path.read_text(encoding='utf-8'))['rows'] if op_path.exists() else {}
    fills = {}

    def fill(name):
        if name not in fills:
            p = EN / '_fill' / (name + '.json')
            fills[name] = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        return fills[name]
    groups = [p for p in AUTO.glob('*.json') if p.name != 'overrides.json']
    changed, total = set(), 0
    for _ in range(5):
        n = 0
        for g in groups:
            for ref, a in json.loads(g.read_text(encoding='utf-8'))['rows'].items():
                if a['mode'] == 'tm':
                    en = a['value']
                else:
                    src, _, si = a['value'].partition('#')
                    en = fill(src).get(si)
                en = overrides.get(ref) or en
                name, _, idx = ref.partition('#')
                if en and fill(name).get(idx) != en:
                    fill(name)[idx] = en; changed.add(name); n += 1
        total += n
        if not n:
            break
    for name in changed:
        p = EN / '_fill' / (name + '.json')
        p.write_text(json.dumps(dict(sorted(fills[name].items(), key=lambda kv: int(kv[0]))), ensure_ascii=False, indent=1)
                     + '\n', encoding='utf-8')
    print('automatic rows: %d written in %d tables (%s)' % (total, len(changed), ', '.join(sorted(changed))))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('batch', nargs='?')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--auto', action='store_true', help='re-apply the automatic rows of every group (after applying)')
    args = ap.parse_args()
    if args.auto:
        return apply_auto()
    ctx = context()
    lotes = [args.batch] if args.batch else sorted(p.stem for p in (AGENT / 'returns').glob('*.json'))
    bad = [l for l in lotes if not validate(l, ctx, args.apply)]
    if bad:
        raise SystemExit('rejected: ' + ' '.join(bad))


if __name__ == '__main__':
    main()
