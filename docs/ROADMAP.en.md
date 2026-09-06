# Project roadmap

[简体中文](ROADMAP.md)

## Current priority: calving experiments

1. Continue video/IMU annotation and human review, separating behavior labels from calving outcome anchors.
2. Develop behavior and event models in the recognition repository, retaining time and quality metadata.
3. The risk repository already contains temperature and activity evidence modules. Verify binding, timing, missing data and state restoration first.
4. Implement the event adapter and fusion strategy using fixed cow/calving development, validation and test splits.
5. Evaluate first valid warning lead time, misses, false alerts per cow/day and observation coverage before deployment.

## Later tasks

Estrus, pregnancy and health research remain task modules in the decision repository until ownership, dependencies, permissions or release schedules justify further separation.

A complete alert service, frontend/backend and farm deployment have not been delivered by these repositories. The system hub will own integration when these components are built.
