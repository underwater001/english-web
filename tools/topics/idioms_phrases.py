"""Idioms & phrases: 3 past questions, 8 original practice items and one generated question per idiom.
Each answer is checked against the idiom's stored meaning in WORDS; distractors are the meanings of idioms from other
groups, so no wrong option can also be right. Meanings and example sentences are written fresh."""
from bank import mistake, ruled_out, q, word

TOPIC = "idioms-phrases"
TIER = "full"
PREFIX = "id"

NODES = {
    "q-idiom-meaning": {"short": "Meaning", "label": "Meaning of an idiom", "kind": "qtype", "parent": TOPIC, "order": 1,
                        "summary": "An idiom in inverted commas; pick the option that gives its meaning.", "links": []},
    "q-idiom-identify": {"short": "Identify idiom", "label": "Pick the idiom that has this meaning", "kind": "qtype", "parent": TOPIC, "order": 2,
                        "summary": "A meaning is spelled out in full; pick the idiom (from four real idioms) that actually means that.", "links": []},
    "q-idiom-correct": {"short": "Correct idiom", "label": "Restore a garbled idiom", "kind": "qtype", "parent": TOPIC, "order": 3,
                        "summary": "A highlighted idiom has been reordered or had a word swapped; pick the option that restores its fixed wording.", "links": []},
}

RULES = [
    {"id": "id-r1", "node": "q-idiom-meaning", "text": "An idiom means something different from its words put together. Never choose the option that restates the literal picture.",
     "ok": "Spill the beans = reveal a secret.", "bad": "Spill the beans = drop some beans."},
    {"id": "id-r2", "node": "q-idiom-meaning", "text": "Idioms cluster by feeling: trouble, anger, secrecy, ease, effort, luck, haste. Decide the feeling from the sentence, then match the option with that feeling.",
     "ok": "'in hot water' and 'on thin ice' both say trouble or risk.", "bad": "Choosing an effort meaning for 'in hot water'."},
    {"id": "id-r3", "node": "q-idiom-identify", "text": "When the meaning is given and the idiom itself is the answer, the three wrong options are usually other real idioms, often built from the same image or word (bell, blood, water). Match the feeling of the given meaning first, then confirm by recalling the exact idiom; do not pick an option merely because it shares a word with the meaning.",
     "ok": "Meaning 'eagerly, with enthusiasm' -> 'with bells on'.", "bad": "Picking 'sound as a bell' because it also contains 'bell'."},
    {"id": "id-r4", "node": "q-idiom-correct", "text": "Some idioms pair two images in a fixed order (hare/hounds, cart/horse, pot/kettle). The exam may swap that order, or replace one half with a word from a different idiom. Recall the idiom as one fixed phrase, not word by word, and restore its exact order rather than checking only that the right words appear somewhere.",
     "ok": "'run with the hare and hunt with the hounds' keeps 'run' with 'hare' and 'hunt' with 'hounds'.", "bad": "'run with the hounds and hunt with the hare' swaps the two pairings and is not a real idiom."},
]

METHODS = {
    "q-idiom-meaning": {
        "cue": "'Select the most appropriate meaning of the idiom/phrase' with the idiom in inverted commas. Four to five per paper in total; three appeared in the three 12 Sep 2025 papers.",
        "standard": "Recall the meaning as a unit, then match it. If you do not know it, work out the feeling the idiom carries (good, bad, secret, effort, anger) from the sentence it came from.",
        "fast": "Drop any option that is the literal reading, then match the remaining ones by feeling.",
        "eliminate": "Other idioms' meanings are usually the wrong options; if you recognise one of them as belonging to a different idiom, cross it out.",
        "traps": ["The literal meaning is nearly always listed as bait.", "The meaning of a similar-sounding idiom is the second common trap.",
                  "Do not pick an option only because it contains a word from the idiom."],
        "rules": ["id-r1", "id-r2"], "tech": ["literal-trap"]},
    "q-idiom-identify": {
        "cue": "The full meaning is spelled out in a sentence; the four options are themselves idioms, and you must name the one that carries that meaning.",
        "standard": "Decide the feeling the given meaning carries (eager, secretive, angry, lucky), then pick the one option among the four idioms that matches that feeling exactly.",
        "fast": "Recall the idiom as a fixed phrase first; do not reason from the individual words of the options.",
        "eliminate": "Drop any option idiom whose stored meaning you know is different, even if it shares a word (bell, blood) with the given meaning.",
        "traps": ["An option that shares a word with the meaning but is a different idiom entirely.", "Two idioms built on the same image (bell, water, moon) tested against each other."],
        "rules": ["id-r3"], "tech": ["literal-trap"]},
    "q-idiom-correct": {
        "cue": "A sentence with a highlighted idiom that has been garbled — its two halves reordered, or one word swapped for a wrong one; pick the option that restores the correct idiom, or 'No improvement required' if it is already correct.",
        "standard": "Recall the idiom as one whole fixed phrase. Check which word is paired with which half, and whether any word has been swapped in from a different idiom.",
        "fast": "If the highlighted phrase sounds almost right but 'off', the two halves have likely been swapped; try reversing just the two key words first.",
        "eliminate": "Drop any option that changes only one word to another wrong word, or that keeps the swapped order.",
        "traps": ["Swapping the two halves of a paired idiom.", "Replacing one half with a word from a different, similarly-themed idiom.", "Choosing 'No improvement required' when the idiom is in fact garbled."],
        "rules": ["id-r4"], "tech": ["literal-trap"]},
}

REFS = []

