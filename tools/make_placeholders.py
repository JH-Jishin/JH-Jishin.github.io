# 회색 「이미지 대기」 자리표시자 사진을 만든다. 사용: python tools/make_placeholders.py <폴더이름> <사진개수>
import os, sys
from PIL import Image, ImageDraw, ImageFont

FONT = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts\Pretendard-Medium.otf")

def placeholder(path, w, h, label):
    im = Image.new("RGB", (w, h), (236, 238, 242))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w - 1, h - 1], outline=(210, 214, 222), width=max(2, w // 400))
    f = ImageFont.truetype(FONT, max(18, w // 28)) if os.path.exists(FONT) else ImageFont.load_default()
    d.text(((w - d.textlength(label, font=f)) / 2, h / 2 - w // 50), label, fill=(140, 146, 158), font=f)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, quality=82)

if __name__ == "__main__":
    slug, n = sys.argv[1], int(sys.argv[2])
    base = f"assets/images/portfolio/{slug}"
    placeholder(f"{base}/teaser.jpg", 800, 500, "대표 이미지 대기")
    for i in range(1, n + 1):
        placeholder(f"{base}/{i:02d}.jpg", 1600, 1000, f"현장 사진 {i:02d} 대기")
        placeholder(f"{base}/{i:02d}-th.jpg", 600, 375, f"사진 {i:02d} 대기")
