# 图片盘点、引导补图与提示词

这套版式的精致感主要靠图撑起来。不论哪类项目，用户的原稿几乎总会缺几类图。每次排版都要：
1. 盘点现有的图；
2. 用大白话告诉用户缺什么、为什么缺、先补哪张；
3. 交付《图片补全清单.md》和一份**待补图版 PPT**，用户生成图片后直接换进去。

> 除非用户要求，不要自己调用生图工具。用户最了解自己的作品，也最清楚想用哪个工具。
> 用户明确要求代为生成、而且会话里有生图工具时，可以按清单里的提示词生成，并用用户的作品图作参考图。

目录：1 补图的通用原则 · 2 盘点步骤 · 3 引导用户 · 4 清单格式 · 5 提示词配方 · 6 各类镜头的提示词模板 · 7 工具要点 · 8 待补图版 PPT · 9 用户换了新版本素材时 · 10 交回与排入

---

## 1. 补图的通用原则
按「单元 × 四类图」，加上「整组 × 三类图」来对照（单元是什么、各类型的具体图，见 project-types.md）：

| 层级 | 图的类型 | 放在 | 作用 |
|---|---|---|---|
| 每个单元 | **主图** | G 预告、I 主图 | 作品最完整、最好看的样子；**必需** |
| 每个单元 | **过程** | H | 怎么来的：草图、草稿、线框、推敲 |
| 每个单元 | **细节** | J | 局部特写 ×3 + 一张结构或拆解图 |
| 每个单元 | **情境** | K | 放进真实环境里的样子 ×2 |
| 每个单元 | 说明 / 多视角（按类型） | I′ | 技术图、规范、其他角度 |
| 整组 | **总览** | A 封面、L | 全部单元放在一起 |
| 整组 | **材料 / 色板 / 字体** | L | 这个作品的「材料」 |
| 整组 | **氛围大图** | M | 2–3 张，在时间、空间或情绪上拉开 |
| 各章 | 扉页 / 目录插图 | B、C | 线稿、草图、局部 |

**判断「能不能用」**：
- **✓**：能直接用。
- **缺**：没有这类图。
- **仅裁切**：只是从别的图里裁出的局部，放大后不够清晰。
- **旧稿**：图还在，但画的是旧版本。
- **低清**：宽度不到排版宽度的 2 倍。

**哪些图不要让 AI 生成或修改**：作品本身是摄影、插画、界面截图时，AI 只用来补展陈、样机、氛围，不碰作品。需要准确数据的图（尺寸图、平立剖、规范、数据图表）应当从源文件导出；AI 版只能当风格示意，必须向用户说明这一点。

## 2. 盘点步骤
1. 运行 `python -I scripts/inventory.py deck.pptx --images-out WORK/media`，导出每张图，并记下它在哪些页被用到。没有 PPT、只有素材文件夹时，直接看文件夹。
2. 逐张看图，给每张归类：主图、过程、细节、情境、说明 / 技术、总览、材料、参考 / 调研、线稿。
3. 建一张「单元 × 图片类型」矩阵，按第 1 节的判断标准填。
4. 从现有作品图里提炼每个单元的**对象锚点**：一句英文，说清它的形态、材料 / 媒介、颜色、关键特征。这句话会粘进每条提示词。
5. 提炼**全套风格锚点**：光线、空间或背景、色调、情绪。
6. 看文件名和用户的备注，弄清每张图对应哪个单元、哪个角度。拿不准就问。

## 3. 引导用户
先把盘点结果用大白话告诉用户，然后再生成清单和待补图版：
1. **一句话结论**：现在有什么、缺什么。例如：「每个单元都有主图，缺的主要是细节和情境；整组缺材料板。」
2. **按影响排优先级**：哪张图补上效果提升最大。通常顺序是：一张氛围大图（可以替换多处）→ 过时的过程图 → 每单元一张情境图 → 材料 / 色板 → 技术图。
3. **每类图问来源**：用户手上有没有？能不能从源文件（3D、CAD、Figma、AI 文件、相机原片）导出？还是要 AI 生成？能导出的就不要生成。
4. **说明怎么用待补图版**：复制框里的提示词 → 生成 → 删除提示框 → 右键灰框「更改图片」。
5. 用户说某类图「先不换」：照样列进清单，旧图留在原位并盖上卡片，不要删。

