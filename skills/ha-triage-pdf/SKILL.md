---
name: ha-triage-pdf
description: Use when there is a backlog of Home Assistant ideas, fixes or questions for the user to decide on. Produces a fillable PDF where each item gets Now / Later / Ignore and a free-text note, plus a log of what was already done - then reads the answers back.
---

# Triage PDF (Now / Later / Ignore)

Long chats bury decisions. A fillable PDF lets the user decide calmly, on any device, and gives you structured answers back.

## Build it

- Use reportlab's AcroForm fields: per item, a **radio group** `Now / Later / Ignore` and a **multiline text field** for notes (give it real height, ~80 pt).
- Each item: a short title, one or two lines of *why* and *what it would change*, and the effort.
- Put **pending items first**, then a **done log** (newest batch on top, dated) so the user sees progress.
- Add a final free-text "anything else" page.
- **No selection means Later.** Say so at the top.
- Name files with date and version (`… (2026-11-08 v5).pdf`) and save where the user can find them.

## Read it back

- Use `pypdf`'s `get_fields()` to read every radio and text value.
- Act on **Now** items, park **Later**, drop **Ignore**, and remember ignored ideas so you never re-suggest them.
- Quote the user's notes back when you act on them, so nothing is misread.

## Tips

- Keep each item self-contained. The user may read it days later.
- Preview a page as an image (pypdfium2 with forms initialised) before sending, to check the fields are where you think.
