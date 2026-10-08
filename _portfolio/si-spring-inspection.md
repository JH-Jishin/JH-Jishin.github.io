---
title: "D사 (Edge AI 다채널 비전 스프링 전수검사·라인 인터락 시스템)"
status: done
types: ["Computer Vision"]
solution: cv
featured: true
kind: si
order: 2
excerpt: "카메라 30대로 열처리 이상과 외관 불량을 실시간으로 잡고 이상이 나면 PLC 인터락으로 설비를 바로 세웁니다"
sidebar:
  - title: "고객"
    text: "자동차 스프링 제조사"
  - title: "기술"
    text: "Object Detection · Multi-Object Tracking · Anomaly Detection"
  - title: "기간"
    text: "2025.09 ~ 2026"
  - title: "상태"
    text: "양산 적용·시양산"
header:
  teaser: /assets/images/portfolio/si-spring-inspection/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-spring-inspection/01.jpg
    image_path: /assets/images/portfolio/si-spring-inspection/01-th.jpg
    alt: "정면 카메라 스테이지 설치"
    title: "정면 카메라 스테이지 설치"
  - url: /assets/images/portfolio/si-spring-inspection/02.jpg
    image_path: /assets/images/portfolio/si-spring-inspection/02-th.jpg
    alt: "후공정 검사장치 현장 설치"
    title: "후공정 검사장치 현장 설치"
  - url: /assets/images/portfolio/si-spring-inspection/03.jpg
    image_path: /assets/images/portfolio/si-spring-inspection/03-th.jpg
    alt: "정면 영상 좌우 대칭(gap) 판정"
    title: "정면 영상 좌우 대칭(gap) 판정"
  - url: /assets/images/portfolio/si-spring-inspection/04.jpg
    image_path: /assets/images/portfolio/si-spring-inspection/04-th.jpg
    alt: "후공정 24캠 배치와 검사 화면"
    title: "후공정 24캠 배치와 검사 화면"
---

D사 2공장의 스프링 라인 두 곳에 비전 AI를 붙였습니다.

### 열처리 공정 실시간 이상 감시
코일 라인 정면에 5MP 머신비전 카메라 2대, 측면에 8MP 카메라 4대를 달았습니다. 정면 영상에서는 스프링과 양 끝단을 잡아 중심점 간 거리 차(gap)로 좌우 대칭을 판정합니다. 측면 영상에서는 다중 객체 추적(MOT)으로 스프링의 움직임과 간격, 돌발 스파크를 봅니다. 하나라도 어긋나면 Edge AI PC가 PLC 인터락으로 설비를 바로 세웁니다. 현장에서는 모델 6개가 돌고 작업자는 키오스크에서 작업지시 정보와 이상 횟수, 녹화 영상을 확인합니다.

### 후공정 외관 전수검사
좌우 라인에 카메라 24대를 배치해 하루 12만 개 스프링을 전부 찍고 연마 미흡·마킹 반대·부분 마킹을 비롯한 불량 22유형을 판정합니다. 하루 10~30건의 불량을 걸러 PLC 연동으로 라인 밖으로 빼냅니다. 시양산 기준 검출 정확도는 99.9%이고, 99.99%를 목표로 고도화하고 있습니다.

{% include gallery %}
