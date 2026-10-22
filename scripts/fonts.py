"""Pick the font pair for this machine. Prints the CN serif, the EN serif and the EN font file (used to
measure English line wraps). The first installed font in each list wins.

  python fonts.py            -> human summary + a configure(...) line to paste into the build script
"""
import os, sys, glob, platform, subprocess

CN = [  # (family name written into the pptx, file-name patterns)
    ('Source Han Serif SC', ['SourceHanSerif*', 'SourceHanSerifSC*', 'NotoSerifCJK*', 'NotoSerifSC*', '思源宋体*']),
    ('FZShuSong-Z01', ['FZSSK*', 'FZShuSong*', '方正书宋*']),
    ('Songti SC', ['Songti.ttc']),
    ('STSong', ['STSong*', '华文宋体*']),
    ('SimSun', ['simsun.ttc', 'SimSun*']),
]
EN = [
    ('EB Garamond', ['EBGaramond*']),
    ('Adobe Garamond Pro', ['AGaramondPro*']),
    ('Garamond', ['GARA.TTF', 'Garamond*.ttf']),
    ('Cormorant Garamond', ['CormorantGaramond*']),
    ('Hoefler Text', ['Hoefler Text.ttc']),
    ('Baskerville', ['Baskerville.ttc']),
    ('Times New Roman', ['Times New Roman.ttf', 'times.ttf']),
]


def font_dirs():
    home = os.path.expanduser('~')
    if platform.system() == 'Darwin':
        return [f'{home}/Library/Fonts', '/Library/Fonts', '/System/Library/Fonts', '/System/Library/Fonts/Supplemental',
                '/Applications/Microsoft PowerPoint.app/Contents/Resources/DFonts']
    if platform.system() == 'Windows':
        return [os.path.join(os.environ.get('WINDIR', r'C:\Windows'), 'Fonts'),
                os.path.join(os.environ.get('LOCALAPPDATA', ''), r'Microsoft\Windows\Fonts')]
    return [f'{home}/.fonts', f'{home}/.local/share/fonts', '/usr/share/fonts', '/usr/local/share/fonts']


def find(cands):
    for fam, pats in cands:
        for d in font_dirs():
            for pat in pats:
                hits = glob.glob(os.path.join(d, '**', pat), recursive=True)
                if hits:
                    return fam, sorted(hits)[0]
    return None, None


def main():
    cn, cn_file = find(CN)
    en, en_file = find(EN)
    print(f'CN serif: {cn or "none found"}  ({cn_file})')
    print(f'EN serif: {en or "none found"}  ({en_file})')
    if cn != CN[0][0] or en not in ('EB Garamond', 'Adobe Garamond Pro', 'Garamond'):
        print('note: the preferred pair is Source Han Serif SC + EB Garamond (both free). Tell the user which '
              'substitute was used; they can install the pair and swap fonts in one place (theme fonts).')
    print(f"\nK.configure(en_font={en!r}, cn_font={cn!r}, en_font_file={en_file!r})")


if __name__ == '__main__':
    main()
