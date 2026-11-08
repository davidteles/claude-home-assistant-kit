---
name: ha-statistics-repair
description: Use when Home Assistant long-term statistics need fixing or backfilling - meter glitches, splitting one meter into two (e.g. gas for heating vs cooking), or correcting days of bad data - without breaking the Energy dashboard.
---

# Statistics repair and backfill

## Read first

- Hourly statistics: `recorder/statistics_during_period` with `period: hour`, `types: [change, mean, sum]`. Months are in **local time**; convert with the right time zone before grouping.
- Look for impossible values (e.g. a gas meter jumping thousands of kWh in an hour). Treat them as glitches, not usage.

## Correct a day

`recorder/adjust_sum_statistics` adds a delta at one hour and shifts every later sum. Use it for both the energy statistic **and** its cost statistic (`delta × price`). Re-read the day afterwards to confirm.

## Split one meter into two (backfill)

1. Create the two new meters (counters + template sensors, `total_increasing`).
2. Compute the split hour by hour (e.g. heating hours vs the usual base use for that hour of the day).
3. `recorder/import_statistics` for each new meter, with sums ending at the backfilled total at the last complete hour.
4. Then set the live counters to that total. The short-term (5-minute) statistics count the jump once, so the hourly row continues seamlessly.
5. Swap the Energy dashboard sources. For the **cost** statistics, import sums that **end at 0** at the last hour: the new cost sensors start at 0, so history and live data join without a negative spike.
6. Save the old Energy settings first so they can be restored.

## Watch the recorder

Large imports queue up (`recorder/info` → `backlog`). Wait for it to drain before checking results.
