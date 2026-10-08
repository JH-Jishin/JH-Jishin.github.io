---
title: "C사 (프레스 성형품 AI 비전 불량 검출·자동 선별)"
status: done
types: ["Computer Vision"]
solution: cv
kind: si
order: 15
excerpt: "프레스로 찍어 낸 부품의 홀 누락과 크랙을 비전 AI로 잡아 컨베이어에서 바로 걸러 냅니다"
sidebar:
  - title: "고객"
    text: "자동차 부품 프레스 성형 제조사"
  - title: "기술"
    text: "Defect Detection · Machine Vision"
  - title: "사업"
    text: "2025년 포스코 대·중소 상생형 스마트공장"
  - title: "기간"
    text: "2026.01 ~ 2026.03"
  - title: "상태"
    text: "완료"
header:
  teaser: /assets/images/portfolio/si-press-vision/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-press-vision/01.jpg
    image_path: /assets/images/portfolio/si-press-vision/01-th.jpg
    alt: "가장자리 크랙 촬영 원본"
    title: "가장자리 크랙 촬영 원본"
  - url: /assets/images/portfolio/si-press-vision/02.jpg
    image_path: /assets/images/portfolio/si-press-vision/02-th.jpg
    alt: "컨베이어·암실 검사장치 구성"
    title: "컨베이어·암실 검사장치 구성"
  - url: /assets/images/portfolio/si-press-vision/03.jpg
    image_path: /assets/images/portfolio/si-press-vision/03-th.jpg
    alt: "Vision AI 시스템 아키텍처"
    title: "Vision AI 시스템 아키텍처"
---

프레스로 성형한 부품은 홀이 빠지거나 가장자리에 크랙이 생겨도 눈으로 하나하나 확인해야 했습니다.

컨베이어 위에 암실형 검사장치를 올리고, 산업용 카메라로 부품을 찍어 AI가 홀 유무와 크랙을 판정하게 했습니다. 불량이 나오면 LS PLC 통신으로 버저를 울리고 해당 부품을 걸러 내며, 검사 결과는 대시보드에 쌓입니다.

{% include gallery %}
