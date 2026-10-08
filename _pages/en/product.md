---
title: "Product"
permalink: /en/product/
layout: splash
kind: product
---

{%- assign cname = "portfolio_en" -%}
<nav class="area-filter area-jump">
  {%- for s in site.data.solutions %}{% unless s.key == "onto" %}
  <a href="#{{ s.key }}">{{ s.name.en }} <span>{{ site[cname] | where: "solution", s.key | size }}</span></a>
  {%- endunless %}{% endfor %}
</nav>

{%- for s in site.data.solutions %}{% unless s.key == "onto" %}
<section class="product-area portfolio-section" id="{{ s.key }}">
  <div class="product-area__head">
    <h2>{{ s.name.en }}</h2>
    <p>{{ s.title.en }}</p>
  </div>
  {% include portfolio-grid.html solution=s.key compact=true collection=cname %}
</section>
{%- endunless %}{% endfor %}
