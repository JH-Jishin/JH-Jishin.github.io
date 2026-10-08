---
title: "K사 (MES 데이터 연동 AI 질의응답·가동/비가동 모니터링)"
status: ongoing
types: ["Ontology", "LLM · Agent"]
solution: onto
kind: apex-os
order: 3
excerpt: "MES 데이터를 정제해 온톨로지로 묶고, 가동·비가동 모니터링과 근거를 보여주는 AI 질의응답, 리포트 자동화를 만듭니다"
sidebar:
  - title: "고객"
    text: "자동차 커넥터·전장부품 제조사"
  - title: "기술"
    text: "Ontology · LLM Agent · MES Integration"
  - title: "기간"
    text: "2026.10 ~ 2027.02"
  - title: "상태"
    text: "구축 착수"
header:
  teaser: /assets/images/portfolio/apex-k-mes-agent/teaser.jpg
gallery:
  - url: /assets/images/portfolio/apex-k-mes-agent/01.jpg
    image_path: /assets/images/portfolio/apex-k-mes-agent/01-th.jpg
    alt: "실시간 가동·비가동 모니터링(화면 예시)"
    title: "실시간 가동·비가동 모니터링(화면 예시)"
  - url: /assets/images/portfolio/apex-k-mes-agent/02.jpg
    image_path: /assets/images/portfolio/apex-k-mes-agent/02-th.jpg
    alt: "근거를 보여주는 AI 질의응답(화면 예시)"
    title: "근거를 보여주는 AI 질의응답(화면 예시)"
  - url: /assets/images/portfolio/apex-k-mes-agent/03.jpg
    image_path: /assets/images/portfolio/apex-k-mes-agent/03-th.jpg
    alt: "팀별 KPI 대시보드(화면 예시)"
    title: "팀별 KPI 대시보드(화면 예시)"
  - url: /assets/images/portfolio/apex-k-mes-agent/04.jpg
    image_path: /assets/images/portfolio/apex-k-mes-agent/04-th.jpg
    alt: "금형 타발 알림(화면 예시)"
    title: "금형 타발 알림(화면 예시)"
---

K사는 프레스·사출·도금·조립 공정을 운영합니다. 팀마다 MES 데이터를 엑셀로 내려받아 PPT 보고서를 만드는 데 정기 보고 한 건에 3시간 안팎이 들었습니다. 가동률은 하루 단위로만 집계돼 주간·야간을 나눠 볼 수 없었고 계획된 정지와 실제 비가동이 섞여 가동률이 실제보다 낮게 보였습니다. 금형 타발 수가 기준을 넘어도 알림이 없었습니다.

### 만드는 것
공장 MES 데이터를 AI 전용 정제 DB로 옮기고 APEX OS 온톨로지로 묶어 화면·리포트·질의응답이 모두 같은 데이터를 보게 합니다. 사내 구축형으로 설치합니다.

- 실시간 가동·비가동, 노무공수, 자재·창고 모니터링
- 질문하면 어떤 데이터를 어떻게 조회했는지 근거와 함께 답하는 AI 질의응답
- 팀별 KPI 대시보드와 주간·월간 리포트 자동 생성
- 금형 타발 도달 알림과 수리 의뢰 초안

### 진행
2026년 8월 파일럿 킥오프를 거쳐 10월 계약을 맺고, 2027년 2월까지 공장 3곳을 대상으로 구축합니다.

{% include gallery %}
