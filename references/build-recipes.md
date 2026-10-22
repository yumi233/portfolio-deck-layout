# 构建做法与踩过的坑

目录：1 环境 · 2 选路线 · 3 构建脚本骨架 · 4 质检 · 5 坑与对策

## 1. 环境
```bash
python3 -m venv WORK/venv
WORK/venv/bin/pip install python-pptx pillow numpy pymupdf lxml
```
- 读取原稿里的图片、或运行其他会解析文件的 Python 时，加 `-I` 参数，并把路径作为参数传进去。
- **出图**：`scripts/render.py` 在 macOS 上用 Keynote（通过 AppleScript 调用，会短暂打开 Keynote），否则用 LibreOffice。
  - 渲染结果用的是本机字体，所以结论只对本机成立；交付时要说明。
- **格式校验**：若装了 pptx 技能，用它的 `scripts/office/validate.py out.pptx --original src.pptx`，需要 Python 3.10 以上。

## 2. 选路线
- **改造原稿（常用）**：原稿是 PPT，里面有矢量地图、示意图、表格时，保留这些元素，只做缩放、换色、换字、移位。这些矢量元素不可能手工重画。
- **从素材新建**：只有图片和文字（一个文件夹、一份 Word、一堆截图）、没有可用版面时，从一个空白 16:9 演示文稿开始（`Presentation()` 后设宽高），用 `new_slide` + 模板函数（build_cover / build_toc / build_divider / build_g / build_views / text_block / tb / pic）逐页搭。
- **从零新建的底稿**：用 `K.blank_deck(base=现成的 16:9 pptx)`，例如用户自己的任意一个 PPT，删光页面后留下母版和主题。
  - 本机实测：用 python-pptx 自带默认模板新建的稿子，Keynote 打开时卡住，疑似弹出了缺字体之类的对话框，之后 Keynote 对所有文件都没有响应。
  - 遇到这种情况，请用户切到 Keynote 关掉对话框，或者退出 Keynote。
- **混合**：原稿版面能用的页改造，不能用的页按模板新建。
- 三条路线都用 `scripts/pptx_kit.py`。`examples/nodes-bamboo-court/` 是**产品 / 家具类**的完整示例（改造原稿，三轮）。`examples/space-from-scratch/` 是**室内类、从零新建**的示例（只有照片，强调色由照片推导）。其他类型照同样的步骤做，页面和图按 project-types.md 换。

## 3. 构建脚本骨架
```python
import sys; sys.path.insert(0, '<skill>/scripts')
import pptx_kit as K, assets as AS, fonts as FN
from pptx import Presentation

cn, _ = FN.find(FN.CN); en, en_file = FN.find(FN.EN)
K.configure(en_font=en, cn_font=cn, en_font_file=en_file)
acc = AS.suggest_accent([主图1, 主图2, 主图3])  # 作品主色 → 强调色；无彩时返回茶红
K.set_accent(acc['main'], acc['light'])
prs = Presentation(SRC)
k = 960 / (prs.slide_width / 12700)            # 原稿等比缩放到 960 宽
prs.slide_width, prs.slide_height = K.E(960), K.E(540)
S = {i + 1: s for i, s in enumerate(prs.slides)}

def base(sl, i):                               # 每个改造页先走一遍
    K.drop_chrome(sl, names=(...原稿页眉/页码/背景图的形状名...), texts=(...页脚文字...))
    K.scale_geometry(sl, k)
    K.recolor(sl, accent_on=是分析类章节, text_map=..., line_map=..., fill_map=..., accents=..., overrides=...)
    K.retype(sl); K.restyle_tables(sl); K.white_bg(sl)

# 内容页（D）
for i in 内容页:
    base(S[i], i)
    K.header(S[i], 中文标题, K.en_case(英文副标题))
    K.credit(S[i], 出处)                       # 有出处才加
    K.swap_full_renders(S[i], {sha: cutout_png})
    K.apply_en(S[i], {形状名: ('block', 'English')}, rows=是否行式列表)
    K.vfit(S[i])
# 模板页：build_cover / build_toc / build_divider / build_g / text_block ……
# 新增页：K.new_slide(prs)；最后调页序：K.reorder(prs, order)
prs.save(OUT); K.set_theme_fonts(OUT)
# 然后运行 clean_media.py OUT OUT_clean.pptx
```
- **其他常用函数**：
  - `K.set_lines(el, [行1, 行2])`：改文本框的中文，保留原格式。
  - `K.set_region(slide, el, png, cx, cy, w)`：在原图框里换成新图的某个区域。
  - `K.build_views(...)`：多角度页。
  - `K.swap_cutout(...)`：整张物体图换成抠图。
  - `K.set_accent(main, light)`：设置这份稿子的强调色（`assets.py accent` 给出建议）。
  - `K.add_slot(slide, x, y, w, h, sid, head, ref, prompt, workdir, font_file)`：AI 图片占位框 + 提示框（待补图版用）。
  - `K.add_old_card(slide, x, y, w, h, sid, head, ref, prompt, steps=None)`：盖在旧图上的提示卡片。
  - `K.add_notes(slide, text)`：往这一页的备注里追加文字。
