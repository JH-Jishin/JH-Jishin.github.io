---
title: "Company D (Vision judgment of spring grinding and self-adjusting grinding stones)"
status: ongoing
types: ["Computer Vision", "Optimization · Control"]
solution: cv
kind: si
order: 6
excerpt: "Reads the ground surface with cameras and positions six grinding stones automatically, replacing visual setup by operators"
sidebar:
  - title: "Client"
    text: "Automotive spring maker"
  - title: "Techniques"
    text: "Segmentation · Closed-loop PLC Control"
  - title: "Period"
    text: "2026"
  - title: "Status"
    text: "Being rolled out on site"
header:
  teaser: /assets/images/portfolio/si-grinder-ai/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-grinder-ai/01.jpg
    image_path: /assets/images/portfolio/si-grinder-ai/01-th.jpg
    alt: "Ground spring end-face judgment"
    title: "Ground spring end-face judgment"
  - url: /assets/images/portfolio/si-grinder-ai/02.jpg
    image_path: /assets/images/portfolio/si-grinder-ai/02-th.jpg
    alt: "Ground-surface segmentation result"
    title: "Ground-surface segmentation result"
  - url: /assets/images/portfolio/si-grinder-ai/03.jpg
    image_path: /assets/images/portfolio/si-grinder-ai/03-th.jpg
    alt: "Semi-automatic labeling of ground surfaces"
    title: "Semi-automatic labeling of ground surfaces"
metrics:
  - value: "±5mm"
    label: "Spring length measurement"
  - value: "6"
    label: "Grinding stones adjusted automatically"
  - value: "90%+"
    label: "Ground-surface segmentation mIoU"
    note: "Target"
---

On the grinder that finishes both ends of a spring, operators set the position and speed of six grinding stones by eye, so quality varied with whoever did the setup.

A top camera measures spring length within ±5 mm, and side cameras segment the ground surface (targeting mIoU of 90% or higher) to score how well it is ground. That score and the free-height difference correct PLC parameters so the stones adjust themselves, and every spring gets a pass/fail result and a history record. Grinding-height measurement and correction went live on site in July 2026, with automatic rejection of defective parts running alongside.

{% include gallery %}