# (id, idiom, meaning, own example sentence, group, extra accepted wording)
_I = [
    ("blessing-in-disguise", "a blessing in disguise", "A misfortune that turns out to be beneficial.", "Losing that job was a blessing in disguise, because it pushed her to start her own firm.", "luck", ()),
    ("bite-the-bullet", "bite the bullet", "To face a painful or difficult situation with courage.", "We will have to bite the bullet and cut the budget this year.", "brave", ()),
    ("break-the-ice", "break the ice", "To ease the awkwardness among people meeting for the first time.", "A quick joke helped him break the ice at the meeting.", "start", ()),
    ("once-in-a-blue-moon", "once in a blue moon", "Very rarely.", "He visits his village once in a blue moon.", "rare", ()),
    ("spill-the-beans", "spill the beans", "To reveal a secret.", "Someone spilled the beans about the surprise party.", "secret", ()),
    ("hit-the-nail-on-the-head", "hit the nail on the head", "To state exactly what is true or right.", "You hit the nail on the head when you said the plan lacked money.", "right", ()),
    ("burn-the-midnight-oil", "burn the midnight oil", "To work or study late into the night.", "She burnt the midnight oil before the exam.", "effort", ()),
    ("cost-an-arm-and-a-leg", "cost an arm and a leg", "To be extremely expensive.", "The repair cost an arm and a leg.", "costly", ()),
    ("piece-of-cake", "a piece of cake", "Something very easy to do.", "After weeks of practice, the driving test was a piece of cake.", "ease", ()),
    ("beat-around-the-bush", "beat around the bush", "To avoid coming to the main point.", "Stop beating around the bush and tell us the price.", "avoid", ()),
    ("cry-over-spilt-milk", "cry over spilt milk", "To be upset about a loss that cannot be undone.", "The match is lost, so there is no use crying over spilt milk.", "regret", ()),
    ("count-chickens", "count one's chickens before they hatch", "To rely on a result that has not yet happened.", "Do not count your chickens before they hatch; the offer is not yet signed.", "early", ()),
    ("silver-lining", "every cloud has a silver lining", "There is something good in every bad situation.", "He lost the race but found a coach; every cloud has a silver lining.", "luck", ()),
    ("under-the-weather", "under the weather", "Feeling slightly unwell.", "I stayed home because I was feeling under the weather.", "ill", ()),
    ("get-out-of-hand", "get out of hand", "To become impossible to control.", "The crowd could get out of hand if the gates are shut.", "control", ()),
    ("heat-of-the-moment", "in the heat of the moment", "While overcome by strong feeling and without thinking.", "In the heat of the moment, she said things she later regretted.", "emotion", ()),
    ("jump-on-the-bandwagon", "jump on the bandwagon", "To join an activity because it has become popular.", "Soon every shop jumped on the bandwagon and sold the new drink.", "trend", ()),
    ("keep-at-bay", "keep at bay", "To keep something dangerous or unwelcome away.", "Vaccines keep many diseases at bay.", "away", ()),
    ("lose-ones-touch", "lose one's touch", "To lose a skill one once had.", "A striker can lose his touch in front of goal after a long injury.", "skill", ()),
    ("make-a-long-story-short", "make a long story short", "To tell only the main point, briefly.", "To make a long story short, we missed the train.", "brief", ()),
    ("no-pain-no-gain", "no pain, no gain", "Nothing worthwhile is achieved without effort.", "Wake up and run; no pain, no gain.", "effort", ()),
    ("out-of-the-blue", "out of the blue", "Suddenly and unexpectedly.", "A letter from her old teacher arrived out of the blue.", "surprise", ()),
    ("put-on-ice", "put on ice", "To postpone something for later.", "The project was put on ice until funds arrived.", "delay", ()),
    ("queer-the-pitch", "queer the pitch", "To spoil someone's plans or chances.", "His late arrival queered the pitch for the whole team.", "spoil", ()),
    ("rain-on-someones-parade", "rain on someone's parade", "To spoil someone's pleasure or plans.", "I hate to rain on your parade, but the show is cancelled.", "spoil", ()),
    ("grain-of-salt", "take with a grain of salt", "To doubt something and not accept it fully.", "Take rumours about the exam with a grain of salt.", "doubt", ()),
    ("up-in-arms", "up in arms", "Protesting angrily.", "Residents were up in arms over the new tax.", "angry", ()),
    ("vanish-into-thin-air", "vanish into thin air", "To disappear completely.", "The thief seemed to vanish into thin air.", "vanish", ()),
    ("heart-on-sleeve", "wear one's heart on one's sleeve", "To show one's feelings openly.", "She wears her heart on her sleeve, so you always know her mood.", "emotion2", ()),
    ("book-by-its-cover", "judge a book by its cover", "To judge something by its looks alone.", "He looks stern, but never judge a book by its cover.", "looks", ()),
    ("zero-in-on", "zero in on", "To focus attention closely on something.", "The inspector zeroed in on the missing receipt.", "focus", ()),
    ("break-a-leg", "break a leg", "Good luck, said to a performer.", "Break a leg tonight, said the director.", "wish", ()),
    ("cool-as-a-cucumber", "cool as a cucumber", "Very calm and composed.", "The pilot stayed cool as a cucumber during the storm.", "calm", ()),
    ("down-in-the-dumps", "down in the dumps", "Feeling sad or depressed.", "He has been down in the dumps since he lost his job.", "sad", ()),
    ("elephant-in-the-room", "the elephant in the room", "A serious problem that everyone avoids talking about.", "Nobody mentioned the loss; it was the elephant in the room.", "avoid2", ()),
    ("fit-as-a-fiddle", "fit as a fiddle", "In very good health.", "After a month of walking, he is as fit as a fiddle.", "healthy", ()),
    ("go-the-extra-mile", "go the extra mile", "To make more effort than is expected.", "She goes the extra mile for every customer.", "effort", ()),
    ("hit-the-books", "hit the books", "To start studying seriously.", "Exams begin next week, so it is time to hit the books.", "effort", ()),
    ("in-a-pickle", "in a pickle", "In a difficult situation.", "He is in a pickle: the tickets are booked but the leave is refused.", "trouble", ()),
    ("just-what-the-doctor-ordered", "just what the doctor ordered", "Exactly what was needed.", "A cool drink was just what the doctor ordered.", "needed", ()),
    ("kick-the-bucket", "kick the bucket", "To die.", "The old tractor finally kicked the bucket.", "death", ()),
    ("let-the-cat-out", "let the cat out of the bag", "To reveal a secret by mistake.", "He let the cat out of the bag about the gift.", "secret", ()),
    ("miss-the-boat", "miss the boat", "To lose an opportunity.", "Apply today or you will miss the boat.", "chance", ()),
    ("full-deck", "not playing with a full deck", "Not very sensible or intelligent.", "Selling your house for a bicycle? You are not playing with a full deck.", "foolish", ()),
    ("eggs-in-one-basket", "put all one's eggs in one basket", "To risk everything on a single plan.", "Spread your savings; do not put all your eggs in one basket.", "risk", ()),
    ("quiet-as-a-mouse", "quiet as a mouse", "Very quiet.", "The children were quiet as mice during the film.", "quiet", ()),
    ("rule-of-thumb", "rule of thumb", "A rough guide based on experience, not exact.", "As a rule of thumb, add an hour to any travel estimate.", "guide", ()),
    ("smell-a-rat", "smell a rat", "To suspect that something is wrong or dishonest.", "When an offer is too good, I tend to smell a rat.", "suspect", ()),
    ("variety-spice", "variety is the spice of life", "New and different experiences make life enjoyable.", "She tries a new hobby every month; variety is the spice of life.", "variety", ()),
    ("when-pigs-fly", "when pigs fly", "Something that will never happen.", "He will repay the loan when pigs fly.", "never", ()),
    ("omelette-eggs", "cannot make an omelette without breaking eggs", "Nothing great is achieved without some damage or sacrifice.", "Closing the old plant hurts, but you cannot make an omelette without breaking eggs.", "sacrifice", ()),
    ("zip-your-lip", "zip one's lip", "To stay quiet.", "Zip your lip; the baby has just fallen asleep.", "quiet", ()),
    ("barking-up-wrong-tree", "bark up the wrong tree", "To make a mistake about whom or what to blame or pursue.", "If you suspect the cook, you are barking up the wrong tree.", "mistaken", ()),
    ("cry-wolf", "cry wolf", "To raise a false alarm.", "If you cry wolf too often, nobody comes when the fire is real.", "false", ()),
    ("devils-advocate", "play devil's advocate", "To argue against an idea only to test it.", "Let me play devil's advocate and ask who will pay for it.", "argue", ()),
    ("easy-as-pie", "easy as pie", "Very easy.", "The new software is easy as pie to install.", "ease", ()),
    ("fish-out-of-water", "a fish out of water", "A person in surroundings where they feel uncomfortable.", "In the boardroom he felt like a fish out of water.", "uncomfortable", ()),
    ("hit-the-ground-running", "hit the ground running", "To start something quickly and with energy.", "The new manager hit the ground running on her first day.", "quickstart", ()),
    ("ignorance-is-bliss", "ignorance is bliss", "Not knowing about a problem keeps one happy.", "I never read the reviews; ignorance is bliss.", "bliss", ()),
    ("jack-of-all-trades", "a jack of all trades", "A person who can do many different jobs.", "Our caretaker is a jack of all trades: he fixes pipes, wiring and roofs.", "versatile", ()),
    ("master-of-none", "jack of all trades, master of none", "Someone who knows a little of many things but is expert in none.", "He tries every sport but, a jack of all trades, he is master of none.", "shallow", ()),
    ("chin-up", "keep one's chin up", "To stay cheerful in hard times.", "Keep your chin up; the results come out tomorrow.", "cheer", ()),
    ("leave-no-stone-unturned", "leave no stone unturned", "To make every possible effort to achieve a goal.", "Detectives promised to leave no stone unturned in searching for the missing file.", "effort", ("To make every possible effort to achieve a goal",)),
    ("monkey-business", "monkey business", "Silly, mischievous or dishonest behaviour.", "Enough monkey business; open your books.", "mischief", ()),
    ("nip-in-the-bud", "nip in the bud", "To stop a problem at an early stage.", "The principal nipped the quarrel in the bud.", "early", ()),
    ("cloud-nine", "on cloud nine", "Extremely happy.", "She was on cloud nine after the result.", "happy", ()),
    ("play-it-by-ear", "play it by ear", "To decide what to do as events unfold, without a plan.", "We have no fixed plan, so we will play it by ear.", "improvise", ()),
    ("quick-as-a-flash", "quick as a flash", "Extremely fast.", "He ducked quick as a flash.", "speed", ()),
    ("rome-built", "Rome was not built in a day", "Great things take time and patience.", "Be patient with your progress; Rome was not built in a day.", "patience", ()),
    ("shake-a-leg", "shake a leg", "To hurry up.", "Shake a leg or we will miss the bus.", "speed", ()),
    ("own-medicine", "a taste of one's own medicine", "Being treated the way one has treated others.", "The bully got a taste of his own medicine.", "payback", ()),
    ("up-for-grabs", "up for grabs", "Available for anyone to take or win.", "Two seats are still up for grabs.", "available", ()),
    ("whole-nine-yards", "the whole nine yards", "Everything; the full extent of something.", "She planned the wedding with the whole nine yards: band, fireworks and feast.", "everything", ()),
    ("scratch-my-back", "you scratch my back and I will scratch yours", "Help each other by exchanging favours.", "Share your notes and I will share mine; you scratch my back, I scratch yours.", "mutual", ()),
    ("bird-in-the-hand", "a bird in the hand is worth two in the bush", "A sure thing now is better than a bigger chance later.", "Take the job on offer; a bird in the hand is worth two in the bush.", "certain", ()),
    ("drawing-board", "back to the drawing board", "To start planning again after a failure.", "The design failed the test, so it is back to the drawing board.", "restart", ()),
    ("rock-hard-place", "between a rock and a hard place", "Facing two equally unpleasant choices.", "Pay the fine or lose the licence: she was between a rock and a hard place.", "dilemma", ()),
    ("diamond-in-the-rough", "a diamond in the rough", "A person with great talent who is not yet polished.", "The village boy was a diamond in the rough and soon became a champion.", "potential", ()),
    ("early-bird", "the early bird catches the worm", "Those who act early gain the advantage.", "Reach the counter at six; the early bird catches the worm.", "early2", ()),
    ("face-the-music", "face the music", "To accept the consequences of one's actions.", "He broke the window and had to face the music.", "consequence", ()),
    ("rabbit-hole", "go down the rabbit hole", "To get absorbed in a deep and confusing subject.", "Look up one word and you may go down the rabbit hole for hours.", "deep", ()),
    ("haste-makes-waste", "haste makes waste", "Doing things in a hurry leads to mistakes.", "Check your answers; haste makes waste.", "haste", ()),
    ("hot-water", "in hot water", "In trouble.", "The clerk is in hot water for losing the files.", "trouble", ()),
    ("fingers-crossed", "keep one's fingers crossed", "To hope for good luck.", "Keep your fingers crossed for my interview.", "wish", ()),
    ("sleeping-dogs", "let sleeping dogs lie", "To avoid stirring up old trouble.", "The matter is closed; let sleeping dogs lie.", "leave", ()),
    ("make-hay", "make hay while the sun shines", "To use an opportunity while it lasts.", "Sell now while prices are high; make hay while the sun shines.", "chance", ()),
    ("not-a-hair-out-of-place", "not a hair out of place", "Perfectly neat and tidy.", "After the long flight, he arrived with not a hair out of place.", "neat", ()),
    ("on-thin-ice", "on thin ice", "In a risky position where things could go wrong.", "After two warnings, he is on thin ice with his manager.", "trouble", ()),
    ("penny-for-your-thoughts", "a penny for your thoughts", "A way of asking what someone is thinking.", "You look lost in thought; a penny for your thoughts?", "ask", ()),
    ("quick-on-the-draw", "quick on the draw", "Quick to react or reply.", "The anchor is quick on the draw with a witty reply.", "speed", ()),
    ("rain-or-shine", "rain or shine", "In any weather; whatever happens.", "The parade will go ahead, rain or shine.", "regardless", ()),
    ("see-eye-to-eye", "see eye to eye", "To agree completely.", "The two partners rarely see eye to eye on money.", "agree", ()),
    ("up-a-creek", "up the creek without a paddle", "In a difficult situation with no way out.", "With the engine dead and no phone signal, we were up the creek without a paddle.", "trouble", ()),
    ("when-in-rome", "when in Rome, do as the Romans do", "Follow the customs of the place you are in.", "Eat with your hands here: when in Rome, do as the Romans do.", "adapt", ()),
    ("year-in-year-out", "year in, year out", "Every year, without a break.", "He has won the prize year in, year out.", "regular", ()),
    ("sixes-and-sevens", "at sixes and sevens", "In a state of confusion or disorder.", "With the manager away, the office was at sixes and sevens.", "confusion", ("In complete confusion",)),
    ("blow-a-fuse", "blow a fuse", "To lose one's temper suddenly.", "Dad will blow a fuse when he sees the broken window.", "angry", ("To become suddenly angry",)),
    ("shoulder-responsibility", "shoulder the responsibility", "To accept a duty or blame as one's own.", "The captain shouldered the responsibility for the defeat.", "duty", ()),
    ("cross-purposes", "at cross purposes", "Misunderstanding each other's aims.", "We talked at cross purposes because I meant the museum and he meant the market.", "misunderstand", ()),
    ("lose-heart", "lose heart", "To lose hope or confidence.", "Do not lose heart after one failure.", "discourage", ()),
    ("chip-on-shoulder", "have a chip on one's shoulder", "To feel angry or resentful about a past wrong.", "Do not have a chip on your shoulder about being passed over.", "resent", ()),
    ("give-one-the-slip", "give one the slip", "To escape from someone, often by a trick.", "He managed to give his pursuers the slip near the station.", "escape", ("to escape from someone",)),
    ("red-letter-day", "a red letter day", "A memorable day because of some pleasant or important event.", "Her graduation was a red letter day for the whole family.", "memorable", ("memorable day",)),
    ("up-to-the-minute", "up to the minute", "To be as current or up to date as possible.", "The live blog keeps its headlines up to the minute.", "current", ("to be as current as is possible",)),
    ("with-bells-on", "with bells on", "Eagerly, with great enthusiasm, or ready to enjoy oneself.", "Tell them I will be there with bells on.", "eager", ()),
    ("work-the-system", "work the system", "To take advantage of a set of rules, procedures, or structures to achieve a personal or institutional goal, often in a way that is clever, slightly dishonest, or exploits loopholes.",
     "The contractor worked the system to win every tender without ever technically breaking a rule.", "exploit", ()),
    ("bang-for-buck", "bang for your buck", "Greater value for the amount of money one is spending.", "Buying the family-size pack gives you a much bigger bang for your buck.", "value", ()),
    ("hoist-with-own-petard", "hoist with one's own petard", "To be harmed or ruined by the very scheme or trap one devised against someone else.",
     "The con artist was hoist with his own petard when his forged contract was used as evidence against him.", "backfire",
     ("To be harmed or ruined by the very scheme one devised against another",)),
    ("horses-mouth", "straight from the horse's mouth", "Directly from the original or most reliable source.",
     "I didn't believe the rumour until I heard it straight from the horse's mouth.", "source", ("From a reliable source",)),
    ("run-with-hare-hunt-hounds", "run with the hare and hunt with the hounds", "To try to support or please both sides of a dispute at once, often by misleading each about the other.",
     "The negotiator was accused of running with the hare and hunting with the hounds, promising concessions to the strikers while privately assuring management nothing would change.", "twoface", ()),
    ("squeaky-wheel-grease", "the squeaky wheel gets the grease", "The most noticeable problem, or the loudest complaint, is the one that receives attention and is addressed first.",
     "After weeks of quiet waiting produced nothing, she learned that the squeaky wheel gets the grease and started emailing the manager every day.", "complain", ()),
    ("cart-before-horse", "put the cart before the horse", "To do things in the wrong order, reversing a cause and what should follow from it.",
     "Announcing the sequel before the first film's script was even finished, the studio put the cart before the horse.", "order", ()),
    ("pot-calling-kettle-black", "the pot calling the kettle black", "Accusing someone of a fault that one has oneself.",
     "Criticising him for arriving late is the pot calling the kettle black, since she is never on time either.", "hypocrite", ()),
    ("rob-peter-pay-paul", "rob Peter to pay Paul", "To solve one debt or problem by creating another, taking from one place to cover another.",
     "Cutting the library's budget to fund the new stadium is really just robbing Peter to pay Paul.", "debt", ()),
]

