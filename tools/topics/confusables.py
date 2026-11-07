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
    "q-cf-replace": {"short": "Fix or leave it", "label": "Replace the highlighted phrase, or say none is needed", "kind": "qtype", "parent": TOPIC, "order": 3,
                     "summary": "A sentence highlights a phrase built on a confused word; pick the correct replacement, or 'No substitution required' if it is already correct.", "links": []},
    "q-cf-dual": {"short": "Two blanks", "label": "Two blanks filled from the same confused pair", "kind": "qtype", "parent": TOPIC, "order": 4,
                  "summary": "One sentence with two blanks; each option gives both members of a confused pair, in some order, and only one order fits both blanks.", "links": []},
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
    {"id": "cf-r5", "node": "q-cf-replace", "text": "First decide whether the highlighted phrase is already correct; if it is, the answer is 'No substitution required', not the closest-looking candidate. 'Comprise' already means 'consist of' or 'be made up of', so 'comprises of' is always wrong and must lose the 'of'.",
     "ok": "The committee comprises nine members: this already needs no change.", "bad": "Changing an already-correct 'comprises' because the option list offers a near-miss."},
    {"id": "cf-r6", "node": "q-cf-dual", "text": "When two blanks in one sentence are both filled from the same confused pair, work out what each blank needs on its own. The right option gives the correct member of the pair for the first blank AND the correct member for the second, in that order; a pair with the right two words in the wrong order is still wrong.",
     "ok": "The drug did not ___ (affect) her blood pressure, so its ___ (effect) was called negligible.", "bad": "The drug did not ___ (effect) her blood pressure, so its ___ (affect) was called negligible."},
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
    "q-cf-replace": {"cue": "A full sentence with one phrase highlighted, and a fourth option 'No substitution required'.",
                     "standard": "Decide what the highlighted phrase should say, then compare it letter by letter with the sentence's own wording before looking at the options.",
                     "fast": "If the highlighted phrase is already exactly right, stop and pick 'No substitution required'; do not second-guess a correct phrase.",
                     "eliminate": "Drop every option that merely adds a different wrong preposition or form; what remains is either the one correct phrase or 'No substitution required'.",
                     "traps": ["Assuming an error exists just because the question offers correction options.", "'Comprises of' and 'is comprised of', both of which keep an unwanted 'of'."],
                     "rules": ["cf-r5"], "tech": ["read-whole"]},
    "q-cf-dual": {"cue": "One sentence with two blanks, and four options each giving two words from a confused pair in some order.",
                  "standard": "Work out the sense each blank needs on its own first, then find the option that supplies the right word for the first blank and the right word for the second, in that order.",
                  "fast": "Decide the part of speech or sense each blank needs before looking at the options; an option with both words the right way round is the only one that can fit both blanks.",
                  "eliminate": "Drop any option built from the wrong pair of words entirely, then drop the option that has the right pair but the two words swapped.",
                  "traps": ["An option with the right pair of words but in the wrong order for the two blanks.", "An option built from a different, unrelated confused pair altogether."],
                  "rules": ["cf-r6"], "tech": ["back-substitute"]},
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
    ("expect", [("expect", "expect", "to think something is likely to happen", "I expect the result by Friday.", "She did not ___ the exam to be postponed."),
                ("suspect", "suspect", "to believe something is true, often something bad, without full proof", "He suspected a trick.", "The guard began to ___ that the parcel was fake.")]),
    ("allude", [("allude", "allude", "to refer to something indirectly, without naming it", "He alluded to an earlier scandal.", "In his speech the minister ___d to an old controversy without naming anyone."),
                ("elude", "elude", "to escape or avoid someone or something skilfully", "The thief eluded the police for a week.", "The suspect managed to ___ capture for three days.")]),
    ("alternate", [("alternate", "alternate", "happening in turns, one after the other", "He works on alternate days.", "The clerk is on duty on ___ Saturdays."),
                   ("alternative", "alternative", "a different option one could choose instead", "There is no alternative to hard work.", "If the train is cancelled, we will need an ___ plan.")]),
    ("access", [("access", "access", "a way of reaching or entering a place or a system", "She has access to the file.", "Only the manager has ___ to the strong room."),
                ("excess", "excess", "an amount that is more than is needed or allowed", "He was fined for the excess baggage.", "Passengers must pay extra for any ___ baggage over 15 kg.")]),
    ("averse", [("averse", "averse", "unwilling or opposed to doing something", "He is averse to taking risks.", "She has always been ___ to borrowing money."),
                ("adverse", "adverse", "unfavourable, or having a harmful effect", "The adverse weather delayed the flight.", "The new tax had an ___ effect on small traders.")]),
    ("amend", [("amend", "amend", "to make small changes to a document or law in order to improve it", "Parliament amended the Act.", "The committee decided to ___ the outdated bylaw."),
               ("emend", "emend", "to correct the errors in a piece of writing", "The editor emended the manuscript.", "The proofreader was asked to ___ the printer's mistakes before the second edition.")]),
    ("ensure", [("ensure", "ensure", "to make certain that something happens", "Please ensure the gate is locked.", "It is the guard's job to ___ that no one enters after ten."),
                ("insure", "insure", "to pay a company so it covers a loss if something bad happens", "He insured his car against theft.", "She decided to ___ the shop against fire and flood."),
                ("assure", "assure", "to tell someone confidently that something is true, so as to remove their doubt", "He assured her of his full support.", "The doctor tried to ___ the family that the operation had gone well.")]),
    ("especially", [("especially", "especially", "above all, particularly", "He loves fruit, especially mangoes.", "The city gets crowded, ___ during the festival season."),
                    ("specially", "specially", "for one particular purpose, specifically", "The cake was specially made for her birthday.", "This hall was ___ built for the annual function and nothing else.")]),
    ("excite", [("excite", "excite", "to cause strong, usually pleasant, feelings in someone", "The news excited the whole class.", "The announcement of a holiday ___d the students at once."),
                ("incite", "incite", "to stir up anger or violence in people", "The speech incited the crowd to riot.", "The pamphlet was accused of trying to ___ unrest among the factory workers.")]),
    ("human", [("human", "human", "relating to people in general", "Human error caused the delay.", "Investigators traced the accident to ___ error, not a machine fault."),
               ("humane", "humane", "kind and showing compassion, especially towards suffering", "They sought a humane solution.", "The new rules call for more ___ treatment of undertrial prisoners.")]),
    ("invent", [("invent", "invent", "to create something that did not exist before", "He invented a new machine.", "The young engineer ___ed a cheap water filter for villages."),
                ("discover", "discover", "to find something that already existed but was unknown until now", "She discovered a new species.", "The team ___ed a sealed chamber hidden inside the old temple.")]),
    ("illegal", [("illegal", "illegal", "against the law", "Smuggling is illegal.", "Parking a vehicle here without a permit is ___."),
                 ("illicit-cf", "illicit", "not approved of by society, often carried on secretly", "They had an illicit affair.", "The raid uncovered an ___ trade in forged certificates.")]),
    ("envelop", [("envelop-v", "envelop", "to cover or surround something completely (a verb)", "Fog enveloped the valley by evening.", "Thick black smoke began to ___ the entire warehouse."),
                 ("envelope-n", "envelope", "a flat paper covering used to post a letter (a noun)", "He sealed the envelope and posted it.", "She slipped the admit card into a brown ___.")]),
    ("gate", [("gate", "gate", "a hinged barrier set in a wall or fence at an entrance", "Close the gate behind you.", "The watchman locked the main ___ sharply at nine."),
              ("gait", "gait", "a person's particular manner or style of walking", "He walks with an unusual gait.", "Years of training gave the dancer a remarkably graceful ___.")]),
    ("hear", [("hear", "hear", "to become aware of a sound through the ears", "I can hear the rain outside.", "Did you ___ the announcement that was just made?"),
              ("listen", "listen", "to pay deliberate, close attention to a sound", "Listen to the teacher carefully.", "You must ___ to the full instructions before you start the test.")]),
    ("flair", [("flair", "flair", "a natural talent or stylish ability for doing something", "She has a flair for languages.", "The young chef showed a genuine ___ for presentation."),
               ("flare", "flare", "a sudden burst of light, flame, or temper", "Tempers began to flare at the meeting.", "A sudden ___ of anger spoiled what had been a calm discussion.")]),
    ("deny", [("deny", "deny", "to say firmly that something is not true", "He will deny the allegation at once.", "The minister ___ied any personal involvement in the scam."),
              ("refute", "refute", "to prove, usually with evidence, that a claim or theory is wrong", "She refuted his claims with hard data.", "The scientist ___d the old theory by presenting fresh evidence.")]),
    ("defy", [("defy", "defy", "to openly resist or refuse to obey a rule or order", "He dared to defy the curfew order.", "The workers ___ied the ban and continued their strike."),
              ("deify", "deify", "to treat or worship someone as if they were a god", "Fans deify the actor.", "In some villages, the memory of the old king is still ___ied.")]),
    ("disinterested", [("disinterested", "disinterested", "impartial, having no personal stake in the outcome", "A disinterested judge is essential for fairness.", "We need a genuinely ___ observer to referee the final match."),
                        ("uninterested", "uninterested", "not interested in something, bored by it", "He was uninterested in the lecture.", "The children looked completely ___ throughout the long speech.")]),
    ("contagious", [("contagious", "contagious", "a disease that spreads mainly by direct physical touch", "Chickenpox is contagious.", "The doctor said the rash was ___ and advised the child be kept home."),
                    ("infectious", "infectious", "a disease that spreads more widely, through air, water or germs in general", "Malaria is an infectious disease.", "Cholera is an ___ disease spread mainly through contaminated water.")]),
]

