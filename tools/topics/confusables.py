"""Words often confused and misused. Seed tier: Plinth to Paramount gives these a chapter of their own, and SSC asks them as
fill-in-the-blank and sentence-improvement questions. Every answer is checked against the stored word, and the word it is set
against is always among the options, because that is the whole difficulty."""
from bank import mistake, ruled_out, q, word

TOPIC = "confusables"
TIER = "seed"
PREFIX = "cf"

NODES = {
    "q-cf-fit": {"short": "Which word", "label": "Choose between the confused words", "kind": "qtype", "parent": TOPIC, "order": 1,
                 "summary": "A sentence with a blank, and the pair it is usually confused with among the options.", "links": []},
    "q-cf-spot": {"short": "Spot it", "label": "The confused word inside a sentence", "kind": "qtype", "parent": TOPIC, "order": 2,
                  "summary": "One part of the sentence uses the partner word by mistake.", "links": []},
}

RULES = [
    {"id": "cf-r1", "node": "q-cf-fit", "text": "Several pairs differ only as noun and verb: advice (noun) / advise (verb), practice (noun) / practise (verb), effect (noun) / affect (verb), licence (noun) / license (verb). Decide which part of speech the slot needs first.",
     "ok": "Take my advice; I advise you to wait. The effect was clear; it did not affect me.", "bad": "Take my advise; the affect was clear."},
    {"id": "cf-r2", "node": "q-cf-fit", "text": "Some pairs differ by one letter and have nothing else in common: principal (chief, or head of a college) / principle (a rule); stationary (not moving) / stationery (paper and pens); complement (completes) / compliment (praise); desert (sand) / dessert (sweet).",
     "ok": "The principal explained the principle.", "bad": "The principle explained the principal."},
    {"id": "cf-r3", "node": "q-cf-fit", "text": "Some pairs are close in sense and so get swapped: eminent (famous) / imminent (about to happen); continual (repeated with breaks) / continuous (without a break); childish (silly) / childlike (innocent); economic (of the economy) / economical (thrifty); credible (believable) / credulous (too ready to believe).",
     "ok": "An eminent judge warned of an imminent crisis.", "bad": "An imminent judge warned of an eminent crisis."},
    {"id": "cf-r4", "node": "q-cf-spot", "text": "Lie, rise and sit take no object; lay, raise and set take one. Lie-lay-lain is to rest; lay-laid-laid is to put something down.",
     "ok": "He lies down after lunch. He laid the book on the table.", "bad": "He lays down after lunch. He lied the book on the table."},
]

METHODS = {
    "q-cf-fit": {"cue": "A blank with two look-alike or sound-alike words among the four options.",
                 "standard": "Decide what part of speech and what meaning the slot needs, then pick the member of the pair that has it.",
                 "fast": "For noun-and-verb pairs, test whether 'a' or 'the' could stand in front of the blank: if it could, the noun is wanted.",
                 "eliminate": "Cross out the unrelated options first; the real choice is almost always between two of the four.",
                 "traps": ["Advice and advise, practice and practise, effect and affect.",
                           "Principal and principle, stationary and stationery.",
                           "Eminent and imminent, continual and continuous, credible and credulous."],
                 "rules": ["cf-r1", "cf-r2", "cf-r3"], "tech": ["back-substitute", "context-clue"]},
    "q-cf-spot": {"cue": "A long sentence in which one word of a confused pair has been used for the other.",
                  "standard": "Read each part and test any word you know to have a twin. Replace it with its partner and see which reading makes sense.",
                  "fast": "Scan for the known pairs first: lie/lay, affect/effect, principal/principle.",
                  "eliminate": "Parts with no word from a confused pair can be skipped.",
                  "traps": ["'Lay down' for 'lie down'.", "'Comprises of', where 'comprises' takes no 'of'."],
                  "rules": ["cf-r4", "cf-r1"], "tech": ["read-whole"]},
}

REFS = []

