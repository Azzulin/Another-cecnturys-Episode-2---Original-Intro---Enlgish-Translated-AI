"""Format library for Another Century's Episode 2 - Special Vocal Version (SLPS-25829).

Adapted from the ACE1 library (D:\\Ace 1\\tools\\ace1\\ace1lib.py), which itself copies codecs from ACE3 0.9.3 (MIT).

Containers
  DATA.BIN index binder    'BND\\0' f7ff0000 d3 | +12 total size | +16 count | +24 0x30800 (kept as is)
                           entries @36: (id, offset, size), ids ascending, payloads 2048-aligned, no names
  inner binder             'BND\\0' | +4 size | +8 count | (id, offset) pairs @16, payloads 32-aligned
  packed                   ACE3 LZSS: 00 01 00 00 | unpacked size BE | 0 | body
  text table               magic 0x10000, size, 0, ranges, count, pointer array, 0 | ranges | pointers | CP932 pool
  mission container        00 01 00 00 ... | +8..+12 sub-table records (id, offset) x16 | +20 pointer to the dialogue table
"""
import hashlib
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# Base disc: every build starts from the untouched Special Vocal Version.
BASE = ROOT / "Another Century's Episode 2 - Special Vocal Version (Japan).iso"
# Original 2006 release: source of the opening movie with "Glorious" only.
ORIGINAL_RELEASE = ROOT / "Another Century's Episode 2 (Japan).iso"
BASE_EXE = '/SLPS_258.29'
SECTOR = 2048


def u32(data, offset):
    return struct.unpack_from('<I', data, offset)[0]


def require(value, message):
    if not value:
        raise ValueError(message)


def align(value, to):
    return (value + to - 1) // to * to


def sha(data):
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------- ISO9660

