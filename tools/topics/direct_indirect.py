"""Direct & indirect speech. Quiz tier: 6 past questions plus practice. Back-shift and word changes are cited rules, not machine-checked."""
from bank import mistake, ruled_out, q

TOPIC = "direct-indirect"
TIER = "quiz"
PREFIX = "di"

NODES = {
    "q-di-statement": {"short": "Statements", "label": "Statements and back-shift", "kind": "qtype", "parent": TOPIC, "order": 1,
                       "summary": "A past reporting verb pushes the tense back (am -> was, will -> would) and changes time words (yesterday -> the previous day).", "links": []},
    "q-di-question": {"short": "Questions", "label": "Reported questions", "kind": "qtype", "parent": TOPIC, "order": 2,
                      "summary": "A yes/no question becomes if / whether with statement order; no 'did', no question mark.", "links": []},
    "q-di-command": {"short": "Commands", "label": "Commands and must", "kind": "qtype", "parent": TOPIC, "order": 3,
                     "summary": "Commands become 'told / ordered ... to'; 'must' stays 'must' in speech.", "links": []},
}

RULES = [
    {"id": "di-r1", "node": "q-di-statement", "text": "With a past reporting verb the tense moves back one step: am / is -> was, will -> would, can -> could, simple past / present perfect -> past perfect. To go from indirect back to direct, reverse the step (would -> will).",
     "ok": "He said, \"I am not feeling fine\" -> He said that he was not feeling fine.", "bad": "He said that he is not feeling fine (no back-shift)."},
    {"id": "di-r2", "node": "q-di-statement", "text": "Time words shift in reported speech: yesterday -> the previous day, tomorrow -> the next day, now -> then, here -> there. In the past tense the sentence becomes past perfect.",
     "ok": "She said, \"I met him yesterday\" -> She said she had met him the previous day.", "bad": "She said she has met him yesterday."},
    {"id": "di-r3", "node": "q-di-question", "text": "A reported yes/no question uses if or whether, then statement order (subject before verb), back-shifted, with no 'did' and no question mark.",
     "ok": "He asked, \"Did you submit it?\" -> He asked if I had submitted it.", "bad": "He asked did I submit it. / He asked whether had I submitted it."},
    {"id": "di-r4", "node": "q-di-command", "text": "'Must' does not change in reported speech, and a reported 'must' remains a statement. A direct command is an imperative; to undo a reported command, return it to the imperative form. Pick the option that keeps the force of the original.",
     "ok": "The librarian said that silence must be maintained -> \"Maintain silence,\" said the librarian (command force kept).", "bad": "\"Must you maintain silence?\" (turns it into a question)."},
]

METHODS = {
    "q-di-statement": {"cue": "'He said that ...' or 'He said, \"...\"' with a verb in the said-clause and a tense or time word to change.",
                       "standard": "Mark the tense and time words. Move back (direct to indirect) or forward (indirect to direct) one step.",
                       "fast": "Look at the auxiliary: would / was / had in the indirect means will / am / has / simple past in the direct.",
                       "eliminate": "Drop options with no back-shift, with the wrong aspect (was meeting) or with ungrammatical forms (had meet).",
                       "traps": ["Leaving 'yesterday' unchanged.", "Changing would to would in reverse.", "'Shall' vs 'will' for first person: the exam default is will -> would."],
                       "rules": ["di-r1", "di-r2"], "tech": ["eliminate-pair"]},
    "q-di-question": {"cue": "He asked me, \"Did you ...?\" or the reverse.",
                      "standard": "Replace the question with if / whether, put the subject before the verb, back-shift the tense.",
                      "fast": "Pick the option with 'if / whether' + subject + past perfect, no 'did'.",
                      "eliminate": "Drop options keeping the question order (did I submit, had I submitted).",
                      "traps": ["'Whether had I' keeps the inversion.", "'Whether I have' skips the back-shift."],
                      "rules": ["di-r3"], "tech": ["eliminate-pair"]},
    "q-di-command": {"cue": "A reporting sentence with must / should and an option that changes it to a command.",
                     "standard": "Decide what the speaker did: stated a rule or gave an order. Choose the option with that force and no change of meaning.",
                     "fast": "Rule out options that change must to should or turn it into a question.",
                     "eliminate": "Drop options that add 'you will' or end in a question mark.",
                     "traps": ["Must -> should changes the strength.", "A rule can be stated either as a statement or as an imperative; the exam expects one of them."],
                     "rules": ["di-r4"], "tech": ["eliminate-pair"]},
}

