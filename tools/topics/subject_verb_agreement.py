"""Subject-verb agreement. Quiz tier: 4 past questions plus practice.
Grammar answers are grounded in a stated rule. The one machine check: of the four verb options, exactly one has the number
the rule demands (so no item can have two defensible answers by number)."""
from bank import mistake, ruled_out, q

TOPIC = "subject-verb-agreement"
TIER = "quiz"
PREFIX = "sv"

NODES = {
    "q-sva-each": {"short": "Each / every", "label": "Each, every, either, neither", "kind": "qtype", "parent": TOPIC, "order": 1,
                   "summary": "Each, every, either, neither and words like everyone take a singular verb.", "links": []},
    "q-sva-nearer": {"short": "Either-or", "label": "Either...or, neither...nor", "kind": "qtype", "parent": TOPIC, "order": 2,
                     "summary": "With either...or and neither...nor, the verb agrees with the nearer subject.", "links": []},
    "q-sva-number": {"short": "A number of", "label": "The number of / a number of", "kind": "qtype", "parent": TOPIC, "order": 3,
                     "summary": "'The number of' is singular; 'a number of' is plural.", "links": []},
    "q-sva-phrase": {"short": "Along with", "label": "Along with, as well as", "kind": "qtype", "parent": TOPIC, "order": 4,
                     "summary": "The verb agrees with the first subject, not with the noun after 'along with' or 'as well as'.", "links": []},
    "q-sva-spot": {"short": "Far subject", "label": "Subject far from its verb", "kind": "qtype", "parent": TOPIC, "order": 5,
                   "summary": "Long sentences put phrases between the subject and the verb, or make a whole clause the subject; find the real subject and check the verb.", "links": []},
    "q-sva-inverted": {"short": "Inverted order", "label": "Verb before its subject", "kind": "qtype", "parent": TOPIC, "order": 6,
                       "summary": "After 'so + adjective', 'here', 'there' and similar openers the verb comes first; it still agrees with the subject that follows.", "links": []},
}

RULES = [
    {"id": "sva-r1", "node": "q-sva-each", "text": "Each, every, either, neither, everyone, everybody, nobody and anyone take a singular verb, even when 'of' plus a plural noun follows.",
     "ok": "Each of the boys was rewarded.", "bad": "Each of the boys were rewarded."},
    {"id": "sva-r3", "node": "q-sva-nearer", "text": "When subjects are joined by either...or, neither...nor, or, nor, the verb agrees with the subject nearest to it.",
     "ok": "Neither the teacher nor the students were aware.", "bad": "Neither the teacher nor the students was aware."},
    {"id": "sva-r6", "node": "q-sva-number", "text": "'The number of' + plural noun takes a singular verb (it is about the number). 'A number of' + plural noun takes a plural verb (it means 'many').",
     "ok": "The number of cases is rising. A number of cases are pending.", "bad": "The number of cases are rising."},
    {"id": "sva-r7", "node": "q-sva-phrase", "text": "With, along with, together with, as well as, in addition to and besides do not add to the subject. The verb agrees with the first subject.",
     "ok": "The principal, along with the teachers, is attending.", "bad": "The principal, along with the teachers, are attending."},
    {"id": "sva-r8", "node": "q-sva-spot", "text": "A clause used as the subject ('That ...', 'What ...', 'Whether ...') takes a singular verb, however many plural nouns sit inside it.",
     "ok": "That the reports were late was surprising.", "bad": "That the reports were late were surprising."},
    {"id": "sva-r9", "node": "q-sva-spot", "text": "The verb agrees with the subject, never with the complement. 'Much of ...' and other uncountable subjects are singular even if a plural noun follows the verb.",
     "ok": "Much of what he said is rumour.", "bad": "Much of what he said are rumours."},
    {"id": "sva-r10", "node": "q-sva-spot", "text": "Cross out the phrases between commas and the prepositional phrases after the subject, then match the verb to the noun left. 'The focus on X' is singular, however plural X is.",
     "ok": "The focus on small farms, though praiseworthy, ignores big ones.", "bad": "The focus on small farms, though praiseworthy, ignore big ones."},
    {"id": "sva-r11", "node": "q-sva-inverted", "text": "When the sentence opens with 'so + adjective' (or here, there, never ...), the verb comes before its subject and still agrees with the subject that follows it; also keep the tense the rest of the sentence needs.",
     "ok": "So fragile were the talks that one leak could end them.", "bad": "So fragile was the talks that one leak could end them."},
]

