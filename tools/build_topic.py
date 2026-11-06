#!/usr/bin/env python3
"""Verify one topic module and write its data shard.

    python3 tools/build_topic.py synonyms-antonyms          # build (skipped if nothing changed)
    python3 tools/build_topic.py synonyms-antonyms --force  # rebuild anyway
    python3 tools/build_topic.py --all                      # every topic whose shard is stale or missing
    python3 tools/build_topic.py synonyms-antonyms --check  # verify only, write nothing

A topic lives entirely in tools/topics/<topic>.py (see tools/topics/_template.py) and builds to
data/shards/<topic>.json. Nothing else is touched, so adding a topic never forces a rebuild of the others.
The shard records a hash of its sources; tools/build.py refuses to assemble the site from a stale shard.

Checks, in order. Any failure stops the build before anything is written.
  1. Words: every lexicon entry is complete, its example contains it, no word is its own synonym.
  2. Every question (past or practice): four distinct options, one key, a real note for each wrong option,
     a rule / lexicon fact / evidence line behind the answer, the right shape for its format, and, for
     vocabulary, the answer is checked against the lexicon (the key is in the word's list, no wrong option is).
  3. Past questions: the paper and question number exist in data/papers with the same topic, format, key and answer text.
  4. Nodes, rules, methods, passages and technique tags reference things that exist.
  5. Tier coverage.

Tiers (TIER in the module)
  "seed"  practice only, at least 2 per question type: a topic can be played before any paper has been filed
  "quiz"  at least one past question; each type has the whole method; practice optional
  "full"  quiz plus at least 3 practice per type, one of them Medium or Hard
"""
import hashlib, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")

import bank

METHOD_KEYS = ["cue", "standard", "fast", "eliminate", "traps"]
MIN_PRACTICE = {"seed": 2, "quiz": 0, "full": 3}


def jload(p):
    with open(p, encoding="utf-8") as fp:
        return json.load(fp)


def mod(topic):
    return topic.replace("-", "_")


def all_topics():
    return sorted(f[:-3].replace("_", "-") for f in os.listdir(os.path.join(HERE, "topics")) if f.endswith(".py") and not f.startswith("_"))


def source_hash(topic):
    h = hashlib.sha1()
    for p in (os.path.join(HERE, "topics", mod(topic) + ".py"), os.path.join(HERE, "bank.py"), os.path.abspath(__file__)):
        if os.path.exists(p):
            h.update(open(p, "rb").read())
    pp = os.path.join(DATA, "papers")
    if os.path.isdir(pp):          # past questions are checked against the paper files, so they are part of the source
        for f in sorted(os.listdir(pp)):
            if f.endswith(".json"):
                p = jload(os.path.join(pp, f))
                h.update(json.dumps([r for r in p["rows"] if r["topic"] == topic], sort_keys=True).encode())
    tp = os.path.join(DATA, "tree.json")
    h.update(open(tp, "rb").read())
    return h.hexdigest()[:16]


