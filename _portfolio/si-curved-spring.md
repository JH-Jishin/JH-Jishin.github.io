---
title: "D사 (곡률 고려 포토메트릭 AI 비전 자동 취출 시스템)"
status: ongoing
types: ["Computer Vision"]
solution: cv
featured: true
kind: si
order: 5
excerpt: "정상품만으로 기준을 세워 휘어진 스프링의 형상·외관 불량을 전수 판정하고 불량품을 자동으로 빼냅니다"
sidebar:
  - title: "고객"
    text: "자동차 스프링 제조사"
  - title: "기술"
    text: "Photometric Imaging · Anomaly Detection · SPC"
  - title: "기간"
    text: "2026.04 ~"
  - title: "상태"
    text: "설치 완료 · 시양산 준비"
header:
  teaser: /assets/images/portfolio/si-curved-spring/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-curved-spring/01.jpg
    image_path: /assets/images/portfolio/si-curved-spring/01-th.jpg
    alt: "직접 제작한 암실 검사장치"
    title: "직접 제작한 암실 검사장치"
  - url: /assets/images/portfolio/si-curved-spring/02.jpg
    image_path: /assets/images/portfolio/si-curved-spring/02-th.jpg
    alt: "암실 검사 시스템 구성"
    title: "암실 검사 시스템 구성"
  - url: /assets/images/portfolio/si-curved-spring/03.jpg
    image_path: /assets/images/portfolio/si-curved-spring/03-th.jpg
    alt: "모니터링 화면(A·B열 판정)"
    title: "모니터링 화면(A·B열 판정)"
  - url: /assets/images/portfolio/si-curved-spring/04.jpg
    image_path: /assets/images/portfolio/si-curved-spring/04-th.jpg
    alt: "3색 조명 암실 설계"
    title: "3색 조명 암실 설계"
  - url: /assets/images/portfolio/si-curved-spring/05.jpg
    image_path: /assets/images/portfolio/si-curved-spring/05-th.jpg
    alt: "정상 기준 대비 이상 부위 시각화"
    title: "정상 기준 대비 이상 부위 시각화"
---
커브드 스프링은 휘어진 형태라 곡률과 피치가 고르게 나와야 합니다. 그동안은 숙련 작업자가 감으로 설비를 조정하고 일부만 샘플링 검사해 불량을 늦게 발견할 때가 있었습니다.

암실 안에서 조명 4개를 차례로 켜며 찍은 이미지를 합성해 스프링의 형상과 표면을 한 장에 또렷하게 담습니다. 불량 데이터가 거의 없는 현장이라 정상품만으로 기준을 세웁니다. 품번별 정상 기준과 비교해 형상이 얼마나 벗어났는지(z-점수)를 보고 정상품으로 학습한 모델의 재구성 오차로 국부 외관 결함을 잡습니다. 판정 결과는 PLC로 넘겨 불량품을 라인 밖으로 빼내고 성형 offset 보정값도 함께 보냅니다. 모니터링 화면에서는 SPC 관리도와 Cp·Cpk로 공정 상태를 봅니다.

암실 검사장치와 전용 컨베이어는 지신이 직접 설계·제작했고, 2026년 6월 설치와 PLC 연결을 마쳤습니다.

### 결과
- 내부 시험에서 실물 불량 19건 모두 검출, 양품 오검출 0.17%
- 장당 판정 0.11~0.19초 (허용 0.3초)

{% include gallery %}
