# 영문 페이지 원문. 국문 _portfolio/*.md 를 고치면 여기 같은 slug 도 같이 고친다. 생성: python tools/build_en.py
LABEL = {"고객": "Client", "기술": "Techniques", "사업": "Program", "기간": "Period", "상태": "Status"}

VALUE = {
    "1단계 완료 · 2단계 진행 중": "Phase 1 complete · Phase 2 in progress",
    "2025년 포스코 대·중소 상생형 스마트공장": "POSCO Large–Small Business Win-Win Smart Factory (2025)",
    "2026년 경기도형 스마트공장": "Gyeonggi-do Smart Factory Program (2026)",
    "POC": "Proof of concept",
    "레전드50+ 2.0 · 데이터바우처 · 명품강소기업 자율지원": "Legend 50+ 2.0 · Data Voucher · Myeongpum Gangso Support",
    "레전드50+ 지역특화 스마트공장 구축사업": "Legend 50+ Regional Smart Factory Program",
    "모델 개발 중": "Model in development",
    "분말·코팅 소재 제조사": "Powder & coating materials maker",
    "산업용 고무·우레탄 롤 제조사": "Industrial rubber & urethane roll maker",
    "수입차 판매사": "Imported car dealership",
    "양산 실증·적용": "Applied in production",
    "양산 적용·시양산": "In production · pilot production",
    "완료": "Completed",
    "운영 중": "In operation",
    "자동차 부품 제조사": "Automotive parts maker",
    "자동차 부품용 프레스 금형 제조사": "Press die maker for automotive parts",
    "자동차 스프링 제조사": "Automotive spring maker",
    "자동화기기 제조사": "Automation equipment maker",
    "제조AI 현장 적용 지원사업": "Manufacturing AI Field Application Program",
    "제조사": "Manufacturer",
    "진행 중": "In progress",
    "파일럿 진행 중": "Pilot in progress",
    "펄프몰딩 포장재 제조사": "Molded pulp packaging maker",
    "현장 적용 중": "Being rolled out on site",
    "실데이터 파일럿": "Pilot on live data",
    "구축 진행 중": "Build in progress",
    "자동차 미러 부품 제조사": "Automotive mirror parts maker",
    "자동차 부품 프레스 성형 제조사": "Automotive stamped parts maker",
    "실증 완료": "Validated on site",
    "설치 완료 · 시양산 준비": "Installed · preparing pilot production",
}

