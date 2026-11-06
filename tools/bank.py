"""Shared library for English Web: rubrics, vocabularies, question constructors and the checks every question must pass.

A topic lives in tools/topics/<name>.py and is built with `python3 tools/build_topic.py <name>`.
A daily drop is data/days/<date>.json and is validated by tools/build.py with the same checks.
See README.md for the module interface.
"""
import re

LETTERS = "abcd"
LEVELS = ["Easy", "Medium", "Hard"]

# What the question asks you to do. A grammar question is filed under the RULE it tests (its topic) and carries its FORMAT here.
FORMATS = {
    "fill": "Fill in the blank",
    "spot-error": "Spot the error",
    "improve": "Sentence improvement",
    "transform": "Active/passive, direct/indirect",
    "synonym": "Synonym",
    "antonym": "Antonym",
    "meaning": "Meaning of idiom / phrase / word",
    "ows": "One-word substitution",
    "spelling": "Correct / incorrect spelling",
    "cloze": "Cloze test",
    "rearrange": "Sentence / para jumble",
    "rc": "Reading comprehension",
    "homonym": "Homonym in a sentence",
}

# Quick-solving ideas a question can be filtered by
TECHNIQUES = {
    "read-whole": "Read the whole sentence first",
    "subject-first": "Find the true subject",
    "tone": "Match the tone (positive / negative)",
    "context-clue": "Use the context clue",
    "root-prefix": "Use root, prefix and suffix",
    "back-substitute": "Put each option back in",
    "eliminate-pair": "Drop options that clash",
    "opposite-trap": "Expect the opposite as a trap",
    "first-sentence": "Find the opening sentence",
    "connectors": "Follow the connectors",
    "pair-up": "Pair the sentences",
    "scan-evidence": "Scan for the evidence line",
    "literal-trap": "Do not take the idiom literally",
}

# Word kinds in the lexicon
KINDS = {"word": "Word", "idiom": "Idiom / phrase", "ows": "One-word substitution", "phrasal": "Phrasal verb", "spelling": "Spelling",
         "confused": "Often confused"}

# lex=(kind, word_id) checks a question against the lexicon:
#   syn / ant   the key is in the word's synonym / antonym list and no wrong option is
#   meaning     the key is the stored meaning (or an accepted paraphrase) of the idiom or word
#   ows         the question holds the stored phrase and the key is the stored word
#   fits        the blank is filled by the stored word and no wrong option is that word
#   spell       choose the right spelling: key is the stored spelling, every wrong option is a declared misspelling
#   misspelt    choose the misspelt word: key is a declared misspelling, every other option is a stored correct spelling
LEX_KINDS = ("syn", "ant", "meaning", "ows", "fits", "spell", "misspelt")


# ----------------------------------------------------------------------------------------------
# Difficulty rubric (applied the same way to every question)
#   rules  = distinct rules (or word senses) the answer depends on   1 -> 1 point, 2 -> 2, 3+ -> 3
#   trap   = at least one wrong option is the result of a named common mistake            +1
#   rare   = a hard or rarely-seen word is the point of the question                      +1
#   score <= 2 Easy, 3 Medium, >= 4 Hard
# ----------------------------------------------------------------------------------------------
def score(n_rules, trap, rare):
    n = max(n_rules, 1)
    return (1 if n == 1 else 2 if n == 2 else 3) + (1 if trap else 0) + (1 if rare else 0)


def level(sc):
    return "Easy" if sc <= 2 else "Medium" if sc == 3 else "Hard"


def likelihood(shifts, total):
    """Share of the analysed papers in which a topic or format appeared."""
    if total <= 0 or shifts <= 0:
        return "not seen"
    r = shifts / total
    return "high" if r >= 2 / 3 else "medium" if r >= 1 / 3 else "low"


def norm(s):
    """Loose comparison form for option text: lower case, no trailing full stop, one space between words."""
    s = str(s).replace("\u201c", '"').replace("\u201d", '"').replace("\u2018", "'").replace("\u2019", "'")   # curly and straight quotes compare equal
    return re.sub(r"\s+", " ", s.strip().lower().rstrip(". "))


