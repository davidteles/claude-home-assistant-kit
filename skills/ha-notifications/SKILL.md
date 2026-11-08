---
name: ha-notifications
description: Use whenever a Home Assistant automation or script sends a phone (mobile app) notification. Conventions for readable pushes - short push plus persistent notification for long reports, tap-to-open links, action buttons that say "press and hold", tags that replace and clear.
---

# Phone notification conventions

## Long reports: short push + full report

iOS cuts long pushes off ("…"). For anything longer than ~3 lines:

1. **Push:** one line ending "Tap for the details." Set `data.url` to a page that shows the full report (a live dashboard page, or `/energy`). Home Assistant has no URL that opens the notification drawer itself.
2. **Persistent notification:** the full report via `persistent_notification.create` with a **fixed `notification_id`** so each run replaces the last one.
3. A **live dashboard page** with the same report is the most reliable target: persistent notifications are cleared when Home Assistant restarts.

## Action buttons

Buttons are hidden until you press and hold. Every push with `data.actions` ends its message with a new line:

```
👆 Press and hold for: Remind me in 30 min · Done
```

## Tags: replace and clear

- Give each kind of alert a `tag` (e.g. `dehumidifier-tank`). A newer push with the same tag replaces the old one.
- When the situation resolves, clear it: send `message: clear_notification` with the same tag. Users love alerts that disappear when they're no longer true.
- Use a `group` per topic (`home-summary`, `appliances`).

## Who and when

- Send to the person who can act. Use a helper script (e.g. `script.notify_phones` with an `only_<person>` flag) so recipients are one change away.
- Urgent / act-now alerts (alarm, leak, smoke, door left open) stay as full-text pushes. Never hide them behind a tap.
- Prefer **real device signals** over guesses. A "stopped by itself" heuristic will fire on mode changes and train people to ignore alerts.
- Add a delay where people are mid-task (e.g. wait 2 minutes before "empty the tank").

## Example

```yaml
- action: persistent_notification.create
  data:
    notification_id: weekly_safety_check
    title: "🛡️ Weekly safety check"
    message: "{{ report }}"
- action: notify.mobile_app_phone
  data:
    title: "🛡️ Weekly safety check"
    message: "{{ short }}"
    data: { tag: weekly-safety-check, group: home-summary, url: /dashboard-phone/safety-check }
```