# Sets of words the exam confuses with each other. (id, word, our meaning, our example, a sentence with the blank)
_SETS = [
    ("advice", [("advice", "advice", "guidance offered to somebody (a noun)", "Her advice saved us a week's work.", "I took his ___ and applied a day early."),
                ("advise", "advise", "to offer guidance (a verb)", "I advise you to read the rules first.", "The doctor will ___ you to rest for a week.")]),
    ("practice", [("practice", "practice", "the doing of something repeatedly, or a profession (a noun)", "Daily practice improved his speed.", "An hour of ___ every morning changed his handwriting."),
                  ("practise", "practise", "to do something repeatedly in order to improve (a verb)", "She practises the flute before school.", "You must ___ the same sum until it takes one minute.")]),
    ("effect", [("effect", "effect", "a result (a noun)", "The effect of the fine was immediate.", "The new rule had no ___ on the queues."),
                ("affect", "affect", "to have an influence on (a verb)", "Rain will affect the turnout.", "A power cut should not ___ the server.")]),
    ("principal", [("principal", "principal", "chief or most important, or the head of a college", "The principal addressed the first-year students.", "The ___ reason for the delay was a missing signature."),
                   ("principle", "principle", "a rule or a basic truth", "He refused on principle.", "The whole scheme rests on one ___ of fairness.")]),
    ("stationary", [("stationary", "stationary", "not moving", "The train stood stationary for an hour.", "The lorry was ___ when the car struck it."),
                    ("stationery", "stationery", "paper, pens and other writing materials", "The office orders stationery once a quarter.", "The clerk indented for ___ for the whole floor.")]),
    ("complement", [("complement", "complement", "something that completes or goes well with another", "The sauce is a complement to the fish.", "The new wing is a ___ to the old building rather than a replacement."),
                    ("compliment", "compliment", "an expression of praise", "She paid him a compliment on his work.", "He meant it as a ___ and she took it as one.")]),
    ("eminent", [("eminent", "eminent", "famous and respected", "An eminent surgeon chaired the panel.", "An ___ historian was asked to write the foreword."),
                 ("imminent", "imminent", "about to happen very soon", "A storm was imminent.", "The clouds warned of an ___ downpour.")]),
    ("continual", [("continual", "continual", "happening again and again with breaks in between", "Continual interruptions spoilt the hour.", "___ power cuts, three or four a day, held up the work."),
                   ("continuous", "continuous", "going on without a break", "A continuous line runs down the middle.", "The machine needs a ___ supply of water, with no interruption at all.")]),
    ("credible", [("credible-cf", "credible", "able to be believed", "The account was detailed and credible.", "The witness gave a ___ account that the court accepted."),
                  ("credulous-cf", "credulous", "too ready to believe things", "A credulous reader believes every headline.", "A ___ buyer accepted every promise without asking for proof.")]),
    ("childish", [("childish", "childish", "silly, like a badly behaved child", "Sulking over it was childish.", "Refusing to speak for a week was simply ___."),
                  ("childlike", "childlike", "innocent and trusting, like a child", "He had a childlike delight in trains.", "Her ___ wonder at the planetarium charmed everyone.")]),
    ("economic", [("economic", "economic", "to do with the economy or with trade", "The economic survey came out in January.", "The budget follows the ___ survey of the whole country."),
                  ("economical", "economical", "careful not to waste money or resources", "A small car is more economical.", "A pressure cooker is the most ___ way to cook dal.")]),
    ("accept", [("accept", "accept", "to agree to receive or to take", "She accepted the award.", "He will ___ the transfer if the allowance is paid."),
                ("except", "except", "not including", "Everyone came except the treasurer.", "The office works on all days ___ the second Saturday.")]),
    ("adapt", [("adapt", "adapt", "to change something so that it suits a new use", "The hall was adapted for a clinic.", "We must ___ the old syllabus to the new pattern."),
               ("adopt", "adopt", "to take up or to take as one's own", "The council adopted the proposal.", "The committee voted to ___ the resolution unchanged.")]),
    ("later", [("later", "later", "at a time after now", "We can talk later.", "The result will be declared a week ___."),
               ("latter", "latter", "the second of two things mentioned", "Of tea and coffee, the latter keeps me awake.", "Of the two options, the ___ costs less but takes longer.")]),
    ("lose", [("lose", "lose", "to be deprived of, or to fail to win", "Do not lose the receipt.", "If you ___ the receipt there is no refund."),
              ("loose", "loose", "not firmly fixed", "A loose screw rattled.", "A ___ wire was found behind the meter.")]),
    ("precede", [("precede", "precede", "to come before", "A short film preceded the feature.", "A written test will ___ the interview."),
                 ("proceed", "proceed", "to go on or carry on", "Please proceed with the reading.", "After the recess the court will ___ with the argument.")]),
    ("respectful", [("respectful", "respectful", "showing respect to others", "He gave a respectful answer.", "The junior clerk sent a ___ reply to the notice."),
                    ("respectable", "respectable", "regarded by others as decent and proper", "A respectable firm with a long record.", "They are a ___ family of small traders.")]),
    ("sensible", [("sensible", "sensible", "showing good judgement", "A sensible decision, given the cost.", "Taking the earlier train was the ___ thing to do."),
                  ("sensitive", "sensitive", "easily affected or easily hurt", "Sensitive skin reacts to the soap.", "The instrument is so ___ that a footstep disturbs it.")]),
    ("historic", [("historic", "historic", "important enough to be remembered in history", "A historic judgment on privacy.", "The treaty was a ___ moment for both countries."),
                  ("historical", "historical", "to do with history or with the past", "Historical records survive from 1820.", "He writes ___ novels set in the Mughal period.")]),
    ("farther", [("farther", "farther", "at a greater physical distance", "The next village is farther than I thought.", "The second gate is ___ down the road."),
                 ("further", "further", "additional, or to a greater extent", "No further questions were asked.", "The committee asked for ___ information before deciding.")]),
    ("council", [("council", "council", "a body of people who meet to decide things", "The municipal council met on Monday.", "The municipal ___ passed the budget."),
                 ("counsel", "counsel", "advice, or a lawyer in a case", "She acted on her father's counsel.", "The accused was represented by senior ___.")]),
    ("desert", [("desert", "desert", "a dry sandy region, or to abandon", "The desert cools sharply at night.", "Camels cross the ___ in the cool of the night."),
                ("dessert", "dessert", "the sweet course at the end of a meal", "Dessert was a slice of melon.", "They served a mango ___ after the rice.")]),
    ("altar", [("altar", "altar", "a raised table used in worship", "Flowers were placed on the altar.", "Candles were lit on the ___ before the prayer."),
               ("alter", "alter", "to change", "The tailor altered the sleeves.", "We may have to ___ the timings of the class.")]),
    ("canvas", [("canvas", "canvas", "a strong coarse cloth, or a surface for painting", "The tent is made of canvas.", "The painter stretched a fresh ___ on the frame."),
                ("canvass", "canvass", "to go round asking for votes or support", "They canvassed the whole ward.", "Volunteers will ___ every street before the poll.")]),
    ("cite", [("cite", "cite", "to quote as an example or an authority", "He cited two earlier rulings.", "The lawyer went on to ___ three earlier judgments."),
              ("site", "site", "a place where something is built or located", "The site was cleared last week.", "Work on the ___ begins after the survey.")]),
    ("wave", [("wave", "wave", "to move the hand to and fro, or a ridge of water", "She waved from the platform.", "He stood at the gate and began to ___ with both hands."),
              ("waive", "waive", "to give up a right or a claim", "The bank waived the penalty.", "The court agreed to ___ the late fee in his case.")]),
    ("weather", [("weather", "weather", "the state of the air and the sky", "The weather turned in the afternoon.", "The ___ in the hills changes within an hour."),
                 ("whether", "whether", "introducing a choice between possibilities", "Ask whether the office is open.", "Nobody could say ___ the office would open on Saturday.")]),
    ("luxurious", [("luxurious", "luxurious", "very comfortable and expensive", "A luxurious waiting room with deep chairs.", "They stayed in a ___ hotel with a pool on the roof."),
                   ("luxuriant", "luxuriant", "growing thickly and strongly", "Luxuriant creepers covered the wall.", "___ grass had covered the whole courtyard.")]),
    ("imply", [("imply", "imply", "to suggest something without saying it outright", "His silence implied consent.", "The notice seemed to ___ that the shop would close."),
               ("infer", "infer", "to work something out from what is said or seen", "From the figures we infer a fall in demand.", "From the empty shelves we may ___ that supply has stopped.")]),
    ("beside", [("beside", "beside", "at the side of", "He sat beside the driver.", "The dog slept ___ the gate all night."),
                ("besides", "besides", "in addition to", "Besides the fee there is a deposit.", "___ the tuition fee, there is a deposit of two thousand rupees.")]),
]