WORDS = [word(i, w, "confused", m[0].upper() + m[1:], ex=e) for g, ws in _SETS for i, w, m, e, cue in ws]
_M = {i: m for g, ws in _SETS for i, w, m, e, cue in ws}
_W = {i: w for g, ws in _SETS for i, w, m, e, cue in ws}
_CUE = {i: cue for g, ws in _SETS for i, w, m, e, cue in ws}
_SET_OF = {i: g for g, ws in _SETS for i, w, m, e, cue in ws}
_BY_WORD = {w: i for g, ws in _SETS for i, w, m, e, cue in ws}
_GROUPS = [g for g, ws in _SETS]
_RARE = {"canvass", "waive", "luxuriant", "credulous", "childlike", "farther", "counsel", "complement", "respectful",
         "emend", "allude", "elude", "deify", "disinterested", "gait", "contagious", "infectious"}
_RULE = {"advice": "cf-r1", "practice": "cf-r1", "effect": "cf-r1", "envelop": "cf-r1",
         "principal": "cf-r2", "stationary": "cf-r2", "complement": "cf-r2", "desert": "cf-r2", "altar": "cf-r2", "canvas": "cf-r2",
         "cite": "cf-r2", "weather": "cf-r2", "accept": "cf-r2", "later": "cf-r2", "lose": "cf-r2", "council": "cf-r2", "wave": "cf-r2",
         "access": "cf-r2", "gate": "cf-r2", "flair": "cf-r2", "defy": "cf-r2"}
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
    rep = [
        q("q-cf-replace", "improve", "Select the most appropriate option that can substitute the highlighted segment in the given sentence. If there is no need to substitute it, select 'No substitution required'.\n"
          "The warden announced that the hostel [[comprises of]] four wings and a common dining hall, so new students should note their wing number.",
          ["comprises", "is comprised of", "comprising of", "No substitution required"], "a",
          "'Comprise' already means 'consist of', so it takes no 'of'; the highlighted phrase must lose the 'of' and become 'comprises'.",
          {"b": mistake("'Is comprised of' is a common way to try to fix the error, but 'comprise' is active in sense and does not need the passive 'is ... of' either."),
           "c": mistake("'Comprising of' keeps the same unwanted 'of' in a different form."),
           "d": mistake("This says no change is needed, but 'comprises of' is wrong; the 'of' must be dropped.")},
          rules=["cf-r5"], uid="cf-p05"),
        q("q-cf-replace", "improve", "Select the most appropriate option that can substitute the highlighted segment in the given sentence. If there is no need to substitute it, select 'No substitution required'.\n"
          "The final report confirms that the committee [[comprises]] seven elected members and two co-opted advisers.",
          ["comprises of", "is comprised", "comprise", "No substitution required"], "d",
          "The sentence already reads 'comprises' with no 'of', which is the correct form, so no substitution is required.",
          {"a": ruled_out("'Comprises of' adds the unwanted 'of' that the sentence's own correct wording does not have."),
           "b": ruled_out("'Is comprised' drops the object entirely and reads as incomplete."),
           "c": mistake("'Comprise' (with no 's') does not agree with the singular subject 'the committee'.")},
          rules=["cf-r5"], uid="cf-p06"),
    ]
    dual = [
        q("q-cf-dual", "fill", _F + "I will not ___ you on something I know nothing about, but my honest ___ is always to ask an expert first.",
          ["advice, advise", "advise, advice", "practice, practise", "practise, practice"], "b",
          "The first blank needs the verb 'advise' (to offer guidance); the second needs the noun 'advice' (guidance given). So the pair is 'advise, advice', in that order.",
          {"a": mistake("This has the right pair of words but in the wrong order: the first blank needs the verb 'advise', not the noun 'advice'."),
           "c": ruled_out("'Practice' (repeated doing) and 'practise' (to do repeatedly) are a different confused pair and do not fit a sentence about giving guidance."),
           "d": ruled_out("This is the same unrelated practice/practise pair as (c), only reordered, and still does not fit a sentence about giving guidance.")},
          rules=["cf-r1", "cf-r6"], uid="cf-p07", tech=["back-substitute"]),
        q("q-cf-dual", "fill", _F + "The tailor said the scarf would ___ my coat perfectly, and I took it as a nice ___ on my choice of colours.",
          ["complement, compliment", "compliment, complement", "principal, principle", "principle, principal"], "a",
          "The first blank needs 'complement' (to go well with); the second needs 'compliment' (an expression of praise). So the pair is 'complement, compliment', in that order.",
          {"b": mistake("This has the right pair but in the wrong order: the first blank needs 'complement' (to go well with), not 'compliment' (praise)."),
           "c": ruled_out("'Principal' (chief, or head of a college) and 'principle' (a rule) are a different confused pair and do not fit a sentence about matching colours and praise."),
           "d": ruled_out("This is the same unrelated principal/principle pair as (c), only reordered, and still does not fit this sentence.")},
          rules=["cf-r2", "cf-r6"], uid="cf-p08", tech=["back-substitute"]),
    ]
    return hand + _gen() + rep + dual


