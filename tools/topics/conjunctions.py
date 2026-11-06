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
    "q-cj-placement": {"short": "Where the pair sits", "label": "Not only / but also right before the matching words", "kind": "qtype", "parent": TOPIC, "order": 3,
                          "summary": "Each half of a correlative pair (not only, but also, both, and) must sit directly before the word or phrase it is matching, not scattered earlier in the sentence.", "links": []},
    "q-cj-redundant": {"short": "No double joiner", "label": "If...then, since...so are one joiner too many", "kind": "qtype", "parent": TOPIC, "order": 4,
                          "summary": "If/when, since/as/because and although already join the two clauses, so adding then/so/therefore/yet as well repeats the same job and is dropped.", "links": []},
}

RULES = [
    {"id": "cj-r1", "node": "q-cj-correlative", "text": "Pairs are fixed: no sooner ... than; hardly / scarcely ... when (or before); neither ... nor; either ... or; not only ... but also; whether ... or. 'No sooner ... when' and 'neither ... or' are wrong. After 'no sooner' the auxiliary comes first: No sooner had I arrived than ...",
     "ok": "No sooner had I arrived than the train left. Neither he nor she knew.", "bad": "No sooner had I arrived when the train left. Neither he or she knew."},
    {"id": "cj-r2", "node": "q-cj-relative", "text": "After a time noun ('on Monday', 'in May', 'the day'), 'when' links a clause to it: The committee meets on Monday, when the final decision will be announced. Whereupon means 'immediately after which' and is not a time link.",
     "ok": "We meet on Monday, when the plan will be shared.", "bad": "We meet on Monday, whereupon the plan will be shared (changes the sense)."},
    {"id": "cj-r3", "node": "q-cj-placement", "text": "Each half of a correlative pair (not only/but also, both/and, either/or, neither/nor) must come directly before the exact word, phrase or clause it is matching, so that the same kind of thing follows each half. Moving one half earlier in the sentence breaks the parallel.",
     "ok": "He cheated not only his friends but also his parents.", "bad": "Not only he cheated his friends but also his parents (the first half sits before the whole clause, the second only before 'his parents')."},
    {"id": "cj-r4", "node": "q-cj-redundant", "text": "If/when, since/as/because and although already join two clauses by themselves, so a second linking word (then, so, therefore, yet) in the other clause repeats the same job and is dropped.",
     "ok": "Since I was ill, I could not come.", "bad": "Since I was ill, so I could not come."},
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
    "q-cj-placement": {"cue": "'Not only', 'both' or 'either' placed well before the verb, with its partner later in the sentence.",
                          "standard": "Find the two things actually being paired (two objects, two verbs, two clauses) and move each half of the correlative to sit directly before its own matching item.",
                          "fast": "Not only X but also Y: X and Y must be the same kind of thing, each immediately after its own half of the pair.",
                          "eliminate": "Drop any option where one half sits before the whole clause while the other sits before just a word.",
                          "traps": ["'Not only' placed at the very start of the sentence out of habit, even when it is matching only one object deep inside the clause."],
                          "rules": ["cj-r3"], "tech": ["connectors"]},
    "q-cj-redundant": {"cue": "if/when, since/as/because or although in one clause, and then/so/therefore/yet appearing again in the other.",
                          "standard": "Check whether the first clause already has its own linking word; if so, delete the second one instead of keeping both.",
                          "fast": "since ... so = one joiner too many; drop 'so'.",
                          "eliminate": "Drop every option that keeps both linking words.",
                          "traps": ["Each joiner looks correct on its own, so the error is easy to miss unless both clauses are checked together."],
                          "rules": ["cj-r4"], "tech": ["connectors"]},
}

