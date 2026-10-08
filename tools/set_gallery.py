# 프로젝트 사진을 한 번에 다시 깐다: 고른 원본 사진 → NN.jpg / NN-th.jpg / teaser.jpg, md 의 gallery·teaser 갱신
# 사용: python tools/set_gallery.py spec.json   (spec: {"slug": {"teaser": 1, "items": [["원본경로", "설명"], ...]}})
# 원본은 이미 마스킹(크롭·덧칠)된 이미지여야 한다.
import json, os, re, sys, shutil, tempfile
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "images", "portfolio")

def cover(im, ratio=1.6):
    w, h = im.size
    if w / h > ratio:
        nw = int(h * ratio); return im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    nh = int(w / ratio); return im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))

def apply(slug, spec):
    items = spec["items"]
    loaded = [(Image.open(p).convert("RGB"), cap) for p, cap in items]  # 덮어쓰기 전에 먼저 읽는다
    d = os.path.join(IMG, slug)
    if os.path.isdir(d): shutil.rmtree(d)
    os.makedirs(d)
    for i, (im, _) in enumerate(loaded, 1):
        full = im.copy(); full.thumbnail((1600, 1600)); full.save(f"{d}/{i:02d}.jpg", quality=86)
        th = im.copy(); th.thumbnail((640, 640)); th.save(f"{d}/{i:02d}-th.jpg", quality=84)
    t = spec.get("teaser", 1)
    cover(loaded[t - 1][0]).resize((800, 500), Image.LANCZOS).save(f"{d}/teaser.jpg", quality=86)

    md = os.path.join(ROOT, "_portfolio", f"{slug}.md")
    text = open(md, encoding="utf-8").read()
    _, fm, body = text.split("---\n", 2)
    fm = re.sub(r"^header:\n(  .*\n)+", "", fm, flags=re.M)
    fm = re.sub(r"^gallery:\n(  .*\n)+", "", fm, flags=re.M)
    fm += f"header:\n  teaser: /assets/images/portfolio/{slug}/teaser.jpg\n"
    fm += "gallery:\n" + "".join(
        f'  - url: /assets/images/portfolio/{slug}/{i:02d}.jpg\n'
        f'    image_path: /assets/images/portfolio/{slug}/{i:02d}-th.jpg\n'
        f'    alt: "{cap}"\n    title: "{cap}"\n' for i, (_, cap) in enumerate(loaded, 1))
    if "{% include gallery %}" not in body:
        body = body.rstrip() + "\n\n{% include gallery %}\n"
    open(md, "w", encoding="utf-8").write(f"---\n{fm}---\n{body}")
    print(slug, len(loaded))

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    for slug, s in spec.items(): apply(slug, s)
