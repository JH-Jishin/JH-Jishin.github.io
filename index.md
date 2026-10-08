---
layout: splash
title: "JISHIN"
permalink: /
---

{%- assign cname = "portfolio" -%}

<div class="area-filter" role="group">
  <button type="button" data-area="all" aria-pressed="true">전체</button>
  {%- for s in site.data.solutions %}
  <button type="button" data-area="{{ s.key }}" aria-pressed="false">{% if s.key == "onto" %}APEX OS{% else %}{{ s.name.ko }}{% endif %}</button>
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
