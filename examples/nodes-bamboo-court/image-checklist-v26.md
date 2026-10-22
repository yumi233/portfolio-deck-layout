# 图片补全清单 — 节序 Nodes in Order（v26 待补图版）

v25 已经换上你这次给的 16 张新渲染图。**v26（待补图版）** 在 v25 的基础上，把下面每一张缺的图都留好了位置。

下面是 **还没有可用图片** 的部分。以 v26 的页码为准。

---

## 1. 缺图总览

| | 白底渲染 | 多角度 | 草图（形态推敲） | 三视图 + 尺寸 | 爆炸图 | 材质特写 ×3 | 场景 ×2 |
|---|---|---|---|---|---|---|---|
| 围炉 · 茶台 | ✓ | ✓ 正、背、俯 | **旧稿** | 缺 | 缺 | 仅裁切 | 缺 |
| 东道 · 主位椅 | ✓ | ✓ 正、侧、背、3/4 | **旧稿** | 缺 | 缺 | 仅裁切 | 缺 |
| 西宾 · 客位椅 | ✓ | 缺正面 | **旧稿** | 缺 | 缺 | 仅裁切 | 缺 |
| 比肩 · 并坐连坐 | ✓ | ✓ 三视合图 | **旧稿** | 缺尺寸 | 缺 | 仅裁切 | 缺 |
| 藏器 · 展示架 | ✓ | ✓ 正、侧、3/4 | ✓ 与新图一致 | 缺 | 缺 | 仅裁切 | 缺 |
| 秉烛 · 折光吊灯 | ✓ | 缺侧面、仰视 | ✓ 与新图一致 | 缺 | 缺 | 仅裁切 | 缺 |

| 全系列 | 状态 |
|---|---|
| 系列合影（封面） | 用新抠图拼成，可以用；有一张真实的 45° 俯视合影会更好（可选） |
| 材质板 | 缺 |
| 大场景 | **旧稿**（第 21、71、76 页的场景里是旧版家具） |

**说明**：
- **旧稿**：图还在 PPT 里，但画的是旧版家具，造型和新渲染对不上。
  - 第 30、37、44、51 页的形态推敲草图：旧茶台是板脚，旧主位椅是包覆搭脑，旧客位椅是圈椅，旧并坐是藤编。
  - 第 21、71、76 页的场景图：旧版藤编家具。
  - 你说场景先不换，所以这几页暂时保留；下面给了重新生成的提示词。
- **仅裁切**：第 23、25 页的材质、节点图是从新渲染图里裁的局部，能用，但放大后细节不够，有真特写更好。

**v26 已经把位置留好了**：每一张缺的图都在 v26 里有一个灰色虚线框，框里写着编号、比例、像素、参考图和完整提示词。页码见本文末尾的「编号 → 页码」表。
---

## 2. 通用设置

**全套风格锚点**（粘在每条场景、氛围类提示词末尾）：
```
contemporary Chinese tea furniture, brushed stainless-steel round tubes joined by cylindrical clamp collars and round disc bolts like bamboo nodes, warm walnut, walnut-brown saddle leather with contrast top-stitching, cream cotton webbing in a basket weave, fluted glass, cream translucent mulberry-paper panels; soft natural daylight, muted low-saturation warm palette, quiet minimal oriental atmosphere
```

**通用负面词**：
```
text, watermark, logo, signature, extra legs, warped or melted joints, wrong number of tubes, distorted proportions, rattan, cane, cluttered props, oversaturated colours, plastic look, CGI artefacts, people facing camera
```
（加 rattan / cane 是为了防止模型照着旧场景画出藤编。）

**保持造型一致**：
1. 每张都用对应单品的新渲染作参考图：
   - Midjourney：图片链接放提示词最前面，加 `--iw 1.5–2`。
   - 即梦 / 可灵：参考图强度 0.4–0.5。
   - Gemini / GPT-image：用编辑模式，写「家具造型、材质、比例完全不变，只换背景为……」。这样最稳。
2. 三视图、爆炸图优先从 3D 模型导出，尺寸才准；AI 版只当风格示意。
3. 生成后逐张核对：管子数量、套环位置、腿数、皮革和木头的位置。

