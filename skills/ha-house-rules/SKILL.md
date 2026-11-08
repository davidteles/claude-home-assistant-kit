---
name: ha-house-rules
description: Read before creating or changing anything in a Home Assistant instance (automations, scripts, helpers, dashboards, integrations, HomeKit bridges). The ground rules for working safely on a family's live home - guardrails, naming, categories and labels, testing, and what must never be touched.
---

# Home Assistant house rules

A Home Assistant instance is a family's live home, so everything you change is felt by real people. Work like a careful electrician, not a demo.

## Guardrails (never break these)

- **Physical safety first.** Never open garage doors, gates or locks yourself, not even to test. Two-stage confirmation for doors is a feature, not friction.
- **No credentials in chat.** Never type, print, store or repeat passwords, PINs, alarm codes, tokens, HomeKit setup codes or Bluetooth keys (IRKs). The user enters them in their own UI. If a flow needs a code, stop and hand over.
- **Don't break what the family uses.** Apple Home, Google Home, voice assistants and the wall panel must keep working. Before changing a bridge, a dashboard others use or a shared device, say what will change for them.
- **Ask before anything destructive or security-related:** deleting, disabling the alarm or its triggers, removing devices, changing who can do what.
- **Never enable "kiosk" lock-in on personal phones.** A phone stuck in a dashboard with no way out is a real problem.

## Every automation

- **Alias:** `Area/Topic - what it does`, e.g. `Notify - weekly safety check`, `Entrance - lights off when no motion`.
- **Description:** what it does, when it was added or changed (absolute date), who asked and *why*. Future you will thank you.
- **Category and labels:** always set them; create a category if none fits.
- **Native triggers and conditions** over templates; templates belong in messages and variables.
- **Test it for real.** Run it (or trigger its path), read the trace, and report what actually happened. Don't say "should work".
- **New behaviour gets a first-run check** (see `ha-first-run-checks`) so the user confirms it in real life.

## Helpers and entities

- Give entities human names; rename entity IDs *before* anything else references them (bridges, dashboards).
- Don't expose internal helpers (panel flags, automation state) to Apple Home or voice assistants.

## HomeKit Bridge (Apple Home)

- **List entities one by one. Never include whole domains.** A whole-domain rule silently picks up every new entity at the next bridge reload and floods Apple Home.
- Any save reloads the bridge. Afterwards, read the bridge's diagnostics and check the accessory list is exactly what you intended.

## Working style

- Keep a visible task list and report outcomes faithfully, including what you didn't verify.
- Prefer small, reversible steps; keep a copy of what you change (e.g. Energy settings) so it can be restored.
- When something a person relies on breaks (alerts, presence, alarm), fix that before anything cosmetic.