METHODS = {
    "q-sva-each": {"cue": "A blank before 'each / every / either / neither / everyone', often followed by 'of the ...' plus a plural noun.",
                   "standard": "Find the subject word (each, every, neither ...). Ignore the plural noun after 'of'. Choose the singular verb.",
                   "fast": "See 'each' or 'every' and go straight to the singular option: is, was, has.",
                   "eliminate": "Cross out every plural verb (are, were, have) before reading the rest.",
                   "traps": ["The plural noun after 'of' pulls the eye towards a plural verb.", "'Every boy and every girl' still takes a singular verb."],
                   "rules": ["sva-r1"], "tech": ["subject-first"]},
    "q-sva-nearer": {"cue": "'Either ... or', 'neither ... nor', or two subjects joined by 'or' / 'nor'.",
                     "standard": "Look at the subject placed immediately before the verb. Match the verb to its number.",
                     "fast": "Read only the last subject and the blank.",
                     "eliminate": "Drop the options that agree with the first subject unless it is also the nearer one.",
                     "traps": ["Agreeing with the first subject because it is read first.", "Reversing the order of subjects changes the correct verb."],
                     "rules": ["sva-r3"], "tech": ["subject-first"]},
    "q-sva-number": {"cue": "'The number of' or 'A number of' before a plural noun.",
                     "standard": "'The number' is the subject: singular. 'A number of' works as 'many': plural.",
                     "fast": "'The' keeps it singular, 'A' makes it plural.",
                     "eliminate": "Decide the article first (the or a). It fixes the number of the verb.",
                     "traps": ["Reading the plural noun that follows as the subject after 'the number of'.", "Treating 'a number of' as a singular count."],
                     "rules": ["sva-r6"], "tech": ["subject-first"]},
    "q-sva-phrase": {"cue": "A subject followed by 'along with', 'together with', 'as well as' or 'in addition to' and another noun, then the blank.",
                     "standard": "Cover the phrase between commas. The subject left is the one the verb agrees with.",
                     "fast": "Strike out the 'along with ...' phrase and read the sentence without it.",
                     "eliminate": "Remove every option that agrees with the noun inside the phrase.",
                     "traps": ["The nearer plural noun inside the phrase pulls the verb to the plural.", "'And' would make a plural subject, but 'along with' does not."],
                     "rules": ["sva-r7"], "tech": ["subject-first"]},
    "q-sva-spot": {"cue": "'Find the part of the sentence that contains an error' over a long sentence where the verb is far from its subject or the subject begins with 'That', 'What' or 'Much'.",
                   "standard": "Find the verb in each part. Locate its true subject by crossing out the commas, 'of ...' and 'on ...' phrases. Check number. The part with the mismatch is the error.",
                   "fast": "Go to the part with the main verb (is/are/was/were or a verb with -s) and match it with the first noun of the sentence.",
                   "eliminate": "Parts without a verb cannot be an agreement error; skip them.",
                   "traps": ["A plural noun just before the verb ('causes', 'overlaps') pulls the eye to a plural verb.", "A clause subject starting with 'That' is singular.",
                             "'Much of' is singular."],
                   "rules": ["sva-r8", "sva-r9", "sva-r10"], "tech": ["subject-first"]},
    "q-sva-inverted": {"cue": "A blank right after 'So + adjective' or 'Here/There', with the subject coming after the blank.",
                       "standard": "Turn the sentence round (The talks were so fragile ...), find the subject, and choose the verb that agrees with it and suits the tense.",
                       "fast": "Look right of the blank for the noun it agrees with.",
                       "eliminate": "Remove the verbs with the wrong number first; if two remain, decide by tense.",
                       "traps": ["Agreeing with the adjective before the blank.", "When two options agree in number (are, were), the tense of the rest of the sentence decides."],
                       "rules": ["sva-r11"], "tech": ["subject-first"]},
}

REFS = []

SING = {"is", "was", "has", "has been"}
PLUR = {"are", "were", "have", "have been"}


def _one_with_number(want):
    """Exactly one of the four verb options has the required number."""
    pool = SING if want == "sing" else PLUR
    return lambda x: x["options"][("abcd".index(x["key"]))] in pool and sum(1 for o in x["options"] if o in pool) == 1


