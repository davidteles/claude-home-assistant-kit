# Changelog

All notable changes to this project. Versions follow [semantic versioning](https://semver.org/); each entry links to its full release notes on GitHub, which also say how each change was tested.

## [0.3.0] — 2026-11-17

Lessons from a week of real use.

- Back up before changing anything.
- Presence automations: ignore phone-app blips, respect a **Guest at home** switch, and give each job **one owner** (not Apple Home *and* Home Assistant). Find who sent a command from the logbook context.
- Template traps: text `false` in automation variables is truthy; read state when a queued run starts; pair readings from two devices by time.
- Guided test sessions that the user starts, one step at a time; progress and rollback rules for shadow tests.
- Bump the version on every new file; a since-last-version note, a real-life check table, a review page and NEW / UPDATED badges.
- Check an OK (release, merge) hasn't already happened before asking for it.

## [0.2.0] — 2026-11-09

First public release.

- **Skills:** house rules (guardrails, naming, real testing, HomeKit Bridge hygiene), notification conventions, first-run feedback checks, the Now / Later / Ignore triage PDF, wall-tablet and phone dashboard design, statistics repair and backfill, small custom integrations.
- **Commands:** `/ha-review` (read-only, ranked health review), `/ha-checks`, `/ha-triage-pdf`.
- **Blueprint:** first-run feedback checks (import button in the README).

[0.3.0]: https://github.com/davidteles/claude-home-assistant-kit/releases/tag/v0.3.0
[0.2.0]: https://github.com/davidteles/claude-home-assistant-kit/releases/tag/v0.2.0
