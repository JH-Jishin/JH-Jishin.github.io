---
title: "APEX OS"
permalink: /en/apex-os/
layout: splash
kind: product
excerpt: "A manufacturing operating system that ties shop-floor data into one ontology for planning, root-cause tracing, workflow improvement and simulation"
header:
  overlay_color: "#0C162A"
---

<p class="apex-lead">{{ site.data.apex.en.lead }}</p>

{% include apex-product.html lang="en" %}

<section class="portfolio-section apex-arch">
  <div class="portfolio-section__head">
    <h2 class="portfolio-section__title">Architecture</h2>
  </div>
  <figure class="portfolio-figure">
    <img src="{{ '/assets/images/apex-os-architecture.png' | relative_url }}" alt="APEX OS ontology system architecture">
    <figcaption>Scattered source databases are consolidated into one physical layer; on top of the ontology, people and AI query and act on the same definitions.</figcaption>
  </figure>
  <figure class="portfolio-figure">
    <img src="{{ '/assets/images/apex/s2_hub.jpg' | relative_url }}" alt="From siloed systems to a company-wide ontology">
    <figcaption>Data scattered across systems is tied into one ontology, and decisions and actions run on top of it.</figcaption>
  </figure>
  <figure class="portfolio-figure">
    <img src="{{ '/assets/images/apex/s4_offer.jpg' | relative_url }}" alt="Four APEX OS offerings">
    <figcaption>Planning (Plan), anomaly tracing (Trace), improvement suggestions (Advisor) and a digital twin (Twin) on a single ontology.</figcaption>
  </figure>
  <figure class="portfolio-figure">
    <img src="{{ '/assets/images/apex/s5_layers.jpg' | relative_url }}" alt="Five-layer structure and phased rollout">
    <figcaption>Five layers from data collection to visualization, rolled out step by step from assessment to group-wide expansion.</figcaption>
  </figure>
</section>


<section class="portfolio-section apex-cases">
  <div class="portfolio-section__head"><h2 class="portfolio-section__title">Deployments</h2></div>
  {% include portfolio-grid.html solution="onto" collection="portfolio_en" %}
</section>