REFS = []
S1, S2, S3 = "2025-09-12-S1", "2025-09-12-S2", "2025-09-12-S3"
_TO_D = "A sentence is provided in indirect speech. From the four given options, choose the one that most accurately conveys the sentence in its corresponding direct speech.\n"
_TO_I = "A sentence is provided in direct speech. From the four given options, choose the one that most accurately conveys the sentence in its corresponding indirect speech.\n"

PYQS = [
    q("q-di-statement", "transform", _TO_D + "He said that he would attend the meeting after the meal.",
      ["\"I will attend the meeting after the meal,\" he said.", "\"I would attend the meeting after the meal,\" he said.",
       "\"I shall attend the meeting after the meal,\" he said.", "\"I can attend the meeting after the meal,\" he said."], "a",
      "Going back to direct speech, 'would' becomes 'will' and 'he' becomes 'I': \"I will attend ...\".",
      {"b": mistake("Keeping 'would' leaves the back-shift in place; direct speech needs the original 'will'."),
       "c": mistake("'Shall' is the traditional first-person future, but the usual reverse of 'would' in exam practice is 'will'."),
       "d": ruled_out("'Can' changes the meaning from a plan to an ability.")},
      rules=["di-r1"], paper=S1, qno=82, tech=["eliminate-pair"], trick="would -> will.",
      caution="Option c ('shall') is defensible in strict traditional grammar; exam keys use 'will'."),
    q("q-di-question", "transform", _TO_I + "He asked me, \"Did you submit your homework?\"",
      ["He asked me if I had submitted my homework.", "He asked me did I submit my homework.", "He asked me whether I have submitted my homework.", "He asked me whether had I submitted my homework."], "a",
      "A yes/no question becomes 'if / whether' + statement order, and the simple past moves back to past perfect: 'if I had submitted my homework'.",
      {"b": mistake("This keeps 'did I submit', the question order, and has no linking word."),
       "c": mistake("'Whether I have submitted' skips the back-shift; the past reporting verb needs the past perfect."),
       "d": mistake("'Whether had I' keeps the question inversion; reported questions use statement order.")},
      rules=["di-r3"], paper=S1, qno=99, tech=["eliminate-pair"], trick="if + subject + had + pp."),
    q("q-di-command", "transform", _TO_D + "The librarian of Public library said that silence must be maintained in the reading hall.",
      ["\"Silence should be maintained in the reading hall,\" said the librarian of public library.", "\"You will maintain silence in the reading hall,\" said the librarian of public library.",
       "\"Maintain silence in the reading hall,\" said the librarian of public library.", "\"Must you maintain silence in the reading hall?\" asked the librarian of public library."], "c",
      "The librarian's words are a rule given to readers, so the direct form is the imperative \"Maintain silence ...\".",
      {"a": mistake("This changes 'must' to 'should', which weakens the rule."),
       "b": mistake("'You will maintain' turns the rule into a prediction."),
       "d": ruled_out("This turns the statement into a question.")},
      rules=["di-r4"], paper=S2, qno=85, tech=["eliminate-pair"],
      caution="The key is reached by elimination. A reported 'must be maintained' could also stay as \"Silence must be maintained\" (as in the S3 question 'Due dates must be met strictly'), but that option is not offered here."),
    q("q-di-statement", "transform", _TO_I + "She said, \"I met him yesterday morning.\"",
      ["She said she had met him the previous morning.", "She said she has met him yesterday morning.", "She said she was meeting him yesterday morning.", "She said she had meet him the previous morning."], "a",
      "The simple past 'met' goes back to the past perfect 'had met', and 'yesterday' becomes 'the previous (day)': \"the previous morning\".",
      {"b": mistake("This keeps 'yesterday' and uses 'has met', a present perfect, without the back-shift."),
       "c": mistake("'Was meeting' changes the aspect, and 'yesterday' is left unchanged."),
       "d": ruled_out("'Had meet' is not a correct verb form; the past participle is 'met'.")},
      rules=["di-r1", "di-r2"], paper=S2, qno=88, tech=["eliminate-pair"], trick="met -> had met; yesterday -> the previous day."),
    q("q-di-command", "transform", _TO_D + "The manager told the staff that due dates must be met strictly.",
      ["\"Due dates must be met strictly,\" said the manager.", "\"You should meet the due dates strictly,\" said the manager.",
       "\"Meet the due dates strictly,\" the manager said.", "\"Due dates are to be met,\" said the manager."], "a",
      "'Must' does not change in reported speech, so the direct form keeps \"Due dates must be met strictly\".",
      {"b": mistake("'Should' weakens the force of 'must'."),
       "c": mistake("This turns the statement into a command to the staff and loses the passive 'must be met'."),
       "d": mistake("'Are to be met' changes the modal and drops 'strictly'.")},
      rules=["di-r4"], paper=S3, qno=80, tech=["eliminate-pair"], trick="Must stays must."),
    q("q-di-statement", "transform", _TO_I + "He said, \"I am not feeling fine.\"",
      ["He said that he is not feeling fine.", "He said that he was not feeling fine.", "He said that he didn't feel fine.", "He said he not feeling fine."], "b",
      "The present continuous 'am feeling' moves back to the past continuous 'was feeling', and 'I' becomes 'he'.",
      {"a": mistake("'Is not feeling' keeps the present tense; the past reporting verb needs a back-shift."),
       "c": mistake("'Didn't feel' changes the continuous aspect to a simple past."),
       "d": ruled_out("The auxiliary 'was' is missing, so the sentence is ungrammatical.")},
      rules=["di-r1"], paper=S3, qno=98, tech=["eliminate-pair"], trick="am feeling -> was feeling."),
]


