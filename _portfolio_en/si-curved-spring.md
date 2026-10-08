---
title: "Company D (Curvature-aware photometric AI vision with automatic rejection)"
status: ongoing
types: ["Computer Vision"]
solution: cv
featured: true
kind: si
order: 5
excerpt: "Sets its baseline from good parts only, checks the shape and surface of every curved spring, and rejects defects automatically"
sidebar:
  - title: "Client"
    text: "Automotive spring maker"
  - title: "Techniques"
    text: "Photometric Imaging · Anomaly Detection · SPC"
  - title: "Period"
    text: "2026.04 ~"
  - title: "Status"
    text: "Installed · preparing pilot production"
header:
  teaser: /assets/images/portfolio/si-curved-spring/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-curved-spring/01.jpg
    image_path: /assets/images/portfolio/si-curved-spring/01-th.jpg
    alt: "Dark-enclosure inspection units built in-house"
    title: "Dark-enclosure inspection units built in-house"
  - url: /assets/images/portfolio/si-curved-spring/02.jpg
    image_path: /assets/images/portfolio/si-curved-spring/02-th.jpg
    alt: "Dark-enclosure inspection system layout"
    title: "Dark-enclosure inspection system layout"
  - url: /assets/images/portfolio/si-curved-spring/03.jpg
    image_path: /assets/images/portfolio/si-curved-spring/03-th.jpg
    alt: "Monitoring screen (lane A and B results)"
    title: "Monitoring screen (lane A and B results)"
  - url: /assets/images/portfolio/si-curved-spring/04.jpg
    image_path: /assets/images/portfolio/si-curved-spring/04-th.jpg
    alt: "Three-color lighting enclosure design"
    title: "Three-color lighting enclosure design"
  - url: /assets/images/portfolio/si-curved-spring/05.jpg
    image_path: /assets/images/portfolio/si-curved-spring/05-th.jpg
    alt: "Deviation from the normal baseline, visualized"
    title: "Deviation from the normal baseline, visualized"
---

Curved springs are bent by design, so curvature and pitch have to come out even. Until now, skilled operators adjusted the machine by feel and only samples were inspected, so defects were sometimes found late.

Inside a dark enclosure, four lights switch on one after another and the images are combined into a single frame that shows the spring's shape and surface clearly. Real defect samples are scarce on the floor, so the baseline is built from good parts only. Each spring is compared with the normal profile for its part number to see how far its shape deviates (z-score), and a model trained on good parts flags local surface defects through reconstruction error. Results go to the PLC, which pushes defective springs off the line and receives forming-offset corrections. On the monitoring screen, SPC control charts and Cp/Cpk show the state of the process.

JISHIN designed and built the dark-enclosure inspection units and the dedicated conveyor; installation and PLC connection were completed in June 2026.

### Development-stage evaluation (in-house, before pilot production)
- All 19 real defect samples detected, 0.17% false rejects on good parts
- 0.11–0.19 s per decision (budget 0.3 s)

{% include gallery %}
