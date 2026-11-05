#!/usr/bin/env python3
"""Run every check in one go. This is the only command to run after adding or changing anything.

    python3 tools/check.py             # rebuild stale topics, assemble data/core.json and data/lexicon.json
    python3 tools/check.py --browser   # also run the browser test (needs Playwright and Chromium)
    python3 tools/check.py --selftest  # also prove the checks can fail (breaks a temp copy on purpose)

Stops at the first failing step. Topics whose sources have not changed are skipped, so this stays fast as the bank grows.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
py = sys.executable
steps = [("topics (words, questions, notes, papers, tiers)", [py, os.path.join(HERE, "build_topic.py"), "--all"]),
         ("assemble the site data (papers, days, lexicon, gap gates)", [py, os.path.join(HERE, "build.py")])]
if "--selftest" in sys.argv: steps.append(("selftest: every check can fail", [py, os.path.join(HERE, "selftest.py")]))
if "--browser" in sys.argv: steps.append(("browser test", [py, os.path.join(HERE, "render_test.py")]))
for name, cmd in steps:
    print(f"== {name}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    print((r.stdout or "").rstrip())
    if r.returncode != 0:
        print((r.stderr or "")[-800:]); sys.exit(f"FAILED at: {name}")
print("\nall good")