WORDS = [word(i, t, "idiom", m, ex=e, also=list(a)) for i, t, m, e, g, a in _I]
_G = {i: g for i, t, m, e, g, a in _I}
# Groups whose meanings could be argued as near-equivalents are merged, so a distractor is never drawn from the same cluster as the key.
_MERGE = {"brave": "consequence", "sacrifice": "consequence", "duty": "consequence", "discourage": "mood", "sad": "mood", "cheer": "mood", "resent": "angry",
          "quickstart": "speed", "needed": "right", "available": "chance", "risk": "trouble", "dilemma": "trouble", "avoid2": "avoid", "leave": "avoid",
          "emotion2": "emotion", "suspect": "doubt", "shallow": "versatile", "mutual": "agree", "misunderstand": "agree"}
_G = {i: _MERGE.get(g, g) for i, g in _G.items()}
_M = {i: m.rstrip(".") for i, t, m, e, g, a in _I}
_T = {i: t for i, t, m, e, g, a in _I}
_RARE = {"queer-the-pitch", "diamond-in-the-rough", "devils-advocate", "cross-purposes", "rock-hard-place", "elephant-in-the-room"}


def _pick(i, k):
    gi = _G[_I[i][0]]
    pool = [x[0] for x in _I if _G[x[0]] != gi]
    out, j = [], (i * 7 + k * 3) % len(pool)
    seen_g = set()
    while len(out) < 3:
        c = pool[j % len(pool)]
        if _G[c] not in seen_g:
            out.append(c); seen_g.add(_G[c])
        j += 5
    return out


