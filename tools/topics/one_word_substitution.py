"""One-word substitution: 3 past questions and a generated question for every word stored. Each answer is checked against the phrase stored in WORDS."""
from bank import mistake, ruled_out, q, word

TOPIC = "one-word-substitution"
TIER = "full"
PREFIX = "ow"

NODES = {
    "q-ows": {"short": "One word", "label": "One word for a phrase", "kind": "qtype", "parent": TOPIC, "order": 1,
              "summary": "A phrase is given; pick the single word that means the same.", "links": []},
}

RULES = [
    {"id": "ow-r1", "node": "q-ows", "text": "Many one-word substitutions are built from a Greek or Latin root: phobia (fear), phile (lover), mis(o) (hate), anthropo (mankind). Match the root to the phrase.",
     "ok": "Bibliophile: biblio (book) + phile (lover) = lover of books.", "bad": "Bibliophobe is not the word for a lover of books; phobe means one who fears."},
    {"id": "ow-r2", "node": "q-ows", "text": "Look-alike words come in sets that differ by one root: -cide (killing), -phobia (fear), omni- (all), -gamy (marriage), -cracy (rule). Fix the root first, then the prefix.",
     "ok": "Patricide (father) and matricide (mother) differ only in the prefix.", "bad": "Choosing matricide for the killing of one's father."},
]

METHODS = {
    "q-ows": {"cue": "'Select the word that can be used as a substitute for the given group of words.'",
              "standard": "Know the word, or break it into root parts and match them to the phrase.",
              "fast": "Split each option into its root, discard the roots that do not match the phrase.",
              "eliminate": "The wrong options are usually real words with a neighbouring meaning (hater instead of lover), so match both halves of the root.",
              "traps": ["A word with the right root but the opposite sense (phile vs phobe).", "A word that sounds similar but belongs to another phrase."],
              "rules": ["ow-r1", "ow-r2"], "tech": ["root-prefix"]},
}

REFS = []


