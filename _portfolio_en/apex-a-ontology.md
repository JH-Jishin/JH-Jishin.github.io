---
title: "Company D (Ontology platform linking work orders, material lots and machine conditions)"
status: ongoing
types: ["Ontology", "LLM · Agent"]
solution: onto
featured: true
kind: apex-os
order: 1
excerpt: "Work orders, demand, inventory, defect records and machine conditions in one ontology, queried together with a single question"
sidebar:
  - title: "Client"
    text: "Automotive spring maker"
  - title: "Techniques"
    text: "Ontology · LLM Agent · Root-cause Tracing"
  - title: "Period"
    text: "2025.09 ~"
  - title: "Status"
    text: "Pilot on live data"
header:
  teaser: /assets/images/portfolio/apex-a-ontology/teaser.jpg
gallery:
  - url: /assets/images/portfolio/apex-a-ontology/01.jpg
    image_path: /assets/images/portfolio/apex-a-ontology/01-th.jpg
    alt: "From anomaly detection to tracing the root-cause lot"
    title: "From anomaly detection to tracing the root-cause lot"
  - url: /assets/images/portfolio/apex-a-ontology/02.jpg
    image_path: /assets/images/portfolio/apex-a-ontology/02-th.jpg
    alt: "Production planning screens and data intake paths"
    title: "Production planning screens and data intake paths"
  - url: /assets/images/portfolio/apex-a-ontology/03.jpg
    image_path: /assets/images/portfolio/apex-a-ontology/03-th.jpg
    alt: "Work order status compiled from a natural-language query"
    title: "Work order status compiled from a natural-language query"
---

We tied together the MES, ERP (SAP), SCADA and quality data of Company D's Plant 1 in a single ontology and are validating it on live data. Work orders, demand, capacity and inventory sit on the same object model, so when someone asks a question in plain language, APEX OS queries the systems together and answers.

### Monitoring dashboard
OEE, inventory, delivery and defect rate (PPM) are judged automatically and sorted into critical, warning and normal.

### Anomaly detection agent
When the defect rate crosses its limit, the agent traces MES, ERP and SCADA history back to narrow down the suspect material lot and reports with the evidence.

### Production planning
Reading work orders, demand, capacity and inventory together, it totals volume by line and works out line assignment, sequence and cost. One natural-language query organized 46 work orders covering 131,166 units and flagged that more than half of the volume was still waiting.

### Results
- Four systems (MES, ERP, SCADA, quality) linked in one ontology
- One natural-language query compiled 46 work orders covering 131,166 units

{% include gallery %}
