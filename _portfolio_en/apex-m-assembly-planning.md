---
title: "Company S (Sequence-driven assembly planning automation)"
status: ongoing
types: ["Ontology"]
solution: onto
kind: apex-os
order: 2
excerpt: "Moves assembly planning that ran on Excel workbooks and messenger chats onto the ontology, linking sequence intake to work orders in one flow"
sidebar:
  - title: "Client"
    text: "Automotive mirror parts maker"
  - title: "Techniques"
    text: "Ontology · Rule Extraction · Planning Simulation"
  - title: "Period"
    text: "2026.08 ~"
  - title: "Status"
    text: "Build in progress"
header:
  teaser: /assets/images/portfolio/apex-m-assembly-planning/teaser.jpg
gallery:
  - url: /assets/images/portfolio/apex-m-assembly-planning/01.jpg
    image_path: /assets/images/portfolio/apex-m-assembly-planning/01-th.jpg
    alt: "APEX Plan production planning structure"
    title: "APEX Plan production planning structure"
---

Company S's assembly planning runs on one planner's Excel workbook. Every morning the planner downloads delivery sequences by plant from the automaker's portal, copies defect reports received by messenger into the sheet by hand, calculates theoretical inventory, finds the specs that will run short, and prints work orders. Scaling quantities by a single ratio, assigning shifts, splitting into cart-sized lots and preparing the SAP sequence-production upload are all stitched together by hand.

JISHIN is unpacking the workbook's formulas and labels one by one, confirming what they mean in interviews with the planner, and moving those rules into APEX OS ontology objects and constraints. Six MES views (production results, run history, line status, two inventory views and issue history) are connected so theoretical inventory reconciles automatically; the first scope runs up to entering D+3 production quantities and comparing the result with the existing plan. A simulator screen the planner can run directly is being built alongside.

### Progress
- Three on-site interviews in September 2026 and a confirmed rule sheet for the workbook
- Planning for painting and injection lines to follow the assembly line

{% include gallery %}
