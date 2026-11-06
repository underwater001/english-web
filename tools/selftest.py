#!/usr/bin/env python3
"""Prove the checks can fail. Copies the repo to a temp folder, breaks one thing at a time, and requires the build to refuse.

    python3 tools/selftest.py

Each case below must make `build_topic.py --all` or `build.py` exit non-zero and print the expected message.
A check that cannot fail protects nothing, so run this after changing any check in bank.py, build_topic.py or build.py.
"""
import json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
py = sys.executable


def fresh():
    d = tempfile.mkdtemp(prefix="ew-selftest-")
    shutil.copytree(ROOT, d + "/r", ignore=shutil.ignore_patterns(".git", "__pycache__", "node_modules"))
    return d + "/r"


def run(root, *args):
    r = subprocess.run([py, os.path.join(root, "tools", args[0]), *args[1:]], capture_output=True, text=True, cwd=root)
    return r.returncode, r.stdout + r.stderr


def sub(root, rel, old, new, count=1):
    p = os.path.join(root, rel)
    s = open(p, encoding="utf-8").read()
    assert old in s, f"selftest is out of date: {old!r} not found in {rel}"
    open(p, "w", encoding="utf-8").write(s.replace(old, new, count))


PAPER = {"id": "T-1", "exam": "SSC CGL Tier-I", "kind": "official", "publisher": "test", "date": "2025-01-01", "shift": 1, "link": None, "section": "English",
         "rows": [{"qno": 1, "topic": "subject-verb-agreement", "fmt": "fill", "key": "a", "answer": "was", "keySource": "official"}]}

DAY = {"date": "2026-01-01", "paper": {"publication": "Test", "edition": "", "pages": "1", "link": None, "title": "t"},
       "words": [{"id": "w-tenacious", "w": "tenacious", "kind": "word", "pos": "adj", "meaning": "Holding firmly to a purpose.", "syn": ["persistent", "determined"], "ant": ["yielding"],
                  "ex": "Her tenacious effort won the case.", "also": [], "note": ""}],
       "capsule": [{"text": "**Tenacious** means holding firmly to a purpose.", "words": ["w-tenacious"]}],
       "quiz": [{"id": "q20260101-001", "qtype": "daily", "fmt": "synonym", "text": "Select the synonym of: TENACIOUS", "options": ["Persistent", "Yielding", "Careless", "Gentle"], "key": "a",
                 "why": "Tenacious means holding firmly to a purpose, as persistent does.", "lex": ["syn", "w-tenacious"],
                 "wrong": {"b": "Yielding gives way, the opposite of holding firmly to a purpose.", "c": "Careless means not paying attention; unrelated to firmness of purpose.",
                           "d": "Gentle means mild; it says nothing about determination or purpose."}}]}


