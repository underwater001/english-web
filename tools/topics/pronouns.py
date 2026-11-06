"""Pronouns: case, agreement, reflexives and relatives. Seed tier: no pronoun question appeared in the three papers analysed so far,
so this topic is built from the rules and drilled, not from a filed question."""
from bank import mistake, ruled_out, q

TOPIC = "pronouns"
TIER = "seed"
PREFIX = "pn"

NODES = {
    "q-pn-case": {"short": "I or me", "label": "Subject and object forms", "kind": "qtype", "parent": TOPIC, "order": 1,
                  "summary": "I, he, she, we, they do the action; me, him, her, us, them receive it or follow a preposition.", "links": []},
    "q-pn-agree": {"short": "Agreement", "label": "Agreement with the noun it stands for", "kind": "qtype", "parent": TOPIC, "order": 2,
                   "summary": "Each, every, everyone, nobody and a singular noun take a singular pronoun.", "links": ["subject-verb-agreement"]},
    "q-pn-reflexive": {"short": "Reflexives", "label": "Myself, himself, themselves", "kind": "qtype", "parent": TOPIC, "order": 3,
                       "summary": "A reflexive is used only when the doer and the receiver are the same, or for emphasis.", "links": []},
    "q-pn-relative": {"short": "Who / which", "label": "Relative pronouns", "kind": "qtype", "parent": TOPIC, "order": 4,
                      "summary": "Who for people, which for things, that for either, whose for possession, whom as an object.", "links": []},
}

RULES = [
    {"id": "pn-r1", "node": "q-pn-case", "text": "After a preposition, and as the object of a verb, use the object form: between you and me, for him and me. The subject form (I, he, she, we, they) is used only when the pronoun does the action.",
     "ok": "Between you and me; he invited my brother and me.", "bad": "Between you and I; he invited my brother and I."},
    {"id": "pn-r2", "node": "q-pn-case", "text": "After 'than' and 'as ... as' in a comparison, the pronoun takes the form it would have if the verb were written out: she is taller than I (am), not than me, in formal use.",
     "ok": "He works harder than I do.", "bad": "He works harder than me do."},
    {"id": "pn-r3", "node": "q-pn-agree", "text": "Each, every, everyone, everybody, nobody, anyone, either and neither are singular, so the pronoun that refers back is his, her or his or her, and the verb is singular.",
     "ok": "Everyone must bring his or her own pen.", "bad": "Everyone must bring their own pen (in exam grammar)."},
    {"id": "pn-r4", "node": "q-pn-reflexive", "text": "A reflexive (myself, himself, themselves) is correct only when it refers back to the subject of the same clause, or when it is added for emphasis. It is never used in place of a plain subject or object pronoun.",
     "ok": "He hurt himself. I myself saw it.", "bad": "Myself will attend. He invited my friend and myself."},
    {"id": "pn-r5", "node": "q-pn-relative", "text": "Use 'who' for people and 'which' for things; 'that' can do either but is not used after a comma. 'Whom' is the object form, used after a verb or a preposition.",
     "ok": "The officer who signed it; the file which was lost; the man to whom I spoke.", "bad": "The officer which signed it; the man to who I spoke."},
    {"id": "pn-r6", "node": "q-pn-relative", "text": "Make sure a pronoun has exactly one possible noun to refer to. If two nouns could be meant, name the noun again instead of using a pronoun.",
     "ok": "When Ravi met Arun, Ravi was in a hurry.", "bad": "When Ravi met Arun, he was in a hurry (who was?)."},
]

