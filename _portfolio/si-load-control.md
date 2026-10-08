---
title: "D사 (Stroke-Load 곡선 기반 냉간 세팅 하중 자동 보정 AI)"
status: ongoing
types: ["Time Series", "Optimization · Control"]
solution: ts
kind: si
order: 8
excerpt: "작업자 숙련도에 따라 달라지던 하중을 AI 보정값으로 맞춥니다"
sidebar:
  - title: "고객"
    text: "자동차 스프링 제조사"
  - title: "기술"
    text: "Regression · Closed-loop PLC Control"
  - title: "기간"
    text: "2026"
  - title: "상태"
    text: "모델 개발 중"
header:
  teaser: /assets/images/portfolio/si-load-control/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-load-control/01.jpg
    image_path: /assets/images/portfolio/si-load-control/01-th.jpg
    alt: "하중-스트로크 측정 곡선"
    title: "하중-스트로크 측정 곡선"
---
냉간 세팅 공정에는 하중 조절 장치가 있지만, 작업자 숙련도에 따라 결과 하중이 달라졌습니다.

설비 로그 5,609사이클의 Stroke-Load 곡선을 분석해 하중을 좌우하는 변수를 찾았습니다. AI가 RAM·Stroke 보정값을 계산해 PLC로 넘기는 구조를 만들고 있습니다. 현장에 넣기 전에는 실제 제어 없이 결과만 비교하는 Shadow Test로 검증합니다.

### 결과
- 셋팅 로그 5,609사이클을 분석해 하중을 좌우하는 변수 도출

{% include gallery %}
