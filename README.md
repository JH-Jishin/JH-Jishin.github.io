# JH-Jishin.github.io — JISHIN Portfolio

테마는 [Minimal Mistakes 4.28.1](https://mmistakes.github.io/minimal-mistakes/)을 그대로 씁니다(`remote_theme`).
고친 건 색(#0C162A·#245CD1), 글꼴(Pretendard), 국문 줄바꿈, 로고뿐입니다.

## 프로젝트 하나 추가하기

1. `_portfolio/` 에 md 파일 하나를 만듭니다. 기존 파일을 복사해서 고치는 게 제일 빠릅니다.
2. 사진은 `assets/images/portfolio/<파일이름>/` 에 넣습니다.
   - `teaser.jpg` : 목록 카드 사진 (가로 16:10 권장)
   - `01.jpg`, `02.jpg` … : 상세 페이지 사진 원본
   - `01-th.jpg`, `02-th.jpg` … : 갤러리 썸네일 (600px 폭 정도)
3. 머리말(front matter)만 채우면 목록·상세 페이지가 알아서 나옵니다.

```yaml
title: "자동차부품 A사 (프로젝트 이름)"   # 「고객(프로젝트)」 형식, 고객은 반드시 가린 이름
kind: si                                 # apex-os 또는 si
status: done                             # done(완료) 또는 ongoing(진행 중) — 카드 배지·거르기 버튼에 쓰임
solution: cv                             # 분야(상단 탭): onto · cv · ts · sw (_data/solutions.yml)
types: ["Computer Vision"]               # 카드에 붙는 기술 칩(여러 개 가능)
featured: true                           # 홈 «주요 사례»에 올릴 때만
order: 3                                 # 목록 순서 (작을수록 앞)
excerpt: "카드에 보이는 한 줄 요약"
header:
  teaser: /assets/images/portfolio/si-a/teaser.jpg
sidebar:                                 # 상세 페이지 왼쪽 정보칸
  - title: "고객"
    text: "자동차부품 1차 협력사"
  - title: "기간"
    text: "2025.09 ~ 2026.03"
gallery:                                 # 사진 개수 제한 없음
  - url: /assets/images/portfolio/si-a/01.jpg
    image_path: /assets/images/portfolio/si-a/01-th.jpg
    alt: "현장 사진 01"
    title: "사진 설명"
```

## 사이트 구조

상단 탭 = 분야. `_data/solutions.yml` 의 key 와 프로젝트의 `solution:` 이 맞으면 그 탭에 자동으로 들어갑니다.
- **APEX OS** (`/apex-os/`, solution: onto): 제품 설명(`_data/apex.yml`) + 아래 도입 사례
- **Computer Vision** (`/computer-vision/`, solution: cv)
- **Time Series** (`/time-series/`, solution: ts) — 예지보전·공정 최적화
- **Software** (`/software/`, solution: sw) — MES·FEMS·CRM

## 사진 바꾸기

`tools/set_gallery.py` 에 JSON 으로 «원본 사진 경로 + 설명»을 넘기면 썸네일·대표 사진·md 의 gallery 까지 한 번에 다시 깝니다.
사진은 넣기 전에 고객사 로고·회사명·품번·주소창을 잘라내거나 덧칠해 둡니다.

## 영문 페이지

영문은 `_portfolio_en/` 에 따로 있고 `/en/` 아래로 나갑니다. 직접 고치지 말고
`tools/en_content.py`(영문 원고)를 고친 뒤 `python tools/build_en.py` 를 돌립니다.
사진·순서·상태는 국문 파일에서 그대로 가져오므로, 국문에 프로젝트를 추가하면 en_content.py 에도 같은 이름으로 원고를 넣어야 합니다(빠지면 스크립트가 알려 줌).


## 로컬에서 미리보기

```bash
bundle install
bundle exec jekyll serve      # http://localhost:4000
```

## 사진 자리표시자

지금 들어 있는 회색 「이미지 대기」 사진은 `tools/make_placeholders.py` 로 만든 임시 파일입니다. 실제 사진으로 덮어쓰면 됩니다.
