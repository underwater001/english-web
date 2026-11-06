"""Prepositions: fixed collocations, noun + of + -ing, and verbs that take their object directly. Quiz tier: 3 past questions plus practice."""
from bank import mistake, ruled_out, q

TOPIC = "prepositions"
TIER = "quiz"
PREFIX = "pr"

NODES = {
    "q-pr-collocation": {"short": "Fixed phrase", "label": "Preposition in a fixed phrase", "kind": "qtype", "parent": TOPIC, "order": 1,
                         "summary": "Many nouns and verbs take a particular preposition: under pressure, under conditions, in danger, on duty.", "links": []},
    "q-pr-gerund": {"short": "Noun + of + -ing", "label": "Noun + preposition + -ing", "kind": "qtype", "parent": TOPIC, "order": 2,
                    "summary": "After a noun such as reputation, habit, chance, way, the preposition is followed by -ing, not by to + verb.", "links": []},
    "q-pr-object": {"short": "No extra 'to'", "label": "Verbs that take the person directly", "kind": "qtype", "parent": TOPIC, "order": 3,
                    "summary": "Ask, tell, request, advise take the person with no preposition: asked the student to submit.", "links": []},
}

RULES = [
    {"id": "pr-r1", "node": "q-pr-collocation", "text": "Learn the preposition with the noun: under conditions / pressure / circumstances, in danger, on duty, at risk. The wrong options are real prepositions that do not belong with the word.",
     "ok": "It may occur under prolonged drought conditions.", "bad": "It may occur towards prolonged drought conditions."},
    {"id": "pr-r2", "node": "q-pr-gerund", "text": "After reputation, habit, chance, possibility, way, experience + of, the verb takes -ing: reputation of being honest. 'Reputation to be' is wrong.",
     "ok": "She has the reputation of being an honest leader.", "bad": "She has the reputation to be an honest leader."},
    {"id": "pr-r3", "node": "q-pr-object", "text": "Verbs such as ask, tell, request, advise, order take the person directly as their object and add 'to' only for the action: asked the student to submit. Do not put 'to' between the verb and the person.",
     "ok": "The teacher asked the student to submit the papers.", "bad": "The teacher asked to the student to submit the papers."},
]

METHODS = {
    "q-pr-collocation": {"cue": "A blank before a noun phrase (conditions, pressure, circumstances) in a short sentence.",
                         "standard": "Say the phrase with each option; the one that sounds like a stored phrase is the answer.",
                         "fast": "Think of the noun's usual company: conditions go with under; pressure goes with under.",
                         "eliminate": "Cross out prepositions of direction (towards) and of time that do not fit the noun.",
                         "traps": ["Two options may be possible in loose English (amidst); the stored phrase wins.", "Between needs two things; it is wrong with a single noun phrase."],
                         "rules": ["pr-r1"], "tech": ["back-substitute"]},
    "q-pr-gerund": {"cue": "A noun like reputation / chance / habit followed by 'to' + verb that you must replace.",
                    "standard": "Replace 'to be' with 'of being' after the noun. Check the article of the next noun.",
                    "fast": "Pick the option starting with 'of being' / 'of having' after a noun.",
                    "eliminate": "Remove options that turn the verb into a noun (to have honesty) or keep to + verb.",
                    "traps": ["'The honest leader' (with the) changes the meaning to one specific leader.", "'To be honesty' mixes a verb and a noun."],
                    "rules": ["pr-r2"], "tech": ["back-substitute"]},
    "q-pr-object": {"cue": "'asked to the student', 'told to him', 'requested to them' in the given sentence.",
                    "standard": "Delete the extra 'to' before the person. Keep 'to' only before the action verb.",
                    "fast": "Choose the option with no 'to' between the verb and the person.",
                    "eliminate": "Drop options with 'that' + base verb for ask, or with 'told to'.",
                    "traps": ["Using 'to' before the person (asked to the student).", "Dropping the article in the object (submit papers vs the papers)."],
                    "rules": ["pr-r3"], "tech": ["eliminate-pair"]},
}

REFS = []
S1, S2 = "2025-09-12-S1", "2025-09-12-S2"
_IMP = "Choose the most suitable option to replace the highlighted part of the sentence:\n"

