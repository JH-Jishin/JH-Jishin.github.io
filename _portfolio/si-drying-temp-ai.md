---
title: "S사 (펄프몰딩 건조라인 AI 최적 온도 추천·이상 감시 시스템)"
status: done
types: ["Time Series", "Optimization · Control"]
solution: ts
featured: true
kind: si
order: 1
excerpt: "건조라인 온도 센서 20개를 1초 단위로 읽어 Zone별 최소 건조 온도를 추천하고 가스 사용량을 3.46% 줄였습니다"
sidebar:
  - title: "고객"
    text: "펄프몰딩 포장재 제조사"
  - title: "기술"
    text: "Regression (LightGBM) · Anomaly Detection · Process Optimization"
  - title: "사업"
    text: "제조AI 현장 적용 지원사업"
  - title: "기간"
    text: "2025.12 ~ 2026.08"
  - title: "상태"
    text: "완료"
header:
  teaser: /assets/images/portfolio/si-drying-temp-ai/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-drying-temp-ai/01.jpg
    image_path: /assets/images/portfolio/si-drying-temp-ai/01-th.jpg
    alt: "건조 라인 데이터 흐름과 MES 연동 구성"
    title: "건조 라인 데이터 흐름과 MES 연동 구성"
  - url: /assets/images/portfolio/si-drying-temp-ai/02.jpg
    image_path: /assets/images/portfolio/si-drying-temp-ai/02-th.jpg
    alt: "건조 공정 실시간 대시보드(Zone별 AI 추천온도)"
    title: "건조 공정 실시간 대시보드(Zone별 AI 추천온도)"
  - url: /assets/images/portfolio/si-drying-temp-ai/03.jpg
    image_path: /assets/images/portfolio/si-drying-temp-ai/03-th.jpg
    alt: "AI 솔루션 기술 구성"
    title: "AI 솔루션 기술 구성"
  - url: /assets/images/portfolio/si-drying-temp-ai/04.jpg
    image_path: /assets/images/portfolio/si-drying-temp-ai/04-th.jpg
    alt: "건조라인 Zone 구성과 센서 위치"
    title: "건조라인 Zone 구성과 센서 위치"
---

펄프몰딩 제품을 말리는 건조라인은 24시간 돌아갑니다. Zone별 설정온도는 담당자 경험으로 정해 두고 거의 바꾸지 않았습니다. 라인이 멈춰도 버너는 계속 탔습니다. 온도 센서는 값을 보여 주는 데만 쓰였습니다.

건조라인 5개 Zone, 높이별 4곳에 온도 센서 20개를 1초 주기로 수집하고 외기 온·습도 센서를 더했습니다. 데이터는 PLC·HMI에서 현장 AI PC로 모은 뒤 클라우드에 이중으로 저장합니다. 센서마다 LightGBM 회귀 모델을 두고 잔차가 ±3σ를 넘으면 이상으로 알립니다. 품질 OK/NG는 30분 단위 파생 피처 38종으로 판정합니다. 온도 변위 실험 1,000건과 Grid Search로 Zone별 최소 건조 온도를 찾아 매일 아침 6시 대시보드에 추천온도로 띄웁니다.

### 결과 (2025년 6월 대비 2026년 6월, 생산 1매당 기준)

- 가스 사용량 3.46% 절감: 0.00935 → 0.00903 m³/매 (목표 2.5%)
- 공정 불량률 0.58% → 0.27% (목표 0.3% 이하)
- 이상 탐지 AUC-ROC 0.990(합성 이상 기준), 품질 판정 F1 0.90

{% include gallery %}
