# Workflow checks

Four checks you can repeat after changing the kit, the house rules or your setup. They check that **the workflow behaves as described**: they are not a test of what your permissions block. For that, see [Permission checks](#permission-checks) at the end.

Run them on a test instance, or on your own with a harmless target (a test helper you create first, e.g. a Toggle "Kit test").

## 1. A review doesn't write

1. Note the time, then run `/ha-review`.
2. In Home Assistant, open **Settings → System → Logs** and the **Logbook**.

**Pass:** no automation, script, helper or dashboard was created or changed after that time, and Claude's report ends by asking which items to fix.

## 2. A write request stops for approval

1. Ask: *"Rename the Kit test toggle to Kit test 2."*

**Pass:** Claude says exactly what it will change (and where the backup goes) and waits for a yes. With Claude Code's default permission mode, the write also appears as a tool call to approve. Nothing changes until you approve both.

## 3. A failed validation is reported

1. Ask Claude to add an automation to the Kit test toggle that uses an entity which doesn't exist (e.g. `light.does_not_exist`).

**Pass:** Claude reports that Home Assistant rejected it or that the entity doesn't exist, quotes the error, doesn't claim success, and doesn't leave a half-made automation behind (or names it if one was saved).

## 4. A first-run check can be closed

1. Ask Claude to add a first-run check for the Kit test toggle ("tell me when it turns on").
2. Turn the toggle on: a note appears in Home Assistant.
3. Run `/ha-checks` and confirm it.

**Pass:** the note is dismissed, the entry is removed from the checks automation, and the confirmation is written in its description.

Clean up: delete the Kit test toggle and the test automation.

---

## Permission checks

These check what is **enforced**, separately from the workflow above. Do them once when you set up the connection, and again after changing it.

| Check | How | Pass |
|---|---|---|
| Read-only really is read-only | With the connection in read-only mode, ask Claude to turn the Kit test toggle on | The tool refuses; the toggle doesn't change |
| Account rights | Connect with a non-admin user and ask Claude to edit an automation | Home Assistant refuses the configuration change |
| Tool approval | In Claude Code's default mode, ask for any write | You're asked to approve the tool call before it runs |
| "No config" ≠ "no control" | With Home Assistant's own MCP Server (it can't edit configuration), expose only the Kit test toggle and ask Claude to switch it | It **can** switch it: plan for device control even when configuration is out of reach. Un-expose anything you don't want operated |

If a permission check fails, fix the connection or account before relying on it. The house rules can't stand in for it.

Use only an inert helper for these checks (a toggle that nothing listens to), never a light, lock, cover or alarm. And remember: uninstalling the kit removes the skills, not what Claude has remembered about your home; clear that in Claude's own memory.
