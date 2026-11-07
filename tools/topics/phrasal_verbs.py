"""Phrasal verbs: a verb plus a particle whose meaning is not the sum of its parts. Seed tier: no phrasal-verb question appeared in the
three papers analysed so far, so this topic is drilled from the list. Every answer is checked against the meaning stored in WORDS,
and the wrong options are the meanings of phrasal verbs from other groups, so no wrong option can also be right."""
import re

from bank import mistake, ruled_out, q, word

TOPIC = "phrasal-verbs"
TIER = "seed"
PREFIX = "ph"

NODES = {
    "q-ph-meaning": {"short": "Meaning", "label": "Meaning of a phrasal verb", "kind": "qtype", "parent": TOPIC, "order": 1,
                     "summary": "A phrasal verb in a sentence; pick what it means there.", "links": ["idioms-phrases"]},
    "q-ph-fit": {"short": "Fill the blank", "label": "The phrasal verb that fits", "kind": "qtype", "parent": TOPIC, "order": 2,
                 "summary": "A sentence with a blank; pick the phrasal verb whose meaning the sentence needs.", "links": []},
}

RULES = [
    {"id": "ph-r1", "node": "q-ph-meaning", "text": "The particle carries the meaning, so one verb makes many different phrasal verbs: put off (postpone), put up with (tolerate), put down (write, or humiliate), put out (extinguish). Read the particle, not just the verb.",
     "ok": "The match was put off because of rain (postponed).", "bad": "The match was put off because of rain (extinguished)."},
    {"id": "ph-r2", "node": "q-ph-meaning", "text": "A phrasal verb almost never means its literal picture. If one option simply describes the physical action of the verb and the particle, it is the bait.",
     "ok": "He turned down the offer (refused it).", "bad": "He turned down the offer (rotated it downwards)."},
    {"id": "ph-r3", "node": "q-ph-fit", "text": "For a blank, work out what the sentence needs in plain words first (stop, tolerate, discover, postpone), and only then look for the phrasal verb that says it. Check that the particle and the object fit: you put up WITH a person, you look INTO a matter.",
     "ok": "The police will look into the complaint (investigate it).", "bad": "The police will look after the complaint (take care of it)."},
]

METHODS = {
    "q-ph-meaning": {"cue": "A sentence with a phrasal verb in inverted commas or highlighted, and four meanings as options.",
                     "standard": "Read the whole sentence, decide from the situation what the speaker must mean, then match the option.",
                     "fast": "Translate the phrasal verb into one plain word in your head, then look for that word among the options.",
                     "eliminate": "Drop the literal reading at once, then drop meanings that belong to the same verb with a different particle.",
                     "traps": ["The literal picture of the words.", "The meaning of the same verb with another particle (put off / put up with).",
                               "Two options that are close in sense: the sentence decides which."],
                     "rules": ["ph-r1", "ph-r2"], "tech": ["literal-trap", "context-clue"]},
    "q-ph-fit": {"cue": "A sentence with a blank and four phrasal verbs as options.",
                 "standard": "Say what the sentence needs in one plain word, then test each option in the blank.",
                 "fast": "Check the particle against the object: 'into' a matter, 'with' a person, 'for' a thing you want.",
                 "eliminate": "Remove options whose particle cannot take that object at all.",
                 "traps": ["Two options from the same verb (look into, look after, look for).", "A phrasal verb that fits the grammar but not the situation."],
                 "rules": ["ph-r3", "ph-r1"], "tech": ["back-substitute", "context-clue"]},
}

REFS = []

