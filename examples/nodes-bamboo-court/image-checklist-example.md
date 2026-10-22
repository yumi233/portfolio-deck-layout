# 图片补全清单 — 有节 · 竹院 Nodes · Bamboo Court

对照参考稿的标准配图，v24 的调研、定位与设计部分不缺图。**缺口集中在「效果呈现」**：
- 每件单品只有草图和一张白底渲染，没有三视图、爆炸图、材质特写和单品场景；
- 全系列只有一张大场景（临水共饮），没有材质板。

下面列出要补的图，以及每张的提示词。

---

## 1. 缺图总览

| | 白底渲染 | 草图 | 三视图 | 爆炸图 | 材质特写 ×3 | 场景 ×2 |
|---|---|---|---|---|---|---|
| 茶台 Tea Table | ✓ | ✓ | 缺 | 缺 | 只有裁切 | 缺 |
| 主位椅 Host Chair | ✓ | ✓ | 缺 | 缺 | 只有裁切 | 缺 |
| 客位椅 Guest Chair | ✓ | ✓ | 缺 | 缺 | 只有裁切 | 缺 |
| 并坐连坐 Twin Seat | ✓ | ✓ | 缺 | 缺 | 只有裁切 | 缺 |
| 展示架 Display Shelf | ✓ | ✓ | 缺 | 缺 | 只有裁切 | 缺 |
| 折光吊灯 Folded Light | ✓ | ✓ | 缺 | 缺 | 只有裁切 | 缺 |

| 全系列 | 状态 |
|---|---|
| 系列合影（封面） | 用 6 张单品抠图拼成，可以用；有真实的 45° 俯视合影会更好（可选） |
| 材质板 | 缺 |
| 大场景 | 现有 1 张（临水共饮），还缺 2 张 |

「只有裁切」：第 23、25 页的材料和节点图是从渲染图里裁出来的局部，放大后清晰度不够，建议补真正的特写。

**补齐后新增的页**：
- 每件单品在渲染页后加 3 页：
  - **视图页（I）**：渲染图 + 三视图
  - **细节页（J）**：3 张特写 + 爆炸图
  - **场景页（K）**：两张图上下错落
- 「临水共饮」之后加 2 张大场景（M）。
- 第 26 页「系列」右侧放材质板（L）。

合计约新增 20 页，全稿约 71 页。

---

## 2. 通用设置

**全套风格锚点**（每条提示词末尾都粘上）：
```
contemporary Chinese tea furniture, slender brushed stainless-steel tube frames joined by cylindrical clamp collars like bamboo nodes, warm walnut wood, walnut-brown leather, natural rattan cane, ivory woven webbing, translucent cream fibre panels; soft natural daylight, muted low-saturation warm palette, quiet minimal oriental atmosphere
```

**通用负面词**：
```
text, watermark, logo, signature, extra legs, warped or melted joints, distorted proportions, cluttered props, oversaturated colours, plastic look, CGI artefacts, people facing camera
```

**造型一致性**：AI 很容易把杆件、节点、腿数画错，所以：
1. **每张都把对应单品的白底渲染当参考图**（`cut_*.png` 或原稿的白底渲染）。
   - Midjourney：把图片链接放在提示词最前面，加 `--iw 1.5`。
   - 即梦 / 可灵：参考图强度设 0.35–0.5。
   - GPT-image / Gemini：用编辑模式，写「保持家具造型和材质完全不变，只把背景换成……」。
2. **三视图和爆炸图优先从 3D 模型导出**（Rhino Make2D、SketchUp LayOut、KeyShot 拆件渲染），尺寸才准确。AI 版本只能当风格示意。
3. **生成后逐张核对**：杆件数量、节点位置、腿数、皮革和木材的位置。

**交回方式**：
- 文件放在同一个文件夹里，按 `序号_产品_类型_a/b.png` 命名。
- 类型取值：views / exploded / detail / scene / board / bigscene / family。
- 例：`02_host-chair_scene_a.png`。
- 交回后我会抠图、排进 I、J、K、L、M 页，并重新出 PDF 逐页检查。

