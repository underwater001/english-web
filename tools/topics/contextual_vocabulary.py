"""Contextual vocabulary: pick the word that fits the sentence. 2 past questions and 10 original practice items.
Each key must be the stored word (checked); the fit itself rests on the cited rules (part of speech, then clue words)."""
from bank import mistake, ruled_out, q, word

TOPIC = "contextual-vocabulary"
TIER = "full"
PREFIX = "cv"

NODES = {
    "q-cv-fit": {"short": "Word in context", "label": "Fill the blank with the best word", "kind": "qtype", "parent": TOPIC, "order": 1,
                 "summary": "A sentence with a blank; pick the word whose meaning matches the clue words around it.", "links": ["synonyms-antonyms"]},
}

RULES = [
    {"id": "cv-r1", "node": "q-cv-fit", "text": "Check the part of speech first. If the blank needs a verb and one option is a noun, that option is out before meaning is even considered.",
     "ok": "'can ___ the inertia' needs a verb: dislodge, not 'persuasion'.", "bad": "Choosing a noun for a verb slot."},
    {"id": "cv-r2", "node": "q-cv-fit", "text": "Find the clue words (an adjective or a second clause) that say what the blank must do, then choose the word whose meaning does that. Words such as entrenched, covert, dissent and austerity point to the sense.",
     "ok": "'Entrenched inertia' needs something to shift it: dislodge.", "bad": "Choosing a word because it sounds learned."},
]

METHODS = {
    "q-cv-fit": {"cue": "'Select the correct option to fill in the blank' with a single word to place, usually an advanced verb.",
                 "standard": "Read the sentence without the blank to see what job the word does; eliminate options of the wrong part of speech; pick the one whose meaning does that job.",
                 "fast": "Underline the clue word (entrenched, covert, dissent) and turn it into a simple phrase ('shift something stuck', 'put down opposition'), then match.",
                 "eliminate": "Remove the wrong part of speech first; then remove words whose meaning pulls the opposite way.",
                 "traps": ["One option is often a noun or adjective among verbs.", "A word that sounds close in sense (disillusion, discourage) but has a different meaning.", "A word that is the opposite of what is needed."],
                 "rules": ["cv-r1", "cv-r2"], "tech": ["read-whole"]},
}

REFS = []

WORDS = [
    word("dislodge", "dislodge", "word", "To force something out of the place where it is firmly fixed.", syn=["displace", "uproot", "shift"], ant=["fix", "embed", "anchor"],
         ex="A strong gust could dislodge the loose tiles from the roof.", pos="verb"),
    word("quell", "quell", "word", "To put an end to, especially by force; to suppress.", syn=["suppress", "crush", "subdue"], ant=["incite", "provoke", "inflame"],
         ex="Police moved in to quell the riot.", pos="verb"),
    word("curtail", "curtail", "word", "To cut short or reduce.", syn=["cut", "shorten", "reduce"], ant=["extend", "prolong", "lengthen"],
         ex="The heavy rain forced them to curtail the trip.", pos="verb"),
    word("mitigate", "mitigate", "word", "To make less severe or painful.", syn=["lessen", "ease", "soften"], ant=["worsen", "aggravate", "intensify"],
         ex="Tree planting can mitigate the heat of the city.", pos="verb"),
    word("substantiate", "substantiate", "word", "To support a claim with evidence.", syn=["prove", "verify", "back up"], ant=["disprove", "refute", "contradict"],
         ex="Can you substantiate your claim with records?", pos="verb"),
    word("ostracise", "ostracise", "word", "To exclude someone from a group by common consent.", syn=["exclude", "shun", "banish"], ant=["welcome", "include", "embrace"],
         ex="Villagers ostracised the family for breaking the custom.", pos="verb"),
    word("reiterate", "reiterate", "word", "To say again for emphasis.", syn=["repeat", "restate", "stress"], ant=["retract", "withdraw", "forget"],
         ex="Let me reiterate that the deadline will not move.", pos="verb"),
    word("cajole", "cajole", "word", "To persuade by flattery or gentle coaxing.", syn=["coax", "wheedle", "sweet-talk"], ant=["coerce", "bully", "force"],
         ex="She tried to cajole her father into lending the car.", pos="verb"),
    word("impugn", "impugn", "word", "To challenge or call into question a person's honesty or a statement.", syn=["challenge", "question", "attack"], ant=["defend", "uphold", "vindicate"],
         ex="The lawyer tried to impugn the witness's honesty.", pos="verb"),
    word("rebut", "rebut", "word", "To argue against a claim with evidence and show it is false.", syn=["refute", "counter", "disprove"], ant=["concede", "accept", "admit"],
         ex="The minister rose to rebut the charge.", pos="verb"),
]
S2, S3 = "2025-09-12-S2", "2025-09-12-S3"
_SEL = "Select the correct option to fill in the blank.\n"

PYQS = [
    q("q-cv-fit", "fill", _SEL + "Only a complete paradigm shift can ___ the deeply entrenched bureaucratic inertia.",
      ["discourage", "dislodge", "disillusion", "persuasion"], "b",
      "'Entrenched' inertia is firmly fixed in place, so it takes something that forces it out: to dislodge it. A verb is needed after 'can'.",
      {"a": mistake("To discourage is to take away someone's confidence; inertia is a state, not a person to be put off."),
       "c": mistake("To disillusion is to free someone from a false belief; it is about a person's beliefs, not a fixed habit."),
       "d": ruled_out("'Persuasion' is a noun; after 'can' the sentence needs a verb.")},
      rules=["cv-r1", "cv-r2"], lex=("fits", "dislodge"), paper=S2, qno=87, trick="Entrenched = stuck in place; the verb must move it."),
    q("q-cv-fit", "fill", _SEL + "The new rules, though seemingly driven by fiscal necessity, were actually a covert move to ___ dissent under \"austerity.\"",
      ["quell", "impugn", "swell", "rebut"], "a",
      "The rules are a hidden way to put down opposition, so the verb must mean to suppress: quell. 'Dissent' is the opposition being suppressed.",
      {"b": mistake("To impugn is to challenge someone's honesty; one does not impugn dissent itself, and it does not mean to suppress."),
       "c": mistake("To swell would make dissent grow, the opposite of what a covert move to silence it would do."),
       "d": mistake("To rebut is to answer an argument openly with evidence; a covert move is not a public reply.")},
      rules=["cv-r1", "cv-r2"], lex=("fits", "quell"), paper=S3, qno=89, rare=True, trick="Covert + dissent = hidden suppression."),
]