# (id, word, phrase it replaces, own example sentence, group)
_O = [
    ("omniscient", "omniscient", "One who knows everything", "Nobody is omniscient, so even experts should ask questions.", "know"),
    ("omnipotent", "omnipotent", "Having unlimited power", "No ruler is omnipotent; every one answers to someone.", "power"),
    ("omnipresent", "omnipresent", "Present everywhere at the same time", "Advertising feels omnipresent in a big city.", "place"),
    ("omnivorous", "omnivorous", "Eating both plants and animals", "Bears are omnivorous, eating berries as well as fish.", "diet"),
    ("herbivorous", "herbivorous", "Feeding only on plants", "Cows are herbivorous animals.", "diet"),
    ("carnivorous", "carnivorous", "Feeding on flesh", "The lion is a carnivorous animal.", "diet"),
    ("philanthropist", "philanthropist", "One who loves mankind and helps others", "The philanthropist funded three new libraries.", "love"),
    ("misanthrope", "misanthrope", "One who hates mankind", "After the betrayal he became a misanthrope and avoided everyone.", "hate"),
    ("misogynist", "misogynist", "One who hates women", "The misogynist refused to work under a woman manager.", "hate"),
    ("bibliophile", "bibliophile", "A lover of books", "Every wall of the bibliophile's house is lined with shelves.", "hobby"),
    ("polyglot", "polyglot", "A person who knows many languages", "The polyglot translated for guests from five countries.", "language"),
    ("somnambulist", "somnambulist", "One who walks in sleep", "The somnambulist woke up in the garden at dawn.", "sleep"),
    ("insomniac", "insomniac", "A person who cannot sleep", "An insomniac often reads till the early hours.", "sleep"),
    ("egoist", "egoist", "One who thinks only of himself", "The egoist never thanked the people who helped him.", "self"),
    ("altruist", "altruist", "One who puts the welfare of others before his own", "The altruist gave away most of her salary.", "love"),
    ("atheist", "atheist", "One who does not believe in God", "The atheist politely declined to join the prayer.", "belief"),
    ("agnostic", "agnostic", "One who holds that the existence of God cannot be known", "The agnostic said the question could never be settled.", "belief"),
    ("sceptic", "sceptic", "One who doubts accepted beliefs", "The sceptic asked for proof before accepting the claim.", "belief"),
    ("cynic", "cynic", "One who believes that people act only out of selfish motives", "The cynic said every act of kindness had a hidden price.", "belief"),
    ("optimist", "optimist", "One who expects the best to happen", "An optimist sees the half-filled glass as half full.", "attitude"),
    ("pessimist", "pessimist", "One who expects the worst to happen", "A pessimist carries an umbrella even in the dry season.", "attitude"),
    ("pedant", "pedant", "One who makes a show of minute learning or rules", "The pedant corrected every comma in the notice.", "show"),
    ("philistine", "philistine", "A person who has no taste for art and culture", "The philistine yawned through the whole exhibition.", "taste"),
    ("connoisseur", "connoisseur", "An expert judge of art or taste", "As a connoisseur of tea, she could name the estate from one sip.", "taste"),
    ("amateur", "amateur", "One who does something for pleasure and not for pay", "The amateur painter sold her first canvas last week.", "skill"),
    ("novice", "novice", "A beginner", "Every novice makes mistakes in the first week.", "skill"),
    ("veteran", "veteran", "A person with long experience in a field", "The veteran driver knew every turn of the pass.", "skill"),
    ("pacifist", "pacifist", "One who opposes war and violence", "The pacifist marched against the arms deal.", "peace"),
    ("fanatic", "fanatic", "One who is extremely and blindly enthusiastic about a cause", "The fanatic refused to listen to any other view.", "zeal"),
    ("hypocrite", "hypocrite", "One who pretends to be better than he really is", "Preaching thrift while spending freely makes him a hypocrite.", "show"),
    ("miser", "miser", "One who hoards wealth and spends as little as possible", "The miser kept his old coat for thirty years.", "money"),
    ("spendthrift", "spendthrift", "One who spends money wastefully", "The spendthrift had nothing left by the middle of the month.", "money"),
    ("philatelist", "philatelist", "A collector of postage stamps", "The philatelist paid a fortune for the rare stamp.", "hobby2"),
    ("numismatist", "numismatist", "A collector of coins", "The numismatist displayed coins from the Gupta period.", "hobby2"),
    ("epicure", "epicure", "One who enjoys fine food and drink", "The epicure travelled far just to taste a local dish.", "food"),
    ("glutton", "glutton", "One who eats too much", "The glutton emptied three plates before anyone else started.", "food"),
    ("sycophant", "sycophant", "One who flatters powerful people to gain favour", "The sycophant laughed at every joke the boss made.", "show"),
    ("nomad", "nomad", "A person who wanders from place to place with no fixed home", "The nomad moved his tent with the seasons.", "wander"),
    ("plagiarist", "plagiarist", "One who passes off another's writing as his own", "The plagiarist was caught when the editor found the original article.", "writing"),
    ("mercenary", "mercenary", "A soldier who fights for a foreign army for money", "The mercenary changed sides when the pay was doubled.", "war"),
    ("polymath", "polymath", "A person of great learning in many fields", "Leonardo is remembered as a polymath who excelled in art and science.", "know"),
    ("anonymous", "anonymous", "Of unknown name", "The donor chose to remain anonymous.", "name"),
    ("unanimous", "unanimous", "By the agreement of all", "The committee's decision was unanimous.", "agree"),
    ("posthumous", "posthumous", "Happening or published after a person's death", "The poet won a posthumous award.", "death"),
    ("infallible", "infallible", "Incapable of making mistakes", "No umpire is infallible.", "cannot"),
    ("invincible", "invincible", "Impossible to defeat", "The team seemed invincible after ten wins.", "cannot"),
    ("inevitable", "inevitable", "Impossible to avoid", "Delay was inevitable after the heavy snow.", "cannot"),
    ("illegible", "illegible", "That which cannot be read", "His handwriting was so illegible that nobody could read the note.", "cannot"),
    ("legible", "legible", "Clear enough to be read", "Write in a legible hand so the examiner can read it.", "cannot2"),
    ("inaudible", "inaudible", "That which cannot be heard", "The speaker was almost inaudible at the back of the hall.", "cannot"),
    ("incorrigible", "incorrigible", "Too bad to be reformed", "The incorrigible rascal was late again.", "cannot"),
    ("indelible", "indelible", "That which cannot be erased", "The visit left an indelible memory.", "cannot"),
    ("irreparable", "irreparable", "That which cannot be put right or repaired", "The flood caused irreparable damage to the old bridge.", "cannot"),
    ("impregnable", "impregnable", "Impossible to capture by force", "The hill fort was considered impregnable.", "cannot"),
    ("insatiable", "insatiable", "Impossible to satisfy", "She has an insatiable appetite for stories.", "cannot"),
    ("insolvent", "insolvent", "Unable to pay one's debts", "The firm was declared insolvent last spring.", "money"),
    ("unprecedented", "unprecedented", "Never done or known before", "The floods reached an unprecedented height.", "new"),
    ("credulous", "credulous", "Ready to believe too easily", "The credulous buyer believed every promise the salesman made.", "belief"),
    ("versatile", "versatile", "Able to do many different things well", "She is a versatile actor who plays comedy and tragedy.", "skill"),
    ("anarchy", "anarchy", "A state of disorder due to the absence of government", "Anarchy followed the fall of the regime.", "rule"),
    ("autocracy", "autocracy", "Rule by one person with unlimited power", "Under autocracy no one can challenge the ruler.", "rule"),
    ("plutocracy", "plutocracy", "Rule by the wealthy", "Critics call it a plutocracy because money decides policy.", "rule"),
    ("theocracy", "theocracy", "Rule by religious leaders", "In a theocracy the clergy make the law.", "rule"),
    ("aviary", "aviary", "A place where birds are kept", "We watched parrots in the aviary.", "placeof"),
    ("apiary", "apiary", "A place where bees are kept", "The apiary hummed with thousands of bees.", "placeof"),
    ("aquarium", "aquarium", "A tank or building where fish and water animals are kept", "The aquarium has a tunnel through a shark tank.", "placeof"),
    ("arsenal", "arsenal", "A place where weapons are made or stored", "The arsenal was guarded day and night.", "placeof"),
    ("mortuary", "mortuary", "A place where dead bodies are kept before burial", "The police took the body to the mortuary.", "placeof"),
    ("sanatorium", "sanatorium", "A place for the treatment and recovery of long-term illness", "He spent a year in a hill sanatorium.", "placeof"),
    ("granary", "granary", "A building where grain is stored", "The village granary was full after the harvest.", "placeof"),
    ("genocide", "genocide", "The killing of a whole race or people", "The world condemned the genocide.", "killing"),
    ("patricide", "patricide", "The killing of one's father", "The play deals with patricide and its guilt.", "killing"),
    ("matricide", "matricide", "The killing of one's mother", "Matricide is the subject of the old tragedy.", "killing"),
    ("fratricide", "fratricide", "The killing of one's brother", "The epic's war is a story of fratricide.", "killing"),
    ("regicide", "regicide", "The killing of a king", "The regicide shocked the whole kingdom.", "killing"),
    ("claustrophobia", "claustrophobia", "Fear of closed or confined spaces", "Her claustrophobia made lifts impossible.", "fear"),
    ("agoraphobia", "agoraphobia", "Fear of open or crowded places", "His agoraphobia keeps him from busy markets.", "fear"),
    ("acrophobia", "acrophobia", "Fear of heights", "Acrophobia stopped him from crossing the bridge.", "fear"),
    ("xenophobia", "xenophobia", "Fear or hatred of foreigners", "Xenophobia grew as the town changed.", "fear"),
    ("monogamy", "monogamy", "Having only one spouse at a time", "Monogamy is the rule in most countries.", "marriage"),
    ("bigamy", "bigamy", "Marriage to a second spouse while the first is living", "Bigamy is a crime under the law.", "marriage"),
    ("polygamy", "polygamy", "Having more than one spouse at a time", "Polygamy is banned in many countries.", "marriage"),
    ("obituary", "obituary", "A notice in the newspaper announcing a person's death", "The obituary praised her years of service.", "writing"),
    ("epitaph", "epitaph", "An inscription on a tomb", "The epitaph on the stone was only one line long.", "writing"),
    ("autobiography", "autobiography", "The story of a person's life written by himself", "His autobiography became a bestseller.", "writing"),
    ("amnesty", "amnesty", "A general pardon for offences", "The government announced an amnesty for minor offenders.", "law"),
    ("panacea", "panacea", "A remedy for all diseases or troubles", "No single policy is a panacea for unemployment.", "remedy"),
    ("utopia", "utopia", "An imaginary place of perfect happiness", "The poet imagined a utopia free of hunger.", "place2"),
    ("nostalgia", "nostalgia", "A sentimental longing for the past", "Old songs filled him with nostalgia.", "feeling"),
    ("ambidextrous", "ambidextrous", "Able to use both hands equally well", "An ambidextrous bowler can deliver with either hand.", "skill"),
    ("nocturnal", "nocturnal", "Active during the night", "Owls are nocturnal birds.", "time2"),
    ("amphibian", "amphibian", "An animal that lives both on land and in water", "A frog is an amphibian.", "animal"),
    ("celibate", "celibate", "One who remains unmarried, especially by vow", "The monk took a vow to remain celibate.", "marriage2"),
    ("orphan", "orphan", "A child whose parents are dead", "The orphan was raised by his grandmother.", "family"),
    ("novelty", "novelty", "The quality of being new and unusual", "The novelty of the gadget wore off in a week.", "new"),
    ("bilingual", "bilingual", "A person who speaks two languages fluently", "A bilingual guide helped both groups.", "language"),
    ("ascetic", "ascetic", "A person who avoids pleasures and lives with strict self-discipline", "The ascetic lived on one meal a day.", "belief2"),
    ("desuetude", "desuetude", "A condition of disuse or inactivity", "The old custom fell into desuetude.", "state"),
    ("interregnum", "interregnum", "A period between two reigns or governments", "An interregnum followed the king's death.", "time3"),
    ("lethargy", "lethargy", "A state of drowsy lack of energy", "Heat brought on a lethargy in the afternoon.", "state2"),
    ("destitute", "destitute", "Without money, food and the basic things of life", "The flood left many families destitute.", "money2"),
    ("mystic", "mystic", "One who seeks union with God through deep meditation", "The mystic spent years in silent meditation.", "belief2"),
]
_CONF = {
    "omniscient": ["omnipotent", "omnipresent"], "omnipotent": ["omniscient", "omnipresent"], "omnipresent": ["omnipotent", "omniscient"],
    "omnivorous": ["herbivorous", "carnivorous"], "herbivorous": ["carnivorous", "omnivorous"], "carnivorous": ["herbivorous", "omnivorous"],
    "philanthropist": ["misanthrope", "misogynist"], "misanthrope": ["philanthropist", "misogynist"], "misogynist": ["misanthrope", "philanthropist"],
    "patricide": ["matricide", "fratricide"], "matricide": ["patricide", "fratricide"], "fratricide": ["patricide", "regicide"], "regicide": ["patricide", "genocide"],
    "genocide": ["regicide", "fratricide"], "monogamy": ["bigamy", "polygamy"], "bigamy": ["monogamy", "polygamy"], "polygamy": ["bigamy", "monogamy"],
    "claustrophobia": ["agoraphobia", "acrophobia"], "agoraphobia": ["claustrophobia", "xenophobia"], "acrophobia": ["claustrophobia", "agoraphobia"],
    "xenophobia": ["agoraphobia", "acrophobia"], "atheist": ["agnostic", "sceptic"], "agnostic": ["atheist", "sceptic"], "sceptic": ["agnostic", "cynic"],
    "cynic": ["sceptic", "pessimist"], "illegible": ["legible", "inaudible"], "legible": ["illegible"], "unanimous": ["anonymous"], "anonymous": ["unanimous"],
    "miser": ["spendthrift"], "spendthrift": ["miser"], "numismatist": ["philatelist"], "philatelist": ["numismatist"], "aviary": ["apiary", "aquarium"],
    "apiary": ["aviary", "aquarium"], "aquarium": ["aviary", "apiary"], "optimist": ["pessimist"], "pessimist": ["optimist", "cynic"],
    "epicure": ["glutton"], "glutton": ["epicure"], "amateur": ["novice", "connoisseur"], "novice": ["amateur", "veteran"], "veteran": ["novice"],
    "autocracy": ["plutocracy", "theocracy"], "plutocracy": ["autocracy", "theocracy"], "theocracy": ["autocracy", "plutocracy"],
    "infallible": ["invincible"], "invincible": ["infallible", "impregnable"], "impregnable": ["invincible"], "indelible": ["incorrigible", "irreparable"],
    "incorrigible": ["indelible"], "irreparable": ["indelible"], "ascetic": ["mystic", "sceptic"], "mystic": ["ascetic", "agnostic"],
    "bibliophile": ["philatelist"], "altruist": ["egoist"], "egoist": ["altruist"], "autobiography": ["obituary"], "obituary": ["epitaph"], "epitaph": ["obituary"],
    "desuetude": ["lethargy", "interregnum"], "lethargy": ["desuetude"], "interregnum": ["desuetude"], "destitute": ["insolvent"], "insolvent": ["destitute"],
    "bilingual": ["polyglot"], "polyglot": ["bilingual"], "polymath": ["polyglot"], "somnambulist": ["insomniac"], "insomniac": ["somnambulist"],
}
# Pairs that could be argued as near-equivalents are never put side by side as key and wrong option, and a confusable listed above is the only
# way a same-group word is allowed as a distractor.
_NEVER = {frozenset(p) for p in [("hypocrite", "sycophant"), ("pedant", "hypocrite"), ("sceptic", "cynic"), ("destitute", "insolvent"), ("optimist", "altruist"),
                                  ("illegible", "inaudible"), ("lethargy", "desuetude"), ("miser", "egoist"), ("ascetic", "pacifist"), ("novice", "amateur"),
                                  ("amateur", "novice"), ("incorrigible", "indelible"), ("sceptic", "agnostic"), ("agnostic", "mystic"), ("ascetic", "mystic")]}