**交回方式**：
- 放进同一个文件夹，命名 `序号_英文名_类型_a/b.png`。
- 英文名：hearthside / east-seat / west-seat / shoulder / vessel-keeper / candlelight。
- 类型：sketch / views / exploded / detail / scene / board / bigscene / family / angle。
- 例：`02_east-seat_scene_a.png`。

**尺寸**：

| 类型 | 比例 | 像素 |
|---|---|---|
| 草图 | 3:2 | 2400×1600 |
| 三视图 | 3:2 | 2400×1600 |
| 爆炸图 | 4:5 | 1600×2000 |
| 特写 | 1:1 | 1200×1200 |
| 场景 a | 2:3 | 1600×2400 |
| 场景 b | 4:5 | 1600×2000 |
| 大场景 | 16:9 | 3200×1800 |
| 材质板 | 1:1 | 2000×2000 |

---

## 3. 逐件提示词

### 3.1 围炉 · 茶台 Hearthside（第 29–35 页）
造型锚点：
```
a long tea table with a thick walnut top with softly bevelled edges; one end stands on a tall brushed stainless-steel pedestal cabinet with a small access door and a round cable port near the floor; the other end stands on an open frame of stainless round tubes with walnut-sleeved posts, clamp collars, a brushed steel panel between the posts and two low rails; a square steel stretcher runs along the floor between the two ends; set flush into the top: a small stainless sink with a basket, a slotted drip tray, and an induction kettle plate
```

| 编号 | 用途 | 比例 | 来源 |
|---|---|---|---|
| 01-K | 形态推敲草图（替换第 30 页旧稿） | 3:2 | AI 或手绘 |
| 01-V | 三视图（I） | 3:2 | **3D 导出** |
| 01-X | 爆炸图（J） | 4:5 | 3D 拆件优先 |
| 01-D1–D3 | 特写 ×3（J） | 1:1 | AI 或局部渲染 |
| 01-Sa / Sb | 场景（K） | 2:3 / 4:5 | AI |

**01-K 形态推敲草图**
```
Designer's pencil sketch sheet of [锚点]: one large three-quarter perspective and two small thumbnail studies of the pedestal end and the tube-frame end, fine graphite lines with light construction lines and subtle hatching, on plain white paper, no text --ar 3:2
```

**01-V 三视图**（尺寸换成真实数据）
```
Technical orthographic drawing of [锚点]: front elevation, side elevation and top plan on one sheet, thin black hairlines on white, dimension lines in millimetres, small sans-serif labels FRONT VIEW / SIDE VIEW / TOP VIEW, architectural drafting style, no shading --ar 3:2
```

**01-X 爆炸图**
```
Exploded axonometric render of [锚点]: walnut top lifted above the frame, sink, drip tray and kettle plate lifted out of their cut-outs, pedestal cabinet and tube frame separated along their axes with thin dashed alignment lines, clamp collars visible, floating on seamless white, soft studio light --ar 4:5
```

**01-D1 / D2 / D3 特写**
```
Macro close-up of the stainless sink, slotted drip tray and induction plate set flush into the walnut tabletop, [锚点], shallow depth of field, soft raking light --ar 1:1
```
```
Macro close-up of the brushed stainless-steel pedestal cabinet with its access door and round cable port, meeting the floor stretcher, [锚点] --ar 1:1
```
```
Macro close-up of a walnut-sleeved tube post gripped by a stainless clamp collar beside the steel side panel, [锚点] --ar 1:1
```

**01-Sa 场景（竖图）**
```
[锚点] in a quiet tea room with lime-plaster walls and a timber lattice window, morning light across the walnut top, a white tea set on the drip tray and a steel kettle on the plate, editorial interior photograph, eye-level 35mm, generous negative space above, [风格锚点] --ar 2:3
```

**01-Sb 场景**
```
Three-quarter close view of [锚点] at dusk, steam rising from the kettle, a hand pouring tea (face not visible), warm low light, shallow depth of field, [风格锚点] --ar 4:5
```

