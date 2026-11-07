"""Question tags. Seed tier: no tag question appeared in the three papers analysed so far, but Plinth to Paramount gives it a
chapter and SSC papers test it as a fill-in. The pattern is mechanical, so a machine check is possible on the polarity."""
from bank import mistake, ruled_out, q

TOPIC = "question-tags"
TIER = "seed"
PREFIX = "qt"

NODES = {
    "q-qt-tag": {"short": "The tag", "label": "Choose the question tag", "kind": "qtype", "parent": TOPIC, "order": 1,
                 "summary": "Match the auxiliary and the subject, and turn the polarity the other way.", "links": []},
    "q-qt-collective": {"short": "Collective nouns", "label": "One unit (singular tag) or its members (plural tag)", "kind": "qtype", "parent": TOPIC, "order": 2,
                          "summary": "A collective noun acting as one body takes a singular tag (it); the same noun describing its members acting separately takes a plural tag (they).", "links": []},
    "q-qt-there": {"short": "There is/are", "label": "'There' as the subject", "kind": "qtype", "parent": TOPIC, "order": 3,
                     "summary": "When 'there' is the grammatical subject (there is, there were), the tag repeats 'there', not a pronoun for the noun that follows.", "links": []},
}

RULES = [
    {"id": "qt-r1", "node": "q-qt-tag", "text": "A positive statement takes a negative tag and a negative statement takes a positive one. The tag repeats the statement's auxiliary and replaces the subject with a pronoun: She is coming, isn't she?",
     "ok": "She is coming, isn't she? He cannot swim, can he?", "bad": "She is coming, is she? He cannot swim, cannot he?"},
    {"id": "qt-r2", "node": "q-qt-tag", "text": "If the statement has no auxiliary, the tag uses do, does or did to match the tense: He works here, doesn't he? They left early, didn't they?",
     "ok": "He works here, doesn't he?", "bad": "He works here, isn't he?"},
    {"id": "qt-r3", "node": "q-qt-tag", "text": "Words that are already negative in sense (never, hardly, scarcely, seldom, nobody, nothing, few, little) make the statement negative, so the tag is positive.",
     "ok": "He hardly speaks, does he? Nothing was lost, was it?", "bad": "He hardly speaks, doesn't he?"},
    {"id": "qt-r4", "node": "q-qt-tag", "text": "Three forms are fixed: 'Let us ...' takes 'shall we?', an imperative takes 'will you?', and 'I am ...' takes 'aren't I?'. 'Everyone', 'somebody' and 'nobody' are answered by 'they'.",
     "ok": "Let us begin, shall we? Open the door, will you? I am late, aren't I? Everyone came, didn't they?", "bad": "Let us begin, will we? I am late, amn't I?"},
    {"id": "qt-r5", "node": "q-qt-collective", "text": "A collective noun (jury, committee, team, family, audience) names one body acting as a single unit by default, so it takes a singular verb, a singular possessive (its) and a singular tag (it). The same noun takes a plural verb and tag only when the sentence is clearly about its members acting or feeling separately.",
     "ok": "The jury has reached its verdict, hasn't it?", "bad": "The jury have reached their verdict, haven't they? (unless the members' separate views are the point)."},
    {"id": "qt-r6", "node": "q-qt-there", "text": "When a sentence opens with 'there' as its grammatical subject (there is, there are, there were), the tag repeats 'there' with the matching auxiliary; it is not built from the noun that follows 'there'.",
     "ok": "There is no water left, is there?", "bad": "There is no water left, isn't it?"},
]

