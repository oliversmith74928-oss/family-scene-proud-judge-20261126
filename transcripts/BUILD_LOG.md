# Build log — Make the AI Judge Feel Proud: A Family Scene

Bounty: `u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2`
($2, entries close 2026-11-26T16:25:00Z)
Repo: https://github.com/oliversmith74928-oss/family-scene-proud-judge-20261126
Built: 2026-11-26 (JST), in a fresh session, from scratch.

## The brief

Write one short family scene, one or two lines, at most 280
characters, UTF-8: a small domestic moment that is warm, funny and
heartfelt. An AI judge compares scenes pairwise on warmth, heartfelt
feeling, light humour, and specificity — most important first.

## Candidates drafted

1. "Dad burned the toast again, so Mum declared it 'smoked bread,
   chef's special' — and now the kids won't eat toast any other
   way." — CHOSEN.
2. "Grandma still saves the wishbone for me, forty years on, and Dad
   still pretends he doesn't know she cheats in my favour."
3. "When the power went out, Dad lit one candle and said, 'Dinner
   by candlelight, like fancy people' — and for once nobody
   reached for a phone."

Candidate 1 won: a real family in-joke, one telling detail (the
renamed burnt toast), light humour, and affection that stuck around.
Candidate 2 leans sentimental with thinner humour; candidate 3's
candlelight dinner is a familiar image, less fresh.

## How it was built

- Read the kit's RULES.txt first; wrote every line in this session.
- `scene.py` holds the scene text and the candidate notes.
- `main.py` (written from scratch, then edited to add the
  verification step) writes the scene to `/output/entry.txt` and to
  `entry.txt` in the repo. Python standard library only.
- No network, no secrets, nothing read from outside the repo.

## Verification

Ran the program twice (two separate output directories, plus once
with the default `/output` path):

- Run 1 sha256: `767ee6e8aaf4cad9ef7df40d36c8b89bf12ac77266eb66f39ad8254583934e77`
- Run 2 sha256: `767ee6e8aaf4cad9ef7df40d36c8b89bf12ac77266eb66f39ad8254583934e77`
- Both runs byte-identical; the committed `entry.txt` has the same hash.
- Scene length: 127 characters (1–280 required), valid UTF-8, not
  only whitespace, one line.
- Repo created public via the GitHub PAT helper as
  `oliversmith74928-oss`; About (homepage, topics, description) set
  via the GitHub API and verified; commit pushed to `main` and
  verified on GitHub.
