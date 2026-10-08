---
title: "Company J (Laser engraving and AI OCR for steel core ID with barcode-linked paperless MES)"
status: ongoing
types: ["Computer Vision", "Software"]
solution: cv
featured: true
kind: si
order: 3
excerpt: "Identifies 10,000+ kinds of steel cores with laser engraving and AI OCR instead of the human eye, and connects work orders to shipping without paper"
sidebar:
  - title: "Client"
    text: "Industrial rubber & urethane roll maker"
  - title: "Techniques"
    text: "OCR · Barcode · MES"
  - title: "Program"
    text: "Gyeonggi-do Smart Factory Program (2026)"
  - title: "Period"
    text: "2026"
  - title: "Status"
    text: "In progress"
header:
  teaser: /assets/images/portfolio/si-ocr-mes/teaser.jpg
gallery:
  - url: /assets/images/portfolio/si-ocr-mes/01.jpg
    image_path: /assets/images/portfolio/si-ocr-mes/01-th.jpg
    alt: "OCR and MES system architecture"
    title: "OCR and MES system architecture"
  - url: /assets/images/portfolio/si-ocr-mes/02.jpg
    image_path: /assets/images/portfolio/si-ocr-mes/02-th.jpg
    alt: "On-site hardware layout"
    title: "On-site hardware layout"
  - url: /assets/images/portfolio/si-ocr-mes/03.jpg
    image_path: /assets/images/portfolio/si-ocr-mes/03-th.jpg
    alt: "Capturing a steel core with tablet AI OCR"
    title: "Capturing a steel core with tablet AI OCR"
  - url: /assets/images/portfolio/si-ocr-mes/04.jpg
    image_path: /assets/images/portfolio/si-ocr-mes/04-th.jpg
    alt: "Portable laser engraver"
    title: "Portable laser engraver"
metrics:
  - value: "15 → <1 min"
    label: "Core identification and history lookup (per item)"
    note: "Target"
  - value: "8% fewer"
    label: "Defects"
    note: "Target"
  - value: "3% more"
    label: "Output"
    note: "Target"
---

Company J coats steel cores with rubber or urethane, ships them, and recoats worn rolls when they come back. There are more than 10,000 kinds of cores, which people told apart by eye, and chalk or paint marks wore off in high-heat and shot-blasting steps, breaking the history. Each core also carried both an in-house number and a customer number, which added to the confusion.

A portable laser engraver marks a unique ID on the side of each core, and when a tablet on the floor photographs it, AI OCR reads the number. The ID links to the work order automatically, and the in-house and customer numbers are stored in the MES as a pair. Barcode labels on semi-finished goods let them be tracked by cart (LOT), and we are building toward a paperless flow that covers tablet-based web work orders and PLC monitoring of ovens and vulcanizers.

{% include gallery %}