- **形状名**：用 `inventory.py` 的输出（方括号里的组名 / 形状名）查原稿里的元素。原稿是生成器做的时，名字通常很规整，例如 `v20-title`、`history-copy-0`。
- **配色映射**：先用 `inventory.py` 统计原稿颜色，写出显式映射。没写到的颜色由 `auto_colour` 按明度兜底，并记进 `K.log`；看日志补全映射。

## 4. 质检（每轮都做）
1. 运行 `render.py OUT.pptx WORK/png`，逐张看拼图，可疑页再看大图。重点检查：
   - 文字溢出或互相压字
   - 元素重叠
   - 圆点、编号、图注没有跟着主体走
   - 内容超出 y≈494
   - 白底渲染露出灰框
   - 英文最后一行只剩一个单词
   - 中英两行挤在一起
2. 对比新旧稿的文字清单，确认除了有意删掉的导航文字，没有内容丢失；备注页数不变。
3. 运行 `clean_media.py`，再做格式校验。
4. 只改了少数页时，用 PyMuPDF 逐页比较新旧 PDF 的像素差，确认只有预期的页变了。

## 5. 坑与对策
| 现象 | 原因 | 对策 |
|---|---|---|
| 中文显示成黑体 | 只写了 latin 字体 | `K.set_fonts` 同时写 latin、ea、cs |
| 白底渲染在白页上露出灰框 | 渲染底色 #FEFEFE，带地面阴影 | `assets.py cutout` 做反向合成去白；然后 `swap_cutout` |
| 移动后文字跑到框外右侧 | 原稿文本框右对齐，且不自动换行 | 叠放前 `K.left_align` |
| 缩放后组里的子元素错位 | 单子元素包装组的 chOff/chExt 没同步 | 一律用 `K.place`，组和子元素一起改 |
| 文件变大 | 删掉的图片关系还留在包里 | `clean_media.py` |
| 表格出现蓝色条纹 | 去掉单元格填充后露出了表格样式的填充 | `restyle_tables` 写入 noFill，并关闭 firstRow / bandRow |
| 加英文后时间轴圆点离开主线 | 列模式只推了部分元素 | `K.anchor(..., 'c')` |
| 加英文后编号和名称错行 | 编号在另一列，没被推动 | 用行模式，或 `K.anchor` 对齐到名称 |
| 图注离图片太远 | 行模式把图注推多了 | `K.anchor(图注, 图, ('below', 18))` |
| 原稿文本框太高，导致叠放间距过大 | 字号缩小后框高没跟着变 | `K.fit_height` |
| 运动模糊太重，看不出主体 | 模糊半径太大 | `assets.py blur --amount 0.035`，保留 18% 清晰重影 |
| 条目标题加大后挤爆信息图 | 字号规则过激 | 条目标题保持 11pt，靠颜色区分（已是默认） |
| 用户想保留原版式 | 换结构是为了塞英文 | 先缩短英文；换结构前先问 |
| 灰底渲染抠完有灰边或地面光晕 | 用了只去纯白的 `cutout` | 改用 `assets.py studio`：先除掉背景，再去掉零散的低透明度光晕 |
| 主体在页面里很小（吊灯、旗杆、天线类） | 细长的附属部分把整张图拉得很高 | 排版用截短的版本，附属部分留约主体高度的 12% |
| 构建脚本导入了错误的 `assets.py` | 工作目录里有同名的旧脚本，抢先被导入 | 技能的 scripts 目录 `insert(0)`，本地目录用 `append` 放最后 |
| 换了新版本素材后旧图还残留 | 局部裁切没被整图替换覆盖到 | 局部用 `K.set_region` 换；构建后按旧图的 sha 扫一遍全稿 |
| 新设计和旧文字不符 | 只换了图没改字 | 用 `K.set_lines` 改中文，并同步改 EN；完了全稿搜一遍旧词 |
| 作品被转成了灰度或换了颜色 | 把作品图当成调研图处理，或者 recolor 动到了作品里的色块 | 只对调研、参考图用 `gray`；品牌色块、作品配色写进 overrides，保持原色 |
| 强调色太艳或太灰 | 直接用了作品原色 | 用 `assets.py accent` 的沉稳版（亮度 0.30、饱和度 0.45）；作品无彩时用茶红 |