# (id, phrasal verb, meaning, own example sentence, group)
_V = [
    ("put-off", "put off", "To postpone something to a later time.", "The hearing was put off to the following month.", "delay"),
    ("put-up-with", "put up with", "To tolerate something unpleasant without complaining.", "She had to put up with the noise from the road.", "tolerate"),
    ("put-out", "put out", "To extinguish a fire or a light.", "It took an hour to put out the fire.", "stop"),
    ("put-down", "put down", "To write something on paper.", "Put down your name and number at the top.", "record"),
    ("call-off", "call off", "To cancel something that was planned.", "The strike was called off at midnight.", "cancel"),
    ("call-on", "call on", "To visit someone briefly.", "I shall call on my aunt this evening.", "visit"),
    ("carry-out", "carry out", "To perform or complete a task or an order.", "The engineers carried out the repairs overnight.", "perform"),
    ("carry-on", "carry on", "To continue doing something.", "Carry on reading while I answer the door.", "continue"),
    ("break-down", "break down", "To stop working, said of a machine or a vehicle.", "The bus broke down near the bridge.", "fail"),
    ("break-out", "break out", "To begin suddenly, said of something unwelcome such as a war or a disease.", "Cholera broke out after the floods.", "begin"),
    ("break-into", "break into", "To enter a building by force in order to steal.", "Thieves broke into the shop at night.", "enter"),
    ("bring-up", "bring up", "To raise a child.", "Her grandmother brought up all five children.", "raise"),
    ("bring-about", "bring about", "To cause something to happen.", "The new rule brought about a sharp fall in accidents.", "cause"),
    ("come-across", "come across", "To meet or find something by chance.", "I came across an old photograph in the drawer.", "find"),
    ("come-up-with", "come up with", "To think of an idea or a plan.", "She came up with a cheaper design.", "invent"),
    ("come-round", "come round", "To regain consciousness.", "He came round a few minutes after the fall.", "recover"),
    ("get-along", "get along", "To have a friendly relationship with someone.", "The two brothers get along well.", "relate"),
    ("get-over", "get over", "To recover from an illness or an unhappy event.", "It took him a year to get over the loss.", "recover2"),
    ("get-rid-of", "get rid of", "To remove or throw away something unwanted.", "We must get rid of these old files.", "remove"),
    ("give-in", "give in", "To stop resisting and accept defeat.", "After an hour of argument he gave in.", "yield"),
    ("give-up", "give up", "To stop doing something one has been doing regularly.", "He gave up smoking last year.", "quit"),
    ("give-away", "give away", "To reveal a secret, usually by accident.", "His face gave away the surprise.", "reveal"),
    ("go-through", "go through", "To examine something carefully from beginning to end.", "Go through the draft once before you sign it.", "examine"),
    ("go-on", "go on", "To happen.", "Nobody could tell us what was going on inside.", "happen"),
    ("look-into", "look into", "To investigate a matter.", "The department will look into the complaint.", "investigate"),
    ("look-after", "look after", "To take care of a person or a thing.", "She looks after her father's shop.", "care"),
    ("look-for", "look for", "To search for something.", "I am looking for my spectacles.", "search"),
    ("look-up-to", "look up to", "To respect and admire someone.", "Young officers look up to her.", "respect"),
    ("look-down-on", "look down on", "To regard someone as inferior.", "He looks down on anyone without a degree.", "despise"),
    ("make-out", "make out", "To manage to see, hear or understand something with difficulty.", "I could just make out a figure in the fog.", "discern"),
    ("make-up", "make up", "To invent a story or an excuse.", "He made up an excuse about a puncture.", "fabricate"),
    ("make-up-for", "make up for", "To compensate for something lost or missed.", "Extra classes will make up for the holidays.", "compensate"),
    ("pull-off", "pull off", "To succeed in something difficult.", "The team pulled off a win in the last over.", "succeed"),
    ("pull-through", "pull through", "To recover from a serious illness.", "The doctors think she will pull through.", "recover3"),
    ("run-out-of", "run out of", "To use up the whole supply of something.", "We have run out of printer paper.", "exhaust"),
    ("run-into", "run into", "To meet someone unexpectedly.", "I ran into an old classmate at the station.", "meet"),
    ("set-up", "set up", "To establish an organisation or a system.", "They set up a small press in the town.", "establish"),
    ("set-off", "set off", "To begin a journey.", "We set off before sunrise.", "depart"),
    ("take-after", "take after", "To resemble an older relative.", "She takes after her mother in looks.", "resemble"),
    ("take-over", "take over", "To assume control of something.", "A new manager took over the branch.", "control"),
    ("take-up", "take up", "To begin a hobby, a subject or an activity.", "He has taken up gardening since retiring.", "start"),
    ("turn-down", "turn down", "To refuse an offer or a request.", "She turned down the transfer.", "refuse"),
    ("turn-up", "turn up", "To arrive or appear, often unexpectedly.", "He turned up an hour late.", "arrive"),
    ("turn-out", "turn out", "To prove to be the case in the end.", "The rumour turned out to be false.", "prove"),
    ("do-away-with", "do away with", "To abolish something.", "The state did away with the old levy.", "abolish"),
    ("stand-by", "stand by", "To support someone in a difficulty.", "His colleagues stood by him through the inquiry.", "support"),
    ("bear-out", "bear out", "To confirm that something is true.", "The records bear out his account.", "confirm"),
    ("let-down", "let down", "To disappoint someone by failing them.", "He promised to come and then let us down.", "disappoint"),
    ("hold-up", "hold up", "To delay something or someone.", "An accident held up the traffic for an hour.", "delay2"),
    ("fall-back-on", "fall back on", "To use something as a last resort when other plans fail.", "If the loan is refused we can fall back on our savings.", "resort"),
    ("lay-out", "lay out", "To arrange or spread something out neatly and attractively.", "The staff lay out fresh linen on every bed each morning.", "arrange"),
]