# ----------------------------------------------------------------------------------------------
# Wrong-option notes. Every wrong option carries a note that says WHY it fails.
#   mistake(note)    the option is what a named common mistake produces (counts as a trap for difficulty)
#   ruled_out(note)  the option simply does not fit; the note says why
# ----------------------------------------------------------------------------------------------
def mistake(note):
    return {"kind": "mistake", "note": note}


def ruled_out(note):
    return {"kind": "ruled-out", "note": note}


# ----------------------------------------------------------------------------------------------
# Lexicon entry: a word, idiom, one-word substitution or phrasal verb with its checked facts.
#   word    w is the word; meaning one plain sentence; syn / ant lists of single words or short phrases
#   idiom   w is the idiom; meaning is what it means; `also` lists other accepted paraphrases
#   ows     w is the single word; meaning is the phrase it replaces
#   phrasal w is the phrasal verb; meaning is what it means
#   ex      your own example sentence, which must contain the word
# ----------------------------------------------------------------------------------------------
def word(wid, w, kind, meaning, *, syn=(), ant=(), ex="", pos="", also=(), note="", misspell=()):
    return {"id": wid, "w": w, "kind": kind, "pos": pos, "meaning": meaning, "syn": list(syn), "ant": list(ant),
            "ex": ex, "also": list(also), "note": note, "misspell": list(misspell)}


def check_word(e, where):
    errs = []
    for k in ("id", "w", "kind", "meaning", "ex"):
        if not e.get(k): errs.append(f"{where}: word is missing '{k}'")
    if errs: return errs
    if e["kind"] not in KINDS: errs.append(f"{where}: kind {e['kind']!r} must be one of {list(KINDS)}")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", e["id"]): errs.append(f"{where}: id {e['id']!r} must be lowercase letters, digits and hyphens")
    if e["kind"] == "word" and len(e.get("syn", [])) < 2: errs.append(f"{where}: a word needs at least 2 synonyms")
    stem = norm(e["w"])
    stem = stem[: max(4, len(stem) - 3)] if e["kind"] in ("word", "confused") else stem
    if e["kind"] == "spelling" and not e.get("misspell"): errs.append(f"{where}: a spelling entry needs at least one misspelling")
    if e["kind"] in ("word", "idiom", "ows", "spelling", "confused") and stem.split(" ")[0] not in norm(e["ex"]):
        errs.append(f"{where}: the example sentence must contain {e['w']!r}")
    for k in ("syn", "ant", "also", "misspell"):
        for x in e.get(k, []):
            if not isinstance(x, str) or not x.strip(): errs.append(f"{where}: blank entry in {k}")
    both = {norm(x) for x in e.get("syn", [])} & {norm(x) for x in e.get("ant", [])}
    if both: errs.append(f"{where}: {sorted(both)} is listed as both synonym and antonym")
    if norm(e["w"]) in {norm(x) for x in e.get("syn", []) + e.get("ant", [])}: errs.append(f"{where}: the word is listed as its own synonym or antonym")
    return errs


# ----------------------------------------------------------------------------------------------
# A question. Past questions (PYQ) and practice questions share one shape.
#   qtype   question-type node id in the topic module
#   fmt     one of FORMATS
#   options exactly four strings; key is the letter of the right one
#   why     the reason in one or two sentences, naming the rule or the meaning
#   wrong   {letter: mistake(...) | ruled_out(...) | "plain note"} for each non-key option
#   rules   rule ids from the module's RULES that the answer depends on (grammar)
#   lex     (kind, word_id): a mechanical check against the lexicon (see check_question)
#   rare    a hard word is the point (adds a difficulty point)
#   check   optional function(q) -> True for any extra mechanical check you can write
#   passage id of a passage in the module's PASSAGES (reading comprehension); evidence must be a line of that passage
#   caution a warning shown with the answer when the item is weak or the key can be argued (say why, in one or two sentences)
# ----------------------------------------------------------------------------------------------
def q(qtype, fmt, text, options, key, why, wrong, *, rules=(), lex=None, trick="", tech=(), rare=False,
      paper=None, qno=None, uid=None, evidence="", check=None, passage=None, caution=""):
    return {"id": f"{paper}-Q{qno}" if paper else uid, "paper": paper, "qno": qno, "qtype": qtype, "fmt": fmt, "text": text,
            "options": list(options), "key": key, "why": why, "wrong": wrong, "rules": list(rules),
            "lex": list(lex) if lex else None, "trick": trick, "tech": list(tech), "rare": rare,
            "evidence": evidence, "passage": passage, "caution": caution, "_check": check}