CAPTION = {
    "ERP·MES 객체를 잇는 온톨로지 맵": "Ontology map linking ERP and MES objects",
    "Zone별 온도 변위 실험 양품률": "Yield by zone in temperature offset trials",
    "각인 번호 인식 결과": "Engraved ID recognition result",
    "건조 공정 실시간 대시보드(Zone별 AI 추천온도)": "Live drying dashboard with AI-recommended temperature per zone",
    "건조라인 Zone 구성과 센서 위치": "Drying line zones and sensor positions",
    "검사 설비 컨베이어 제작": "Building the inspection conveyor",
    "공구 교환 장치를 비추는 카메라 설치": "Camera aimed at the automatic tool changer",
    "마킹 반대 불량 검출": "Reversed-marking defect detected",
    "머시닝센터 옆 키오스크와 타워램프": "Kiosk and tower lamp beside the machining center",
    "사용량·요금 현황": "Usage and cost overview",
    "색상 마킹 검출 결과": "Color marking detection result",
    "스프링 끝단 연마면 판정": "Ground spring end-face judgment",
    "실시간 관제 화면(공구번호·좌표)": "Live monitoring screen (tool number and coordinates)",
    "에너지 관리 화면": "Energy management screen",
    "연마면 반자동 라벨링": "Semi-automatic labeling of ground surfaces",
    "연마면 분할 결과": "Ground-surface segmentation result",
    "예지보전 대시보드": "Predictive maintenance dashboard",
    "자연어 질의로 집계한 작업지시 현황": "Work order status compiled from a natural-language query",
    "정면 영상 좌우 대칭(gap) 판정": "Left–right symmetry (gap) check on the front view",
    "정면 카메라 스테이지 설치": "Front camera stage installed",
    "커브드 스프링 시험 촬영": "Curved spring test capture",
    "태블릿 AI OCR 철심 촬영": "Capturing a steel core with tablet AI OCR",
    "투입 → 컨베이어 → AI 검사 구성": "Infeed → conveyor → AI inspection layout",
    "후공정 검사 카메라 마운트": "Camera mount for post-process inspection",
    "휴대용 레이저 각인기": "Portable laser engraver",
    "Ontology · LLM Agent · MES Integration": "Ontology · LLM Agent · MES Integration",
    "Energy Monitoring · KEPCO OpenAPI · Demand Forecast": "Energy Monitoring · KEPCO OpenAPI · Demand Forecast",
    "자동차 커넥터·전장부품 제조사": "Automotive connector and electrical parts maker",
    "구축 착수": "Build started",
    "금형 타발 알림(화면 예시)": "Mold shot-count alerts (sample screen)",
    "팀별 KPI 대시보드(화면 예시)": "Team KPI dashboard (sample screen)",
    "근거를 보여주는 AI 질의응답(화면 예시)": "AI Q&A with traceable evidence (sample screen)",
    "실시간 가동·비가동 모니터링(화면 예시)": "Live run/idle monitoring (sample screen)",
    "이론재고를 계산하는 노드 그래프": "Theoretical-inventory logic as a node graph",
    "숙련자 판단을 쌓는 APEX OS 구성": "How APEX OS builds up expert judgment",
    "발주에서 사출까지, 공정별 숙련자 판단": "Where expert judgment shapes each stage of the plan",
    "설비 심볼 8종": "Eight equipment symbols",
    "한전 사용량·요금 화면": "KEPCO usage and tariff view",
    "유효·비효율 사용량 리포트": "Effective vs. wasted usage report",
    "도면 위 설비별 에너지 모니터링": "Energy per machine on the floor plan",
    "라인에 설치한 포장 수량 검사장치": "Pack count inspection unit installed on the line",
    "포장 내 스프링 수량 AI 집계 화면": "AI count of springs in a pack",
    "APEX Plan 생산계획 수립 구조": "APEX Plan production planning structure",
    "건조 라인 데이터 흐름과 MES 연동 구성": "Drying line data flow and MES integration",
    "AI 솔루션 기술 구성": "AI solution technical architecture",
    "OCR·MES 시스템 구성": "OCR and MES system architecture",
    "현장 하드웨어 배치": "On-site hardware layout",
    "컨베이어·암실 검사장치 구성": "Conveyor and dark-enclosure inspection unit",
    "Vision AI 시스템 아키텍처": "Vision AI system architecture",
    "Vision AI 시스템 구성": "Vision AI system configuration",
    "Safety AI 시스템 아키텍처": "Safety AI system architecture",
    "Safety AI 하드웨어 구성": "Safety AI hardware",
    "상담 상세·상담 카드 등록 화면": "Consultation detail and card entry screens",
    "암실 검사 시스템 구성": "Dark-enclosure inspection system layout",
    "3색 조명 암실 설계": "Three-color lighting enclosure design",
    "후공정 검사장치 현장 설치": "Post-process inspection unit installed on site",
    "후공정 24캠 배치와 검사 화면": "24-camera layout and inspection screen",
    "하중-스트로크 측정 곡선": "Measured load–stroke curves",
    "연마면 AI 검출 결과": "AI detection on a ground surface",
    "마킹 검사 메인·리포트 화면": "Marking inspection main and report screens",
    "마킹 검사 하드웨어(릴레이·키오스크·카메라)": "Marking inspection hardware (relay, kiosk, camera)",
    "sTPM 시스템 구성": "sTPM system architecture",
    "실시간 종합 현황(OEE·잔여수명)": "Real-time overview (OEE and remaining life)",
    "이상 감지에서 원인 로트 역추적까지": "From anomaly detection to tracing the root-cause lot",
    "생산계획 수립 화면과 데이터 인입 경로": "Production planning screens and data intake paths",
    "가장자리 크랙 촬영 원본": "Raw capture of an edge crack",
    "정상 성형품 촬영 원본": "Raw capture of a good part",
    "컨베이어·암실 검사장치 설계": "Conveyor and dark-enclosure inspection unit design",
    "정상 기준 대비 이상 부위 시각화": "Deviation from the normal baseline, visualized",
    "모니터링 화면(A·B열 판정)": "Monitoring screen (lane A and B results)",
    "직접 제작한 암실 검사장치": "Dark-enclosure inspection units built in-house",
}

