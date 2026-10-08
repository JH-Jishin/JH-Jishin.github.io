---
title: "Company D (AI vision pack count inspection for springs)"
status: ongoing
solution: cv
types: ["Computer Vision"]
kind: si
order: 10
excerpt: "Cameras photograph packed springs, AI counts them and checks the count against the standard before shipping"
sidebar:
  - title: "Client"
    text: "Automotive spring maker"
  - title: "Techniques"
    text: "Object Counting · Machine Vision · DB Integration"
header:
  teaser: /assets/images/portfolio/si-spring-packaging/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-spring-packaging/01.jpg
    image_path: /assets/images/portfolio/si-spring-packaging/01-th.jpg
    alt: "Pack count inspection unit installed on the line"
    title: "Pack count inspection unit installed on the line"
  - url: /assets/images/portfolio/si-spring-packaging/02.jpg
    image_path: /assets/images/portfolio/si-spring-packaging/02-th.jpg
    alt: "AI count of springs in a pack"
    title: "AI count of springs in a pack"
---

### Background
Operators were checking spring counts by eye and by hand during packing, and fatigue from the repetitive work could lead to counting errors. Shipping short or over-filled packs leads to customer claims and rework costs.

### How it works
1. Look up the part number in production and its standard pack quantity from the database in real time.
2. Photograph each packed tray on the conveyor with the installed camera.
3. Analyze the image with AI to count the springs in the pack.
4. Compare the count with the standard quantity and judge whether they match.

### Expected benefits
- Less manual counting work for operators
- Short or over-filled packs caught before shipping
- Fewer customer claims and less rework from count mismatches

{% include gallery %}
