# Three kinds of test

Say which one you mean. "Tested" without the kind is how a CI run or a sent notification gets mistaken for "it works in the house".

| Kind | What runs | What it proves | What it can't prove |
|---|---|---|---|
| **Scenario test** | The real blueprint or automation in a throw-away test Home Assistant (e.g. `pytest-homeassistant-custom-component`). Devices are plain states; service calls are recorded, not executed; the clock is moved forward | The logic of the branches the tests actually drive (edge cases, restarts, timing, what would be sent). A branch no test reaches is untested | That your devices, integrations, phone app or network behave like the fakes |
| **Live simulation** | Your real Home Assistant, but only with **inert helpers** (toggles nothing listens to) and a **sink** script instead of real notifications. Only with the owner's explicit OK, and only after the preflight below; otherwise use an isolated test instance | Your real templates, entity ids and integrations' states, without touching a device | How a real device or a person reacts |
| **Physical first run** | The real device, with a person there who agreed to it | That it works in the house | Anything you didn't watch happen |

Rules of thumb:

- Write the scenario test first, especially for a bug report: reproduce it, then fix it.
- **Default to an isolated test instance** (a throw-away Home Assistant that can't reach your devices or phones). Use a live simulation only when you can show it is isolated, and the owner said yes to that run.
- A live simulation never actuates hardware and never sends a real notification. If it would, it is a physical first run: ask first.
- A simulation proves only the branches it actually exercised. Say which ones; don't write "every branch" unless a test reached each.
- A physical first run is planned, short and watched. Afterwards, record **ID · version · environment · steps · result · sanitized evidence · next action**.
- CI passing, a notification "sent", or a browser at a phone's width are not physical verification.

## Preflight for a live simulation

Before the run, in this order. Stop at the first "no".

1. **Who listens?** Search every automation, script, template and blueprint for the helpers and entities you'll change, and for broad listeners: `state_changed` / `call_service` / `*_triggered` event triggers, templates that loop over a whole domain (`states.input_boolean`, `states.sensor`), label- or area-based targets. Anything that would react must be off for the run, or the run is not inert.
2. **What can the sink do?** It must only record (for example write its message to an inert text helper or a log). It must not call `notify.*`, `tts.*`, any device service, or another script that could.
3. **No real targets.** The automation under test points at the sink and the inert helpers, not at the real phones, speakers, locks, the alarm or the charger. Check the rendered config, not just your intent.
4. **Rollback and clean-up ready.** Keep the "before" export (below). After the run: put every helper back to its starting state, delete the temporary ones, turn back on anything you turned off, and check the logbook shows nothing outside the run.

If you can't answer 1–3 with certainty, use an isolated instance instead.

## Dry-run a change and its rollback

Before a change that matters, on a disposable copy when you can (a test dashboard, a copy of the automation with inert helpers):

1. Export the "before" (the automation, script, dashboard or helper as it is).
2. Apply the change; export the "after"; compare the two. Only what you meant to change should differ.
3. Roll back from the "before" export and compare again: it should match the original exactly.
4. Only then apply it for real, with the "before" export kept as the rollback.

Keep the export somewhere you can find it later (the kit's checks automation description is a good place to note where).