def iso_files(stream):
    """{'/DATA.BIN': {'offset', 'size', 'record'}}; record = absolute offset of the directory record."""
    stream.seek(16 * SECTOR)
    pvd = stream.read(SECTOR)
    require(pvd[:7] == b'\x01CD001\x01', 'Expected ISO9660 primary volume')
    found = {}

    def walk(lba, size, parent):
        stream.seek(lba * SECTOR)
        data = stream.read(size)
        at = 0
        while at < len(data):
            length = data[at]
            if not length:
                at = (at // SECTOR + 1) * SECTOR
                continue
            record = data[at:at + length]
            name = record[33:33 + record[32]]
            if name not in (b'\0', b'\1'):
                full = parent + '/' + name.decode('ascii').split(';')[0]
                if record[25] & 2:
                    walk(u32(record, 2), u32(record, 10), full)
                else:
                    found[full] = {'offset': u32(record, 2) * SECTOR, 'size': u32(record, 10), 'record': lba * SECTOR + at}
            at += length

    walk(u32(pvd, 158), u32(pvd, 166), '')
    return found


# ---------------------------------------------------------------- DATA.BIN

class DataBin:
    """DATA.BIN index. Payload order and 2048 alignment are preserved on rebuild."""
    HEAD = 36
    MAGIC = b'BND\0\xff\xf7\0\0'

    def __init__(self, head, entries, size):
        self.head, self.entries, self.size = head, entries, size
        self.by_id = {e[0]: e for e in entries}

    @classmethod
    def read_index(cls, stream, base):
        stream.seek(base)
        top = stream.read(cls.HEAD)
        require(top[:8] == cls.MAGIC, 'Not an ACE2 DATA.BIN')
        count = u32(top, 16)
        stream.seek(base)
        probe = stream.read(cls.HEAD + count * 12)
        entries = [struct.unpack_from('<3I', probe, cls.HEAD + i * 12) for i in range(count)]
        require([e[0] for e in entries] == sorted(e[0] for e in entries), 'DATA.BIN ids not ascending')
        first = min(e[1] for e in entries)
        stream.seek(base)
        return cls(stream.read(first), entries, u32(top, 12))

    def layout(self, sizes):
        """New (offset, size) per id, original payload order, 2048-aligned. Returns (offsets, total)."""
        order = sorted(self.entries, key=lambda e: e[1])
        cursor = order[0][1]
        require(cursor >= self.HEAD + len(self.entries) * 12, 'Index overlaps payloads')
        result = {}
        for i, e in enumerate(order):
            size = sizes[e[0]]
            result[e[0]] = (cursor, size)
            cursor = cursor + size if i + 1 == len(order) else align(cursor + size, SECTOR)
        return result, cursor

    def header_for(self, offsets, total):
        head = bytearray(self.head)
        struct.pack_into('<I', head, 12, total)
        for i, e in enumerate(self.entries):
            off, size = offsets[e[0]]
            struct.pack_into('<II', head, self.HEAD + i * 12 + 4, off, size)
        return bytes(head)


class Disc:
    """Read-only access to a disc image and its DATA.BIN resources."""

    def __init__(self, path=BASE):
        self.path = Path(path)
        self.stream = self.path.open('rb')
        self.files = iso_files(self.stream)
        self.data_file = self.files['/DATA.BIN']
        self.index = DataBin.read_index(self.stream, self.data_file['offset'])

    def get(self, rid):
        _, off, size = self.index.by_id[rid]
        self.stream.seek(self.data_file['offset'] + off)
        return self.stream.read(size)

    def ids(self):
        return [e[0] for e in self.index.entries]

    def close(self):
        self.stream.close()


# ---------------------------------------------------------------- inner binder

def inner_entries(data):
    if data[:4] != b'BND\0' or len(data) < 16 or u32(data, 4) != len(data):
        return None
    count = u32(data, 8)
    if not 0 < count < 4096 or 16 + count * 8 > len(data):
        return None
    rows = [struct.unpack_from('<II', data, 16 + i * 8) for i in range(count)]
    out = []
    for n, (eid, off) in enumerate(rows):
        end = rows[n + 1][1] if n + 1 < count else len(data)
        if not (16 + count * 8 <= off <= end <= len(data)):
            return None
        out.append((eid, off, end))
    return out


def inner_get(data, eid):
    return next(data[a:b] for e, a, b in inner_entries(data) if e == eid)


def inner_rebuild(data, replace):
    """Rebuild an inner binder; every payload but the last is padded to 32 like the original."""
    rows = inner_entries(data)
    require(rows is not None, 'Not an inner binder')
    out = bytearray(data[:rows[0][1]])
    for n, (eid, start, end) in enumerate(rows):
        struct.pack_into('<I', out, 16 + n * 8 + 4, len(out))
        payload = replace.get(eid, data[start:end])
        out.extend(payload)
        if n + 1 < len(rows):
            out.extend(bytes(align(len(out), 32) - len(out)))
    struct.pack_into('<I', out, 4, len(out))
    return bytes(out)


# ---------------------------------------------------------------- LZSS (ACE3 tools/packed_resource.py, MIT)

PACK_MAGIC = b'\x00\x01\x00\x00'
WINDOW, MAX_LEN = 4096, 16


def is_packed(data):
    return len(data) >= 12 and data[:4] == PACK_MAGIC and data[8:12] == b'\0\0\0\0'


def unpack(data):
    require(is_packed(data), 'Not a packed resource')
    size = struct.unpack('>I', data[4:8])[0]
    out = bytearray()
    at = 12
    while len(out) < size:
        flags = data[at]; at += 1
        for bit in range(8):
            if len(out) >= size:
                break
            if flags >> bit & 1:
                b0, b1 = data[at], data[at + 1]; at += 2
                field = b0 << 4 | b1 >> 4
                source = field if len(out) < WINDOW else len(out) - WINDOW + field
                for k in range((b1 & 15) + 1):
                    out.append(out[source + k] if source + k < len(out) else 0)
            else:
                out.append(data[at]); at += 1
    return bytes(out)


def try_unpack(data):
    """Unpacked bytes, or None when the LZSS signature is a false positive (truncated stream)."""
    if not is_packed(data):
        return None
    try:
        return unpack(data)
    except IndexError:
        return None


def pack(plain, align_to=16):
    out = bytearray(PACK_MAGIC + struct.pack('>I', len(plain)) + b'\0\0\0\0')
    chains, n, at = {}, len(plain), 0
    flag_at, bit, items = None, 8, bytearray()

    def insert(p):
        if p + 3 <= n:
            chains.setdefault(plain[p:p + 3], []).append(p)

    while at < n:
        best_len, best_src = 0, 0
        if at + 3 <= n:
            candidates = chains.get(plain[at:at + 3], ())
            limit = min(MAX_LEN, n - at)
            for p in reversed(candidates[-64:]):
                if at - p > WINDOW:
                    break
                k = 3
                while k < limit and plain[p + k] == plain[at + k]:
                    k += 1
                if k > best_len:
                    best_len, best_src = k, p
                    if k == limit:
                        break
        if bit == 8:
            out += items; items = bytearray(); flag_at = len(out); out.append(0); bit = 0
        if best_len >= 3:
            field = best_src if at < WINDOW else WINDOW - (at - best_src)
            out[flag_at] |= 1 << bit
            items += bytes([field >> 4, (field & 15) << 4 | (best_len - 1)])
            for p in range(at, at + best_len):
                insert(p)
            at += best_len
        else:
            items.append(plain[at]); insert(at); at += 1
        bit += 1
    out += items
    out += bytes(-len(out) % align_to)
    return bytes(out)


# ---------------------------------------------------------------- text tables

class TextTable:
    def __init__(self, data):
        require(len(data) >= 40, 'Short text table')
        magic, size, zero, ranges, count, pointers, reserved = struct.unpack_from('<7I', data)
        require(magic == 0x10000 and zero == reserved == 0, 'Not a text table')
        require(0 < ranges < 4096 and pointers == 28 + ranges * 12 and pointers + count * 4 <= size <= len(data), 'Bad table layout')
        ids = []
        for i in range(ranges):
            base, first, last = struct.unpack_from('<3I', data, 28 + i * 12)
            require(base == len(ids) and first <= last, 'Bad ID range')
            ids.extend(range(first, last + 1))
        require(len(ids) == count, 'Slot count mismatch')
        self.data, self.size, self.pointers, self.ids = bytes(data[:size]), size, pointers, ids
        self.rows = {}
        for slot, tid in enumerate(ids):
            p = u32(data, pointers + slot * 4)
            if p:
                end = data.index(b'\0', p, size)
                self.rows[tid] = data[p:end].decode('cp932')

    def rebuild(self, texts):
        """New table with replaced rows; identical strings share one pool entry; size padded to 32."""
        head_end = self.pointers + len(self.ids) * 4
        out = bytearray(self.data[:head_end])
        pool = {}
        for slot, tid in enumerate(self.ids):
            if tid not in self.rows:
                continue
            raw = texts.get(tid, self.rows[tid]).encode('cp932')
            require(b'\0' not in raw, 'NUL in text')
            if raw not in pool:
                pool[raw] = len(out); out.extend(raw + b'\0')
            struct.pack_into('<I', out, self.pointers + slot * 4, pool[raw])
        out.extend(bytes(align(len(out), 32) - len(out)))
        struct.pack_into('<I', out, 4, len(out))
        check = TextTable(out)
        require(check.rows == {t: texts.get(t, s) for t, s in self.rows.items()}, 'Table round-trip failed')
        return bytes(out)


def mission_table(data):
    """(offset, TextTable) of a mission container's active dialogue table, or None."""
    if data[:4] != b'\0\1\0\0' or len(data) < 32 or is_packed(data):
        return None
    at = u32(data, 20)
    try:
        return at, TextTable(data[at:])
    except (ValueError, UnicodeError, struct.error):
        return None


def mission_rebuild(data, texts):
    """ACE3 method: append the rebuilt table (32-aligned) and repoint +20; everything else stays byte-identical."""
    at, table = mission_table(data)
    new_table = table.rebuild(texts)
    start = align(len(data), 32)
    out = bytearray(data + bytes(start - len(data)) + new_table)
    struct.pack_into('<I', out, 20, start)
    require(out[:20] == data[:20] and out[24:len(data)] == data[24:], 'Mission container modified outside +20')
    return bytes(out)


def small_tables(data):
    """Sub-tables listed in a mission container header (id, offset) records from +8..+12 (e.g. enemy names)."""
    first, end = u32(data, 8), u32(data, 12)
    out = []
    for at in range(first, end, 16):
        sid, off = struct.unpack_from('<II', data, at)
        try:
            out.append((sid, off, TextTable(data[off:])))
        except (ValueError, UnicodeError, struct.error):
            pass
    return out
