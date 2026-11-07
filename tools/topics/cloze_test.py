"""Cloze test: a short paragraph with numbered blanks, each blank a four-option question. Quiz tier: the 07-Oct-2026 paper is the first
analysed paper that actually set a cloze (Q88-92, a 5-blank vocabulary passage on the Silk Road); its own passage is never copied here, so the
5 PYQ items are built on an original lighthouse-keeper paragraph of our own that fills the same blank slots with the same target words.
The paragraphs are written by us. Each question shows the paragraph with the blank in question marked."""
from bank import mistake, ruled_out, q

TOPIC = "cloze-test"
TIER = "quiz"
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


def _cq(uid, qtype, para, n, opts, key, why, wrong, rules, tech, paper, qno, rare=False):
    text = f"In the paragraph below, select the most appropriate option for blank {n}.\n\n" + para.replace(f"__{n}__", "[[___]]")
    for k in range(1, 6):
        text = text.replace(f"__{k}__", f"({k})")
    return q(qtype, "cloze", text, opts, key, why, wrong, rules=list(rules), tech=list(tech), uid=uid, rare=rare, paper=paper, qno=qno)


_P3 = ("Long before electric beacons made the work largely automatic, a lighthouse keeper's life was a test of endurance against an __1__ "
       "coastline, where a single storm could strip away a jetty overnight. The bond between the keeper and the ships that passed was quietly "
       "__2__: sailors trusted the beam to find safe water, and in turn every vessel that passed word ashore so that help could be sent if the "
       "light ever failed to appear. The coast offered little mercy to the __3__ traveller who misjudged the tide, and more than one rescue began "
       "only because a keeper's lamp had been left burning through a night when no ship was expected. For the families who grew up in these towers, "
       "the sound of the foghorn left an __4__ impression, one that no later, quieter life could ever fully erase. Even today, as satellite "
       "navigation has made the manned lighthouse all but obsolete, the keeper's solitary vigil still carries a strange __5__ for anyone who has "
       "ever waited, alone, for a signal that might not come.")

_P4 = ("After thirty years on the bench, Judge Ortiz had grown accustomed to the small rituals of a trial: the opening statements, the parade of "
       "exhibits, the occasional objection raised more as a __1__ than as a serious challenge to the evidence. What she found harder to grow "
       "accustomed to was the way a jury's first impression of a witness, once formed, tended to resist every later correction. A witness who "
       "seemed __2__ with the facts already established would be believed almost without question, while one whose account, however accurate, "
       "failed to fit the story the jury had already assembled in its mind would struggle to be heard at all. Jurors did not set out to be unfair; "
       "they simply became __3__ to detail that did not confirm what they had decided early on. The judge had come to doubt whether even an "
       "entirely __4__ slip, a wrong date, a misremembered colour, ever read as harmless once suspicion had taken hold. What she still believed, "
       "after all those years, was that a patient, __5__ witness, one who corrected their own small errors rather than cover them, usually won a "
       "jury over in the end, however long it took.")


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


