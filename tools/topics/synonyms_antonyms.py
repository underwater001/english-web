"""Synonyms & antonyms: 7 past questions (12 Sep 2025 similar papers), 8 hand-written practice questions and one generated
practice question per word and direction. Every answer is checked against WORDS: the key is in the word's list, no wrong
option is. Distractors come from words in other groups, and each distractor note quotes that word's own meaning."""
from bank import mistake, ruled_out, q, word

TOPIC = "synonyms-antonyms"
TIER = "full"
PREFIX = "sa"

NODES = {
    "q-syn": {"short": "Synonym", "label": "Closest in meaning", "kind": "qtype", "parent": TOPIC, "order": 1,
              "summary": "One capitalised word; pick the option closest in meaning.", "links": []},
    "q-ant": {"short": "Antonym", "label": "Opposite in meaning", "kind": "qtype", "parent": TOPIC, "order": 2,
              "summary": "One capitalised word; pick the option opposite in meaning.", "links": []},
}

RULES = [
    {"id": "sa-r1", "node": "q-syn", "text": "A word is positive, negative or neutral in tone. Its synonyms share the tone, so options of the opposite tone can be dropped at once.",
     "ok": "BENEVOLENT (positive): charitable, kindly.", "bad": "BENEVOLENT: malicious (negative) cannot be a synonym."},
    {"id": "sa-r2", "node": "q-ant", "text": "In an antonym question the word's synonym is almost always one of the options as a trap. Find the meaning first, then choose the opposite, not the same.",
     "ok": "SCARCE: plentiful is the opposite.", "bad": "SCARCE: rare means the same, so it is the trap."},
    {"id": "sa-r3", "node": "q-syn", "text": "Use the word's root or prefix when you do not know it: a-, in-, un-, non- usually negate; bene- is good, mal- is bad; poly- is many; anti- is against.",
     "ok": "POLYMATHIC: poly (many) + math (learning), so wide learning.", "bad": "Assuming 'poly' means 'one' and reading POLYMATHIC as narrow."},
]

METHODS = {
    "q-syn": {"cue": "'Select the most appropriate synonym of the given word' with one capitalised word.",
              "standard": "Recall the meaning, then pick the option that could replace the word in a sentence without changing it.",
              "fast": "Decide positive or negative first, drop options of the other tone, then choose among the rest.",
              "eliminate": "An antonym is usually among the options, so drop the option that opposes the word before comparing the others.",
              "traps": ["The antonym is almost always listed.", "A word that merely fits the same topic is not a synonym.",
                        "In recent papers the word is often rare (abjure, amorphous, duplicitous): use root and tone when you do not know it."],
              "rules": ["sa-r1", "sa-r3"], "tech": ["tone", "opposite-trap", "root-prefix"]},
    "q-ant": {"cue": "'Select the most appropriate antonym of the given word' with one capitalised word.",
              "standard": "Recall the meaning, then pick the option that says the reverse.",
              "fast": "Spot and ignore the synonym trap, then pick the option of the opposite tone.",
              "eliminate": "Cross out every option that is close in meaning to the word. What remains contains the answer.",
              "traps": ["The synonym is nearly always listed as bait, sometimes two or three of them.", "An unrelated word is not an antonym: the answer must reverse the meaning."],
              "rules": ["sa-r2"], "tech": ["tone", "opposite-trap"]},
}

REFS = []

