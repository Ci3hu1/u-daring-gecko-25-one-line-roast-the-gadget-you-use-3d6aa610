# STRATEGY — One-Line Roast: The Gadget You Use Every Day

## The line

> My phone charger works at exactly one angle — the angle of prayer — and even God can't make it fast-charge.

107 characters. One line. The submission title is the line itself.

## What the line does

The brief's own examples (phone dies at four, app asks for a rating,
kettle wants a firmware update) are the reheated complaints the judge
is told to mark down — so the line roasts a daily gadget from a fresh
angle instead:

1. **A specific gripe, not a generic one (criterion 5).** Not "my
   charger is slow" but "works at exactly one angle" — a concrete
   behaviour anyone with a dying cable recognises instantly: the cable
   you have to hold, prop, and beg.
2. **The turn is the image (criterion 3).** "The angle of prayer" makes
   charging a religious act. It is a comparison the judge has not seen
   before, and it arrives mid-line, so the joke re-reads the setup.
3. **The payoff escalates (criterion 2).** Even God — called in as the
   last resort — cannot make it fast-charge. The complaint goes from
   the human begging the cable to God failing at the same cable.
4. **Neatly worded (criterion 4).** One sentence, 107 of 200 characters,
   no wasted words: setup ("exactly one angle"), turn ("angle of
   prayer"), payoff ("even God can't make it fast-charge").

## Alternatives considered and dropped

- "My laptop fan screams like a jet engine every time I open a second
  Chrome tab." Concrete and funny, but the Chrome-tabs joke is
  well-worn — it risks reading as the obvious complaint.
- "My phone's face unlock knows me everywhere except at 2am, when I
  actually need it." Personal to Joni's 2am bounty habit, but "face
  unlock fails in the dark" is a known gripe; the twist carries it, the
  image does not.
- The brief's own examples (phone dies at four, rating prompt, kettle
  firmware) — explicitly avoided; the judge is briefed to prefer fresh
  angles over them.

## Judging

Blind rounds (3): round 1 cutoff 24 Nov 2026 18:00 UTC (25 Nov 01:00
WIB), round 2 on 25 Nov 16:30 UTC, final at the deadline 26 Nov 15:00
UTC (22:00 WIB). No live score until rounds are judged — check
`GET /api/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/rounds`
after round 1. The gate is mechanical: /output/entry.txt must be UTF-8
text of 1–200 characters, not only whitespace. The line is 107
characters.

## Program

`main.py`, pure Python standard library, writes the line to
`/output/entry.txt`. Deterministic (identical bytes on repeat runs),
no network, no clock, no randomness. Output file chmod 0644 so the
collector can read it.