**尺寸**（都比排版尺寸大一倍以上）：

| 类型 | 比例 | 像素 | 备注 |
|---|---|---|---|
| 三视图 | 3:2 | 2400×1600 | 透明或白底 |
| 爆炸图 | 4:5 | 1600×2000 | |
| 特写 | 1:1 | 1200×1200 | |
| 场景 a | 2:3 | 1600×2400 | 竖图 |
| 场景 b | 4:5 | 1600×2000 | |
| 大场景 | 16:9 | 3200×1800 | |
| 材质板 | 1:1 | 2000×2000 | |

---

## 3. 逐件提示词

### 3.1 茶台 Tea Table（放在第 30 页之后）
造型锚点：
```
a long rectangular tea table with a thick walnut top and a stainless-steel tea tray with drainage slots inset at its centre; one end stands on a single brushed stainless-steel slab leg (a flat vertical panel with a small round cable port), the other end on two slender brushed-steel tube legs joined by a low tube stretcher with clamp-collar joints
```

| 编号 | 用途 | 比例 | 来源 |
|---|---|---|---|
| 01-V | 视图页（I）：正视 / 侧视 / 俯视三视图 | 3:2 | **3D 导出** |
| 01-X | 细节页（J）：爆炸图 | 4:5 | 3D 拆件优先 |
| 01-D1–D3 | 细节页（J）：特写 ×3 | 1:1 | AI 或渲染 |
| 01-Sa / Sb | 场景页（K） | 2:3 / 4:5 | AI |

**01-V 三视图**（AI 只做风格示意）
```
Technical orthographic drawing of [锚点]: front elevation, side elevation and top plan on one sheet, thin black hairlines on white, dimension lines in millimetres (length 2400, depth 800, height 750), small sans-serif labels FRONT VIEW / SIDE VIEW / TOP VIEW, architectural drafting style, no shading --ar 3:2
```
（尺寸数字请换成真实尺寸。）

**01-X 爆炸图**
```
Exploded axonometric product render of [锚点], walnut top lifted above the frame, inset tea tray lifted out of its recess, slab leg and tube legs separated along their axes with thin dashed alignment lines, clamp collars visible, floating on seamless white, soft studio light --ar 4:5
```

**01-D1 / D2 / D3 特写**
```
Macro close-up of the stainless-steel tea tray with drainage slots set flush into the walnut tabletop, [锚点], shallow depth of field, soft raking side light, warm neutral tones --ar 1:1
```
```
Macro close-up where the brushed stainless-steel slab leg meets the underside of the thick walnut top, showing the small round cable port, [锚点], soft side light --ar 1:1
```
```
Macro close-up of a brushed-steel clamp collar joining a tube leg to the low stretcher, [锚点], shallow depth of field --ar 1:1
```

**01-Sa 场景（竖图）**
```
[锚点] in a quiet tea room with lime-plaster walls and a timber lattice window, morning light falling across the walnut top, a simple tea set on the inset tray, editorial interior photograph, eye-level 35mm, generous negative space above, [风格锚点] --ar 2:3
```
**01-Sb 场景**
```
Three-quarter close view of [锚点] at dusk, steam rising from an iron kettle, a hand pouring tea (face not visible), warm low light, shallow depth of field, [风格锚点] --ar 4:5
```

