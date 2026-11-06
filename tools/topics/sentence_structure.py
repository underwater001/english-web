"""Sentence structure: parallelism and word order. Quiz tier: 4 past questions plus practice. Grammar answers rest on the cited rule."""
from bank import mistake, ruled_out, q

TOPIC = "sentence-structure"
TIER = "quiz"
PREFIX = "ss"

NODES = {
    "q-ss-parallel": {"short": "Parallelism", "label": "Parallel structure", "kind": "qtype", "parent": TOPIC, "order": 1,
                      "summary": "Items joined by 'and', 'or', 'not ... but' must have the same grammatical form.", "links": []},
    "q-ss-order": {"short": "Word order", "label": "Word order in embedded questions", "kind": "qtype", "parent": TOPIC, "order": 2,
                   "summary": "Inside a sentence, a question word is followed by statement order: where he is staying, not where is he staying.", "links": []},
}

RULES = [
    {"id": "ss-r1", "node": "q-ss-parallel", "text": "Things joined by and, or, but, or in a list must be in the same form: all nouns, all to-infinitives, or all -ing words.",
     "ok": "He likes reading, writing and painting.", "bad": "He likes reading, to write and painting."},
    {"id": "ss-r2", "node": "q-ss-parallel", "text": "In 'not X but Y' (and 'either X or Y', 'both X and Y'), X and Y must match in form. A noun phrase after 'not' needs a noun phrase after 'but'.",
     "ok": "It is not the plan but its cost that worries us.", "bad": "It is not the plan but that it costs too much."},
    {"id": "ss-r3", "node": "q-ss-parallel", "text": "A list of abstract nouns cannot end in an -ing form: prudence, propriety and avoidance, not prudence, propriety and avoiding.",
     "ok": "Prudence, propriety and avoidance of early disclosure.", "bad": "Prudence, propriety and avoiding of early disclosure."},
    {"id": "ss-r4", "node": "q-ss-order", "text": "A question word inside another sentence (know, tell, ask, wonder) is followed by statement order: subject then verb, with no do/does/did and no inversion.",
     "ok": "No one knows where he is staying.", "bad": "No one knows where is he staying."},
]

METHODS = {
    "q-ss-parallel": {"cue": "'Find the part with the error' or 'choose the best replacement' in a sentence with a list, an 'and', or 'not ... but'.",
                      "standard": "Mark the joined items. Write each in its bare form. If one is a different form from its partners, that is the error.",
                      "fast": "Look at the words just before and after 'and' / 'but': they must look alike.",
                      "eliminate": "Drop options that mix to-forms and -ing forms in the same list.",
                      "traps": ["A list that begins with 'to ...' and then switches to -ing.", "'Not X but that ...' mixes a noun phrase and a clause.", "Abstract nouns ending a list with -ing."],
                      "rules": ["ss-r1", "ss-r2", "ss-r3"], "tech": ["eliminate-pair"]},
    "q-ss-order": {"cue": "A question word (where, what, when, how) in the middle of a sentence after know / tell / wonder / ask.",
                   "standard": "Turn the clause into a plain statement: subject, then verb. Choose the option with that order and no extra auxiliary.",
                   "fast": "Cross out options that start the clause with an auxiliary (is he, did she).",
                   "eliminate": "Remove options with an extra word at the end (staying at) or a wrong tense.",
                   "traps": ["Keeping the question order from the direct question.", "Adding 'at' or 'to' where the verb needs none."],
                   "rules": ["ss-r4"], "tech": ["read-whole"]},
}

REFS = []
S1, S2, S3 = "2025-09-12-S1", "2025-09-12-S2", "2025-09-12-S3"
_SPOT = "Find the part of the sentence that contains an error:\n"
_IMP = "Choose the most suitable option to replace the highlighted part of the sentence:\n"

