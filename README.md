# English Web: SSC CGL English question bank

A question bank and daily reader for the SSC CGL English section: vocabulary, grammar and comprehension. Every question is playable, every answer is explained, and every wrong option says why it fails.

It is built the same way as **Maths Web** (topic bank, papers filed one file at a time, a gap gate so nothing filed is unplayable) and **Current Affairs Web** (one daily drop per newspaper, a capsule, a quiz built from it).

## Using the site

| Place | What it is |
|---|---|
| **Syllabus** (home) | Every topic grouped under Vocabulary, Grammar and Comprehension. Each card shows past and practice counts, the tier, its question types and your progress. |
| **Topic page** | Study the rules first (each with a right and a wrong example), then the question types (how to spot it, the fast way, the traps), then the questions easiest first, filterable by type, level and progress. |
| **Daily** | One drop per editorial or article: a capsule of the words and ideas, a short passage in our own words, and a quiz that tests every word. |
| **Word bank** | Every word, idiom, one-word substitution and phrasal verb, searchable, with a "I know this" tick. |
| **Mixed practice** | Every question from every topic, filtered by topic, format, level, source and progress. |
| **Sources** | Every paper and daily source with its link. Links live only here. |

## What is in it now

A seed: 4 topics (synonyms & antonyms, idioms & phrases, one-word substitution, subject-verb agreement), 26 original practice questions and 22 lexicon entries. **No past paper is filed yet.** The other 15 topics appear dimmed until material arrives.

## How a question is checked

English has no arithmetic to recompute, so the checks are different. The build refuses a question unless all of these hold:

- Four distinct options, one key, and a real note for **each** wrong option (no generic "does not match").
- The answer is grounded: it cites a **rule** defined in the topic, a **lexicon fact**, or an **evidence line** that is actually in the passage.
- **Vocabulary answers are checked against the lexicon.** A synonym question's key must be in the word's synonym list and no wrong option may be; the same for antonyms; an idiom's key must be its stored meaning; a one-word substitution must contain the phrase and key the word.
- **Shape by format**: a fill-in has a blank; a spot-the-error question's options are parts of the sentence; a sentence improvement marks its part as `[[...]]`.
- **Past questions** must agree with the paper file on topic, format, key **and** the answer text, so a transcription slip in either place fails the build.
- Optional per-question `check=` function for any mechanical test you can write (subject-verb items use one: exactly one option has the number the rule demands).
- `python3 tools/selftest.py` breaks each check on purpose in a temp copy and requires the build to refuse.

**What is not machine-checked:** whether a grammar rule is applied correctly in a sentence. That rests on the rule cited, which is stated on the topic page. Keys for past questions that were worked out by us and not copied from an official key are marked `keySource: "derived"`, shown on the question and counted on the Sources page.

## Adding material

Send anything: a question paper (PDF, photos, or a PDF open in Chrome), an editorial or newspaper page, a rule sheet, a word list.

**A question paper** is filed the Maths Web way:
1. `data/papers/<id>.json`: details (`exam`, `kind` = official | memory | similar-paper | chapter-bank, `publisher`, `date`, `shift`, `link`, `section`) and one row per English question: `qno`, `topic` (a topic in `data/tree.json`), `fmt` (a key of `FORMATS` in `tools/bank.py`), `key`, `answer` (the keyed option's text), `keySource` (`official` or `derived`).
2. In `tools/topics/<topic>.py` add each as `q(..., paper=..., qno=...)`. The build fails with "N filed question(s) ... have no quiz yet" until you do. Set `TIER = "quiz"`.
3. Passages are stored as a condensed restatement, never the paper's own text or the PDF.

**A daily drop** is one file, `data/days/<YYYY-MM-DD>.json`:
- `paper`: `publication`, `edition`, `pages`, `link`, `title`.
- `words`: lexicon entries (`id`, `w`, `kind`, `meaning`, `syn`, `ant`, `ex`, `pos`). Ids already in the lexicon are reused, not added again.
- `capsule`: points of at most 260 characters with `**bold**` testable terms, each citing the word ids it carries, with optional `more` lines behind a tap.
- `quiz`: questions (`id` `q<YYYYMMDD>-NNN`, `fmt`, `text`, `options`, `key`, `why`, `wrong`, `lex: [kind, word_id]`).
- `passage` (optional): `title`, `text` written **in our own words**, at most 400 words, and `questions` that each carry an `evidence` line which must appear in the passage.
- Gap gate: every word must be in a capsule point **and** tested by a quiz question.

**A rule sheet or word list** becomes rules in a topic module (each with a right and a wrong example) and entries in `WORDS`.

Then run `python3 tools/check.py --browser`, commit and push to `main`. GitHub Pages serves the repo root.

### Tiers

| | `seed` | `quiz` | `full` |
|---|---|---|---|
| Past questions | none yet | at least one | at least one |
| Method per type (cue, standard, fast, eliminate, traps) | yes | yes | yes |
| Practice per type | at least 2 | optional | at least 3, one Medium or Hard |

Start a topic as `seed` or `quiz`, upgrade to `full` when time allows.

## How difficulty and likelihood are worked out

| Input | Points |
|---|---|
| Rules (or word senses) the answer depends on | 1 = 1, 2 = 2, 3 or more = 3 |
| A wrong option is the result of a named common mistake | +1 |
| A hard or rarely seen word is the point | +1 |

Up to 2 Easy, 3 Medium, 4 or more Hard. **Likelihood** is the share of analysed papers that contained the topic: High at 2/3 or more, Medium at 1/3 or more, Low below. Always read it with the number of papers, and remember official, memory-based and coaching papers differ.

## How it is built

```
data/tree.json            junctions and topics                         hand-kept
data/papers/<id>.json     one file per paper                           source of truth
data/days/<date>.json     one file per daily drop                      source of truth
tools/topics/<topic>.py   one module per topic: rules, methods, words, questions
data/shards/<topic>.json  built per topic                              generated
data/core.json            small: nodes, papers, days, stats            generated
data/lexicon.json         every word, idiom, substitution              generated
index.html                the whole front end
```

The page loads `core.json` first and fetches a topic's shard only when it is opened. Each shard records a hash of its sources and `tools/build.py` refuses to assemble from a stale one.

## Rules

- Nothing unverified goes in. Practice questions are written fresh; outside material is kept as links with notes in the topic's `REFS`, never copied text.
- No PDFs in this public repo. Passages, idioms lists and questions are condensed restatements in our own words, with paper and question number.
- Paper and source links show only on the Sources page.

## Commands

```
python3 tools/check.py                # rebuild stale topics, assemble core.json and lexicon.json
python3 tools/check.py --browser      # plus the browser test (Playwright + Chromium)
python3 tools/check.py --selftest     # plus proof that every check can fail
python3 tools/build_topic.py idioms-phrases --force
python3 tools/make_artifact.py OUT.html   # one self-contained page with all data inlined
```