WORDS = [word(i, w, "confused", m[0].upper() + m[1:], ex=e) for g, ws in _SETS for i, w, m, e, cue in ws]
_M = {i: m for g, ws in _SETS for i, w, m, e, cue in ws}
_W = {i: w for g, ws in _SETS for i, w, m, e, cue in ws}
_CUE = {i: cue for g, ws in _SETS for i, w, m, e, cue in ws}
_SET_OF = {i: g for g, ws in _SETS for i, w, m, e, cue in ws}
_BY_WORD = {w: i for g, ws in _SETS for i, w, m, e, cue in ws}
_GROUPS = [g for g, ws in _SETS]
_RARE = {"canvass", "waive", "luxuriant", "credulous", "childlike", "farther", "counsel", "complement", "respectful"}
_RULE = {"advice": "cf-r1", "practice": "cf-r1", "effect": "cf-r1",
         "principal": "cf-r2", "stationary": "cf-r2", "complement": "cf-r2", "desert": "cf-r2", "altar": "cf-r2", "canvas": "cf-r2",
         "cite": "cf-r2", "weather": "cf-r2", "accept": "cf-r2", "later": "cf-r2", "lose": "cf-r2", "council": "cf-r2", "wave": "cf-r2"}
_F = "Select the most appropriate option to fill in the blank.\n"
_S = "Find the part of the sentence that contains an error:\n"


