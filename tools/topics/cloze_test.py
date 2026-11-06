"""Cloze test: a short paragraph with numbered blanks, each blank a four-option question. Seed tier: the three papers analysed so far
used a reading passage instead of a cloze, so this topic is built from the rules and drilled, not from a filed question.
The paragraphs are written by us. Each question shows the paragraph with the blank in question marked."""
from bank import mistake, ruled_out, q

TOPIC = "cloze-test"
TIER = "seed"
PREFIX = "cz"

NODES = {
    "q-cz-grammar": {"short": "Grammar blank", "label": "A blank the grammar decides", "kind": "qtype", "parent": TOPIC, "order": 1,
                     "summary": "A preposition, article, conjunction or verb form that the sentence around it forces.", "links": []},
    "q-cz-sense": {"short": "Meaning blank", "label": "A blank the meaning decides", "kind": "qtype", "parent": TOPIC, "order": 2,
                   "summary": "Four possible words; the sense of the paragraph picks one.", "links": ["contextual-vocabulary"]},
}

RULES = [
    {"id": "cz-r1", "node": "q-cz-grammar", "text": "Read the whole paragraph once before filling anything. A cloze is one connected piece of writing, so a later sentence often settles an earlier blank.",
     "ok": "Reading on shows the paragraph is about a past event, which fixes every verb tense in it.", "bad": "Filling blank 1 from blank 1's sentence alone."},
    {"id": "cz-r2", "node": "q-cz-grammar", "text": "Settle the grammar blanks first: a blank after a preposition takes a noun or an -ing form, a blank between two clauses takes a conjunction, and every verb must match the tense the paragraph has already set.",
     "ok": "He succeeded in winning the seat.", "bad": "He succeeded in win the seat."},
    {"id": "cz-r3", "node": "q-cz-sense", "text": "For a meaning blank, decide first whether the sentence is going the same way as the one before it or turning against it. A contrast word (but, however, yet) means the blank must reverse the earlier idea.",
     "ok": "The scheme was generous; in practice, however, it reached very few.", "bad": "The scheme was generous; in practice, however, it reached many."},
    {"id": "cz-r4", "node": "q-cz-sense", "text": "Put each option back in and read the whole sentence aloud. Keep the one that fits both the meaning and the words it has to combine with, since many English words take only one partner (take a decision, make a mistake, pay attention).",
     "ok": "The committee took a decision.", "bad": "The committee did a decision."},
]

METHODS = {
    "q-cz-grammar": {"cue": "A paragraph with numbered blanks; the options for this blank are prepositions, articles, conjunctions or verb forms.",
                     "standard": "Read the paragraph through once. Fix the tense the paragraph is in, then fill the blank with the form the sentence around it forces.",
                     "fast": "Look only at the two or three words on each side of the blank: they usually decide a grammar blank by themselves.",
                     "eliminate": "Cross out the options whose form cannot stand in that slot at all, then choose between what is left.",
                     "traps": ["Filling blanks in order instead of doing the easy ones first.", "Ignoring the tense the rest of the paragraph has set.",
                               "A preposition that fits the single sentence but not the fixed phrase the writer is using."],
                     "rules": ["cz-r1", "cz-r2"], "tech": ["read-whole", "back-substitute"]},
    "q-cz-sense": {"cue": "A paragraph with numbered blanks; the options for this blank are four different words of the same part of speech.",
                   "standard": "Decide from the sentence before whether the idea continues or turns, then pick the word that carries that direction and takes the right partner words.",
                   "fast": "Find the connector (but, so, because, however) nearest the blank; it tells you which way the meaning runs.",
                   "eliminate": "Drop words whose tone is wrong for the paragraph, then drop any that do not combine with the noun or verb beside them.",
                   "traps": ["Two options with nearly the same meaning: one of them will not fit the words around it.", "Choosing the hardest-looking word instead of the one that fits."],
                   "rules": ["cz-r3", "cz-r4"], "tech": ["context-clue", "back-substitute"]},
}

REFS = []
WORDS = []

_P1 = ("For most of the last century the bicycle was treated in Indian cities as a vehicle for those who could afford __1__ else. "
       "Road width went to cars, and the cyclist was pushed to the broken edge of the carriageway. That assumption is now being "
       "questioned, __2__ because of any affection for the bicycle, but because the arithmetic of space has become impossible to "
       "ignore: a lane of cars moves a few thousand people an hour, while the same lane given to cycles moves several times as many. "
       "Cities that have __3__ the change report a further gain they had not counted on. Shopkeepers on streets closed to cars at first "
       "__4__ the plan, and then found their takings rising, because a cyclist stops where a driver passes by. The lesson is modest but "
       "useful: street space is not a fixed quantity to be shared out, and what a street carries __5__ on how it is arranged.")

_P2 = ("Weather forecasting improved more in the last forty years than in the four centuries before them, and almost none of that gain "
       "came from better instruments. It came from __1__ that the atmosphere obeys equations which a large enough computer can solve "
       "step by step. The method has one unavoidable weakness. A forecast begins from a picture of today's atmosphere, and that picture "
       "is never __2__; a small error in it grows as the calculation runs forward, until after about ten days the forecast says nothing "
       "at all. Forecasters live with this __3__ running the same model many times from slightly different starting pictures. Where the "
       "runs agree, the forecast is firm; where they scatter, it is not, __4__ a forecast is now given as a chance rather than a "
       "statement. The honest number is more useful than the confident one, __5__ it is harder to put on a television screen.")


def _c(uid, qtype, para, n, opts, key, why, wrong, rules, tech, rare=False):
    text = f"In the paragraph below, select the most appropriate option for blank {n}.\n\n" + para.replace(f"__{n}__", "[[___]]")
    for k in range(1, 6):
        text = text.replace(f"__{k}__", f"({k})")
    return q(qtype, "cloze", text, opts, key, why, wrong, rules=list(rules), tech=list(tech), uid=uid, rare=rare)


