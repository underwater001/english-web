"""Active & passive voice. Quiz tier: 6 past questions plus practice. The tense is carried over unchanged: be + past participle in the tense of the active verb."""
from bank import mistake, ruled_out, q

TOPIC = "active-passive"
TIER = "quiz"
PREFIX = "ap"

NODES = {
    "q-ap-passive": {"short": "To passive", "label": "Active to passive", "kind": "qtype", "parent": TOPIC, "order": 1,
                     "summary": "The object becomes the subject; the verb becomes a form of be + past participle in the same tense; the old subject follows 'by'.", "links": []},
    "q-ap-active": {"short": "To active", "label": "Passive to active", "kind": "qtype", "parent": TOPIC, "order": 2,
                    "summary": "Undo the passive: the 'by' agent becomes the subject and the verb returns to its active form in the same tense.", "links": []},
}

RULES = [
    {"id": "ap-r1", "node": "q-ap-passive", "text": "Keep the tense: the passive of an active verb in tense T is be (in tense T) + past participle. Present perfect continuous 'have been ignoring' becomes 'has been being ignored'; simple past 'did disregard' becomes 'were disregarded'.",
     "ok": "They have been ignoring the records -> The records have been being ignored by them.", "bad": "The records had been ignored by them (a different tense)."},
    {"id": "ap-r2", "node": "q-ap-passive", "text": "A modal stays unchanged: can + base becomes can + be + past participle. Do not change can to could, or add 'being'.",
     "ok": "Citizens can access stamps -> Stamps can be accessed.", "bad": "Stamps can being accessed."},
    {"id": "ap-r3", "node": "q-ap-passive", "text": "In a question, 'did + base verb' becomes 'was / were + past participle': Why did the editor disregard the irregularities? -> Why were the irregularities disregarded by the editor? The tense is past, so was / were, not have been or are being.",
     "ok": "Why were the irregularities disregarded by the editor?", "bad": "Why are the irregularities being disregarded by the editor?"},
    {"id": "ap-r4", "node": "q-ap-active", "text": "To go back to active, the agent after 'by' becomes the subject, and the verb takes the tense of the passive's 'be'. 'Was being reported' becomes 'were reporting'; 'is delivered' becomes 'delivers'. If there is no agent, use someone / people.",
     "ok": "It was being reported by several sources -> Several sources were reporting.", "bad": "Several sources reported (the continuous aspect is lost)."},
    {"id": "ap-r5", "node": "q-ap-active", "text": "Do not choose a new subject from another noun in the sentence. The reception desk is where the parcel is delivered, not the doer; the unnamed doer becomes 'someone'.",
     "ok": "The parcel is delivered to the reception desk -> Someone delivers the parcel to the reception desk.", "bad": "The reception desk delivers the parcel."},
]

METHODS = {
    "q-ap-passive": {"cue": "'Change the following from active to passive'.",
                     "standard": "Find the tense and object. Put the object first, then be (in the same tense) + past participle, then 'by' + the old subject.",
                     "fast": "Check the auxiliary only: has been / was / can be, and see which option matches the original tense.",
                     "eliminate": "Drop options whose tense is different from the active sentence, and options with could/being added.",
                     "traps": ["A neat option that changes the tense (had been ignored).", "'Can being' or 'could' instead of 'can be'.", "Using have been / are being for a past question."],
                     "rules": ["ap-r1", "ap-r2", "ap-r3"], "tech": ["eliminate-pair"]},
    "q-ap-active": {"cue": "'Convert the sentence from passive to active'.",
                    "standard": "Make the 'by' agent the subject (someone if none), keep the object, and restore the tense of the passive's be.",
                    "fast": "Match the tense word: was being = were / was ...ing.",
                    "eliminate": "Drop options that change the tense or choose a wrong subject.",
                    "traps": ["Using a simple past instead of the continuous.", "Choosing the destination noun as the new subject.", "Adding words such as 'allegedly'."],
                    "rules": ["ap-r4", "ap-r5"], "tech": ["eliminate-pair"]},
}

