# Cross-repository interface proposal · draft 0.1

[简体中文](INTERFACES.md)

This is a design proposal, not a claim that every component implements it. Existing component schemas remain authoritative.

## Annotation → recognition

Retain cow/session/binding identity, protocol version, machine label code, point versus interval semantics, absolute timestamps, provenance and human-review status. Calving outcome labels and behavior-training labels need separate mappings. Unknown labels must be rejected or explicitly reported, never silently converted to background.

Annotatable labels can exceed a model's supported classes. For example, `TAIL_WAGGING` needs explicit protocol/model mapping rather than rewriting historical label meaning.

## Recognition → decision (adapter pending)

Proposed fields: `schema_version`, `cow_id`, `binding_id`, `event_id`, `event_code`, `start_ms`, `end_ms`, `score`, `quality_status`, `model_version`, `produced_at_ms`, `available_at_ms`.

Distinguish persistent states and discrete events. All `*_ms` fields use Unix milliseconds. Event occurrence and result availability differ; replay must respect availability to avoid future-data leakage. Preserve uncertain binding quality and deduplicate using explicit identifiers/rules.

## Auxiliary modules → decision

Use the temperature/activity `output.schema.json` and `as_fusion_features` in cowmata-risk. Keep binding identity consistent and preserve evidence, quality, freshness and versions. Scores are not calibrated calving probabilities.

## Compatibility gate

Before enabling adapters, use fixed samples to check label mapping, timestamp units, point/interval semantics, duplicates, missing evidence and version rejection. `components.json` registers baselines only; these cross-repository checks are not yet declared complete.