REFS = []
S2 = "2025-09-12-S2"
_SEL = "Select the correct option to fill in the blank.\n"
_IMP = "Choose the most suitable option to replace the highlighted part of the sentence:\n"
_S = "Find the part of the sentence that contains an error:\n"
_I = _IMP

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
        q("q-cj-placement", "spot-error", _S + "Not only he / wasted his own time / but also / disturbed his classmates.",
          ["Not only he", "wasted his own time", "but also", "disturbed his classmates."], "a",
          "'Not only' is matching 'wasted his own time' with 'disturbed his classmates', not the subject 'he'; it should read 'He not only wasted ... but also disturbed ...'.",
          {"b": ruled_out("A correct verb phrase, once 'not only' is moved after 'he'."), "c": ruled_out("'But also' is correctly placed right before the second matching verb."),
           "d": ruled_out("A correct closing verb phrase.")},
          rules=["cj-r3"], uid="cj-p05", tech=["connectors"]),
        q("q-cj-placement", "improve", _I + "[[Not only she sings well]] but also dances gracefully.",
          ["She not only sings well", "Not only she sings well", "She is not only sings well", "Not only does she sing well"], "a",
          "'Not only' must sit right before the first matching verb ('sings'), not before the subject 'she': She not only sings well but also dances gracefully.",
          {"b": ruled_out("This repeats the original error unchanged."), "c": ruled_out("'Is not only sings' puts two verb forms together, which is not grammatical."),
           "d": mistake("This inverts the auxiliary ('does she sing'), which only applies when 'not only' opens the whole sentence, not when the subject comes first.")},
          rules=["cj-r3"], uid="cj-p06", tech=["connectors"]),
        q("q-cj-placement", "fill", _SEL + "The scheme will benefit both the farmers ___ the traders in the region.", ["but also", "and", "or", "nor"], "b",
          "'Both' pairs with 'and', each placed directly before the item it is matching: both the farmers and the traders.",
          {"a": mistake("'But also' is the partner of 'not only', not of 'both'."), "c": ruled_out("'Or' does not complete 'both'."), "d": ruled_out("'Nor' does not complete 'both'.")},
          rules=["cj-r3"], uid="cj-p07", tech=["connectors"]),
        q("q-cj-redundant", "spot-error", _S + "Since he had / not submitted the form on time, / so his application / was rejected.",
          ["Since he had", "not submitted the form on time,", "so his application", "was rejected."], "c",
          "'Since' already joins the two clauses, so the second clause does not need 'so' as well; it should read 'his application was rejected'.",
          {"a": ruled_out("'Since he had' correctly opens the first clause."), "b": ruled_out("A correct continuation of the first clause."),
           "d": ruled_out("A correct closing verb phrase, once 'so' is removed.")},
          rules=["cj-r4"], uid="cj-p08", tech=["connectors"]),
        q("q-cj-redundant", "improve", _I + "Although the team played well, [[but they lost]] the final match.",
          ["they lost", "but they lost", "so they lost", "yet they lost"], "a",
          "'Although' already joins the two clauses, so the second clause needs no extra joiner at all: they lost the final match.",
          {"b": ruled_out("This repeats the original error unchanged."), "c": mistake("'So' is a different joiner, but the clause still does not need any second joiner once 'although' is used."),
           "d": mistake("'Yet' is the classic partner that gets wrongly doubled with 'although'; the clause still needs no second joiner.")},
          rules=["cj-r4"], uid="cj-p09", tech=["connectors"]),
        q("q-cj-redundant", "fill", _SEL + "When the alarm rang, ___ everyone rushed out of the building.", ["then", "so", "___ (nothing needed)", "therefore"], "c",
          "'When' already joins the two clauses by itself, so no second linking word (then/so/therefore) is needed in the other clause.",
          {"a": mistake("'Then' repeats the joining job 'when' has already done."), "b": mistake("'So' makes the same mistake with a different word."), "d": mistake("'Therefore' is the most formal-sounding of the repeated joiners, but it is still one too many.")},
          rules=["cj-r4"], uid="cj-p10", tech=["connectors"], rare=True),
    ]
