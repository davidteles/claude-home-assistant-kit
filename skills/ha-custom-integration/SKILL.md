---
name: ha-custom-integration
description: Use when a device has features Home Assistant doesn't expose and a small custom integration would add them - e.g. vendor-private HomeKit characteristics behind HomeKit Controller. How to write, install, test and package one safely.
---

# Small custom integrations

## When

A device works in Home Assistant but hides features (a vendor's private HomeKit service, extra modes, alarms). Look at the device's **diagnostics** first: they often list every characteristic with its type, permissions and current value.

## Design

- **Reuse the existing connection** (e.g. HomeKit Controller's `entry.runtime_data.pairing` → `get_characteristics` / `put_characteristics`). Never pair a second time.
- **Find things by UUID, not by fixed IDs.** iids differ between units.
- A `DataUpdateCoordinator` that polls (~30 s) and updates state **optimistically** after writes.
- Entities with `translation_key`; attach them to the existing device (Home Assistant gives each device one config entry, so move entities onto it rather than creating a twin).
- A one-click config flow that finds the device; `ConfigEntryNotReady` while the base integration is still connecting.
- **Learn the device's behaviour by testing**, then encode it (e.g. "switching the purifier off turns the unit off", so a mode select only switches the wanted job on).

## Install and test

- Write files into `config/custom_components/<domain>/` (File editor / Studio Code Server, or Samba). New integrations and code changes need a **restart**; run the configuration check first.
- Check the log for your domain, confirm entities read real values, and test each write once, then put things back as they were.

## Package for others

- `manifest.json` with `version`, `documentation`, `issue_tracker`, `codeowners`; `hacs.json`; translations; CI with **hassfest** + HACS validation; a README with requirements, setup, entities, behaviour notes, limitations and troubleshooting.
- No personal data in code, docs or screenshots.