# (id, word, pos, meaning, synonyms, antonyms, own example sentence, group, rare)
_W = [
    ("benevolent", "benevolent", "adj", "Kind and generous towards others.", ["charitable", "kindly", "generous", "humane"], ["malicious", "malevolent", "cruel", "stingy"],
     "The benevolent landlord waived the rent for families who had lost their jobs.", "kind", False),
    ("frugal", "frugal", "adj", "Careful with money and resources; not wasteful.", ["thrifty", "economical", "sparing"], ["lavish", "extravagant", "wasteful"],
     "She led a frugal life and saved half of every salary.", "money", False),
    ("obsolete", "obsolete", "adj", "No longer in use because something newer has replaced it.", ["outdated", "outmoded", "archaic"], ["modern", "current", "contemporary"],
     "Film cameras became obsolete once digital ones arrived.", "time", False),
    ("verbose", "verbose", "adj", "Using more words than are needed.", ["wordy", "long-winded", "prolix"], ["concise", "terse", "succinct"],
     "His verbose reply took ten minutes to say what a sentence could have said.", "words", True),
    ("scarce", "scarce", "adj", "Not available in enough quantity.", ["rare", "meagre", "sparse", "insufficient"], ["plentiful", "abundant", "ample"],
     "Clean water is scarce in the region during summer.", "quantity", False),
    ("ephemeral", "ephemeral", "adj", "Lasting for a very short time.", ["fleeting", "transient", "short-lived", "brief"], ["eternal", "permanent", "enduring"],
     "The ephemeral beauty of the cherry blossom lasts about a week.", "time", True),
    ("diligent", "diligent", "adj", "Showing steady, careful effort in work.", ["industrious", "hardworking", "assiduous"], ["lazy", "indolent", "negligent"],
     "A diligent student, she revised every lesson on the day it was taught.", "work", False),
    ("candid", "candid", "adj", "Truthful and straightforward, even when it is uncomfortable.", ["frank", "honest", "forthright", "open"], ["devious", "evasive", "secretive"],
     "He gave a candid account of what had gone wrong with the project.", "truth", False),
    ("transient", "transient", "adj", "Lasting for a very short time.", ["temporary", "fleeting", "momentary", "brief"], ["permanent", "lasting", "enduring", "perpetual"],
     "A transient heatwave passed through the region in just two days.", "time", False),
    ("enervate", "enervate", "verb", "To cause someone to feel drained of energy or vitality.", ["debilitate", "weaken", "enfeeble", "sap"], ["invigorate", "strengthen", "energize", "fortify"],
     "The humid afternoon heat seemed to enervate everyone in the hall.", "energy", True),
    ("venerate", "venerate", "verb", "To regard with great respect; to revere.", ["revere", "respect", "honour", "admire"], ["despise", "scorn", "disdain", "deride"],
     "The villagers still venerate the old banyan tree as sacred.", "respect", False),
    # words from the 12 Sep 2025 papers
    ("duplicitous", "duplicitous", "adj", "Deliberately deceptive in speech or action.", ["deceitful", "two-faced", "dishonest", "treacherous"], ["candid", "honest", "sincere", "faithful", "loyal"],
     "The duplicitous agent sold secrets to both sides.", "truth", True),
    ("abjure", "abjure", "verb", "To give up a belief, claim or habit formally and solemnly.", ["renounce", "relinquish", "forswear"], ["retain", "embrace", "adopt", "uphold"],
     "He abjured violence after the war and became a teacher of peace.", "bad", True),
    ("potent", "potent", "adj", "Having great power or a strong effect.", ["powerful", "strong", "mighty", "effective"], ["feeble", "weak", "impotent", "ineffectual"],
     "A potent medicine must be taken in the exact dose prescribed.", "strength", False),
    ("polymathic", "polymathic", "adj", "Having wide learning in many different subjects.", ["erudite", "learned", "well-read", "knowledgeable"], ["uninformed", "ignorant", "unlettered", "ill-informed"],
     "Leonardo's polymathic mind moved easily between art, anatomy and engineering.", "mind", True),
    ("eulogy", "eulogy", "noun", "A speech or piece of writing that praises someone highly.", ["panegyric", "tribute", "commendation", "praise"], ["castigation", "censure", "condemnation", "denunciation"],
     "The minister delivered a moving eulogy at the funeral of the poet.", "praise", True),
    ("amorphous", "amorphous", "adj", "Without a clear shape or structure.", ["vague", "shapeless", "formless", "indistinct"], ["definite", "distinct", "clear", "structured", "precise"],
     "The plan was still amorphous, with no fixed dates or duties.", "words", True),
    # high-frequency SSC words
    ("abate", "abate", "verb", "To become less in force or amount.", ["subside", "ease", "diminish", "lessen"], ["intensify", "escalate", "increase", "swell"],
     "The storm abated by morning and the ferries began to run.", "strength", False),
    ("abstain", "abstain", "verb", "To choose not to do or take something.", ["refrain", "desist", "forgo", "hold back"], ["indulge", "partake", "participate"],
     "Patients were told to abstain from salt before the test.", "social", False),
    ("adamant", "adamant", "adj", "Refusing to change one's mind or position.", ["obstinate", "unyielding", "firm", "stubborn"], ["flexible", "yielding", "pliable"],
     "She was adamant that the meeting could not be postponed.", "bold", False),
    ("affluent", "affluent", "adj", "Having a great deal of money.", ["wealthy", "rich", "prosperous", "well-off"], ["poor", "destitute", "impoverished"],
     "The affluent suburb has three private hospitals.", "money", False),
    ("alleviate", "alleviate", "verb", "To make pain or a problem less severe.", ["relieve", "ease", "mitigate", "soothe"], ["aggravate", "worsen", "intensify"],
     "New wells will alleviate the water shortage in the village.", "strength", False),
    ("ambiguous", "ambiguous", "adj", "Open to more than one meaning.", ["unclear", "equivocal", "doubtful", "uncertain"], ["clear", "explicit", "unambiguous", "definite"],
     "The ambiguous clause let both sides claim victory.", "words", False),
    ("arduous", "arduous", "adj", "Needing great effort and stamina.", ["strenuous", "laborious", "gruelling", "demanding"], ["easy", "effortless", "simple"],
     "The arduous climb took nine hours.", "work", False),
    ("audacious", "audacious", "adj", "Boldly daring and willing to take risks.", ["bold", "daring", "fearless", "brazen"], ["timid", "cautious", "cowardly", "meek"],
     "It was an audacious plan to cross the river at night.", "bold", False),
    ("brevity", "brevity", "noun", "The quality of using few words.", ["conciseness", "terseness", "succinctness", "shortness"], ["verbosity", "wordiness", "prolixity"],
     "Brevity is the soul of a good telegram.", "words", False),
    ("clandestine", "clandestine", "adj", "Kept secret, usually because it is improper.", ["secret", "covert", "furtive", "surreptitious"], ["open", "overt", "public", "above-board"],
     "They held a clandestine meeting behind the warehouse.", "truth", True),
    ("coerce", "coerce", "verb", "To force someone to act by threats or pressure.", ["compel", "force", "pressurise", "oblige"], ["persuade", "convince", "entice"],
     "No employee should be coerced into signing the paper.", "social", False),
    ("concur", "concur", "verb", "To agree with someone or something.", ["agree", "assent", "accord", "concede"], ["differ", "disagree", "dissent"],
     "The two judges concurred on the verdict.", "social", False),
    ("conspicuous", "conspicuous", "adj", "Easy to see or notice.", ["obvious", "noticeable", "prominent", "striking"], ["inconspicuous", "hidden", "unnoticeable", "obscure"],
     "His red coat was conspicuous in the grey crowd.", "bad", False),
    ("contempt", "contempt", "noun", "A feeling that someone or something is worthless.", ["scorn", "disdain", "disrespect", "derision"], ["respect", "admiration", "esteem", "regard"],
     "He looked at the cheat with open contempt.", "praise", False),
    ("copious", "copious", "adj", "Existing in large amounts.", ["abundant", "plentiful", "ample", "profuse"], ["scanty", "meagre", "sparse", "inadequate"],
     "She took copious notes throughout the lecture.", "quantity", False),
    ("cursory", "cursory", "adj", "Done quickly without attention to detail.", ["hasty", "superficial", "perfunctory", "fleeting"], ["thorough", "careful", "detailed", "meticulous"],
     "He gave the contract only a cursory glance before signing it.", "work", True),
    ("dearth", "dearth", "noun", "A lack or shortage of something.", ["scarcity", "shortage", "lack", "paucity"], ["abundance", "plenty", "surplus", "glut"],
     "There is a dearth of trained nurses in rural clinics.", "quantity", True),
    ("derogatory", "derogatory", "adj", "Showing a low opinion of someone.", ["insulting", "disparaging", "belittling", "uncomplimentary"], ["complimentary", "flattering", "respectful", "appreciative"],
     "The editor apologised for the derogatory remark about farmers.", "praise", True),
    ("diffident", "diffident", "adj", "Lacking confidence in oneself.", ["shy", "timid", "reserved", "bashful"], ["confident", "bold", "assertive", "outgoing"],
     "A diffident speaker, he kept his eyes on his notes.", "social", True),
    ("eloquent", "eloquent", "adj", "Fluent and persuasive in speech or writing.", ["articulate", "fluent", "expressive", "persuasive"], ["inarticulate", "tongue-tied", "hesitant"],
     "Her eloquent plea won the support of the whole hall.", "words", False),
    ("exacerbate", "exacerbate", "verb", "To make a bad situation worse.", ["aggravate", "worsen", "intensify", "inflame"], ["alleviate", "soothe", "relieve", "improve"],
     "Delay will only exacerbate the shortage of beds.", "strength", True),
    ("frivolous", "frivolous", "adj", "Not serious or sensible.", ["trivial", "silly", "flippant", "petty"], ["serious", "sensible", "earnest", "grave"],
     "The court dismissed the frivolous petition at once.", "mood", False),
    ("gregarious", "gregarious", "adj", "Fond of company; sociable.", ["sociable", "outgoing", "friendly", "convivial"], ["unsociable", "reclusive", "withdrawn"],
     "Her gregarious nature made her the centre of every party.", "social", False),
    ("hostile", "hostile", "adj", "Unfriendly and ready to oppose.", ["antagonistic", "unfriendly", "aggressive", "belligerent"], ["friendly", "amiable", "cordial", "welcoming"],
     "The crowd was hostile to the new rule.", "social", False),
    ("impeccable", "impeccable", "adj", "Without any fault.", ["flawless", "faultless", "perfect", "immaculate"], ["flawed", "faulty", "imperfect", "blemished"],
     "Her impeccable record earned her a quick promotion.", "bad", True),
    ("irascible", "irascible", "adj", "Easily made angry; quick-tempered.", ["short-tempered", "testy", "irritable", "touchy"], ["calm", "even-tempered", "placid", "tranquil"],
     "His irascible boss snapped at the smallest delay.", "mood", False),
    ("innocuous", "innocuous", "adj", "Not harmful or offensive.", ["harmless", "safe", "inoffensive", "benign"], ["harmful", "noxious", "dangerous", "toxic"],
     "The remark seemed innocuous until he heard the tone.", "bad", True),
    ("lucid", "lucid", "adj", "Clearly expressed and easy to understand.", ["clear", "intelligible", "comprehensible", "transparent"], ["obscure", "confused", "muddled"],
     "The teacher gave a lucid account of the water cycle.", "words", False),
    ("magnanimous", "magnanimous", "adj", "Generous and forgiving, especially towards a rival.", ["generous", "big-hearted", "noble", "forgiving"], ["petty", "mean", "vindictive", "ungenerous"],
     "The champion was magnanimous in victory and praised his opponent.", "kind", True),
    ("meticulous", "meticulous", "adj", "Showing great attention to detail.", ["careful", "precise", "painstaking", "thorough"], ["careless", "sloppy", "negligent", "slapdash"],
     "She kept meticulous records of every expense.", "work", False),
    ("mundane", "mundane", "adj", "Ordinary and lacking interest.", ["ordinary", "routine", "humdrum", "everyday"], ["extraordinary", "exciting", "remarkable", "unusual"],
     "He escaped his mundane office job by painting at night.", "mood", False),
    ("nefarious", "nefarious", "adj", "Wicked or criminal.", ["wicked", "evil", "villainous", "sinister"], ["virtuous", "honourable", "noble", "righteous"],
     "The police uncovered a nefarious plot to forge ration cards.", "bad", True),
    ("obstinate", "obstinate", "adj", "Stubbornly refusing to change.", ["stubborn", "headstrong", "pig-headed", "inflexible"], ["compliant", "yielding", "docile", "amenable"],
     "The obstinate mule would not cross the bridge.", "bold", False),
    ("ostentatious", "ostentatious", "adj", "Designed to impress; showy.", ["showy", "flamboyant", "pretentious", "flashy"], ["modest", "unpretentious", "restrained", "simple"],
     "The ostentatious wedding cost more than the whole village earns in a year.", "bold", True),
    ("pragmatic", "pragmatic", "adj", "Dealing with things sensibly and realistically.", ["practical", "realistic", "sensible", "down-to-earth"], ["impractical", "idealistic", "unrealistic", "visionary"],
     "A pragmatic leader accepts a small gain now over a big promise later.", "mind", False),
    ("prudent", "prudent", "adj", "Careful and sensible about the future.", ["wise", "cautious", "judicious", "sensible"], ["imprudent", "rash", "reckless", "foolish"],
     "It is prudent to keep some savings for an emergency.", "mind", False),
    ("recalcitrant", "recalcitrant", "adj", "Stubbornly resisting authority or control.", ["defiant", "disobedient", "unruly", "refractory"], ["obedient", "compliant", "docile", "submissive"],
     "The recalcitrant student ignored every warning.", "bold", True),
    ("rebuke", "rebuke", "verb", "To express sharp disapproval or criticism of someone.", ["reprimand", "admonish", "reprove", "censure"], ["applaud", "praise", "commend", "compliment"],
     "The coach rebuked the team for their careless play.", "praise", False),
    ("reprimand", "reprimand", "verb", "To criticise someone formally for a fault.", ["rebuke", "scold", "admonish", "reproach"], ["praise", "commend", "applaud", "compliment"],
     "The officer was reprimanded for arriving late.", "praise", False),
    ("suave", "suave", "adj", "Smoothly charming, confident and polished in manner.", ["urbane", "polished", "charming", "smooth"], ["awkward", "gauche", "uncouth", "boorish"],
     "The suave diplomat put everyone at ease within minutes.", "mood", False),
    ("serene", "serene", "adj", "Calm and untroubled.", ["calm", "tranquil", "peaceful", "placid"], ["agitated", "turbulent", "troubled", "stormy"],
     "The lake looked serene in the early light.", "mood", False),
    ("sporadic", "sporadic", "adj", "Happening now and then, not regularly.", ["occasional", "intermittent", "irregular", "scattered"], ["frequent", "constant", "continual", "regular"],
     "Sporadic firing was heard through the night.", "time", False),
    ("tedious", "tedious", "adj", "Too long, slow or dull.", ["boring", "monotonous", "dull", "tiresome"], ["interesting", "exciting", "engaging", "stimulating"],
     "Copying the register by hand was a tedious task.", "mood", False),
    ("vindicate", "vindicate", "verb", "To clear someone of blame or show them to be right.", ["exonerate", "absolve", "acquit", "justify"], ["blame", "condemn", "accuse", "convict"],
     "The audit vindicated the manager.", "praise", True),
    ("zealous", "zealous", "adj", "Full of eager and strong enthusiasm.", ["ardent", "fervent", "enthusiastic", "passionate"], ["apathetic", "indifferent", "unenthusiastic", "lukewarm"],
     "A zealous volunteer, she never missed a camp.", "mood", False),
    ("appease", "appease", "verb", "To calm someone by giving in to their demands.", ["pacify", "placate", "soothe", "mollify"], ["provoke", "anger", "incite", "enrage"],
     "The company offered a refund to appease angry customers.", "social", False),
    ("conceal", "conceal", "verb", "To keep something hidden.", ["hide", "cover", "mask", "veil"], ["reveal", "disclose", "expose", "uncover"],
     "He tried to conceal his disappointment behind a smile.", "truth", False),
    ("condemn", "condemn", "verb", "To express strong disapproval of something.", ["censure", "denounce", "criticise", "blame"], ["praise", "approve", "applaud", "commend"],
     "Leaders of all parties condemned the attack.", "praise", False),
    ("feeble", "feeble", "adj", "Lacking physical or moral strength.", ["weak", "frail", "puny", "infirm"], ["strong", "robust", "sturdy", "vigorous"],
     "The feeble old man needed a stick to cross the road.", "strength", False),
    ("rigid", "rigid", "adj", "Not able to bend or change.", ["stiff", "inflexible", "strict", "unbending"], ["flexible", "pliable", "supple", "lenient"],
     "The company's rigid rules left no room for exceptions.", "strength", False),
    ("wary", "wary", "adj", "Cautious about possible danger.", ["cautious", "careful", "watchful", "vigilant"], ["careless", "reckless", "unwary", "heedless"],
     "Travellers are wary of strangers offering cheap tickets.", "mind", False),
    ("vital", "vital", "adj", "Absolutely necessary or very important.", ["essential", "crucial", "indispensable", "critical"], ["trivial", "unimportant", "inessential", "minor"],
     "Water is vital for every living thing.", "bad", False),
    ("gloomy", "gloomy", "adj", "Dark, or without hope or cheer.", ["dismal", "glum", "sombre", "depressing"], ["cheerful", "bright", "hopeful", "jovial"],
     "The gloomy forecast kept shoppers at home.", "mood", False),
    ("lenient", "lenient", "adj", "More merciful or tolerant than expected.", ["merciful", "tolerant", "indulgent", "permissive"], ["strict", "harsh", "stern", "severe"],
     "The judge was lenient with the first-time offender.", "kind", False),
    ("abundant", "abundant", "adj", "Present in large quantity.", ["plentiful", "ample", "profuse", "bountiful"], ["scanty", "meagre", "sparse", "deficient"],
     "Fish are abundant in the delta.", "quantity", False),
]

