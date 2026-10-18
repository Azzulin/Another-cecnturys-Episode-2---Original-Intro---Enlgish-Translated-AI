"""The only changes made to the game executable /SLPS_258.29 (project owner's decision, 2026-10-10): the stack/heap
boundary (memory for the arena) and the glyph capacity of the message window (PATCHES).

Memory map of the game (32 MB): executable up to 0x003afd80 | memory arena 0x003afe00..0x01cfff00 (every scene and
mission is loaded there; a request that does not fit returns NULL, and the game does not check it) | second area
0x01cfff00..0x01efff00 (last 2 MB of the same block) | main thread stack 0x01f00000..0x02000000.

The stack had 1 MB and the game used at most 161 KB of it (boot, menus, briefing, Op 12-1 and its cutscene;
work/crash/20261010-110851-travamento-12-1). Moving the stack/heap boundary up 256 KB gives the arena 256 KB more:
about 200 times what the translation still adds to a mission (ESTUDO 8.6 item 0), and the stack keeps 768 KB.
The second area follows the arena end (getter 0x150290), so it moves up with it.

  python tools/ace2/exe.py      prints the patches checked against the base disc
"""
import struct, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import BASE, BASE_EXE, Disc, require

STACK_GAIN = 0x40000
PATCHES = [
    # (address, original word, new word, what)
    (0x10019c, 0x3c0501f0, 0x3c0501f4, 'crt0 SetupThread: stack base 0x01f00000 -> 0x01f40000'),
    (0x1001a0, 0x3c060010, 0x3c06000c, 'crt0 SetupThread: stack size 0x100000 -> 0xc0000 (top stays 0x02000000)'),
    (0x12b268, 0x3c0201f0, 0x3c0201f4, 'heap size for the arena (0x12b260): heap end 0x01f00000 -> 0x01f40000'),
    (0x292704, 0x2405003c, 0x24050080, 'message window text: glyph capacity 60 -> 128 (see GLYPHS below)'),
]
# Text widgets (class with init 0x289bd0) draw one 7-quadword sprite per character into a buffer reserved once from
# their capacity (0x289e30: (7 n + 11) * 16 bytes); the glyph builder 0x1a1050 never checks it. The message window
# class (method 0x292700) asks for 60: the Japanese script never goes past 60 characters per message, English does
# (about 2,000 rows), and every extra character overwrites the next object in the arena. That froze Op 12-1 after
# its cutscene (rows of 65-67 characters before it corrupted a HUD sprite drawn in the boss phase) and the pause
# menu of 0.0.9 (confirmations of 89-96 characters). The text itself is copied into a 128-byte field of the message
# window (0x017e2d7c in the 0.0.10 freeze, count right after it), so 128 glyphs is all a message can ever show.
GLYPHS = 128


def file_offset(elf, address):
    """ELF file offset of a virtual address (program headers)."""
    phoff, phnum = struct.unpack_from('<I', elf, 28)[0], struct.unpack_from('<H', elf, 44)[0]
    for i in range(phnum):
        kind, off, vaddr, _, filesz = struct.unpack_from('<5I', elf, phoff + i * 32)
        if kind == 1 and vaddr <= address < vaddr + filesz:
            return off + address - vaddr
    raise ValueError('Address 0x%x is not in the executable' % address)


def patch(elf):
    """Patched executable; every original word must be the expected one."""
    out = bytearray(elf)
    for address, old, new, _ in PATCHES:
        at = file_offset(elf, address)
        require(struct.unpack_from('<I', elf, at)[0] == old, 'Unexpected word at 0x%x' % address)
        struct.pack_into('<I', out, at, new)
    return bytes(out)


def read_exe(disc):
    rec = disc.files[BASE_EXE]
    disc.stream.seek(rec['offset'])
    return disc.stream.read(rec['size'])


def main():
    elf = read_exe(Disc(BASE))
    new = patch(elf)
    for address, old, new_word, what in PATCHES:
        print('0x%06x  %08x -> %08x  %s' % (address, old, new_word, what))
    print('%d bytes differ; arena +%d KB; message window %d glyphs' % (sum(a != b for a, b in zip(elf, new)),
                                                                        STACK_GAIN // 1024, GLYPHS))


if __name__ == '__main__':
    main()