## 4. 清单格式（交付文件《图片补全清单.md》）
```
# 图片补全清单 — <项目名>
## 1. 缺图总览
（矩阵：行 = 每个单元 + 整组，列 = 主图 / 过程 / 说明 / 细节 / 情境 / 总览 / 材料 / 氛围；格内写 ✓、缺、仅裁切、旧稿或低清）
一段说明：旧稿、仅裁切各指哪些页；待补图版里已经留好了哪些位置

## 2. 通用设置
- 全套风格锚点（英文，可直接粘贴）
- 通用负面词
- 保持一致的做法：参考图、种子、同一镜头
- 文件命名与交回方式；各类图的比例和像素表

## 3. 逐单元提示词
### 3.x <单元中文名 English Name>（第 a–b 页）
对象锚点：<一句英文>
| 编号 | 用途（模板 · 页码） | 比例 | 推荐来源 |
然后每张一段：**<编号> <图名>**、提示词、注意事项

## 4. 整组
## 5. 优先级
## 5.5 在待补图版里怎么换图
## 6. 编号 → 页码（构建后扫描得到）
```
- 编号规则：单元两位数字 + 类型，例如 `01-K` 过程、`01-V` 说明、`01-X` 结构、`01-D1` 细节、`01-Sa` 情境、`01-A` 补角度；整组用 `00-B` 材料、`00-M1` 氛围大图。
- 清单只写**缺的图**。已有的图在总览矩阵里打 ✓ 即可。
- 页码要对照新稿的实际页序，不要凭推算。

## 5. 提示词配方
`[对象锚点] + [镜头类型] + [环境 / 背景] + [光线] + [机位与镜头] + [质感与风格] + [版面留白] + [参数]`

- **对象锚点**：每张都完整粘贴，不要写「同上」，图像模型没有上下文。
- **参考图**：每张都写清楚用哪张作参考图（写用户自己的文件名）。有参考图时，可以在锚点后加 *exactly as the reference image*。
- **版面留白**：写明画面里哪里要留空，例如 *generous negative space on the left*。
- **全套统一**：同一套作品里，光线和色调用同一句风格锚点。
- **背景**：要放在白页上、不加框的图（结构图、多视角、样机单品），提示词里要求 *seamless pure white background*。
- **通用负面词**：*text, watermark, logo, signature, distorted proportions, extra parts, cluttered props, oversaturated colours, plastic look, CGI artefacts, people facing camera*。
  - 按项目再加：产品加 *extra legs, warped joints*；UI 加 *fake UI text*；人物类先问用户要不要露脸。
- **防止画回旧版本**：稿子里还有旧版本的图时，把旧版的特征写进负面词。

## 6. 各类镜头的提示词模板（把花括号里的内容换掉）
| 用途 | 模板 |
|---|---|
| 主图（物体） | `Studio photograph of {ANCHOR}, three-quarter view from slightly above, isolated on a seamless pure white background, soft diffused light, faint contact shadow, crisp material detail --ar 4:3` |
| 主图（空间） | `Architectural visualization of {ANCHOR}, eye-level 24mm, {LIGHT}, calm editorial mood, generous negative space --ar 16:9` |
| 过程 / 草图 | `Designer's pencil sketch sheet of {ANCHOR}: one large perspective and two small thumbnail studies, fine graphite lines with light construction lines, plain white paper, no text --ar 3:2` |
| 过程 / 线框（UI） | 不用 AI，用 Figma 导出线框图；概念示意可用 `Low-fidelity wireframe sketches of {SCREENS} on white paper, marker lines --ar 3:2` |
| 技术图 | `Technical orthographic drawing of {ANCHOR}: front, side and top views on one sheet, thin black hairlines on pure white, dimension lines, small sans-serif labels, no shading --ar 3:2`（只当示意，准确的要从源文件导出） |
| 结构 / 拆解 | `Exploded axonometric of {ANCHOR}, components separated along their axes with thin dashed alignment lines, on a seamless pure white background, soft studio light --ar 4:5` |
| 细节特写 | `Macro close-up of {DETAIL} on {ANCHOR}; materials exactly as the reference image; shallow depth of field, soft raking side light, tightly cropped, no text --ar 1:1` |
| 情境 | `{ANCHOR} in {CONTEXT}, editorial photograph, {LIGHT}, muted low-saturation palette, eye-level 35mm, the work as the clear subject, generous negative space, {STYLE}. {NEGATIVE} --ar 2:3` |
| 样机（品牌 / UI / 插画） | `{ITEM} mockup on a neutral linen surface, soft daylight, top-down flat lay, realistic paper / screen texture, no extra text --ar 4:5`；界面截图、作品图后期贴进样机，不让 AI 画 |
| 材料 / 色板 | `Flat-lay material board, top-down: overlapping swatches of {MATERIALS}, loose diagonal cluster, soft shadow, on white paper, no text --ar 1:1`；纯色板可以直接用 kit 画色块，不必生成 |
| 氛围大图 | `{ALL UNITS} together in {SETTING}, {TIME/LIGHT}, wide shot 24mm, {STYLE}. {NEGATIVE} --ar 16:9`；2–3 张在时间、空间或情绪上拉开差异 |
| 总览 | `All {UNITS} arranged on a seamless white surface, 45-degree high angle, soft overhead light, catalogue still life, generous spacing --ar 3:2`；也可以用现有抠图 `compose` 拼 |

