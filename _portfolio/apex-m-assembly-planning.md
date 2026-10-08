---
title: "S사 (서열 기반 조립 생산계획 자동화)"
status: ongoing
types: ["Ontology"]
solution: onto
kind: apex-os
order: 2
excerpt: "담당자 한 사람의 엑셀로 짜던 조립 생산계획을 온톨로지로 옮기고, 숙련자 판단을 이력으로 쌓아 추천에 씁니다"
sidebar:
  - title: "고객"
    text: "자동차 미러 부품 제조사"
  - title: "기술"
    text: "Ontology · Rule Extraction · Planning Simulation"
  - title: "기간"
    text: "2026.08 ~"
  - title: "상태"
    text: "구축 진행 중"
header:
  teaser: /assets/images/portfolio/apex-m-assembly-planning/teaser.jpg
gallery:
  - url: /assets/images/portfolio/apex-m-assembly-planning/01.jpg
    image_path: /assets/images/portfolio/apex-m-assembly-planning/01-th.jpg
    alt: "발주에서 사출까지, 공정별 숙련자 판단"
    title: "발주에서 사출까지, 공정별 숙련자 판단"
  - url: /assets/images/portfolio/apex-m-assembly-planning/02.jpg
    image_path: /assets/images/portfolio/apex-m-assembly-planning/02-th.jpg
    alt: "숙련자 판단을 쌓는 APEX OS 구성"
    title: "숙련자 판단을 쌓는 APEX OS 구성"
  - url: /assets/images/portfolio/apex-m-assembly-planning/03.jpg
    image_path: /assets/images/portfolio/apex-m-assembly-planning/03-th.jpg
    alt: "이론재고를 계산하는 노드 그래프"
    title: "이론재고를 계산하는 노드 그래프"
---
S사는 사출·도장·조립을 거쳐 자동차 미러를 만듭니다. 완성차 고객사의 계획이 하루 2~4번 바뀌는데, 조립 생산계획은 담당자 한 사람이 엑셀 워크북으로 3~4시간씩 짜 왔습니다. 차수를 어떻게 나눌지 같은 판단은 차종마다 숙련자의 경험에 기대고 있었습니다.

### 만드는 것
고객 서열을 기준으로 이론재고를 확정하고(전일재고 + 전일계획 − 실적 − 미생산), 부족 사양을 판정해 차수별 작업지시와 SAP 업로드 파일까지 만듭니다. MES·SAP·도장 SCADA·고객 서열·엑셀 계획 파일을 APEX OS 온톨로지로 묶고, 숙련자가 내린 판단과 그 이유를 이력으로 쌓아 다음 계획 추천에 씁니다. 계획 담당자는 결과 옆에서 단계별 근거를 보고 자기 예상치와 나란히 비교한 뒤 확정합니다.

### 결과
- 기존 워크북 결과와 대조해 이론재고 52/52건, 잔여·부족 312/312건, 당일계획 판정 416/416건 일치
- 일 계획 수립 시간 8.0시간 → 1.5시간 (목표)

### 다음 단계
1차 데모 뒤 기존 방식과 병행하는 Shadow Mode로 검증하고 양산에 적용합니다.

{% include gallery %}
