---
name: ha-dashboard-design
description: Use when designing or changing Home Assistant dashboards for a wall tablet or for phones. Layout, navigation, overlays, privacy and the technical traps (strict-mode templates, subviews, kiosk) learned from building real ones.
---

# Dashboard design (wall tablet and phones)

## Wall tablet

- **Sections views** with a clear Home page: greeting, an **attention strip** that lists only what needs someone (doors open, leaks, rain, appliance done), people, alarm, climate, quick actions (Leaving / Arriving / Good night).
- Navigation chips in a **footer**; room pages as **subviews**.
- A screensaver (photos, clock, now playing) with **edge taps that close it**. Never swallow taps.
- Overlays (smoke alarm screen, alarm PIN entry, leaving countdown) are fixed-position cards with **visibility conditions**.
- Settings that change the panel itself (screensaver mode, guest mode, admin) sit behind a **PIN**.

## Phones

- A **separate dashboard**, built from the tablet's cards so the logic stays identical. A copy, so re-check it when the tablet changes.
- **Never kiosk mode** on phones, and keep the header and menu.
- **Bottom tab bar** (e.g. navbar-card) with 4-5 items plus a "More" popup; make every other view a **subview** so Home Assistant's top tabs disappear and the header shows a back arrow.
- No pop-ups or overlays; show countdowns inline (e.g. "Leaving · Cancel / Arm now").
- Alerts as one per line, left-aligned; drop the big clock (the phone has one).
- A simpler view for less technical household members via **user visibility conditions** on sections and cards.

## Technical traps

- **Markdown cards render templates in strict mode.** `selectattr('attributes.device_class', 'eq', …)` fails on entities without that attribute; guard with `selectattr('attributes.device_class', 'defined')` first. Give each block its own `namespace` name.
- Paths change when you copy a dashboard; rewrite every `navigation_path`.
- Verify at the real viewport size (tablet ~1194×834, phone ~402×874) with screenshots before calling it done.

## Privacy for screenshots

People-free photos only; blur maps, balances and small avatars; no names or addresses.
