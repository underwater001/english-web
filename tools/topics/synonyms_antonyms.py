"""Synonyms & antonyms. Seed tier: practice only until a paper is filed.
Every answer is checked against WORDS: the key is in the word's list, no wrong option is."""
from bank import mistake, ruled_out, q, word

TOPIC = "synonyms-antonyms"
TIER = "seed"
PREFIX = "sa"

NODES = {
    "q-syn": {"short": "Synonym", "label": "Closest in meaning", "kind": "qtype", "parent": TOPIC, "order": 1,
              "summary": "One capitalised word; pick the option closest in meaning.", "links": []},
    "q-ant": {"short": "Antonym", "label": "Opposite in meaning", "kind": "qtype", "parent": TOPIC, "order": 2,
              "summary": "One capitalised word; pick the option opposite in meaning.", "links": []},
}

RULES = [
    {"id": "sa-r1", "node": "q-syn", "text": "A word is positive, negative or neutral in tone. Its synonyms share the tone, so options of the opposite tone can be dropped at once.",
     "ok": "BENEVOLENT (positive): charitable, kindly.", "bad": "BENEVOLENT: malicious (negative) cannot be a synonym."},
    {"id": "sa-r2", "node": "q-ant", "text": "In an antonym question the word's synonym is almost always one of the options as a trap. Find the meaning first, then choose the opposite, not the same.",
     "ok": "SCARCE: plentiful is the opposite.", "bad": "SCARCE: rare means the same, so it is the trap."},
]

METHODS = {
    "q-syn": {"cue": "'Select the most appropriate synonym of the word' with one capitalised word.",
              "standard": "Recall the meaning, then pick the option that could replace the word in a sentence without changing it.",
              "fast": "Decide positive or negative first, drop options of the other tone, then choose among the rest.",
              "eliminate": "An antonym is usually among the options, so drop the option that opposes the word before comparing the others.",
              "traps": ["The antonym is almost always listed.", "A word that merely fits the same topic is not a synonym."],
              "rules": ["sa-r1"], "tech": ["tone", "opposite-trap"]},
    "q-ant": {"cue": "'Select the most appropriate antonym of the word' with one capitalised word.",
              "standard": "Recall the meaning, then pick the option that says the reverse.",
              "fast": "Spot and ignore the synonym trap, then pick the option of the opposite tone.",
              "eliminate": "Cross out every option that is close in meaning to the word. What remains contains the answer.",
              "traps": ["The synonym is nearly always listed as bait.", "An unrelated word is not an antonym: the answer must reverse the meaning."],
              "rules": ["sa-r2"], "tech": ["tone", "opposite-trap"]},
}

REFS = []

WORDS = [
    word("benevolent", "benevolent", "word", "Kind and generous towards others.", pos="adj", syn=["charitable", "kindly", "generous", "humane"], ant=["malicious", "malevolent", "cruel", "stingy"],
         ex="The benevolent landlord waived the rent for families who had lost their jobs."),
    word("frugal", "frugal", "word", "Careful with money and resources; not wasteful.", pos="adj", syn=["thrifty", "economical", "sparing"], ant=["lavish", "extravagant", "wasteful"],
         ex="She led a frugal life and saved half of every salary."),
    word("obsolete", "obsolete", "word", "No longer in use because something newer has replaced it.", pos="adj", syn=["outdated", "outmoded", "archaic"], ant=["modern", "current", "contemporary"],
         ex="Film cameras became obsolete once digital ones arrived."),
    word("verbose", "verbose", "word", "Using more words than are needed.", pos="adj", syn=["wordy", "long-winded", "prolix"], ant=["concise", "terse", "succinct"],
         ex="His verbose reply took ten minutes to say what a sentence could have said."),
    word("scarce", "scarce", "word", "Not available in enough quantity.", pos="adj", syn=["rare", "meagre", "sparse", "insufficient"], ant=["plentiful", "abundant", "ample"],
         ex="Clean water is scarce in the region during summer."),
    word("ephemeral", "ephemeral", "word", "Lasting for a very short time.", pos="adj", syn=["fleeting", "transient", "short-lived", "brief"], ant=["eternal", "permanent", "enduring"],
         ex="The ephemeral beauty of the cherry blossom lasts about a week."),
    word("diligent", "diligent", "word", "Showing steady, careful effort in work.", pos="adj", syn=["industrious", "hardworking", "assiduous"], ant=["lazy", "indolent", "negligent"],
         ex="A diligent student, she revised every lesson on the day it was taught."),
    word("candid", "candid", "word", "Truthful and straightforward, even when it is uncomfortable.", pos="adj", syn=["frank", "honest", "forthright", "open"], ant=["devious", "evasive", "secretive"],
         ex="He gave a candid account of what had gone wrong with the project."),
]


