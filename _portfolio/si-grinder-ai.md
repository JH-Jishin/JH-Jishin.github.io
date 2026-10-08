---
title: "D사 (스프링 연마 상태 비전 판정·연마석 자율 보정 AI)"
status: ongoing
types: ["Computer Vision", "Optimization · Control"]
solution: cv
kind: si
order: 6
excerpt: "연마면을 카메라로 읽어 연마석 6개의 위치를 자동으로 맞추고 작업자의 육안 세팅을 대신합니다"
sidebar:
  - title: "고객"
    text: "자동차 스프링 제조사"
  - title: "기술"
    text: "Segmentation · Closed-loop PLC Control"
  - title: "기간"
    text: "2026"
  - title: "상태"
    text: "현장 적용 중"
header:
  teaser: /assets/images/portfolio/si-grinder-ai/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-grinder-ai/01.jpg
    image_path: /assets/images/portfolio/si-grinder-ai/01-th.jpg
    alt: "스프링 끝단 연마면 판정"
    title: "스프링 끝단 연마면 판정"
  - url: /assets/images/portfolio/si-grinder-ai/02.jpg
    image_path: /assets/images/portfolio/si-grinder-ai/02-th.jpg
    alt: "연마면 분할 결과"
    title: "연마면 분할 결과"
  - url: /assets/images/portfolio/si-grinder-ai/03.jpg
    image_path: /assets/images/portfolio/si-grinder-ai/03-th.jpg
    alt: "연마면 반자동 라벨링"
    title: "연마면 반자동 라벨링"
---
스프링 양 끝단을 가는 연마기는 연마석 6개의 위치와 회전수를 작업자가 눈으로 보고 맞춰 왔습니다. 사람마다 세팅이 달라 품질 편차가 생겼습니다.

상단 카메라로 스프링 길이를 ±5mm 안에서 재고, 좌우 카메라로 연마면을 분할(mIoU 90% 이상 목표)해 연마도 점수를 매깁니다. 이 점수와 자유고 차이로 PLC 파라미터를 보정해 연마석을 자동으로 맞추고 스프링마다 양불 판정과 이력을 남깁니다. 2026년 7월 연마고 측정·보정을 현장에 적용했고 불량품 라인아웃도 함께 돌아가고 있습니다.

### 결과
- 스프링 길이를 ±5mm 안에서 측정하고 연마석 6개를 자동 보정
- 연마면 분할 정확도 mIoU 90% 이상을 목표로 고도화 중

{% include gallery %}
