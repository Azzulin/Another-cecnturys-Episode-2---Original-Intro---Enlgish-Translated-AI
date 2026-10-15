"""Disc writer for ACE2 (ported from D:\\Ace 1\\tools\\ace1\\build.py, ACE3 method).

write_disc(base, out, resources, files):
  resources  {DATA.BIN id: new payload bytes}
  files      {'/MOVIE0/MOVIE001.PSS': (source image path, ISO path)} - whole-file swaps from another disc image
Layout: DATA.BIN is rebuilt with every payload 2048-aligned in its original order; the files after it on the disc
move by DATA.BIN's growth (absorbed by the empty disc tail, so the image size never changes); ISO9660 records (both
endians) and UDF file entries are rewritten. The output is re-read and every extent, file payload and changed
resource is verified before the function returns.
"""
import binascii, hashlib, struct
from pathlib import Path
from ace2lib import SECTOR, DataBin, iso_files, u32, require, align

COPY_BLOCK = 8 << 20


def fix_udf_checksum(data):
    length = struct.unpack_from('<H', data, 10)[0]
    struct.pack_into('<H', data, 8, binascii.crc_hqx(bytes(data[16:16 + length]), 0))
    data[4] = 0
    data[4] = sum(data[:16]) & 255


def plan_layout(files, new_sizes):
    order = sorted(files, key=lambda k: files[k]['offset'])
    wanted, shift = {}, 0
    for name in order:
        size = new_sizes.get(name, files[name]['size'])
        wanted[name] = {'offset': files[name]['offset'] + shift, 'size': size}
        shift += align(size, SECTOR) - align(files[name]['size'], SECTOR)
    return order, wanted, shift