REFS = []
S1, S2, S3 = "2025-09-12-S1", "2025-09-12-S2", "2025-09-12-S3"
_P = "Change the following from active to passive:\n"
_A = "Convert the sentence provided below from its passive voice structure to an active voice structure:\n"

PYQS = [
    q("q-ap-passive", "transform", _P + "They have been ignoring preservation of the records for years.",
      ["Preservation of the records had been ignored by them for years.", "Preservation of the records is being ignored by them for years.",
       "Preservation of the records was being ignored by them for years.", "Preservation of the records has been being ignored by them for years."], "d",
      "The active verb is present perfect continuous (have been ignoring). Its passive is has been being ignored, the only option that keeps both the perfect and the continuous aspect.",
      {"a": mistake("'Had been ignored' is past perfect, a different tense from the present perfect continuous."),
       "b": mistake("'Is being ignored' is present continuous; it loses the perfect aspect that 'for years' needs."),
       "c": mistake("'Was being ignored' is past continuous and loses the link with the present.")},
      rules=["ap-r1"], paper=S1, qno=77, rare=True, tech=["eliminate-pair"], trick="Count the aspects: perfect + continuous.",
      caution="'Has been being ignored' is correct but clumsy; it is the only option that keeps the original tense, which is why it is the key."),
    q("q-ap-active", "transform", _A + "It was being reported by several sources that the mission had been compromised internally.",
      ["Several sources were reporting that the mission had been compromised internally.", "The mission was compromised, several sources reported.",
       "The sources were reporting an internal mission compromise.", "The mission had compromised several internal sources."], "a",
      "'It was being reported by several sources' becomes 'Several sources were reporting'; the that-clause stays unchanged.",
      {"b": mistake("This changes 'was being reported' to a simple past and rewrites the clause, so the tense is lost."),
       "c": ruled_out("This reshapes the that-clause into a noun phrase and changes what was reported."),
       "d": ruled_out("This swaps the subject and object, which reverses the meaning.")},
      rules=["ap-r4"], paper=S1, qno=78, tech=["eliminate-pair"], trick="was being reported by X -> X were reporting."),
    q("q-ap-passive", "transform", _P + "Citizens can rarely access archived stamps without clearance.",
      ["Archived stamps can rarely being accessed without clearance.", "Archived stamps could rarely be accessed without clearance.",
       "Archived stamps can rarely be accessed without clearance.", "Archived stamps are rarely able to be accessed without clearance."], "c",
      "A modal stays as it is: can + be + past participle.",
      {"a": ruled_out("'Can being accessed' is not a correct form."),
       "b": mistake("'Could' changes 'can' to a past modal, so the tense and sense shift."),
       "d": mistake("'Are rarely able to be accessed' rewrites the modal and is a clumsy paraphrase.")},
      rules=["ap-r2"], paper=S2, qno=91, tech=["eliminate-pair"], trick="can + be + pp."),
    q("q-ap-active", "transform", _A + "The parcel is delivered to the reception desk every evening.",
      ["The reception desk delivers the parcel every evening.", "Someone delivers the parcel to the reception desk every evening.",
       "The reception desk has delivered the parcel every evening.", "The parcel delivers itself to the reception desk every evening."], "b",
      "No doer is named, so 'someone' becomes the subject, and 'is delivered' becomes 'delivers' in the same present tense.",
      {"a": mistake("The reception desk is the place of delivery, not the doer; this makes it the subject."),
       "c": ruled_out("This changes the tense to the present perfect and also makes the desk the doer."),
       "d": ruled_out("A parcel does not deliver itself; this distorts the meaning.")},
      rules=["ap-r4", "ap-r5"], paper=S2, qno=92, tech=["eliminate-pair"],
      caution="The original passive names no doer. 'Someone' is invented to complete the active form, which is the only option that keeps the meaning."),
    q("q-ap-active", "transform", _A + "It has been claimed that important data was being disclosed by employees within the firm.",
      ["Someone has claimed that employees were disclosing important data within the firm.", "Important data had been disclosed by employees, it is claimed.",
       "Employees have allegedly been disclosing important data within the firm.", "The firm was allegedly disclosing employee's data."], "a",
      "'It has been claimed' becomes 'Someone has claimed'; 'was being disclosed by employees' becomes 'employees were disclosing'.",
      {"b": ruled_out("This stays passive and changes the tense of 'was being disclosed'."),
       "c": mistake("This changes the 'has been claimed' frame into 'allegedly' and shifts the clause to present perfect continuous."),
       "d": ruled_out("This makes the firm the doer, which reverses the meaning.")},
      rules=["ap-r4"], paper=S3, qno=78, tech=["eliminate-pair"], trick="Do each clause: has been claimed -> has claimed; was being disclosed -> were disclosing."),
    q("q-ap-passive", "transform", _P + "Why did the editor disregard the major stylistic irregularities?",
      ["Why have the major stylistic irregularities been disregarded by the editor?", "Why are the major stylistic irregularities being disregarded by the editor?",
       "Why did the major stylistic irregularities be disregarded by the editor?", "Why were the major stylistic irregularities disregarded by the editor?"], "d",
      "The active verb 'did disregard' is simple past, so the passive is 'were disregarded'.",
      {"a": mistake("'Have been disregarded' is present perfect, a different tense."),
       "b": mistake("'Are being disregarded' is present continuous, a different tense."),
       "c": ruled_out("'Did ... be disregarded' is not a correct passive form.")},
      rules=["ap-r3"], paper=S3, qno=100, tech=["eliminate-pair"], trick="did + base -> were + pp."),
]