def load_module(topic):
    p = os.path.join(HERE, "topics", mod(topic) + ".py")
    spec = importlib.util.spec_from_file_location("topic_" + mod(topic), p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def module_words(topic):
    """Lexicon entries a topic module defines (read without verifying the rest)."""
    return load_module(topic).WORDS if hasattr(load_module(topic), "WORDS") else []


def build(topic, write=True):
    errs = []
    tree = jload(os.path.join(DATA, "tree.json"))
    if tree.get(topic, {}).get("kind") != "topic":
        return [f"{topic}: not a topic in data/tree.json"], None
    m = load_module(topic)
    tier = getattr(m, "TIER", "full")
    if m.TOPIC != topic: errs.append(f"{topic}: module TOPIC is {m.TOPIC!r}")
    if tier not in MIN_PRACTICE: errs.append(f"{topic}: TIER {tier!r} must be one of {list(MIN_PRACTICE)}")
    nodes, rules, methods, refs = m.NODES, m.RULES, m.METHODS, getattr(m, "REFS", [])
    words = getattr(m, "WORDS", [])
    prefix = m.PREFIX

    # ---- nodes -----------------------------------------------------------------------------------
    qtypes = set()
    for k, n in nodes.items():
        for f in ("short", "label", "kind", "parent", "order", "summary"):
            if f not in n: errs.append(f"node {k}: missing {f}")
        if n.get("kind") != "qtype": errs.append(f"node {k}: kind must be 'qtype'")
        if n.get("parent") != topic: errs.append(f"node {k}: parent must be the topic {topic}")
        qtypes.add(k)
    if not qtypes: errs.append(f"{topic}: define at least one question type in NODES")

    # ---- rules -----------------------------------------------------------------------------------
    rule_ids = set()
    for r in rules:
        for f in ("id", "node", "text"):
            if not r.get(f): errs.append(f"rule {r.get('id')}: missing {f}")
        if r.get("id") in rule_ids: errs.append(f"rule {r['id']} appears twice")
        rule_ids.add(r.get("id"))
        if r.get("node") not in qtypes and r.get("node") != topic: errs.append(f"rule {r.get('id')}: node {r.get('node')} is not a question type of this topic")
        if bool(r.get("ok")) != bool(r.get("bad")): errs.append(f"rule {r.get('id')}: give both a correct example (ok) and an incorrect one (bad), or neither")

    # ---- methods ---------------------------------------------------------------------------------
    for k in qtypes:
        mt = methods.get(k)
        if not mt: errs.append(f"{k}: no entry in METHODS"); continue
        for f in METHOD_KEYS:
            if not mt.get(f): errs.append(f"{k}: method is missing '{f}'")
        if not isinstance(mt.get("traps", []), list) or not mt.get("traps"): errs.append(f"{k}: traps must be a non-empty list")
        for r in mt.get("rules", []):
            if r not in rule_ids: errs.append(f"{k}: method cites rule {r} which does not exist")
        for t in mt.get("tech", []):
            if t not in bank.TECHNIQUES: errs.append(f"{k}: unknown technique {t}")
    for k in methods:
        if k not in qtypes: errs.append(f"METHODS has {k} which is not a question type")
    for rf in refs:
        if not (rf.get("title") and str(rf.get("url", "")).startswith("http") and rf.get("note")): errs.append(f"REFS entry needs title, url and note: {rf}")

    # ---- words -----------------------------------------------------------------------------------
    wmap = {}
    for e in words:
        errs += bank.check_word(e, f"word {e.get('id')}")
        if e.get("id") in wmap: errs.append(f"word {e['id']} appears twice")
        wmap[e.get("id")] = e
    passages = getattr(m, "PASSAGES", {})
    for pid, pg in passages.items():
        for f in ("title", "text", "src"):
            if not pg.get(f): errs.append(f"passage {pid}: missing {f}")
        n = len(bank.re.findall(r"\w+", pg.get("text", "")))
        if n > 400: errs.append(f"passage {pid}: {n} words; store a condensed restatement of at most 400 words")
    ctx = {"words": wmap, "rules": rule_ids, "qtypes": qtypes, "passages": passages}

    # ---- past questions: against the paper files ---------------------------------------------------
    papers = {}
    pp = os.path.join(DATA, "papers")
    if os.path.isdir(pp):
        for f in sorted(os.listdir(pp)):
            if f.endswith(".json"):
                p = jload(os.path.join(pp, f)); papers[p["id"]] = p
    pyqs, practice, ids = [], [], set()
    for x in m.PYQS:
        where = f"pyq {x.get('id')}"
        errs += bank.check_question(x, ctx, where)
        if x["id"] in ids: errs.append(f"{where}: appears twice")
        ids.add(x["id"])
        p = papers.get(x["paper"])
        row = next((r for r in p["rows"] if r["qno"] == x["qno"]), None) if p else None
        if not p: errs.append(f"{where}: paper {x['paper']} has no file in data/papers"); continue
        if not row: errs.append(f"{where}: paper {x['paper']} has no row for question {x['qno']}"); continue
        if row["topic"] != topic: errs.append(f"{where}: paper file files it under {row['topic']}")
        if row.get("fmt") != x["fmt"]: errs.append(f"{where}: format {x['fmt']} but the paper file says {row.get('fmt')}")
        if row["key"] != x["key"]: errs.append(f"{where}: key {x['key']} but the paper file says {row['key']}")
        if bank.norm(row["answer"]) != bank.norm(x["options"][bank.LETTERS.index(x["key"])]): errs.append(f"{where}: keyed option {x['options'][bank.LETTERS.index(x['key'])]!r} is not the paper file's answer {row['answer']!r}")
        out = bank.finish_question(x)
        out["keySource"] = row.get("keySource", "derived")
        pyqs.append(out)

    # ---- practice ---------------------------------------------------------------------------------
    items = m.practice_items() if hasattr(m, "practice_items") else []
    for x in items:
        where = f"practice {x.get('id')}"
        if not (x.get("id") or "").startswith(prefix + "-"): errs.append(f"{where}: id must start with {prefix}-")
        errs += bank.check_question(x, ctx, where)
        if x["id"] in ids: errs.append(f"{where}: appears twice")
        ids.add(x["id"])
        practice.append(bank.finish_question(x))

    # ---- tier coverage ----------------------------------------------------------------------------
    if tier in ("quiz", "full") and not pyqs: errs.append(f"{topic}: tier {tier} needs at least one past question (use TIER = 'seed' until a paper is filed)")
    for k in qtypes:
        n_p = sum(1 for x in practice if x["qtype"] == k)
        n_q = sum(1 for x in pyqs if x["qtype"] == k)
        if n_p + n_q == 0: errs.append(f"{k}: a question type with no question")
        if tier in MIN_PRACTICE and n_p < MIN_PRACTICE[tier] and tier != "quiz": errs.append(f"{k}: tier {tier} needs {MIN_PRACTICE[tier]} practice questions, has {n_p}")
        if tier == "full" and n_p and not any(x["level"] in ("Medium", "Hard") for x in practice if x["qtype"] == k):
            errs.append(f"{k}: a full topic needs at least one Medium or Hard practice question")
    if errs: return errs, None

    shard = {"topic": topic, "tier": tier, "src_hash": source_hash(topic),
             "nodes": nodes, "rules": rules, "methods": methods, "refs": refs,
             "words": [w["id"] for w in words], "passages": passages, "pyqs": pyqs, "practice": practice}
    if write:
        os.makedirs(os.path.join(DATA, "shards"), exist_ok=True)
        path = os.path.join(DATA, "shards", topic + ".json")
        with open(path, "w", encoding="utf-8") as fp:
            json.dump(shard, fp, ensure_ascii=False, separators=(",", ":")); fp.write("\n")
    return [], shard


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force, check_only = "--force" in sys.argv, "--check" in sys.argv
    topics = all_topics() if "--all" in sys.argv else args
    if not topics: sys.exit(__doc__)
    bad = 0
    for t in topics:
        path = os.path.join(DATA, "shards", t + ".json")
        if not force and not check_only and os.path.exists(path) and jload(path).get("src_hash") == source_hash(t):
            print(f"unchanged: {t}"); continue
        errs, shard = build(t, write=not check_only)
        if errs:
            bad += 1; print(f"FAILED: {t}"); [print("  -", e) for e in errs]
        else:
            print(f"built: {t} ({shard['tier']}, {len(shard['pyqs'])} past, {len(shard['practice'])} practice)")
    if bad: sys.exit(1)


if __name__ == "__main__":
    main()