### 3.2 东道 · 主位椅 East Seat（第 36–42 页）
造型锚点：
```
an armchair with a slender brushed stainless round-tube frame and slightly splayed legs, round disc bolts at the seat corners, walnut armrests with stainless end collars, walnut stretchers low between front and back legs, a walnut-brown saddle-leather sling back with contrast top-stitching hung between two capped posts, and a seat of cream cotton webbing in a basket weave
```
- **02-K 形态推敲草图**（替换第 37 页旧稿）：用 01-K 的模板，锚点换成本件，thumbnails 写 "the sling back and the armrest joint"。
- **02-V 三视图**：用 01-V 的模板。
- **02-X 爆炸图**：
```
Exploded axonometric render of [锚点]: leather sling back, webbing seat and walnut armrests lifted off the tube frame, disc bolts and collars separated with dashed alignment lines, white background --ar 4:5
```
- **02-D1–D3 特写**：
```
Macro close-up of the walnut-brown leather sling wrapping a capped steel post, contrast top-stitching, [锚点] --ar 1:1
```
```
Macro close-up of the cream cotton webbing seat, basket-weave texture and tension, soft side light, [锚点] --ar 1:1
```
```
Macro close-up of a round disc bolt joint where the seat rail meets the leg, [锚点] --ar 1:1
```
- **02-Sa 场景**：
```
[锚点] at the head of a long walnut tea table under a covered timber veranda, dappled sunlight through leaves, lake glimpsed beyond, [风格锚点] --ar 2:3
```
- **02-Sb 场景**：
```
[锚点] beside a tall window, bamboo shadows moving across a plaster wall, a single cup on a small side table, calm afternoon light, [风格锚点] --ar 4:5
```

### 3.3 西宾 · 客位椅 West Seat（第 43–49 页）
造型锚点：
```
an armchair on four straight vertical stainless round-tube legs with collars, walnut stretchers in an H pattern joined by stainless T-joints, a cream cotton webbing seat on a bent-tube seat frame, a walnut-brown leather back held by two hairpin-bent stainless tube loops with rivets and a buckled strap at the back, two walnut back posts, and walnut armrests carried on V-shaped stainless braces that meet at a large round disc hub at each side of the seat
```
- **03-A 正面角度**：在第 46 页多角度页补正面。最好用渲染软件出；AI 只能在参考图上换角度。
```
Studio product photograph of [锚点], straight front view at seat height, isolated on a seamless light grey background, soft diffused light, faint contact shadow --ar 16:9
```
- **03-K 形态推敲草图**（替换第 44 页旧稿）：用 01-K 的模板，thumbnails 写 "the V-brace arm and the hairpin back loop"。
- **03-V 三视图**：用 01-V 的模板。
- **03-X 爆炸图**：
```
Exploded axonometric render of [锚点]: leather back and hairpin loops lifted off, V-braces and disc hubs separated from the seat frame, H-stretchers and T-joints spaced along dashed lines, white background --ar 4:5
```
- **03-D1–D3 特写**：
```
Macro close-up of the V-shaped arm braces meeting the round disc hub at the side of the seat, [锚点] --ar 1:1
```
```
Macro close-up of the riveted leather back and buckled strap seen from behind, [锚点] --ar 1:1
```
```
Macro close-up of a stainless T-joint holding the walnut H-stretchers, [锚点] --ar 1:1
```
- **03-Sa 场景**：
```
A pair of [锚点] facing each other across a low walnut table in a minimal plaster-walled tea room, soft afternoon light, [风格锚点] --ar 2:3
```
- **03-Sb 场景**：
```
[锚点] in a quiet corner with a single branch in a celadon vase, long gentle shadow, [风格锚点] --ar 4:5
```

