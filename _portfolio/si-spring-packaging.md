---
title: "D사 (AI 비전 스프링 포장 수량 자동 검사)"
status: ongoing
solution: cv
types: ["Computer Vision"]
kind: si
order: 10
excerpt: "포장된 스프링을 카메라로 찍어 AI가 수량을 세고 기준 수량과 맞는지 출하 전에 판정합니다"
sidebar:
  - title: "고객"
    text: "자동차 스프링 제조사"
  - title: "기술"
    text: "Object Counting · Machine Vision · DB Integration"
header:
  teaser: /assets/images/portfolio/si-spring-packaging/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-spring-packaging/01.jpg
    image_path: /assets/images/portfolio/si-spring-packaging/01-th.jpg
    alt: "라인에 설치한 포장 수량 검사장치"
    title: "라인에 설치한 포장 수량 검사장치"
  - url: /assets/images/portfolio/si-spring-packaging/02.jpg
    image_path: /assets/images/portfolio/si-spring-packaging/02-th.jpg
    alt: "포장 내 스프링 수량 AI 집계 화면"
    title: "포장 내 스프링 수량 AI 집계 화면"
---

### 도입 배경
스프링 포장 과정에서 작업자가 육안·수작업으로 수량을 확인하고 있어, 반복 작업에 따른 피로로 수량 집계 오류가 생길 수 있었습니다. 수량이 부족하거나 초과된 채 출하되면 고객사 클레임과 재작업 비용으로 이어집니다.

### 처리 과정
1. DB에서 현재 작업 중인 품번과 기준 포장 수량을 실시간으로 조회합니다.
2. 컨베이어로 이송되는 포장된 스프링을 설치된 카메라로 촬영합니다.
3. 촬영한 이미지를 AI로 분석해 포장 안의 스프링 수량을 셉니다.
4. 집계한 수량을 기준 포장 수량과 비교해 일치 여부를 판정합니다.

### 기대 효과
- 수작업으로 수량을 확인하던 작업자의 부담 감소
- 포장 수량의 누락·초과를 출하 전에 확인
- 수량 불일치로 인한 고객사 클레임과 재작업 비용 감소

{% include gallery %}
