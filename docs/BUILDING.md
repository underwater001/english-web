# Building and extending English Web

For whoever maintains the repo. The site itself is explained in the [README](../README.md).

## Commands

```
python3 tools/check.py                # rebuild stale topics, assemble core.json and lexicon.json
python3 tools/check.py --browser      # plus the browser test (Playwright + Chromium)
python3 tools/check.py --selftest     # plus proof that every check can fail
python3 tools/build_topic.py idioms-phrases --force
python3 tools/make_artifact.py OUT.html   # one self-contained page with all data inlined
```

## Layout

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

The page loads `core.json` first and fetches a topic's shard only when it is opened. Each shard records a hash of its sources, and `tools/build.py` refuses to assemble from a stale one. A new paper is one file, a new day is one file, a new topic is one `tree.json` entry plus one module.

## Adding a past paper

1. **File it.** `data/papers/<id>.json` with `exam`, `kind` (official | memory | similar-paper | chapter-bank), `publisher`, `date`, `shift`, `link`, `section`, and one row per question: `qno`, `topic`, `fmt`, `key`, `answer` (the keyed option's text), `keySource` (`official` or `derived`). `fmt` is a key of `FORMATS` in `tools/bank.py`. A grammar question is filed under the rule it tests.
2. **Give every question a page.** In `tools/topics/<topic>.py` add `q(..., paper="<id>", qno=<n>)`. The build fails with "N filed question(s) ... have no quiz yet" until you do. Set `TIER = "quiz"`.
3. Store passages and questions as condensed restatements. Never store the PDF.

## Adding a daily drop

One file, `data/days/<YYYY-MM-DD>.json`:

| Field | Content |
|---|---|
| `paper` | `publication`, `edition`, `pages`, `link`, `title` |
| `words` | lexicon entries: `id`, `w`, `kind`, `meaning`, `syn`, `ant`, `ex`, `pos`. Reuse ids already in the lexicon. |
| `capsule` | points of at most 260 characters with `**bold**` terms, each citing word ids, optional `more` behind a tap |
| `quiz` | questions: `id` as `q<YYYYMMDD>-NNN`, `fmt`, `text`, `options`, `key`, `why`, `wrong`, `lex: [kind, word_id]` |
| `passage` | optional: `title`, `text` in our own words (at most 400 words), `questions` that each carry an `evidence` line found in the passage |

Gap gate: every word must be in a capsule point **and** tested by a quiz question.

## Adding a topic

Add the topic to `data/tree.json`, copy `tools/topics/_template.py` to `tools/topics/<topic_with_underscores>.py`, fill it in, run `python3 tools/check.py`.

## Tiers

| | `seed` | `quiz` | `full` |
|---|---|---|---|
| Past questions | none yet | at least one | at least one |
| Method per type (cue, standard, fast, eliminate, traps) | yes | yes | yes |
| Practice per type | at least 2 | optional | at least 3, one Medium or Hard |

Start a topic as `seed` or `quiz`, upgrade to `full` when time allows.

## What the build checks

A question is refused unless all of these hold:

- Four distinct options, one key, and a specific note for each wrong option.
- It is grounded: it cites a **rule** defined in the topic, a **lexicon fact**, or an **evidence line** that is in the passage.
- **Vocabulary is checked against the lexicon.** A synonym key must be in the word's synonym list and no wrong option may be; the same for antonyms; an idiom's key must be its stored meaning; a one-word substitution must contain the phrase and key the word.
- **Shape by format:** a fill-in has a blank, a spot-the-error question's options are parts of the sentence, a sentence improvement marks its part as `[[...]]`.
- **Past questions** agree with the paper file on topic, format, key and answer text.
- An optional `check=` function on a question for any mechanical test you can write. Subject-verb items use one: exactly one option has the number the rule demands.
- `python3 tools/selftest.py` breaks each check on purpose in a temp copy and requires the build to refuse.

Not machine-checked: whether a grammar rule is applied correctly in a sentence.

## Difficulty and likelihood

| Input | Points |
|---|---|
| Rules (or word senses) the answer depends on | 1 = 1, 2 = 2, 3 or more = 3 |
| A wrong option is the result of a named common mistake | +1 |
| A hard or rarely seen word is the point | +1 |

Up to 2 Easy, 3 Medium, 4 or more Hard.

**Likelihood** is the share of analysed papers that contained the topic: High at 2/3 or more, Medium at 1/3 or more, Low below. Read it with the number of papers, and remember official, memory-based and coaching papers differ.
