#!/usr/bin/env python3
"""Assemble the site's data from the topic shards, the paper files and the daily files. Cheap: no topic is re-verified here.

    python3 tools/build.py            # fail if any topic shard is stale, else write data/core.json and data/lexicon.json
    python3 tools/build.py --rebuild  # first rebuild the stale shards (tools/build_topic.py --all)

Inputs   data/tree.json            junctions and topics (hand-kept; a new topic is one new entry)
         data/papers/<id>.json     one file per paper: details and one row per English question (topic, format, key, answer)
         data/days/<date>.json     one file per daily drop: words, capsule, quiz and an optional passage with questions
         data/shards/<topic>.json  built by tools/build_topic.py
Outputs  data/core.json            small, loaded at start
         data/lexicon.json         every word, idiom, one-word substitution and phrasal verb

Gap gates (the build fails on any of them)
  - a filed paper question with no quiz, or a quiz with no filed question
  - a daily word that no quiz question tests, or that no capsule point carries
"""
import json, os, re, subprocess, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")

import bank
import build_topic as BT


def jload(p):
    with open(p, encoding="utf-8") as fp:
        return json.load(fp)


def write_if_changed(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n"
    if os.path.exists(path) and open(path, encoding="utf-8").read() == text:
        return False
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(text)
    return True


def stat_block(rows, n_papers):
    topics, fmts = {}, {}
    for r in rows:
        for d, k in ((topics, r["topic"]), (fmts, r["fmt"])):
            v = d.setdefault(k, {"n": 0, "papers": set(), "kinds": Counter()})
            v["n"] += 1; v["papers"].add(r["paper"]); v["kinds"][r["kind"]] += 1
    def fin(d):
        return {k: {"n": v["n"], "shifts": len(v["papers"]), "lik": bank.likelihood(len(v["papers"]), n_papers),
                    "perShift": round(v["n"] / n_papers, 2), "kinds": dict(v["kinds"])} for k, v in sorted(d.items())}
    return {"papers": n_papers, "questions": len(rows), "topics": fin(topics), "formats": fin(fmts)}


def check_day(date, d, lexicon_static, errs):
    """Validate one daily file. Returns (words, public questions)."""
    w = f"day {date}"
    for k in ("date", "paper", "words", "capsule", "quiz"):
        if k not in d: errs.append(f"{w}: missing '{k}'")
    if errs and any(e.startswith(w) for e in errs): return [], []
    if d["date"] != date: errs.append(f"{w}: file name and date field differ")
    if not d["paper"].get("publication"): errs.append(f"{w}: paper.publication is required (link may be null)")
    words = d["words"]
    wmap = dict(lexicon_static)
    own = {}
    for e in words:
        errs += bank.check_word(e, f"{w} word {e.get('id')}")
        if e.get("id") in wmap: errs.append(f"{w}: word id {e.get('id')} already exists in the lexicon; reuse it instead of adding it again")
        wmap[e.get("id")] = e; own[e.get("id")] = e
    # capsule
    carried = set()
    for i, c in enumerate(d["capsule"]):
        if not c.get("text") or len(c["text"]) > 260: errs.append(f"{w}: capsule point {i + 1} needs text of at most 260 characters")
        if "**" not in c.get("text", ""): errs.append(f"{w}: capsule point {i + 1} should bold its testable terms with **")
        for x in c.get("words", []):
            if x not in wmap: errs.append(f"{w}: capsule point {i + 1} cites unknown word {x}")
            carried.add(x)
    for x in own:
        if x not in carried: errs.append(f"{w}: word {x} is in no capsule point")
    # quiz
    passage = d.get("passage")
    ptxt = passage["text"] if passage else None
    if passage:
        n = len(re.findall(r"\w+", passage["text"]))
        if n > 400: errs.append(f"{w}: the passage is {n} words; keep it to your own condensed version (at most 400 words)")
        if not passage.get("title"): errs.append(f"{w}: passage needs a title")
    qs, ids, tested = [], set(), set()
    pre = "q" + date.replace("-", "") + "-"
    allq = [(x, False) for x in d["quiz"]] + [(x, True) for x in (passage or {}).get("questions", [])]
    for x, is_p in allq:
        if not str(x.get("id", "")).startswith(pre): errs.append(f"{w}: question id {x.get('id')} must start with {pre}")
        if x.get("id") in ids: errs.append(f"{w}: {x.get('id')} appears twice")
        ids.add(x.get("id"))
        x = dict(x); x.setdefault("qtype", "daily"); x.setdefault("rules", []); x["lex"] = x.get("lex")
        if is_p: x["_passage"] = ptxt; x.setdefault("fmt", "rc")
        e2 = bank.check_question(x, {"words": wmap, "rules": None, "qtypes": None}, f"{w} {x.get('id')}")
        errs += e2
        if x.get("lex"): tested.add(x["lex"][1])
        if not e2: qs.append(bank.finish_question(x))
    for x in own:
        if x not in tested: errs.append(f"{w}: word {x} is tested by no quiz question")
    return words, qs


def main():
    if "--rebuild" in sys.argv:
        if subprocess.call([sys.executable, os.path.join(HERE, "build_topic.py"), "--all"]) != 0: sys.exit(1)
    errs = []
    tree = jload(os.path.join(DATA, "tree.json"))

    # ---- shards ---------------------------------------------------------------------------------
    modules = BT.all_topics()
    shards = {}
    for t in modules:
        p = os.path.join(DATA, "shards", t + ".json")
        if not os.path.exists(p): errs.append(f"topic {t}: no shard. Run: python3 tools/build_topic.py {t}"); continue
        s = jload(p)
        if s["src_hash"] != BT.source_hash(t): errs.append(f"topic {t}: shard is stale. Run: python3 tools/build_topic.py {t}"); continue
        shards[t] = s
    sd = os.path.join(DATA, "shards")
    for f in os.listdir(sd) if os.path.isdir(sd) else []:
        if f.endswith(".json") and f[:-5] not in modules: errs.append(f"shard {f} has no module in tools/topics/")

    # ---- nodes ----------------------------------------------------------------------------------
    nodes = {k: dict(v) for k, v in tree.items()}
    for t, s in shards.items():
        for k, n in s["nodes"].items():
            if k in nodes: errs.append(f"node id {k} is used by two topics")
            nodes[k] = dict(n)
    for k, n in nodes.items():
        n["links"] = list(n.get("links", []))
        if n["parent"] != "hub" and n["parent"] not in nodes: errs.append(f"node {k}: parent {n['parent']} missing")
        if n["kind"] == "junction" and ("hue" not in n or n["parent"] != "hub"): errs.append(f"junction {k}: needs hue and parent hub")
        if n["kind"] == "topic" and nodes.get(n["parent"], {}).get("kind") != "junction": errs.append(f"topic {k}: parent must be a junction")
    for k, n in list(nodes.items()):
        for l in n["links"]:
            if l not in nodes: errs.append(f"node {k}: link {l} missing")
            elif k not in nodes[l]["links"]: nodes[l]["links"].append(k)
    for n in nodes.values(): n["links"].sort()

    # ---- lexicon: topic words + daily words -----------------------------------------------------
    lexicon, static = [], {}
    for t in shards:
        for e in BT.load_module(t).WORDS if hasattr(BT.load_module(t), "WORDS") else []:
            if e["id"] in static: errs.append(f"word id {e['id']} is defined by two topics")
            static[e["id"]] = e; lexicon.append({**e, "src": "topic:" + t})

    # ---- papers ---------------------------------------------------------------------------------
    papers, rows = [], []
    pdir = os.path.join(DATA, "papers")
    for f in sorted(os.listdir(pdir)) if os.path.isdir(pdir) else []:
        if not f.endswith(".json"): continue
        p = jload(os.path.join(pdir, f))
        if p["id"] + ".json" != f: errs.append(f"papers/{f}: id {p['id']} does not match the file name")
        seen = set()
        for r in p["rows"]:
            if r["qno"] in seen: errs.append(f"{p['id']}: question {r['qno']} appears twice")
            seen.add(r["qno"])
            if nodes.get(r["topic"], {}).get("kind") != "topic": errs.append(f"{p['id']} Q{r['qno']}: {r['topic']!r} is not a topic in data/tree.json")
            if r.get("fmt") not in bank.FORMATS: errs.append(f"{p['id']} Q{r['qno']}: fmt {r.get('fmt')!r} is not a known format")
            if r.get("key") not in bank.LETTERS: errs.append(f"{p['id']} Q{r['qno']}: key must be a, b, c or d")
            rows.append({"id": f"{p['id']}-Q{r['qno']}", "paper": p["id"], "kind": p["kind"], "exam": p["exam"], "topic": r["topic"], "fmt": r["fmt"]})
        papers.append({k: v for k, v in p.items() if k != "rows"} | {"n": len(p["rows"]), "topics": dict(sorted(Counter(r["topic"] for r in p["rows"]).items())),
                                                                       "derivedKeys": sum(1 for r in p["rows"] if r.get("keySource", "derived") != "official")})
    quizzed = {q["id"] for s in shards.values() for q in s["pyqs"]}
    gaps = defaultdict(list)
    for r in rows:
        if r["id"] not in quizzed: gaps[r["topic"]].append("Q" + r["id"].split("-Q")[1])
    for t, ids in sorted(gaps.items()):
        errs.append(f"{len(ids)} filed question(s) in {t} have no quiz yet ({', '.join(ids[:6])}{'…' if len(ids) > 6 else ''}). Add them to tools/topics/{BT.mod(t)}.py (TIER = \"quiz\" is enough to go live).")
    filed = {r["id"] for r in rows}
    for t, s in shards.items():
        for q in s["pyqs"]:
            if q["id"] not in filed: errs.append(f"{q['id']}: quiz exists but the paper file has no such question")
    for p in papers: p["built"] = sum(1 for s in shards.values() for q in s["pyqs"] if q["paper"] == p["id"])

    # ---- days -----------------------------------------------------------------------------------
    days = []
    ddir = os.path.join(DATA, "days")
    for f in sorted(os.listdir(ddir)) if os.path.isdir(ddir) else []:
        if not f.endswith(".json"): continue
        date = f[:-5]
        d = jload(os.path.join(ddir, f))
        words, qs = check_day(date, d, {**static, **{e["id"]: e for e in lexicon if e["src"].startswith("day:")}}, errs)
        for e in words: lexicon.append({**e, "src": "day:" + date})
        days.append({"date": date, "publication": d["paper"].get("publication"), "edition": d["paper"].get("edition"), "pages": d["paper"].get("pages"),
                     "title": d["paper"].get("title"), "link": d["paper"].get("link"), "words": len(d["words"]), "capsule": len(d["capsule"]),
                     "questions": len(d["quiz"]) + len((d.get("passage") or {}).get("questions", [])), "passage": bool(d.get("passage"))})
    if errs:
        print("BUILD FAILED"); [print(" -", e) for e in errs]; sys.exit(1)

    # ---- stats: how often each topic and format appears -----------------------------------------
    shift_rows = [r for r in rows if r["kind"] != "chapter-bank"]
    scopes = {"all": shift_rows} | {e: [r for r in shift_rows if r["exam"] == e] for e in sorted({r["exam"] for r in shift_rows})}
    stats = {}
    for name, rs in scopes.items():
        n_papers = len({r["paper"] for r in rs})
        if n_papers: stats[name] = stat_block(rs, n_papers)

    cols = ["id", "topic", "qtype", "fmt", "level", "src"]
    bank_rows = []
    for t, s in shards.items():
        for q in s["pyqs"]: bank_rows.append([q["id"], t, q["qtype"], q["fmt"], q["level"], "pyq"])
        for q in s["practice"]: bank_rows.append([q["id"], t, q["qtype"], q["fmt"], q["level"], "practice"])
    by_topic = Counter(r["topic"] for r in rows)
    topics_meta = {}
    for k, n in nodes.items():
        if n["kind"] == "topic":
            s = shards.get(k)
            topics_meta[k] = {"indexed": by_topic.get(k, 0), "built": bool(s), "tier": s["tier"] if s else None, "pyqs": len(s["pyqs"]) if s else 0,
                              "practice": len(s["practice"]) if s else 0, **({"v": s["src_hash"]} if s else {})}
    refs = [{"topic": t, **r} for t, s in shards.items() for r in s.get("refs", [])]
    core = {"nodes": nodes, "papers": papers, "days": days, "stats": stats, "topics": topics_meta, "bank": {"cols": cols, "rows": bank_rows},
            "formats": bank.FORMATS, "techniques": bank.TECHNIQUES, "kinds": bank.KINDS, "refs": refs, "lexiconSize": len(lexicon),
            "rubric": {"rules": "1 rule = 1 point, 2 = 2, 3 or more = 3", "trap": "+1 if a wrong option is the result of a named common mistake",
                       "rare": "+1 if a hard or rarely seen word is the point", "levels": "up to 2 Easy, 3 Medium, 4 or more Hard"},
            "likelihood": "High if the topic appeared in at least 2/3 of the analysed papers, Medium if at least 1/3, Low otherwise. Always read it with the number of papers."}
    a = write_if_changed(os.path.join(DATA, "core.json"), core)
    b = write_if_changed(os.path.join(DATA, "lexicon.json"), sorted(lexicon, key=lambda e: e["w"].lower()))
    print(f"{'wrote' if a else 'unchanged'}: core.json ({len(nodes)} nodes, {len(papers)} papers, {len(days)} days, {len(bank_rows)} questions); "
          f"{'wrote' if b else 'unchanged'}: lexicon.json ({len(lexicon)} entries); topics: {', '.join(shards) or 'none'}")


if __name__ == "__main__":
    main()
