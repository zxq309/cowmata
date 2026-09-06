# Four-repository maintenance

[简体中文](MAINTENANCE.md)

The hub owns project scope, roadmap and component combinations. Components own their code, interface documentation, tests, changelogs and releases. Cross-component work is coordinated in the hub with links to affected changes.

Repositories release independently; version numbers need not match. Record fixed commits in `components.json`, not an ambiguous “latest” reference. Validate components first, then fixed cross-repository exchange samples; only tested combinations may be declared compatible.

Maintain code in its owning repository. The annotator should consume recognition through an adapter rather than duplicate model logic. Private experiment details stay in the decision repository; public components remain usable without it.

Every user-visible update changes both README latest-update summaries and CHANGELOG in the same commit. Distinguish documentation maintenance dates, experiment dates and tagged software releases. Do not rewrite a historical release date to make a repository appear newer.