PYQS = [
    _cq("cz-q88", "q-cz-sense", _P3, 1, ["hospitable", "tranquil", "inhospitable", "fertile"], "c",
        "A coastline that can 'strip away a jetty overnight' gives no comfort or shelter, so it is 'inhospitable', harsh and unwelcoming.",
        {"a": mistake("'Hospitable' is the direct opposite of the harsh coast the sentence goes on to describe."),
         "b": ruled_out("'Tranquil' says the coast is calm, but the sentence is about its power to destroy a jetty."),
         "d": ruled_out("'Fertile' describes land good for growing things, not a dangerous coastline.")},
        ["cz-r3", "cz-r4"], ["context-clue"], paper="2026-10-07", qno=88),
    _cq("cz-q89", "q-cz-sense", _P3, 2, ["unilateral", "reciprocal", "one-sided", "accidental"], "b",
        "The sentence describes a two-way exchange — sailors trust the beam, and ships send word back — so the bond is 'reciprocal', given and returned by both sides.",
        {"a": mistake("'Unilateral' means coming from one side only, which contradicts the 'and in turn' that follows."),
         "c": ruled_out("'One-sided' again denies the two-way exchange the sentence describes."),
         "d": ruled_out("'Accidental' says the bond happened by chance, not that it was returned on both sides.")},
        ["cz-r3", "cz-r4"], ["context-clue"], paper="2026-10-07", qno=89),
    _cq("cz-q90", "q-cz-sense", _P3, 3, ["vigilant", "wary", "cautious", "unwary"], "d",
        "A traveller who 'misjudged the tide' was not on guard against the danger, so the word needed is 'unwary', the one option meaning off guard; the other three all mean watchful, the opposite of what the sentence describes.",
        {"a": mistake("'Vigilant' means watchful, the opposite of a traveller who misjudges the tide."),
         "b": mistake("'Wary' also means on guard, which does not fit a traveller caught out by the tide."),
         "c": ruled_out("'Cautious' again means careful, not careless, so it does not fit the misjudging traveller.")},
        ["cz-r3", "cz-r4"], ["context-clue"], paper="2026-10-07", qno=90),
    _cq("cz-q91", "q-cz-sense", _P3, 4, ["fleeting", "indelible", "faint", "forgettable"], "b",
        "An impression 'no later, quieter life could ever fully erase' is one that cannot be rubbed out, so it is 'indelible', permanent.",
        {"a": mistake("'Fleeting' means brief, which contradicts an impression that can never be erased."),
         "c": ruled_out("'Faint' says the impression was weak, not that it lasted forever."),
         "d": ruled_out("'Forgettable' is the opposite sense: the sentence says the memory could never be erased.")},
        ["cz-r3", "cz-r4"], ["context-clue"], paper="2026-10-07", qno=91),
    _cq("cz-q92", "q-cz-sense", _P3, 5, ["resonance", "irrelevance", "obsolescence", "ambiguity"], "a",
        "Even though the lighthouse itself is 'all but obsolete', the image of a solitary vigil still strikes an emotional chord with the reader, which is its 'resonance', the lingering power to move someone.",
        {"b": mistake("'Irrelevance' says the image no longer matters, the opposite of 'still carries' something."),
         "c": ruled_out("'Obsolescence' repeats the earlier point about the lighthouse being outdated, not the feeling it still provokes."),
         "d": ruled_out("'Ambiguity' means being unclear in meaning, not striking an emotional chord.")},
        ["cz-r3", "cz-r4"], ["context-clue"], paper="2026-10-07", qno=92, rare=True),
    _cq("cz-q76", "q-cz-sense", _P4, 1, ["exculpation", "cavil", "imputation", "salience"], "b",
        "An objection raised without being a serious challenge is a 'cavil', a trivial or petty objection, matching 'more as a ... than as a serious challenge'.",
        {"a": ruled_out("'Exculpation' means clearing someone of blame, unrelated to raising an objection."),
         "c": mistake("'Imputation' means an accusation or suggestion of wrongdoing, not a trivial objection to evidence."),
         "d": ruled_out("'Salience' means being prominent or noticeable, which does not fit 'objection' at all.")},
        ["cz-r3", "cz-r4"], ["context-clue"], paper="2026-10-08", qno=76, rare=True),
    _cq("cz-q77", "q-cz-sense", _P4, 2, ["congruous", "refractory", "pellucid", "censorious"], "a",
        "A witness whose account matches what the jury already believes seems 'congruous' with it, meaning fitting or consistent.",
        {"b": mistake("'Refractory' means stubbornly resistant to control, which does not describe a witness's account matching the facts."),
         "c": ruled_out("'Pellucid' means extremely clear, describing how something is expressed, not whether it fits the established facts."),
         "d": ruled_out("'Censorious' means harshly critical, unrelated to whether an account fits the facts.")},
        ["cz-r3", "cz-r4"], ["context-clue"], paper="2026-10-08", qno=77, rare=True),
    _cq("cz-q78", "q-cz-sense", _P4, 3, ["inimical", "receptive", "obsequious", "impervious"], "d",
        "Jurors who stop noticing facts that contradict their first impression have become 'impervious' to that detail, meaning unaffected by it, resistant to letting it in.",
        {"a": mistake("'Inimical' means harmful or hostile, which overstates a juror's passive refusal to notice contrary detail."),
         "b": ruled_out("'Receptive' means open to new information, the opposite of what the sentence describes."),
         "c": ruled_out("'Obsequious' means excessively eager to please, unrelated to resisting information.")},
        ["cz-r3", "cz-r4"], ["context-clue"], paper="2026-10-08", qno=78, rare=True),
    _cq("cz-q79", "q-cz-sense", _P4, 4, ["innocuous", "recondite", "pernicious", "desultory"], "a",
        "A wrong date or misremembered colour is, in itself, a harmless slip, so the word needed is 'innocuous', meaning harmless, matching the sentence's own 'ever read as harmless'.",
        {"b": ruled_out("'Recondite' means obscure or hard to understand, not harmless."),
         "c": mistake("'Pernicious' means harmful in a gradual, damaging way, the opposite of the harmless slip the sentence describes."),
         "d": ruled_out("'Desultory' means lacking a plan or purpose, unrelated to whether a slip is harmless.")},
        ["cz-r3", "cz-r4"], ["context-clue"], paper="2026-10-08", qno=79, rare=True),
    _cq("cz-q80", "q-cz-sense", _P4, 5, ["verisimilar", "veracious", "prolix", "vituperative"], "b",
        "A witness who corrects their own small errors rather than hide them is being truthful, so the word needed is 'veracious', meaning truthful or honest.",
        {"a": mistake("'Verisimilar' means having the appearance of truth, which is not the same as actually being truthful."),
         "c": ruled_out("'Prolix' means tediously long-winded, unrelated to honesty."),
         "d": ruled_out("'Vituperative' means harshly abusive in language, unrelated to a witness correcting their own errors.")},
        ["cz-r3", "cz-r4"], ["context-clue"], paper="2026-10-08", qno=80, rare=True),
]
