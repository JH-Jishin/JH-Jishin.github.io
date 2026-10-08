---
title: "Company D (Multi-channel edge AI vision for 100% spring inspection with line interlock)"
status: done
types: ["Computer Vision"]
solution: cv
featured: true
kind: si
order: 2
excerpt: "30 cameras catch heat-treatment anomalies and surface defects in real time, and a PLC interlock stops the line on the spot"
sidebar:
  - title: "Client"
    text: "Automotive spring maker"
  - title: "Techniques"
    text: "Object Detection · Multi-Object Tracking · Anomaly Detection"
  - title: "Period"
    text: "2025.09 ~ 2026"
  - title: "Status"
    text: "In production · pilot production"
header:
  teaser: /assets/images/portfolio/si-spring-inspection/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-spring-inspection/01.jpg
    image_path: /assets/images/portfolio/si-spring-inspection/01-th.jpg
    alt: "Front camera stage installed"
    title: "Front camera stage installed"
  - url: /assets/images/portfolio/si-spring-inspection/02.jpg
    image_path: /assets/images/portfolio/si-spring-inspection/02-th.jpg
    alt: "Post-process inspection unit installed on site"
    title: "Post-process inspection unit installed on site"
  - url: /assets/images/portfolio/si-spring-inspection/03.jpg
    image_path: /assets/images/portfolio/si-spring-inspection/03-th.jpg
    alt: "Left–right symmetry (gap) check on the front view"
    title: "Left–right symmetry (gap) check on the front view"
  - url: /assets/images/portfolio/si-spring-inspection/04.jpg
    image_path: /assets/images/portfolio/si-spring-inspection/04-th.jpg
    alt: "24-camera layout and inspection screen"
    title: "24-camera layout and inspection screen"
---

We added vision AI to two spring lines at Company D's Plant 2.

### Real-time anomaly monitoring in heat treatment
Two 5 MP machine-vision cameras face the coil line and four 8 MP cameras watch from the side. The front view finds the spring and both ends and checks left–right symmetry from the distance between center points (gap). The side view uses multi-object tracking (MOT) to follow spring movement, spacing and sudden sparks. If anything is off, the edge AI PC stops the equipment through a PLC interlock. Six models run on site, and operators check work order details, anomaly counts and recorded video at a kiosk.

### 100% surface inspection after processing
Twenty-four cameras on the left and right lines photograph all 120,000 springs a day and judge 22 defect types, including insufficient grinding, reversed marking and partial marking. The 10 to 30 defects found each day are pushed off the line through the PLC. Detection accuracy is 99.9% in pilot production, and we are working toward 99.99%.

{% include gallery %}
