"""Conjunctions: correlative pairs and relative 'when'. Quiz tier: 3 past questions plus practice."""
from bank import mistake, ruled_out, q

TOPIC = "conjunctions"
TIER = "quiz"
PREFIX = "cj"

NODES = {
    "q-cj-correlative": {"short": "Pairs", "label": "Paired conjunctions", "kind": "qtype", "parent": TOPIC, "order": 1,
                         "summary": "No sooner ... than, neither ... nor, either ... or, hardly ... when, not only ... but also: each pair has fixed partners.", "links": []},
    "q-cj-relative": {"short": "when / where", "label": "Relative 'when' after a time noun", "kind": "qtype", "parent": TOPIC, "order": 2,
                      "summary": "After a noun of time (Monday, the day), when begins a clause giving more detail.", "links": []},
}

RULES = [
    {"id": "cj-r1", "node": "q-cj-correlative", "text": "Pairs are fixed: no sooner ... than; hardly / scarcely ... when (or before); neither ... nor; either ... or; not only ... but also; whether ... or. 'No sooner ... when' and 'neither ... or' are wrong. After 'no sooner' the auxiliary comes first: No sooner had I arrived than ...",
     "ok": "No sooner had I arrived than the train left. Neither he nor she knew.", "bad": "No sooner had I arrived when the train left. Neither he or she knew."},
    {"id": "cj-r2", "node": "q-cj-relative", "text": "After a time noun ('on Monday', 'in May', 'the day'), 'when' links a clause to it: The committee meets on Monday, when the final decision will be announced. Whereupon means 'immediately after which' and is not a time link.",
     "ok": "We meet on Monday, when the plan will be shared.", "bad": "We meet on Monday, whereupon the plan will be shared (changes the sense)."},
]

METHODS = {
    "q-cj-correlative": {"cue": "'No sooner', 'neither', 'hardly' or 'either' at the start; the partner conjunction is the blank or the highlighted part.",
                         "standard": "Name the first half of the pair, then recall its fixed partner.",
                         "fast": "No sooner = than. Neither = nor. Either = or. Hardly = when.",
                         "eliminate": "Drop options that give the wrong partner (or after neither, when after no sooner, then for than).",
                         "traps": ["'Then' for 'than' (spelling lookalike).", "'Or' after 'neither'.", "Extra auxiliary after 'nor' ('nor did') when the subject follows directly."],
                         "rules": ["cj-r1"], "tech": ["connectors"]},
    "q-cj-relative": {"cue": "A date or time noun followed by a comma and a blank before a clause.",
                      "standard": "Test each option in the sentence: the blank must link a clause back to the time noun.",
                      "fast": "Time noun + comma + blank = when.",
                      "eliminate": "Drop ungrammatical options (at then) and options that change the meaning.",
                      "traps": ["Whereupon looks formal and clever but has a different sense.", "'On which' is possible but would need the noun 'day'."],
                      "rules": ["cj-r2"], "tech": ["connectors"]},
}

REFS = []
S2 = "2025-09-12-S2"
_SEL = "Select the correct option to fill in the blank.\n"
_IMP = "Choose the most suitable option to replace the highlighted part of the sentence:\n"

PYQS = [
    q("q-cj-correlative", "improve", _IMP + "No sooner had I arrived at the platform [[when the train left]].",
      ["than the train left", "then the train left", "when the train had left", "than did the train leave"], "a",
      "'No sooner' pairs with 'than', so the clause is 'than the train left'.",
      {"b": mistake("'Then' is a time word that looks like 'than'; the pair needs 'than'."),
       "c": mistake("'When' is the partner of 'hardly' and 'scarcely', not of 'no sooner', and the tense is shifted too."),
       "d": mistake("'Than' is right, but the extra 'did ... leave' inversion is not needed after the first clause already has the inversion.")},
      rules=["cj-r1"], paper=S2, qno=78, tech=["connectors"], trick="No sooner ... than."),
    q("q-cj-relative", "fill", _SEL + "The committee meets on Monday, ___ the final decision will be announced.",
      ["whereupon", "at then", "when", "on which"], "c",
      "After the time noun 'Monday', 'when' links the clause about the decision.",
      {"a": mistake("'Whereupon' means 'immediately after which', which describes a sequence and not the day itself."),
       "b": ruled_out("'At then' is not a correct English phrase."),
       "d": mistake("'On which' is possible only with a noun like 'day' ('on which day'); here it leaves 'Monday' without a link.")},
      rules=["cj-r2"], paper=S2, qno=86, rare=True, tech=["connectors"], trick="Time noun + comma = when.",
      caution="'On which' can be defended in formal writing. The key 'when' is the natural relative adverb after a time noun."),
    q("q-cj-correlative", "fill", _SEL + "Neither the project lead ___ the team members were prepared for the audit.",
      ["or", "nor", "either", "nor did"], "b",
      "'Neither' pairs with 'nor': neither the lead nor the team members. The verb agrees with the nearer subject (members, plural).",
      {"a": mistake("'Neither ... or' is a common error; the partner is 'nor'."),
       "c": ruled_out("'Either' is the start of the pair either ... or and cannot partner 'neither'."),
       "d": mistake("'Nor did' adds an auxiliary and inverts the sentence, which the following 'were prepared' does not allow.")},
      rules=["cj-r1"], paper=S2, qno=90, tech=["connectors"], trick="Neither -> nor."),
]


def practice_items():
    return [
        q("q-cj-correlative", "fill", _SEL + "Hardly had the show begun ___ the lights went out.",
          ["than", "when", "then", "or"], "b",
          "'Hardly' pairs with 'when' (or 'before').",
          {"a": mistake("'Than' is the partner of 'no sooner', not of 'hardly'."), "c": ruled_out("'Then' is a time word, not a conjunction."), "d": ruled_out("'Or' is not a partner of 'hardly'.")},
          rules=["cj-r1"], uid="cj-p01"),
        q("q-cj-correlative", "fill", _SEL + "She is not only intelligent ___ also hardworking.",
          ["and", "but", "so", "or"], "b",
          "'Not only' pairs with 'but also'.",
          {"a": ruled_out("'Not only ... and also' is not the fixed pair."), "c": ruled_out("'So' does not complete the pair."), "d": ruled_out("'Or' does not complete the pair.")},
          rules=["cj-r1"], uid="cj-p02"),
        q("q-cj-correlative", "fill", _SEL + "You can either call me ___ send a message.",
          ["nor", "or", "than", "but"], "b",
          "'Either' pairs with 'or'.",
          {"a": mistake("'Nor' belongs with 'neither'."), "c": ruled_out("'Than' is used in comparisons."), "d": ruled_out("'But' does not complete 'either'.")},
          rules=["cj-r1"], uid="cj-p03"),
        q("q-cj-relative", "fill", _SEL + "The festival begins in October, ___ the weather turns pleasant.",
          ["where", "when", "which", "why"], "b",
          "After the time noun 'October', 'when' links the clause.",
          {"a": mistake("'Where' links a place, but October is a time."), "c": ruled_out("'Which' would need a following verb and does not fit the sentence."), "d": ruled_out("'Why' links a reason.")},
          rules=["cj-r2"], uid="cj-p04", rare=True),
    ]
