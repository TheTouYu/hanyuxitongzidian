"""Minimal Word 97 (.doc) text extractor: CFB container + FIB piece table.
Usage: python _tmp_doc2txt.py <file.doc> <out.txt>
"""
import struct, sys

def read_cfb(path):
    data = open(path, 'rb').read()
    if data[:8] != bytes.fromhex('D0CF11E0A1B11AE1'):
        raise SystemExit('not an OLE2 compound file')
    sect = 1 << struct.unpack_from('<H', data, 0x1E)[0]
    mini = 1 << struct.unpack_from('<H', data, 0x20)[0]
    nfat = struct.unpack_from('<I', data, 0x2C)[0]
    dirstart = struct.unpack_from('<I', data, 0x30)[0]
    cutoff = struct.unpack_from('<I', data, 0x38)[0]
    minifat_start = struct.unpack_from('<I', data, 0x3C)[0]
    difat_start = struct.unpack_from('<I', data, 0x44)[0]

    def sector_off(s):
        return 512 + s * sect

    # DIFAT -> list of FAT sector numbers
    fat_sectors = [struct.unpack_from('<I', data, 0x4C + i * 4)[0] for i in range(109)]
    nxt = difat_start
    while nxt not in (0xFFFFFFFE, 0xFFFFFFFF) and len(fat_sectors) < 100000:
        off = sector_off(nxt)
        per = sect // 4 - 1
        fat_sectors += [struct.unpack_from('<I', data, off + i * 4)[0] for i in range(per)]
        nxt = struct.unpack_from('<I', data, off + per * 4)[0]
    fat_sectors = [s for s in fat_sectors if s < 0xFFFFFFF0][:nfat]

    fat = []
    for s in fat_sectors:
        off = sector_off(s)
        fat += list(struct.unpack_from('<%dI' % (sect // 4), data, off))

    def chain(start):
        out, s, guard = [], start, 0
        while s < 0xFFFFFFF0 and guard < 1 << 20:
            out.append(s)
            s = fat[s] if s < len(fat) else 0xFFFFFFFE
            guard += 1
        return out

    def read_chain(start, size):
        return b''.join(data[sector_off(s):sector_off(s) + sect] for s in chain(start))[:size]

    # directory
    d = read_chain(dirstart, 1 << 30)
    entries = []
    for i in range(len(d) // 128):
        e = d[i * 128:(i + 1) * 128]
        nlen = struct.unpack_from('<H', e, 0x40)[0]
        name = e[:max(0, nlen - 2)].decode('utf-16-le', 'ignore')
        typ = e[0x42]
        start = struct.unpack_from('<I', e, 0x74)[0]
        size = struct.unpack_from('<Q', e, 0x78)[0]
        entries.append((name, typ, start, size))

    root = next(e for e in entries if e[1] == 5)
    ministream = read_chain(root[2], root[3])
    minifat = []
    if minifat_start < 0xFFFFFFF0:
        mf = read_chain(minifat_start, 1 << 30)
        minifat = list(struct.unpack_from('<%dI' % (len(mf) // 4), mf, 0))

    def read_mini(start, size):
        out, s, guard = b'', start, 0
        while s < 0xFFFFFFF0 and guard < 1 << 20:
            out += ministream[s * mini:(s + 1) * mini]
            s = minifat[s] if s < len(minifat) else 0xFFFFFFFE
            guard += 1
        return out[:size]

    streams = {}
    for name, typ, start, size in entries:
        if typ != 2:
            continue
        streams[name] = read_mini(start, size) if size < cutoff else read_chain(start, size)
    return streams

def extract(path):
    st = read_cfb(path)
    wd = st['WordDocument']
    flags = struct.unpack_from('<H', wd, 0x0A)[0]
    table = st['1Table' if flags & 0x0200 else '0Table']
    fcClx, lcbClx = struct.unpack_from('<II', wd, 0x01A2)
    ccpText = struct.unpack_from('<I', wd, 0x4C)[0]
    clx = table[fcClx:fcClx + lcbClx]
    # skip Prc blocks
    i = 0
    while i < len(clx) and clx[i] == 1:
        cb = struct.unpack_from('<h', clx, i + 1)[0]
        i += 3 + cb
    assert clx[i] == 2, 'no Pcdt found'
    lcb = struct.unpack_from('<I', clx, i + 1)[0]
    plc = clx[i + 5:i + 5 + lcb]
    n = (lcb - 4) // 12
    cps = list(struct.unpack_from('<%dI' % (n + 1), plc, 0))
    out = []
    for k in range(n):
        pcd = plc[(n + 1) * 4 + k * 8:(n + 1) * 4 + (k + 1) * 8]
        fc = struct.unpack_from('<I', pcd, 2)[0]
        chars = cps[k + 1] - cps[k]
        if fc & 0x40000000:
            off = (fc & 0x3FFFFFFF) // 2
            out.append(wd[off:off + chars].decode('cp1252', 'replace'))
        else:
            out.append(wd[fc:fc + chars * 2].decode('utf-16-le', 'replace'))
    text = ''.join(out)[:ccpText]
    text = text.replace('\r', '\n').replace('\x07', '\n').replace('\x0b', '\n')
    text = text.replace('\x0c', '\n').replace('\x1e', '-').replace('\xa0', ' ')
    text = ''.join(ch for ch in text if ch == '\n' or ch >= ' ' or ch == '\t')
    lines = [ln.rstrip() for ln in text.split('\n')]
    return '\n'.join(lines)

if __name__ == '__main__':
    open(sys.argv[2], 'w', encoding='utf-8').write(extract(sys.argv[1]))
    print('ok')
