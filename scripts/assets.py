"""Image preparation for the portfolio layout. Run with -I and pass paths as arguments.

  cutout   IN OUT [--eps 0.035]      white/near-white backdrop -> transparent PNG, trimmed (renders on #FEFEFE)
  studio   IN OUT [--eps 0.045]      grey / gradient studio backdrop -> transparent PNG (most product renders);
                                    divides out the backdrop, keeps glowing parts, drops floor haze, keeps thin cables
  blur     IN OUT [--amount 0.035]   horizontal motion-blur teaser of a cut-out (G title pages)
  gray     IN OUT                    archival grayscale, alpha kept (research collages, timeline figures)
  knockout IN OUT [--keep-color]     studio-grey backdrop -> transparent, grayscale by default (museum object photos)
  lineart  IN OUT [--gray 138]       recolour dark line art to a mid grey, trimmed (contents page / dividers)
  trim     IN OUT                    trim transparent margins
  compose  SPEC.json OUT             arrange cut-outs on one transparent canvas (cover group, divider line-up)
  accent   IMG [IMG ...]             suggest the deck's accent colour pair from the project's main images

compose spec: {"canvas": [480, 320], "px_per_pt": 6,
               "items": [{"src": "cut_shelf.png", "x": 8, "y": 6, "h": 170}, {"src": "cut_table.png", "x": 118, "y": 52, "w": 250}]}
  x/y/w/h are points on the canvas; give either w or h. Avoid overlaps: cut-outs of pale objects are partly transparent.
"""
import sys, json, argparse, os, math
import numpy as np
from PIL import Image, ImageFilter


def trim(im, thr=8, pad=0):
    al = np.asarray(im.split()[-1])
    ys, xs = np.where(al > thr)
    if not len(xs):
        return im
    return im.crop((max(0, xs.min() - pad), max(0, ys.min() - pad),
                    min(im.width, xs.max() + 1 + pad), min(im.height, ys.max() + 1 + pad)))


def white_to_alpha(im, eps=0.035):
    """Exact inverse of compositing over white, so the cut-out looks identical on a white page."""
    a = np.asarray(im.convert('RGB')).astype(float) / 255
    al = np.clip(((1 - a).max(2) - eps) / (1 - eps), 0, 1)
    safe = np.where(al > 0, al, 1)[..., None]
    c = np.clip((a - (1 - al[..., None])) / safe, 0, 1)
    return Image.fromarray((np.concatenate([c, al[..., None]], 2) * 255).round().astype('uint8'))


def _gauss1d(sigma):
    r = max(1, int(3 * sigma))
    x = np.arange(-r, r + 1)
    k = np.exp(-x ** 2 / (2 * sigma ** 2))
    return k / k.sum()


def _blur(a, sigma):
    """Separable gaussian on a 2-D float array, edge-padded."""
    k = _gauss1d(sigma); r = len(k) // 2
    p = np.pad(a, ((0, 0), (r, r)), mode='edge')
    a = np.apply_along_axis(lambda row: np.convolve(row, k, mode='valid'), 1, p)
    p = np.pad(a, ((r, r), (0, 0)), mode='edge')
    return np.apply_along_axis(lambda col: np.convolve(col, k, mode='valid'), 0, p)