def practice_items():
    return [
        q("q-di-statement", "transform", _TO_I + "She said, \"I will call you tomorrow.\"",
          ["She said that she would call me the next day.", "She said that she will call me tomorrow.", "She said that she would call you tomorrow.", "She said that she called me the next day."], "a",
          "Will -> would, tomorrow -> the next day, you -> me.",
          {"b": mistake("No back-shift and tomorrow is unchanged."), "c": mistake("'You' must change to 'me', and tomorrow to 'the next day'."), "d": mistake("The simple past drops the future sense.")}, rules=["di-r1", "di-r2"], uid="di-p01"),
        q("q-di-question", "transform", _TO_I + "He asked, \"Where do you live?\"",
          ["He asked where I lived.", "He asked where did I live.", "He asked where I live.", "He asked that where I lived."], "a",
          "A wh- question keeps its wh-word, uses statement order and back-shifts: 'where I lived'.",
          {"b": mistake("Keeps the question order with 'did'."), "c": mistake("Skips the back-shift."), "d": ruled_out("An extra 'that' is not used before the wh-word.")}, rules=["di-r3"], uid="di-p02"),
        q("q-di-statement", "transform", _TO_D + "He said that he had finished the work the previous day.",
          ["He said, \"I finished the work yesterday.\"", "He said, \"I have finished the work the previous day.\"", "He said, \"I had finished the work yesterday.\"", "He said, \"He finished the work yesterday.\""], "a",
          "Past perfect goes back to the simple past, and the previous day goes back to yesterday.",
          {"b": mistake("'The previous day' is a reported-speech time word."), "c": mistake("This keeps the past perfect that belongs to indirect speech."), "d": ruled_out("'He' should be 'I' in his own words.")}, rules=["di-r1", "di-r2"], uid="di-p03"),
    ]