def _fill(uid, qtype, text, options, key, why, wrong, rule, want, **kw):
    return q(qtype, "fill", "Select the most appropriate option to fill in the blank.\n" + text, options, key, why, wrong,
             rules=[rule], uid=uid, tech=["subject-first"], check=_one_with_number(want), **kw)


def practice_items():
    return [
        _fill("sv-p01", "q-sva-each", "Each of the students ___ given a certificate.", ["was", "were", "are", "have been"], "a",
              "'Each' is the subject and is singular; 'of the students' does not change that.",
              {"b": mistake("Plural verb chosen because 'students' sits next to the blank; the subject is 'each'."),
               "c": mistake("Plural present form, pulled by 'students'; the subject 'each' needs a singular verb."),
               "d": mistake("'Have been' is plural; 'each' needs 'has been' or 'was'.")}, "sva-r1", "sing"),
        _fill("sv-p02", "q-sva-each", "Every boy and every girl in the class ___ invited to the party.", ["were", "was", "are", "have been"], "b",
              "Every before each noun keeps the subject singular even though 'and' joins two nouns.",
              {"a": mistake("Plural verb chosen because 'and' joins two nouns; 'every' before each noun keeps it singular."),
               "c": mistake("Plural present verb, with the same pull from 'and'; the sentence is also in the past."),
               "d": mistake("'Have been' is plural; 'every' needs a singular verb.")}, "sva-r1", "sing"),
        _fill("sv-p03", "q-sva-nearer", "Neither the teacher nor the students ___ aware of the change.", ["was", "is", "were", "has been"], "c",
              "The subject nearer to the verb is 'students' (plural), so the verb is plural.",
              {"a": mistake("Singular verb chosen to agree with 'teacher', the first subject, instead of the nearer 'students'."),
               "b": mistake("Singular verb agreeing with 'teacher', the first subject, instead of the nearer 'students'."),
               "d": mistake("Singular again, agreeing with 'teacher' rather than the nearer plural 'students'.")}, "sva-r3", "plur"),
        _fill("sv-p04", "q-sva-nearer", "Either the children or their mother ___ going to attend the function.", ["are", "is", "were", "have been"], "b",
              "The nearer subject is 'mother' (singular), so the verb is singular.",
              {"a": mistake("Plural verb chosen to agree with 'children', the first subject, not the nearer 'mother'."),
               "c": mistake("Plural past verb agreeing with 'children'; the nearer subject 'mother' is singular."),
               "d": mistake("Plural verb agreeing with 'children' rather than the nearer 'mother'.")}, "sva-r3", "sing"),
        _fill("sv-p05", "q-sva-number", "The number of unemployed youth ___ increasing every year.", ["are", "is", "were", "have been"], "b",
              "The subject is 'the number', which is singular.",
              {"a": mistake("Plural verb chosen because 'youth' is read as the subject; after 'the number of' the subject is 'number'."),
               "c": mistake("Plural past verb: 'the number of' is singular, and 'every year' calls for the present."),
               "d": mistake("Plural verb agreeing with 'youth'; the subject is the singular 'number'.")}, "sva-r6", "sing"),
        _fill("sv-p06", "q-sva-number", "A number of passengers ___ waiting at the gate.", ["is", "was", "are", "has been"], "c",
              "'A number of' means 'many', so the subject is plural.",
              {"a": mistake("Singular verb, as if the subject were 'the number'; 'a number of' means many and is plural."),
               "b": mistake("Singular past verb, treating 'a number' as one count; it means many and is plural."),
               "d": mistake("Singular verb: 'a number of passengers' is plural.")}, "sva-r6", "plur"),
        _fill("sv-p07", "q-sva-phrase", "The principal, along with the teachers, ___ attending the seminar.", ["are", "is", "were", "have been"], "b",
              "The phrase 'along with the teachers' does not add to the subject; 'principal' is singular.",
              {"a": mistake("Plural verb pulled by 'teachers', the noun inside the 'along with' phrase."),
               "c": mistake("Plural past verb pulled by 'teachers'; the real subject is 'principal'."),
               "d": mistake("Plural verb pulled by 'teachers'; 'along with' does not make the subject plural.")}, "sva-r7", "sing"),
        _fill("sv-p08", "q-sva-phrase", "The captain as well as the players ___ delighted with the win.", ["was", "were", "are", "have been"], "a",
              "'As well as the players' is an extra phrase; the subject is the singular 'captain'.",
              {"b": mistake("Plural verb pulled by 'players' in the 'as well as' phrase."),
               "c": mistake("Plural present verb pulled by 'players'; the sentence is also in the past."),
               "d": mistake("Plural verb pulled by 'players'; the subject is the singular 'captain'.")}, "sva-r7", "sing"),
    ]