WORDS = [word(i, w, "ows", m, ex=e) for i, w, m, e, g in _O]
_W = {i: w for i, w, m, e, g in _O}
_M = {i: m for i, w, m, e, g in _O}
_GR = {i: g for i, w, m, e, g in _O}
_RARE = {"desuetude", "interregnum", "sycophant", "polymath", "numismatist", "philistine", "pedant", "plutocracy", "theocracy", "nostalgia", "regicide",
         "credulous", "epicure", "connoisseur", "sanatorium", "apiary", "amnesty", "mystic", "ascetic", "insatiable", "indelible"}
_STEM = "Select the word that can be used as a substitute for the given group of words.\n"
_ids = [i for i, *_ in _O]


def _cap(w):
    return w[0].upper() + w[1:]


def _lc(m):
    return m[0].lower() + m[1:]


def _gen():
    items = []
    for n, wid in enumerate(_ids, 1):
        opts_ids = [d for d in _CONF.get(wid, []) if frozenset((wid, d)) not in _NEVER][:2]
        pool = [x for x in _ids if x != wid and _GR[x] != _GR[wid] and x not in opts_ids and not (x in _CONF and wid in _CONF[x])]
        j = (n * 7) % len(pool)
        seen = {_GR[wid]} | {_GR[d] for d in opts_ids}
        while len(opts_ids) < 3:
            c = pool[j % len(pool)]
            if _GR[c] not in seen and frozenset((wid, c)) not in _NEVER:
                opts_ids.append(c); seen.add(_GR[c])
            j += 3
        kpos = n % 4
        order = opts_ids[:]; order.insert(kpos, wid)
        wrong, conf = {}, False
        for ltr, oid in zip("abcd", order):
            if oid == wid: continue
            if oid in _CONF.get(wid, []):
                conf = True
                wrong[ltr] = mistake(f"'{_W[oid]}' looks like the right word but means {_lc(_M[oid])}.")
            else:
                wrong[ltr] = ruled_out(f"'{_W[oid]}' means {_lc(_M[oid])}.")
        rare = wid in _RARE
        items.append(q("q-ows", "ows", _STEM + _M[wid], [_cap(_W[o]) for o in order], "abcd"[kpos],
                       f"'{_W[wid]}' is the word for: {_lc(_M[wid])}.", wrong, lex=("ows", wid), uid=f"ow-g{n:03d}",
                       rules=["ow-r1", "ow-r2"] if conf else ["ow-r1"], tech=["root-prefix"], rare=rare))
    return items


