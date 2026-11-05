"""Idioms & phrases. Seed tier. Each answer is checked against the idiom's meaning in WORDS."""
from bank import mistake, ruled_out, q, word

TOPIC = "idioms-phrases"
TIER = "seed"
PREFIX = "id"

NODES = {
    "q-idiom-meaning": {"short": "Meaning", "label": "Meaning of an idiom", "kind": "qtype", "parent": TOPIC, "order": 1,
                        "summary": "An idiom in inverted commas; pick the option that gives its meaning.", "links": []},
}

RULES = [
    {"id": "id-r1", "node": "q-idiom-meaning", "text": "An idiom means something different from its words put together. Never choose the option that restates the literal picture.",
     "ok": "Spill the beans = reveal a secret.", "bad": "Spill the beans = drop some beans."},
]

METHODS = {
    "q-idiom-meaning": {
        "cue": "'Select the most appropriate meaning of the idiom/phrase' with the idiom in inverted commas.",
        "standard": "Recall the meaning as a unit, then match it. If you do not know it, work out the feeling the idiom carries (good, bad, secret, effort) from the sentence it came from.",
        "fast": "Drop any option that is the literal reading, then match the remaining ones by feeling.",
        "eliminate": "Other idioms' meanings are usually the wrong options; if you recognise one of them as belonging to a different idiom, cross it out.",
        "traps": ["The literal meaning is nearly always listed as bait.", "The meaning of a similar-sounding idiom is the second common trap."],
        "rules": ["id-r1"], "tech": ["literal-trap"]},
}

REFS = []

WORDS = [
    word("blessing-in-disguise", "a blessing in disguise", "idiom", "A misfortune that turns out to be beneficial.", ex="Losing that job was a blessing in disguise, because it pushed her to start her own firm."),
    word("bite-the-bullet", "bite the bullet", "idiom", "To face a painful or difficult situation with courage.", ex="We will have to bite the bullet and cut the budget this year."),
    word("break-the-ice", "break the ice", "idiom", "To ease the awkwardness among people meeting for the first time.", ex="A quick joke helped him break the ice at the meeting."),
    word("once-in-a-blue-moon", "once in a blue moon", "idiom", "Very rarely.", ex="He visits his village once in a blue moon."),
    word("spill-the-beans", "spill the beans", "idiom", "To reveal a secret.", ex="Someone spilled the beans about the surprise party."),
    word("hit-the-nail-on-the-head", "hit the nail on the head", "idiom", "To state exactly what is true or right.", ex="You hit the nail on the head when you said the plan lacked money."),
    word("burn-the-midnight-oil", "burn the midnight oil", "idiom", "To work or study late into the night.", ex="She burnt the midnight oil before the exam."),
    word("cost-an-arm-and-a-leg", "cost an arm and a leg", "idiom", "To be extremely expensive.", ex="The repair cost an arm and a leg."),
]

_M = {w["id"]: w["meaning"].rstrip(".") for w in WORDS}


def _item(uid, wid, options, key, why, wrong, **kw):
    return q("q-idiom-meaning", "meaning", f"Select the most appropriate meaning of the given idiom.\n'{next(w for w in WORDS if w['id'] == wid)['w']}'",
             options, key, why, wrong, lex=("meaning", wid), uid=uid, rules=["id-r1"], tech=["literal-trap"], **kw)


def practice_items():
    return [
        _item("id-p01", "spill-the-beans", [_M["burn-the-midnight-oil"], _M["spill-the-beans"], "To drop food while cooking", _M["once-in-a-blue-moon"]], "b",
              "To spill the beans is to reveal a secret.",
              {"a": ruled_out("That is the meaning of 'burn the midnight oil', a different idiom."),
               "c": mistake("This is the literal reading of the words; an idiom never means its literal picture."),
               "d": ruled_out("That is the meaning of 'once in a blue moon'; it has nothing to do with secrets.")}),
        _item("id-p02", "blessing-in-disguise", [_M["cost-an-arm-and-a-leg"], _M["hit-the-nail-on-the-head"], _M["blessing-in-disguise"], "A prayer said quietly"], "c",
              "A blessing in disguise is a misfortune that turns out to be beneficial.",
              {"a": ruled_out("That is the meaning of 'cost an arm and a leg'."),
               "b": ruled_out("That is the meaning of 'hit the nail on the head'."),
               "d": mistake("This takes 'blessing' and 'disguise' literally; the idiom is about luck in the end.")}),
        _item("id-p03", "once-in-a-blue-moon", [_M["once-in-a-blue-moon"], "On the night of a full moon", _M["break-the-ice"], _M["bite-the-bullet"]], "a",
              "Once in a blue moon means very rarely.",
              {"b": mistake("This reads 'blue moon' as the moon itself; the idiom is about how seldom something happens."),
               "c": ruled_out("That is the meaning of 'break the ice'."),
               "d": ruled_out("That is the meaning of 'bite the bullet'.")}),
        _item("id-p04", "bite-the-bullet", [_M["spill-the-beans"], _M["bite-the-bullet"], "To chew something hard", _M["blessing-in-disguise"]], "b",
              "To bite the bullet is to face a painful situation with courage.",
              {"a": ruled_out("That is the meaning of 'spill the beans'."),
               "c": mistake("This is the literal picture of biting; the idiom means enduring something hard."),
               "d": ruled_out("That is the meaning of 'a blessing in disguise'.")}),
        _item("id-p05", "hit-the-nail-on-the-head", [_M["burn-the-midnight-oil"], _M["hit-the-nail-on-the-head"], "To strike a nail with a hammer", _M["cost-an-arm-and-a-leg"]], "b",
              "To hit the nail on the head is to state exactly what is true or right.",
              {"a": ruled_out("That is the meaning of 'burn the midnight oil'."),
               "c": mistake("This is the literal reading; the idiom is about being exactly right."),
               "d": ruled_out("That is the meaning of 'cost an arm and a leg'.")}),
        _item("id-p06", "cost-an-arm-and-a-leg", ["To be injured badly", _M["break-the-ice"], _M["blessing-in-disguise"], _M["cost-an-arm-and-a-leg"]], "d",
              "To cost an arm and a leg is to be extremely expensive.",
              {"a": mistake("This reads the body parts literally; the idiom is about price."),
               "b": ruled_out("That is the meaning of 'break the ice'."),
               "c": ruled_out("That is the meaning of 'a blessing in disguise'.")}),
    ]


PYQS = []