def _lc(m):
    return m[0].lower() + m[1:]


def _gen():
    items, n = [], 0
    for g, ws in _SETS:
        for wid, w, m, e, cue in ws:
            n += 1
            partners = [p[1] for p in ws if p[0] != wid]
            opts = [w] + partners
            pool = [p[1] for g2, ws2 in _SETS if g2 != g for p in [(x[0], x[1]) for x in ws2]]
            j = (n * 7) % len(pool)
            while len(opts) < 4:
                c = pool[j % len(pool)]
                if c not in opts: opts.append(c)
                j += 5
            kpos = n % 4
            rest = [o for o in opts if o != w]; rest.insert(kpos, w)
            wrong = {}
            for ltr, o in zip("abcd", rest):
                if o == w: continue
                mm = _lc(_M[_BY_WORD[o]])
                wrong[ltr] = mistake(f"'{o}' is the word this one is confused with: it means {mm}.") if o in partners else ruled_out(f"'{o}' means {mm}.")
            items.append(q("q-cf-fit", "fill", _F + cue, rest, "abcd"[kpos],
                           f"'{w}' means {_lc(m)}, which is what the sentence needs.", wrong,
                           lex=("fits", wid), uid=f"cf-g{n:03d}", rules=[_RULE.get(g, "cf-r3")],
                           tech=["back-substitute"], rare=w in _RARE))
    return items


def practice_items():
    hand = [
        q("q-cf-spot", "spot-error", _S + "After the long journey / he went upstairs / to lay down for an hour / before dinner.",
          ["After the long journey", "he went upstairs", "to lay down for an hour", "before dinner"], "c",
          "'Lay' needs an object. To rest one's own body is 'to lie down', so it should be 'to lie down for an hour'.",
          {"a": ruled_out("'After the long journey' is a correct phrase of time."),
           "b": ruled_out("'He went upstairs' is a correct main clause."),
           "d": ruled_out("'Before dinner' is a correct phrase of time.")},
          rules=["cf-r4"], uid="cf-p01", tech=["read-whole"]),
        q("q-cf-spot", "spot-error", _S + "The chairman said / that the committee comprises of / nine members, / three of them officials.",
          ["The chairman said", "that the committee comprises of", "nine members,", "three of them officials"], "b",
          "'Comprise' already means 'consist of', so it takes no 'of': the committee comprises nine members.",
          {"a": ruled_out("'The chairman said' is a correct reporting clause."),
           "c": ruled_out("'Nine members' is the object and holds no error."),
           "d": ruled_out("'Three of them officials' is a correct phrase in apposition.")},
          rules=["cf-r4"], uid="cf-p02", tech=["read-whole"]),
        q("q-cf-spot", "spot-error", _S + "The principle of the college / addressed the new students / in the main hall / on Monday morning.",
          ["The principle of the college", "addressed the new students", "in the main hall", "on Monday morning"], "a",
          "The head of a college is the 'principal'; 'principle' is a rule or a basic truth.",
          {"b": ruled_out("'Addressed the new students' is a correct verb with its object."),
           "c": ruled_out("'In the main hall' is a correct phrase of place."),
           "d": ruled_out("'On Monday morning' is a correct phrase of time.")},
          rules=["cf-r2"], uid="cf-p03", tech=["read-whole"]),
        q("q-cf-spot", "spot-error", _S + "The sudden change in the rules / will effect every candidate / who applied / before the first of June.",
          ["The sudden change in the rules", "will effect every candidate", "who applied", "before the first of June"], "b",
          "The verb is 'affect'; 'effect' is the noun for a result. It should be 'will affect every candidate'.",
          {"a": ruled_out("'The sudden change in the rules' is a correctly built subject."),
           "c": ruled_out("'Who applied' is a correct relative clause."),
           "d": ruled_out("'Before the first of June' is a correct phrase of time.")},
          rules=["cf-r1"], uid="cf-p04", tech=["read-whole"]),
    ]
    return hand + _gen()


PYQS = []