def practice_items():
    return [
        q("q-syn", "synonym", "Select the most appropriate synonym of the given word.\nBENEVOLENT",
          ["Malicious", "Charitable", "Reluctant", "Stingy"], "b",
          "Benevolent means kind and generous; charitable carries the same positive sense.",
          {"a": mistake("Malicious means wishing to harm: the opposite of benevolent, chosen by mistake when the tone is not checked."),
           "c": ruled_out("Reluctant means unwilling; it says nothing about kindness or generosity."),
           "d": mistake("Stingy means unwilling to give: it opposes benevolent, a classic antonym trap.")},
          lex=("syn", "benevolent"), uid="sa-p01", tech=["tone", "opposite-trap"], rules=["sa-r1"]),
        q("q-syn", "synonym", "Select the most appropriate synonym of the given word.\nFRUGAL",
          ["Thrifty", "Lavish", "Greedy", "Cheerful"], "a",
          "Frugal means careful with money; thrifty says the same thing.",
          {"b": mistake("Lavish means spending freely: the antonym of frugal, placed as bait."),
           "c": ruled_out("Greedy means wanting more than one needs; a frugal person is careful, not greedy."),
           "d": ruled_out("Cheerful describes mood, not the way a person spends money.")},
          lex=("syn", "frugal"), uid="sa-p02", tech=["tone", "opposite-trap"], rules=["sa-r1"]),
        q("q-syn", "synonym", "Select the most appropriate synonym of the given word.\nOBSOLETE",
          ["Modern", "Outdated", "Fragile", "Permanent"], "b",
          "Obsolete means no longer used because something newer has replaced it; outdated means the same.",
          {"a": mistake("Modern is the antonym of obsolete, chosen when the word is mixed up with its opposite."),
           "c": ruled_out("Fragile means easily broken and has no link to being out of use."),
           "d": ruled_out("Permanent means lasting for ever, which does not describe something that has gone out of use.")},
          lex=("syn", "obsolete"), uid="sa-p03", rules=["sa-r1"]),
        q("q-syn", "synonym", "Select the most appropriate synonym of the given word.\nVERBOSE",
          ["Concise", "Silent", "Wordy", "Humorous"], "c",
          "Verbose means using more words than needed; wordy is the direct synonym.",
          {"a": mistake("Concise is the antonym of verbose: it means brief and to the point."),
           "b": ruled_out("Silent means making no sound, the reverse of using many words."),
           "d": ruled_out("Humorous means funny; a verbose speaker need not be funny.")},
          lex=("syn", "verbose"), uid="sa-p04", rare=True, rules=["sa-r1"]),
        q("q-ant", "antonym", "Select the most appropriate antonym of the given word.\nSCARCE",
          ["Rare", "Plentiful", "Limited", "Meagre"], "b",
          "Scarce means not available in enough quantity; plentiful means available in large quantity.",
          {"a": mistake("Rare is a synonym of scarce, which is why it is placed as the trap."),
           "c": mistake("Limited is close in meaning to scarce, so it is a synonym-side trap, not the opposite."),
           "d": mistake("Meagre means small in amount, the same side as scarce.")},
          lex=("ant", "scarce"), uid="sa-p05", tech=["opposite-trap"], rules=["sa-r2"]),
        q("q-ant", "antonym", "Select the most appropriate antonym of the given word.\nEPHEMERAL",
          ["Fleeting", "Transient", "Eternal", "Brief"], "c",
          "Ephemeral means lasting a very short time; eternal means lasting for ever.",
          {"a": mistake("Fleeting is a synonym of ephemeral."),
           "b": mistake("Transient is a synonym of ephemeral."),
           "d": mistake("Brief is a synonym of ephemeral: it describes the same short duration.")},
          lex=("ant", "ephemeral"), uid="sa-p06", rare=True, tech=["opposite-trap"], rules=["sa-r2"]),
        q("q-ant", "antonym", "Select the most appropriate antonym of the given word.\nDILIGENT",
          ["Industrious", "Lazy", "Careful", "Eager"], "b",
          "Diligent means steadily hardworking; lazy means unwilling to work.",
          {"a": mistake("Industrious is a synonym of diligent."),
           "c": ruled_out("Careful describes attention to detail and is closer to diligent than to its opposite."),
           "d": ruled_out("Eager means keen; it is not the opposite of working steadily.")},
          lex=("ant", "diligent"), uid="sa-p07", tech=["opposite-trap"], rules=["sa-r2"]),
        q("q-ant", "antonym", "Select the most appropriate antonym of the given word.\nCANDID",
          ["Frank", "Honest", "Devious", "Open"], "c",
          "Candid means truthful and straightforward; devious means using indirect or dishonest means.",
          {"a": mistake("Frank is a synonym of candid."),
           "b": mistake("Honest is a synonym of candid."),
           "d": mistake("Open is a synonym of candid in the sense of being straightforward.")},
          lex=("ant", "candid"), uid="sa-p08", tech=["opposite-trap"], rules=["sa-r2"]),
    ]


PYQS = []
