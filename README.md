# Claude Home Assistant Kit

**Build your smart home with an AI pair-programmer: safely, step by step, without breaking what your family relies on.**

A plugin for [Claude Code](https://claude.com/claude-code). It packages a way of working that grew out of turning a real home's Home Assistant into a wall-panel-driven, notification-smart, family-friendly system with Claude: the guardrails, conventions and workflows that made it work. It isn't a set of dashboards to copy (those live in their own repos). It's the **method**.

**See it in action:** [a worked example](docs/worked-example.md) follows one real fix from `/ha-review` to the household confirming it, including how it would have been rolled back.

## Trust and permissions

This kit is **instructions**: skills and commands that shape how Claude works. They are not a security boundary. What Claude can actually do is decided by the connection you give it, the Home Assistant account behind it, and Claude Code's own permission settings.

| Layer | What enforces it | What it means |
|---|---|---|
| **Claude Code** | Its permission mode | In the default mode, Claude asks before running commands and tools you haven't allow-listed. Don't run it with permission checks bypassed against a live home. |
| **The connection to Home Assistant** | The MCP server or API you set up | Home Assistant's own **MCP Server** integration only reaches entities you exposed to Assist and can't edit configuration, **but it can control them**: switch lights, open covers, unlock an exposed lock. Community MCP servers can usually edit automations, dashboards and helpers; some offer a **read-only mode**. A logged-in browser session has that user's full rights. |
| **The Home Assistant account** | Home Assistant | A token or session acts as its user. **Non-admin** users can control devices but can't change configuration; **admins** can change everything. Home Assistant has no built-in read-only user. |
| **The house rules** (this kit) | Nothing: Claude follows them | Back up first, ask before anything destructive, never open doors, no credentials in chat. They make Claude careful; they don't stop it. |

**Recommended start:** connect read-only (Home Assistant's MCP Server, or a community server in read-only mode), run `/ha-review`, and only give write access when you want Claude to change something. Keep Claude Code in its default permission mode.

**"Can't edit configuration" is not "inspect-only".** A connection that can't change automations may still operate every device it can see. For a truly inspect-only start, use a server in read-only mode, or expose nothing you wouldn't want switched. [Permission checks](docs/workflow-checks.md#permission-checks) shows how to find out with a harmless helper.

- **Read-only:** reviews, reading traces and logs, reading configuration.
- **Writes, each one approved:** automations, scripts, helpers, dashboards, settings. Claude states the change and the backup first.
- **Never in this repo or in chat:** passwords, tokens, alarm codes, HomeKit setup codes, Bluetooth keys, addresses, family names.

[docs/testing.md](docs/testing.md) explains the three kinds of test (scenario tests, live simulations, physical first runs) and how to dry-run a change and its rollback. [docs/patterns.md](docs/patterns.md) collects design patterns worth reusing. [docs/workflow-checks.md](docs/workflow-checks.md) has four repeatable checks for the workflow (a review doesn't write, a write waits for approval, failures are reported, first-run checks close) and, separately, the permission checks worth doing when you set up the connection.

## What's inside

### Skills (Claude loads them when they're relevant)

| Skill | What it gives Claude |
|---|---|
| `ha-house-rules` | Guardrails (never open doors, no credentials in chat, don't break what the family uses), naming, categories/labels, real testing, backups, presence and guest rules, template traps, guided test sessions, HomeKit Bridge hygiene |
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
| `/ha-triage-pdf` | Build the triage PDF from the current backlog (the `ha-triage-pdf` skill) |
| `/ha-checks` | List pending first-run checks and close the confirmed ones |

### Blueprint

- [`blueprints/first_run_checks.yaml`](blueprints/first_run_checks.yaml): the first-run feedback automation, ready to import.

  [![Import blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fdavidteles%2Fclaude-home-assistant-kit%2Fblob%2Fmain%2Fblueprints%2Ffirst_run_checks.yaml)

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

Import the blueprint with the button above, or in Home Assistant: *Settings → Automations & scenes → Blueprints → Import blueprint* and paste the blueprint's GitHub URL.

## Remove it

```
/plugin uninstall home-assistant-kit@claude-home-assistant-kit
/plugin marketplace remove claude-home-assistant-kit
```

Delete the automation made from the blueprint, and the blueprint, in Home Assistant if you imported it. What Claude remembered about your home stays in your local Claude memory, not here: delete it there if you want it gone.

## How to work with it

1. **Start with a review:** `/ha-review`. Claude ranks what matters and changes nothing yet (and *can't*, if the connection is read-only).
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

Built with this workflow:

- [`ha-blueprints`](https://github.com/davidteles/ha-blueprints): automations, each tested for real before release.
- [`ha-wall-panel-kit`](https://github.com/davidteles/ha-wall-panel-kit): the wall tablet and phone dashboards (`ha-dashboard-design`).
- [`ha-delonghi-ddsx`](https://github.com/davidteles/ha-delonghi-ddsx): the `ha-custom-integration` skill in practice, with regression tests against a fake device.
- [`ks-glass-info`](https://github.com/davidteles/ks-glass-info) and [`ha-festive-panel`](https://github.com/davidteles/ha-festive-panel): the idle tablet screen and the seasonal layer.

## Contributing

Ideas, new skills and fixes are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[MIT](LICENSE)