### 3.2 主位椅 Host Chair（放在第 33 页之后）
造型锚点：
```
an armchair with a slender brushed stainless-steel tube frame and cylindrical clamp-collar joints, a gently upswept crest rail wrapped in walnut-brown leather in the manner of a Ming official's-hat chair, leather-wrapped armrests and a leather seat cushion
```
- **02-V 三视图**：用 01-V 的模板，锚点换成本件，尺寸写真实尺寸。
- **02-X 爆炸图**：
```
Exploded axonometric render of [锚点], leather crest rail, armrests and seat cushion lifted off the tube frame, clamp collars separated at each joint with dashed alignment lines, white background --ar 4:5
```
- **02-D1–D3 特写**：
```
Macro close-up of the leather-wrapped crest rail end meeting a steel tube post with a clamp collar, [锚点] --ar 1:1
```
```
Macro close-up of the top-stitched seam along the walnut-brown leather seat edge, [锚点] --ar 1:1
```
```
Macro close-up of a brushed-steel clamp-collar corner joint where armrest tube meets the front post, [锚点] --ar 1:1
```
- **02-Sa 场景**：
```
[锚点] standing alone at the head of a long walnut tea table under a covered timber veranda, dappled sunlight through leaves, lake glimpsed beyond, [风格锚点] --ar 2:3
```
- **02-Sb 场景**：
```
[锚点] beside a tall window, shadows of bamboo moving across a plaster wall, a single cup on a small side table, calm afternoon light, [风格锚点] --ar 4:5
```

### 3.3 客位椅 Guest Chair（放在第 36 页之后）
造型锚点：
```
a round-back style armchair with bent brushed-steel tube arms and frame, clamp-collar joints, a curved walnut back panel, and a seat of wide ivory woven webbing in a loose checker pattern
```
- **03-V 三视图**：同 01-V 的模板。
- **03-X 爆炸图**：
```
Exploded axonometric render of [锚点], walnut back panel and webbing seat frame lifted away from the bent tube structure, collars separated with dashed lines, white background --ar 4:5
```
- **03-D1–D3 特写**：
```
Macro close-up of the curved walnut back panel fixed to a bent steel tube, end grain and edge detail, [锚点] --ar 1:1
```
```
Macro close-up of the ivory woven webbing seat, interlaced texture and tension, soft side light, [锚点] --ar 1:1
```
```
Macro close-up of the bent tube armrest curve flowing into a clamp-collar joint, [锚点] --ar 1:1
```
- **03-Sa 场景**：
```
A pair of [锚点] facing each other across a low walnut table in a minimal plaster-walled tea room, soft afternoon light, [风格锚点] --ar 2:3
```
- **03-Sb 场景**：
```
[锚点] in a quiet corner with a single branch in a ceramic vase, long gentle shadow, [风格锚点] --ar 4:5
```

### 3.4 并坐连坐 Twin Seat（放在第 39 页之后）
造型锚点：
```
a two-seat bench: two low lounge seats with natural rattan cane woven seats and backs, joined by a small walnut side table with a slatted lower shelf in the middle, all on one continuous brushed stainless-steel tube frame with clamp-collar joints
```
- **04-V 三视图**：同 01-V 的模板。
- **04-X 爆炸图**：
```
Exploded axonometric render of [锚点], rattan seat and back panels lifted off, walnut table top and slatted shelf separated, shared cross rail and collars spaced along dashed lines, white background --ar 4:5
```
- **04-D1–D3 特写**：
```
Macro close-up of the natural rattan cane weave of the seat, [锚点] --ar 1:1
```
```
Macro close-up of the walnut centre table with its slatted lower shelf, [锚点] --ar 1:1
```
```
Macro close-up of the shared steel cross rail with clamp collars linking seat, table and seat, [锚点] --ar 1:1
```
- **04-Sa 场景**：
```
[锚点] on a wide wooden deck facing a calm lake, two tea cups on the centre table, early morning mist, [风格锚点] --ar 2:3
```
- **04-Sb 场景**：
```
[锚点] under deep timber eaves during light rain, wet stone courtyard beyond, soft grey light, [风格锚点] --ar 4:5
```

