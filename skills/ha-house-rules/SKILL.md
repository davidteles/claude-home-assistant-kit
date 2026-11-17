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
- **Back up before you change.** Save the old config (automation, script, dashboard, YAML file) to a dated rollback file first, and name it in the description or your report.

## Presence ("everyone left") automations

- **Ignore presence blips.** A phone app reloading makes its person `unknown` for a split second, which can look like "everyone left". Use `not_from: [unknown, unavailable]` on state triggers, or check `trigger.from_state` / `to_state` on zone triggers, or require the empty house to last a minute.
- **Respect a guest.** If the home has a "Guest at home" toggle (or should have one), every automation that acts on an empty house (arming the alarm, lights off, blinds, heating away, leaving reminders, screen off) checks it first. Nobody wants to leave a guest in the dark with the alarm armed around them.
- **One owner per job.** If Apple Home, Google Home or a vendor app also has an "everyone left" automation, two systems fight over the same lights, and the phone apps' presence can misfire. Pick one (usually Home Assistant, which has the guards above) and ask the user to switch the other off.
- **Who did it?** When "everything turned off" and no automation ran, check the logbook context: HomeKit Bridge entries ("send command turn_off for …") mean the command came from Apple Home, not from Home Assistant.

## Templates that bite

- **`false` written as text in automation `variables` stays the string "false", which is truthy.** In variables, write `{{ false }}` / `{{ true }}` (or a full expression). In template *conditions* and *triggers*, text "false" is fine.
- Read the state **when the run starts**, not when it was triggered, in `queued` automations: several sensors changing in the same second otherwise each act on old state (duplicate notifications, double cards).
- Combining two readings from different devices (e.g. two energy clamps)? Check they are from the same moment (`last_reported` within a second or two) before doing maths with them.

## Helpers and entities

- Give entities human names; rename entity IDs *before* anything else references them (bridges, dashboards).
- Don't expose internal helpers (panel flags, automation state) to Apple Home or voice assistants.

## HomeKit Bridge (Apple Home)

- **List entities one by one. Never include whole domains.** A whole-domain rule silently picks up every new entity at the next bridge reload and floods Apple Home.
- Any save reloads the bridge. Afterwards, read the bridge's diagnostics and check the accessory list is exactly what you intended.

## Testing with the user

- Some things can only be checked in real life (presence, alarms, phone cards). Offer a **guided test session**: a short script of steps (what they do / what you do / what they should see / the question you'll ask), saved where they can read it first.
- **The user starts it**, at a time that suits them. Run one step at a time and ask after each one. Keep steps reversible and never include doors, gates, locks or codes.
- Long-running comparisons (a new controller shadowing an old one) report progress every time: runs so far, your confidence, and the last bug fixed. Switch over only when the user agrees; keep the old one installed but stopped for a quick rollback, and remove it after a few good days.

## Working style

- Keep a visible task list and report outcomes faithfully, including what you didn't verify.
- Prefer small, reversible steps; keep a copy of what you change (e.g. Energy settings) so it can be restored.
- When something a person relies on breaks (alerts, presence, alarm), fix that before anything cosmetic.
