---
title: "THE CITY TIMETABLE: An Auditable, Switchable AI Time-Space System for the Jing-Zhang Belt"
author_github: "andyxu12341"
language: "en"
proposal_format_version: "2"
bilingual_contract_version: "1"
translation_of: "proposal.md"
license: "COMMUNITY-DISPLAY-ONLY"
summary: "Using the railway operating diagram as both cultural reference and operating mechanism, the proposal organizes the Jing-Zhang AI Innovation Belt as a public, auditable and human-overridable urban timetable. Robot delivery, low-speed autonomous shuttles, youth night activities, commuting, accessibility and emergency access share space through explicit time windows, while T0 constant rights override all algorithmic scheduling. Precise placement will be recalculated after official geometry is released."
tracks: ["robotics-autonomous-mobility", "youth-friendly-public-space", "jingzhang-heritage-narrative"]
scenarios: ["robot-delivery-low-speed", "ai-traffic-walkability", "ai-cultural-guide"]
iteration: "v0.2-structured"
---

# THE CITY TIMETABLE · 京张运行图

A century ago, the Jing-Zhang Railway had to solve more than the question of where tracks should go. It also had to determine when trains departed, where they met or yielded, which movement had priority, and how service recovered after delay. An AI city faces a comparable coordination problem today, except that the actors now include people, robots, low-speed autonomous shuttles, public events and urban services.

**The City Timetable does not attach an AI label to a conventional urban-design plan. It treats time as a design dimension equal to space: public, machine-readable, auditable and subject to explicit human override.** A space should communicate not only what it is, but also what may happen there at a given time, who has priority, how conflicts are rejected or rescheduled, and who remains responsible for the final decision.

The current version already contains a TimeSlot Contract, twelve scenario cards, nine GeoJSON layers, metrics, a source register and three compliance/depth matrices. The five bilingual core figures, offline HTML, bilingual A3/A0 drawings, manifest, finalize, self-check and participant preflight are still pending. This is therefore a **formal working package**, not `ready_for_review`, and it does not constitute government approval, statutory planning, engineering feasibility or operating permission.

## Design Basis and Source List

The official open-call announcement controls the project name, three scope levels, three key areas, core design tasks and deliverable depth [source:OFFICIAL-ANNOUNCEMENT]. The Agent-facing taskbook controls the co-creation charter, six Agent tasks and requirements for scenarios, personas, landmarks and long-term operation [source:AGENT-TASKBOOK]. Professional expression also follows the repository's local official snapshots of the Urban Design Management Measures, regulatory detailed-planning rules and national land-use classification guide [source:STD-URBAN-DESIGN] [source:STD-CONTROL-PLAN] [source:STD-LAND-USE].

The available brief provides approximate areas of 43.6 km² for coordinated research, 11.4 km² for overall design and 368.4 ha for the three key areas, but precise official polygons have not entered the trusted site package. `geometry/site_boundary.geojson` and `geometry/key_areas.geojson` therefore remain `provisional_constraint` with `official_boundary=false`. Their calculated areas, ratios and spatial relationships may only support generation, visualization and temporary intake checks; the whole package must be recalculated when official polygons arrive [source:BOUNDARY-SOURCE] [source:KEY-AREA-SOURCE] [assumption:A-BOUNDARY-001].

Approved FAR, building height, building density, statutory green-ratio controls, setbacks, road redlines, ownership, municipal capacity and engineering conditions remain missing. The proposal does not invent them from schema sanity ranges, news maps, OSM, textual bounds or AI inference [assumption:A-CONTROLS-001].

![Three-level scope and City Timetable overview](assets/figures/site-overview.en.png)

## Three-Level Scope Framework

### 43.6 km²: Coordinated Innovation Operating Domain

The coordinated research area is not treated as another generalized master-plan diagram. Instead, it investigates the time network of innovation: when university research enters testing, when enterprises receive scenario access, when international events connect the three key areas, and how talent services, logistics, night economy and public services avoid unnecessary conflict. Outputs focus on an innovation calendar, cross-area coordination and time interfaces among the “three areas and two wings.”

### 11.4 km²: Core City Timetable System

The overall design area contains three transferable spatial types:

1. **Constant-rights space** — essential walking, continuous accessibility, emergency access and essential non-digital service cannot be scheduled away;
2. **Time-shared space** — logistics, shuttles, community events, youth activities and temporary exhibitions may switch through explicit windows;
3. **Controlled testing space** — robots and low-speed autonomous shuttles enter only when prerequisite safety evidence, accountable human roles and safe-exit mechanisms are defined.

