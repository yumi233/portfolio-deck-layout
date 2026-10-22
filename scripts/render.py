"""Render a deck for visual QA: pptx -> pdf -> one PNG per slide + 3x3 contact sheets.

  python render.py deck.pptx OUTDIR [--prefix s] [--width 1600]

Converter: Keynote on macOS (AppleScript), else LibreOffice (`soffice`/`libreoffice` on PATH).
Fonts are those of the machine doing the rendering — check the deck on the machine that will present it.
"""
import sys, os, math, shutil, subprocess, argparse, platform
import fitz

KEYNOTE = '''on run argv
  set inPath to POSIX file (item 1 of argv)
  set outPath to POSIX file (item 2 of argv)
  with timeout of 280 seconds
    tell application id "com.apple.Keynote"
      set d to open inPath
      delay 1
      export d to outPath as PDF with properties {PDF image quality:Good}
      close d saving no
    end tell
  end timeout
end run'''


def has_keynote():
    if platform.system() != 'Darwin':
        return False
    if os.path.exists('/Applications/Keynote.app'):
        return True
    r = subprocess.run(['mdfind', 'kMDItemCFBundleIdentifier == "com.apple.Keynote"'], capture_output=True, text=True)
    return bool(r.stdout.strip())


def to_pdf(pptx, pdf):
    pptx, pdf = os.path.abspath(pptx), os.path.abspath(pdf)
    if os.path.exists(pdf):
        os.remove(pdf)
    if has_keynote():
        script = os.path.join(os.path.dirname(pdf), '_kn2pdf.applescript')
        open(script, 'w').write(KEYNOTE)
        try:
            subprocess.run(['osascript', script, pptx, pdf], check=True, timeout=300, capture_output=True, text=True)
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
            sys.exit('Keynote 没有在 5 分钟内导出 PDF。Keynote 很可能弹出了对话框（缺字体、格式提示等），'
                     '并且在等人点击；这个对话框不关掉，之后所有文件都会卡住。请用户切到 Keynote 关掉对话框，'
                     '或者退出 Keynote，然后重试。从零新建的稿子，请用 K.blank_deck(base=现成的 16:9 pptx) 作底。'
                     f'\n({type(e).__name__}: {getattr(e, "stderr", "") or ""})')
        finally:
            if os.path.exists(script):
                os.remove(script)
        return pdf
    soffice = shutil.which('soffice') or shutil.which('libreoffice')
    if not soffice:
        sys.exit('No renderer found: install Keynote (macOS) or LibreOffice.')
    subprocess.run([soffice, '--headless', '--convert-to', 'pdf', '--outdir', os.path.dirname(pdf), pptx],
                   check=True, timeout=600)
    produced = os.path.join(os.path.dirname(pdf), os.path.splitext(os.path.basename(pptx))[0] + '.pdf')
    if produced != pdf:
        shutil.move(produced, pdf)
    return pdf


def to_png(pdf, outdir, prefix='s', width=1600):
    os.makedirs(outdir, exist_ok=True)
    d = fitz.open(pdf)
    for i, p in enumerate(d):
        z = width / p.rect.width
        p.get_pixmap(matrix=fitz.Matrix(z, z)).save(f'{outdir}/{prefix}{i + 1:02d}.png')
    W = 640; H = int(W * d[0].rect.height / d[0].rect.width); gap = 8; lab = 22
    sheets = []
    for s in range(math.ceil(d.page_count / 9)):
        sheet = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 3 * W + 4 * gap, 3 * (H + lab) + 4 * gap), 0)
        sheet.set_rect(sheet.irect, (200, 60, 200))                      # magenta frame shows page edges
        for k, i in enumerate(range(s * 9, min(d.page_count, (s + 1) * 9))):
            p = d[i]; z = W / p.rect.width
            pix = p.get_pixmap(matrix=fitz.Matrix(z, z))
            x = gap + (k % 3) * (W + gap); y = gap + (k // 3) * (H + lab + gap) + lab
            pix.set_origin(x, y); sheet.copy(pix, pix.irect)
        path = f'{outdir}/{prefix}sheet{s + 1}.png'
        sheet.save(path); sheets.append(path)
    return d.page_count, sheets


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('pptx'); ap.add_argument('outdir')
    ap.add_argument('--prefix', default='s'); ap.add_argument('--width', type=int, default=1600)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    pdf = to_pdf(a.pptx, os.path.join(a.outdir, os.path.splitext(os.path.basename(a.pptx))[0] + '.pdf'))
    n, sheets = to_png(pdf, a.outdir, a.prefix, a.width)
    print(f'{n} slides -> {a.outdir}'); print('\n'.join(sheets)); print('pdf:', pdf)