## 7. 工具要点
- **Midjourney**：用 `--ar` 控制比例，`--style raw` 减少过度美化；参考图的 URL 放在提示词最前面，加 `--iw 1.5–2`；氛围可以用 `--sref` 借现有的图。
- **即梦 / 可灵 / 通义万相**：上传参考图，强度 0.35–0.5；提示词中英文都可以。
- **GPT-image / Gemini 编辑模式**：上传作品图，写「主体完全不变，只替换背景为……」。这是保住造型最可靠的办法。
- **Stable Diffusion**：用线稿或深度图配合 ControlNet。
- **AI 的硬伤**：结构、数量、文字常常出错。生成后逐张核对；技术图、界面、文字类内容不要交给 AI。
- **分辨率**：至少是排版尺寸的 2 倍。

## 8. 待补图版 PPT（默认要做）
完整版（不带占位框）和待补图版分成两个文件交付。待补图版的做法：
- **每个缺的图，在最终版式位置放一个占位框**：`K.add_slot(...)`。
  - 占位框是一张灰色虚线框图片，比例和最终的图一致，底部有淡色的「编号 AI 图片位」。
  - 框上叠一个提示框：编号 · 用途 · 比例 · 像素、参考图、完整英文提示词、操作步骤。提示框的字号会自动缩小，直到放得下。
  - 同样的内容追加到这一页的备注里。
- **页面上的文字先排好**：标题、标签、材料清单都写好，中英对照。需要用户填的写成空格，例如尺寸 `L ___ × W ___ × H ___ mm`、参数、日期。
- **旧图不删**：在旧图上盖一张白底、强调色边框的卡片（`K.add_old_card`）；同一张新图要换多处时，卡片写明「先按第 N 页生成」。
- **页面结构**：每个单元按 project-types.md 的循环补齐 G → H → I → I′ → J → K；整组补 L、M。
- **交付**：
  - 清单末尾附「编号 → 页码」表：构建后扫描形状名「待替换图片-编号」得到，不要手算。
  - 附一段「怎么换图」的操作说明。
  - 告诉用户：「更改图片」会保持框的位置和大小；生成时比例要选对。

## 9. 用户换了新版本素材时
（作品改版、重新渲染、重新拍摄、新的界面截图……）
1. **对号入座**：按文件名或备注，确认每张新图对应哪个单元、哪个角度或哪个画面；拿不准就问。
2. **处理**：
   - 物体类：灰底用 `assets.py studio`，白底用 `cutout`；抠完把所有结果铺在白底上检查。
   - 空间、摄影、插画、界面：不抠图，只统一裁切比例。
3. **全稿替换**：用 `pic_sha` 找出旧图的每一处：
   - 整张替换用 `swap_cutout`，或 `replace_blob` 加 `set_crop_aspect`；
   - 局部裁切用 `K.set_region`（中心点 + 宽度，单位是新图的像素；先在新图上叠一层坐标网格再选）。
   - 构建后按旧图的 sha 再扫一遍，确认没有残留。
4. **改文字**：和新版本不符的描述（材料、结构、名称、数据）中英一起改，改完在全稿搜一遍旧词。
5. **标旧稿**：过程图、情境图里画的若还是旧版本，在矩阵里标「旧稿」，在待补图版里盖上卡片。
6. **特殊形状**：长吊线、细长天线这类会把主体压得很小的部分，排版时用截短的版本。
7. **新增角度**：放进 I′ 多视角页。

## 10. 交回与排入
- **命名**：`<两位编号>_<单元英文名>_<类型>_<a|b>.png`，例如 `02_east-seat_scene_a.png`、`00_series_board.png`。
  - 类型：hero / process / views / exploded / detail / scene / mockup / board / bigscene / family / angle。
- **处理**：物体图先抠图；线稿、技术图用 `assets.py lineart` 转成透明线（`--gray 40` 是深灰）；照片、插画、界面原样使用。
- **排入**：直接在待补图版里「更改图片」；或者交回给 Claude，按编号排入。排完重新出图，逐页检查。
