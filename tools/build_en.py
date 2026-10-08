# 국문 _portfolio/*.md 의 사진·순서·상태를 그대로 쓰고 문구만 en_content.py 로 바꿔 _portfolio_en/*.md 를 만든다
# 사용: python tools/build_en.py   (국문을 고친 뒤 en_content.py 도 고치고 다시 돌린다)
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from en_content import CAPTION, LABEL, METRIC, PAGES, VALUE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, DST = os.path.join(ROOT, "_portfolio"), os.path.join(ROOT, "_portfolio_en")
os.makedirs(DST, exist_ok=True)
missing = []

for f in sorted(os.listdir(SRC)):
    slug = f[:-3]
    if slug not in PAGES:
        missing.append(f"{slug}: 영문 원고 없음")
        continue
    title, excerpt, body = PAGES[slug]
    fm = open(os.path.join(SRC, f), encoding="utf-8").read().split("---\n", 2)[1]
    fm = re.sub(r'^title: ".*"$', lambda _: f'title: "{title}"', fm, flags=re.M)
    fm = re.sub(r'^excerpt: ".*"$', lambda _: f'excerpt: "{excerpt}"', fm, flags=re.M)

    def tr(m):
        key, val = m.group(1), m.group(2)
        out = CAPTION.get(val) or VALUE.get(val) or LABEL.get(val) or METRIC.get(val) or val
        if out == val and re.search("[가-힣]", val):
            missing.append(f"{slug}: {val}")
        return f'{key}"{out}"'

    fm = re.sub(r'^(\s*(?:- )?(?:title|text|alt|label|note|value): )"(.*)"$', tr, fm, flags=re.M)
    gallery = "\n\n{% include gallery %}\n" if "gallery:" in fm else "\n"
    with open(os.path.join(DST, f), "w", encoding="utf-8") as out:
        out.write(f"---\n{fm}---\n\n{body.strip()}{gallery}")

for name in sorted(os.listdir(DST)):
    if name not in os.listdir(SRC):
        os.remove(os.path.join(DST, name))
print("빠진 번역:", missing or "없음")
