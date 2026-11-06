"""Adjectives & adverbs: comparison words and degree adverbs. Quiz tier: 3 past questions plus practice."""
from bank import mistake, ruled_out, q

TOPIC = "adjectives-adverbs"
TIER = "quiz"
PREFIX = "aa"

NODES = {
    "q-aa-comparison": {"short": "more / less ... than", "label": "Comparison with 'than'", "kind": "qtype", "parent": TOPIC, "order": 1,
                        "summary": "Choose more or less by the contrast in the sentence; 'more than' can also mean 'beyond'.", "links": []},
    "q-aa-degree": {"short": "Degree adverbs", "label": "Barely, hardly, merely, scarcely", "kind": "qtype", "parent": TOPIC, "order": 2,
                    "summary": "Barely, hardly and scarcely mean 'only just'; merely means 'only'. Choose by sense.", "links": []},
}

RULES = [
    {"id": "aa-r1", "node": "q-aa-comparison", "text": "A contrast word (even though, although, but) tells you which way the comparison goes. If something 'looked workable' but was hard in practice, it was MORE complicated than expected, not less.",
     "ok": "Though it looked simple, it was more complicated than expected.", "bad": "Though it looked simple, it was less complicated than expected."},
    {"id": "aa-r2", "node": "q-aa-comparison", "text": "'More than + adjective' means 'beyond that': more than impressive = better than impressive. 'Other than' means 'different from', and 'rather than' needs a different pattern.",
     "ok": "Her analysis was more than impressive.", "bad": "Her analysis was other than impressive (= not impressive)."},
    {"id": "aa-r3", "node": "q-aa-degree", "text": "Barely, scarcely and hardly all mean 'only just' (and are nearly negative); merely means 'only'; 'all but' means 'almost'. A sentence about falling behind needs 'barely / scarcely / hardly'.",
     "ok": "Its systems could barely keep up.", "bad": "Its systems could merely keep up."},
]

METHODS = {
    "q-aa-comparison": {"cue": "A blank before 'complicated / impressive / ...' followed by 'than'.",
                        "standard": "Read the contrast in the sentence (workable on paper, nearly revelatory) and decide whether the second part is more or less.",
                        "fast": "If the clue says 'even though it looked X', the real result is the opposite of X.",
                        "eliminate": "Drop 'much' and 'rather', which do not fit before 'than' in this way.",
                        "traps": ["Choosing 'less' because the plan 'looked workable'.", "'Much' and 'rather' sound natural but break the pattern with 'than'."],
                        "rules": ["aa-r1", "aa-r2"], "tech": ["context-clue"]},
    "q-aa-degree": {"cue": "'could ___ keep up / afford / hear', where the blank is a degree adverb.",
                    "standard": "Ask whether the sentence says 'only just' (barely, scarcely, hardly) or 'only' (merely).",
                    "fast": "Fell behind or hardly managed = barely.",
                    "eliminate": "Drop 'merely' (only) and 'all but' (almost).",
                    "traps": ["Two options can be near-synonyms (barely, scarcely).", "Merely sounds neutral but changes the meaning to 'only'."],
                    "rules": ["aa-r3"], "tech": ["back-substitute"]},
}

REFS = []
S1, S3 = "2025-09-12-S1", "2025-09-12-S3"
_SEL = "Select the correct option to fill in the blank.\n"

PYQS = [
    q("q-aa-degree", "fill", _SEL + "The company expanded so quickly that its systems could ___ keep up.",
      ["barely", "merely", "scarcely", "all but"], "a",
      "The systems fell behind the quick expansion, so they could 'only just' keep up: barely.",
      {"b": mistake("'Merely' means only; it does not say the systems struggled."),
       "c": mistake("'Scarcely' also means only just and gives the same sense here; it is the closest rival to the key."),
       "d": ruled_out("'All but keep up' means 'almost keep up' and breaks the pattern 'could ___ keep up'.")},
      rules=["aa-r3"], paper=S1, qno=79, tech=["back-substitute"],
      caution="'Scarcely' fits just as well as 'barely' here. If an exam gives both, look for any other difference (usage or register); in this paper the printed key is 'barely'."),
    q("q-aa-comparison", "fill", _SEL + "Even though the plan looked workable on paper, executing it turned out to be ___ complicated than expected.",
      ["less", "more", "much", "rather"], "b",
      "'Even though it looked workable' sets up a contrast: the real work was more complicated than expected.",
      {"a": mistake("'Less complicated than expected' would not be a contrast with 'looked workable'; it would repeat it."),
       "c": ruled_out("'Much' would need 'much more' before 'than'."),
       "d": ruled_out("'Rather complicated than expected' does not form a comparison with 'than'.")},
      rules=["aa-r1"], paper=S1, qno=96, tech=["context-clue"], trick="Even though X looked easy, it was MORE hard."),
    q("q-aa-comparison", "fill", _SEL + "Her analysis was ___ than impressive; it was nearly revelatory.",
      ["less", "more", "other", "rather"], "b",
      "'More than impressive' means beyond impressive, which fits 'nearly revelatory'.",
      {"a": mistake("'Less than impressive' means not impressive, which clashes with 'nearly revelatory'."),
       "c": mistake("'Other than impressive' means different from impressive, which would mean not impressive."),
       "d": ruled_out("'Rather than impressive' is not a comparison of degree.")},
      rules=["aa-r2"], paper=S3, qno=97, tech=["context-clue"], trick="More than = beyond."),
]


def practice_items():
    return [
        q("q-aa-comparison", "fill", _SEL + "The task looked easy, but doing it was ___ difficult than we had imagined.",
          ["less", "more", "much", "rather"], "b",
          "'Looked easy, but' signals the opposite: more difficult than imagined.",
          {"a": mistake("'Less difficult' would repeat the idea of 'easy' rather than contrast with it."), "c": ruled_out("'Much' needs 'more' to make a comparison with 'than'."), "d": ruled_out("'Rather' cannot be used with 'than' to compare the degree here.")},
          rules=["aa-r1"], uid="aa-p01"),
        q("q-aa-degree", "fill", _SEL + "The old man was so tired that he could ___ lift his bag.",
          ["merely", "barely", "all but", "just as"], "b",
          "So tired that he could 'only just' lift it: barely.",
          {"a": mistake("'Merely' means only and drops the sense of struggle."), "c": ruled_out("'All but' means almost and cannot sit between 'could' and the verb."), "d": ruled_out("'Just as' begins a comparison; it is not a degree adverb here.")},
          rules=["aa-r3"], uid="aa-p02"),
        q("q-aa-comparison", "fill", _SEL + "Her answer was ___ than correct; it was brilliant.",
          ["more", "less", "other", "rather"], "a",
          "'More than correct' means beyond correct, which suits 'brilliant'.",
          {"b": mistake("'Less than correct' means not quite correct, which clashes with 'brilliant'."), "c": mistake("'Other than correct' means not correct."), "d": ruled_out("'Rather than correct' is not a degree comparison.")},
          rules=["aa-r2"], uid="aa-p03", rare=True),
    ]
