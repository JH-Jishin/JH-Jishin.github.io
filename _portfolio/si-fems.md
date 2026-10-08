---
title: "E사 (한전 요금 연동 실시간 공장 에너지 관리 FEMS)"
status: done
types: ["Software"]
solution: sw
kind: si
order: 4
excerpt: "설비별 실시간 전력과 비효율 사용량을 배치도 위에서 보고 한전 요금과 탄소배출 집약도까지 한 화면에서 관리합니다"
sidebar:
  - title: "고객"
    text: "분말·코팅 소재 제조사"
  - title: "기술"
    text: "Energy Monitoring · KEPCO OpenAPI · Demand Forecast"
  - title: "사업"
    text: "레전드50+ 지역특화 스마트공장 구축사업"
  - title: "기간"
    text: "2025.06 ~ 2026.03"
  - title: "상태"
    text: "운영 중"
header:
  teaser: /assets/images/portfolio/si-fems/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-fems/01.jpg
    image_path: /assets/images/portfolio/si-fems/01-th.jpg
    alt: "도면 위 설비별 에너지 모니터링"
    title: "도면 위 설비별 에너지 모니터링"
  - url: /assets/images/portfolio/si-fems/02.jpg
    image_path: /assets/images/portfolio/si-fems/02-th.jpg
    alt: "유효·비효율 사용량 리포트"
    title: "유효·비효율 사용량 리포트"
  - url: /assets/images/portfolio/si-fems/03.jpg
    image_path: /assets/images/portfolio/si-fems/03-th.jpg
    alt: "한전 사용량·요금 화면"
    title: "한전 사용량·요금 화면"
  - url: /assets/images/portfolio/si-fems/04.jpg
    image_path: /assets/images/portfolio/si-fems/04-th.jpg
    alt: "설비 심볼 8종"
    title: "설비 심볼 8종"
metrics:
  - value: "15분"
    label: "한전 계량 데이터 자동 수집 주기"
  - value: "10대"
    label: "실시간 계측 설비"
  - value: "7개"
    label: "에너지 관리 화면"
---
분말 공정(비드밀)과 코팅 공정(플라즈마)을 가진 공장에 MES와 함께 에너지 관리 시스템(FEMS)을 구축했습니다. 데이터 수집 장비와 DB는 고객사가 맡고 화면과 백엔드, AI는 지신이 만들었습니다.

### 도면 위에서 보는 설비별 에너지
공장 도면을 배경으로 올리고 설비를 끌어다 놓으면 설비마다 실시간 전력(kW)과 유효·비효율 사용량이 그 자리에 표시됩니다. 좌표를 도면 대비 비율로 저장해 화면 크기가 달라도 위치가 어긋나지 않습니다. 설비 모니터링, 알람 로그(월별 Top3·발생 통계), 설비별·전체 리포트, 한전 사용량 보기, 탄소배출 집약도, 에너지 수요 예측까지 7개 화면으로 구성했습니다.

### 한전 데이터 연동
한전 파워플래너 OpenAPI의 계약자 정보·월별 청구·15분 계량 데이터를 연결했습니다. 15분 계량값은 서버가 자동으로 모아 실시간 사용량과 예상 요금, 탄소 집약도 계산에 씁니다. 수요 예측 화면에서는 계약전력과 단가를 바꿔 요금이 어떻게 달라지는지 미리 계산해 볼 수 있습니다.

{% include gallery %}