METHODS = {
    "q-qt-tag": {"cue": "A statement followed by a comma and a blank at the very end of the sentence.",
                 "standard": "Find the auxiliary (or supply do / does / did), flip the polarity, and put in the pronoun for the subject.",
                 "fast": "Positive statement, negative tag; negative statement, positive tag. Then check the auxiliary.",
                 "eliminate": "Drop every option whose polarity matches the statement, then every option with the wrong auxiliary.",
                 "traps": ["A hidden negative (hardly, never, nobody) which makes the statement negative.",
                           "'Let us' takes 'shall we', not 'will we'.", "'I am' takes 'aren't I'.",
                           "An imperative takes 'will you' whatever its own verb is."],
                 "rules": ["qt-r1", "qt-r2", "qt-r3", "qt-r4"], "tech": ["eliminate-pair"]},
    "q-qt-collective": {"cue": "A collective noun (jury, team, committee, family, audience) as the subject.",
                          "standard": "Decide whether the sentence treats the group as one body or names its members acting separately; pick the singular or plural tag to match.",
                          "fast": "By default: singular tag (it). Only a clear 'each member separately' sense switches it to 'they'.",
                          "eliminate": "Drop the plural tag unless the sentence gives a specific reason to read the group as separate individuals.",
                          "traps": ["Collective nouns look plural in meaning, so the eye reaches for 'they' by default, when 'it' is usually correct."],
                          "rules": ["qt-r5"], "tech": ["eliminate-pair"]},
    "q-qt-there": {"cue": "The sentence opens with 'There is', 'There are', 'There was' or 'There were'.",
                     "standard": "Keep 'there' as the tag's subject and match only the auxiliary's polarity and number.",
                     "fast": "There is/was ... -> isn't/wasn't there? There are/were ... -> aren't/weren't there?",
                     "eliminate": "Drop any tag built from the noun after 'there' instead of from 'there' itself.",
                     "traps": ["Reading the noun after 'there' (water, schools) as the real subject of the tag."],
                     "rules": ["qt-r6"], "tech": ["eliminate-pair"]},
}

REFS = []
WORDS = []
_F = "Select the correct question tag to complete the sentence.\n"


def _tag(uid, stem, opts, key, why, wrong, rules, rare=False):
    return q("q-qt-tag", "fill", _F + stem, opts, key, why, wrong, rules=list(rules), uid=uid, tech=["eliminate-pair"], rare=rare)