METHODS = {
    "q-pn-case": {"cue": "A blank or an underlined pronoun after a preposition, after 'and', or after 'than'.",
                  "standard": "Drop the other name and read the sentence with the pronoun alone: 'he invited me' tells you at once that 'me' is right.",
                  "fast": "A pronoun straight after a preposition is always the object form.",
                  "eliminate": "Cross out the subject forms whenever the pronoun is not doing the action.",
                  "traps": ["'Between you and I' sounds polite but is wrong.", "'Than me' and 'than I' differ; exam keys take the subject form in formal comparison."],
                  "rules": ["pn-r1", "pn-r2"], "tech": ["subject-first"]},
    "q-pn-agree": {"cue": "Everyone, each, nobody or a singular noun early in the sentence, with a pronoun later.",
                   "standard": "Find the noun the pronoun stands for and match its number and person.",
                   "fast": "Everyone, each, nobody: singular pronoun.",
                   "eliminate": "Drop plural pronouns when the noun they point back to is singular.",
                   "traps": ["'Their' after 'everyone' is normal in speech but marked wrong in these papers.", "A plural noun inside an 'of' phrase pulls the pronoun to the plural."],
                   "rules": ["pn-r3"], "tech": ["subject-first"]},
    "q-pn-reflexive": {"cue": "Myself, himself or themselves in a place where a plain pronoun would do.",
                       "standard": "Check whether the reflexive refers back to the subject of its own clause. If not, replace it with I, me, he or him.",
                       "fast": "No subject to refer back to means no reflexive.",
                       "eliminate": "Remove options that use a reflexive as a subject.",
                       "traps": ["'Myself' used politely as a subject or after 'and'.", "'Themself' is not used in these papers; 'themselves' is."],
                       "rules": ["pn-r4"], "tech": ["read-whole"]},
    "q-pn-relative": {"cue": "A blank joining two clauses, with who, whom, which, that or whose among the options.",
                      "standard": "Decide whether the noun before the blank is a person or a thing, then whether the pronoun is the subject or the object of its clause.",
                      "fast": "A verb straight after the blank means the subject form (who); a subject straight after means the object form (whom).",
                      "eliminate": "Drop 'that' after a comma and 'which' after a person.",
                      "traps": ["'Who' used where 'whom' is needed after a preposition.", "'Whose' confused with 'who's'.", "A pronoun with two possible nouns to refer to."],
                      "rules": ["pn-r5", "pn-r6"], "tech": ["read-whole"]},
}

REFS = []
WORDS = []
_F = "Select the most appropriate option to fill in the blank.\n"
_S = "Find the part of the sentence that contains an error:\n"
_I = "Choose the most suitable option to replace the highlighted part of the sentence:\n"