def _base():
    return [
        q("q-ap-passive", "transform", _P + "The committee will announce the results tomorrow.",
          ["The results will be announced by the committee tomorrow.", "The results will announced by the committee tomorrow.", "The results would be announced by the committee tomorrow.", "The results are announced by the committee tomorrow."], "a",
          "Future simple passive: will + be + past participle.",
          {"b": ruled_out("The 'be' is missing after 'will'."), "c": mistake("'Would' changes the tense of 'will'."), "d": mistake("The present simple loses the future sense.")}, rules=["ap-r1"], uid="ap-p01"),
        q("q-ap-passive", "transform", _P + "The students are watching a film.",
          ["A film is watched by the students.", "A film is being watched by the students.", "A film was being watched by the students.", "A film has been watched by the students."], "b",
          "Present continuous passive: is / are + being + past participle.",
          {"a": mistake("This is the present simple passive and loses the 'watching' now."), "c": mistake("This is past continuous."), "d": mistake("This is present perfect.")}, rules=["ap-r1"], uid="ap-p02"),
        q("q-ap-active", "transform", _A + "The bridge was built by the engineers in two years.",
          ["The engineers built the bridge in two years.", "The engineers were building the bridge in two years.", "The engineers had built the bridge in two years.", "The bridge built the engineers in two years."], "a",
          "Simple past passive 'was built' goes back to simple past 'built'.",
          {"b": mistake("This changes simple past to past continuous."), "c": mistake("This changes simple past to past perfect."), "d": ruled_out("Subject and object are swapped.")}, rules=["ap-r4"], uid="ap-p03"),
        q("q-ap-passive", "transform", _P + "Who wrote this letter?",
          ["By whom was this letter written?", "By whom is this letter written?", "Who was this letter written?", "By whom has this letter been written?"], "a",
          "'Who wrote' is simple past; the passive is 'By whom was this letter written?'",
          {"b": mistake("Present simple loses the past tense."), "c": ruled_out("'Who' cannot replace the 'by whom' agent here."), "d": mistake("Present perfect changes the tense.")}, rules=["ap-r3"], uid="ap-p04", rare=True),
    ]