def _gen():
    items = []
    for n, (wid, t, m, e, g, a) in enumerate(_I, 1):
        d = _pick(n - 1, 1)
        key = _M[wid]
        opts = [key] + [_M[x] for x in d]
        kpos = n % 4
        rest = opts[1:]; rest.insert(kpos, key)
        letters = "abcd"
        wrong = {}
        for ltr, o in zip(letters, rest):
            if o == key: continue
            other = next(x for x in d if _M[x] == o)
            wrong[ltr] = ruled_out(f"That is the meaning of '{_T[other]}', not of '{t}'.")
        items.append(q("q-idiom-meaning", "meaning", f"Select the most appropriate meaning of the given idiom.\n'{t}'", rest, letters[kpos],
                       f"'{t}' means: {key[0].lower() + key[1:]}.", wrong, lex=("meaning", wid), uid=f"id-g{n:03d}",
                       rules=["id-r1", "id-r2"] if wid in _RARE else ["id-r1"], tech=["literal-trap"], rare=wid in _RARE))
    return items


def _item(uid, wid, options, key, why, wrong, **kw):
    return q("q-idiom-meaning", "meaning", f"Select the most appropriate meaning of the given idiom.\n'{_T[wid]}'",
             options, key, why, wrong, lex=("meaning", wid), uid=uid, rules=["id-r1"], tech=["literal-trap"], **kw)