def practice_items():
    return [
        q("q-pn-case", "fill", _F + "This matter is strictly between you and ___.", ["I", "me", "myself", "mine"], "b",
          "After the preposition 'between' the object form is needed: between you and me.",
          {"a": mistake("'Between you and I' is the best-known error of this kind; 'between' is a preposition and takes 'me'."),
           "c": mistake("'Myself' has no subject in this clause to refer back to, so a reflexive cannot be used here."),
           "d": ruled_out("'Mine' is possessive and would mean 'the thing belonging to me'.")}, rules=["pn-r1"], uid="pn-p01", tech=["subject-first"]),
        q("q-pn-case", "fill", _F + "The principal congratulated my partner and ___ on the result.", ["I", "me", "myself", "mine"], "b",
          "Drop 'my partner and' and the sentence reads 'congratulated me', so the object form is right.",
          {"a": mistake("'And I' is chosen because it sounds more careful, but the pronoun here receives the action."),
           "c": mistake("A reflexive after 'and' is a common politeness error; the subject of the clause is the principal, not me."),
           "d": ruled_out("'Mine' is possessive and does not fit as the object of 'congratulated'.")}, rules=["pn-r1"], uid="pn-p02", tech=["subject-first"]),
        q("q-pn-agree", "fill", _F + "Each of the candidates must bring ___ own documents.", ["their", "his or her", "them", "theirs"], "b",
          "'Each' is singular, so the pronoun referring back to it is singular.",
          {"a": mistake("'Their' after 'each' is normal in speech, but these papers treat 'each' as singular."),
           "c": ruled_out("'Them' is an object form and cannot stand before 'own documents'."),
           "d": ruled_out("'Theirs' is possessive and stands alone, so it cannot be followed by a noun.")}, rules=["pn-r3"], uid="pn-p03", tech=["subject-first"]),
        q("q-pn-agree", "spot-error", _S + "Every student in the two sections / has submitted their assignment / to the class teacher / before the deadline.",
          ["Every student in the two sections", "has submitted their assignment", "to the class teacher", "before the deadline"], "b",
          "'Every student' is singular, so the pronoun must be 'his or her assignment'.",
          {"a": ruled_out("'Every student in the two sections' is a correctly built singular subject."),
           "c": ruled_out("'To the class teacher' is a prepositional phrase and holds no pronoun error."),
           "d": ruled_out("'Before the deadline' is a phrase of time.")}, rules=["pn-r3"], uid="pn-p04", tech=["subject-first"]),
        q("q-pn-reflexive", "improve", _I + "[[Myself and my brother]] will attend the function.",
          ["My brother and I", "Myself and my brother", "Me and my brother", "My brother and myself"], "a",
          "The pronoun is the subject, so it takes 'I', and the courteous order puts the other person first.",
          {"b": mistake("'Myself' cannot be a subject; there is no earlier subject for it to refer back to."),
           "c": mistake("'Me' is the object form and cannot be the subject of 'will attend'."),
           "d": mistake("A reflexive after 'and' is still a reflexive with nothing to refer back to.")}, rules=["pn-r4"], uid="pn-p05", tech=["read-whole"]),
        q("q-pn-reflexive", "spot-error", _S + "The manager asked the clerk / to send the papers / to the auditor and myself / by Friday evening.",
          ["The manager asked the clerk", "to send the papers", "to the auditor and myself", "by Friday evening"], "c",
          "The subject of the clause is 'the clerk', not the speaker, so the reflexive has nothing to refer back to; it should be 'and me'.",
          {"a": ruled_out("'The manager asked the clerk' is a correct main clause."),
           "b": ruled_out("'To send the papers' is a correct infinitive with its object."),
           "d": ruled_out("'By Friday evening' is a phrase of time.")}, rules=["pn-r4"], uid="pn-p06", tech=["read-whole"]),
        q("q-pn-relative", "fill", _F + "The officer ___ signed the order has been transferred.", ["which", "who", "whom", "whose"], "b",
          "The noun is a person and the pronoun is the subject of 'signed', so 'who' is right.",
          {"a": mistake("'Which' is used for things, not for a person."),
           "c": mistake("'Whom' is the object form, but here the pronoun does the signing."),
           "d": ruled_out("'Whose' shows possession and would need a noun after it.")}, rules=["pn-r5"], uid="pn-p07", tech=["read-whole"]),
        q("q-pn-relative", "fill", _F + "This is the colleague to ___ I handed the file.", ["who", "whom", "which", "whose"], "b",
          "After a preposition the object form is used: to whom I handed the file.",
          {"a": mistake("'To who' keeps the subject form after a preposition, which formal grammar does not allow."),
           "c": ruled_out("'Which' is for things, and a colleague is a person."),
           "d": ruled_out("'Whose' shows possession and would need a noun after it.")}, rules=["pn-r5"], uid="pn-p08", tech=["read-whole"]),
        q("q-pn-relative", "improve", _I + "When Ravi met Arun, [[he was in a hurry]].",
          ["Ravi was in a hurry", "he was in a hurry", "he himself was in a hurry", "that he was in a hurry"], "a",
          "'He' could mean either man, so the noun is repeated to make the reference certain.",
          {"b": mistake("Leaving 'he' in keeps the ambiguity: either Ravi or Arun could be meant."),
           "c": mistake("Adding 'himself' emphasises the pronoun but still does not say which man is meant."),
           "d": ruled_out("'That he was in a hurry' turns the clause into a noun clause with nothing to attach to.")}, rules=["pn-r6"], uid="pn-p09", tech=["read-whole"]),
        q("q-pn-case", "fill", _F + "My sister sings far better than ___.", ["me", "I", "myself", "mine"], "b",
          "The comparison is with the full clause 'than I do', so the subject form is used in formal grammar.",
          {"a": mistake("'Than me' is normal in conversation, but exam keys expect the form that would stand before the understood verb."),
           "c": mistake("A reflexive has nothing to refer back to in this clause."),
           "d": ruled_out("'Mine' is possessive and would compare her singing with a thing of mine.")},
          rules=["pn-r2"], uid="pn-p10", tech=["subject-first"], rare=True,
          caution="Everyday English allows 'than me'. These papers follow the older rule, which supplies the verb: than I (do)."),
        q("q-pn-agree", "improve", _I + "Neither of the two sisters has brought [[their]] certificate.",
          ["her", "their", "theirs", "her own their"], "a",
          "'Neither' is singular and both people are women, so the pronoun is 'her'.",
          {"b": mistake("'Their' is plural and does not agree with the singular 'neither'."),
           "c": ruled_out("'Theirs' stands alone and cannot be followed by 'certificate'."),
           "d": ruled_out("This mixes two pronouns together and is not possible English.")}, rules=["pn-r3"], uid="pn-p11", tech=["subject-first"]),
        q("q-pn-relative", "spot-error", _S + "The committee rejected the proposal, / that had been submitted / without the supporting papers, / at its first meeting.",
          ["The committee rejected the proposal,", "that had been submitted", "without the supporting papers,", "at its first meeting"], "b",
          "'That' is not used after a comma; the clause adds information, so it needs 'which had been submitted'.",
          {"a": ruled_out("'The committee rejected the proposal' is a correct main clause."),
           "c": ruled_out("'Without the supporting papers' is a correct prepositional phrase."),
           "d": ruled_out("'At its first meeting' is correct, with a singular pronoun for the committee.")}, rules=["pn-r5"], uid="pn-p12", tech=["read-whole"]),
    ]


PYQS = []
