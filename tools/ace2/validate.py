"""Row checks shared by the build and the translation review tools.

check_row(jp, en) -> list of problems (empty when the row is safe to build):
  tokens    control tokens (<sp()>, <ab()>, <op()>, <ed()>, <on()>, <off()>, <im()>, <fz()>, #c[..]/#c, %d, %s, button
            and icon glyphs) must appear in the same order as in the Japanese source
  encoding  the text must encode as CP932 and contain no NUL
  ascii     letters must be ASCII (not fullwidth) so they use the completed fonts and 1 byte each
  newlines  no more line breaks than the source plus one (layout check before the width check exists)
"""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from textdb import TOKEN

FULLWIDTH_LATIN = re.compile(r'[Ａ-Ｚａ-ｚ０-９]')
JAPANESE = re.compile(r'[぀-ヿ一-鿿]')


def check_row(jp, en):
    problems = []
    jt, et = TOKEN.findall(jp), TOKEN.findall(en)
    if jt != et:
        problems.append('tokens %s != %s' % (jt, et))
    try:
        raw = en.encode('cp932')
        if b'\0' in raw:
            problems.append('NUL in text')
    except UnicodeEncodeError as ex:
        problems.append('not CP932: %r' % en[ex.start:ex.end])
    if FULLWIDTH_LATIN.search(en):
        problems.append('fullwidth letters/digits: use ASCII')
    if JAPANESE.search(TOKEN.sub('', en)):
        problems.append('Japanese left in translation')
    if en.count('\n') > jp.count('\n') + 1:
        problems.append('%d line breaks vs %d in source' % (en.count('\n'), jp.count('\n')))
    return problems
