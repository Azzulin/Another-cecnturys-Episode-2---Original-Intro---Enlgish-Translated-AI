"""Row checks shared by the build and the translation review tools.

check_row(jp, en, table=None) -> list of problems (empty when the row is safe to build):
  tokens    control tokens (<sp()>, <ab()>, <op()>, <ed()>, <on()>, <off()>, <im()>, <fz()>, #c[..]/#c, %d, %s, button
            and icon glyphs) must appear in the same order as in the Japanese source
  encoding  the text must encode as CP932 and contain no NUL
  ascii     letters must be ASCII (not fullwidth) so they use the completed fonts and 1 byte each
  newlines  no more line breaks than the source plus one (layout check before the width check exists)
  message   a message-window row (one with <sp()>) shows at most MESSAGE_BYTES visible bytes (tags and colour codes
            not counted, line breaks counted): the window copies the text into a 128-byte field and draws one
            sprite per character into a buffer of 128 (exe.py GLYPHS; the Japanese never goes past 122)
  widget    a plain one-line row (no tags, no line break, Japanese within WIDGET_GLYPHS) of a mission (m6###, not
            the credits m6285) or HUD table shows at most WIDGET_GLYPHS characters, spaces included: mission
            objectives, counters and pause help lines go to text widgets with the default capacity of 32 (init
            0x289dfc; both widget classes, buffers (7n+11)*16 and (11n+12)*16+32 bytes), and the game never checks
            it (Op 11-1 freeze of 0.0.14, CHANGELOG 0.0.15); menu3056 (objectives on the mission data screens) too

check_counters(table, rows) -> problems of a whole table, rows = [(jp, en)] in table order:
  counter   the HUD counter of a mission draws its label, a full-width colon and the formatted value in one
            32-character widget ('Solar Facilities Destroyed：1 facilities' froze Op 11-1 in 0.0.15): a plain
            row with %d right after a plain row (the label) must fit label + 1 + value in WIDGET_GLYPHS
"""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from textdb import TOKEN

FULLWIDTH_LATIN = re.compile(r'[Ａ-Ｚａ-ｚ０-９]')
JAPANESE = re.compile(r'[぀-ヿ一-鿿]')
CODES = re.compile(r'<[a-z]+\([^)]*\)>|#c\[[0-9A-Fa-f]{6}\]|#c|#i')
MESSAGE_BYTES = 127
WIDGET_GLYPHS = 32
WIDGET_TABLE = re.compile(r'm6(?!285)\d{3}$|hud\d+$|menu3056$')
MISSION_TABLE = re.compile(r'm6(?!285)\d{3}$')


def visible_bytes(text):
    return len(CODES.sub('', text).encode('cp932', 'replace'))


def glyphs(text):
    """Characters a text widget draws: one sprite each, spaces included, line breaks and codes not; %d counted
    as 3 digits."""
    return len(CODES.sub('', text).replace('%d', '000').replace('\n', ''))


def check_row(jp, en, table=None):
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
    if '<sp(' in jp and visible_bytes(en) > MESSAGE_BYTES:
        problems.append('message window holds %d visible bytes, this row has %d' % (MESSAGE_BYTES, visible_bytes(en)))
    if (table and WIDGET_TABLE.match(table) and '<' not in jp and '\n' not in jp
            and glyphs(jp) <= WIDGET_GLYPHS < glyphs(en)):
        problems.append('text widget holds %d characters, this row has %d' % (WIDGET_GLYPHS, glyphs(en)))
    return problems


def plain(jp):
    return '<' not in jp and '\n' not in jp


def check_counters(table, rows):
    problems = []
    if not MISSION_TABLE.match(table):
        return problems
    for (ljp, lab), (jp, en) in zip(rows, rows[1:]):
        if '%d' in jp and plain(jp) and plain(ljp) and '%' not in ljp and lab and en:
            used = glyphs(lab) + 1 + glyphs(en)
            if glyphs(ljp) + 1 + glyphs(jp) <= WIDGET_GLYPHS < used:
                problems.append('HUD counter %r：%r draws %d characters in a widget of %d'
                                % (lab, en, used, WIDGET_GLYPHS))
    return problems
