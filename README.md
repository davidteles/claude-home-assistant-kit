# Claude Home Assistant Kit

**Build your smart home with an AI pair-programmer: safely, step by step, without breaking what your family relies on.**

A plugin for [Claude Code](https://claude.com/claude-code). It packages a way of working that grew out of turning a real home's Home Assistant into a wall-panel-driven, notification-smart, family-friendly system with Claude: the guardrails, conventions and workflows that made it work. It isn't a set of dashboards to copy (those live in their own repos). It's the **method**.

## What's inside

### Skills (Claude loads them when they're relevant)

| Skill | What it gives Claude |
|---|---|
| `ha-house-rules` | Guardrails (never open doors, no credentials in chat, don't break what the family uses), naming, categories/labels, real testing, HomeKit Bridge hygiene |
| `ha-notifications` | Readable phone alerts: short push + full report, "press and hold" for buttons, tags that replace and clear, real signals over guesses |
| `ha-first-run-checks` | Let Home Assistant ask *you* whether a new feature worked, the first time it runs for real |
| `ha-triage-pdf` | Turn a backlog into a fillable Now / Later / Ignore PDF and read the answers back |
| `ha-dashboard-design` | Wall tablet and phone dashboards: layout, navigation, overlays, strict-mode template traps, privacy |
| `ha-statistics-repair` | Fix meter glitches and backfill split meters without breaking the Energy dashboard |
| `ha-custom-integration` | Write a small custom integration to unlock hidden device features, then package it for others |

### Commands

| Command | Does |
|---|---|
| `/ha-review` | A ranked health review: safety first, then what people notice, then quick wins. Read-only. |
| `/ha-triage-pdf` | Build the triage PDF from the current backlog |
| `/ha-checks` | List pending first-run checks and close the confirmed ones |

### Blueprint

- [`blueprints/first_run_checks.yaml`](blueprints/first_run_checks.yaml): the first-run feedback automation, ready to import.

## Requirements

- [Claude Code](https://claude.com/claude-code).
- A Home Assistant instance Claude can reach. For example, a Home Assistant MCP server for the API, and/or a browser session on your Home Assistant.
- Optional: Python with `reportlab`, `pypdf` and `pypdfium2` for the triage PDFs.

## Install

In Claude Code:

```
/plugin marketplace add davidteles/claude-home-assistant-kit
/plugin install home-assistant-kit@claude-home-assistant-kit
```

Import the blueprint in Home Assistant: *Settings → Automations & scenes → Blueprints → Import blueprint* and paste the blueprint's GitHub URL.

## How to work with it

1. **Start with a review:** `/ha-review`. Claude ranks what matters and changes nothing yet.
2. **Decide calmly:** `/ha-triage-pdf`, then fill it in on your phone or tablet and hand it back.
3. **Build in small steps.** Claude follows the house rules: it tests each change for real, tags it, documents why, and adds a first-run check when only real life can confirm it.
4. **Close the loop.** When a check note appears, tell Claude what happened (`/ha-checks`).
5. **Teach it your home.** Keep personal facts (who lives there, which devices are sensitive, what you declined) in Claude's local memory, never in this repo.

## Principles

- **The household comes first.** Safety alerts and the things people use daily beat anything cosmetic.
- **Reversible, visible, verified.** Small steps, a copy of what changes, and an honest report of what was and wasn't tested.
- **Real signals over guesses.** Alerts that cry wolf get ignored.
- **Privacy by default.** No credentials in chat, no personal data in repos or screenshots.

## Related repos

- [`ha-delonghi-ddsx`](https://github.com/davidteles/ha-delonghi-ddsx): an example of the `ha-custom-integration` skill in practice.

## Contributing

Ideas, new skills and fixes are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[MIT](LICENSE)