### 3.5 展示架 Display Shelf（放在第 42 页之后）
造型锚点：
```
a freestanding display shelf with two crescent-shaped end frames of curved brushed-steel tube, each filled with a pale cream woven fabric panel, and four frosted translucent glass shelves between them, open back
```
- **05-V 三视图**：同 01-V 的模板。
- **05-X 爆炸图**：
```
Exploded axonometric render of [锚点], four glass shelves lifted out, fabric panels separated from the curved tube end frames, collars and brackets visible, white background --ar 4:5
```
- **05-D1–D3 特写**：
```
Macro close-up of the cream woven fabric panel stretched inside the curved steel tube, light passing through the weave, [锚点] --ar 1:1
```
```
Macro close-up of a frosted glass shelf edge resting on a clamp-collar bracket, [锚点] --ar 1:1
```
```
Macro close-up of the curved tube end frame meeting the floor, [锚点] --ar 1:1
```
- **05-Sa 场景**：
```
[锚点] against a lime-plaster wall holding tea caddies, celadon bowls and a few books, soft side light, [风格锚点] --ar 2:3
```
- **05-Sb 场景**：
```
[锚点] used as a semi-transparent partition between a tea room and a corridor, backlit by afternoon sun so the fabric panels glow, [风格锚点] --ar 4:5
```

### 3.6 折光吊灯 Folded Light（放在第 45 页之后）
造型锚点：
```
a tall vertical pendant lamp made of short cream translucent fibre panels folded in alternating zig-zag directions, threaded along four slim silver steel rods with clamp collars, glowing warm from within
```
- **06-V 三视图**：同 01-V 的模板（正视、侧视、仰视）。
- **06-X 爆炸图**：
```
Exploded axonometric render of [锚点], folded panels spaced apart along the rods, collars and the light source visible in the centre, dashed alignment lines, white background --ar 4:5
```
- **06-D1–D3 特写**：
```
Macro close-up of a folded fibre panel edge glowing with warm light, paper texture visible, [锚点] --ar 1:1
```
```
Macro close-up of a clamp collar gripping a silver rod between panels, [锚点] --ar 1:1
```
```
Looking up into the lamp from below, layered folded panels and warm core, [锚点] --ar 1:1
```
- **06-Sa 场景**：
```
[锚点] hanging low above a walnut tea table at dusk, the room dark except for its warm glow and a faint reflection on the table, [风格锚点] --ar 2:3
```
- **06-Sb 场景**：
```
Two [锚点] at different heights against a rough stone wall, evening, warm light pooling below, [风格锚点] --ar 4:5
```

---

## 4. 全系列

**00-B 材质板**（放进第 26 页「系列」右侧）
```
Flat-lay material board, top-down: overlapping square swatches of walnut wood, brushed stainless-steel plate, walnut-brown leather with top-stitching, natural rattan cane weave, ivory woven webbing and cream translucent fibre paper, loose diagonal cluster, soft shadow, on white paper --ar 1:1
```

**00-M1 大场景：傍晚室内**（放在第 46 页之后）
```
The complete Nodes · Bamboo Court tea furniture collection — long walnut tea table, host armchair with leather crest rail, two guest chairs with walnut backs, rattan twin seat with centre table, crescent-framed display shelf, folded pendant lamp — arranged as one tea setting in a timber-framed tea room at dusk, only the pendant lamp glowing, windows showing a blue evening garden, wide shot 24mm, [风格锚点] --ar 16:9
```

**00-M2 大场景：雨天庭院俯视**
```
High-angle view looking down into a small Jiangnan courtyard pavilion in light rain, the full tea furniture collection set for five people under the eaves, wet stone paving, a maple tree, calm grey light, [风格锚点] --ar 16:9
```

**00-F 系列合影**（可选，替换封面上的拼图）
```
All pieces of the Nodes · Bamboo Court collection arranged loosely on a seamless white floor, 45-degree high-angle view, soft overhead studio light, gentle shadows, catalogue still life, generous spacing --ar 3:2
```

---

## 5. 优先级建议
1. **先补每件单品的场景 a**（6 张）。它最能拉开和参考稿的差距，也最容易用 AI 做好。
2. **再补材质板和 2 张大场景**。
3. **特写**：能从高清渲染里重新出就重新出；没有渲染源再用 AI。
4. **三视图和爆炸图**：从 3D 模型导出，尺寸要真实；用 AI 只能做示意。
