"""Homonyms: 3 past questions and 13 original practice items. In this question type the stem sentence fixes one sense of a word and the
answer is the one option where the same word carries a different sense. Not machine-checked: each answer rests on the cited rule."""
from bank import mistake, ruled_out, q

TOPIC = "homonyms"
TIER = "full"
PREFIX = "hm"

NODES = {
    "q-hm-sense": {"short": "Other sense", "label": "Sentence with a different sense of the word", "kind": "qtype", "parent": TOPIC, "order": 1,
                   "summary": "A sentence fixes one meaning of a word; choose the option where the word means something else.", "links": []},
}

RULES = [
    {"id": "hm-r1", "node": "q-hm-sense", "text": "A homonym is one spelling (or sound) with more than one meaning. Fix the sense used in the given sentence, then pick the one option where the same word has a different sense; the other three share the given sense.",
     "ok": "'bank' of a river vs 'bank' that keeps money: different senses.", "bad": "Choosing another sentence that also means the riverside."},
    {"id": "hm-r2", "node": "q-hm-sense", "text": "Same spelling can change the part of speech: left (direction) vs left (past of leave), rose (flower) vs rose (past of rise), ring (jewel) vs ring (to sound). A change of part of speech means a change of sense.",
     "ok": "'rose' the flower vs 'rose' the sun did.", "bad": "Treating 'rose' as the same word-sense in both."},
]

METHODS = {
    "q-hm-sense": {"cue": "'Select the sentence containing the homonym of the highlighted word', with a stem sentence and four options that all use the same word.",
                   "standard": "Say what the word means in the stem. Read each option and name the sense the word has there. Three options repeat the stem's sense; the odd one out is the answer.",
                   "fast": "Look for the option whose context (who, where, doing what) is unlike the other three.",
                   "eliminate": "Cross out every option whose meaning of the word is the same as in the stem. Do not stop at the first that 'feels' different.",
                   "traps": ["Rare words (gules, bailey, canon) make the senses hard to name, so the odd sentence is found by elimination.",
                             "A change of part of speech (noun to verb) is a change of sense.",
                             "The word may sit in a proper noun (Bailey) in the odd sentence."],
                   "rules": ["hm-r1", "hm-r2"], "tech": ["read-whole"]},
}

REFS = []
WORDS = []
S1, S2, S3 = "2025-09-12-S1", "2025-09-12-S2", "2025-09-12-S3"
_SEL = "Select the sentence containing the homonym of the highlighted word:\n"

PYQS = [
    q("q-hm-sense", "homonym", _SEL + "The choir began the [[canon]] at the conductor's signal.",
      ["The photographer adjusted the canon before taking the shot.", "The canon echoed beautifully through the hall.",
       "The singers practised the canon repeatedly before the performance.", "The composer introduced a complex canon in the final movement."], "a",
      "In the stem, 'canon' is a piece of music in which voices enter one after another. Options b, c and d all use that musical sense; only option a uses the word for something else.",
      {"b": ruled_out("'Canon' here is still the musical piece that echoed through the hall, the stem's sense."),
       "c": ruled_out("The singers practise a canon, the musical piece, the stem's sense."),
       "d": ruled_out("A composer introducing a canon is the musical sense again.")},
      rules=["hm-r1"], paper=S1, qno=100, rare=True,
      caution="This item is solved by elimination. Three sentences use 'canon' as a piece of music; the keyed sentence is the one that does not, and it is the only one that needs a different noun (the camera sense of Canon, or a cannon). The wording is loose, so do not spend time on the keyed sentence's own meaning."),
    q("q-hm-sense", "homonym", _SEL + "The prince's [[gules]] stood out clearly on the family coat of arms.",
      ["The shield displayed gules and argent in bold patterns.", "The cook served a dish with a sauce of rich gules and cumin.",
       "The gules trim on the banner represented a warrior tradition.", "The guide described the meaning of gules to the audience."], "b",
      "In the stem, 'gules' is the heraldic word for the colour red. Options a, c and d use the heraldic colour; option b puts it in a cooking sentence, where it does not carry the heraldic sense.",
      {"a": ruled_out("Gules and argent are the heraldic red and silver, the stem's sense."),
       "c": ruled_out("A gules trim on a banner is the heraldic red again."),
       "d": ruled_out("The guide explains the meaning of gules, the heraldic colour, the stem's sense.")},
      rules=["hm-r1"], paper=S2, qno=97, rare=True,
      caution="Weak item. 'Gules' has only the one heraldic sense, so the keyed sentence is an odd use, not a second meaning. The key is reached by elimination: the other three are all heraldic."),
    q("q-hm-sense", "homonym", _SEL + "The researcher cited a [[bailey]] in Norman defensive design.",
      ["Bailey presented the findings on Norman fortifications at the seminar.", "The outer bailey encircled the motte and was guarded by watchtowers.",
       "The soldiers retreated into the bailey when the main gate collapsed.", "A wooden palisade was raised around the bailey for extra protection."], "a",
      "In the stem, 'bailey' is the walled courtyard of a medieval castle. Options b, c and d use that sense; in option a, Bailey is a person's name.",
      {"b": ruled_out("The outer bailey around the motte is the castle courtyard, the stem's sense."),
       "c": ruled_out("Soldiers retreating into the bailey is the castle courtyard again."),
       "d": ruled_out("A palisade around the bailey is the castle courtyard again.")},
      rules=["hm-r1"], paper=S3, qno=81, rare=True,
      caution="The odd sentence is the one where the word is a capitalised surname, so the item tests proper noun against common noun more than two meanings of a word."),
]