PYQS = [
    q("q-cf-replace", "improve", "Select the most appropriate option that can substitute the highlighted segment in the given sentence. If there is no need to substitute it, select 'No substitution required'.\n"
      "During the briefing on the new city-bus timetable, the conductor explained that the route [[comprises of]] three major interchanges and two feeder loops, so commuters should keep extra time for transfers.",
      ["comprises", "is comprised of", "comprising of", "No substitution required"], "a",
      "'Comprise' already means 'consist of' or 'be made up of', so it takes no 'of'; the highlighted 'comprises of' must become plain 'comprises'.",
      {"b": mistake("'Is comprised of' turns 'comprise' passive and keeps an 'of' it does not need; the active 'comprises' is the correct fix."),
       "c": mistake("'Comprising of' keeps the same unwanted 'of' in a different grammatical form."),
       "d": mistake("This says no change is needed, but 'comprises of' is a standard error; the 'of' must be dropped.")},
      rules=["cf-r5"], paper="2026-10-09", qno=76, rare=True),
    q("q-cf-dual", "fill", _F + "The new medication did not ___ the patient's symptoms as expected, so the doctor questioned its overall ___.",
      ["alter, altar", "altar, alter", "effect, affect", "affect, effect"], "d",
      "The first blank needs a verb for 'to influence': 'affect'. The second needs a noun for 'a result': 'effect'. So the pair reads 'affect, effect', in that order.",
      {"a": ruled_out("'Alter' (to change) and 'altar' (a table used in worship) are an unrelated pair; neither word concerns a medication's influence or its result."),
       "b": ruled_out("This is the same unrelated alter/altar pair as (a), only reordered, and still has nothing to do with a medication's influence or result."),
       "c": mistake("This has the right pair of words but in the wrong order: the first blank needs the verb 'affect', and the second needs the noun 'effect', not the reverse.")},
      rules=["cf-r1", "cf-r6"], paper="2026-10-10", qno=83, tech=["back-substitute"],
      trick="Blank 1 is a verb (affect); blank 2 is a noun after 'overall' (effect)."),
]
