"""Subject-verb agreement. Seed tier.
Grammar answers are grounded in a stated rule. The one machine check: of the four verb options, exactly one has the number
the rule demands (so no item can have two defensible answers by number)."""
from bank import mistake, ruled_out, q

TOPIC = "subject-verb-agreement"
TIER = "seed"
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


PYQS = []
