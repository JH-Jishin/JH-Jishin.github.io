# 목록 카드 대표 사진(teaser.jpg)을 다시 만든다.
# 사진(photo)은 16:10 칸을 꽉 채우게 가운데를 자르고, 구성도·화면(fit)은 잘리지 않게 옅은 바탕 위에 통째로 넣는다.
# 사용: python tools/make_teasers.py   (아래 PICK 에서 프로젝트별로 몇 번째 사진을 어떤 방식으로 쓸지 정한다)
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "images", "portfolio")
W, H, BG = 800, 500, (243, 245, 248)

PICK = {
    "apex-a-ontology": (1, "fit"),
    "si-crm-server": (1, "fit"),
    "si-curved-spring": (1, "fit"),
    "si-cutting-tool-ai": (1, "photo"),
    "si-drying-temp-ai": (4, "fit"),
    "si-fems": (2, "fit"),
    "si-grind-inspection-darkroom": (1, "photo"),
    "si-grinder-ai": (2, "photo"),
    "si-load-control": (1, "fit"),
    "si-marking-vision": (3, "photo"),
    "si-ocr-mes": (4, "photo"),
    "si-press-vision": (2, "photo"),
    "si-smartfactory-rnd": (1, "fit"),
    "si-spring-inspection": (1, "photo"),
    "si-stpm": (1, "fit"),
    "si-spring-packaging": (1, "photo"),
    "apex-m-assembly-planning": (1, "fit"),
}


def photo(im):
    r = W / H
    w, h = im.size
    if w / h > r:
        nw = int(h * r); box = ((w - nw) // 2, 0, (w - nw) // 2 + nw, h)
    else:
        nh = int(w / r); box = (0, (h - nh) // 2, w, (h - nh) // 2 + nh)
    return im.crop(box).resize((W, H), Image.LANCZOS)


def fit(im, pad=0.06):
    bg = Image.new("RGB", (W, H), BG)
    im = im.copy(); im.thumbnail((int(W * (1 - 2 * pad)), int(H * (1 - 2 * pad))), Image.LANCZOS)
    bg.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
    return bg


for slug, (n, mode) in PICK.items():
    src = os.path.join(IMG, slug, f"{n:02d}.jpg")
    im = Image.open(src).convert("RGB")
    (photo if mode == "photo" else fit)(im).save(os.path.join(IMG, slug, "teaser.jpg"), quality=88)
    print(slug, n, mode)
