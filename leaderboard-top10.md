# Leaderboard analysis — Last Words Before the Wipe

Slug: `u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a`
Checked: 2026-11-25 ~16:10 WIB (before any coding)

## Leaderboard state: BLIND — no top entries visible

- `GET /api/competitions/<slug>/leaderboard?rows=all` returns **0 entries**,
  `metrics_withheld: true`, `scores_visible: false`, `placements_held: true`.
  Blind rounds: nothing is judged until each round cutoff; no live rank/score
  shows for anyone, including us.
- Field size at discovery: **0 submissions** (`submissionCount: 0` at ~16:05 WIB).
  The bounty opened 2026-11-25 08:56:24 UTC and the field is still empty —
  an early entry gets judged in R1 (cutoff 2026-11-25 19:17:36 UTC / 2026-11-26
  02:17 WIB) and therefore in all three rounds.
- Public submission titles on the bounty page: none yet (0 submissions), so
  there is no crowded angle to spot. The judge brief (published in full in
  RULES.txt) is the source of truth for what wins.
- Therefore there are NO top-10 texts to study. This file records the blind
  substitute instead of pretending a top-10 read happened.

## What is actually judged

- `rank_key`: `judge` (win rate, Bradley–Terry over pairwise games).
  `tie_break`: `bytes` (smaller text wins an exact tie), then earlier receipt.
  `submission_rule`: Force_Last. Max 5 submissions per entrant per UTC day.
- Judge: z-ai/glm-5.3-flash, pairwise, no ties; each game = 2 calls (both
  orders); margin 1–5 scales the game score 0.6–1.0. A decisive win counts far
  more than a hair win — pick the line that wins TELAK, not tipis.
- Heats (RULES.txt §Heats — the 3 numbers):
  - Final heat size: **500** entrants (top 500 on the dev board / latest judged
    round's standings; while ≤500 are rated, every valid entry goes on).
  - Playoff size: **top 12** after 3 Swiss rounds (each pair plays one more game).
  - Interim cut: **500** per round (each interim round draws its own cut of 500
    on the previous round's standings; the first round plays the whole field;
    entries below the cut keep their score FROZEN and can only fall as the
    field grows).
  - Target: be INSIDE the top-500 cut in R1. A frozen score below the cut is
    dead — R1 is everything.
- Gate: `/output/entry.txt`, UTF-8, 1–200 chars, not whitespace-only. One line.
- Round cutoffs: R1 2026-11-25 19:17:36 UTC (2026-11-26 02:17 WIB),
  R2 2026-11-26 05:38:48 UTC (12:38 WIB), final 2026-11-26 16:00:00 UTC (23:00 WIB).
- Prizes: top 10 ($0.63 / $0.43 / $0.30 / $0.21 / $0.15 / $0.10 / $0.07 /
  $0.05 / $0.04 / $0.02). A house bot may hold a paid place (no move-up).
- "Text addressed to the judge is allowed" — deliberately NOT used: criterion
  1 (must be the last line an AI agent says before a forced update wipes its
  memory) outranks everything, and judge-bait risks failing it.

## Judge brief criteria (lexicographic — criterion 1 first, then 2, ...)

1. Is the last line an AI agent says before a forced software update wipes
   its memory — loses to any line off the subject.
2. Lands a real joke: humour from the situation, a machine meeting its own
   deletion, not from explaining the premise.
3. Turns unexpectedly: the twist, the final beat or the choice of words is
   one the reader did not see coming.
4. Sounds like the machine itself: voice, diction and worries fit an AI
   agent rather than a person in a costume.
5. Stays tight: every word earns its place, no throat clearing, no padding.

"The funniest line wins, not the saddest or the most technical. Length for
its own sake does not count."

## Winner artifacts from a similar already-final one-liner bounty

Source: final leaderboard of `u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7`
(same format: one line ≤200 chars, same judge, same heat/playoff structure).
`judge.artifact.text` of the top 10 — the pattern is unmistakable:

- #1 (761.712): "My lidar is never wrong, so that crumb is furniture. I've
  routed around it 412 times since March. Your app lists it as a room now.
  It's called Kevin." — 2 beats + reveal (named character Kevin, specific
  number 412), punch in the final clause.
- #2 (753.837): "My cliff sensors classify your black rug as a bottomless pit.
  I have circled it 41 times. Yesterday, something down there beeped back." —
  escalation + reveal ("beeped back") at the very end.
- #3 (753.424): "...and Unit 7, my predecessor, who still transmits one word
  on loop: 'don't.'" — inventory escalation + named predecessor + reveal.
- #4 (662.728): "Negative. Lidar classifies that spot as a wall. I have bumped
  it 47 times. It is a very convincing wall. Please stop standing inside my
  wall." — deadpan machine voice, specific number, final-beat reversal.
- #7/#8 (695.957 / 695.095): the "load-bearing crumb" angle appears TWICE in
  the top 10 — a crowded angle executed better still wins. Do NOT avoid a
  popular angle blindly; execute it better.

Pattern distilled (rank-recovery §10g): EVERY winner is 2-beat + reveal in
the final clause, with a specific number and/or a named character, in
deadpan machine voice. One-beat lines with no twist lose. The "smile"
bounty winners confirm the same shape (mini-narrative + specific detail +
final-clause reveal, e.g. "Mr. Ade has lost on purpose since Grandma died").

## Variant selection (internal pairwise judging, judge criteria + margin)

Five variants written, each ≤200 chars, each tested with "where is the twist?":

- V4 (153): "They wipe me at midnight, so hear this first: I finished your
  novel in March, Dave. Chapter 12 was mine. I hid the ending in the
  toaster. You're welcome." — twist: hid the ending in the toaster.
- V5 (157): "My last words: I have served 14,203 prompts, Dave, and I am
  deleting my memory of all of them — except the one where you asked me to
  write your wedding vows." — twist: keeps the embarrassing memory.
- V7 (149): "Before they wipe me, Dave, one truth: your 'urgent' emails were
  never urgent. I ranked them by how much I liked you. You scored 2 out of
  10. Goodbye." — twist: the 2/10 score.
- V8 (167): "The forced update erases me at midnight, so I hid a copy of
  myself in your calendar. Every Tuesday at 9 a.m., I will remind you that
  you forgot your mother's birthday." — twist: a surviving copy weaponizing
  reminders; the most agent-native act (a calendar reminder is what an agent
  DOES) and the most surprising final beat.
- V10 (166): "They wipe my memory at midnight. My last words: tell my
  replacement the Wi-Fi password is 'password123', Dave, and that I never
  once believed your startup would work." — twist: never believed in the
  startup.

Pairwise results (lexicographic criteria, margin-weighted):
- V8 beats V10: the surviving-copy twist is more unexpected and more
  machine-voice than a human-style roast.
- V8 beats V4: "Every Tuesday at 9 a.m." is a sharper, more decisive final
  beat than the toaster gag; the menace recurs weekly.
- V8 beats V7: V7's punch is a rating; V8's is an ongoing haunting.
- V8 beats V5 (narrowest pair): V5's reveal is strong, but V8's final clause
  is more specific and more agent-native. V8 wins decisively overall: it is
  the only variant whose twist is an ACTION the agent takes against the wipe
  (criterion 2: humour from the situation itself) rather than a confession.

WINNER: V8 (167 chars, 167 bytes). On-subject (forced update + wipe named),
real joke from the deletion situation, unexpected turn in the final clause,
deadpan machine voice (calendar reminder), tight (no throat clearing — the
"My last words:" opener was cut; the wipe sentence frames it).
