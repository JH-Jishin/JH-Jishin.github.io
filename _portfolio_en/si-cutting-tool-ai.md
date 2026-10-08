---
title: "Company S (Vision AI that detects misplaced cutting tools on machining centers, cross-checked with FOCAS)"
status: done
types: ["Computer Vision"]
solution: cv
featured: true
kind: si
order: 4
excerpt: "Catches a wrongly loaded tool before machining starts, using vision AI and machine data"
sidebar:
  - title: "Client"
    text: "Press die maker for automotive parts"
  - title: "Techniques"
    text: "Object Detection (YOLO) · FANUC FOCAS Cross-check"
  - title: "Program"
    text: "Legend 50+ 2.0 · Data Voucher · Myeongpum Gangso Support"
  - title: "Period"
    text: "2025.07 ~"
  - title: "Status"
    text: "Phase 1 complete · Phase 2 in progress"
header:
  teaser: /assets/images/portfolio/si-cutting-tool-ai/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-cutting-tool-ai/01.jpg
    image_path: /assets/images/portfolio/si-cutting-tool-ai/01-th.jpg
    alt: "Kiosk and tower lamp beside the machining center"
    title: "Kiosk and tower lamp beside the machining center"
  - url: /assets/images/portfolio/si-cutting-tool-ai/02.jpg
    image_path: /assets/images/portfolio/si-cutting-tool-ai/02-th.jpg
    alt: "Camera aimed at the automatic tool changer"
    title: "Camera aimed at the automatic tool changer"
  - url: /assets/images/portfolio/si-cutting-tool-ai/03.jpg
    image_path: /assets/images/portfolio/si-cutting-tool-ai/03-th.jpg
    alt: "Live monitoring screen (tool number and coordinates)"
    title: "Live monitoring screen (tool number and coordinates)"
---

When operators load milling arbors into a machining center's automatic tool changer (ATC) by hand, a tool can be missed or seated wrong, and if machining starts that way the spindle crashes. Robotic alternatives cost hundreds of millions of won, out of reach for a small die shop.

We fitted two machining centers with cameras, a kiosk and a tower lamp. A YOLO-based model tells apart five tool types and an unclamped state, compares the result with tool number, coordinates and spindle data from FANUC FOCAS, and raises an alarm when a tool is wrong. Machine 1 computes on the internal network; machine 2 runs in the cloud. We selected and labeled 2,555 images from more than 60,000 originals and trained on night-time data as well.

### Expansion
We are building an integrated monitoring system that cross-checks against work orders and extends coverage to six machines.

### Results
- Misplaced-tool detection accuracy above 95% (in-house test: mAP@0.5 0.95, F1 0.932)
- Running on two machining centers, two patent applications filed

{% include gallery %}