def _pq(qno, paper, wid, options, key, why, wrong, **kw):
    return q("q-idiom-meaning", "meaning", f"Choose the correct meaning of idiom: {_T[wid].capitalize() if wid != 'sixes-and-sevens' else 'At sixes and sevens'}",
             options, key, why, wrong, lex=("meaning", wid), paper=paper, qno=qno, rules=["id-r1", "id-r2"], tech=["literal-trap"], **kw)


def _rev(uid, wid, options, key, why, wrong, **kw):
    return q("q-idiom-identify", "meaning", f"Which of the following idioms has the meaning: '{_M[wid]}'?",
             options, key, why, wrong, lex=("fits", wid), uid=uid, rules=["id-r3"], tech=["literal-trap"], **kw)


def _fix(text, options, key, why, wrong, **kw):
    return q("q-idiom-correct", "improve",
             "A part of the following sentence is highlighted. Choose the option that can replace the highlighted part to improve the sentence. "
             "If you feel the other options do not improve the sentence, choose 'No improvement required'.\n" + text,
             options, key, why, wrong, rules=["id-r4"], tech=["literal-trap"], **kw)


S1, S2, S3 = "2025-09-12-S1", "2025-09-12-S2", "2025-09-12-S3"

PYQS = [
    _pq(88, S1, "sixes-and-sevens", ["A dilemma between two evils", "A free and fair decision", "In complete confusion", "A selection made under duress"], "c",
        "At sixes and sevens describes disorder or confusion, as when nobody knows who is doing what.",
        {"a": mistake("A choice between two evils is a dilemma ('between a rock and a hard place'), not confusion; the numbers six and seven tempt one to think of 'two'."),
         "b": ruled_out("A free and fair decision is about choice, not disorder."),
         "d": ruled_out("A forced selection is about pressure, not about things being in a muddle.")},
        trick="Think 'a mess': sixes and sevens is a muddle, never a choice.", rare=True),
    _pq(99, S2, "leave-no-stone-unturned", ["To keep shifting from one place to another repeatedly", "To make every possible effort to achieve a goal", "To remain quiet as a form of protest", "To obey someone without questioning"], "b",
        "To leave no stone unturned is to search or try in every way, so that nothing is missed.",
        {"a": mistake("This reads 'stone' and 'turning' as movement; the idiom is about completeness of effort, not travel."),
         "c": ruled_out("Staying quiet in protest has no link to effort or searching."),
         "d": ruled_out("Obeying without questioning is about submission, not effort.")},
        trick="'No stone left' means everything was tried: effort, not travel."),
    _pq(88, S3, "blow-a-fuse", ["To slip away quietly", "To vanish suddenly", "To become suddenly angry", "To manage a situation smartly"], "c",
        "When a fuse blows, the circuit breaks suddenly; the idiom means losing one's temper all at once.",
        {"a": ruled_out("Slipping away quietly is the opposite of the loud outburst a blown fuse suggests."),
         "b": mistake("Vanishing suddenly takes 'blow' to mean 'disappear'; a blown fuse is an outburst, not a disappearance."),
         "d": ruled_out("Managing a situation smartly has nothing to do with losing control.")},
        trick="A blown fuse is an electrical outburst: sudden anger."),
    _pq(80, "2026-10-07", "give-one-the-slip", ["to flatter others", "to neglect someone", "to give a notice", "to escape from someone"], "d",
        "To give someone the slip means to escape or get away from them, often by a trick.",
        {"a": ruled_out("Flattering someone is about praise, unrelated to escaping."), "b": mistake("Neglecting someone is about ignoring a duty, not getting away from a pursuer."),
         "c": ruled_out("Giving a notice means a formal warning, which has nothing to do with escape.")},
        trick="'Slip' suggests slipping away unnoticed: to escape."),
    _pq(99, "2026-10-07", "red-letter-day", ["Memorable day", "Rose day", "Holiday", "Birthday"], "a",
        "A red letter day is a memorable day because of some important or pleasant event, not necessarily a holiday or birthday.",
        {"b": ruled_out("'Rose day' is not a recognised meaning of this idiom."), "c": mistake("A holiday is a day off work, but a red letter day is defined by being memorable, not by being a holiday."),
         "d": mistake("A birthday is one kind of memorable day, but the idiom is broader and covers any important or pleasant occasion.")},
        trick="Red letters once marked feast days and holy days on old calendars: a day worth remembering."),
    _pq(82, "2026-10-08", "up-to-the-minute", ["At the last possible instant or opportunity", "To wait or pause", "To be as current as is possible", "At a very rapid pace"], "c",
        "Up to the minute means as current or up to date as possible, so the sense is about currency of information, not speed or timing.",
        {"a": ruled_out("'At the last possible instant' is about timing, confusing 'minute' as a point in time rather than up-to-dateness."),
         "b": ruled_out("'To wait or pause' has no connection to being current."),
         "d": mistake("'At a very rapid pace' again reads 'minute' as a unit of speed, not of how current the information is.")},
        trick="'Minute' here means 'current moment', not 'fast' or 'brief'."),
    q("q-idiom-identify", "meaning", "Which of the following idioms has the meaning: 'Eagerly, with great enthusiasm, or ready to enjoy oneself'?",
      ["Bear the bell", "Passing bells", "With bells on", "Sound as a bell"], "c",
      "'With bells on' means to come eagerly and enthusiastically, ready to enjoy oneself, exactly the meaning given.",
      {"a": ruled_out("'Bear the bell' means to take the lead or be the best at something, not to arrive eagerly."),
       "b": ruled_out("'Passing bells' are the bells rung to mark a death, unrelated to eagerness or enthusiasm."),
       "d": mistake("'Sound as a bell' means perfectly healthy or in excellent condition, not eager or enthusiastic.")},
      lex=("fits", "with-bells-on"), rules=["id-r3"], paper="2026-10-08", qno=83, tech=["literal-trap"]),
    _rev("id-q81", "work-the-system",
         ["Buck the system", "Get something out of one's system", "Get something out of your system", "Work the system"], "d",
         "'Work the system' is exactly to take advantage of a set of rules or procedures to achieve a personal or institutional goal, often by exploiting a loophole.",
         {"a": ruled_out("'Buck the system' means to resist or go against established rules, the opposite of exploiting them."),
          "b": mistake("'Get something out of one's system' means to stop feeling or thinking about something by expressing it, unrelated to rules or procedures."),
          "c": mistake("'Get something out of your system' is the same idiom as (b) with a different pronoun, still unrelated to exploiting rules.")},
         paper="2026-10-09", qno=81),
    _pq(97, "2026-10-09", "bang-for-buck",
        ["To begin to put forth more effort in some area", "To be very healthy",
         "To make money quickly and/or without effort, often through dishonest, unscrupulous, or ethically dubious means", "Greater value for the amount of money one is spending"], "d",
        "'A bigger bang for one's buck' means getting greater value for the money being spent.",
        {"a": ruled_out("Putting forth more effort is unrelated to value for money."),
         "b": ruled_out("Being very healthy has no connection to spending money."),
         "c": mistake("Making money dishonestly or without effort describes a different idiom ('easy money'), not getting good value for what one spends.")}),
    _pq(84, "2026-10-10", "hoist-with-own-petard",
        ["To be promoted far beyond one's competence", "To be rescued unexpectedly at the last moment", "To be burdened with another person's debts",
         "To be harmed or ruined by the very scheme one devised against another"], "d",
        "To be hoist with one's own petard is to be harmed or ruined by the very trap or scheme one set up against someone else.",
        {"a": ruled_out("Being promoted beyond one's competence describes a different idea entirely, not a scheme turning on its own maker."),
         "b": ruled_out("Being rescued unexpectedly is close to the opposite of being caught out by one's own plot."),
         "c": ruled_out("Being burdened with another person's debts is a financial idiom, unrelated to a scheme backfiring on its own author.")},
        trick="A petard was an explosive device; being 'hoist' (blown up) by one's own petard means your own trap destroys you."),
    _pq(85, "2026-10-10", "horses-mouth",
        ["From an anonymous tip", "Hearing it from someone else", "Reading it from a book", "From a reliable source"], "d",
        "Straight from the horse's mouth means directly from the original or most reliable source, not through any go-between.",
        {"a": ruled_out("An anonymous tip is by definition not traceable to a known, reliable source, the opposite sense of this idiom."),
         "b": mistake("Hearing it from someone else suggests it passed through an intermediary, exactly what 'straight from the horse's mouth' rules out."),
         "c": ruled_out("Reading it from a book is one possible source but not what the idiom names; the idiom is about directness, not books specifically.")},
        trick="'Straight from' signals no middleman: the information comes directly from the one who would know best."),
    _fix("The cunning minister is a master at the art of [[running with the hounds and hunting with the hare]].",
         ["dancing with the hare and hunting with the hounds", "dining with the hare and running with the hounds", "running with the hare and hunting with the hounds", "No improvement required"], "c",
         "The idiom pairs 'run' with 'hare' and 'hunt' with 'hounds'; the sentence has swapped the two pairings, so the fix restores 'running with the hare and hunting with the hounds'.",
         {"a": mistake("'Dancing with the hare' replaces 'running' with a verb from no idiom at all, even though 'hunting with the hounds' is left correct."),
          "b": mistake("'Dining with the hare and running with the hounds' swaps in two wrong verbs, neither of which belongs to this idiom."),
          "d": mistake("This says no change is needed, but the sentence has swapped the idiom's two halves ('hounds' with 'run', 'hare' with 'hunt'), so it is not the correct idiom as it stands.")},
         paper="2026-10-12", qno=85),
    _rev("id-q90-sq", "squeaky-wheel-grease",
         ["Stew in one's own grease", "Grease the skids", "The squeaky wheel gets the grease", "Grease the wheels"], "c",
         "'The squeaky wheel gets the grease' means the most noticeable problem or the loudest complaint is the one that gets attention and is addressed first, exactly the meaning given.",
         {"a": ruled_out("'Stew in one's own grease' means to suffer the consequences of one's own actions without help, not to draw attention by complaining."),
          "b": mistake("'Grease the skids' means to make a process move along quickly and smoothly, not to be the complaint that gets noticed first."),
          "d": mistake("'Grease the wheels' means to make something run more smoothly, often with a small inducement; close in image but not the same as getting attention by being the loudest.")},
         paper="2026-10-12", qno=90),
]


