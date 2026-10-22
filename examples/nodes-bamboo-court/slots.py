"""Every AI-image slot in v26: id -> prompt, aspect, reference image, and the page labels around it.
IDs match 图片补全清单.md."""

STYLE = ('contemporary Chinese tea furniture, brushed stainless-steel round tubes joined by cylindrical clamp collars and '
         'round disc bolts like bamboo nodes, warm walnut, walnut-brown saddle leather with contrast top-stitching, cream '
         'cotton webbing in a basket weave, fluted glass, cream translucent mulberry-paper panels; soft natural daylight, '
         'muted low-saturation warm palette, quiet minimal oriental atmosphere')
NEG = ('Negative: text, watermark, logo, signature, extra legs, warped or melted joints, wrong number of tubes, distorted '
       'proportions, rattan, cane, cluttered props, oversaturated colours, plastic look, CGI artefacts, people facing camera')

ANCHOR = {
    'table': ('a long tea table with a thick walnut top with softly bevelled edges; one end stands on a tall brushed '
              'stainless-steel pedestal cabinet with a small access door and a round cable port near the floor; the other '
              'end stands on an open frame of stainless round tubes with walnut-sleeved posts, clamp collars, a brushed steel '
              'panel between the posts and two low rails; a square steel stretcher runs along the floor between the two ends; '
              'set flush into the top: a small stainless sink with a basket, a slotted drip tray, and an induction kettle plate'),
    'host': ('an armchair with a slender brushed stainless round-tube frame and slightly splayed legs, round disc bolts at the '
             'seat corners, walnut armrests with stainless end collars, walnut stretchers low between front and back legs, a '
             'walnut-brown saddle-leather sling back with contrast top-stitching hung between two capped posts, and a seat of '
             'cream cotton webbing in a basket weave'),
    'guest': ('an armchair on four straight vertical stainless round-tube legs with collars, walnut stretchers in an H pattern '
              'joined by stainless T-joints, a cream cotton webbing seat on a bent-tube seat frame, a walnut-brown leather back '
              'held by two hairpin-bent stainless tube loops with rivets and a buckled strap at the back, two walnut back posts, '
              'and walnut armrests carried on V-shaped stainless braces that meet at a large round disc hub at each side of the seat'),
    'twin': ('a two-seat bench: two low lounge seats, each with a walnut-brown saddle-leather sling back and a cream cotton '
             'webbing seat, walnut armrests on the outer sides only, joined in the middle by a square walnut side table with a '
             'slatted walnut lower shelf, all on one continuous brushed stainless round-tube frame with round disc joints and '
             'walnut-sleeved low rails'),
    'shelf': ('a freestanding display shelf: two pointed crescent-shaped end frames of curved brushed stainless tube, each '
              'wrapped in cream translucent mulberry-paper fabric gathered at the bottom into a small dark steel foot plate, a '
              'straight stainless post at the back of each end, and four fluted (reeded) glass shelves held by cylindrical clamp '
              'collars, open back'),
    'lamp': ('a tall pendant lamp hung from a thin steel cable: four square stainless rods form the corners and extend above and '
             'below the body, five tiers of square stainless cross-bar frames, two long bands of cream paper-veneer folded in '
             'zig-zags weaving through the tiers, warm light glowing from translucent panels inside'),
}
REF = {
    'table': '参考图：有节茶室-茶桌（俯视 3/4 那张）',
    'host': '参考图：有节茶室-主椅（3/4 那张）',
    'guest': '参考图：有节茶室-客椅（V 形扶手 3/4 那张）',
    'twin': '参考图：有节茶室-双人椅（3/4 那张）',
    'shelf': '参考图：有节茶室-架子（3/4 那张）',
    'lamp': '参考图：Gemini_Generated_Image（吊灯）',
}
NUM = {'table': '01', 'host': '02', 'guest': '03', 'twin': '04', 'shelf': '05', 'lamp': '06'}

def views(k):
    return (f'Technical orthographic drawing of {ANCHOR[k]}: front elevation, side elevation and top plan on one sheet, '
            'thin black hairlines on pure white, dimension lines in millimetres, small sans-serif labels FRONT VIEW / SIDE VIEW / '
            'TOP VIEW, architectural drafting style, no shading --ar 3:2')