def metadata(base, src, files, wanted):
    import pycdlib
    prefix_end = min(r['offset'] for r in files.values())
    src.seek(0); prefix = bytearray(src.read(prefix_end))
    for name, r in files.items():
        require(r['record'] + 34 <= prefix_end, 'Directory record outside metadata prefix')
        for delta, value in ((2, wanted[name]['offset'] // SECTOR), (10, wanted[name]['size'])):
            struct.pack_into('<I', prefix, r['record'] + delta, value)
            struct.pack_into('>I', prefix, r['record'] + delta + 4, value)
    udf = pycdlib.PyCdlib(); udf.open(str(base))
    partition = udf.udf_main_descs.partitions[0].part_start_location
    count = 0
    for parent, _, names in udf.walk(udf_path='/'):
        for n in names:
            path = parent.rstrip('/') + '/' + n
            record = wanted[path.upper()]
            entry = udf.get_record(udf_path=path)
            start = entry.orig_extent_loc * SECTOR
            raw = bytearray(prefix[start:start + SECTOR])
            require(struct.unpack_from('<H', raw)[0] == 261, 'Expected a UDF file entry for ' + path)
            ad = 176 + u32(raw, 168)
            require(u32(raw, 172) == 8, 'Expected one short allocation descriptor')
            struct.pack_into('<Q', raw, 56, record['size'])
            struct.pack_into('<Q', raw, 64, align(record['size'], SECTOR) // SECTOR)
            struct.pack_into('<II', raw, ad, record['size'], record['offset'] // SECTOR - partition)
            fix_udf_checksum(raw)
            prefix[start:start + SECTOR] = raw
            count += 1
    udf.close()
    require(count == len(files), 'UDF entries (%d) do not match ISO9660 files (%d)' % (count, len(files)))
    return bytes(prefix)


def copy(src, dst, offset, size, digest):
    src.seek(offset); left = size
    while left:
        block = src.read(min(COPY_BLOCK, left)); require(block, 'Short read')
        dst.write(block); digest.update(block); left -= len(block)


def file_digest(stream, offset, size):
    d = hashlib.sha256(); stream.seek(offset); left = size
    while left:
        block = stream.read(min(COPY_BLOCK, left)); d.update(block); left -= len(block)
    return d.hexdigest()


def plan(base, resources, files):
    """Dry run: returns the layout summary without writing anything."""
    with Path(base).open('rb') as src:
        iso = iso_files(src)
        idx = DataBin.read_index(src, iso['/DATA.BIN']['offset'])
        sizes = {e[0]: len(resources[e[0]]) if e[0] in resources else e[2] for e in idx.entries}
        offsets, total = idx.layout(sizes)
        swap_sizes = {}
        for name, (image, path) in files.items():
            with Path(image).open('rb') as other:
                swap_sizes[name] = iso_files(other)[path]['size']
        order, wanted, shift = plan_layout(iso, dict(swap_sizes, **{'/DATA.BIN': total}))
        image_size = Path(base).stat().st_size
        last_end = max(w['offset'] + w['size'] for w in wanted.values())
        require(align(last_end, SECTOR) <= image_size, 'Disc would need to grow beyond the original image')
        return {'data_bin': [iso['/DATA.BIN']['size'], total], 'files_shifted_bytes': shift,
                'tail_left_bytes': image_size - align(last_end, SECTOR),
                'changed_resources': {str(k): [idx.by_id[k][2], len(v)] for k, v in sorted(resources.items())},
                'swapped_files': {k: [iso[k]['size'], v] for k, v in swap_sizes.items()}}


def write_disc(base, out, resources, files):
    base, out = Path(base), Path(out)
    require(not out.exists(), 'Output exists: ' + str(out))
    out.parent.mkdir(parents=True, exist_ok=True)
    with base.open('rb') as src:
        iso = iso_files(src)
        data_file = iso['/DATA.BIN']
        idx = DataBin.read_index(src, data_file['offset'])
        require(set(resources) <= set(idx.by_id), 'Unknown resource ids')
        sizes = {e[0]: len(resources[e[0]]) if e[0] in resources else e[2] for e in idx.entries}
        offsets, total = idx.layout(sizes)
        swaps = {}
        for name, (image, path) in files.items():
            require(name in iso, 'No such file on the base disc: ' + name)
            other = Path(image).open('rb')
            swaps[name] = (other, iso_files(other)[path])
        order, wanted, shift = plan_layout(iso, dict({k: v[1]['size'] for k, v in swaps.items()}, **{'/DATA.BIN': total}))
        image_size = base.stat().st_size
        prefix = metadata(base, src, iso, wanted)
        header = idx.header_for(offsets, total)
        hashes = {}
        with out.open('xb') as dst:
            dst.write(prefix)
            for name in order:
                w = wanted[name]
                require(dst.tell() <= w['offset'], 'Extent overlap at ' + name)
                dst.write(bytes(w['offset'] - dst.tell()))
                d = hashlib.sha256()
                if name in swaps:
                    other, rec = swaps[name]
                    copy(other, dst, rec['offset'], rec['size'], d)
                elif name != '/DATA.BIN':
                    copy(src, dst, iso[name]['offset'], iso[name]['size'], d)
                else:
                    dst.write(header); d.update(header)
                    cursor = len(header)
                    for e in sorted(idx.entries, key=lambda e: offsets[e[0]][0]):
                        off, size = offsets[e[0]]
                        pad = bytes(off - cursor); dst.write(pad); d.update(pad)
                        payload = resources.get(e[0])
                        if payload is None:
                            copy(src, dst, data_file['offset'] + e[1], e[2], d)
                        else:
                            dst.write(payload); d.update(payload)
                        cursor = off + size
                    require(cursor == total, 'DATA.BIN size mismatch')
                hashes[name] = d.hexdigest()
            dst.write(bytes(align(dst.tell(), SECTOR) - dst.tell()))
            src.seek(align(max(r['offset'] + r['size'] for r in iso.values()), SECTOR))
            tail = src.read()
            require(not any(tail[:max(0, shift)]), 'Disc tail is not empty where files moved')
            dst.write(tail[max(0, shift):] if shift >= 0 else bytes(-shift) + tail)
        for other, _ in swaps.values():
            other.close()
    # verification on the written image
    with out.open('rb') as o:
        got = iso_files(o)
        require({k: (v['offset'], v['size']) for k, v in got.items()} == {k: (v['offset'], v['size']) for k, v in wanted.items()},
                'Output extents differ from plan')
        for name in order:
            require(file_digest(o, got[name]['offset'], got[name]['size']) == hashes[name], 'Payload differs: ' + name)
        idx2 = DataBin.read_index(o, got['/DATA.BIN']['offset'])
        for rid, payload in resources.items():
            _, off, size = idx2.by_id[rid]
            o.seek(got['/DATA.BIN']['offset'] + off)
            require(o.read(size) == payload, 'Resource %d differs' % rid)
    require(out.stat().st_size == image_size, 'Image size changed')
    digest = hashlib.sha256()
    with out.open('rb') as o:
        for block in iter(lambda: o.read(COPY_BLOCK), b''):
            digest.update(block)
    return {'sha256': digest.hexdigest(), 'files_shifted_bytes': shift, 'data_bin': [data_file['size'], total]}