PAGES = {
    "apex-a-ontology": (
        "Company D (Ontology platform linking work orders, material lots and machine conditions)",
        "Work orders, demand, inventory, defect records and machine conditions in one ontology, queried together with a single question",
        """
We tied together the MES, ERP (SAP), SCADA and quality data of Company D's Plant 1 in a single ontology and are validating it on live data. Work orders, demand, capacity and inventory sit on the same object model, so when someone asks a question in plain language, APEX OS queries the systems together and answers.

### Monitoring dashboard
OEE, inventory, delivery and defect rate (PPM) are judged automatically and sorted into critical, warning and normal.

### Anomaly detection agent
When the defect rate crosses its limit, the agent traces MES, ERP and SCADA history back to narrow down the suspect material lot and reports with the evidence.

### Production planning
Reading work orders, demand, capacity and inventory together, it totals volume by line and works out line assignment, sequence and cost. One natural-language query organized 46 work orders covering 131,166 units and flagged that more than half of the volume was still waiting.
"""),
    "apex-m-assembly-planning": (
        "Company S (Sequence-driven assembly planning automation)",
        "Moves assembly planning that one planner ran in Excel onto the ontology and builds up expert decisions as history for recommendations",
        """
Company S makes automotive mirrors through injection molding, painting and assembly. The automaker's plan changes two to four times a day, and one planner spent three to four hours building each assembly plan in an Excel workbook. Decisions such as how to split work into shifts relied on experienced staff, model by model.

### Workshop and kickoff
A three-day on-site workshop in August 2026 produced 28 requirements, and assembly planning automation was chosen as the first project. After the September kickoff, interviews with the planner broke the job into seven data-preparation steps and five planning steps.

### What we are building
Theoretical inventory is confirmed from customer sequences (previous stock + previous plan − actuals − unproduced), short specs are flagged, and the system generates shift-by-shift work orders and the SAP upload file. MES, SAP, paint-shop SCADA, customer sequences and Excel planning files are tied together in the APEX OS ontology, and the decisions experts make — with their reasons — are kept as history to inform the next plan. The planner sees the evidence for each step beside the result, compares it with their own estimate, and then confirms.

### Progress
Checked against the existing workbook, theoretical inventory matched 52 of 52, remaining and shortage 312 of 312, and same-day plan decisions 416 of 416. After a first demo, it will run in Shadow Mode alongside the current method before going into production.
"""),
    "apex-k-mes-agent": (
        "Company K (MES-connected AI Q&A and run/idle monitoring)",
        "Cleans MES data into an ontology and builds run/idle monitoring, AI Q&A that shows its evidence, and automated reporting",
        """
Company K runs stamping, injection, plating and assembly. Each team downloaded MES data into Excel to build PowerPoint reports, taking around three hours per regular report. Utilization was only totaled per day, so day and night shifts couldn't be separated, and planned stops mixed with real downtime made utilization look lower than it was. There was no alert when a mold's shot count passed its limit.

### What we are building
Plant MES data is moved into a cleaned database for AI and tied into the APEX OS ontology, so screens, reports and Q&A all read the same data. It is installed on premises.

- Live run/idle, labor-hour and materials/warehouse monitoring
- AI Q&A that answers with the evidence: which data was queried and how
- Team KPI dashboards and automatic weekly and monthly reports
- Mold shot-count alerts and draft repair requests

### Progress
After a pilot kickoff in August 2026 and a contract in October, the build covers three plants through February 2027.
"""),
    "si-drying-temp-ai": (
        "Company S (AI temperature recommendation and anomaly alerts for a molded pulp drying line)",
        "Reads 20 temperature sensors every second, recommends the minimum drying temperature per zone, and cut gas use by 3.46%",
        """
The line that dries molded pulp products runs around the clock. Zone set points were fixed by experience and rarely changed, and the burners kept firing even when the line stopped. The temperature sensors were only there to display values.

We collect 20 temperature sensors (5 zones × 4 heights) every second and added outdoor temperature and humidity sensors. Data flows from the PLC and HMI to an on-site AI PC and is stored twice, on site and in the cloud. A LightGBM regression model per sensor raises an alert when the residual exceeds ±3σ, and 38 features over 30-minute windows decide quality OK/NG. From 1,000 temperature offset trials and a grid search we found the minimum drying temperature for each zone, which appears on the dashboard every morning at 6 as the recommended set point.

### Results (June 2025 vs June 2026, per unit produced)

- Gas use down 3.46%: 0.00935 → 0.00903 m³ per unit (target 2.5%)
- Process defect rate 0.58% → 0.27% (target 0.3% or lower)
- Anomaly detection AUC-ROC 0.990 (synthetic anomalies), quality judgment F1 0.90
"""),
    "si-spring-inspection": (
        "Company D (Multi-channel edge AI vision for 100% spring inspection with line interlock)",
        "30 cameras catch heat-treatment anomalies and surface defects in real time, and a PLC interlock stops the line on the spot",
        """
We added vision AI to two spring lines at Company D's Plant 2.

### Real-time anomaly monitoring in heat treatment
Two 5 MP machine-vision cameras face the coil line and four 8 MP cameras watch from the side. The front view finds the spring and both ends and checks left–right symmetry from the distance between center points (gap). The side view uses multi-object tracking (MOT) to follow spring movement, spacing and sudden sparks. If anything is off, the edge AI PC stops the equipment through a PLC interlock. Six models run on site, and operators check work order details, anomaly counts and recorded video at a kiosk.

### 100% surface inspection after processing
Twenty-four cameras on the left and right lines photograph all 120,000 springs a day and judge 22 defect types, including insufficient grinding, reversed marking and partial marking. The 10 to 30 defects found each day are pushed off the line through the PLC. Detection accuracy is 99.9% in pilot production, and we are working toward 99.99%.
"""),
    "si-ocr-mes": (
        "Company J (Laser engraving and AI OCR for steel core ID with barcode-linked paperless MES)",
        "Identifies 10,000+ kinds of steel cores with laser engraving and AI OCR instead of the human eye, and connects work orders to shipping without paper",
        """
Company J coats steel cores with rubber or urethane, ships them, and recoats worn rolls when they come back. There are more than 10,000 kinds of cores, which people told apart by eye, and chalk or paint marks wore off in high-heat and shot-blasting steps, breaking the history. Each core also carried both an in-house number and a customer number, which added to the confusion.

A portable laser engraver marks a unique ID on the side of each core, and when a tablet on the floor photographs it, AI OCR reads the number. The ID links to the work order automatically, and the in-house and customer numbers are stored in the MES as a pair. Barcode labels on semi-finished goods let them be tracked by cart (LOT), and we are building toward a paperless flow that covers tablet-based web work orders and PLC monitoring of ovens and vulcanizers.

### Targets

- Core identification and history lookup: 15 minutes → under 1 minute per item
- Defects down 8%, output up 3%
"""),
    "si-cutting-tool-ai": (
        "Company S (Vision AI that detects misplaced cutting tools on machining centers, cross-checked with FOCAS)",
        "Catches a wrongly loaded tool before machining starts, using vision AI and machine data",
        """
When operators load milling arbors into a machining center's automatic tool changer (ATC) by hand, a tool can be missed or seated wrong, and if machining starts that way the spindle crashes. Robotic alternatives cost hundreds of millions of won, out of reach for a small die shop.

We fitted two machining centers with cameras, a kiosk and a tower lamp. A YOLO-based model tells apart five tool types and an unclamped state, compares the result with tool number, coordinates and spindle data from FANUC FOCAS, and raises an alarm when a tool is wrong. Machine 1 computes on the internal network; machine 2 runs in the cloud. We selected and labeled 2,555 images from more than 60,000 originals and trained on night-time data as well.

### Results
- Detection accuracy above 95% (in-house test: mAP@0.5 0.95, F1 0.932)
- Two prototype units running on site, two patent applications filed

### Phase 2
We are building an integrated monitoring system that cross-checks against work orders and extends coverage to six machines.
"""),
    "si-fems": (
        "Company E (Real-time factory energy management (FEMS) linked to KEPCO tariffs)",
        "Energy per machine on the floor plan, KEPCO tariff data and demand forecasting in one system",
        """
We built a factory energy management system (FEMS) together with an MES for a plant with powder (bead mill) and coating (plasma) processes. The customer handled the data collection hardware and database; JISHIN built the screens, back end and AI.

### Energy per machine on the floor plan
Upload the plant drawing, drag machines onto it, and each one shows live power (kW) and effective versus wasted usage right where it sits. Positions are stored relative to the drawing, so they stay put at any screen size. Seven screens cover machine monitoring, alarm logs (monthly top 3 and statistics), per-machine and plant-wide reports, KEPCO usage, carbon intensity and energy demand forecasting.

### KEPCO data integration
We connected contract, monthly billing and 15-minute metering data from the KEPCO PowerPlanner OpenAPI. The server collects 15-minute readings automatically and uses them for live usage, expected cost and carbon intensity. On the forecasting screen, users can change contract power and unit price to see how the bill would change.

### Progress
All six findings from the August 2026 review were resolved and reported complete, and the system is running on site.
"""),
    "si-curved-spring": (
        "Company D (Curvature-aware photometric AI vision with automatic rejection)",
        "Sets its baseline from good parts only, checks the shape and surface of every curved spring, and rejects defects automatically",
        """
Curved springs are bent by design, so curvature and pitch have to come out even. Until now, skilled operators adjusted the machine by feel and only samples were inspected, so defects were sometimes found late.

Inside a dark enclosure, four lights switch on one after another and the images are combined into a single frame that shows the spring's shape and surface clearly. Real defect samples are scarce on the floor, so the baseline is built from good parts only. Each spring is compared with the normal profile for its part number to see how far its shape deviates (z-score), and a model trained on good parts flags local surface defects through reconstruction error. Results go to the PLC, which pushes defective springs off the line and receives forming-offset corrections. On the monitoring screen, SPC control charts and Cp/Cpk show the state of the process.

JISHIN designed and built the dark-enclosure inspection units and the dedicated conveyor; installation and PLC connection were completed in June 2026.

### Development-stage evaluation (in-house, before pilot production)
- All 19 real defect samples detected, 0.17% false rejects on good parts
- 0.11–0.19 s per decision (budget 0.3 s)
"""),
    "si-grinder-ai": (
        "Company D (Vision judgment of spring grinding and self-adjusting grinding stones)",
        "Reads the ground surface with cameras and positions six grinding stones automatically, replacing visual setup by operators",
        """
On the grinder that finishes both ends of a spring, operators set the position and speed of six grinding stones by eye, so quality varied with whoever did the setup.

A top camera measures spring length within ±5 mm, and side cameras segment the ground surface (targeting mIoU of 90% or higher) to score how well it is ground. That score and the free-height difference correct PLC parameters so the stones adjust themselves, and every spring gets a pass/fail result and a history record. Grinding-height measurement and correction went live on site in July 2026, with automatic rejection of defective parts running alongside.
"""),
    "si-stpm": (
        "Company D (Time-series AI predictive maintenance for shot blasters and loading robots)",
        "Uses about 20 million vibration and robot readings from 20 machines to warn of failures early",
        """
From about 20 million time-series readings collected over 10 months on 20 shot-blasting machines at Company D's Plant 1 (14 vibration sensors, 6 loading robots), we built a GRU Seq2Seq anomaly detection model and completed on-site validation.

A floor-plan dashboard shows each machine's risk score and how many need immediate maintenance or inspection, and sends alerts when warning signs appear.
"""),
    "si-marking-vision": (
        "Company D (Vision AI for identifying color markings on springs)",
        "Reads the color markings on each spring and checks them against the specification",
        """
Springs carry color markings that identify vehicle model and load class. At Company D's Plant 1, cameras now detect the position and color of each marking together and check them against the specification. After a two-month PoC and commissioning, the system replaced the existing vision setup.

### Results
- In-house test: marking detection F1 0.987, color classification accuracy 0.989
"""),
    "si-load-control": (
        "Company D (Stroke–load curve based automatic load correction for cold setting)",
        "Uses AI correction values to even out load results that used to depend on operator skill",
        """
The cold-setting process has a load adjustment device, but the final load still varied with operator skill.

We analyzed stroke–load curves from 5,609 cycles of machine logs to find the variables that drive load, and are building a setup in which AI calculates RAM and stroke corrections and sends them to the PLC. Before going live, it is validated with a shadow test that compares results without actually controlling the machine.
"""),
    "si-grind-inspection-darkroom": (
        "Company D (Upgraded spring grinding inspection and dark-enclosure packaging line)",
        "Improves the existing grinding inspection equipment and adds dark-enclosure packaging to the line",
        """
This project improves the spring grinding inspection equipment at Company D's Plant 2 and applies dark-enclosure packaging to an existing line. We supply the machine-vision hardware, AI models and back-end and dashboard software, and handle installation and commissioning.
"""),
    "si-spring-packaging": (
        "Company D (AI vision pack count inspection for springs)",
        "Cameras photograph packed springs, AI counts them and checks the count against the standard before shipping",
        """
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
"""),
    "si-press-vision": (
        "Company C (AI vision defect detection and automatic sorting for pressed parts)",
        "Catches missing holes and cracks in stamped parts with vision AI and sorts them out right on the conveyor",
        """
Stamped parts with a missing hole or a crack at the edge had to be checked one by one by eye.

We mounted a dark-enclosure inspection unit over the conveyor, and an industrial camera photographs each part so AI can judge whether holes are present and whether there are cracks. When a defect turns up, LS PLC communication sounds a buzzer and the part is pulled out, and every result is logged on a dashboard.
"""),
    "si-crm-server": (
        "Company T (Sales CRM for imported car dealers with AI extraction from consultations)",
        "A CRM for sales staff that brings consultations, inventory, test drives and lead scoring into one place",
        """
We are building a CRM for the sales staff of an imported car dealership. We designed the consultation, inventory and test-drive screens, customer and consultation lists, and a dashboard; when a consultation is entered, AI pulls out and organizes the key details. Lead scores help staff decide whom to contact first.

The prototype was demonstrated at two showrooms, and we also handled the server that runs the program, from choosing the specification to installation, network setup and initial configuration.
"""),
    "si-production-optimization": (
        "Company S (AI-based factory production optimization system)",
        "Built an AI system for production optimization based on factory production data",
        """
We built an AI system for optimizing factory production.
"""),
    "si-welding-ai-mes": (
        "Company Z (Welding quality AI, MES, and press predictive maintenance)",
        "Built welding AI models, MES screens and a press predictive maintenance system together",
        """
We developed welding AI models and built the MES screens (UI/UX). On the press equipment at the same site, we added a predictive maintenance system.
"""),
    "si-ai-mes": (
        "Company T (Manufacturing AI MES built on shop-floor data)",
        "Developed an MES based on shop-floor data",
        """
We developed an MES built on the data generated on the shop floor.
"""),
    "si-smartfactory-rnd": (
        "Company Z (R&D for Vision Safety and QC AI solutions)",
        "Researched, developed and deployed vision AI for workplace safety and quality inspection",
        """
We researched, developed and deployed JISHIN's Vision Safety AI and Vision QC AI solutions for Company Z's environment, then handled maintenance and additional AI and software development for a year.
"""),
}