def _pq(qno, paper, wid, options, key, why, wrong, **kw):
    return q("q-ows", "ows", f"Choose the correct one-word substitute for: '{_M[wid]}'.", options, key, why, wrong, lex=("ows", wid),
             paper=paper, qno=qno, rules=["ow-r1"], tech=["root-prefix"], **kw)


S1, S2, S3 = "2025-09-12-S1", "2025-09-12-S2", "2025-09-12-S3"

PYQS = [
    _pq(84, S1, "bilingual", ["Accusation", "Denunciation", "Bilingual", "Indictment"], "c",
        "Bilingual joins bi (two) and lingua (tongue): a person who speaks two languages.",
        {"a": ruled_out("An accusation is a charge of wrongdoing; it has nothing to do with language."),
         "b": ruled_out("A denunciation is a public condemnation of someone."),
         "d": ruled_out("An indictment is a formal charge of a crime.")},
        trick="bi- means two; lingua is the tongue."),
    _pq(76, S2, "ascetic", ["Skeptic", "Ascetic", "Mystic", "Agnostic"], "b",
        "An ascetic gives up pleasures and lives with strict self-discipline, usually for spiritual reasons.",
        {"a": ruled_out("A sceptic doubts accepted beliefs; the word says nothing about self-denial."),
         "c": mistake("A mystic seeks union with God through meditation. Mystics are often ascetics too, but the phrase asks for the one who gives up pleasures, and that is the ascetic."),
         "d": ruled_out("An agnostic holds that God's existence cannot be known; it is about belief, not lifestyle.")},
        trick="Ascetic: the self-denial, not the belief, is the point.", rare=True),
    _pq(99, S3, "desuetude", ["Interregnum", "Destitute", "Lethargy", "Desuetude"], "d",
        "Desuetude is the state of no longer being used or practised, as when a custom falls out of use.",
        {"a": ruled_out("An interregnum is the period between two reigns or governments."),
         "b": mistake("Destitute means without money and basic necessities. It sounds like 'desuetude', but it describes poverty, not disuse."),
         "c": mistake("Lethargy is drowsy lack of energy in a person; desuetude is about a custom or law no longer being used.")},
        trick="Desuetude comes from the Latin for 'to become unaccustomed': a custom no longer used.", rare=True),
]


