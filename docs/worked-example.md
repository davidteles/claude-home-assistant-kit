# Worked example: from review to rollback

A condensed, anonymised version of a real session. Names, entity IDs and times are made up; the steps are what happened. The margin notes say what stops each step: **[permission]** something the tools enforce, **[approval]** a person deciding, **[undo]** how to reverse it.

---

## 1. Review: nothing changes

> **Operator:** `/ha-review`

Claude reads automations, recent traces, entity states and repairs. It doesn't write anything.

> **Claude:** Ranked by impact on the household:
>
> 1. **Safety: nobody would be told if the alarm went off.** *Alarm - warn everyone when it goes off* runs, but both of its phone notifications are disabled (greyed out). The last trace shows it triggered on 2 Nov and sent nothing.
> 2. The storage-room door sensor has been offline for 3 days, so the alarm can't arm "away" with it.
> 3. Four automations have no category.
>
> Nothing has been changed. Which do you want me to fix?

- **[permission]** With a read-only connection to Home Assistant (see [Trust and permissions](../README.md#trust-and-permissions)), this step *can't* write, whatever the instructions say.
- **[approval]** Nothing moves until the operator picks.

## 2. Proposal: small and specific

> **Operator:** Fix 1.
>
> **Claude:** Plan for *Alarm - warn everyone when it goes off*:
> - Save the current automation to `rollback/alarm_warn_before_2026-11-04.json`.
> - Re-enable both phone notifications, as **critical** alerts (they ring on silent), naming the sensor that set it off.
> - Add `continue_on_error`, so one phone failing doesn't stop the other.
> - Send **one** test alert to both phones while you're here to hear it.
>
> OK?

- **[approval]** The plan names the exact automation, the backup file and the one test that will make noise.

## 3. Change: backup first, then the write

> **Operator:** Yes, go.

Claude saves the backup, then writes the automation. In Claude Code's default permission mode, the write shows up as a tool call the operator approves or denies.

- **[permission]** The write needs a Home Assistant account allowed to edit automations (an admin), and Claude Code asks before the tool call unless the operator has allow-listed it.
- **[undo]** The backup exists before anything changes.

## 4. Validation: real outcomes, reported honestly

> **Claude:** Saved. Configuration check: valid. I triggered the notification step on its own: the test alert rang on both phones at 18:08 (you confirmed). Not tested: a real alarm trigger. That's what the first-run check is for.

If validation had failed (an invalid config, a phone not ringing), Claude would say so with the error, leave the backup in place and not move on.

## 5. First-run check: the household confirms

Claude adds the feature to the **first-run checks** automation (see the `ha-first-run-checks` skill). The first time the alarm really goes off, Home Assistant posts a note: *"Just ran for real. Did both phones ring, and did it name the right sensor?"*

Three weeks later the alarm goes off (a door left ajar):

> **Operator:** `/ha-checks`. The alarm alert worked, both phones, said "Front door".
>
> **Claude:** Removed it from the checks and noted the confirmation in the automation's description.

## 6. Rollback, if it had gone wrong

Say the critical alerts turn out to be too loud at night:

> **Operator:** Put it back as it was.
>
> **Claude:** Restoring `rollback/alarm_warn_before_2026-11-04.json` over the automation, then checking the configuration and reading it back to confirm it matches the backup.

- **[undo]** One file, one write, verified by reading it back. The same pattern works for scripts, dashboards and helpers.

---

## What blocked what

| Step | Enforced by the tools | Needs a person | Reversible |
|---|---|---|---|
| Review | Read-only connection (if you set one up) | Choosing what to fix | Nothing to undo |
| Proposal | – | Approving the plan | – |
| Backup + write | HA account rights; Claude Code's tool approval | Approving the tool call | Yes: the backup |
| Test alert | HA account rights | Being there to hear it | Nothing to undo |
| First-run check | – | Confirming in real life | Remove the entry |
| Rollback | HA account rights | Asking for it | Yes: re-apply the change |

The house rules in this kit shape *how* Claude works. They are instructions, not a lock: the left column is what actually stops a write.