def main():
    cases, ok = [], True

    def case(name, fn, expect):
        nonlocal ok
        root = fresh()
        try:
            code, out = fn(root)
        finally:
            shutil.rmtree(os.path.dirname(root), ignore_errors=True)
        passed = (code != 0) and (expect in out) if expect else code == 0
        ok &= passed
        print(("PASS " if passed else "FAIL ") + name + ("" if passed else f"\n   got exit {code}: {out[-400:]}"))

    sa, sva = "tools/topics/synonyms_antonyms.py", "tools/topics/subject_verb_agreement.py"
    case("baseline builds", lambda r: run(r, "build_topic.py", "--all", "--force"), None)
    case("key not in the lexicon's synonym list", lambda r: (sub(r, sa, '["charitable", "kindly", "generous", "humane"], ["malicious"', '["kindly", "generous", "humane"], ["malicious"'), run(r, "build_topic.py", "--all", "--force"))[1], "is not in the lexicon's syn list")
    case("a wrong option is also a synonym", lambda r: (sub(r, sa, '["Malicious", "Charitable", "Reluctant", "Stingy"]', '["Malicious", "Charitable", "Kindly", "Stingy"]'), run(r, "build_topic.py", "--all", "--force"))[1], "is also a syn of benevolent")
    case("antonym question keyed to a synonym", lambda r: (sub(r, sa, '["plentiful", "abundant", "ample"]', '["abundant", "ample"]'), run(r, "build_topic.py", "--all", "--force"))[1], "not in the lexicon's ant list")
    case("two options with the same number", lambda r: (sub(r, sva, '["was", "were", "are", "have been"], "a"', '["was", "has", "are", "have been"], "a"'), run(r, "build_topic.py", "--all", "--force"))[1], "own check failed")
    case("duplicate options", lambda r: (sub(r, sva, '["was", "were", "are", "have been"], "a"', '["was", "was", "are", "have been"], "a"'), run(r, "build_topic.py", "--all", "--force"))[1], "not four distinct")
    case("a wrong option with no note", lambda r: (sub(r, "tools/topics/idioms_phrases.py", '"d": ruled_out("That is the meaning of \'once in a blue moon\'; it has nothing to do with secrets.")', ""), run(r, "build_topic.py", "--all", "--force"))[1], "wrong-option notes must be exactly")
    case("idiom key is not its meaning", lambda r: (sub(r, "tools/topics/idioms_phrases.py", '[_M["burn-the-midnight-oil"], _M["spill-the-beans"], "To drop food while cooking", _M["once-in-a-blue-moon"]], "b"', '[_M["burn-the-midnight-oil"], _M["spill-the-beans"], "To drop food while cooking", _M["once-in-a-blue-moon"]], "a"'), run(r, "build_topic.py", "--all", "--force"))[1], "is not the lexicon meaning")
    case("one-word key is the wrong word", lambda r: (sub(r, "tools/topics/one_word_substitution.py", '["Omnipotent", "Omniscient", "Omnipresent", "Philanthropist"], "b"', '["Omnipotent", "Omniscient", "Omnipresent", "Philanthropist"], "a"'), run(r, "build_topic.py", "--all", "--force"))[1], "is not omniscient")

    sp = "tools/topics/spellings.py"
    case("spelling option that is not a declared misspelling", lambda r: (sub(r, sp, '"Ventriculoatriall", "Ventriculoateriel"]', '"Ventriculoatriall", "Ventriculoatreal"]'), run(r, "build_topic.py", "--all", "--force"))[1], "is not a declared misspelling")
    case("misspelt-word question with an unstored 'correct' option", lambda r: (sub(r, sp, '("vicereine", "vicereine",', '("vicereine", "vicereen",'), run(r, "build_topic.py", "--all", "--force"))[1], "is not stored as a correct spelling")

    def coverage(r):
        sub(r, "tools/topics/para_jumbles.py", "return _base() + _EXTRA", "return _base()")
        run(r, "build_topic.py", "--all", "--force")
        return run(r, "build.py", "--coverage")
    case("a format with less drill stock than the blueprint asks for", coverage, "is asked 2.00 times a paper")

    def stale(r):
        run(r, "build_topic.py", "--all", "--force")
        sub(r, sa, '"frugal", "frugal"', '"frugal", "frugal"  ')
        return run(r, "build.py")
    case("stale shard refuses to assemble", stale, "shard is stale")

    def filed_no_quiz(r):
        run(r, "build_topic.py", "--all", "--force")
        json.dump(PAPER, open(os.path.join(r, "data/papers/T-1.json"), "w"))
        return run(r, "build.py")
    case("filed paper question with no quiz", filed_no_quiz, "have no quiz yet")

    def pyq_key_mismatch(r):
        # the T-1 paper file says question 1 of a spare topic is keyed 'a'; give the module a past question keyed 'b' for it
        json.dump(PAPER, open(os.path.join(r, "data/papers/T-1.json"), "w"))
        sub(r, sva, "PYQS = [\n", '''PYQS = [
    q("q-sva-each", "fill", "Select the most appropriate option to fill in the blank.\\nEach of the boys ___ here.", ["was", "were", "are", "have been"], "b",
      "Each is singular, so the verb is singular and the right option is was.",
      {"a": mistake("Singular verb; this note is here only for the selftest."), "c": mistake("Plural present verb; selftest."), "d": mistake("Plural verb; selftest.")},
      rules=["sva-r1"], paper="T-1", qno=1),
''')
        return run(r, "build_topic.py", "--all", "--force")
    case("past question key differs from the paper file", pyq_key_mismatch, "but the paper file says")

    def day_ok(r):
        run(r, "build_topic.py", "--all", "--force")
        json.dump(DAY, open(os.path.join(r, "data/days/2026-01-01.json"), "w"))
        return run(r, "build.py")
    case("a valid daily file builds", day_ok, None)

    def day_untested(r):
        run(r, "build_topic.py", "--all", "--force")
        d = json.loads(json.dumps(DAY)); d["quiz"] = []
        json.dump(d, open(os.path.join(r, "data/days/2026-01-01.json"), "w"))
        return run(r, "build.py")
    case("daily word with no quiz question", day_untested, "is tested by no quiz question")

    def day_wrong_key(r):
        run(r, "build_topic.py", "--all", "--force")
        d = json.loads(json.dumps(DAY)); d["quiz"][0]["options"][1] = "Persistent "; d["quiz"][0]["options"][0] = "Determined"
        d["quiz"][0]["options"][1] = "Persistent"
        json.dump(d, open(os.path.join(r, "data/days/2026-01-01.json"), "w"))
        return run(r, "build.py")
    case("daily wrong option is also a synonym", day_wrong_key, "is also a syn of tenacious")

    def day_evidence(r):
        run(r, "build_topic.py", "--all", "--force")
        d = json.loads(json.dumps(DAY))
        d["passage"] = {"title": "P", "text": "The council approved the plan on Monday.", "questions": [
            {"id": "q20260101-101", "fmt": "rc", "qtype": "daily", "text": "When was the plan approved?", "options": ["Monday", "Friday", "Sunday", "Tuesday"], "key": "a",
             "why": "The passage says the council approved the plan on Monday.", "evidence": "approved the plan on Tuesday",
             "wrong": {"b": "Friday is not mentioned anywhere in the passage.", "c": "Sunday is not mentioned anywhere in the passage.", "d": "Tuesday is not mentioned anywhere in the passage."}}]}
        json.dump(d, open(os.path.join(r, "data/days/2026-01-01.json"), "w"))
        return run(r, "build.py")
    case("passage question whose evidence is not in the passage", day_evidence, "evidence line is not in the passage")

    print("\nall checks can fail as intended" if ok else "\nSELFTEST FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
