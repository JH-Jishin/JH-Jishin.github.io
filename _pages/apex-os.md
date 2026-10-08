---
title: "APEX OS"
permalink: /apex-os/
layout: splash
kind: product
excerpt: "현장 데이터를 하나의 온톨로지로 묶어 계획·원인 추적·업무 개선·시뮬레이션을 돌리는 제조 운영체제"
header:
  overlay_color: "#0C162A"
---

<p class="apex-lead">{{ site.data.apex.ko.lead }}</p>

{% include apex-product.html lang="ko" %}

<section class="portfolio-section apex-arch">
  <div class="portfolio-section__head">
    <h2 class="portfolio-section__title">구조</h2>
  </div>
  <figure class="portfolio-figure">
    <img src="{{ '/assets/images/apex-os-architecture.png' | relative_url }}" alt="APEX OS 온톨로지 시스템 아키텍처">
    <figcaption>흩어진 원천 DB를 하나의 물리 레이어로 모으고, 온톨로지 위에서 사람과 AI가 같은 기준으로 조회·실행합니다.</figcaption>
  </figure>
  <figure class="portfolio-figure">
    <img src="{{ '/assets/images/apex/s2_hub.jpg' | relative_url }}" alt="분산 시스템에서 전사 온톨로지로">
    <figcaption>시스템마다 흩어진 데이터를 하나의 온톨로지로 묶고, 그 위에서 판단과 실행을 합니다.</figcaption>
  </figure>
  <figure class="portfolio-figure">
    <img src="{{ '/assets/images/apex/s4_offer.jpg' | relative_url }}" alt="APEX OS 4가지 Offering">
    <figcaption>생산계획(Plan), 이상 추적(Trace), 개선 제안(Advisor), 디지털 트윈(Twin)을 하나의 온톨로지 위에서 제공합니다.</figcaption>
  </figure>
  <figure class="portfolio-figure">
    <img src="{{ '/assets/images/apex/s5_layers.jpg' | relative_url }}" alt="APEX OS 5계층 구조와 단계별 도입">
    <figcaption>데이터 수집부터 시각화까지 5계층으로 나뉘고, 현황 진단에서 그룹 확산까지 단계적으로 도입합니다.</figcaption>
  </figure>
</section>


<section class="portfolio-section apex-cases">
  <div class="portfolio-section__head"><h2 class="portfolio-section__title">도입 사례</h2></div>
  {% include portfolio-grid.html solution="onto" %}
</section>