PYQS = [
    q("q-ss-parallel", "spot-error", _SPOT + "What makes the draft legislation especially contentious is not its proposed restructuring of fiscal authority per se, / but that it assumes, without empirical evidence, / a fiscal parity among states whose developmental starting points are / incomparable by any accepted standard.",
      ["not its proposed restructuring of fiscal authority per se,", "but that it assumes, without empirical evidence,", "a fiscal parity among states whose developmental starting points are", "incomparable by any accepted standard."], "b",
      "'Not its proposed restructuring' is a noun phrase, so what follows 'but' must be a noun phrase too (for example 'but its assumption, without empirical evidence, of a fiscal parity'). 'But that it assumes' switches to a clause.",
      {"a": ruled_out("This sets up 'not X' as a noun phrase; it is the model the second part must match, not the error."),
       "c": ruled_out("The relative clause 'whose developmental starting points are ...' is correct and continues into the last part."),
       "d": ruled_out("'Incomparable by any accepted standard' correctly completes 'are' from the previous part.")},
      rules=["ss-r2"], paper=S1, qno=76, rare=True, tech=["eliminate-pair"], trick="After 'not <noun phrase>' expect 'but <noun phrase>'."),
    q("q-ss-parallel", "improve", _IMP + "The doctor advised him [[to stop consuming junk food and doing workouts regularly]].",
      ["stopping junk food and doing regular workouts", "to stop junk food and to workouts regularly", "to stop consuming junk food and to work out regularly", "to not consume junk food and do workouts"], "c",
      "Both advised actions must be to-infinitives joined by 'and': 'to stop consuming junk food and to work out regularly'. This keeps the same form on both sides.",
      {"a": mistake("'Stopping ... and doing' is parallel, but it no longer follows 'advised him', which needs 'to ...'."),
       "b": ruled_out("'To workouts' has no verb; 'workouts' is a noun."),
       "d": mistake("'To not consume' is a clumsy negative (the usual form is 'not to consume') and the second verb 'do workouts' loses the 'to' and the 'regularly'.")},
      rules=["ss-r1"], paper=S1, qno=85, tech=["eliminate-pair"], trick="Same form each side of 'and': to ... and to ..."),
    q("q-ss-order", "improve", _IMP + "No one knows [[where is he staying]].",
      ["where is he stay", "where he is staying at", "where he is staying", "where he had stayed is"], "c",
      "Inside another sentence a question word takes statement order: 'where he is staying'.",
      {"a": ruled_out("Keeps the question order and also uses the base 'stay' after 'is'."),
       "b": mistake("Statement order is right, but the extra 'at' at the end is not needed."),
       "d": ruled_out("Garbled order; 'is' ends the clause after a past form.")},
      rules=["ss-r4"], paper=S3, qno=87, tech=["read-whole"], trick="Where he is staying: the subject comes before the verb."),
    q("q-ss-parallel", "spot-error", _SPOT + "The higher the office was / the more pressing became the need / for prudence, propriety, and / avoiding of early disclosure.",
      ["The higher the office was", "the more pressing became the need", "for prudence, propriety, and", "avoiding of early disclosure."], "d",
      "'Prudence, propriety, and ...' is a list of nouns, so the last item must be a noun: 'avoidance of early disclosure', not 'avoiding of'.",
      {"a": ruled_out("'The higher the office was' is the correct first part of the 'the ... the ...' pattern."),
       "b": ruled_out("'The more pressing became the need' is the second part of the pattern, inverted for effect and acceptable."),
       "c": ruled_out("This begins a list of nouns and is correct; the fault is in the last item.")},
      rules=["ss-r3", "ss-r1"], paper=S3, qno=92, tech=["eliminate-pair"], trick="Nouns in a list end with a noun: avoidance."),
]


