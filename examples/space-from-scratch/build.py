"""Example: an interior project (室内 / 建筑类) built from scratch — no source deck, only six photos.
Shows the generic route: accent from the photos, blank_deck base, pages A B C D G I I' J K M, AI slots.

  python -I build.py BASE.pptx IMAGES_DIR OUT.pptx WORKDIR

BASE.pptx: any 16:9 deck whose fonts this machine has (all its slides are dropped).
IMAGES_DIR: main.jpg interior.jpg water.jpg exterior.jpg court.jpg night.jpg (any photos of one space).
"""
import sys, os
BASE, IMAGES, OUT, WORK = sys.argv[1:5]
SKILL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(SKILL, 'scripts'))
from PIL import Image
from pptx import Presentation
import pptx_kit as K, assets as AS, fonts as FN

cn, _ = FN.find(FN.CN); en, en_file = FN.find(FN.EN)
_, cn_file = FN.find(FN.CN)
K.configure(en_font=en, cn_font=cn, en_font_file=en_file)
os.makedirs(WORK, exist_ok=True)
img = {k: os.path.join(IMAGES, f'{k}.jpg') for k in ('main', 'interior', 'water', 'exterior', 'court', 'night')}
acc = AS.suggest_accent([img['main'], img['interior'], img['water']])
K.set_accent(acc['main'], acc['light'])
print('accent', acc)

prs = K.blank_deck(base=BASE)
def page():
    return K.new_slide(prs, 'Blank')

def crop_to(path, aspect, out):
    im = Image.open(path); W, H = im.size
    if W / H > aspect:
        w = H * aspect; box = ((W - w) / 2, 0, (W + w) / 2, H)
    else:
        h = W / aspect; box = (0, (H - h) / 2, W, (H + h) / 2)
    im.crop(tuple(int(v) for v in box)).save(out, quality=90); return out

K.build_cover(page(), '檐下', 'Under the Eaves', '茶室空间改造设计', 'Tea Room Renovation', 'October 2026', img['main'])
K.build_toc(page(), [('场地分析', 'Site Analysis'), ('设计策略', 'Design Strategy'), ('空间呈现', 'Spaces'), ('设计总结', 'Summary')])
K.build_divider(page(), '场地分析', 'Site Analysis', None, (0, 0, 1, 1))

d = page(); K.white_bg(d); K.header(d, '人流与视线', 'Circulation and Views')
K.pic(d, crop_to(img['exterior'], 3 / 2, os.path.join(WORK, 'ext32.jpg')), 60, 96, w=420)
K.line(d, 520, 290, 900, 290, K.MIDL, 0.75)
for k, (x, t, e) in enumerate(((540, '入口', 'Entrance'), (690, '庭院', 'Courtyard'), (840, '水面', 'Water'))):
    c = d.shapes.add_shape(9, K.E(x - 3), K.E(287), K.E(6), K.E(6)); c.fill.solid()
    c.fill.fore_color.rgb = K.RGBColor.from_string(K.RED); c.line.fill.background()
    K.tb(d, x - 40, 302, 80, 30, [K.P1(t, 11, K.TITLE), K.P1(e, 8.5, K.AUX, before=1)], align='c')
K.tb(d, 520, 180, 380, 60, [K.P1('人流从街面进入，在庭院停留，最后面向水面。', 12, K.BODY, ln=19),
                            K.P1('Visitors enter from the street, pause in the courtyard and end facing the water.', 10, K.BODY, ln=14, before=4)])
K.vfit(d)

g = page(); K.build_g(g, 'The Water Room', '临水茶室', crop_to(img['water'], 16 / 9, os.path.join(WORK, 'water169.jpg')), (160, 150, 640, 330))

i = page(); K.white_bg(i); K.header(i, '临水茶室', 'The Water Room')
K.pic(i, crop_to(img['interior'], 4 / 3, os.path.join(WORK, 'int43.jpg')), 64, 104, w=480)
blk = [K.tb(i, 640, 0, 260, 40, [K.P1('框景入室', 14, K.TITLE), K.P1('Framing the View', 11, K.BODY, before=2)]),
       K.tb(i, 640, 0, 260, 70, [K.P1('木构柱网收住座席，开口把水面框进室内。', 12, K.BODY, ln=19),
                                 K.P1('The timber grid holds the seats; openings frame the water.', 10, K.BODY, ln=14, before=4)]),
       K.tb(i, 640, 0, 260, 50, [K.P1('杉木 · 夯土 · 石材', 10, K.AUX), K.P1('Fir · Rammed earth · Stone', 8.5, K.AUX, before=1)])]
K.text_block(i, [b._element for b in blk], 640, 284, [0, 12, 22])

v = page(); K.white_bg(v); K.header(v, '临水茶室', 'The Water Room')
K.build_views(v, [(crop_to(img['court'], 3 / 4, os.path.join(WORK, 'court34.jpg')), '庭院', 'Courtyard'),
                  (crop_to(img['night'], 3 / 4, os.path.join(WORK, 'night34.jpg')), '夜景', 'At Night')], max_h=300)

j = page(); K.white_bg(j); K.header(j, '临水茶室', 'The Water Room')
K.add_slot(j, 56, 84, 304, 380, '01-X', '轴测爆炸 · 4:5 · 1600×2000', '参考图：主效果图',
           'Exploded axonometric of a timber-framed tea room by the water: roof, timber column grid, rammed-earth walls and stone floor separated along vertical dashed lines, on a seamless pure white background, soft light --ar 4:5',
           os.path.join(WORK, 'slots'), font_file=cn_file)
for n, (cn_l, en_l) in enumerate((('木构节点', 'Timber joint'), ('夯土墙面', 'Rammed earth'), ('石材收边', 'Stone edge'))):
    x = 400 + n * 173
    K.add_slot(j, x, 182, 154, 154, f'01-D{n + 1}', '细部特写 · 1:1', '参考图：主效果图',
               f'Macro close-up of the {en_l.lower()} in a minimal timber tea room, soft raking light, no text --ar 1:1',
               os.path.join(WORK, 'slots'), font_file=cn_file)
    K.tb(j, x - 10, 344, 174, 26, [K.P1(cn_l, 10, K.BODY), K.P1(en_l, 8, K.AUX, before=1)], align='c')

kpg = page(); K.white_bg(kpg)
K.pic(kpg, crop_to(img['court'], 2 / 3, os.path.join(WORK, 'court23.jpg')), 135, 30, w=320, h=480)
K.pic(kpg, crop_to(img['water'], 4 / 5, os.path.join(WORK, 'water45.jpg')), 495, 98, w=330, h=412.5)

m = page(); K.white_bg(m)
K.pic(m, crop_to(img['main'], 16 / 9, os.path.join(WORK, 'main169.jpg')), 80, 45, w=800, h=450)

back = page(); K.build_cover(back, '檐下', 'Under the Eaves', '茶室空间改造设计', 'Tea Room Renovation', 'October 2026', img['main'])
prs.save(OUT)
K.set_theme_fonts(OUT)
print('saved', OUT, len(prs.slides), 'slides;', K.log or 'no warnings')