EXPLODE = {
    'table': 'walnut top lifted above the frame, sink, drip tray and kettle plate lifted out of their cut-outs, pedestal cabinet and tube frame separated along their axes',
    'host': 'leather sling back, webbing seat and walnut armrests lifted off the tube frame, disc bolts and collars separated',
    'guest': 'leather back and hairpin loops lifted off, V-braces and disc hubs separated from the seat frame, H-stretchers and T-joints spaced apart',
    'twin': 'both leather backs and webbing seats lifted off, walnut table top and slatted shelf separated, the shared tube frame and disc joints spaced apart',
    'shelf': 'four fluted glass shelves lifted out, fabric sleeves slid off the curved end frames, collars and foot plates separated',
    'lamp': 'the five cross-bar tiers spaced apart along the four rods, the two folded bands lifted away, the light source in the centre',
}
def exploded(k):
    return (f'Exploded axonometric product render of {ANCHOR[k]}: {EXPLODE[k]}, with thin dashed alignment lines, every joint '
            'visible, floating on a seamless pure white background, soft studio light, centred with generous margins --ar 4:5')

# close-ups: (subject for the prompt, CN label, EN label)
DETAIL = {
    'table': [('the stainless sink, slotted drip tray and induction kettle plate set flush into the walnut tabletop', '嵌入水槽、茶盘与烧水位', 'Inset sink, tray and kettle plate'),
              ('the brushed stainless-steel pedestal cabinet with its access door and round cable port, meeting the floor stretcher', '不锈钢立柜与线孔', 'Steel pedestal and cable port'),
              ('a walnut-sleeved tube post gripped by a stainless clamp collar beside the steel side panel', '胡桃木套杆与套环', 'Walnut-sleeved post and collar')],
    'host': [('the walnut-brown leather sling wrapping a capped steel post, contrast top-stitching', '皮革吊带靠背', 'Leather sling back'),
             ('the cream cotton webbing seat, basket-weave texture and tension', '棉编带座面', 'Cotton-webbing seat'),
             ('a round disc bolt joint where the seat rail meets the leg', '圆盘螺栓节点', 'Disc-bolt joint')],
    'guest': [('the V-shaped arm braces meeting the round disc hub at the side of the seat', 'V 形扶手撑与圆盘', 'V-brace and disc hub'),
              ('the riveted leather back and buckled strap seen from behind', '铆钉皮背与扣带', 'Riveted back and strap'),
              ('a stainless T-joint holding the walnut H-stretchers', 'T 形接头与 H 形横撑', 'T-joint and H-stretchers')],
    'twin': [('the slatted walnut lower shelf under the centre table', '胡桃木格栅下层', 'Slatted walnut shelf'),
             ('a round disc joint linking the seat frame and the table frame', '圆盘连接节点', 'Disc joint'),
             ('the leather sling back seam and the walnut armrest end cap', '皮革靠背与扶手端头', 'Leather back and arm cap')],
    'shelf': [('the mulberry-paper fabric gathered at the dark steel foot plate, fibres visible', '织面收口与底板', 'Gathered fabric and foot plate'),
              ('a fluted glass shelf edge held by a clamp collar on the curved tube', '长虹玻璃与套环', 'Fluted glass and collar'),
              ('the pointed tip of the crescent frame with the fabric pulled taut, backlit', '弯杆尖端', 'Crescent tip')],
    'lamp': [('a folded paper-veneer band glowing with warm light, grain visible', '发光折面', 'Glowing folded band'),
             ('a square cross-bar frame clamped to a corner rod', '井字横框与方杆', 'Cross-bar tier and rod'),
             ('the square rod ends projecting below the lamp body, warm light above', '下伸杆端', 'Rod ends below')],
}
def detail(k, i):
    return (f'Macro close-up of {DETAIL[k][i][0]}; materials exactly as the reference image; shallow depth of field, soft raking '
            'side light, warm neutral tones, tightly cropped, no text --ar 1:1')

SCENE = {
    'table': ('in a quiet tea room with lime-plaster walls and a timber lattice window, morning light across the walnut top, a white tea set on the drip tray and a steel kettle on the plate, editorial interior photograph, eye-level 35mm, generous negative space above',
              'three-quarter close view at dusk, steam rising from the kettle, a hand pouring tea (face not visible), warm low light, shallow depth of field'),
    'host': ('at the head of a long walnut tea table under a covered timber veranda, dappled sunlight through leaves, lake glimpsed beyond, editorial interior photograph, eye-level 35mm',
             'beside a tall window, bamboo shadows moving across a plaster wall, a single cup on a small side table, calm afternoon light'),
    'guest': ('a pair facing each other across a low walnut table in a minimal plaster-walled tea room, soft afternoon light, editorial interior photograph',
              'in a quiet corner with a single branch in a celadon vase, long gentle shadow'),
    'twin': ('on a wide timber deck facing a calm lake, two tea cups on the centre table, early morning mist, editorial photograph',
             'under deep timber eaves during light rain, wet stone courtyard beyond, soft grey light'),
    'shelf': ('against a lime-plaster wall holding tea caddies, celadon bowls and a few books, soft side light, editorial interior photograph',
              'used as a semi-transparent partition between a tea room and a corridor, backlit by afternoon sun so the paper panels glow'),
    'lamp': ('hanging low above a walnut tea table at dusk, the room dark except for its warm glow and a faint reflection on the table',
             'two lamps at different heights against a rough stone wall, evening, warm light pooling below'),
}
def scene(k, i):
    ar = '--ar 2:3' if i == 0 else '--ar 4:5'
    return f'{ANCHOR[k][0].upper() + ANCHOR[k][1:]}, {SCENE[k][i]}, {STYLE}. {NEG} {ar}'