WORDS = [word(i, v, "phrasal", m, ex=e) for i, v, m, e, g in _V]
_M = {i: m.rstrip(".") for i, v, m, e, g in _V}
_V2 = {i: v for i, v, m, e, g in _V}
_G = {i: g for i, v, m, e, g in _V}
_EX = {i: e for i, v, m, e, g in _V}
_RARE = {"bear-out", "fall-back-on", "do-away-with", "pull-through", "make-up-for", "look-down-on", "come-round", "make-out"}
_VERB = {i: v.split(" ")[0] for i, v, m, e, g in _V}
_ids = [i for i, *_ in _V]


def _pick(n, wid):
    """Three meanings from phrasal verbs of other groups, preferring one that shares this verb (put off / put out)."""
    same = [x for x in _ids if _VERB[x] == _VERB[wid] and _G[x] != _G[wid]]
    out = same[n % len(same):n % len(same) + 1] if same else []
    pool = [x for x in _ids if _G[x] != _G[wid] and x not in out and _VERB[x] != _VERB[wid]]
    j, seen = (n * 11) % len(pool), {_G[wid]} | {_G[x] for x in out}
    while len(out) < 3:
        c = pool[j % len(pool)]
        if _G[c] not in seen: out.append(c); seen.add(_G[c])
        j += 7
    return out


def _hl(sent, pv):
    """Mark the phrasal verb in the example sentence, allowing for an inflected first word (called off, gives away)."""
    parts = pv.split(" ")
    pat = (r"\b\w+\s+" + r"\s+".join(re.escape(x) for x in parts[1:])) if len(parts) > 1 else r"\b" + re.escape(parts[0]) + r"(?:s|es|ed|ing)?\b"
    return re.sub(pat, lambda m: "[[" + m.group(0) + "]]", sent, count=1, flags=re.I)