def _p(uid, stem, opts, key, why, wrong, rules=("hm-r1",), rare=False):
    return q("q-hm-sense", "homonym", _SEL + stem, opts, key, why, wrong, rules=list(rules), uid=uid, rare=rare)


def practice_items():
    return [
        _p("hm-p01", "She sat on the [[bank]] of the river.",
           ["The bank of the pond was muddy.", "They walked along the grassy bank.", "He deposited his salary in the bank.", "Fish gathered near the bank of the stream."], "c",
           "In the stem, 'bank' is the sloping edge of a river. Only option c uses it for an institution that keeps money.",
           {"a": ruled_out("The edge of a pond is the stem's sense."), "b": ruled_out("A grassy bank beside the path is the stem's sense."),
            "d": ruled_out("The bank of a stream is the stem's sense.")}),
        _p("hm-p02", "The dog began to [[bark]] at the stranger.",
           ["The cat ran when the dog let out a loud bark.", "Neighbours complained about the constant bark.", "The bark of the old oak was rough.", "Its bark scared the thief."], "c",
           "In the stem, 'bark' is the sharp sound a dog makes. Only option c uses it for the outer covering of a tree.",
           {"a": ruled_out("The sound the dog makes is the stem's sense."), "b": ruled_out("A constant bark is a dog's noise, the stem's sense."),
            "d": ruled_out("The thief is scared by a sound, the stem's sense.")}),
        _p("hm-p03", "Flowers bloom in [[spring]].",
           ["The spring brought rain and new leaves.", "Birds return every spring.", "The mattress spring had broken.", "Spring is my favourite season."], "c",
           "In the stem, 'spring' is the season. Only option c uses it for a coiled piece of metal.",
           {"a": ruled_out("Spring that brings new leaves is the season."), "b": ruled_out("Birds returning every spring is the season."),
            "d": ruled_out("Spring as a favourite season is the stem's sense.")}),
        _p("hm-p04", "This bag is very [[light]].",
           ["A light jacket is enough for summer.", "He carried a light load.", "Switch on the light, please.", "The ship carried a light cargo."], "c",
           "In the stem, 'light' means of little weight. Only option c uses it for the brightness from a lamp.",
           {"a": mistake("A light jacket is a thin, not heavy jacket, so it shares the stem's 'not heavy' sense."), "b": ruled_out("A light load is of little weight, the stem's sense."),
            "d": ruled_out("A light cargo is of little weight, the stem's sense.")}),
        _p("hm-p05", "The batsman swung the [[bat]].",
           ["He bought a new cricket bat.", "The bat was too heavy for the child.", "A bat flew out of the cave at dusk.", "Please hand me the bat and ball."], "c",
           "In the stem, 'bat' is the wooden tool used to hit a ball. Only option c uses it for the flying mammal.",
           {"a": ruled_out("A cricket bat is the stem's sense."), "b": ruled_out("A bat that is too heavy for a child is the playing bat."),
            "d": ruled_out("A bat and ball are the playing equipment, the stem's sense.")}),
        _p("hm-p06", "She wore a gold [[ring]] on her finger.",
           ["He lost his wedding ring.", "A diamond ring sparkled in the box.", "The boxers stepped into the ring.", "The ring was too tight for her."], "c",
           "In the stem, 'ring' is a circle of metal worn on a finger. Only option c uses it for the square space where boxers fight.",
           {"a": ruled_out("A wedding ring is the stem's sense."), "b": ruled_out("A diamond ring is the stem's sense."),
            "d": ruled_out("A ring that is too tight for her is the finger ring, the stem's sense.")}),
        _p("hm-p07", "The archer fitted an arrow to the [[bow]].",
           ["An old bow hung on the wall of the hunter's hut.", "The bow snapped when he pulled the string.", "The girl wore a red bow in her hair.", "He bought a new bow and a quiver of arrows."], "c",
           "In the stem, 'bow' is the weapon that shoots arrows. Only option c uses it for a knot of ribbon.",
           {"a": ruled_out("A hunter's bow is the stem's weapon."), "b": ruled_out("A bow that snaps when the string is pulled is the stem's weapon."),
            "d": ruled_out("A bow bought with a quiver of arrows is the stem's weapon.")}),
        _p("hm-p08", "The villagers drew water from the [[well]].",
           ["A deep well stood in the courtyard.", "They dug a new well near the fields.", "She did well in the examination.", "The well had run dry in summer."], "c",
           "In the stem, 'well' is a hole dug for water. Only option c uses it as an adverb meaning 'in a good way'.",
           {"a": ruled_out("A deep well in the courtyard is the stem's sense."), "b": ruled_out("Digging a new well is the stem's sense."),
            "d": ruled_out("A well that runs dry is the stem's sense.")}),
        _p("hm-p09", "The workers went down into the coal [[mine]].",
           ["A gold mine was found in the hills.", "The mine collapsed after the blast.", "That book is mine.", "Miners worked deep inside the mine."], "c",
           "In the stem, 'mine' is an underground place where minerals are dug. Only option c uses it as a pronoun meaning 'belonging to me'.",
           {"a": ruled_out("A gold mine is the stem's sense."), "b": ruled_out("A mine that collapses is the stem's sense."),
            "d": ruled_out("Miners working inside the mine is the stem's sense.")}),
        _p("hm-p10", "The village [[fair]] was held in March.",
           ["We went to the fair to see the rides.", "A book fair opens next week.", "The umpire's decision was fair.", "The cattle fair attracted many traders."], "c",
           "In the stem, 'fair' is a gathering with stalls and entertainment. Only option c uses it as an adjective meaning 'just'.",
           {"a": ruled_out("A fair with rides is the stem's sense."), "b": ruled_out("A book fair is the stem's sense."),
            "d": ruled_out("A cattle fair is the stem's sense.")}),
        _p("hm-p11", "India won the [[match]] by ten runs.",
           ["The match began at noon.", "Rain delayed the football match.", "He struck a match to light the lamp.", "A thrilling match ended in a draw."], "c",
           "In the stem, 'match' is a game between two sides. Only option c uses it for a small stick that makes fire.",
           {"a": ruled_out("A match that begins at noon is a game, the stem's sense."), "b": ruled_out("A football match is a game, the stem's sense."),
            "d": ruled_out("A match that ends in a draw is a game, the stem's sense.")}),
        _p("hm-p12", "Turn [[left]] at the next signal.",
           ["Her left hand was injured.", "The shop is on the left.", "He left the house early.", "Keep to the left of the road."], "c",
           "In the stem, 'left' is the direction opposite to right. Only option c uses 'left' as the past tense of leave.",
           {"a": mistake("It is easy to read 'left hand' as the same word as the verb, but it is the direction, the stem's sense."),
            "b": ruled_out("'On the left' is the direction, the stem's sense."), "d": ruled_out("'To the left' is the direction, the stem's sense.")},
           rules=("hm-r1", "hm-r2")),
        _p("hm-p13", "A [[rose]] grew in the garden.",
           ["She plucked a red rose.", "The rose smelt sweet.", "The sun rose at six.", "He gave her a white rose."], "c",
           "In the stem, 'rose' is the flower. Only option c uses 'rose' as the past tense of rise.",
           {"a": ruled_out("A red rose is the flower, the stem's sense."),
            "b": mistake("A word that smells sweet can only be the flower, so it shares the stem's sense."),
            "d": ruled_out("A white rose given to her is the flower, the stem's sense.")},
           rules=("hm-r1", "hm-r2"), rare=True),
    ]
