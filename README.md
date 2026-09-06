<div align="center">
<a href="https://www.cowmata.com/"><img src="assets/brand/cowmata-logo.svg" width="360" alt="COWMATA"></a>

# COWMATA · Cattle Monitoring

**Continuous sensing for the moments that matter in cattle care.**

[![CI](https://github.com/zxq309/cowmata/actions/workflows/docs.yml/badge.svg)](https://github.com/zxq309/cowmata/actions/workflows/docs.yml)
![Documentation updated](https://img.shields.io/badge/docs-2026--09--07-0A7EA4)
![Scope](https://img.shields.io/badge/COWMATA-project-92C142)

[English](README.md) · [简体中文](README.zh-CN.md) · [COWMATA](https://github.com/zxq309/cowmata)

</div>

<p align="center"><img src="assets/showcase/farm-wearing.jpeg" width="860" alt="Tail rings in the field: extending occasional checks with continuous observation."><br><em>Tail rings in the field: extending occasional checks with continuous observation.</em></p>

## What this project does

COWMATA is a smart cattle tail-ring and companion software project developed by Yangling Yuanshangyuan Intelligent Technology Co., Ltd. It covers cattle reproduction, behavior and health monitoring. The sensor captures nine-axis IMU together with temperature and PPG; synchronized video provides reviewable evidence for behavior and calving events.

The project aims to turn continuous observations into behavior timelines and risk evidence for farm reproductive management and health observation. Calving is the current research and field-experiment priority; estrus, pregnancy and health/disease-risk monitoring are separate follow-on research tasks.

**This repository is the single project overview:** products, application context, team, progress and component responsibilities. The three specialist repositories focus on their own functionality, interfaces, usage and validation.

## Hardware and application context

The tail-ring worn near the tail root is the sensing entry point, supported by synchronized video annotation, behavior recognition and decision research. Existing product imagery represents farm and veterinary editions.

<table><tr><td align="center" width="50%"><img src="assets/showcase/farm-edition.jpeg" width="420" alt="Tail sensor farm edition"><br>Farm edition</td><td align="center" width="50%"><img src="assets/showcase/veterinary-edition.jpeg" width="420" alt="Tail sensor veterinary edition"><br>Veterinary edition</td></tr></table>

| Product / component | Intended context | Role in the project |
|---|---|---|
| Tail-ring · farm edition | Farm reproductive management and daily observation | Continuous sensing for estrus, pregnancy and calving monitoring research |
| Tail-ring · veterinary edition | Reproductive and animal-health observation | Auxiliary observations for professional review and research |
| Video–IMU annotator | Data collection, experiments and review | Align video/signals and produce traceable state/event labels |
| Recognition and decision software | Algorithm development and evaluation | Produce behavior events and multimodal auxiliary evidence respectively |

A complete farm service, business frontend/backend and unified alert deployment have not been delivered by these four repositories. Product information: [COWMATA website](https://www.cowmata.com/); provenance and usage terms: [assets/README.md](assets/README.md).

## From field observations to software

**Wear & sense → Review video → Identify behavior → Combine risk evidence → Act & record.** Tail rings capture changes, annotation establishes ground truth, recognition locates events, and decision research combines observations for human review.

<p align="center"><img src="assets/showcase/annotation-workstation.png" width="860" alt="Synchronized video and sensor annotation workstation"><br><em>Aligned video and sensor signals make behavior labels traceable to field observations.</em></p>

<p align="center"><a href="https://zxq309.github.io/cowmata/showcase/en.html"><img src="assets/showcase/product-packaging.png" width="640" alt="Tail-ring product and packaging"></a><br><strong><a href="https://zxq309.github.io/cowmata/showcase/en.html">Explore product imagery and field video →</a></strong></p>

The gallery presents hardware, field use, software interfaces and a calving video extracted from the project presentation dated 2026-08-26. Product imagery does not establish delivery of a complete platform in this repository; the video illustrates the observation setting. Original interface screenshots retain their Chinese labels, with English explanations alongside them.

## Research progress and capability boundaries

| Direction | Available today | Next step |
|---|---|---|
| Behavior/event recognition | Continuous-IMU training/inference baseline, review workflow and cow-level evaluation | More labels, hard negatives and independent validation |
| Calving | Temperature/activity evidence modules and ongoing field experiments | Event integration, fusion calibration and continuous-warning validation |
| Estrus and pregnancy | Project research and data-collection directions | Task-specific ground truth, models and independent evaluation |
| Health/disease risk | Multimodal data and feasibility-research direction | Quality assessment, control data and task validation |

Auxiliary evidence is not a calibrated calving probability; a product direction is not a completed diagnostic capability. Specialist repositories record specific software and experiment versions.

## Four repositories, one project

| Repository | Responsibility |
|---|---|
| [cowmata](https://github.com/zxq309/cowmata) | System architecture, roadmap and demos |
| [cowmata-tailring](https://github.com/zxq309/cowmata-tailring) | Behavior/event training, inference and evaluation |
| [cowmata-risk](https://github.com/zxq309/cowmata-risk) | Decision research; private, authorized access |
| [cattle-tail-ring-annotator](https://github.com/zxq309/cattle-tail-ring-annotator) | Annotation and human review |

## Current system architecture

<p align="center"><img src="assets/figures/system-en.svg" width="860" alt="System architecture"></p>

## Explore the system demo

**[Open the live interactive demo →](https://zxq309.github.io/cowmata/demo/?lang=en)** — no installation required. The same page also works offline.

<p align="center"><img src="assets/screenshots/system-demo-en.png" width="860" alt="Offline system demo"></p>

Clone this repository and open **[demo/index.html](demo/index.html)** in a browser. It works offline, switches between English and Chinese, and shows normal, changing-evidence and missing-data scenarios. All displayed values are illustrative; no recognition or risk model runs in this page.

```sh
git clone https://github.com/zxq309/cowmata.git
cd cowmata
python -m http.server 8000 --bind 127.0.0.1
# Open http://127.0.0.1:8000/demo/
```

For **actual component execution**, see [the demo guide](docs/DEMO.md). The runner invokes the recognition demo and optionally the authorized risk demo, records component commits and returns failure if a selected component fails. It does not pretend that the components form a validated fused pipeline.

## Documentation and reproducibility

- [Roadmap](docs/ROADMAP.en.md) · [Interface proposal](docs/INTERFACES.en.md)
- [Pinned component commits](components.json) · [Maintenance](docs/MAINTENANCE.en.md)
- [Demo guide](docs/DEMO.md) · [Asset provenance](assets/README.md)
- [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Notice](NOTICE)

## Team

The development company is **Yangling Yuanshangyuan Intelligent Technology Co., Ltd.**, under the **COWMATA** brand. Team information is maintained here; component contribution and citation records remain in their owning repositories.

| Member | Role / affiliation |
|---|---|
| Xiangqing Zhang（张向清） | CTO, Yangling Yuanshangyuan Intelligent Technology Co., Ltd.; Yan'an University; Postdoctoral Researcher, Northwestern Polytechnical University |
| Yalong Zhang | Founder, Yangling Yuanshangyuan Intelligent Technology Co., Ltd. |
| Tengyu Jiao | Yan'an University |
| Yachen Zhao | Yan'an University |

<p align="center"><img src="assets/brand/cowmata-company-logo.png" height="64" alt="Yangling Yuanshangyuan Intelligent Technology Co., Ltd."></p>

Company/product inquiries: [official contact page](https://www.cowmata.com/contact/). Reproducible software issues belong in the relevant specialist repository; cross-component interfaces and overall roadmap discussions belong here.

## Latest update

**2026-09-07** — Corrected Xiangqing Zhang’s Chinese name and added his postdoctoral affiliation at Northwestern Polytechnical University; added original presentation media, bilingual galleries and centered imagery. [Full changelog](CHANGELOG.md).