def sketch(k):
    return (f"Designer's pencil sketch sheet of {ANCHOR[k]}: one large three-quarter perspective and two small thumbnail studies "
            'of its key joints, fine graphite lines with light construction lines and subtle hatching, on plain white paper, no text --ar 3:2')

ANGLE = {
    '03-A': ('guest', '补正面角度 · 4:5 · 1600×2000', 4 / 5,
             'Studio product photograph of {a}, straight front view at seat height, isolated on a seamless pure white background, centred, filling 85% of the frame height, soft contact shadow --ar 4:5',
             '正面', 'Front'),
    '06-A1': ('lamp', '补侧面角度 · 1:2 · 1000×2000', 1 / 2,
              'Studio product photograph of {a}, rotated 45 degrees, lit, isolated on a seamless pure white background, centred, filling 85% of the frame height --ar 1:2',
              '侧面', 'Side'),
    '06-A2': ('lamp', '补仰视角度 · 1:1 · 1200×1200', 1.0,
              'Studio product photograph looking straight up into {a} from below, the folded bands and glowing core visible, pure white background --ar 1:1',
              '仰视', 'From Below'),
}

SERIES = {
    '00-B': ('材质板 · 1:1 · 2000×2000', '参考图：任意一张单品渲染（看材质）',
             'Flat-lay material board, top-down: overlapping square swatches of walnut wood, brushed stainless-steel plate, '
             'walnut-brown saddle leather with contrast top-stitching, cream cotton webbing in basket weave, fluted glass, and cream '
             'translucent mulberry paper, loose diagonal cluster, soft shadow, on white paper, no text --ar 1:1'),
    '00-M1': ('大场景 · 临水廊下 · 16:9 · 3200×1800', '参考图：六件单品的渲染（可多图参考）',
              'The complete Nodes in Order tea furniture collection — a long walnut tea table with a stainless pedestal cabinet, a '
              'host armchair with a leather sling back, two guest armchairs with V-braced walnut arms, a two-seat bench with a walnut '
              'centre table, a crescent-framed paper display shelf and a tall folded-paper pendant lamp — set as one tea setting for '
              f'five under a covered timber veranda beside a lake, afternoon light, wide shot 24mm, {STYLE}. {NEG} --ar 16:9'),
    '00-M2': ('大场景 · 傍晚室内 · 16:9 · 3200×1800', '参考图：六件单品的渲染（可多图参考）',
              'The Nodes in Order tea furniture collection — long walnut tea table with a stainless pedestal cabinet, leather '
              'sling-back host chair, two V-braced guest chairs, two-seat bench with walnut centre table, crescent paper shelf, '
              'folded-paper pendant lamp — arranged in a timber-framed tea room at dusk, only the pendant lamp glowing, windows '
              f'showing a blue evening garden, wide shot, {STYLE}. {NEG} --ar 16:9'),
    '00-M3': ('大场景 · 雨天庭院俯视 · 16:9 · 3200×1800（可选）', '参考图：六件单品的渲染（可多图参考）',
              'High-angle view down into a small Jiangnan courtyard pavilion in light rain, the full Nodes in Order collection '
              '(walnut tea table with steel pedestal, leather sling chairs, two-seat bench, crescent paper shelf, folded pendant '
              f'lamp) set for five under the eaves, wet stone paving, a maple tree, calm grey light, {STYLE}. {NEG} --ar 16:9'),
}

MATERIALS = [
    ('胡桃木', 'Walnut', '台面、扶手、横撑、中几', 'Tops, armrests, stretchers, centre table'),
    ('拉丝不锈钢', 'Brushed stainless steel', '杆架、套环、立柜', 'Frames, collars, pedestal'),
    ('胡桃棕皮革', 'Walnut-brown leather', '主位、客位与并坐的靠背', 'Chair and bench backs'),
    ('棉编带', 'Cotton webbing', '三种座面', 'All three seats'),
    ('长虹玻璃', 'Fluted glass', '展示架层板', 'Shelf boards'),
    ('纤维纸面', 'Fibre and paper panels', '展示架侧面、吊灯折面', 'Shelf sides, lamp bands'),
]