def practice_items():
    hand = [
        q("q-ows", "ows", _STEM + "One who knows everything", ["Omnipotent", "Omniscient", "Omnipresent", "Philanthropist"], "b",
          "Omniscient is built from omni (all) and scient (knowing): one who knows everything.",
          {"a": mistake("Omnipotent means all-powerful: it shares the root omni but not the sense of knowing."),
           "c": mistake("Omnipresent means present everywhere, not knowing everything."),
           "d": ruled_out("A philanthropist is a person who loves mankind and helps others.")},
          lex=("ows", "omniscient"), uid="ow-p01", rules=["ow-r1", "ow-r2"], tech=["root-prefix"]),
        q("q-ows", "ows", _STEM + "One who hates mankind", ["Philanthropist", "Bibliophile", "Misanthrope", "Somnambulist"], "c",
          "Misanthrope joins miso (hate) and anthropos (man): one who hates mankind.",
          {"a": mistake("Philanthropist has the same anthropo root but phil means love, so it is the opposite sense."),
           "b": ruled_out("A bibliophile is a lover of books."),
           "d": ruled_out("A somnambulist is one who walks in sleep.")},
          lex=("ows", "misanthrope"), uid="ow-p02", rules=["ow-r1", "ow-r2"], tech=["root-prefix"]),
    ]
    return hand + _gen()
