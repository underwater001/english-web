"""One-word substitution. Seed tier. Each answer is checked against the phrase stored in WORDS."""
from bank import mistake, ruled_out, q, word

TOPIC = "one-word-substitution"
TIER = "seed"
PREFIX = "ow"

NODES = {
    "q-ows": {"short": "One word", "label": "One word for a phrase", "kind": "qtype", "parent": TOPIC, "order": 1,
              "summary": "A phrase is given; pick the single word that means the same.", "links": []},
}

RULES = [
    {"id": "ow-r1", "node": "q-ows", "text": "Many one-word substitutions are built from a Greek or Latin root: phobia (fear), phile (lover), mis(o) (hate), anthropo (mankind). Match the root to the phrase.",
     "ok": "Bibliophile: biblio (book) + phile (lover) = lover of books.", "bad": "Bibliophobe is not the word for a lover of books; phobe means one who fears."},
]

METHODS = {
    "q-ows": {"cue": "'Select the word that can be used as a substitute for the given group of words.'",
              "standard": "Know the word, or break it into root parts and match them to the phrase.",
              "fast": "Split each option into its root, discard the roots that do not match the phrase.",
              "eliminate": "The wrong options are usually real words with a neighbouring meaning (hater instead of lover), so match both halves of the root.",
              "traps": ["A word with the right root but the opposite sense (phile vs phobe).", "A word that sounds similar but belongs to another phrase."],
              "rules": ["ow-r1"], "tech": ["root-prefix"]},
}

REFS = []

WORDS = [
    word("omniscient", "omniscient", "ows", "One who knows everything", ex="Nobody is omniscient, so even experts should ask questions."),
    word("philanthropist", "philanthropist", "ows", "One who loves mankind and helps others", ex="The philanthropist funded three new libraries."),
    word("misanthrope", "misanthrope", "ows", "One who hates mankind", ex="After the betrayal he became a misanthrope and avoided everyone."),
    word("bibliophile", "bibliophile", "ows", "A lover of books", ex="Every wall of the bibliophile's house is lined with shelves."),
    word("somnambulist", "somnambulist", "ows", "One who walks in sleep", ex="The somnambulist woke up in the garden at dawn."),
    word("illegible", "illegible", "ows", "That which cannot be read", ex="His handwriting was so illegible that nobody could read the note."),
]


def practice_items():
    return [
        q("q-ows", "ows", "Select the word that can be used as a substitute for the given group of words.\nOne who knows everything",
          ["Omnipotent", "Omniscient", "Omnipresent", "Philanthropist"], "b",
          "Omniscient is built from omni (all) and scient (knowing): one who knows everything.",
          {"a": mistake("Omnipotent means all-powerful: it shares the root omni but not the sense of knowing."),
           "c": mistake("Omnipresent means present everywhere, not knowing everything."),
           "d": ruled_out("A philanthropist is a person who loves mankind and helps others.")},
          lex=("ows", "omniscient"), uid="ow-p01", rules=["ow-r1"], tech=["root-prefix"]),
        q("q-ows", "ows", "Select the word that can be used as a substitute for the given group of words.\nOne who hates mankind",
          ["Philanthropist", "Bibliophile", "Misanthrope", "Somnambulist"], "c",
          "Misanthrope joins miso (hate) and anthropos (man): one who hates mankind.",
          {"a": mistake("Philanthropist has the same anthropo root but phil means love, so it is the opposite sense."),
           "b": ruled_out("A bibliophile is a lover of books."),
           "d": ruled_out("A somnambulist is one who walks in sleep.")},
          lex=("ows", "misanthrope"), uid="ow-p02", rules=["ow-r1"], tech=["root-prefix"]),
        q("q-ows", "ows", "Select the word that can be used as a substitute for the given group of words.\nA lover of books",
          ["Bibliophile", "Misanthrope", "Illegible", "Omniscient"], "a",
          "Bibliophile joins biblio (book) and phile (lover).",
          {"b": ruled_out("A misanthrope hates mankind; it has nothing to do with books."),
           "c": ruled_out("Illegible describes writing that cannot be read; it is an adjective, not a person."),
           "d": ruled_out("Omniscient means knowing everything, not loving books.")},
          lex=("ows", "bibliophile"), uid="ow-p03", rules=["ow-r1"], tech=["root-prefix"]),
        q("q-ows", "ows", "Select the word that can be used as a substitute for the given group of words.\nOne who walks in sleep",
          ["Bibliophile", "Philanthropist", "Illegible", "Somnambulist"], "d",
          "Somnambulist comes from somnus (sleep) and ambulare (walk).",
          {"a": ruled_out("A bibliophile is a lover of books."),
           "b": ruled_out("A philanthropist loves mankind and helps others."),
           "c": ruled_out("Illegible means that which cannot be read.")},
          lex=("ows", "somnambulist"), uid="ow-p04", rules=["ow-r1"], tech=["root-prefix"]),
    ]


PYQS = []