def studio_background(im, work_w=400, sigma_frac=0.07, iters=4):
    """Estimate the smooth studio backdrop (grey sweep, light gradient) behind a product.
    Normalised convolution over pixels classed as background, re-classifying a few times."""
    rgb = np.asarray(im.convert('RGB')).astype(float) / 255
    H, W = rgb.shape[:2]
    small = np.asarray(im.convert('RGB').resize((work_w, max(2, round(H * work_w / W))), Image.BILINEAR)).astype(float) / 255
    sig = sigma_frac * work_w
    B = np.stack([_blur(small[..., c], sig * 2) for c in range(3)], -1)
    for _ in range(iters):
        d = small - B
        chroma = small.max(2) - small.min(2) - (B.max(2) - B.min(2))
        obj = (d.min(2) < -0.03) | (d.max(2) > 0.05) | (chroma > 0.05)
        obj = _blur(obj.astype(float), 2) > 0.05                       # grow the mask over edges and soft shadows
        m = (~obj).astype(float)
        den = _blur(m, sig)
        far = _blur(m, sig * 3)
        B = np.stack([np.where(den > 0.05, _blur(small[..., c] * m, sig) / np.maximum(den, 1e-6),
                               _blur(small[..., c] * m, sig * 3) / np.maximum(far, 1e-6)) for c in range(3)], -1)
    full = np.stack([np.asarray(Image.fromarray(np.ascontiguousarray(B[..., c], dtype='float32')).resize((W, H), Image.BILINEAR))
                     for c in range(3)], -1)
    return rgb, np.clip(full, 0.05, 1)


def _components(mask):
    """4-connected labelling of a small boolean array. Returns (labels, sizes)."""
    H, W = mask.shape
    lab = np.zeros((H, W), int); sizes = [0]
    for y0, x0 in zip(*np.nonzero(mask)):
        if lab[y0, x0]:
            continue
        n = len(sizes); sizes.append(0); stack = [(y0, x0)]; lab[y0, x0] = n
        while stack:
            y, x = stack.pop(); sizes[n] += 1
            for yy, xx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= yy < H and 0 <= xx < W and mask[yy, xx] and not lab[yy, xx]:
                    lab[yy, xx] = n; stack.append((yy, xx))
    return lab, sizes


def keep_main(im, strong=64, min_frac=0.03, grow=0.035, work_w=480):
    """Drop stray low-alpha haze (floor light, backdrop seams): keep the large opaque components
    (and everything within `grow` x width of them, so soft edges and contact shadows survive)."""
    a = np.asarray(im.convert('RGBA')).astype(float)
    H, W = a.shape[:2]
    f = max(1, math.ceil(W / work_w))                       # max-pool so thin parts (pendant cables, rods) survive
    m = a[..., 3] > strong
    m = np.pad(m, ((0, (-H) % f), (0, (-W) % f)))
    sm = m.reshape(m.shape[0] // f, f, m.shape[1] // f, f).max((1, 3))
    lab, sizes = _components(sm)
    if len(sizes) <= 1:
        return im
    big = max(sizes)
    keep = np.isin(lab, [i for i, z in enumerate(sizes) if i and z >= big * min_frac])
    region = _blur(keep.astype(float), max(1, grow * keep.shape[1]))
    region = np.clip(region / max(region.max(), 1e-6) * 6, 0, 1)            # soft, generous halo around kept parts
    region = np.asarray(Image.fromarray((region * 255).astype('uint8')).resize((W, H), Image.BILINEAR)).astype(float) / 255
    a[..., 3] *= region
    return Image.fromarray(a.astype('uint8'))


def studio_cutout(im, eps=0.045, shadow=0.0):
    """Grey / gradient studio backdrop -> transparent PNG that looks the same on a white page.
    Divides out the estimated backdrop (so it becomes pure white), keeps parts brighter than the
    backdrop (glowing shades) by hue, then un-composites over white. shadow>0 fades faint floor shadows."""
    rgb, B = studio_background(im)
    N = rgb / B
    N = N / np.maximum(1, N.max(2, keepdims=True))                    # brighter-than-backdrop: keep hue, cap at 1
    out = white_to_alpha(Image.fromarray((N * 255).round().astype('uint8')), eps)
    if shadow:
        a = np.asarray(out).astype(float)
        al = a[..., 3] / 255
        neutral = (a[..., :3].max(2) - a[..., :3].min(2)) < 25
        al = np.where(neutral, np.clip((al - shadow) / (1 - shadow), 0, 1), al)
        a[..., 3] = al * 255
        out = Image.fromarray(a.astype('uint8'))
    return trim(keep_main(out), thr=12, pad=4)


def _hue_sat_val(rgb):
    mx, mn = rgb.max(-1), rgb.min(-1)
    d = mx - mn
    s = np.where(mx > 0, d / np.maximum(mx, 1e-6), 0)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    h = np.where(mx == r, (g - b) / np.maximum(d, 1e-6) % 6,
                 np.where(mx == g, (b - r) / np.maximum(d, 1e-6) + 2, (r - g) / np.maximum(d, 1e-6) + 4)) / 6
    return h % 1, s, mx


def _contrast_on_white(hex6):
    def lin(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hex6[i:i + 2], 16) for i in (0, 2, 4))
    L = 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
    return 1.05 / (L + 0.05)


