---
name: ha-first-run-checks
description: Use after adding or changing a Home Assistant feature that can only be confirmed in real life (alerts, presence, countdowns, appliance behaviour). Sets up a first-run feedback note so the user confirms it works, instead of a to-do list nobody reads.
---

# First-run feedback checks

Many features can't be fully tested while you're at the keyboard: a reminder that fires at 22:00, an alert when a tank fills, presence when someone leaves. Instead of asking the user to remember to test, let Home Assistant ask them **the first time the feature runs for real**.

## Pattern

One automation ("Checks - ask for feedback the first times a new feature runs") holds a dictionary of `feature → question`:

- **Trigger:** the event that *really matters* for each feature (not every run). Use `automation_triggered` for simple cases, a specific state (`door open for 10 min`), or a custom event the feature fires only when it truly acts:
  ```yaml
  - event: checks_feature_ran
    event_data: { feature: automation.notify_dehumidifier_tank }
  ```
- **Action:** `persistent_notification.create` with `notification_id: check_<feature>` (one per feature, never piles up): "Just ran for real (Sat 08 Nov, 12:08). *Question.* Tell Claude what you saw, then dismiss this."

## Lifecycle

1. Add the feature → add its entry to the checks dictionary and a trigger.
2. It runs for real → the user sees the note and tells you what happened.
3. User confirms it works → **remove the entry and trigger**, dismiss the note, and record the confirmation in the automation's description.
4. It didn't work → fix it and keep the entry.

See `blueprints/first_run_checks.yaml` for a ready-made version.