### 3.4 比肩 · 并坐连坐 Shoulder to Shoulder（第 50–56 页）
造型锚点：
```
a two-seat bench: two low lounge seats, each with a walnut-brown saddle-leather sling back and a cream cotton webbing seat, walnut armrests on the outer sides only, joined in the middle by a square walnut side table with a slatted walnut lower shelf, all on one continuous brushed stainless round-tube frame with round disc joints and walnut-sleeved low rails
```
- **04-K 形态推敲草图**（替换第 51 页旧稿，旧稿是藤编版）：用 01-K 的模板，thumbnails 写 "the shared centre table and the disc joints"。
- **04-V 带尺寸三视图**：第 53 页已有正、侧、俯三视渲染图，只缺尺寸线。可以在 3D 软件里加标注后导出，用 01-V 的模板。
- **04-X 爆炸图**：
```
Exploded axonometric render of [锚点]: both leather backs and webbing seats lifted off, walnut table top and slatted shelf separated, the shared tube frame and disc joints spaced along dashed lines, white background --ar 4:5
```
- **04-D1–D3 特写**：
```
Macro close-up of the slatted walnut lower shelf under the centre table, [锚点] --ar 1:1
```
```
Macro close-up of a round disc joint linking seat frame and table frame, [锚点] --ar 1:1
```
```
Macro close-up of the leather sling back seam and the walnut armrest end cap, [锚点] --ar 1:1
```
- **04-Sa 场景**：
```
[锚点] on a wide timber deck facing a calm lake, two tea cups on the centre table, early morning mist, [风格锚点] --ar 2:3
```
- **04-Sb 场景**：
```
[锚点] under deep timber eaves during light rain, wet stone courtyard beyond, soft grey light, [风格锚点] --ar 4:5
```

### 3.5 藏器 · 展示架 Vessel Keeper（第 57–63 页）
造型锚点：
```
a freestanding display shelf: two pointed crescent-shaped end frames of curved brushed stainless tube, each wrapped in cream translucent mulberry-paper fabric gathered at the bottom into a small dark steel foot plate, a straight stainless post at the back of each end, and four fluted (reeded) glass shelves held by cylindrical clamp collars, open back
```
现有草图与新造型一致，不用重画。
- **05-V 三视图**：用 01-V 的模板。
- **05-X 爆炸图**：
```
Exploded axonometric render of [锚点]: four fluted glass shelves lifted out, fabric sleeves slid off the curved end frames, collars and foot plates separated with dashed lines, white background --ar 4:5
```
- **05-D1–D3 特写**：
```
Macro close-up of the mulberry-paper fabric gathered at the foot plate, fibres visible, [锚点] --ar 1:1
```
```
Macro close-up of a fluted glass shelf edge held by a clamp collar on the curved tube, [锚点] --ar 1:1
```
```
Macro close-up of the pointed tip of the crescent frame with the fabric pulled taut, backlit, [锚点] --ar 1:1
```
- **05-Sa 场景**：
```
[锚点] against a lime-plaster wall holding tea caddies, celadon bowls and a few books, soft side light, [风格锚点] --ar 2:3
```
- **05-Sb 场景**：
```
[锚点] used as a semi-transparent partition between a tea room and a corridor, backlit by afternoon sun so the paper panels glow, [风格锚点] --ar 4:5
```

