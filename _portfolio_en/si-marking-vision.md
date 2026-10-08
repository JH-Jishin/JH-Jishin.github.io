---
title: "Company D (Vision AI for identifying color markings on springs)"
status: done
types: ["Computer Vision"]
solution: cv
kind: si
order: 8
excerpt: "Reads the color markings on each spring and checks them against the specification"
sidebar:
  - title: "Client"
    text: "Automotive spring maker"
  - title: "Techniques"
    text: "Object Detection · Color Classification"
  - title: "Status"
    text: "Completed"
header:
  teaser: /assets/images/portfolio/si-marking-vision/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-marking-vision/01.jpg
    image_path: /assets/images/portfolio/si-marking-vision/01-th.jpg
    alt: "Marking inspection main and report screens"
    title: "Marking inspection main and report screens"
  - url: /assets/images/portfolio/si-marking-vision/02.jpg
    image_path: /assets/images/portfolio/si-marking-vision/02-th.jpg
    alt: "Marking inspection hardware (relay, kiosk, camera)"
    title: "Marking inspection hardware (relay, kiosk, camera)"
  - url: /assets/images/portfolio/si-marking-vision/03.jpg
    image_path: /assets/images/portfolio/si-marking-vision/03-th.jpg
    alt: "Color marking detection result"
    title: "Color marking detection result"
---

Springs carry color markings that identify vehicle model and load class. At Company D's Plant 1, cameras now detect the position and color of each marking together and check them against the specification. After a two-month PoC and commissioning, the system replaced the existing vision setup.


### Results
- Marking detection F1 0.987, color classification accuracy 0.989 (in-house test)
- Two months from PoC to replacing the existing vision system

{% include gallery %}