WORDS = [word(i, w, "word", m, pos=p, syn=s, ant=a, ex=e) for i, w, p, m, s, a, e, g, r in _W]
_BY = {i: (w, m, s, a, g, r) for i, w, p, m, s, a, e, g, r in _W}


def _lower(m):
    return m[0].lower() + m[1:].rstrip(".")


def _pick(i, n, k):
    """Deterministic distractor words from other groups, avoiding the word itself."""
    gi = _BY[_W[i][0]][4]
    pool = [x for x in _W if x[7] != gi]
    out, step = [], 7
    j = (i * 11 + k * 5) % len(pool)
    while len(out) < n:
        c = pool[j % len(pool)]
        if c[0] not in [o[0] for o in out]:
            out.append(c)
        j += step
    return out


def _arrange(opts, key_idx, pos):
    """Place the key option at index pos (0-3); keep the others in order."""
    rest = [o for n, o in enumerate(opts) if n != key_idx]
    rest.insert(pos, opts[key_idx])
    return rest


def _cap(s):
    return s[0].upper() + s[1:]


def _gen():
    items = []
    n = 0
    for i, (wid, w, pos, meaning, syn, ant, ex, grp, rare) in enumerate(_W):
        rules_syn = ["sa-r1", "sa-r3"] if rare else ["sa-r1"]
        rules_ant = ["sa-r2", "sa-r1"] if rare else ["sa-r2"]
        # synonym question: key = a synonym, one antonym trap, two other words
        if ant:
            d = _pick(i, 2, 1)
            key = syn[(i + 1) % len(syn)]
            trap = ant[i % len(ant)]
            opts = [key, trap, d[0][1], d[1][1]]
            kpos = i % 4
            order = _arrange(opts, 0, kpos)
            letters = "abcd"
            wrong = {}
            for ltr, o in zip(letters, order):
                if o == key: continue
                if o == trap: wrong[ltr] = mistake(f"{_cap(o)} is an antonym of {w}: it carries the opposite sense, the usual bait in synonym questions.")
                else:
                    dw = next(x for x in _W if x[1] == o)
                    wrong[ltr] = ruled_out(f"{_cap(o)} means {_lower(dw[3])}, which is not the sense of {w}.")
            n += 1
            items.append(q("q-syn", "synonym", f"Select the most appropriate synonym of the given word.\n{w.upper()}", [_cap(o) for o in order], letters[kpos],
                           f"{_cap(w)} means {_lower(meaning)}; {key} carries the same sense.", wrong, lex=("syn", wid), uid=f"sa-g{n:03d}",
                           rare=rare, rules=rules_syn, tech=["tone", "opposite-trap"] + (["root-prefix"] if "sa-r3" in rules_syn else [])))
        # antonym question: key = an antonym, one synonym trap, two other words
        if len(ant) >= 3:
            d = _pick(i, 2, 2)
            key = ant[(i + 1) % len(ant)]
            trap = syn[i % len(syn)]
            opts = [key, trap, d[0][1], d[1][1]]
            kpos = (i + 2) % 4
            order = _arrange(opts, 0, kpos)
            letters = "abcd"
            wrong = {}
            for ltr, o in zip(letters, order):
                if o == key: continue
                if o == trap: wrong[ltr] = mistake(f"{_cap(o)} is a synonym of {w}: it says the same thing, so it is the bait in an antonym question.")
                else:
                    dw = next(x for x in _W if x[1] == o)
                    wrong[ltr] = ruled_out(f"{_cap(o)} means {_lower(dw[3])}; that is unrelated to {w}, not its opposite.")
            n += 1
            items.append(q("q-ant", "antonym", f"Select the most appropriate antonym of the given word.\n{w.upper()}", [_cap(o) for o in order], letters[kpos],
                           f"{_cap(w)} means {_lower(meaning)}; {key} says the reverse.", wrong, lex=("ant", wid), uid=f"sa-g{n:03d}",
                           rare=rare, rules=rules_ant, tech=["tone", "opposite-trap"]))
    return items


