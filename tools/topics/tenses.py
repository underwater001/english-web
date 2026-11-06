"""Tenses & verb forms: verb form after a modal, and the subjunctive after verbs of demand. Quiz tier: 2 past questions plus practice."""
from bank import mistake, ruled_out, q

TOPIC = "tenses"
TIER = "quiz"
PREFIX = "tn"

NODES = {
    "q-tn-modal": {"short": "After a modal", "label": "Verb form after a modal or auxiliary", "kind": "qtype", "parent": TOPIC, "order": 1,
                   "summary": "After will, can, may, must, should and similar, the verb is the bare base form, even when other words come in between.", "links": []},
    "q-tn-subjunctive": {"short": "Demand that", "label": "Verb after demand, insist, suggest", "kind": "qtype", "parent": TOPIC, "order": 2,
                         "summary": "After demand, insist, suggest, recommend, request + that, use the base verb, with no -s and no tense.", "links": []},
}

RULES = [
    {"id": "tn-r1", "node": "q-tn-modal", "text": "After a modal (will, would, can, could, may, might, shall, should, must) the verb is the bare base form: no -s, no -ed, no -ing, no to. Words placed between the modal and the verb (such as 'without any pressure') do not change this.",
     "ok": "Regional bodies will, without any pressure, comply.", "bad": "Regional bodies will, without any pressure, complies."},
    {"id": "tn-r2", "node": "q-tn-subjunctive", "text": "After demand, insist, suggest, recommend, request, propose, order + that, the verb is the base form (subjunctive) whatever the subject. 'Demand' cannot take 'me to': say 'demanded that I ...'.",
     "ok": "She demanded that I swallow the medication.", "bad": "She demanded me to swallow the medication."},
]

METHODS = {
    "q-tn-modal": {"cue": "A long sentence with 'will', 'can' or 'must' and a verb that appears several words later.",
                   "standard": "Find the modal in each part and join it to the verb that belongs with it, skipping the words in between. The verb must be in its base form.",
                   "fast": "Look for -s / -ed / -ing verbs after a modal.",
                   "eliminate": "Parts without a verb cannot hold the error; skip them.",
                   "traps": ["A plural subject far from the verb making you read 'comply'; the real fault is the -s.", "Words between the modal and the verb hide the mismatch."],
                   "rules": ["tn-r1"], "tech": ["read-whole"]},
    "q-tn-subjunctive": {"cue": "demanded / insisted / suggested / recommended + a person + 'to' or 'that' and a verb.",
                         "standard": "Replace 'demand + me to' with 'demand that I' and put the verb in the base form.",
                         "fast": "Pick the option with 'that' + base verb.",
                         "eliminate": "Drop options that use 'me to' or 'by me', or put an object pronoun ('that me') in the subject slot.",
                         "traps": ["'Demanded me to' copies the pattern of 'asked me to', which works for ask but not demand.", "'That me' puts an object pronoun in the subject position."],
                         "rules": ["tn-r2"], "tech": ["eliminate-pair"]},
}

REFS = []
S2, S3 = "2025-09-12-S2", "2025-09-12-S3"
_SPOT = "Find the part of the sentence that contains an error:\n"
_IMP = "Choose the most suitable option to replace the highlighted part of the sentence:\n"

PYQS = [
    q("q-tn-modal", "spot-error", _SPOT + "That the policy omits provisions for backward compatibility / is less troubling than the belief / that all regional bodies will, without any pressure, / complies with the central directive as issued.",
      ["That the policy omits provisions for backward compatibility", "is less troubling than the belief", "that all regional bodies will, without any pressure,", "complies with the central directive as issued."], "d",
      "'Will' needs a base verb, so 'complies' must be 'comply'. The phrase 'without any pressure' sits between them and hides the pair.",
      {"a": ruled_out("A 'That' clause subject with 'omits': the verb agrees with 'policy', so it is correct."),
       "b": ruled_out("'Is less troubling than the belief' is a correct singular verb phrase for the clause subject."),
       "c": ruled_out("'All regional bodies will' correctly starts the pair; the fault is in the verb that completes it.")},
      rules=["tn-r1"], paper=S2, qno=95, tech=["read-whole"], trick="will ... comply, not complies."),
    q("q-tn-subjunctive", "improve", _IMP + "She [[demanded me to swallow the medication]].",
      ["demanded that I swallow the medication", "me swallowing the medication", "that me swallow the medication", "to swallow the medication by me"], "a",
      "'Demand' takes a that-clause with the base verb: 'demanded that I swallow'. It cannot be followed by 'me to'.",
      {"b": ruled_out("'Demanded me swallowing' is not a correct pattern."),
       "c": mistake("'That me swallow' puts the object form 'me' where the subject 'I' is needed."),
       "d": ruled_out("'By me' is a passive-style ending that does not fit 'demanded'.")},
      rules=["tn-r2"], paper=S3, qno=90, tech=["eliminate-pair"], trick="demand + that + I + base verb."),
]


def practice_items():
    return [
        q("q-tn-modal", "spot-error", _SPOT + "The firm said that / it can, if the weather permits, / completes the work / before the festival.",
          ["The firm said that", "it can, if the weather permits,", "completes the work", "before the festival."], "c",
          "'Can' needs the base verb, so 'completes' must be 'complete'; the if-clause sits between them.",
          {"a": ruled_out("Reporting verb in the past; there is no error."), "b": ruled_out("'It can' is correct and starts the pair."),
           "d": ruled_out("'Before the festival' is a correct phrase of time.")}, rules=["tn-r1"], uid="tn-p01"),
        q("q-tn-modal", "spot-error", _SPOT + "Nobody believed that / the old bridge could, despite the repairs, / to bear the weight / of the heavy trucks.",
          ["Nobody believed that", "the old bridge could, despite the repairs,", "to bear the weight", "of the heavy trucks."], "c",
          "After 'could' the verb is bare: 'bear', not 'to bear'.",
          {"a": ruled_out("Correct reporting clause."), "b": ruled_out("'Could' starts the pair and is correct."), "d": ruled_out("A correct 'of' phrase.")},
          rules=["tn-r1"], uid="tn-p02"),
        q("q-tn-subjunctive", "fill", "Select the most appropriate option to fill in the blank.\nThe committee recommended that the rule ___ revised at once.",
          ["is", "be", "was", "has been"], "b",
          "After 'recommend that' the base form is used, so the passive becomes 'be revised'.",
          {"a": mistake("The ordinary present is used here, but 'recommended that' needs the base verb."), "c": mistake("A past form is used here, but the verb after 'recommend that' is the base form."),
           "d": mistake("The present perfect is used here instead of the base form that 'recommended that' requires.")}, rules=["tn-r2"], uid="tn-p03"),
        q("q-tn-subjunctive", "fill", "Select the most appropriate option to fill in the blank.\nThe coach insisted that every player ___ at six sharp.",
          ["arrives", "arrive", "arrived", "arriving"], "b",
          "After 'insisted that' the base verb is used for every subject: 'arrive'.",
          {"a": mistake("The -s form agrees with 'every player' in the ordinary way, but this verb needs the base form."), "c": mistake("A past form is used here, but 'insist that' takes the base verb."),
           "d": ruled_out("An -ing form cannot be the finite verb of the clause.")}, rules=["tn-r2"], uid="tn-p04", rare=True),
    ]