def _p(uid, text, opts, key, why, wrong, wid, rules=("cv-r1", "cv-r2"), rare=False):
    return q("q-cv-fit", "fill", _SEL + text, opts, key, why, wrong, rules=list(rules), lex=("fits", wid), uid=uid, rare=rare)


def practice_items():
    return [
        _p("cv-p01", "The council decided to ___ the festival to two days because of the budget.", ["extend", "curtail", "celebrate", "mitigate"], "b",
           "A budget problem makes the council shorten the festival: to curtail it.",
           {"a": mistake("To extend makes it longer, the opposite of what a shortage of money forces."), "c": ruled_out("Celebrate does not take 'to two days' as a limit."),
            "d": mistake("To mitigate is to make something harmful less severe; a festival is not a harm.")}, "curtail"),
        _p("cv-p02", "Planting trees along the road can ___ the noise from traffic.", ["mitigate", "reiterate", "ostracise", "cajole"], "a",
           "The trees make the noise less severe: they mitigate it.",
           {"b": ruled_out("To reiterate is to repeat; one cannot repeat noise with trees."), "c": ruled_out("To ostracise is to exclude a person from a group."),
            "d": ruled_out("To cajole is to persuade by coaxing a person.")}, "mitigate"),
        _p("cv-p03", "He could not ___ his claim that the bridge was unsafe, because he had no report.", ["quell", "substantiate", "ostracise", "dislodge"], "b",
           "A claim without a report cannot be supported: he cannot substantiate it.",
           {"a": ruled_out("To quell is to put down a disturbance, not support a claim."), "c": ruled_out("To ostracise is to exclude a person."),
            "d": ruled_out("To dislodge is to force something out of place.")}, "substantiate"),
        _p("cv-p04", "The villagers chose to ___ the family that had broken the custom, and nobody spoke to them.", ["welcome", "ostracise", "reiterate", "substantiate"], "b",
           "'Nobody spoke to them' shows the family was excluded: ostracised.",
           {"a": mistake("To welcome is the opposite of what 'nobody spoke to them' shows."), "c": ruled_out("To reiterate is to repeat something."),
            "d": ruled_out("To substantiate is to support a claim with evidence.")}, "ostracise"),
        _p("cv-p05", "The teacher had to ___ the rule again because half the class had not understood it.", ["reiterate", "curtail", "quell", "impugn"], "a",
           "She says the rule again for emphasis: she reiterates it.",
           {"b": ruled_out("To curtail is to cut short."), "c": ruled_out("To quell is to suppress a disturbance."),
            "d": mistake("To impugn is to challenge someone's honesty, which has nothing to do with a rule being repeated.")}, "reiterate"),
        _p("cv-p06", "She managed to ___ her reluctant brother into joining the trip with gentle flattery.", ["bully", "cajole", "dislodge", "rebut"], "b",
           "Gentle flattery is the method of the verb to cajole.",
           {"a": mistake("To bully is to force by threat, but the sentence says 'gentle flattery'."), "c": ruled_out("To dislodge is to force something from its place."),
            "d": ruled_out("To rebut is to answer an argument.")}, "cajole"),
        _p("cv-p07", "The opposition tried to ___ the minister's honesty by waving old letters in the House.", ["impugn", "quell", "mitigate", "curtail"], "a",
           "Waving old letters to damage his honesty is an attempt to impugn it.",
           {"b": ruled_out("To quell is to suppress a disturbance."), "c": ruled_out("To mitigate is to make something less severe."),
            "d": ruled_out("To curtail is to cut short.")}, "impugn", rare=True),
        _p("cv-p08", "The lawyer rose to ___ the charge with facts from the record.", ["rebut", "cajole", "ostracise", "reiterate"], "a",
           "To answer a charge with facts is to rebut it.",
           {"b": mistake("To cajole is to coax; facts from a record are not coaxing."), "c": ruled_out("To ostracise is to exclude a person."),
            "d": mistake("To reiterate only repeats; the lawyer needs to answer the charge.")}, "rebut"),
        _p("cv-p09", "A strong gust could ___ the loose tiles and send them down on the street.", ["dislodge", "substantiate", "reiterate", "cajole"], "a",
           "The gust forces the tiles out of their fixed place: it dislodges them.",
           {"b": ruled_out("To substantiate supports a claim with proof."), "c": ruled_out("To reiterate repeats something said."),
            "d": ruled_out("To cajole persuades a person by coaxing.")}, "dislodge"),
        _p("cv-p10", "Troops were sent in to ___ the riot before it spread to the next town.", ["quell", "cajole", "reiterate", "substantiate"], "a",
           "Troops sent to stop a riot are sent to quell it.",
           {"b": mistake("To cajole is to coax by flattery; troops do not coax a riot."), "c": ruled_out("To reiterate is to repeat."),
            "d": ruled_out("To substantiate is to support a claim with evidence.")}, "quell"),
    ]
