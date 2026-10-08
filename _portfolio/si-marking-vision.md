---
title: "D사 (스프링 색상 마킹 식별 비전 AI)"
status: done
types: ["Computer Vision"]
solution: cv
kind: si
order: 8
excerpt: "스프링에 찍힌 색상 마킹을 읽어 사양과 맞는지 확인합니다"
sidebar:
  - title: "고객"
    text: "자동차 스프링 제조사"
  - title: "기술"
    text: "Object Detection · Color Classification"
  - title: "상태"
    text: "완료"
header:
  teaser: /assets/images/portfolio/si-marking-vision/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-marking-vision/01.jpg
    image_path: /assets/images/portfolio/si-marking-vision/01-th.jpg
    alt: "마킹 검사 메인·리포트 화면"
    title: "마킹 검사 메인·리포트 화면"
  - url: /assets/images/portfolio/si-marking-vision/02.jpg
    image_path: /assets/images/portfolio/si-marking-vision/02-th.jpg
    alt: "마킹 검사 하드웨어(릴레이·키오스크·카메라)"
    title: "마킹 검사 하드웨어(릴레이·키오스크·카메라)"
  - url: /assets/images/portfolio/si-marking-vision/03.jpg
    image_path: /assets/images/portfolio/si-marking-vision/03-th.jpg
    alt: "색상 마킹 검출 결과"
    title: "색상 마킹 검출 결과"
---
스프링에는 차종과 하중 구분을 위한 색상 마킹이 찍힙니다. D사 1공장에서 카메라로 마킹의 위치와 색을 함께 검출해 사양과 맞는지 확인하도록 했습니다. 두 달간 PoC와 시운전을 거쳐 기존 비전 시스템을 대체했습니다.

### 결과
- 마킹 탐지 F1 0.987, 색상 분류 정확도 0.989 (자체 시험)
- PoC부터 기존 비전 시스템 대체까지 2개월

{% include gallery %}
