---
title: "D사 (쇼트기·장입 로봇 시계열 AI 예지보전)"
status: done
types: ["Time Series"]
solution: ts
kind: si
order: 7
excerpt: "설비 20대의 진동·로봇 데이터 약 2천만 건으로 고장 징후를 먼저 알려 줍니다"
sidebar:
  - title: "고객"
    text: "자동차 스프링 제조사"
  - title: "기술"
    text: "GRU Seq2Seq · Anomaly Detection"
  - title: "기간"
    text: "2026"
  - title: "상태"
    text: "실증 완료"
header:
  teaser: /assets/images/portfolio/si-stpm/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-stpm/01.jpg
    image_path: /assets/images/portfolio/si-stpm/01-th.jpg
    alt: "예지보전 대시보드"
    title: "예지보전 대시보드"
  - url: /assets/images/portfolio/si-stpm/02.jpg
    image_path: /assets/images/portfolio/si-stpm/02-th.jpg
    alt: "sTPM 시스템 구성"
    title: "sTPM 시스템 구성"
  - url: /assets/images/portfolio/si-stpm/03.jpg
    image_path: /assets/images/portfolio/si-stpm/03-th.jpg
    alt: "실시간 종합 현황(OEE·잔여수명)"
    title: "실시간 종합 현황(OEE·잔여수명)"
---

D사 1공장의 쇼트기 20대(진동 센서 14대, 장입 로봇 6대)에서 10개월 동안 쌓인 약 2천만 건의 시계열 데이터로 GRU Seq2Seq 기반 이상 탐지 모델을 만들고 현장 실증을 마쳤습니다.

설비 배치도 대시보드에서 설비별 위험 스코어와 즉시 정비·점검이 필요한 건수를 한눈에 보고 이상 징후가 생기면 알림을 받습니다.

{% include gallery %}
