# English Web

**Practise SSC CGL English in the shape the exam actually asks it, and keep what you learn.**
Every question says why the right option is right and why each wrong option fails. The site then decides what to put in front of you next.

Live site: https://underwater001.github.io/english-web/

## How to use it

Open **Today**. It answers three questions, in this order:

1. **What is due?** Every question you have answered comes back on a schedule. Answer it right and it returns later — a day, three days, a week, a fortnight, five weeks. Answer it wrong and it goes back to the start and into the mistake book. A question you have got right three times running is counted **solid**.
2. **Where are you losing marks?** One row per question type, heaviest loss first. *At risk* is how many of the 50 marks that type costs you at your present accuracy, using how often the type appears in the papers on file. A type you have never tried counts as fully at risk — that is the point.
3. **Can you do it in time?** **Mock paper** draws 25 questions in the same proportions as the filed papers, gives you 13 minutes, and marks them +2 and −0.5 like the real thing. Nothing is revealed until you submit.

The rest: **Syllabus** for the rules and methods topic by topic, **Review** for the due queue, the mistake book and your weak spots, **Drill** for free practice with filters, **Word bank** for every word and idiom, **Daily** for editorial reading, **Sources** for what everything came from.

Your record lives in this browser only. *Today → Your record* holds a copy you can paste back after clearing site data or moving to another machine. Keep it somewhere.

## What is in it today

| | Now |
|---|---|
| Topics | 25, in three areas: Vocabulary, Grammar, Comprehension — all with questions |
| Questions | 1,647 (200 from past papers, 1,447 practice) |
| Word bank | 888 entries: words, idioms, one-word substitutions, phrasal verbs, spellings, confusable pairs |
| Past papers filed | 8 (3 SSC CGL Tier-I similar-paper shifts, 12 Sep 2025; 5 Exam-Day-Based memory papers, 07–10 & 12 Oct 2026) |
| Daily drops | none yet — send an editorial and the first one is built from it |

## The blueprint, and why the bank is shaped the way it is

Everything is measured against the papers on file. Eight papers' worth of English sections ask this mix, per 25-question paper (share of the 25 marks, averaged across all 8):

| Question type | Per paper | Question type | Per paper |
|---|---|---|---|
| Active/passive, direct/indirect | 4.75 | Spelling | 1.62 |
| Sentence / para jumble | 3.38 | Antonym | 1.38 |
| Cloze test | 2.75 | Sentence improvement | 1.12 |
| Spot the error | 2.12 | Synonym | 1.12 |
| Fill in the blank | 1.88 | One-word substitution | 0.75 |
| Reading comprehension | 1.88 | Homonym | 0.5 |
| Idiom / phrase / word meaning | 1.75 | | |

So grammar, sentence structure and comprehension still carry the larger half of the paper. The build enforces this: **a format the papers ask for must hold at least five papers' worth of practice questions, or `tools/check.py` fails** and names what is missing. That is what keeps the bank from drifting back into easy vocabulary drill, which is the smaller half of the paper.

Two topics — conditionals, nouns — have not appeared in any of the 8 papers filed so far. They are built and drilled anyway (as seed-tier practice, honestly marked as not past-question-backed yet), because the real paper varies and the blueprint only knows what it has been shown. Four more — gerund/infinitive, phrasal verbs, pronouns, question tags — have so far surfaced only once each; everything else has turned up repeatedly enough to be marked Medium or High likelihood.

Every grammar chapter of *Plinth to Paramount* (verbs, tense, passive voice, narration, question tags, subject-verb agreement, conditionals, gerund/infinitive, nouns, pronouns, adjectives, conjunctions, articles, prepositions, adverbs, and the confused-words chapter) has been read chapter by chapter — not just its table of contents — for rules the papers haven't surfaced yet, each one rewritten here in fresh wording with original examples. Grammar questions rest on a cited, named rule rather than a machine check; vocabulary and one-word-substitution questions are checked against the stored word bank. Reading comprehension still runs on five self-written passages, and the past-paper base is three shifts of one similar paper plus five Exam-Day-Based memory papers — still the next thing to widen as more real papers come in.

## Feeding it

Send any of these and it is filed, checked and published:

| You send | You get |
|---|---|
| An SSC CGL English paper (PDF or photos) | Every question playable, filed by topic and format, the blueprint and the mock mix updated, the paper's link on Sources |
| An editorial or newspaper page | A daily drop: capsule, passage in our own words, quiz |
| A rule sheet, word list or idiom list | Rules on the topic page and entries in the word bank |

Nothing goes live unless every check passes.

## Can you trust the answers?

Checked by the build, every time:
- every wrong option has its own specific note;
- synonym, antonym, idiom, one-word, phrasal-verb and spelling answers are matched against the stored word facts, so no wrong option can also be right;
- a reading-comprehension answer must quote a line that really appears in the passage;
- a past question must agree with its paper file on the key and the answer text;
- every daily word is in the capsule *and* tested;
- every format the papers ask for has enough practice behind it.

`tools/selftest.py` breaks each of those checks on purpose and requires the build to refuse: 19 cases.

**Not checked by a machine:** whether a grammar rule is applied correctly in a sentence. Those answers rest on the rule shown with the question. Each past question says where its key came from — the official SSC key, the key printed in the coaching paper you supplied ("source", not the official key), or one we worked out. Where a key can be argued (*barely* and *scarcely* both fit), the answer card carries a **Caution** saying so.

## For the repo owner

- How the data files, tiers, blueprint and checks work: [docs/BUILDING.md](docs/BUILDING.md)
- After any change, run `python3 tools/check.py --browser`, then commit and push to `main`. GitHub Pages serves the repo root.

## Rules of the project

- Nothing unverified goes in.
- No PDFs and no copied passages in this public repo. Papers and articles are stored as short restatements in our own words, with the paper and question number.
- Paper and source links show only on the Sources page.