def wrong_notes(raw):
    """Normalise {letter: str | dict} to {letter: {"kind", "note"}}."""
    out = {}
    for k, v in (raw or {}).items():
        out[k] = ruled_out(v) if isinstance(v, str) else {"kind": v.get("kind", "ruled-out"), "note": v.get("note", "")}
    return out


def check_question(x, ctx, where):
    """Every mechanical check a question must pass. Returns a list of error strings.
    ctx: {"words": {id: entry}, "rules": set | None, "qtypes": set | None}"""
    errs = []
    need = ("id", "qtype", "fmt", "text", "options", "key", "why")
    for k in need:
        if not x.get(k): errs.append(f"{where}: missing '{k}'")
    if errs: return errs
    opts, key = x["options"], x["key"]
    if x["fmt"] not in FORMATS: errs.append(f"{where}: fmt {x['fmt']!r} is not one of {list(FORMATS)}")
    if ctx.get("qtypes") is not None and x["qtype"] not in ctx["qtypes"]: errs.append(f"{where}: question type {x['qtype']} is not defined")
    if len(opts) != 4 or any(not isinstance(o, str) or not o.strip() for o in opts): errs.append(f"{where}: needs exactly four non-blank options")
    elif len({norm(o) for o in opts}) != 4: errs.append(f"{where}: options are not four distinct choices")
    if key not in LETTERS: errs.append(f"{where}: key {key!r} must be a, b, c or d")
    if errs: return errs
    # wrong-option notes: one real note per wrong option, none shared
    w = wrong_notes(x.get("wrong"))
    expect = set(LETTERS) - {key}
    if set(w) != expect: errs.append(f"{where}: wrong-option notes must be exactly {sorted(expect)}, got {sorted(w)}")
    seen = set()
    for k, v in w.items():
        n = v["note"].strip()
        if len(n) < 15: errs.append(f"{where}: note for option {k} is too short to say why it fails")
        if re.search(r"does not match|is wrong|incorrect option", n, re.I) and len(n) < 40: errs.append(f"{where}: note for option {k} is generic; name the rule or the mistake")
        if n in seen: errs.append(f"{where}: two options share the same note")
        seen.add(n)
        if v["kind"] not in ("mistake", "ruled-out"): errs.append(f"{where}: note kind {v['kind']!r} for option {k}")
    if len(x["why"].strip()) < 20: errs.append(f"{where}: 'why' is too short")
    bad = [t for t in x.get("tech", []) if t not in TECHNIQUES]
    if bad: errs.append(f"{where}: unknown technique tags {bad}")
    pid = x.get("passage")
    if pid:
        p = (ctx.get("passages") or {}).get(pid)
        if not p: errs.append(f"{where}: passage {pid!r} is not defined in PASSAGES")
        else: x["_passage"] = p["text"]
    if x["fmt"] == "rc" and not x.get("evidence"): errs.append(f"{where}: a reading-comprehension question needs an evidence line from the passage")
    if x["fmt"] == "rc" and x.get("_passage") is None: errs.append(f"{where}: a reading-comprehension question needs a passage")
    # grounding: a rule, a lexicon fact, or a line of evidence
    rules = x.get("rules", [])
    if ctx.get("rules") is not None:
        miss = [r for r in rules if r not in ctx["rules"]]
        if miss: errs.append(f"{where}: rules {miss} are not defined in the module")
    if not (rules or x.get("lex") or x.get("evidence")):
        errs.append(f"{where}: cite a rule (rules=[...]), a lexicon fact (lex=(kind, id)) or evidence from the passage")
    # format shape
    text, fmt = x["text"], x["fmt"]
    if fmt == "fill" and "___" not in text: errs.append(f"{where}: a fill-in question needs ___ in the text")
    if fmt == "spot-error":
        for o in opts:
            if norm(o) != "no error" and o.strip() not in text: errs.append(f"{where}: option {o!r} is not a part of the sentence")
    if fmt == "improve" and not re.search(r"\[\[.+?\]\]", text): errs.append(f"{where}: an improvement question marks the part as [[...]]")
    # lexicon check
    lex = x.get("lex")
    if lex:
        kind, wid = lex
        e = ctx["words"].get(wid)
        if kind not in LEX_KINDS: errs.append(f"{where}: lex kind {kind!r}")
        elif not e: errs.append(f"{where}: lex word {wid!r} is not in the lexicon")
        else:
            ki = LETTERS.index(key)
            keyopt, others = norm(opts[ki]), [norm(o) for j, o in enumerate(opts) if j != ki]
            if kind in ("syn", "ant"):
                field = {norm(s) for s in e[kind]}
                if norm(e["w"]) not in norm(text): errs.append(f"{where}: the question never shows {e['w']!r}")
                if keyopt not in field: errs.append(f"{where}: key {opts[ki]!r} is not in the lexicon's {kind} list for {e['w']}")
                for o in others:
                    if o in field: errs.append(f"{where}: wrong option {o!r} is also a {kind} of {e['w']} in the lexicon")
                    if o == norm(e["w"]): errs.append(f"{where}: the word itself is an option")
            elif kind == "meaning":
                ok = {norm(e["meaning"])} | {norm(a) for a in e.get("also", [])}
                if norm(e["w"]) not in norm(text): errs.append(f"{where}: the question never shows {e['w']!r}")
                if keyopt not in ok: errs.append(f"{where}: key {opts[ki]!r} is not the lexicon meaning of {e['w']}")
                for o in others:
                    if o in ok: errs.append(f"{where}: wrong option {o!r} is also an accepted meaning of {e['w']}")
            elif kind == "ows":
                if norm(e["meaning"]) not in norm(text): errs.append(f"{where}: the question must contain the phrase {e['meaning']!r}")
                if keyopt != norm(e["w"]): errs.append(f"{where}: key {opts[ki]!r} is not {e['w']}")
                if norm(e["w"]) in others: errs.append(f"{where}: the right word appears as a wrong option too")
            elif kind == "fits":
                if keyopt != norm(e["w"]): errs.append(f"{where}: key {opts[ki]!r} is not the stored word {e['w']!r}")
                if norm(e["w"]) in others: errs.append(f"{where}: the right word appears as a wrong option too")
            elif kind == "spell":
                mis = {norm(m) for m in e.get("misspell", [])}
                if keyopt != norm(e["w"]): errs.append(f"{where}: key {opts[ki]!r} is not the stored spelling {e['w']!r}")
                for o in others:
                    if o not in mis: errs.append(f"{where}: wrong option {o!r} is not a declared misspelling of {e['w']}")
            elif kind == "misspelt":
                mis = {norm(m) for m in e.get("misspell", [])}
                good = {norm(w2["w"]) for w2 in ctx["words"].values() if w2["kind"] in ("spelling", "word", "ows", "idiom")}
                if keyopt not in mis: errs.append(f"{where}: key {opts[ki]!r} is not a declared misspelling of {e['w']}")
                for o in others:
                    if o not in good: errs.append(f"{where}: option {o!r} is not stored as a correct spelling in the lexicon")
    if x.get("evidence") and x.get("_passage") is not None and norm(x["evidence"]) not in norm(x["_passage"]):
        errs.append(f"{where}: the evidence line is not in the passage")
    fn = x.get("_check")
    if fn is not None:
        try:
            if not fn(x): errs.append(f"{where}: the question's own check failed")
        except Exception as ex:
            errs.append(f"{where}: the question's own check raised {ex!r}")
    return errs


def finish_question(x):
    """Public form of a checked question: no callables, with its level."""
    w = wrong_notes(x.get("wrong"))
    trap = any(v["kind"] == "mistake" for v in w.values())
    n_rules = len(x.get("rules", [])) or (1 if x.get("lex") or x.get("evidence") else 1)
    sc = score(n_rules, trap, x.get("rare", False))
    out = {k: v for k, v in x.items() if not k.startswith("_")}
    out["wrong"] = w
    out["level"] = level(sc)
    out["score"] = sc
    return out
