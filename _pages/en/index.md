---
layout: splash
title: "JISHIN"
permalink: /en/
---

{%- assign cname = "portfolio_en" -%}
{%- assign all = site[cname] -%}
{%- assign n_apex = all | where: "solution", "onto" | size -%}
{%- assign n_cv = all | where: "solution", "cv" | size -%}{%- assign n_ts = all | where: "solution", "ts" | size -%}{%- assign n_sw = all | where: "solution", "sw" | size -%}{%- assign n_prod = n_cv | plus: n_ts | plus: n_sw -%}

<section class="hero-mosaic">
  <div class="hero-mosaic__grid" aria-hidden="true">
    <span style="background-image:url('{{ '/assets/images/portfolio/si-spring-inspection/teaser.jpg' | relative_url }}')"></span>
    <span style="background-image:url('{{ '/assets/images/portfolio/si-cutting-tool-ai/teaser.jpg' | relative_url }}')"></span>
    <span style="background-image:url('{{ '/assets/images/portfolio/si-curved-spring/teaser.jpg' | relative_url }}')"></span>
    <span style="background-image:url('{{ '/assets/images/portfolio/si-ocr-mes/teaser.jpg' | relative_url }}')"></span>
    <span style="background-image:url('{{ '/assets/images/portfolio/si-grinder-ai/teaser.jpg' | relative_url }}')"></span>
    <span style="background-image:url('{{ '/assets/images/portfolio/si-press-vision/01.jpg' | relative_url }}')"></span>
  </div>
  <div class="hero-mosaic__text">
    <span>JISHIN</span>
    <h1>Portfolio</h1>
  </div>
</section>

<section class="gate">
  <a class="gate__panel gate__panel--apex" href="{{ '/en/apex-os/' | relative_url }}">
    <img src="{{ '/assets/images/apex/s2_hub.jpg' | relative_url }}" alt="">
    <span class="gate__label"><strong>APEX OS</strong><em>{{ n_apex }} Projects</em></span>
  </a>
  <div class="gate__panel gate__panel--product">
    <a class="gate__cover" href="{{ '/en/product/' | relative_url }}" style="background-image:url('{{ '/assets/images/portfolio/si-spring-inspection/teaser.jpg' | relative_url }}')">
      <span class="gate__label"><strong>Product</strong><em>{{ n_prod }} Projects</em></span>
    </a>
    <ul class="gate__areas">
      {%- for s in site.data.solutions %}{% unless s.key == "onto" %}
      <li><a href="{{ '/en/product/' | relative_url }}#{{ s.key }}">{{ s.name.en }}<span>{{ all | where: "solution", s.key | size }}</span></a></li>
      {%- endunless %}{% endfor %}
    </ul>
  </div>
</section>

<div class="area-filter" role="group">
  <button type="button" data-area="all" aria-pressed="true">All</button>
  {%- for s in site.data.solutions %}
  <button type="button" data-area="{{ s.key }}" aria-pressed="false">{% if s.key == "onto" %}APEX OS{% else %}{{ s.name.en }}{% endif %}</button>
  {%- endfor %}
</div>

<div class="home-cases portfolio-section">
  {% include portfolio-grid.html compact=true collection=cname %}
</div>

<script>
  (function () {
    var box = document.querySelector(".area-filter");
    box.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      box.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      document.querySelectorAll(".home-cases .grid__item").forEach(function (it) {
        it.hidden = !(b.dataset.area === "all" || it.dataset.solution === b.dataset.area);
      });
    });
  })();
</script>
