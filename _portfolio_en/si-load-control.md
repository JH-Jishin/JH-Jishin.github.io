---
title: "Company D (Stroke–load curve based automatic load correction for cold setting)"
status: ongoing
types: ["Time Series", "Optimization · Control"]
solution: ts
kind: si
order: 8
excerpt: "Uses AI correction values to even out load results that used to depend on operator skill"
sidebar:
  - title: "Client"
    text: "Automotive spring maker"
  - title: "Techniques"
    text: "Regression · Closed-loop PLC Control"
  - title: "Period"
    text: "2026"
  - title: "Status"
    text: "Model in development"
header:
  teaser: /assets/images/portfolio/si-load-control/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-load-control/01.jpg
    image_path: /assets/images/portfolio/si-load-control/01-th.jpg
    alt: "Measured load–stroke curves"
    title: "Measured load–stroke curves"
metrics:
  - value: "5,609"
    label: "Setting cycles analyzed"
---

The cold-setting process has a load adjustment device, but the final load still varied with operator skill.

We analyzed stroke–load curves from 5,609 cycles of machine logs to find the variables that drive load, and are building a setup in which AI calculates RAM and stroke corrections and sends them to the PLC. Before going live, it is validated with a shadow test that compares results without actually controlling the machine.

{% include gallery %}
