---
title: "Company S (Sequence-driven assembly planning automation)"
status: ongoing
types: ["Ontology"]
solution: onto
kind: apex-os
order: 2
excerpt: "Moves assembly planning that one planner ran in Excel onto the ontology and builds up expert decisions as history for recommendations"
sidebar:
  - title: "Client"
    text: "Automotive mirror parts maker"
  - title: "Techniques"
    text: "Ontology · Rule Extraction · Planning Simulation"
  - title: "Period"
    text: "2026.08 ~"
  - title: "Status"
    text: "Build in progress"
header:
  teaser: /assets/images/portfolio/apex-m-assembly-planning/teaser.jpg
gallery:
  - url: /assets/images/portfolio/apex-m-assembly-planning/01.jpg
    image_path: /assets/images/portfolio/apex-m-assembly-planning/01-th.jpg
    alt: "Where expert judgment shapes each stage of the plan"
    title: "Where expert judgment shapes each stage of the plan"
  - url: /assets/images/portfolio/apex-m-assembly-planning/02.jpg
    image_path: /assets/images/portfolio/apex-m-assembly-planning/02-th.jpg
    alt: "How APEX OS builds up expert judgment"
    title: "How APEX OS builds up expert judgment"
  - url: /assets/images/portfolio/apex-m-assembly-planning/03.jpg
    image_path: /assets/images/portfolio/apex-m-assembly-planning/03-th.jpg
    alt: "Theoretical-inventory logic as a node graph"
    title: "Theoretical-inventory logic as a node graph"
---

Company S makes automotive mirrors through injection molding, painting and assembly. The automaker's plan changes two to four times a day, and one planner spent three to four hours building each assembly plan in an Excel workbook. Decisions such as how to split work into shifts relied on experienced staff, model by model.

### What we are building
Theoretical inventory is confirmed from customer sequences (previous stock + previous plan − actuals − unproduced), short specs are flagged, and the system generates shift-by-shift work orders and the SAP upload file. MES, SAP, paint-shop SCADA, customer sequences and Excel planning files are tied together in the APEX OS ontology, and the decisions experts make — with their reasons — are kept as history to inform the next plan. The planner sees the evidence for each step beside the result, compares it with their own estimate, and then confirms.

### Results
- Matched the existing workbook: theoretical inventory 52/52, remaining and shortage 312/312, same-day plan decisions 416/416
- Daily planning time 8.0 h → 1.5 h (target)

### Next step
After a first demo, it will be validated in Shadow Mode alongside the current method and then put into production.

{% include gallery %}
