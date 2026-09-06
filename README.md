<div align="center">
<a href="https://www.cowmata.com/"><img src="assets/brand/cowmata-logo.svg" width="360" alt="COWMATA"></a>

# COWMATA · Cattle Monitoring

**From tail-ring sensing to reviewable behavior and risk evidence.**

[![CI](https://github.com/zxq309/cowmata/actions/workflows/docs.yml/badge.svg)](https://github.com/zxq309/cowmata/actions/workflows/docs.yml)
![Documentation updated](https://img.shields.io/badge/docs-2026--09--07-0A7EA4)
![Scope](https://img.shields.io/badge/COWMATA-project-92C142)

[English](README.md) · [简体中文](README.zh-CN.md) · [COWMATA](https://github.com/zxq309/cowmata)

</div>

![COWMATA project concept](assets/figures/cowmata-ai-pipeline-hero.png)

*Concept illustration, not a deployed application screenshot.*

## Latest update

**2026-09-07** — Bilingual project portal, relocated product assets, current system diagrams, offline interactive demo and component-demo runner. See [CHANGELOG.md](CHANGELOG.md). Documentation dates are separate from component release dates.

## What this project does

COWMATA connects tail-mounted sensing, synchronized video review, behavior recognition and decision research for cattle reproduction and health. Calving is the current experimental priority. Estrus, pregnancy and health monitoring remain broader project directions; each needs its own data and validation.

## Four repositories, one project

| Repository | Responsibility |
|---|---|
| [cowmata](https://github.com/zxq309/cowmata) | System architecture, roadmap and demos |
| [cowmata-tailring](https://github.com/zxq309/cowmata-tailring) | Behavior/event training, inference and evaluation |
| [cowmata-risk](https://github.com/zxq309/cowmata-risk) | Decision research; private, authorized access |
| [cattle-tail-ring-annotator](https://github.com/zxq309/cattle-tail-ring-annotator) | Annotation and human review |

## Current system architecture

![System architecture](assets/figures/system-en.svg)

**Available:** annotation workstation, recognition baseline, temperature/activity evidence modules. **Next:** behavior-to-decision adapter, calibrated fusion and unified alerts. The private risk repository is not required to use the public tools.

## Explore the system demo

![Offline system demo](assets/screenshots/system-demo-en.png)

Clone this repository and open **[demo/index.html](demo/index.html)** in a browser. It works offline, switches between English and Chinese, and shows normal, changing-evidence and missing-data scenarios. All displayed values are illustrative; no recognition or risk model runs in this page.

```sh
git clone https://github.com/zxq309/cowmata.git
cd cowmata
python -m http.server 8000 --bind 127.0.0.1
# Open http://127.0.0.1:8000/demo/
```

For **actual component execution**, see [the demo guide](docs/DEMO.md). The runner invokes the recognition demo and optionally the authorized risk demo, records component commits and returns failure if a selected component fails. It does not pretend that the components form a validated fused pipeline.

## Hardware and application context

<table><tr><td align="center" width="50%"><img src="assets/product/tail-sensor-farm.png" width="300" alt="Tail sensor farm edition"><br>Farm edition</td><td align="center" width="50%"><img src="assets/product/tail-sensor-vet.png" width="300" alt="Tail sensor veterinary edition"><br>Veterinary edition</td></tr></table>

Official company product imagery, relocated from the algorithm repository. Product context is broader than the currently validated software scope.

## Documentation and reproducibility

- [Roadmap](docs/ROADMAP.en.md) · [Interface proposal](docs/INTERFACES.en.md)
- [Pinned component commits](components.json) · [Maintenance](docs/MAINTENANCE.en.md)
- [Demo guide](docs/DEMO.md) · [Asset provenance](assets/README.md)
- [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Notice](NOTICE)

## Team

Developed by the COWMATA team at Yangling Yuanshangyuan Intelligent Technology Co., Ltd., with research collaboration from Yan'an University. Xiangqing Zhang · Yalong Zhang · Tengyu Jiao · Yachen Zhao.