_EXTRA = [
    q("q-ap-passive", "transform", _P + "The gardener is watering the plants.",
      ["The plants are watered by the gardener.", "The plants are being watered by the gardener.", "The plants were being watered by the gardener.", "The plants have been watered by the gardener."], "b",
      "Present continuous passive keeps both the present and the continuous: is/are + being + past participle.",
      {"a": mistake("This is the present simple passive and loses the 'at this moment' sense of 'is watering'."),
       "c": mistake("'Were being watered' moves the sentence into the past."),
       "d": mistake("'Have been watered' is the present perfect: the action is finished, not going on.")}, rules=["ap-r1"], uid="ap-p05"),
    q("q-ap-passive", "transform", _P + "You must submit the form before Friday.",
      ["The form must be submitted before Friday.", "The form must being submitted before Friday.", "The form should be submitted before Friday.", "The form is must submitted before Friday."], "a",
      "A modal is carried over unchanged and takes be + past participle: must be submitted.",
      {"b": ruled_out("'Must being submitted' is not a possible form; a modal takes the bare 'be'."),
       "c": mistake("'Should' weakens 'must' from an obligation to a recommendation."),
       "d": ruled_out("'Is must submitted' puts two verbs together with no passive form at all.")}, rules=["ap-r2"], uid="ap-p06"),
    q("q-ap-passive", "transform", _P + "They had completed the survey before the monsoon began.",
      ["The survey was completed before the monsoon began.", "The survey has been completed before the monsoon began.", "The survey had been completed before the monsoon began.", "The survey had being completed before the monsoon began."], "c",
      "Past perfect active 'had completed' becomes past perfect passive 'had been completed'; the tense must survive the change.",
      {"a": mistake("'Was completed' is the simple past and loses the 'earlier than the other past event' sense that 'had' carries."),
       "b": mistake("'Has been completed' is the present perfect, which cannot sit beside the past 'began'."),
       "d": ruled_out("'Had being completed' is not a possible form.")}, rules=["ap-r1", "ap-r2"], uid="ap-p07"),
    q("q-ap-active", "transform", _A + "The decision was taken by the committee last week.",
      ["The committee took the decision last week.", "The committee had taken the decision last week.", "The committee takes the decision last week.", "The committee was taking the decision last week."], "a",
      "Simple past passive 'was taken' returns to the simple past active 'took', and the 'by' agent becomes the subject.",
      {"b": mistake("'Had taken' is the past perfect, a tense the original does not have."),
       "c": ruled_out("The present simple cannot go with 'last week'."),
       "d": mistake("'Was taking' adds a continuous aspect the original does not have.")}, rules=["ap-r4"], uid="ap-p08"),
    q("q-ap-active", "transform", _A + "The streets are swept every morning.",
      ["The streets sweep every morning.", "Someone sweeps the streets every morning.", "Someone is sweeping the streets every morning.", "The morning sweeps the streets."], "b",
      "No doer is named, so 'someone' becomes the subject, and the present simple passive returns to the present simple active.",
      {"a": ruled_out("Streets cannot sweep; this makes the object the doer."),
       "c": mistake("'Is sweeping' adds a continuous aspect that 'are swept every morning' does not have."),
       "d": mistake("'The morning' is the time, not the doer; it is the same mistake as making the destination the subject.")}, rules=["ap-r4", "ap-r5"], uid="ap-p09"),
    q("q-ap-active", "transform", _A + "It is believed by many that the bridge is unsafe.",
      ["Many believe that the bridge is unsafe.", "Many believed that the bridge is unsafe.", "The bridge is believed unsafe by many.", "Many are believing that the bridge is unsafe."], "a",
      "'It is believed by many' becomes 'Many believe'; the that-clause is left as it stands.",
      {"b": mistake("'Believed' moves the sentence into the past, which the original does not."),
       "c": ruled_out("This stays in the passive instead of turning the sentence active."),
       "d": ruled_out("'Are believing' is not used for a state of belief.")}, rules=["ap-r4"], uid="ap-p10"),
    q("q-ap-active", "transform", _A + "Why was the meeting cancelled by the secretary?",
      ["Why the secretary cancelled the meeting?", "Why did the secretary cancel the meeting?", "Why has the secretary cancelled the meeting?", "Why the meeting was cancelled by the secretary?"], "b",
      "A passive past question becomes an active past question with 'did' and the bare verb: Why did the secretary cancel the meeting?",
      {"a": ruled_out("A question needs the auxiliary 'did' before the subject."),
       "c": mistake("'Has cancelled' is the present perfect, not the simple past of the original."),
       "d": ruled_out("This leaves the sentence passive and also drops the question word order.")}, rules=["ap-r3", "ap-r4"], uid="ap-p11", rare=True),
]


def practice_items():
    return _base() + _EXTRA