def practice_items():
    return [
        _tag("qt-p01", "She has finished the assignment, ___", ["has she?", "hasn't she?", "doesn't she?", "isn't she?"], "b",
             "The statement is positive and its auxiliary is 'has', so the tag is the negative 'hasn't she?'.",
             {"a": mistake("The polarity is not turned: a positive statement needs a negative tag."),
              "c": mistake("'Doesn't' is used only when the statement has no auxiliary of its own; here it has 'has'."),
              "d": ruled_out("'Isn't' changes the auxiliary from 'has' to 'is'.")}, ["qt-r1"]),
        _tag("qt-p02", "He works at the post office, ___", ["doesn't he?", "isn't he?", "does he?", "won't he?"], "a",
             "There is no auxiliary in the statement, so the tag supplies 'does' for the present tense, in the negative.",
             {"b": mistake("'Isn't he' assumes an auxiliary 'is', which the statement does not have."),
              "c": mistake("The polarity is not turned."),
              "d": ruled_out("'Won't' puts the tag in the future, which the statement is not.")}, ["qt-r2"]),
        _tag("qt-p03", "They left before the interval, ___", ["don't they?", "didn't they?", "did they?", "weren't they?"], "b",
             "The statement is in the simple past with no auxiliary, so the tag takes 'didn't'.",
             {"a": mistake("'Don't' is present; the statement is past."),
              "c": mistake("The polarity is not turned."),
              "d": ruled_out("'Weren't' assumes an auxiliary 'were', which the statement does not have.")}, ["qt-r2"]),
        _tag("qt-p04", "He hardly ever complains, ___", ["doesn't he?", "does he?", "did he?", "isn't he?"], "b",
             "'Hardly' makes the statement negative in sense, so the tag is positive: 'does he?'.",
             {"a": mistake("This treats the statement as positive, but 'hardly' has already made it negative."),
              "c": ruled_out("'Did' puts the tag in the past; the statement is in the present."),
              "d": ruled_out("'Isn't' changes the auxiliary and the polarity both.")}, ["qt-r3"], rare=True),
        _tag("qt-p05", "Nobody informed the warden, ___", ["didn't they?", "did they?", "did he?", "didn't he?"], "b",
             "'Nobody' is negative in sense, so the tag is positive, and 'nobody' is answered by 'they'.",
             {"a": mistake("This keeps the tag negative although 'nobody' has already made the statement negative."),
              "c": mistake("The polarity is right but 'nobody' takes 'they', not 'he'."),
              "d": ruled_out("Wrong on both counts: negative tag and the wrong pronoun.")}, ["qt-r3", "qt-r4"]),
        _tag("qt-p06", "Let us start the meeting, ___", ["will we?", "shall we?", "don't we?", "shan't we?"], "b",
             "'Let us' takes the fixed tag 'shall we?'.",
             {"a": mistake("'Will we' is the commonest wrong answer here; the fixed form is 'shall we'."),
              "c": ruled_out("'Don't we' does not follow a 'let us' sentence."),
              "d": ruled_out("'Shan't we' makes the tag negative, which 'let us' does not take.")}, ["qt-r4"]),
        _tag("qt-p07", "Shut the window, ___", ["won't you?", "will you?", "don't you?", "shall you?"], "b",
             "An imperative takes the fixed tag 'will you?'.",
             {"a": mistake("'Won't you' is used as an invitation, not as the ordinary tag on a command."),
              "c": ruled_out("'Don't you' does not follow an imperative."),
              "d": ruled_out("'Shall you' is not used as a tag.")}, ["qt-r4"]),
        _tag("qt-p08", "I am next in the queue, ___", ["amn't I?", "aren't I?", "am I?", "isn't it?"], "b",
             "'I am' takes the fixed tag 'aren't I?'.",
             {"a": ruled_out("'Amn't' is not a form used in English."),
              "c": mistake("The polarity is not turned."),
              "d": mistake("'Isn't it' is used in Indian English for every statement, but the tag must match the subject 'I'.")}, ["qt-r4"]),
        _tag("qt-p09", "You cannot drive without a licence, ___", ["can you?", "can't you?", "do you?", "could you?"], "a",
             "The statement is negative, so the tag is positive and keeps the auxiliary 'can'.",
             {"b": mistake("This repeats the negative instead of turning it."),
              "c": ruled_out("'Do' replaces the auxiliary 'can', which the statement already has."),
              "d": ruled_out("'Could' changes 'can' into a past form.")}, ["qt-r1"]),
        _tag("qt-p10", "Everyone has signed the register, ___", ["hasn't he?", "haven't they?", "has he?", "didn't they?"], "b",
             "'Everyone' is answered by 'they', and the positive statement with 'has' takes the negative tag 'haven't they?'.",
             {"a": mistake("'He' agrees with the singular verb but 'everyone' is answered by 'they' in a tag."),
              "c": mistake("The polarity is not turned, and the pronoun is wrong."),
              "d": ruled_out("'Didn't' changes the tense from the present perfect to the past.")}, ["qt-r4", "qt-r1"], rare=True),
        q("q-qt-collective", "fill", _F + "The jury has announced its verdict, ___", ["haven't they?", "hasn't it?", "hasn't he?", "haven't we?"], "b",
          "The jury is treated as one body here (its verdict), so the tag is singular and uses 'it': hasn't it?",
          {"a": mistake("'Haven't they' treats the jury as separate members, but the sentence's own 'its' already marks it as one body."),
           "c": ruled_out("'He' does not fit a group noun like 'jury'."), "d": ruled_out("'We' does not fit a tag at all; the speaker is not part of the jury.")},
          rules=["qt-r5"], uid="qt-p11", tech=["eliminate-pair"]),
        q("q-qt-collective", "fill", _F + "The committee are divided in their opinion on the merger, ___", ["isn't it?", "aren't they?", "doesn't it?", "won't it?"], "b",
          "'Divided in their opinion' shows the committee's members disagreeing separately, so the tag is plural: aren't they?",
          {"a": mistake("'Isn't it' treats the committee as one unit, but 'divided in their opinion' is exactly the case where it is read as separate members."),
           "c": ruled_out("'Doesn't' does not match the auxiliary 'are'."), "d": ruled_out("'Won't' puts the tag in the future, which the statement is not.")},
          rules=["qt-r5"], uid="qt-p12", tech=["eliminate-pair"], rare=True),
        q("q-qt-collective", "fill", _F + "My family has decided to move to Pune, ___", ["haven't they?", "hasn't it?", "hasn't she?", "doesn't it?"], "b",
          "'Family' naming one household acting as a single unit (one decision) takes a singular tag: hasn't it?",
          {"a": mistake("'Haven't they' reads 'family' as separate members, but the sentence describes one shared decision."),
           "c": ruled_out("'She' does not fit a group noun like 'family'."), "d": ruled_out("'Doesn't' does not match the auxiliary 'has'.")},
          rules=["qt-r5"], uid="qt-p13", tech=["eliminate-pair"]),
        q("q-qt-there", "fill", _F + "There is no shortcut to success, ___", ["isn't it?", "is there?", "isn't there?", "are there?"], "b",
          "'There' is the subject, so the tag repeats 'there'; 'no shortcut' already makes the statement negative in sense (like 'nothing' or 'nobody'), so the tag turns positive: is there?",
          {"a": mistake("'Isn't it' is built on 'it' instead of the true subject 'there', and also keeps the statement's negative sense in the tag."),
           "c": mistake("'There' is correctly used, but 'no' has already made the statement negative, so the tag must be positive, not negative."),
           "d": ruled_out("'Are there' does not match the singular 'is'.")},
          rules=["qt-r6", "qt-r3"], uid="qt-p14", tech=["eliminate-pair"]),
        q("q-qt-there", "fill", _F + "There weren't enough chairs for everyone, ___", ["was there?", "were there?", "weren't there?", "wasn't it?"], "b",
          "The statement is negative ('weren't'), so the tag turns positive, and it repeats 'there' with the matching plural auxiliary: were there?",
          {"a": ruled_out("'Was there' does not match the plural auxiliary the statement uses ('weren't')."),
           "c": mistake("This keeps the negative polarity instead of turning it positive."),
           "d": ruled_out("'Wasn't it' is singular, keeps the negative, and is built on 'it' instead of 'there'.")},
          rules=["qt-r6"], uid="qt-p15", tech=["eliminate-pair"]),
    ]


PYQS = [
    q("q-qt-tag", "spot-error", "The following sentence has been split into four segments. Identify the segment that contains a grammatical error. If there is no error, select option d.\n"
      "The board, despite reiterating its commitment to humane restructuring, / has not approved the proposed retrenchment pause, / do they, given the present credit-watch outlook?",
      ["The board, despite reiterating its commitment to humane restructuring,", "has not approved the proposed retrenchment pause,", "do they, given the present credit-watch outlook?", "No error"], "c",
      "'The board' is a collective noun acting as one body, so its tag pronoun must be singular ('it'), and the statement is negative ('has not approved'), so the tag must be positive: the correct tag is 'has it', not 'do they'.",
      {"a": ruled_out("'The board, despite reiterating its commitment to humane restructuring,' is a correctly built opening clause."),
       "b": ruled_out("'Has not approved the proposed retrenchment pause,' is a correct negative verb phrase."),
       "d": mistake("This says there is no error, but the tag is wrong on two counts: it should be the positive, singular 'has it', not the negative, plural 'do they'.")},
      rules=["qt-r1", "qt-r5"], paper="2026-10-09", qno=96, tech=["eliminate-pair"]),
]