PYQS = [
    q("q-pr-collocation", "fill", "Select the correct option to fill in the blank.\nEven though the phenomenon is uncommon, it may still occur ___ prolonged drought conditions.",
      ["towards", "amidst", "between", "under"], "d",
      "'Occur under [certain] conditions' is the standard phrase: events happen under conditions.",
      {"a": ruled_out("'Towards' shows direction and does not go with 'conditions'."),
       "b": mistake("'Amidst' is understandable, but 'occur under ... conditions' is the stored phrase the test expects."),
       "c": ruled_out("'Between' needs two things; there is one noun phrase here.")},
      rules=["pr-r1"], paper=S1, qno=86, tech=["back-substitute"],
      caution="'Amidst prolonged drought conditions' is also acceptable in loose English. The key 'under' rests on the stored phrase 'under conditions'."),
    q("q-pr-gerund", "improve", _IMP + "She has the reputation [[to be an honest leader]].",
      ["to have honesty", "of being an honest leader", "of being the honest leader", "to be honesty"], "b",
      "After the noun 'reputation' the preposition 'of' is used, followed by -ing: 'of being an honest leader'.",
      {"a": ruled_out("'To have honesty' keeps the wrong 'to' and changes the meaning."),
       "c": mistake("'Of being' is right, but 'the honest leader' points to one particular leader; the sentence speaks of being an honest leader in general."),
       "d": ruled_out("'To be honesty' mixes a verb and a noun and keeps the wrong 'to'.")},
      rules=["pr-r2"], paper=S1, qno=98, tech=["eliminate-pair"], trick="reputation of being."),
    q("q-pr-object", "improve", _IMP + "The teacher [[asked to the student to submit the papers]].",
      ["asked the student that submit the papers", "requested the student to submit papers", "asked the student to submit the papers", "told to the student submit papers"], "c",
      "'Ask' takes the person directly, with no 'to' before the student, and 'to' only before the action: 'asked the student to submit the papers'.",
      {"a": ruled_out("'Ask ... that submit' is not a correct pattern."),
       "b": mistake("'Requested the student to submit papers' is grammatical, but it drops 'the' from 'the papers' and changes the verb, so it is not the closest correction."),
       "d": ruled_out("'Told to the student' repeats the extra 'to' and has no 'to' before 'submit'.")},
      rules=["pr-r3"], paper=S2, qno=98, tech=["eliminate-pair"], trick="Delete the extra 'to'.",
      caution="Option b is grammatical too. The key is the option that makes the smallest change (just delete the extra 'to')."),
]


def practice_items():
    return [
        q("q-pr-collocation", "fill", "Select the correct option to fill in the blank.\nThe workers continued to build the bridge ___ difficult circumstances.",
          ["under", "between", "towards", "beside"], "a",
          "'Under circumstances' is the stored phrase.",
          {"b": ruled_out("'Between' needs two things."), "c": ruled_out("'Towards' shows direction."), "d": ruled_out("'Beside' means next to a thing, not 'in the situation of'.")},
          rules=["pr-r1"], uid="pr-p01"),
        q("q-pr-gerund", "improve", _IMP + "He has the habit [[to wake up at five]].",
          ["of waking up at five", "to waking at five", "for wake up at five", "of wake up at five"], "a",
          "After the noun 'habit' use 'of' + -ing: 'of waking up at five'.",
          {"b": ruled_out("'To waking' uses the wrong preposition."), "c": ruled_out("'For wake' uses a bare verb after a preposition."), "d": mistake("The preposition 'of' is right but the verb must be -ing, not bare.")},
          rules=["pr-r2"], uid="pr-p02"),
        q("q-pr-gerund", "improve", _IMP + "There is no chance [[to win the match]] now.",
          ["of winning the match", "for won the match", "to winning the match", "that win the match"], "a",
          "After 'no chance' you can use 'of' + -ing: 'of winning the match'. ('A chance to win' is also correct, but it is not among the options.)",
          {"b": ruled_out("'For won' uses a past form after a preposition."), "c": ruled_out("'To winning' mixes to and -ing."), "d": ruled_out("'That win' misses a subject and the verb is in the wrong form.")},
          rules=["pr-r2"], uid="pr-p03", rare=True),
        q("q-pr-object", "improve", _IMP + "The manager [[told to the clerk to send the file]].",
          ["told the clerk to send the file", "said the clerk to send the file", "told the clerk send the file", "told to send the file the clerk"], "a",
          "'Told' takes the person directly, then 'to' before the action.",
          {"b": ruled_out("'Said' cannot take 'the clerk' directly as its object."), "c": mistake("The extra 'to' is removed, but the 'to' before 'send' is lost too."), "d": ruled_out("The action 'send the file' is placed before the person 'the clerk', an order English does not allow after 'told'.")},
          rules=["pr-r3"], uid="pr-p04"),
    ]
