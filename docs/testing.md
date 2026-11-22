# Three kinds of test

Say which one you mean. "Tested" without the kind is how a CI run or a sent notification gets mistaken for "it works in the house".

| Kind | What runs | What it proves | What it can't prove |
|---|---|---|---|
| **Scenario test** | The real blueprint or automation in a throw-away test Home Assistant (e.g. `pytest-homeassistant-custom-component`). Devices are plain states; service calls are recorded, not executed; the clock is moved forward | The logic: every branch, edge cases, restarts, timing, what would be sent | That your devices, integrations, phone app or network behave like the fakes |
| **Live simulation** | Your real Home Assistant, but only with **inert helpers** (toggles nothing listens to) and a **sink** script instead of real notifications | Your real templates, entity ids and integrations' states, without touching a device | How a real device or a person reacts |
| **Physical first run** | The real device, with a person there who agreed to it | That it works in the house | Anything you didn't watch happen |

Rules of thumb:

- Write the scenario test first, especially for a bug report: reproduce it, then fix it.
- A live simulation never actuates hardware and never sends a real notification. If it would, it is a physical first run: ask first.
- A physical first run is planned, short and watched. Afterwards, record **ID · version · environment · steps · result · sanitized evidence · next action**.
- CI passing, a notification "sent", or a browser at a phone's width are not physical verification.

## Dry-run a change and its rollback

Before a change that matters, on a disposable copy when you can (a test dashboard, a copy of the automation with inert helpers):

1. Export the "before" (the automation, script, dashboard or helper as it is).
2. Apply the change; export the "after"; compare the two. Only what you meant to change should differ.
3. Roll back from the "before" export and compare again: it should match the original exactly.
4. Only then apply it for real, with the "before" export kept as the rollback.

Keep the export somewhere you can find it later (the kit's checks automation description is a good place to note where).
