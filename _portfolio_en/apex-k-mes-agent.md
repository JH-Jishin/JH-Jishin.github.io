---
title: "Company K (MES-connected AI Q&A and run/idle monitoring)"
status: ongoing
types: ["Ontology", "LLM · Agent"]
solution: onto
kind: apex-os
order: 3
excerpt: "Cleans MES data into an ontology and builds run/idle monitoring, AI Q&A that shows its evidence, and automated reporting"
sidebar:
  - title: "Client"
    text: "Automotive connector and electrical parts maker"
  - title: "Techniques"
    text: "Ontology · LLM Agent · MES Integration"
  - title: "Period"
    text: "2026.10 ~ 2027.02"
  - title: "Status"
    text: "Build started"
header:
  teaser: /assets/images/portfolio/apex-k-mes-agent/teaser.jpg
gallery:
  - url: /assets/images/portfolio/apex-k-mes-agent/01.jpg
    image_path: /assets/images/portfolio/apex-k-mes-agent/01-th.jpg
    alt: "Live run/idle monitoring (sample screen)"
    title: "Live run/idle monitoring (sample screen)"
  - url: /assets/images/portfolio/apex-k-mes-agent/02.jpg
    image_path: /assets/images/portfolio/apex-k-mes-agent/02-th.jpg
    alt: "AI Q&A with traceable evidence (sample screen)"
    title: "AI Q&A with traceable evidence (sample screen)"
  - url: /assets/images/portfolio/apex-k-mes-agent/03.jpg
    image_path: /assets/images/portfolio/apex-k-mes-agent/03-th.jpg
    alt: "Team KPI dashboard (sample screen)"
    title: "Team KPI dashboard (sample screen)"
  - url: /assets/images/portfolio/apex-k-mes-agent/04.jpg
    image_path: /assets/images/portfolio/apex-k-mes-agent/04-th.jpg
    alt: "Mold shot-count alerts (sample screen)"
    title: "Mold shot-count alerts (sample screen)"
---

Company K runs stamping, injection, plating and assembly. Each team downloaded MES data into Excel to build PowerPoint reports, taking around three hours per regular report. Utilization was only totaled per day, so day and night shifts couldn't be separated, and planned stops mixed with real downtime made utilization look lower than it was. There was no alert when a mold's shot count passed its limit.

### What we are building
Plant MES data is moved into a cleaned database for AI and tied into the APEX OS ontology, so screens, reports and Q&A all read the same data. It is installed on premises.

- Live run/idle, labor-hour and materials/warehouse monitoring
- AI Q&A that answers with the evidence: which data was queried and how
- Team KPI dashboards and automatic weekly and monthly reports
- Mold shot-count alerts and draft repair requests


### Results
- Built for three plants
- Regular report preparation 3 hours → 20–30 minutes (target)

{% include gallery %}
