#!/usr/bin/env python3
"""Browser test: serve the repo, open the page in Chromium, click through every view, fail on any console error.
Counts come from data/core.json, never hard-coded.   python3 tools/render_test.py
"""
import json, os, sys, threading, http.server, socketserver, functools
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
core = json.load(open(os.path.join(ROOT, "data", "core.json"), encoding="utf-8"))
lex = json.load(open(os.path.join(ROOT, "data", "lexicon.json"), encoding="utf-8"))
bp = core.get("blueprint") or {}

class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(("127.0.0.1", 0), functools.partial(Q, directory=ROOT)); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
fails, errors = [], []
def ok(c, m):
    print(("ok   " if c else "FAIL ") + m)
    if not c: fails.append(m)

def go(pg, hash_, sel):
    """Open a view. Same-document hash changes re-render asynchronously, so reload to start from a clean page."""
    pg.goto(f"http://127.0.0.1:{port}/index.html{hash_}"); pg.reload(); pg.wait_for_selector(sel)

built = [t for t, m in core["topics"].items() if m["built"]]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1000, "height": 900})
    pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    pg.on("pageerror", lambda e: errors.append(str(e)))
    # ---- today ------------------------------------------------------------------------------
    go(pg, "#/", ".tile")
    ok(str(len(core["bank"]["rows"])) in pg.inner_text("#stats"), "header shows the question count")
    ok(pg.locator(".tile").count() == 4, "today shows the four headline numbers")
    ok(pg.locator("table.t tbody tr").count() == len(bp.get("formats", [])), "one marks-at-risk row per format in the blueprint")
    ok("0%" in pg.inner_text(".tile:nth-child(3)"), "nothing is solid before any answer")
    # ---- syllabus ---------------------------------------------------------------------------
    go(pg, "#/syllabus", ".card")
    ok(pg.locator(".card a.title").count() == sum(1 for n in core["nodes"].values() if n["kind"] == "topic"), "one card per topic")
    ok(pg.locator(".card.dim").count() == sum(1 for m in core["topics"].values() if not m["built"]), "unbuilt topics are dimmed")
    # ---- a topic ----------------------------------------------------------------------------
    t = built[0]
    go(pg, f"#/topic/{t}", "article.q")
    m = core["topics"][t]
    ok(pg.locator("article.q").count() == m["pyqs"] + m["practice"], f"{t}: every question is on the page")
    ok(pg.locator("section.block .rule").count() >= 1, f"{t}: rules are shown")
    first = pg.locator("article.q").first
    first.locator(".opt").nth(0).click()
    ok(first.locator(".reveal").is_visible(), "answering reveals the explanation")
    ok(first.locator(".reveal li").count() == 3, "three wrong-option notes are shown")
    ok(first.locator(".opt.right").count() == 1, "exactly one option is marked right")
    ok(first.locator(".opt[disabled]").count() == 4, "options lock after answering")
    st = pg.evaluate("() => JSON.parse(localStorage.getItem('ew-state')||'{}')")
    ok(len(st.get("items", {})) == 1, "the answer is written to the saved record")
    one = list(st["items"].values())[0]
    ok("due" in one and "b" in one, "a question gets a box and a next-due day")
    pg.reload(); pg.wait_for_selector("article.q")
    ok(pg.locator("article.q .chip", has_text="seen 1").count() == 1, "the card remembers it has been seen")
    pg.select_option("#fl", "Easy"); easy = pg.locator("article.q").count()
    ok(easy == sum(1 for r in core["bank"]["rows"] if r[1] == t and r[4] == "Easy") or easy == 0, "level filter matches core.json")
    # ---- review: one at a time --------------------------------------------------------------
    go(pg, "#/review/weak", "article.q")
    ok(pg.locator("article.q").count() == 1, "review shows one question at a time")
    ok("1 of" in pg.inner_text(".qnum").lower(), "review counts the questions in the set")
    pg.locator(".opt").nth(0).click()
    pg.wait_for_selector(".reveal .btn")
    ok(pg.locator(".reveal .btn").count() == 1, "a next button appears after answering")
    pg.locator(".reveal .btn").click(); pg.wait_for_selector(".qnum:has-text('2 of')")
    ok(pg.locator("article.q").count() == 1, "next moves to a single new question")
    go(pg, "#/review", "h2")
    ok(pg.locator("article.q").count() >= 1 or pg.locator(".empty").count() == 1, "the due queue renders")
    # ---- mock -------------------------------------------------------------------------------
    go(pg, "#/mock", "table.t")
    ok(sum(bp["mock"].values()) == bp["perPaper"], "the mock mix adds up to a full paper")
    ok(pg.locator("table.t tbody tr").count() == len(bp["mock"]), "the mock mix is shown by format")
    go(pg, "#/mock/go", "#clock")
    ok(pg.locator("article.q").count() == bp["perPaper"], "the mock paper has one question per blueprint slot")
    ok(":" in pg.inner_text("#clock"), "the clock is running")
    pg.locator("article.q").first.locator(".opt").nth(0).click()
    ok(pg.locator(".opt.picked").count() == 1, "an answer is marked but not graded during the paper")
    ok(pg.locator(".reveal:visible").count() == 0, "no explanation is shown during the paper")
    pg.click("#sub"); pg.wait_for_selector(".big")
    ok("/" in pg.inner_text(".big"), "submitting shows a score out of the paper total")
    ok(pg.locator(".reveal:visible").count() == bp["perPaper"], "every question is explained after submitting")
    mk = pg.evaluate("() => (JSON.parse(localStorage.getItem('ew-state')||'{}').mocks||[]).length")
    ok(mk == 1, "the paper is saved to the record")
    # ---- drill ------------------------------------------------------------------------------
    go(pg, "#/drill", "#cnt"); pg.wait_for_selector("article.q")
    ok(pg.locator("article.q").count() == min(10, len(core["bank"]["rows"])), "drill shows up to ten")
    pg.select_option("#ft", built[-1]); ok(pg.locator("article.q").count() >= 1, "topic filter works")
    go(pg, "#/drill/rc", "#cnt")
    ok(pg.eval_on_selector("#ff", "e => e.value") == "rc", "a format link preselects that format")
    # ---- words, daily, sources --------------------------------------------------------------
    go(pg, "#/words", ".card.lex")
    ok(pg.locator(".card.lex").count() == len(lex), "word bank lists every entry")
    pg.fill("#ws", "benevolent"); ok(pg.locator(".card.lex").count() >= 1, "word search finds benevolent")
    go(pg, "#/daily", "h2")
    ok(pg.locator(".card").count() == len(core["days"]) or len(core["days"]) == 0 and pg.locator(".empty").count() == 1, "daily list matches core.json")
    if core["days"]:
        go(pg, f"#/daily/{core['days'][0]['date']}", "article.q")
        ok(pg.locator("article.q").count() == core["days"][0]["questions"], "a day shows all its questions")
    go(pg, "#/sources", "h2")
    ok(pg.locator(".card").count() >= len(core["papers"]) + len(core["days"]), "sources lists every paper and day")
    # ---- phone width: no sideways scroll ----------------------------------------------------
    pg.set_viewport_size({"width": 360, "height": 740})
    for h in ("#/", f"#/topic/{built[0]}", "#/mock/go"):
        go(pg, h, ".tile, article.q, #clock")
        ok(pg.evaluate("() => document.documentElement.scrollWidth <= window.innerWidth"), f"no horizontal scroll at 360px on {h}")
    b.close()
ok(not errors, "no console errors" + (": " + "; ".join(errors[:3]) if errors else ""))
srv.shutdown()
sys.exit(1 if fails else 0)