### 3.6 秉烛 · 折光吊灯 Candlelight（第 64–70 页）
造型锚点：
```
a tall pendant lamp hung from a thin steel cable: four square stainless rods form the corners and extend above and below the body, five tiers of square stainless cross-bar frames, two long bands of cream paper-veneer folded in zig-zags weaving through the tiers, warm light glowing from translucent panels inside
```
现有草图与新造型一致，不用重画。
- **06-A 补角度**（第 67 页）：
```
Studio product photograph of [锚点], side view rotated 45 degrees, lit, on a seamless light grey background --ar 2:3
```
```
Studio product photograph looking straight up into [锚点] from below, the folded bands and glowing core visible --ar 1:1
```
（这两张最好用渲染出，AI 版很难保持折带的走向。）
- **06-V 三视图**：用 01-V 的模板（正视、侧视、仰视）。
- **06-X 爆炸图**：
```
Exploded axonometric render of [锚点]: the five cross-bar tiers spaced apart along the four rods, the two folded bands lifted away, the light source in the centre, dashed alignment lines, white background --ar 4:5
```
- **06-D1–D3 特写**：
```
Macro close-up of a folded paper-veneer band glowing with warm light, grain visible, [锚点] --ar 1:1
```
```
Macro close-up of a square cross-bar frame clamped to a corner rod, [锚点] --ar 1:1
```
```
Close view of the rod ends projecting below the lamp body, warm light above, [锚点] --ar 1:1
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

**00-B 材质板**（第 27 页「节序 · 材料」）
```
Flat-lay material board, top-down: overlapping square swatches of walnut wood, brushed stainless-steel plate, walnut-brown saddle leather with contrast top-stitching, cream cotton webbing in basket weave, fluted glass, and cream translucent mulberry paper, loose diagonal cluster, soft shadow, on white paper --ar 1:1
```

**00-M1 大场景：临水廊下**（替换第 71、76 页的旧场景）
```
The complete Nodes in Order tea furniture collection — a long walnut tea table with a stainless pedestal cabinet, a host armchair with a leather sling back, two guest armchairs with V-braced walnut arms, a two-seat bench with a walnut centre table, a crescent-framed paper display shelf and a tall folded-paper pendant lamp — set as one tea setting for five under a covered timber veranda beside a lake, afternoon light, wide shot 24mm, [风格锚点] --ar 16:9
```
（这张同时用于第 21 页右侧小图，换进去后裁成竖幅即可。）

**00-M2 大场景：傍晚室内**
```
The same collection arranged in a timber-framed tea room at dusk, only the pendant lamp glowing, windows showing a blue evening garden, wide shot, [风格锚点] --ar 16:9
```

**00-M3 大场景：雨天庭院俯视**（可选）
```
High-angle view down into a small Jiangnan courtyard pavilion in light rain, the full collection set for five under the eaves, wet stone paving, a maple tree, calm grey light, [风格锚点] --ar 16:9
```

**00-F 系列合影**（可选，替换封面上的拼图）
```
All pieces of the Nodes in Order collection arranged loosely on a seamless white floor, 45-degree high-angle view, soft overhead studio light, gentle shadows, catalogue still life, generous spacing --ar 3:2
```

---

## 5. 优先级

1. **大场景 00-M1**：一张图能同时替换第 21、71、76 页三处旧家具，效果最明显。
2. **4 张形态推敲草图**（茶台、主位椅、客位椅、并坐）：现在的草图和新家具对不上，评审最容易看出来。
3. **每件单品的场景 a**：6 张。
4. **材质板、特写**：能从高清渲染重新出就重新出。
5. **三视图、爆炸图**：从 3D 模型导出，尺寸要真实。

---

## 5.5 在 v26 里怎么换图

1. 打开 `节序_茶家具设计报告_v26_待补图.pptx`，翻到要补的页。
2. 灰色虚线框里写着编号、比例和像素、参考图、完整英文提示词。复制提示词，带上参考图去生成。同样的内容也在这一页的备注里。
3. 生成时比例要选对（2:3、4:5、1:1、3:2、16:9），换进去后才会正好填满虚线框。
4. 点一下提示框的文字边框，按 Delete 删掉它。
5. 右键灰框 →「更改图片」，选生成好的图。位置和大小保持不变。
6. 红框的卡片盖在旧图上（旧草图、旧场景）。同样删掉卡片，再右键旧图 →「更改图片」。
7. 视图页、爆炸图、多角度页的图请生成纯白背景，放在白页上看不出边。
8. 第 33、40、47、54、61、68 页的尺寸行 `L ___ × W ___ × H ___ mm` 请直接填真实尺寸。

## 6. 编号 → 页码（v26）

| 编号 | 内容 | 页码 |
|---|---|---|
| 01-K | 围炉 · 茶台 · 形态推敲草图（盖在旧草图上） | 30 |
| 01-V | 围炉 · 茶台 · 三视图 + 尺寸 | 33 |
| 01-X | 围炉 · 茶台 · 爆炸图 | 34 |
| 01-D1 | 围炉 · 茶台 · 细节特写 1 | 34 |
| 01-D2 | 围炉 · 茶台 · 细节特写 2 | 34 |
| 01-D3 | 围炉 · 茶台 · 细节特写 3 | 34 |
| 01-Sa | 围炉 · 茶台 · 场景图（竖） | 35 |
| 01-Sb | 围炉 · 茶台 · 场景图 | 35 |
| 02-K | 东道 · 主位椅 · 形态推敲草图（盖在旧草图上） | 37 |
| 02-V | 东道 · 主位椅 · 三视图 + 尺寸 | 40 |
| 02-X | 东道 · 主位椅 · 爆炸图 | 41 |
| 02-D1 | 东道 · 主位椅 · 细节特写 1 | 41 |
| 02-D2 | 东道 · 主位椅 · 细节特写 2 | 41 |
| 02-D3 | 东道 · 主位椅 · 细节特写 3 | 41 |
| 02-Sa | 东道 · 主位椅 · 场景图（竖） | 42 |
| 02-Sb | 东道 · 主位椅 · 场景图 | 42 |
| 03-K | 西宾 · 客位椅 · 形态推敲草图（盖在旧草图上） | 44 |
| 03-A | 西宾 · 客位椅 · 补正面角度 | 46 |
| 03-V | 西宾 · 客位椅 · 三视图 + 尺寸 | 47 |
| 03-X | 西宾 · 客位椅 · 爆炸图 | 48 |
| 03-D1 | 西宾 · 客位椅 · 细节特写 1 | 48 |
| 03-D2 | 西宾 · 客位椅 · 细节特写 2 | 48 |
| 03-D3 | 西宾 · 客位椅 · 细节特写 3 | 48 |
| 03-Sa | 西宾 · 客位椅 · 场景图（竖） | 49 |
| 03-Sb | 西宾 · 客位椅 · 场景图 | 49 |
| 04-K | 比肩 · 并坐连坐 · 形态推敲草图（盖在旧草图上） | 51 |
| 04-V | 比肩 · 并坐连坐 · 三视图 + 尺寸 | 54 |
| 04-X | 比肩 · 并坐连坐 · 爆炸图 | 55 |
| 04-D1 | 比肩 · 并坐连坐 · 细节特写 1 | 55 |
| 04-D2 | 比肩 · 并坐连坐 · 细节特写 2 | 55 |
| 04-D3 | 比肩 · 并坐连坐 · 细节特写 3 | 55 |
| 04-Sa | 比肩 · 并坐连坐 · 场景图（竖） | 56 |
| 04-Sb | 比肩 · 并坐连坐 · 场景图 | 56 |
| 05-V | 藏器 · 展示架 · 三视图 + 尺寸 | 61 |
| 05-X | 藏器 · 展示架 · 爆炸图 | 62 |
| 05-D1 | 藏器 · 展示架 · 细节特写 1 | 62 |
| 05-D2 | 藏器 · 展示架 · 细节特写 2 | 62 |
| 05-D3 | 藏器 · 展示架 · 细节特写 3 | 62 |
| 05-Sa | 藏器 · 展示架 · 场景图（竖） | 63 |
| 05-Sb | 藏器 · 展示架 · 场景图 | 63 |
| 06-A1 | 秉烛 · 折光吊灯 · 补侧面角度 | 67 |
| 06-A2 | 秉烛 · 折光吊灯 · 补仰视角度 | 67 |
| 06-V | 秉烛 · 折光吊灯 · 三视图 + 尺寸 | 68 |
| 06-X | 秉烛 · 折光吊灯 · 爆炸图 | 69 |
| 06-D1 | 秉烛 · 折光吊灯 · 细节特写 1 | 69 |
| 06-D2 | 秉烛 · 折光吊灯 · 细节特写 2 | 69 |
| 06-D3 | 秉烛 · 折光吊灯 · 细节特写 3 | 69 |
| 06-Sa | 秉烛 · 折光吊灯 · 场景图（竖） | 70 |
| 06-Sb | 秉烛 · 折光吊灯 · 场景图 | 70 |
| 00-B | 材质板 | 27 |
| 00-M1 | 大场景 · 临水廊下（第 71 页盖在旧场景上；第 21、76 页用同一张图替换） | 21、71、76 |
| 00-M2 | 大场景 · 傍晚室内 | 72 |
| 00-M3 | 大场景 · 雨天庭院（可选） | 73 |
