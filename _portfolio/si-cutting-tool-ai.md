---
title: "S사 (머시닝센터 절삭공구 오배치 감지 비전 AI·FOCAS 교차검증)"
status: done
types: ["Computer Vision"]
solution: cv
featured: true
kind: si
order: 4
excerpt: "공구가 잘못 꽂힌 채 가공에 들어가기 전에 비전 AI와 설비 데이터로 잡아냅니다"
sidebar:
  - title: "고객"
    text: "자동차 부품용 프레스 금형 제조사"
  - title: "기술"
    text: "Object Detection (YOLO) · FANUC FOCAS Cross-check"
  - title: "사업"
    text: "레전드50+ 2.0 · 데이터바우처 · 명품강소기업 자율지원"
  - title: "기간"
    text: "2025.07 ~"
  - title: "상태"
    text: "1단계 완료 · 2단계 진행 중"
header:
  teaser: /assets/images/portfolio/si-cutting-tool-ai/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-cutting-tool-ai/01.jpg
    image_path: /assets/images/portfolio/si-cutting-tool-ai/01-th.jpg
    alt: "머시닝센터 옆 키오스크와 타워램프"
    title: "머시닝센터 옆 키오스크와 타워램프"
  - url: /assets/images/portfolio/si-cutting-tool-ai/02.jpg
    image_path: /assets/images/portfolio/si-cutting-tool-ai/02-th.jpg
    alt: "공구 교환 장치를 비추는 카메라 설치"
    title: "공구 교환 장치를 비추는 카메라 설치"
  - url: /assets/images/portfolio/si-cutting-tool-ai/03.jpg
    image_path: /assets/images/portfolio/si-cutting-tool-ai/03-th.jpg
    alt: "실시간 관제 화면(공구번호·좌표)"
    title: "실시간 관제 화면(공구번호·좌표)"
---
머시닝센터 자동 공구 교환 장치(ATC)에 작업자가 밀링 아버를 손으로 꽂다 보면 빠뜨리거나 잘못 꽂는 일이 생기고 그대로 가공에 들어가면 주축 충돌로 이어집니다. 로봇식 대안은 수억 원대라 중소 금형사가 들이기 어렵습니다.

머시닝센터 2대에 카메라와 키오스크, 타워램프를 달았습니다. YOLO 기반 모델이 공구 5종과 미체결 상태를 구분하고 FANUC FOCAS로 받은 공구번호·좌표·스핀들 데이터와 맞춰 본 뒤 잘못 꽂혔으면 경보를 띄웁니다. 1호기는 내부망에서 연산하는 현장형, 2호기는 클라우드형으로 구성했습니다. 원천 이미지 6만여 장에서 2,555장을 골라 라벨링했고 야간 데이터까지 학습했습니다.

### 확장
작업지시서와 교차검증하고 관제 대상을 6대로 넓히는 통합 관제 시스템을 개발하고 있습니다.

### 결과
- 공구 오배치 검출 정확도 95% 이상 (자체 시험 mAP@0.5 0.95, F1 0.932)
- 머시닝센터 2대 현장 가동, 특허 2건 출원

{% include gallery %}
