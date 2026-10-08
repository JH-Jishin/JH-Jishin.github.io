---
title: "Company D (Time-series AI predictive maintenance for shot blasters and loading robots)"
status: done
types: ["Time Series"]
solution: ts
kind: si
order: 7
excerpt: "Uses about 20 million vibration and robot readings from 20 machines to warn of failures early"
sidebar:
  - title: "Client"
    text: "Automotive spring maker"
  - title: "Techniques"
    text: "GRU Seq2Seq · Anomaly Detection"
  - title: "Period"
    text: "2026"
  - title: "Status"
    text: "Validated on site"
header:
  teaser: /assets/images/portfolio/si-stpm/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-stpm/01.jpg
    image_path: /assets/images/portfolio/si-stpm/01-th.jpg
    alt: "Predictive maintenance dashboard"
    title: "Predictive maintenance dashboard"
  - url: /assets/images/portfolio/si-stpm/02.jpg
    image_path: /assets/images/portfolio/si-stpm/02-th.jpg
    alt: "sTPM system architecture"
    title: "sTPM system architecture"
  - url: /assets/images/portfolio/si-stpm/03.jpg
    image_path: /assets/images/portfolio/si-stpm/03-th.jpg
    alt: "Real-time overview (OEE and remaining life)"
    title: "Real-time overview (OEE and remaining life)"
---

From about 20 million time-series readings collected over 10 months on 20 shot-blasting machines at Company D's Plant 1 (14 vibration sensors, 6 loading robots), we built a GRU Seq2Seq anomaly detection model and completed on-site validation.

A floor-plan dashboard shows each machine's risk score and how many need immediate maintenance or inspection, and sends alerts when warning signs appear.

{% include gallery %}
