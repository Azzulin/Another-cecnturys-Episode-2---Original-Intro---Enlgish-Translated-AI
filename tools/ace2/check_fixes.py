"""Check proposed reviewer fixes before they go into agent/reviewer_fixes.json (writes nothing).

  python tools/ace2/check_fixes.py <proposal.json> [...]

A proposal is {lote: {ref: english}}, the same shape as reviewer_fixes.json. Every proposed line is run through the
same row check as validate_return.py (tokens, characters, spaces, lines, pixel width with automatic re-wrap, glossary
names, old spellings) against its batch row. Prints OK or the problems for each line.
"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from validate_return import AGENT, check_row, context


def main():
    ctx = context()
    bad = 0
    for path in sys.argv[1:]:
        for lote, rows in json.loads(Path(path).read_text(encoding='utf-8')).items():
            batch = json.loads((AGENT / 'batches' / (lote + '.json')).read_text(encoding='utf-8'))
            ctx['glossary'] = batch['glossary']
            by_ref = {r['ref']: r for r in batch['rows']}
            for ref, en in rows.items():
                if ref not in by_ref:
                    print('NO ROW  %s %s' % (lote, ref)); bad += 1; continue
                rb = by_ref[ref]
                errors, warns = check_row(dict(rb, en=en), rb, ctx)
                if errors:
                    bad += 1
                    print('ERROR   %s %s: %s' % (lote, ref, '; '.join(errors)))
                else:
                    print('OK      %s %s%s' % (lote, ref, ('  (' + '; '.join(w for w in warns if 'nota' not in w) + ')')
                                                  if any('nota' not in w for w in warns) else ''))
    print('%d proposed lines with errors' % bad)
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
