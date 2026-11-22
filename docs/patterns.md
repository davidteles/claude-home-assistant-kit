# Patterns worth reusing

Knowledge, not features: ways of building that held up. Examples use made-up places and people.

## Preflight only what's enabled

Check prerequisites per feature the user turned on: the cards it needs, the helpers it reads, the entities it names. A doorbell nobody configured shouldn't block a first install. Keep two steps apart: **"is the file valid?"** (no Home Assistant needed) and **"does this Home Assistant have it?"** (a template pasted in Developer tools works without any token).

## Device-first layouts

Lay a page out by what the device is for (wall tablet: glanceable, big touch targets, one screen; phone: one column, the tab bar) before adding cards. Prefer built-in cards; add a custom card only for something built-ins can't do, and list it as a prerequisite of the feature that needs it.

## Native first for kiosks

Use what the tablet's kiosk app or Home Assistant already does (screen on/off, screensaver, hide header) before adding automations for it. When you do automate:

- **Camera on demand** (open it when someone asks), **wake on motion** (screen on, nothing else), and **doorbell navigation** (go to the door page, then **return** to where it was, with a timeout fallback if the page can't be reached) are three separate features. Ship each one off by default.
- No permanent camera feed on a screen, and no guest-visible screen that shows people's whereabouts.

## Suggest a zone after repeated long stops (design only)

A quiet suggestion for a **place someone keeps going to**, not an alert about stops and not a route tracker.

- **Opt-in per person**, suggestions to that person only. Reuse the existing location reports; never ask for more frequent tracking to make it work. If the data is too sparse, say "not enough signal" and stop.
- **Starting rules** (tune after a dry run): outside any zone; **45 min** observed dwell; **three visits on three different days within 30 days**; candidates grouped at about **100 m**. Fresh, accurate fixes from more than one moment; a clear departure before counting the next visit. One stale fix, a reporting gap or GPS drift is not a visit; an overnight stay counts once.
- **Store the minimum:** the candidate centre, visit dates and a dismissed/expiry state. No route log, no learned model, no reverse geocoding, no coordinates in notification text. Check what the recorder would keep a second copy of, and expire candidates.
- **Ask once:** "You've spent time here on three different days. Save it as a zone?" with **Review** and **Ignore**. A person places the pin, name and radius; nothing creates a zone automatically. Ignoring stops further prompts for that place (with a cooldown and a way to clear it).
- **Ship it as a blueprint only if** persistence, expiry and dismissal fit a small, documented set of helpers. If it needs custom storage, it stays a pattern.
- **Acceptance:** one long stop doesn't prompt; three separate qualifying visits prompt once; drive-bys, GPS jumps, stale or inaccurate fixes and known zones don't qualify; nearby distinct places aren't merged; dismissal and expiry survive a restart; ignoring or disabling never changes any zone.

**Routes are parked.** Paths add storage and false alarms without helping decide whether a stop recurs.
