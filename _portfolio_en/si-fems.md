---
title: "Company E (Real-time factory energy management (FEMS) linked to KEPCO tariffs)"
status: done
types: ["Software"]
solution: sw
kind: si
order: 4
excerpt: "Energy per machine on the floor plan, KEPCO tariff data and demand forecasting in one system"
sidebar:
  - title: "Client"
    text: "Powder & coating materials maker"
  - title: "Techniques"
    text: "Energy Monitoring · KEPCO OpenAPI · Demand Forecast"
  - title: "Program"
    text: "Legend 50+ Regional Smart Factory Program"
  - title: "Period"
    text: "2025.06 ~ 2026.03"
  - title: "Status"
    text: "In operation"
header:
  teaser: /assets/images/portfolio/si-fems/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-fems/01.jpg
    image_path: /assets/images/portfolio/si-fems/01-th.jpg
    alt: "Energy per machine on the floor plan"
    title: "Energy per machine on the floor plan"
  - url: /assets/images/portfolio/si-fems/02.jpg
    image_path: /assets/images/portfolio/si-fems/02-th.jpg
    alt: "Effective vs. wasted usage report"
    title: "Effective vs. wasted usage report"
  - url: /assets/images/portfolio/si-fems/03.jpg
    image_path: /assets/images/portfolio/si-fems/03-th.jpg
    alt: "KEPCO usage and tariff view"
    title: "KEPCO usage and tariff view"
  - url: /assets/images/portfolio/si-fems/04.jpg
    image_path: /assets/images/portfolio/si-fems/04-th.jpg
    alt: "Eight equipment symbols"
    title: "Eight equipment symbols"
metrics:
  - value: "15 min"
    label: "KEPCO metering collection interval"
  - value: "10"
    label: "Machines metered in real time"
  - value: "7"
    label: "Energy management screen"
---

We built a factory energy management system (FEMS) together with an MES for a plant with powder (bead mill) and coating (plasma) processes. The customer handled the data collection hardware and database; JISHIN built the screens, back end and AI.

### Energy per machine on the floor plan
Upload the plant drawing, drag machines onto it, and each one shows live power (kW) and effective versus wasted usage right where it sits. Positions are stored relative to the drawing, so they stay put at any screen size. Seven screens cover machine monitoring, alarm logs (monthly top 3 and statistics), per-machine and plant-wide reports, KEPCO usage, carbon intensity and energy demand forecasting.

### KEPCO data integration
We connected contract, monthly billing and 15-minute metering data from the KEPCO PowerPlanner OpenAPI. The server collects 15-minute readings automatically and uses them for live usage, expected cost and carbon intensity. On the forecasting screen, users can change contract power and unit price to see how the bill would change.

{% include gallery %}