def _pq(qno, paper, qtype, fmt, text, options, key, why, wrong, **kw):
    return q(qtype, fmt, text, options, key, why, wrong, paper=paper, qno=qno, **kw)


S1, S2, S3 = "2025-09-12-S1", "2025-09-12-S2", "2025-09-12-S3"

PYQS = [
    _pq(90, S1, "q-syn", "synonym", "Select the most appropriate synonym of the given word.\nDUPLICITOUS", ["Honest", "Faithful", "Deceitful", "Loyal"], "c",
        "Duplicitous means deliberately deceptive; deceitful has the same sense.",
        {"a": mistake("Honest is the opposite of duplicitous: it means truthful."),
         "b": mistake("Faithful means true to a person or promise, the reverse of deceptive."),
         "d": mistake("Loyal means firm in support, again the reverse of duplicitous.")},
        lex=("syn", "duplicitous"), rare=True, rules=["sa-r1", "sa-r3"], tech=["tone", "opposite-trap"],
        trick="Duplicity = double dealing. Negative word, so only the negative option (deceitful) survives."),
    _pq(97, S1, "q-ant", "antonym", "Select the most appropriate antonym of the given word.\nDUPLICITOUS", ["Betraying", "Deceitful", "Candid", "Treacherous"], "c",
        "Duplicitous means deceptive; candid means frank and truthful, the reverse.",
        {"a": mistake("Betraying is on the same side as duplicitous: breaking trust by deceit."),
         "b": mistake("Deceitful is a synonym of duplicitous, so it is the bait."),
         "d": mistake("Treacherous is a synonym here: disloyal and deceptive.")},
        lex=("ant", "duplicitous"), rare=True, rules=["sa-r2", "sa-r1"], tech=["tone", "opposite-trap"],
        trick="Three negatives and one positive: the single positive word is the antonym."),
    _pq(77, S2, "q-syn", "synonym", "Select the most appropriate synonym of the given word.\nABJURE", ["Demand", "Accept", "Renounce", "Retain"], "c",
        "Abjure means to give up a belief or claim formally; renounce means the same.",
        {"a": ruled_out("Demand means to ask for forcefully, which is not giving anything up."),
         "b": mistake("Accept is the opposite direction: taking on what abjure gives up."),
         "d": mistake("Retain means to keep, the opposite of giving up.")},
        lex=("syn", "abjure"), rare=True, rules=["sa-r1", "sa-r3"], tech=["root-prefix", "opposite-trap"],
        trick="Ab- (away) + jure (swear): to swear away, i.e. give up. Re-nounce also means to declare away."),
    _pq(84, S2, "q-ant", "antonym", "Select the most appropriate antonym of the given word.\nPOTENT", ["Strong", "Robust", "Powerful", "Feeble"], "d",
        "Potent means powerful; feeble means lacking strength.",
        {"a": mistake("Strong is a synonym of potent, so it is bait."),
         "b": mistake("Robust describes strength and sturdiness, the same side as potent."),
         "c": mistake("Powerful is the direct synonym of potent.")},
        lex=("ant", "potent"), rules=["sa-r2"], tech=["opposite-trap"],
        trick="Three words mean strong; the odd one out is the answer."),
    _pq(76, S3, "q-ant", "antonym", "Select the most appropriate antonym of the given word: POLYMATHIC", ["Intellectual", "Uninformed", "Skilled", "Saintly"], "b",
        "Polymathic means having wide learning (poly = many, math = learning); uninformed means lacking knowledge.",
        {"a": mistake("Intellectual describes a thoughtful, learned person, which is on the same side as polymathic."),
         "c": mistake("Skilled means having ability, closer to polymathic than to its opposite."),
         "d": ruled_out("Saintly describes holiness and has nothing to do with the amount of knowledge.")},
        lex=("ant", "polymathic"), rare=True, rules=["sa-r2", "sa-r3"], tech=["root-prefix", "opposite-trap"],
        trick="Poly (many) + math (learning). Opposite of much learning is little knowledge: uninformed."),
    _pq(77, S3, "q-ant", "antonym", "Select the most appropriate antonym of the given word: Eulogy", ["Panegyric", "Tributary", "Castigation", "Pronunciation"], "c",
        "A eulogy is a speech of high praise; castigation is severe criticism.",
        {"a": mistake("Panegyric is a speech of praise: a synonym of eulogy."),
         "b": ruled_out("A tributary is a stream feeding a larger river; it only looks like 'tribute'."),
         "d": ruled_out("Pronunciation is how a word is spoken; it has nothing to do with praise or blame.")},
        lex=("ant", "eulogy"), rare=True, rules=["sa-r2", "sa-r3"], tech=["root-prefix", "opposite-trap"],
        trick="Eu- means good and logy is speech: a good speech. Opposite is harsh criticism."),
    _pq(94, S3, "q-syn", "synonym", "Select the most appropriate synonym of the given word: AMORPHOUS", ["Vague", "Clear", "Strict", "Accurate"], "a",
        "Amorphous means without a clear shape (a- without + morph shape); vague has the same sense of no clear form.",
        {"b": mistake("Clear is the opposite: something with a clear form or meaning."),
         "c": ruled_out("Strict means firm about rules; it does not describe shape or form."),
         "d": mistake("Accurate means exact, the reverse of formless and vague.")},
        lex=("syn", "amorphous"), rare=True, rules=["sa-r1", "sa-r3"], tech=["root-prefix", "opposite-trap"],
        trick="A- (without) + morph (shape). No shape means vague."),
    _pq(78, "2026-10-07", "q-syn", "synonym", "Select the most appropriate synonym of the given word.\nZealous", ["Envious", "Impersonal", "Enthusiastic", "Formal"], "c",
        "Zealous means full of eager enthusiasm; enthusiastic carries the same sense.",
        {"a": mistake("Envious means resentful of what someone else has, an unrelated negative feeling."),
         "b": ruled_out("Impersonal means detached and formal, the opposite feel of 'zealous'."),
         "d": mistake("Formal describes a style of behaviour, not the strength of feeling 'zealous' carries.")},
        lex=("syn", "zealous"), rules=["sa-r1"], tech=["opposite-trap"]),
    _pq(84, "2026-10-07", "q-ant", "antonym", "Select the most appropriate ANTONYM of the given word.\nArduous", ["Grueling", "Exhausting", "Effortless", "Tedious"], "c",
        "Arduous means needing great effort; effortless means needing none, the direct opposite.",
        {"a": mistake("Grueling is a synonym of arduous, describing something exhausting."), "b": mistake("Exhausting is also a synonym of arduous."),
         "d": mistake("Tedious means tiresome and dull, closer to arduous than to its opposite.")},
        lex=("ant", "arduous"), rules=["sa-r2"], tech=["opposite-trap"]),
    _pq(94, "2026-10-07", "q-ant", "antonym", "Select the correct Antonym of the given word.\nRebuke", ["Repulse", "Admonish", "Applaud", "Reprimand"], "c",
        "Rebuke means to criticise sharply; applaud means to praise, the direct opposite.",
        {"a": ruled_out("Repulse means to drive back or disgust, unrelated to criticism or praise."), "b": mistake("Admonish is a synonym of rebuke, meaning to criticise mildly."),
         "d": mistake("Reprimand is a direct synonym of rebuke.")},
        lex=("ant", "rebuke"), rules=["sa-r2"], tech=["opposite-trap"]),
    _pq(81, "2026-10-08", "q-syn", "synonym", "Select the most appropriate synonym of the given word.\nSuave", ["Urbane", "Prodigal", "Lament", "Nippy"], "a",
        "Suave means smoothly charming and confident in manner; urbane carries the same sense of polished ease.",
        {"b": ruled_out("Prodigal means wastefully extravagant, unrelated to charm or polish."),
         "c": ruled_out("Lament means to express grief, unrelated in sense."),
         "d": ruled_out("Nippy means quick or cold, unrelated to a charming manner.")},
        lex=("syn", "suave"), rules=["sa-r1"], tech=["opposite-trap"]),
    _pq(84, "2026-10-08", "q-ant", "antonym", "What is the antonym of \"Irascible\"?", ["Petulant", "Tranquil", "Hostile", "Fractious"], "b",
        "Irascible means easily made angry; tranquil means calm and even-tempered, the direct opposite.",
        {"a": mistake("Petulant is close in sense to irascible, describing a sulky, easily-irritated temper."),
         "c": mistake("Hostile describes an unfriendly, aggressive manner, close to the bad temper 'irascible' names, not its opposite."),
         "d": mistake("Fractious is a near-synonym of irascible, meaning easily upset or irritable.")},
        lex=("ant", "irascible"), rules=["sa-r2"], tech=["opposite-trap"]),
    _pq(82, "2026-10-09", "q-syn", "synonym", "Find the word most nearly SIMILAR in meaning to the given word:\nEnervate", ["Candid", "Judicious", "Debilitate", "Invigorate"], "c",
        "Enervate means to drain someone of energy or vitality; debilitate carries the same sense of weakening.",
        {"a": ruled_out("Candid means truthful and straightforward, unrelated to loss of energy."),
         "b": ruled_out("Judicious means showing good sense or sound judgement, unrelated to loss of energy."),
         "d": mistake("Invigorate means to fill with energy, the direct opposite of enervate, not its synonym.")},
        lex=("syn", "enervate"), rules=["sa-r1"], tech=["opposite-trap"]),
    _pq(85, "2026-10-09", "q-syn", "synonym", "Select the most appropriate synonym of the given word.\nTransient", ["Transparent", "Permanent", "Temporary", "Truthful"], "c",
        "Transient means lasting for a very short time; temporary carries the same sense.",
        {"a": ruled_out("Transparent means easy to see through or understand, unrelated to how long something lasts."),
         "b": mistake("Permanent means lasting indefinitely, the direct opposite of transient, not its synonym."),
         "d": ruled_out("Truthful means honest, unrelated to how long something lasts.")},
        lex=("syn", "transient"), rules=["sa-r1"], tech=["opposite-trap"]),
    _pq(98, "2026-10-09", "q-ant", "antonym", "Select the most appropriate antonym of the word: Venerate", ["Honor", "Despise", "Respect", "Admire"], "b",
        "Venerate means to regard with great respect; despise means to regard with contempt, the direct opposite.",
        {"a": mistake("Honor is a synonym of venerate."), "c": mistake("Respect is a synonym of venerate."),
         "d": mistake("Admire is a synonym of venerate.")},
        lex=("ant", "venerate"), rules=["sa-r2"], tech=["opposite-trap"]),
]


