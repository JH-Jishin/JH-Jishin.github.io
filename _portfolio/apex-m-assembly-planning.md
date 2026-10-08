---
title: "S사 (서열 기반 조립 생산계획 자동화)"
status: ongoing
types: ["Ontology"]
solution: onto
kind: apex-os
order: 2
excerpt: "엑셀 워크북과 메신저로 돌던 조립 생산계획을 온톨로지 위로 옮겨 서열 수집부터 작업지시까지 한 흐름으로 잇습니다"
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
    alt: "APEX Plan 생산계획 수립 구조"
    title: "APEX Plan 생산계획 수립 구조"
---

S사의 조립 생산계획은 담당자 한 사람의 엑셀 워크북으로 돌아갑니다. 매일 아침 완성차 고객사 포털에서 서열을 공장별로 내려받고 메신저로 통보된 불량을 손으로 옮겨 적은 뒤, 이론재고를 계산하고 부족한 사양을 찾아 작업지시서를 뽑습니다. 사양별 수량을 비율 하나로 끌어올리는 일부터 차수 배정, 대차 단위 분할, SAP 순서생산 업로드까지 사람이 직접 이어 붙입니다.

지신은 이 워크북의 수식과 라벨을 하나씩 풀어 담당자 인터뷰로 의미를 확정하고, 그 규칙을 APEX OS 온톨로지의 객체와 제약으로 옮기고 있습니다. MES 뷰 6종(생산실적·가동 이력·라인 상태·재고 2종·출고 이력)을 연결해 이론재고를 자동으로 맞춥니다. 1차 범위는 D+3 양산 수량을 입력해 결과를 기존 계획과 비교하는 데까지입니다. 계획 담당자가 직접 돌려 볼 수 있는 시뮬레이터 화면도 함께 만들고 있습니다.

### 진행
- 2026년 9월 온사이트 인터뷰 3회, 워크북 규칙 확인표 작성
- 조립 라인 다음으로 도장·사출 라인 계획까지 넓힐 예정

{% include gallery %}
