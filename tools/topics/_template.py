"""TEMPLATE for a new topic. Copy to tools/topics/<topic_with_underscores>.py, fill it in, then run python3 tools/check.py.
The topic must already exist as a node in data/tree.json (kind "topic"). Files starting with _ are ignored by the build.
See README.md ("Adding material", "Tiers") and look at synonyms_antonyms.py or subject_verb_agreement.py for finished examples.
"""
from bank import mistake, ruled_out, q, word

TOPIC = "topic-id-from-tree-json"
TIER = "seed"      # "seed": practice only (2+ per type). "quiz": needs a past question. "full": quiz + 3+ practice per type.
PREFIX = "xx"      # practice ids xx-p01, xx-p02 ... (only ever append)

NODES = {   # question types hang off the topic
    "q-xx-type": {"short": "Type", "label": "Question type", "kind": "qtype", "parent": TOPIC, "order": 1, "summary": "One sentence.", "links": []},
}
RULES = [   # the grammar rule or vocabulary tip behind a type; ok/bad are one right and one wrong example (give both or neither)
    {"id": "xx-r1", "node": "q-xx-type", "text": "The rule in one or two sentences.", "ok": "A correct example.", "bad": "An incorrect example."},
]
METHODS = {  # every type needs all five keys; traps is a list
    "q-xx-type": {"cue": "The wording that tells you this is the type.", "standard": "...", "fast": "...", "eliminate": "...", "traps": ["..."],
                  "rules": ["xx-r1"], "tech": ["read-whole"]},
}
REFS = []    # [{"title": "...", "url": "...", "note": "what the page says, in your own words"}]
WORDS = [    # word(id, w, kind, meaning, syn=[...], ant=[...], ex="your own sentence containing the word")
]

PYQS = [     # q(type, fmt, text, options, key, why, wrong, rules=[...], paper="<paper id>", qno=<n>)
]


def practice_items():
    return [
        # q("q-xx-type", "fill", "Select the most appropriate option to fill in the blank.\nHe ___ to school.", ["go", "goes", "going", "gone"], "b",
        #   "A singular subject takes goes.", {"a": mistake("Base form with a singular subject."), "c": ruled_out("Going needs an auxiliary."), "d": ruled_out("Gone needs an auxiliary.")},
        #   rules=["xx-r1"], uid="xx-p01"),
    ]