def practice_items():
    hand = [
        q("q-syn", "synonym", "Select the most appropriate synonym of the given word.\nBENEVOLENT", ["Malicious", "Charitable", "Reluctant", "Stingy"], "b",
          "Benevolent means kind and generous; charitable carries the same positive sense.",
          {"a": mistake("Malicious means wishing to harm: the opposite of benevolent, chosen by mistake when the tone is not checked."),
           "c": ruled_out("Reluctant means unwilling; it says nothing about kindness or generosity."),
           "d": mistake("Stingy means unwilling to give: it opposes benevolent, a classic antonym trap.")},
          lex=("syn", "benevolent"), uid="sa-p01", tech=["tone", "opposite-trap"], rules=["sa-r1"]),
        q("q-syn", "synonym", "Select the most appropriate synonym of the given word.\nFRUGAL", ["Thrifty", "Lavish", "Greedy", "Cheerful"], "a",
          "Frugal means careful with money; thrifty says the same thing.",
          {"b": mistake("Lavish means spending freely: the antonym of frugal, placed as bait."),
           "c": ruled_out("Greedy means wanting more than one needs; a frugal person is careful, not greedy."),
           "d": ruled_out("Cheerful describes mood, not the way a person spends money.")},
          lex=("syn", "frugal"), uid="sa-p02", tech=["tone", "opposite-trap"], rules=["sa-r1"]),
        q("q-syn", "synonym", "Select the most appropriate synonym of the given word.\nOBSOLETE", ["Modern", "Outdated", "Fragile", "Permanent"], "b",
          "Obsolete means no longer used because something newer has replaced it; outdated means the same.",
          {"a": mistake("Modern is the antonym of obsolete, chosen when the word is mixed up with its opposite."),
           "c": ruled_out("Fragile means easily broken and has no link to being out of use."),
           "d": ruled_out("Permanent means lasting for ever, which does not describe something that has gone out of use.")},
          lex=("syn", "obsolete"), uid="sa-p03", rules=["sa-r1"]),
        q("q-syn", "synonym", "Select the most appropriate synonym of the given word.\nVERBOSE", ["Concise", "Silent", "Wordy", "Humorous"], "c",
          "Verbose means using more words than needed; wordy is the direct synonym.",
          {"a": mistake("Concise is the antonym of verbose: it means brief and to the point."),
           "b": ruled_out("Silent means making no sound, the reverse of using many words."),
           "d": ruled_out("Humorous means funny; a verbose speaker need not be funny.")},
          lex=("syn", "verbose"), uid="sa-p04", rare=True, rules=["sa-r1"]),
        q("q-ant", "antonym", "Select the most appropriate antonym of the given word.\nSCARCE", ["Rare", "Plentiful", "Limited", "Meagre"], "b",
          "Scarce means not available in enough quantity; plentiful means available in large quantity.",
          {"a": mistake("Rare is a synonym of scarce, which is why it is placed as the trap."),
           "c": mistake("Limited is close in meaning to scarce, so it is a synonym-side trap, not the opposite."),
           "d": mistake("Meagre means small in amount, the same side as scarce.")},
          lex=("ant", "scarce"), uid="sa-p05", tech=["opposite-trap"], rules=["sa-r2"]),
        q("q-ant", "antonym", "Select the most appropriate antonym of the given word.\nEPHEMERAL", ["Fleeting", "Transient", "Eternal", "Brief"], "c",
          "Ephemeral means lasting a very short time; eternal means lasting for ever.",
          {"a": mistake("Fleeting is a synonym of ephemeral."),
           "b": mistake("Transient is a synonym of ephemeral."),
           "d": mistake("Brief is a synonym of ephemeral: it describes the same short duration.")},
          lex=("ant", "ephemeral"), uid="sa-p06", rare=True, tech=["opposite-trap"], rules=["sa-r2"]),
        q("q-ant", "antonym", "Select the most appropriate antonym of the given word.\nDILIGENT", ["Industrious", "Lazy", "Careful", "Eager"], "b",
          "Diligent means steadily hardworking; lazy means unwilling to work.",
          {"a": mistake("Industrious is a synonym of diligent."),
           "c": ruled_out("Careful describes attention to detail and is closer to diligent than to its opposite."),
           "d": ruled_out("Eager means keen; it is not the opposite of working steadily.")},
          lex=("ant", "diligent"), uid="sa-p07", tech=["opposite-trap"], rules=["sa-r2"]),
        q("q-ant", "antonym", "Select the most appropriate antonym of the given word.\nCANDID", ["Frank", "Honest", "Devious", "Open"], "c",
          "Candid means truthful and straightforward; devious means using indirect or dishonest means.",
          {"a": mistake("Frank is a synonym of candid."),
           "b": mistake("Honest is a synonym of candid."),
           "d": mistake("Open is a synonym of candid in the sense of being straightforward.")},
          lex=("ant", "candid"), uid="sa-p08", tech=["opposite-trap"], rules=["sa-r2"]),
    ]
    return hand + _gen()