S1, S2, S3 = "2025-09-12-S1", "2025-09-12-S2", "2025-09-12-S3"
_SPOT = "Find the part of the sentence that contains an error:\n"

PYQS = [
    q("q-sva-spot", "spot-error", _SPOT + "That the report overlooked several underlying causes / behind the public unrest were surprising / given the volume of evidence / collected over the past few months.",
      ["That the report overlooked several underlying causes", "behind the public unrest were surprising", "given the volume of evidence", "collected over the past few months"], "b",
      "'That the report overlooked several underlying causes behind the public unrest' is one noun clause acting as the subject, so the verb must be singular: 'was surprising'. 'Were' is wrong.",
      {"a": ruled_out("This is the start of the subject clause and is correct in itself."),
       "c": ruled_out("'Given the volume of evidence' is a phrase of reason and has no agreement problem."),
       "d": ruled_out("'Collected over the past few months' is a participle phrase about the evidence and is correct.")},
      rules=["sva-r8"], paper=S1, qno=83, tech=["subject-first"], trick="A 'That ...' clause is one singular subject."),
    q("q-sva-spot", "spot-error", _SPOT + "Much of what seems to be coordination / among the regulatory bodies and private stakeholders / are, in reality, coincidental overlaps / arising from differing mandates.",
      ["Much of what seems to be coordination", "among the regulatory bodies and private stakeholders", "are, in reality, coincidental overlaps", "arising from differing mandates"], "c",
      "The subject is 'much', which is singular, so the verb should be 'is'. 'Overlaps' is the complement and does not decide the number.",
      {"a": ruled_out("The subject 'much of what seems to be coordination' is correctly built."),
       "b": ruled_out("'Among the regulatory bodies and private stakeholders' is a prepositional phrase and has no verb to disagree."),
       "d": ruled_out("'Arising from differing mandates' is a participle phrase and is correct.")},
      rules=["sva-r9"], paper=S2, qno=94, tech=["subject-first"], trick="'Much' is singular: are becomes is."),
    q("q-sva-spot", "spot-error", _SPOT + "The report's focus on tech-utopianism, though praiseworthy, / ignore the deep-rooted inequities / that continue in data availability and digital competence / across demographic and regional gaps.",
      ["The report's focus on tech-utopianism, though praiseworthy,", "ignore the deep-rooted inequities", "that continue in data availability and digital competence", "across demographic and regional gaps"], "b",
      "The subject is the singular 'focus', so the verb must be 'ignores'. 'Tech-utopianism' and the 'though' phrase sit in between but do not change the number.",
      {"a": ruled_out("This part is the subject and the interrupting phrase and has no error."),
       "c": mistake("'That continue' looks wrong next to singular nouns, but its subject is the plural 'inequities', so 'continue' is correct."),
       "d": ruled_out("'Across demographic and regional gaps' is a prepositional phrase and is correct.")},
      rules=["sva-r10"], paper=S3, qno=93, tech=["subject-first"], trick="Strike the commas and 'on ...': focus ignores."),
    q("q-sva-inverted", "fill", "Select the correct option to fill in the blank.\nSo fragile ___ the talks that one disclosure could sabotage them.",
      ["are", "were", "is", "was"], "b",
      "The talks (plural) follow the blank, so the verb is plural. The sentence also uses 'could', a past form, so 'were' matches the tense.",
      {"a": mistake("'Are' agrees with 'talks' but is present, while 'could sabotage' sets the sentence in the past."),
       "c": mistake("Singular verb agreeing with 'fragile' instead of the plural subject 'talks' that follows."),
       "d": mistake("Singular past verb: the tense is right, but the subject 'talks' is plural.")},
      rules=["sva-r11"], paper=S3, qno=96, tech=["subject-first"],
      caution="'Are' agrees with 'talks' too, and a present-tense reading is grammatical. The printed key (were) rests on matching the past 'could'. Treat it as the answer expected in the exam, not as the only possible grammar."),
]