def suggest_accent(paths, min_colourful=0.02):
    """Accent pair from the project's main colour.
    Finds the dominant hue among clearly coloured pixels (weighted by saturation), then makes
    a quiet version (HLS lightness 0.30, saturation 0.45, darkened until contrast on white >= 4.5)
    and a light version (lightness 0.76, saturation 0.28). If the work is essentially colourless
    (< 2% coloured pixels: black-and-white photos, bare metal, monochrome drawings), returns tea red.
    Returns dict(main, light, hue, coloured_share, source)."""
    import colorsys
    hist = np.zeros(72); coloured = total = 0
    for p in paths:
        im = Image.open(p).convert('RGBA'); im.thumbnail((320, 320))
        a = np.asarray(im).astype(float) / 255
        rgb, al = a[..., :3], a[..., 3]
        h, s, v = _hue_sat_val(rgb)
        valid = (al > 0.5) & ~((v > 0.93) & (s < 0.08))               # ignore white page / backdrop
        m = valid & (s > 0.22) & (v > 0.18) & (v < 0.98)
        total += valid.sum(); coloured += m.sum()
        np.add.at(hist, (h[m] * 72).astype(int) % 72, s[m])
    share = coloured / max(total, 1)
    if share < min_colourful or hist.sum() == 0:
        return {'main': '8C2C2C', 'light': 'CBA7A9', 'hue': None, 'coloured_share': round(share, 3),
                'source': 'fallback: the work is almost colourless, keep tea red'}
    sm = hist + np.roll(hist, 1) + np.roll(hist, -1)                 # circular smoothing
    k = int(np.argmax(sm))
    idx = np.array([k - 1, k, k + 1]) % 72
    ang = np.angle(np.sum(hist[idx] * np.exp(2j * np.pi * (idx + 0.5) / 72))) / (2 * np.pi) % 1
    def hexof(l, s):
        r, g, b = colorsys.hls_to_rgb(ang, l, s)
        return '%02X%02X%02X' % (round(r * 255), round(g * 255), round(b * 255))
    l = 0.30
    main = hexof(l, 0.45)
    while _contrast_on_white(main) < 4.5 and l > 0.12:
        l -= 0.02; main = hexof(l, 0.45)
    return {'main': main, 'light': hexof(0.76, 0.28), 'hue': round(ang * 360), 'coloured_share': round(share, 3),
            'source': 'dominant hue of the main images'}


def motion_blur(im, amount=0.035, ghost=0.18):
    im = im.convert('RGBA')
    pad = int(im.width * 0.08)
    can = Image.new('RGBA', (im.width + 2 * pad, im.height), (0, 0, 0, 0)); can.paste(im, (pad, 0))
    a = np.asarray(can).astype(float) / 255
    pm, al = a[..., :3] * a[..., 3:4], a[..., 3:4]
    r = max(6, int(im.width * amount))
    acc, aac = np.zeros_like(pm), np.zeros_like(al)
    for d in range(-r, r + 1):
        acc += np.roll(pm, d, axis=1); aac += np.roll(al, d, axis=1)
    acc /= 2 * r + 1; aac /= 2 * r + 1
    acc = acc * (1 - ghost) + pm * ghost; aac = aac * (1 - ghost) + al * ghost   # a faint sharp ghost keeps the form legible
    rgb = np.where(aac > 1e-4, acc / np.maximum(aac, 1e-4), 0)
    out = Image.fromarray((np.concatenate([rgb, aac], 2).clip(0, 1) * 255).astype('uint8'))
    return out.filter(ImageFilter.GaussianBlur(1.2))