def _base():
    return [
        q("q-ss-parallel", "improve", _IMP + "She enjoys [[to swim, cycling and to read]] in her free time.",
          ["swimming, cycling and reading", "to swim, cycling and read", "swim, to cycle and reading", "swimming, to cycle and to read"], "a",
          "'Enjoys' takes -ing forms, and all three joined items should match: swimming, cycling and reading.",
          {"b": ruled_out("Still mixes a to-form, an -ing form and a bare verb."), "c": ruled_out("Mixes a bare verb, a to-form and an -ing form."),
           "d": mistake("The first item is fixed, but 'to cycle and to read' breaks the match.")}, rules=["ss-r1"], uid="ss-p01"),
        q("q-ss-parallel", "spot-error", _SPOT + "The manager praised her honesty, / her hard work, and / being punctual / during the review.",
          ["The manager praised her honesty,", "her hard work, and", "being punctual", "during the review."], "c",
          "Honesty and hard work are noun phrases, so the last item should be one too: 'her punctuality'.",
          {"a": ruled_out("A noun phrase and the first item of the list; correct."), "b": ruled_out("A noun phrase that matches the first item; correct."),
           "d": ruled_out("A prepositional phrase of time; correct.")}, rules=["ss-r1"], uid="ss-p02"),
        q("q-ss-parallel", "improve", _IMP + "It is not the weather [[but that he was late]] that annoyed us.",
          ["but his lateness", "but being late he was", "but that late he was", "but to be late of him"], "a",
          "'Not the weather' is a noun phrase, so 'but his lateness' matches.",
          {"b": ruled_out("Garbled; it does not give a noun phrase."), "c": ruled_out("Garbled word order with no noun phrase."), "d": ruled_out("This is not grammatical English and gives no noun phrase.")},
          rules=["ss-r2"], uid="ss-p03", rare=True),
        q("q-ss-order", "improve", _IMP + "I wonder [[what time is it]].",
          ["what time it is", "what is the time it", "what time it was at", "that what time it is"], "a",
          "After 'wonder', the clause takes statement order: 'what time it is'.",
          {"b": ruled_out("The words are in an order no English clause uses here."), "c": mistake("Wrong tense for 'wonder' in the present and an extra 'at'."), "d": mistake("The added 'that' is not needed before a question word.")},
          rules=["ss-r4"], uid="ss-p04"),
        q("q-ss-order", "improve", _IMP + "Can you tell me [[where does the bus stop]]?",
          ["where the bus stops", "where the bus does stop", "where stops the bus", "that where the bus stops"], "a",
          "Inside 'Can you tell me ...' use statement order and drop 'does': 'where the bus stops'.",
          {"b": mistake("Statement order is right, but the 'does' is left over from the direct question."), "c": ruled_out("Inverted order."), "d": ruled_out("Extra 'that' before the question word.")},
          rules=["ss-r4"], uid="ss-p05"),
    ]

_EXTRA = [
    q("q-ss-parallel", "spot-error", _SPOT + "The new policy promises / to simplify the forms, to shorten the queues / and reducing the number of visits / a claimant must make.",
      ["The new policy promises", "to simplify the forms, to shorten the queues", "and reducing the number of visits", "a claimant must make"], "c",
      "The list is built of to-infinitives, so the third item must be 'and to reduce', not 'and reducing'.",
      {"a": ruled_out("'The new policy promises' correctly introduces the list."),
       "b": ruled_out("These two items are both to-infinitives and set the pattern the third must follow."),
       "d": ruled_out("'A claimant must make' is a relative clause describing the visits and is correct.")},
      rules=["ss-r1"], uid="ss-p06", tech=["eliminate-pair"]),
    q("q-ss-order", "spot-error", _SPOT + "The clerk could not explain / why was the file missing / although he had signed / the register that morning.",
      ["The clerk could not explain", "why was the file missing", "although he had signed", "the register that morning"], "b",
      "Inside a sentence a question word takes statement order, so it must be 'why the file was missing'.",
      {"a": ruled_out("'The clerk could not explain' is the main clause and is correct."),
       "c": ruled_out("'Although he had signed' is a correct contrast clause in the past perfect."),
       "d": ruled_out("'The register that morning' is the object with a phrase of time.")},
      rules=["ss-r4"], uid="ss-p07", tech=["read-whole"]),
    q("q-ss-parallel", "improve", _IMP + "The report praises the scheme [[for its reach and because it is cheap]].",
      ["for its reach and its low cost", "for its reach and because of cheap", "for reaching and because it is cheap", "for its reach and it is cheap"], "a",
      "'For its reach' is a noun phrase, so the second item joined by 'and' must be a noun phrase too: 'its low cost'.",
      {"b": ruled_out("'Because of cheap' puts an adjective after a preposition, which is not possible."),
       "c": mistake("This makes the first item an -ing form but leaves the second as a clause, so the two still do not match."),
       "d": mistake("'And it is cheap' is still a clause beside a noun phrase.")},
      rules=["ss-r1", "ss-r2"], uid="ss-p08", tech=["eliminate-pair"]),
    q("q-ss-order", "improve", _IMP + "Nobody could tell us [[when will the results be declared]].",
      ["when the results would be declared", "when will be the results declared", "when the results will be declared at", "that when the results be declared"], "a",
      "The clause takes statement order, and after the past 'could tell' the future 'will' shifts to 'would'.",
      {"b": ruled_out("This keeps the question order with the auxiliary in front."),
       "c": mistake("Statement order is right, but 'will' is not back-shifted after 'could tell' and the trailing 'at' is not needed."),
       "d": ruled_out("The extra 'that' is not used before a question word, and 'be declared' has no auxiliary.")},
      rules=["ss-r4"], uid="ss-p09", tech=["read-whole"], rare=True),
]


def practice_items():
    return _base() + _EXTRA
