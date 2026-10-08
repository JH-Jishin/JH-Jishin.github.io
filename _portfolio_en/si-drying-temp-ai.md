---
title: "Company S (AI temperature recommendation and anomaly alerts for a molded pulp drying line)"
status: done
types: ["Time Series", "Optimization · Control"]
solution: ts
featured: true
kind: si
order: 1
excerpt: "Reads 20 temperature sensors every second, recommends the minimum drying temperature per zone, and cut gas use by 3.46%"
sidebar:
  - title: "Client"
    text: "Molded pulp packaging maker"
  - title: "Techniques"
    text: "Regression (LightGBM) · Anomaly Detection · Process Optimization"
  - title: "Program"
    text: "Manufacturing AI Field Application Program"
  - title: "Period"
    text: "2025.12 ~ 2026.08"
  - title: "Status"
    text: "Completed"
header:
  teaser: /assets/images/portfolio/si-drying-temp-ai/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-drying-temp-ai/01.jpg
    image_path: /assets/images/portfolio/si-drying-temp-ai/01-th.jpg
    alt: "Drying line data flow and MES integration"
    title: "Drying line data flow and MES integration"
  - url: /assets/images/portfolio/si-drying-temp-ai/02.jpg
    image_path: /assets/images/portfolio/si-drying-temp-ai/02-th.jpg
    alt: "Live drying dashboard with AI-recommended temperature per zone"
    title: "Live drying dashboard with AI-recommended temperature per zone"
  - url: /assets/images/portfolio/si-drying-temp-ai/03.jpg
    image_path: /assets/images/portfolio/si-drying-temp-ai/03-th.jpg
    alt: "AI solution technical architecture"
    title: "AI solution technical architecture"
  - url: /assets/images/portfolio/si-drying-temp-ai/04.jpg
    image_path: /assets/images/portfolio/si-drying-temp-ai/04-th.jpg
    alt: "Drying line zones and sensor positions"
    title: "Drying line zones and sensor positions"
metrics:
  - value: "3.46%"
    label: "Gas use reduction (per unit)"
    note: "Jun 2025 vs Jun 2026"
  - value: "0.58→0.27%"
    label: "Process defect rate"
    note: "Jun 2025 vs Jun 2026"
  - value: "0.990"
    label: "Anomaly detection AUC-ROC"
    note: "Synthetic anomalies"
  - value: "20"
    label: "Temperature sensors read every second"
---

The line that dries molded pulp products runs around the clock. Zone set points were fixed by experience and rarely changed, and the burners kept firing even when the line stopped. The temperature sensors were only there to display values.

We collect 20 temperature sensors (5 zones × 4 heights) every second and added outdoor temperature and humidity sensors. Data flows from the PLC and HMI to an on-site AI PC and is stored twice, on site and in the cloud. A LightGBM regression model per sensor raises an alert when the residual exceeds ±3σ, and 38 features over 30-minute windows decide quality OK/NG. From 1,000 temperature offset trials and a grid search we found the minimum drying temperature for each zone, which appears on the dashboard every morning at 6 as the recommended set point.

{% include gallery %}