def practice_items():
    items = []
    for n, wid in enumerate(_ids, 1):
        d = _pick(n, wid)
        key = _M[wid]
        kpos = n % 4
        rest = [_M[x] for x in d]; rest.insert(kpos, key)
        wrong = {}
        for ltr, o in zip("abcd", rest):
            if o == key: continue
            other = next(x for x in d if _M[x] == o)
            note = f"That is what '{_V2[other]}' means, not '{_V2[wid]}'."
            wrong[ltr] = mistake(note + f" The verb is the same, so only the particle tells them apart.") if _VERB[other] == _VERB[wid] else ruled_out(note)
        items.append(q("q-ph-meaning", "meaning", "Select the most appropriate meaning of the phrasal verb in the sentence.\n"
                       + _hl(_EX[wid], _V2[wid]) + f"\n'{_V2[wid]}'",
                       rest, "abcd"[kpos], f"'{_V2[wid]}' means: {key[0].lower() + key[1:]}.", wrong,
                       lex=("meaning", wid), uid=f"ph-g{n:03d}", rules=["ph-r1", "ph-r2"], tech=["literal-trap"], rare=wid in _RARE))
    items += [
        q("q-ph-fit", "fill", "Select the most appropriate option to fill in the blank.\nThe department has promised to ___ the complaint within a month.",
          ["look after", "look into", "look for", "look up to"], "b",
          "The sentence needs 'investigate', which is what 'look into' means.",
          {"a": mistake("'Look after' means to take care of something, and a complaint is not cared for but examined."),
           "c": mistake("'Look for' means to search for a thing that is missing; the complaint is already in hand."),
           "d": ruled_out("'Look up to' means to respect a person and cannot take a complaint as its object.")},
          lex=("fits", "look-into"), uid="ph-p01", rules=["ph-r3"], tech=["back-substitute"]),
        q("q-ph-fit", "fill", "Select the most appropriate option to fill in the blank.\nShe had to ___ a great deal of rudeness from the callers.",
          ["put up with", "put off", "put out", "put down"], "a",
          "The sentence needs 'tolerate', which is what 'put up with' means.",
          {"b": mistake("'Put off' means to postpone, and rudeness is not postponed."),
           "c": mistake("'Put out' means to extinguish a fire or a light."),
           "d": mistake("'Put down' means to write something on paper.")},
          lex=("fits", "put-up-with"), uid="ph-p02", rules=["ph-r3", "ph-r1"], tech=["back-substitute"]),
        q("q-ph-fit", "fill", "Select the most appropriate option to fill in the blank.\nThe records ___ his account of the meeting.",
          ["bear out", "break out", "turn out", "make out"], "a",
          "The sentence needs 'confirm', which is what 'bear out' means.",
          {"b": ruled_out("'Break out' means to begin suddenly, said of a war or a disease."),
           "c": mistake("'Turn out' means to prove to be the case, but it does not take an object in this way: an account turns out to be true, it is not turned out by records."),
           "d": mistake("'Make out' means to manage to see or understand something with difficulty.")},
          lex=("fits", "bear-out"), uid="ph-p03", rules=["ph-r3"], tech=["back-substitute"], rare=True),
        q("q-ph-fit", "fill", "Select the most appropriate option to fill in the blank.\nIf the bank refuses the loan, we can ___ our savings.",
          ["fall back on", "give in to", "do away with", "run out of"], "a",
          "The sentence needs 'use as a last resort', which is what 'fall back on' means.",
          {"b": ruled_out("'Give in to' means to stop resisting something, which savings are not."),
           "c": mistake("'Do away with' means to abolish, which would mean getting rid of the savings rather than using them."),
           "d": mistake("'Run out of' means to exhaust a supply, which is the opposite of having savings to rely on.")},
          lex=("fits", "fall-back-on"), uid="ph-p04", rules=["ph-r3"], tech=["back-substitute"], rare=True),
    ]
    return items


PYQS = [
    q("q-ph-fit", "fill", "Select the most appropriate option to fill in the blank.\nThey ______ the table beautifully for their guests.",
      ["laid in", "laid out", "laid by", "laid on"], "b",
      "The sentence needs 'arranged attractively', which is what 'lay out' means: they laid out the table.",
      {"a": mistake("'Laid in' means to store up a supply of something, not to arrange a table."),
       "c": mistake("'Laid by' means to set something aside for later use, not to arrange a table."),
       "d": mistake("'Laid on' means to arrange or provide a service or event, which is close but is not the phrase used for arranging a table setting itself.")},
      rules=["ph-r3"], paper="2026-10-09", qno=79),
]