def practice_items():
    hand = [
        _item("id-p01", "spill-the-beans", [_M["burn-the-midnight-oil"], _M["spill-the-beans"], "To drop food while cooking", _M["once-in-a-blue-moon"]], "b",
              "To spill the beans is to reveal a secret.",
              {"a": ruled_out("That is the meaning of 'burn the midnight oil', a different idiom."),
               "c": mistake("This is the literal reading of the words; an idiom never means its literal picture."),
               "d": ruled_out("That is the meaning of 'once in a blue moon'; it has nothing to do with secrets.")}),
        _item("id-p02", "blessing-in-disguise", [_M["cost-an-arm-and-a-leg"], _M["hit-the-nail-on-the-head"], _M["blessing-in-disguise"], "A prayer said quietly"], "c",
              "A blessing in disguise is a misfortune that turns out to be beneficial.",
              {"a": ruled_out("That is the meaning of 'cost an arm and a leg'."),
               "b": ruled_out("That is the meaning of 'hit the nail on the head'."),
               "d": mistake("This takes 'blessing' and 'disguise' literally; the idiom is about luck in the end.")}, rare=True),
        _item("id-p03", "once-in-a-blue-moon", [_M["once-in-a-blue-moon"], "On the night of a full moon", _M["break-the-ice"], _M["bite-the-bullet"]], "a",
              "Once in a blue moon means very rarely.",
              {"b": mistake("This reads 'blue moon' as the moon itself; the idiom is about how seldom something happens."),
               "c": ruled_out("That is the meaning of 'break the ice'."),
               "d": ruled_out("That is the meaning of 'bite the bullet'.")}),
        _item("id-p04", "bite-the-bullet", [_M["spill-the-beans"], _M["bite-the-bullet"], "To chew something hard", _M["blessing-in-disguise"]], "b",
              "To bite the bullet is to face a painful situation with courage.",
              {"a": ruled_out("That is the meaning of 'spill the beans'."),
               "c": mistake("This is the literal picture of biting; the idiom means enduring something hard."),
               "d": ruled_out("That is the meaning of 'a blessing in disguise'.")}, rare=True),
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
        _rev("id-rev01", "spill-the-beans", ["Spill the beans", "Burn the midnight oil", "Once in a blue moon", "Lose heart"], "a",
             "'Spill the beans' means to reveal a secret, matching the meaning given.",
             {"b": ruled_out("'Burn the midnight oil' means to work or study late into the night, not to reveal a secret."),
              "c": ruled_out("'Once in a blue moon' means very rarely, not to reveal a secret."),
              "d": mistake("'Lose heart' means to lose hope or confidence, which can follow a setback but is not the same as revealing a secret.")}),
        _rev("id-rev02", "burn-the-midnight-oil", ["At cross purposes", "Burn the midnight oil", "Once in a blue moon", "Spill the beans"], "b",
             "'Burn the midnight oil' means to work or study late into the night, matching the meaning given.",
             {"a": mistake("'At cross purposes' means misunderstanding each other's aims, not working late."),
              "c": ruled_out("'Once in a blue moon' means very rarely, which says nothing about working late."),
              "d": ruled_out("'Spill the beans' means to reveal a secret, unrelated to working late.")}),
        _rev("id-rev03", "queer-the-pitch", ["At cross purposes", "Lose heart", "Queer the pitch", "Once in a blue moon"], "c",
             "'Queer the pitch' means to spoil someone's plans or chances, matching the meaning given.",
             {"a": mistake("'At cross purposes' means two people misunderstanding each other's aims, not one person spoiling another's chances."),
              "b": ruled_out("'Lose heart' means to lose hope or confidence, not to spoil someone else's plan."),
              "d": ruled_out("'Once in a blue moon' means very rarely, unrelated to spoiling a plan.")}, rare=True),
        _fix("By advertising the sequel before finishing the first film's script, the studio [[put the horse before the cart]].",
             ["put the cart before the donkey", "put the cart before the horse", "put the horse behind the cart", "No improvement required"], "b",
             "The idiom fixes the order as 'the cart before the horse' (doing things in the wrong order); the sentence has reversed this to 'horse before the cart', so the fix restores 'put the cart before the horse'.",
             {"a": mistake("This swaps 'horse' for 'donkey', which is not the idiom's wording at all."),
              "c": mistake("This keeps the wrong order ('horse' first) and merely changes 'before' to 'behind', still not the fixed idiom."),
              "d": mistake("This says no change is needed, but the sentence has reversed the idiom's fixed order ('horse before the cart' instead of 'cart before the horse').")},
             uid="id-p07"),
        _fix("Accusing his colleague of being late, when he himself arrives after ten every day, is simply [[the kettle calling the pot black]].",
             ["the kettle calling the pot white", "the pot calling the kettle white", "the pot calling the kettle black", "No improvement required"], "c",
             "The idiom is fixed as 'the pot calling the kettle black' (accusing someone of a fault one shares); the sentence has swapped 'pot' and 'kettle', so the fix restores 'the pot calling the kettle black'.",
             {"a": mistake("This keeps the swapped order ('kettle' calling 'pot') and also changes 'black' to 'white', neither of which restores the idiom."),
              "b": mistake("This restores the correct order ('pot' calling 'kettle') but changes 'black' to 'white', which is not the idiom's fixed wording."),
              "d": mistake("This says no change is needed, but the sentence has swapped 'pot' and 'kettle', which is not the idiom as fixed.")},
             uid="id-p08", rare=True),
        _fix("Cutting the library's budget to fund the new stadium is really just [[robbing Paul to pay Peter]].",
             ["robbing Peter to pay John", "paying Peter to rob Paul", "robbing Peter to pay Paul", "No improvement required"], "c",
             "The idiom fixes the names as 'robbing Peter to pay Paul' (solving one debt by creating another); the sentence has swapped the two names, so the fix restores 'robbing Peter to pay Paul'.",
             {"a": mistake("This replaces 'Paul' with 'John', a name that is not part of this fixed idiom at all."),
              "b": mistake("This reverses the verbs as well as the names ('paying' and 'robbing' swapped), which is not the idiom's fixed wording."),
              "d": mistake("This says no change is needed, but the sentence has swapped the two names, which is not the idiom as fixed.")},
             uid="id-p09"),
    ]
    return hand + _gen()