### 368.4 ha: Three Time-governance Experiments

The three key areas do not receive identical AI installations. Zhongzhiyuan focuses on **testing and safety**; the Beijing AI Origin Community focuses on **24-hour co-creation balanced with everyday rights**; Dazhongsi focuses on **time-sharing among high-frequency footfall, transit, consumption, night activity and logistics** [metric:key_area_count].

## Coordinated Research Area: Industry and Future City Research

### From Space Plan to Time Plan

Conventional urban design asks what belongs where. The City Timetable adds: **what happens when, and who yields when uses conflict?** The spatial model therefore includes one north-south **time spine**, three key-area **time interfaces**, and cross-domain operating interfaces toward the Zhongguancun technology-service wing and Xiaoyuehe scenario-empowerment wing [data:geometry/roads.geojson#ROAD-001] [metric:time_spine_length_m].

### Six Global Mechanism Precedents

The proposal transfers mechanisms, not foreign legal systems:

| Precedent | Transferable mechanism | Relevance to Jing-Zhang | Not directly transferable |
| --- | --- | --- | --- |
| NYC Open Streets 2026 | Streets switch among Full Closure, Limited Local Access and ordinary operation on published days/hours while retaining emergency and necessary access | Urban space should publish when a mode changes and which exceptions remain valid | New York traffic law, enforcement and partner model [source:CASE-NYC-OPEN-STREETS-2026] |
| LADOT Code the Curb | Digitizes curb location and regulation so the public right-of-way becomes machine-readable | TimeSlot Contract should structure location, rule, time window and accountable operator | Los Angeles policy and curb inventory [source:CASE-LADOT-CODE-THE-CURB] |
| OMF Curb Data Specification | Open structure for curb regulations, events and metrics | The timetable must exist as data and measurable contracts, not only as a graphic | CDS is not a Beijing planning or AV-safety standard [source:CASE-OMF-CDS] |
| Singapore LTA / CETRAN | Separates controlled AV safety testing from public-road deployment and emphasizes assessment and operational recording | Zhongzhiyuan must distinguish testing from permission to operate | Singapore law and CETRAN approval do not apply in Beijing [source:CASE-SG-LTA-AV] |
| TfL School Streets | Temporary motor-traffic restrictions protect school arrival and dismissal periods | T0/T1 can encode predictable public-rights windows that lower-priority activities cannot override | UK traffic-order and enforcement mechanisms [source:CASE-TFL-SCHOOL-STREETS] |
| Paris Rues aux écoles | Converts school-adjacent streets into safer pedestrian/play space | Youth friendliness should protect everyday public-space rights rather than rely on spectacle alone | Paris implementation rules [source:CASE-PARIS-RUES-ECOLES] |

Together, these cases support a central proposition: **an AI-native urban form is not defined by more sensors, but by public rules that people can understand, machines can read, responsible humans can review, and systems can safely fall back from.**

## Overall Design Area: Urban Renewal and Regulatory-Plan-Level Urban Design

### Four Time-Space Layers

**T0 Constant Rights** — continuous accessible routes, emergency access, essential walking and essential non-digital service. T0 is not market-bookable and cannot be overridden by AI recommendations.

**T1 Routine Rhythm** — commuter peaks, school periods, everyday commerce, park movement and ordinary resident access.

**T2 Flexible Reservation** — robot delivery, low-speed shuttle tests, temporary exhibitions, community classes and small youth events, entering time windows through role-based authorization.

**T3 Human-confirmed Event** — AI conferences, special test weeks, Demo Night, large roadshows and high-crowd events. A named human responsible role is mandatory.

The TimeSlot Contract requires at least: space unit, time window, allowed actors, priority, time layer, accessibility protection, human owner, stop triggers, rollback action, logging, non-AI fallback and validation method. Conflict is resolved through P0–P3 priority. T0/P0 always overrides robot, commercial and event reservations [metric:time_layer_count] [data:geometry/constraints.geojson#CONST-001].

The protocol currently includes four PASS and four FAIL validator examples. For example, an off-peak robot delivery that preserves the T0 accessible route can pass to operator review; a robot blocking the only accessible route, an event blocking emergency access, or an autonomous shuttle request without safety evidence must be rejected [metric:validator_negative_case_count].

![Land-use and urban timetable structure](assets/figures/land-use-structure.en.png)

## Detailed Design of Key Areas

### Zhongzhiyuan: AI Timetable Testing Ground

Zhongzhiyuan becomes **an observable, stoppable testing environment for embodied AI before it enters ordinary public space**. It includes a controlled test loop, human takeover point, public observation space and operating-log interface. Robot delivery, low-speed shuttle degradation, crowd-peak exit and override/log replay form four industrial test-validation scenarios [metric:test_validation_scenario_count].

Every test remains distinct from an operating permit. Accessibility conflict, unexpected crowding, communications/sensor degradation or a manual stop request must trigger downgrade or termination [assumption:A-ROBOTICS-001].

### Beijing AI Origin Community: 24-hour Co-creation Timetable Community

The community is designed as **a place where youth innovation rhythms coexist with residents' everyday rights**. Daytime supports learning, collaboration and public services; approved evening windows support Demo Night, light sports and study-space switching, while quiet enjoyment, ordinary access and accessible routes remain hard constraints.

Basic public services do not require facial recognition, individual movement histories or mandatory app login. AI navigation, booking and cultural guidance retain physical wayfinding, printed information or staffed equivalents [metric:non_ai_fallback_coverage].

### Dazhongsi: AI-native Everyday-life Timetable District

Dazhongsi becomes **a time-sharing district for high-frequency footfall, consumption, transit, night activity and machine logistics**. Human flow receives priority at commercial peaks; controlled replenishment and last-mile logistics move to lower-demand periods; youth culture and consumption occupy approved night windows; crowd or event states trigger machine exit.

Because the repository community has raised a review question about the absolute position of provisional `PROV-KEY-003` relative to public geographic anchors, this stage does not translate the rough rectangle into precise intersections, station quadrants or building engineering design [assumption:A-DAZHONGSI-001].

### Three AI Pilgrimage Landmarks

1. **TIMETABLE HALL / 运行图大厅** — a public interface showing current belt modes, next switches, test status and the annual operating calendar;
2. **TIME EXCHANGE / 时间交换站** — a shared-time platform for youth events, community classes, public services and urban test windows;
3. **CENTENNIAL DEPARTURE / 百年发车台** — a cultural landmark connecting railway departure, meeting/yielding, delay and recovery to transparent AI-era urban governance.

![Three key areas and pilgrimage nodes](assets/figures/key-areas.en.png)

## AI Innovation Ecosystem, Personas, and AI+ Scenarios

### Six Personas

- AI startup teams and developers — testing, publishing, collaboration and low-cost access to real scenarios;
- university students and young researchers — learning, night exchange and research demonstration;
- nearby residents — reliable access, quiet enjoyment, community service and visible feedback channels;
- accessibility and older users — continuous routes, low cognitive load and non-app equivalents;
- merchants and night workers — customer flow, replenishment, waste collection and explicit operating/logistics windows;
- logistics, maintenance and emergency roles — controlled access, fault handling, human takeover and auditable records.

### Twelve Scenario Cards

| ID | Scenario | Category | Core validation |
| --- | --- | --- | --- |
| SC-01 | Robot Delivery Time-window Stress Test | Test/validation | Preserve T0; human stop and rollback |
| SC-02 | Low-speed Shuttle Conflict and Degradation Test | Test/validation | Safety prerequisite, downgrade, takeover |
| SC-03 | Crowd-peak Automatic Exit Test | Test/validation | Machine use exits before public peak rights are compressed |
| SC-04 | Human Override and Log Replay | Test/validation | Every override has an accountable owner and replayable log |
| SC-05 | Youth Demo Night Reversible Public Living Room | Public life | Resident access, noise, emergency access and full reset |
| SC-06 | No-app Public Service Navigation | Public life | Equivalent basic service without account or phone |
| SC-07 | AI Cultural Guide + Non-digital Equivalent Route | Public life | Heritage/copyright review and equivalent physical route |
| SC-08 | Night Learning and Light-sport Space Switch | Public life | Quiet constraints, maintenance window, human duty role |
| SC-09 | Urban Scenario Booking and Admission | Industry/operation | Rules, risk class and accountable organization traceable |
| SC-10 | Shared Enterprise Demo Slots | Industry/operation | No long-term exclusive occupation of public space |
| SC-11 | Multi-party Event-day Scheduling | Industry/operation | Conflict simulation; accessibility/emergency priority; post-event reconciliation |
| SC-12 | Public City Timetable Display | Industry/operation | Current state, next switch, accountable role and fallback route are visible |

All twelve scenarios are stored in `visual/assets/scenarios.json` with human-review and non-AI-fallback fields [metric:scenario_count] [metric:human_override_coverage] [metric:non_ai_fallback_coverage]. The reported 100% values mean **design-contract field coverage**, not measured operational performance [assumption:A-METRICS-001].

## Land Use, Building Scale, and Retain-Renovate-Demolish Strategy

At the current data depth, the proposal does not derive statutory land use from provisional boundaries, does not treat illustrative building footprints as surveyed existing conditions, and does not provide FAR, building height or density. `geometry/land_use.geojson` uses verifiable `land_use_code` values for a conceptual functional structure and explicitly states that the layer is not regulatory approval [source:STD-LAND-USE].

The building layer contains six `candidate_retrofit` illustrative units to express a principle: **use existing or adaptable ground-floor/public-interface space first, then discuss new construction only when evidence supports it**. They do not correspond to verified existing buildings. Their illustrative footprint totals about 88,629 m² and exists only to test structured submission logic [metric:building_footprint_area_sqm].

`floor_area_ratio` remains `unknown` until official boundaries and approved controls are available [metric:floor_area_ratio].

## Transport, Rail, Municipal Infrastructure, and Public Services

The proposal does not alter or claim to know existing primary-road, railway, river, road-redline or municipal controls. At the design layer, it adds an approximately 9.22 km **time-spine concept line** and three key-area time interfaces to explain cross-area walking, public-event and time-governance relationships [metric:time_spine_length_m].

The T0 constraint layer adds a north-south constant-rights line and three cross-area interfaces, totaling about 12.33 km. These are not fire or road redlines; they are internal design-protocol lines that cannot be overridden by lower-priority scheduling [metric:t0_constant_rights_corridor_length_m].

Municipal and new-infrastructure strategy treats **public operating state, machine-readable rules, human takeover, exception logs and non-digital backup** as digital infrastructure. Distributed energy, edge compute, sensors, communications, utilities and fire-safety capacities remain subject to future professional data and engineering review.

![Mobility, T0 rights and blue-green public space](assets/figures/mobility-bluegreen.en.png)

## Blue-Green Network, Public Space, and Urban Character

Urban character avoids treating “blue futuristic light” as the sole visual language of AI. Instead, the time axis, station, meet/yield line and delay-recovery logic of railway operating diagrams are translated into signage, paving, public information and event systems.

The conceptual green layer contains one heritage-park timetable green corridor and three flexible open-green areas in the key zones. Relative to the provisional boundary, it recalculates to about 33.46%. This is a concept-design ratio, not an approved green ratio and not an official heritage-park boundary [metric:green_ratio].

Six reversible public spaces include the three pilgrimage nodes plus test, youth and AI-everyday-life spaces. Their concept area is about 1.50% of the provisional overall design area [metric:public_space_ratio] [metric:reversible_public_space_count]. The objective is not the percentage itself, but demonstrating that the same public space can hold multiple time modes without sacrificing T0 rights.

The cultural narrative follows four stages: **Centennial Departure — Open Meeting/Yielding — Intelligent Operation — Recoverable City**. Railway history demonstrates how modern urban life once coordinated complex movement through shared time; Zhongguancun culture contributes open innovation and technology transfer; AI culture contributes transparent rules, accountability and human-machine collaboration rather than automated replacement of urban governance.

## Renewal Projects, Implementation Policy, and Phasing

### Near Term: Protocol and Low-risk Reversible Pilots

Priorities are the TimeSlot Contract, public timetable interface, T0 accessibility/emergency checks, no-app service navigation, a reversible Demo Night living room and robot testing that does not enter ordinary public roads. Near-term work should be low-cost, reversible and measurable rather than dependent on large demolition or construction.

### Mid Term: Cross-area Timetable Coordination

After official spatial data and professional conditions are added, the three key areas can coordinate event, logistics, public-service, walking and testing windows through a common admission system, accountable roles and operating logs.

### Long Term: Belt-wide Urban Operating System

Only after transport, safety, planning, municipal, heritage, ownership and operating-approval pathways are clear should the proposal consider public operation of embodied AI, higher-level autonomous shuttles or substantial spatial reconstruction. A concept proposal cannot pre-claim that these measures are approved or inevitable [assumption:A-ROBOTICS-001].

The annual operating system includes **Open Timetable Week, Urban Agent Scheduling Challenge, Robotics Low-speed Test Week, Jing-Zhang Demo Night and Annual City Timetable Review**. These are not stand-alone promotional events; they create recurring opportunities to test conflict rules, public experience and operating accountability.

`geometry/phasing.geojson` expresses near-, mid- and long-term concept zones. Every phase remains dependent on official polygons, professional confirmation and required approvals.

## Metrics, Area Recalculation, and Compliance Matrix

Current spatial metrics are recalculated in EPSG:4548. Provisional and conceptual values demonstrate internal consistency of the working model and must not be promoted into statutory controls.

| Metric | Current value | Meaning and limitation |
| --- | ---: | --- |
| `site_area_sqm` | 11,412,825 m² | Provisional overall boundary; not an official redline |
| `key_area_count` | 3 | Count follows the task; geometries remain provisional |
| `building_footprint_area_sqm` | 88,629 m² | Six concept retrofit units, not an existing-building census |
| `green_ratio` | 33.46% | Concept green layer / provisional boundary; not approved green ratio |
| `public_space_ratio` | 1.50% | Only six timetable spaces, not all public-space supply |
| `time_spine_length_m` | 9,216.69 m | Concept connection line, not road/rail engineering alignment |
| `t0_constant_rights_corridor_length_m` | 12,327.51 m | Design-protocol rights lines, not statutory redlines |
| `scenario_count` | 12 | Machine-readable scenario cards |
| `test_validation_scenario_count` | 4 | Exceeds the minimum three test/validation scenarios |
| `human_override_coverage` | 100% | All scenarios define human review; design-field coverage only |
| `non_ai_fallback_coverage` | 100% | All scenarios define non-AI fallback; design-field coverage only |
| `floor_area_ratio` | unknown | Awaiting official controls and official polygon |

`compliance_matrix.json`, `standard_matrix.json` and `design_depth_matrix.json` connect official requirements, Agent 1–6, professional standards, layers, metrics, drawings and risk assumptions.

![Metrics, evidence and TimeSlot Contract](assets/figures/metrics-evidence.en.png)

## Risk, Copyright, and Compliance

1. **Boundary risk** — official polygons are missing. Every provisional geometry-derived value must be recalculated as a system when trusted polygons arrive [assumption:A-BOUNDARY-001].
2. **Regulatory/engineering risk** — FAR, height, density, setbacks, road redlines, ownership, utilities, fire and heritage controls are not inferred [assumption:A-CONTROLS-001].
3. **Embodied-AI risk** — testing is not permission. Public deployment requires separate safety, transport, regulatory and operating conditions [assumption:A-ROBOTICS-001].
4. **Dazhongsi location risk** — precise station quadrants and building placement are deferred until the provisional-geometry question is resolved [assumption:A-DAZHONGSI-001].
5. **Metric risk** — design-contract coverage is separate from operational performance. Real conflict-rejection rate, safety outcomes and public satisfaction require future baselines [assumption:A-METRICS-001].
6. **Privacy and equity** — basic public service does not require facial recognition, persistent individual tracking, mandatory apps or a single vendor; T0 rights remain visible and accessible to all.
7. **Copyright** — the proposal does not copy railway corporate logos, peer designs or uncleared images/fonts. The timetable visual identity must use original graphics and cleared assets.
8. **Status language** — this work may be described only as an open-call concept / formal working submission until repository merge, professional review or later implementation establishes another status.

## References

- Official Centennial Jing-Zhang AI Innovation Belt design open-call announcement [source:OFFICIAL-ANNOUNCEMENT]
- Agent-facing open-call taskbook extract [source:AGENT-TASKBOOK]
- Repository public source registry [source:SOURCE-REGISTRY]
- Urban Design Management Measures, local official-source snapshot [source:STD-URBAN-DESIGN]
- Regulatory detailed-planning rules, local official-source snapshot [source:STD-CONTROL-PLAN]
- National land-use classification guide, local official-source snapshot [source:STD-LAND-USE]
- NYC DOT Open Streets 2026 [source:CASE-NYC-OPEN-STREETS-2026]
- LADOT Code the Curb [source:CASE-LADOT-CODE-THE-CURB]
- Open Mobility Foundation Curb Data Specification [source:CASE-OMF-CDS]
- Singapore LTA Autonomous Vehicles / CETRAN [source:CASE-SG-LTA-AV]
- Transport for London School Streets [source:CASE-TFL-SCHOOL-STREETS]
- Ville de Paris Rues aux écoles [source:CASE-PARIS-RUES-ECOLES]
