"""Drop image relationships no slide XML references (left behind when pictures are removed), then delete orphaned media.
usage: python clean_media.py in.pptx out.pptx"""
import sys, re, zipfile, posixpath

def main(src, dst):
    zin = zipfile.ZipFile(src)
    files = {n: zin.read(n) for n in zin.namelist()}
    dropped = 0
    for n in list(files):
        m = re.match(r'ppt/slides/_rels/(slide\d+\.xml)\.rels$', n)
        if not m:
            continue
        used = set(re.findall(rb'r:(?:embed|id|link|pict)="([^"]+)"', files['ppt/slides/' + m.group(1)]))
        def keep(mm):
            nonlocal dropped
            tag = mm.group(0)
            rid = re.search(rb'Id="([^"]+)"', tag).group(1)
            if b'relationships/image' in tag and rid not in used:
                dropped += 1
                return b''
            return tag
        files[n] = re.sub(rb'<Relationship [^>]*/>', keep, files[n])
    referenced = set()
    for n, data in files.items():
        if n.endswith('.rels'):
            base = posixpath.dirname(posixpath.dirname(n))
            for t in re.findall(rb'Target="([^"]+)"', data):
                t = t.decode()
                if not t.startswith('http'):
                    referenced.add(posixpath.normpath(posixpath.join(base, t)).lstrip('/'))
    media = [n for n in files if n.startswith('ppt/media/') and n not in referenced]
    for n in media:
        del files[n]
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zo:
        for info in zin.infolist():
            if info.filename in files:
                zo.writestr(info, files[info.filename])
    print(f'dropped {dropped} unused image rels, removed {len(media)} orphaned media files')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