def practice_items():
    return [
        _c("cz-p01", "q-cz-sense", _P1, 1, ["anything", "nothing", "something", "everything"], "b",
           "The sentence means the bicycle was for people with no other choice, so 'could afford nothing else' is the sense required.",
           {"a": mistake("'Could afford anything else' reverses the meaning: it would describe people with money."),
            "c": ruled_out("'Something else' would mean they had another option, which contradicts 'pushed to the broken edge'."),
            "d": ruled_out("'Everything else' makes the sentence say they could afford all other vehicles.")},
           ["cz-r3"], ["context-clue"]),
        _c("cz-p02", "q-cz-grammar", _P1, 2, ["not", "and", "so", "yet"], "a",
           "The pattern is 'not because of X, but because of Y', so the blank takes 'not'.",
           {"b": ruled_out("'And because' would add a reason rather than deny one, and 'but' later in the sentence would have nothing to answer."),
            "c": ruled_out("'So because' puts two connectors together and is not possible English."),
            "d": mistake("'Yet because' reads as a contrast but leaves the following 'but because' without its partner.")},
           ["cz-r1", "cz-r2"], ["read-whole"]),
        _c("cz-p03", "q-cz-grammar", _P1, 3, ["make", "made", "making", "been made"], "b",
           "After 'have' the verb takes its past participle, so 'have made the change' is the only possible form.",
           {"a": ruled_out("'Have make' leaves the verb in its base form after 'have'."),
            "c": ruled_out("'Have making' would need 'been' between them."),
            "d": mistake("'Have been made' is passive, which would say the cities were made by somebody else.")},
           ["cz-r2"], ["back-substitute"]),
        _c("cz-p04", "q-cz-sense", _P1, 4, ["welcomed", "opposed", "ignored", "funded"], "b",
           "'At first ... and then found their takings rising' sets up a reversal, so the shopkeepers must have been against the plan to begin with.",
           {"a": mistake("'Welcomed' removes the reversal that 'at first ... and then' demands."),
            "c": ruled_out("'Ignored' gives no first position for the later discovery to overturn."),
            "d": ruled_out("'Funded' says the shopkeepers paid for the scheme, which the paragraph never suggests.")},
           ["cz-r3"], ["context-clue"]),
        _c("cz-p05", "q-cz-grammar", _P1, 5, ["depend", "depends", "depending", "depended"], "b",
           "The subject is 'what a street carries', a singular clause, and the paragraph is in the present, so the verb is 'depends'.",
           {"a": mistake("'Depend' is plural, pulled by the noun 'street' or by the earlier plurals in the sentence."),
            "c": ruled_out("'Depending' is not a finite verb and cannot be the verb of the clause."),
            "d": mistake("'Depended' moves the sentence into the past, while the rest of it is in the present.")},
           ["cz-r1", "cz-r2"], ["read-whole"]),
        _c("cz-p06", "q-cz-grammar", _P2, 1, ["realise", "realising", "realised", "realisation"], "b",
           "After the preposition 'from' the verb takes the -ing form: from realising that.",
           {"a": ruled_out("'From realise' puts a base verb after a preposition."),
            "c": ruled_out("'From realised' puts a past form after a preposition."),
            "d": mistake("'Realisation' is a noun and would need 'of' or 'that' handled differently: 'from the realisation that'.")},
           ["cz-r2"], ["back-substitute"]),
        _c("cz-p07", "q-cz-sense", _P2, 2, ["exact", "useful", "recent", "complete"], "a",
           "The next clause says a small error in the picture grows, so the picture is never exactly right.",
           {"b": mistake("'Never useful' contradicts the paragraph, which says the method improved forecasting greatly."),
            "c": ruled_out("'Never recent' makes no sense of a picture of today's atmosphere."),
            "d": mistake("'Complete' is close to the sense but the sentence is answered by 'a small error in it', which is about accuracy, not coverage.")},
           ["cz-r3", "cz-r4"], ["context-clue"], rare=True),
        _c("cz-p08", "q-cz-grammar", _P2, 3, ["by", "for", "with", "to"], "a",
           "The blank introduces the method used, so it takes 'by' with the -ing form: live with this by running the model many times.",
           {"b": ruled_out("'For running' would give a purpose rather than the means."),
            "c": ruled_out("'With running' does not form the means-expressing phrase that 'by' does."),
            "d": ruled_out("'To running' puts a preposition where an infinitive marker cannot go.")},
           ["cz-r2"], ["back-substitute"]),
        _c("cz-p09", "q-cz-sense", _P2, 4, ["because", "although", "which is why", "unless"], "c",
           "The scattering of the runs is the reason forecasts are now given as chances, so the blank introduces a consequence.",
           {"a": mistake("'Because' reverses cause and effect: the chance form follows from the scatter, not the other way round."),
            "b": mistake("'Although' makes it a contrast, but the two halves agree with each other."),
            "d": ruled_out("'Unless' sets a condition, and the sentence states no condition.")},
           ["cz-r1", "cz-r3"], ["connectors"]),
        _c("cz-p10", "q-cz-sense", _P2, 5, ["because", "even though", "so that", "as if"], "b",
           "The honest number being harder to present is a drawback set against its usefulness, so the blank marks a contrast.",
           {"a": mistake("'Because' would make the difficulty the reason for the usefulness, which reverses the sense."),
            "c": ruled_out("'So that' gives a purpose, and being hard to show on a screen is not a purpose."),
            "d": ruled_out("'As if' introduces a comparison, which the sentence is not making.")},
           ["cz-r3"], ["connectors"]),
    ]


PYQS = []