def archival_gray(im):
    im = im.convert('RGBA'); r, g, b, a = im.split()
    gray = Image.merge('RGB', (r, g, b)).convert('L').point(lambda v: int(30 + v * 0.86))
    return Image.merge('RGBA', (gray, gray, gray, a))


def knockout(im, keep_color=False, k=3.0):
    im = im.convert('RGB')
    sm = np.asarray(im.filter(ImageFilter.GaussianBlur(2))).astype(float)
    lum, sat = sm.mean(2), sm.max(2) - sm.min(2)
    border = np.concatenate([lum[:10].ravel(), lum[:, :10].ravel(), lum[:, -10:].ravel()])
    bgl, sd = np.median(border), border.std()
    d = np.clip((bgl - k * sd - 8 - lum) / 35, 0, 1)
    d = np.maximum(d, np.clip((sat - 22) / 30, 0, 1))
    al = Image.fromarray((d * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.0))
    if keep_color:
        r, g, b = im.split(); out = Image.merge('RGBA', (r, g, b, al))
    else:
        g = im.convert('L').point(lambda v: int(20 + v * 0.8)); out = Image.merge('RGBA', (g, g, g, al))
    return trim(out, thr=40, pad=4)


def lineart(im, gray=138):
    im = im.convert('RGBA')
    if np.asarray(im.split()[-1]).min() == 255:          # opaque line art on white -> derive alpha from darkness
        im = white_to_alpha(im)
    a = im.split()[-1]
    g = Image.new('L', im.size, gray)
    return trim(Image.merge('RGBA', (g, g, g, a)), thr=10, pad=6)


def compose(spec, base_dir):
    W, H = spec['canvas']; px = spec.get('px_per_pt', 6)
    can = Image.new('RGBA', (int(W * px), int(H * px)), (255, 255, 255, 0))
    for it in spec['items']:
        c = Image.open(os.path.join(base_dir, it['src'])).convert('RGBA')
        s = (it['h'] * px / c.height) if 'h' in it else (it['w'] * px / c.width)
        r = c.resize((max(1, round(c.width * s)), max(1, round(c.height * s))), Image.LANCZOS)
        can.alpha_composite(r, (round(it['x'] * px), round(it['y'] * px)))
    return trim(can, thr=4)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd'); ap.add_argument('src'); ap.add_argument('out', nargs='?', default=None)
    ap.add_argument('more', nargs='*')
    ap.add_argument('--eps', type=float, default=0.035); ap.add_argument('--amount', type=float, default=0.035)
    ap.add_argument('--gray', type=int, default=138); ap.add_argument('--keep-color', action='store_true')
    a = ap.parse_args()
    if a.cmd == 'accent':
        r = suggest_accent([p for p in [a.src, a.out] + a.more if p])
        print(json.dumps(r, ensure_ascii=False))
        return
    if a.cmd == 'compose':
        res = compose(json.load(open(a.src)), os.path.dirname(os.path.abspath(a.src)))
    else:
        im = Image.open(a.src)
        res = {'cutout': lambda: trim(white_to_alpha(im, a.eps), thr=10),
               'studio': lambda: studio_cutout(im, a.eps if a.eps != 0.035 else 0.045),
               'blur': lambda: motion_blur(im, a.amount),
               'gray': lambda: archival_gray(im),
               'knockout': lambda: knockout(im, a.keep_color),
               'lineart': lambda: lineart(im, a.gray),
               'trim': lambda: trim(im.convert('RGBA'), thr=8)}[a.cmd]()
    res.save(a.out)
    print(a.cmd, '->', a.out, res.size)


if __name__ == '__main__':
    main()
