"""Reading comprehension: 15 past questions on three passages. Passages are stored as our own condensed restatements (never the original text);
each question's evidence line must appear in the restated passage, which is the mechanical check."""
from bank import mistake, ruled_out, q

TOPIC = "reading-comprehension"
TIER = "quiz"
PREFIX = "rc"

NODES = {
    "q-rc-detail": {"short": "Stated detail", "label": "A fact the passage states", "kind": "qtype", "parent": TOPIC, "order": 1,
                    "summary": "'According to the passage ...': the answer is a line you can point to.", "links": []},
    "q-rc-main": {"short": "Main idea", "label": "Main idea or key distinction", "kind": "qtype", "parent": TOPIC, "order": 2,
                  "summary": "What the passage is mostly about; the idea that most of its sentences support.", "links": []},
    "q-rc-inference": {"short": "Inference", "label": "Implied meaning or reason", "kind": "qtype", "parent": TOPIC, "order": 3,
                       "summary": "A reason or implication that follows from what is said but is not word for word in the passage.", "links": []},
    "q-rc-remedy": {"short": "Cause / remedy", "label": "Cause, remedy or deciding factor", "kind": "qtype", "parent": TOPIC, "order": 4,
                    "summary": "What causes a problem, what the author suggests to fix it, or what decides an outcome.", "links": []},
}

RULES = [
    {"id": "rc-r1", "node": "q-rc-detail", "text": "The answer is in the passage. Take one key word from the question, find it in the passage, and read that sentence. An option that is true in general but not in the passage is wrong.",
     "ok": "Question: who has wisdom without schooling? Passage: farmers, craftsmen and elders.", "bad": "Choosing 'policy analysts' because it sounds sensible."},
    {"id": "rc-r2", "node": "q-rc-inference", "text": "For an implication, stay close to the passage's own direction: the correct option extends a stated idea (wisdom is the moral use of knowledge), while wrong ones introduce a new topic (language, numbers) or reverse a stated one.",
     "ok": "'Wisdom enriches the soul' -> it nurtures moral understanding.", "bad": "Choosing 'numerical ability', which the passage never mentions."},
    {"id": "rc-r3", "node": "q-rc-remedy", "text": "A remedy or decisive factor is announced by signals such as 'The cure is', 'the antidote', 'depends on', 'essential'. Find that sentence and choose the option that restates it.",
     "ok": "'The cure is to build dissent into the system' -> encouraging constructive dissent.", "bad": "Choosing 'strict compliance', which makes the problem worse."},
]

METHODS = {
    "q-rc-detail": {"cue": "'According to the author / As per the passage ...' with a who, what or which question.",
                    "standard": "Pick one key word from the question, find it in the passage, and read that sentence. Choose the option that restates it.",
                    "fast": "Skim the passage once for names, numbers and lists; they are where details sit.",
                    "eliminate": "Cross out options naming things the passage never mentions.",
                    "traps": ["Options that sound sensible but are not in the passage.", "Mixing up two cases that appear close together."],
                    "rules": ["rc-r1"], "tech": ["scan-evidence"]},
    "q-rc-main": {"cue": "'What key distinction / main point / central idea ...'",
                  "standard": "Read the first and last sentences, then ask what idea every paragraph supports.",
                  "fast": "The first sentence often states the contrast the whole passage develops.",
                  "eliminate": "Drop options that cover only a small part of the passage or a different topic.",
                  "traps": ["An option that names one example, not the central point.", "A broad option about the subject but not the passage's own point."],
                  "rules": ["rc-r1"], "tech": ["scan-evidence"]},
    "q-rc-inference": {"cue": "'What is implied by ...', 'Why does the author describe ... as ...'",
                       "standard": "Find the sentence nearest the idea, then pick the option that follows from it without adding new facts.",
                       "fast": "Look for the option that uses the passage's own key words (moral, ethical, both reliable and false).",
                       "eliminate": "Remove options from a different area or that reverse the author.",
                       "traps": ["An option that is true but not implied.", "An option about a neighbouring topic (language, numbers)."],
                       "rules": ["rc-r2"], "tech": ["scan-evidence"]},
    "q-rc-remedy": {"cue": "'What remedy', 'what factor decides', 'what has contributed to ...'",
                    "standard": "Look for 'the cure is', 'depends on', 'as a result' and read the sentence around it.",
                    "fast": "The last two sentences of a paragraph usually state the remedy or the deciding factor.",
                    "eliminate": "Drop options that make the problem worse or are unrelated to the author's suggestion.",
                    "traps": ["An option that sounds like a remedy but is the opposite of what the author wants.", "A factor named in the passage but not as the cause the question asks for."],
                    "rules": ["rc-r3"], "tech": ["scan-evidence"]},
}

REFS = []

PASSAGES = {
    "education-wisdom": {
        "title": "Education and wisdom",
        "src": "Our own condensed restatement of the passage in the SSC CGL Tier-I similar paper of 12 Sep 2025 (Adda247, shift 1). Not the original text.",
        "text": "People often use 'education' and 'wisdom' as if they meant the same thing, but they do not. Education is the organised gathering of knowledge, proved by degrees and marks and delivered through set courses and examinations. Wisdom goes further: it is the careful and moral use of what one knows in real situations, and it grows out of experience, self-reflection, emotional intelligence and a sense of right and wrong. A highly educated person can still lack wisdom if learning never turns into good judgement or responsible action, while farmers, craftsmen and elders, who may have little schooling, often show great wisdom because their choices rest on lived experience. Education sharpens the mind; wisdom deepens understanding. In an age of information overload and algorithm-driven thinking, the gap has widened. Schools tend to reward rote learning, exam scores and standard results, sometimes at the cost of critical thinking, ethical reasoning and emotional maturity, so society turns out people who solve technical problems well but struggle to decide with empathy, patience and foresight. Wisdom cannot be downloaded, rushed or certified. It comes slowly through trial and error, failure and reflection. Education usually ends with a qualification, whereas wisdom is a lifelong pursuit, shown in humility, steady ethical conduct and the calm handling of uncertainty. The best intelligence, in the end, is not only knowing what is right but acting on it even when that is hard."},
    "social-media-democracy": {
        "title": "Social media and democracy",
        "src": "Our own condensed restatement of the passage in the SSC CGL Tier-I similar paper of 12 Sep 2025 (Adda247, shift 2). Not the original text.",
        "text": "Social media has changed democratic life deeply: it encourages public participation, yet it also carries strategic deception. Platforms that began as places for personal sharing are now major arenas of political talk, where citizens voice opinions, gather around causes and hold the powerful to account almost at once. Because democracy relies on ideas and information moving freely, these platforms widen access by loosening the hold of traditional gatekeepers. Leaders can speak to voters directly, and citizen-led movements can use viral momentum to bring neglected concerns into public view, so during elections, protests and policy disputes they work like a digital marketplace of ideas. But the openness is risky. The networks that spread accurate information also speed up falsehoods, deepen polarisation and harden echo chambers through algorithms. Fake profiles, coordinated harassment and organised disinformation have disturbed elections in several democracies, and content built to stir emotion and maximise engagement often drowns out careful reasoning. So the effect on democracy depends not only on technology but on the ethical rules governing its use. Strong oversight, public media awareness and transparency about how algorithms rank and recommend content are essential if societies want the benefits without the damage. Social media is neither automatically good nor bad; it reflects collective choices, and the outcome depends on how responsibly citizens, institutions and platforms use it."},
    "groupthink": {
        "title": "Groupthink and conformity",
        "src": "Our own condensed restatement of the passage in the SSC CGL Tier-I similar paper of 12 Sep 2025 (Adda247, shift 3). Not the original text.",
        "text": "Groupthink arises when a team's wish for total agreement outweighs its willingness to examine other views critically. Decisions then become flawed, because disagreement is silenced from inside or discouraged by social cost. Related to it is social conformity, the habit of adjusting one's opinions or behaviour to match the majority, often without noticing, to win acceptance or avoid friction. In close circles such as boardrooms, policy groups and academic committees, people may hold back opposing ideas for fear of exclusion or damage to their reputation. Over time this uniformity breeds mental stagnation, weakens creativity and raises the risk of strategic mistakes. The Bay of Pigs episode and the Challenger space shuttle disaster are widely cited as classic cases in which groupthink distorted judgement. Psychologically, conformity is linked to an evolutionary pull towards tribal belonging, when standing apart could threaten survival. Today the same impulse appears as peer pressure, workplace norms and online echo chambers. Digital platforms intensify conformity because their algorithms build personalised bubbles that confirm what people already believe and filter out conflicting views. The cure is to build dissent into the system: when teams welcome principled disagreement, it acts as a safety check against tunnel vision, and valuing counterviews instead of punishing them supports stronger, more balanced decisions. Real progress comes not from automatic loyalty to majority norms but from critical probing and the nerve to challenge what feels comfortable."},
}

WORDS = []
S1, S2, S3 = "2025-09-12-S1", "2025-09-12-S2", "2025-09-12-S3"


def _rc(qtype, text, opts, key, why, wrong, ev, pid, paper, qno, **kw):
    return q(qtype, "rc", text, opts, key, why, wrong, evidence=ev, passage=pid, paper=paper, qno=qno, tech=["scan-evidence"],
             rules=kw.pop("rules", []), **kw)


PYQS = [
    # ---------------- Education and wisdom (S1, Q91-Q95)
    _rc("q-rc-detail", "As per the passage, wisdom is mainly developed through:", ["textbooks", "emotional detachment", "experience and reflection", "algorithmic thinking"], "c",
        "The passage says wisdom grows out of experience and self-reflection, and comes slowly through trial and error, failure and reflection.",
        {"a": ruled_out("Textbooks belong to formal education, which the passage contrasts with wisdom."),
         "b": mistake("The passage names emotional intelligence as a source of wisdom, so detachment is the opposite."),
         "d": ruled_out("Algorithm-driven thinking is named as part of the problem, not as a source of wisdom.")},
        "it grows out of experience, self-reflection", "education-wisdom", S1, 91, rules=["rc-r1"]),
    _rc("q-rc-inference", "What is implied by the statement “wisdom enriches the soul”?", ["It leads to academic achievement", "It nurtures profound moral understanding", "It enhances language skills", "It strengthens numerical ability"], "b",
        "Wisdom is described as the careful and moral use of knowledge, so enriching the soul means deepening moral understanding.",
        {"a": mistake("Academic achievement is what education brings; the passage separates it from wisdom."),
         "c": ruled_out("Language skills are never mentioned in the passage."),
         "d": ruled_out("Numerical ability is never mentioned in the passage.")},
        "the careful and moral use of what one knows in real situations", "education-wisdom", S1, 92, rules=["rc-r2"],
        caution="The quoted statement is not in the passage; the key is an inference from the passage's idea that wisdom is the moral use of knowledge."),
    _rc("q-rc-detail", "According to the author, which individuals may possess wisdom even without formal education?", ["Corporate executives", "Academicians", "Farmers and craftsmen", "Policy analysts"], "c",
        "The passage says farmers, craftsmen and elders with little schooling often show great wisdom.",
        {"a": ruled_out("Corporate executives are not mentioned."), "b": mistake("Academicians are the highly educated, who the passage says can still lack wisdom."),
         "d": ruled_out("Policy analysts are not mentioned.")},
        "farmers, craftsmen and elders, who may have little schooling, often show great wisdom", "education-wisdom", S1, 93, rules=["rc-r1"]),
    _rc("q-rc-main", "What key distinction does the passage primarily highlight?", ["Education and career growth", "Intelligence and memory", "Reading and writing skills", "Formal learning and applied wisdom"], "d",
        "The first sentence says people treat education and wisdom as one thing, but they differ: education is formal knowledge, and wisdom is its thoughtful use.",
        {"a": ruled_out("Career growth is never discussed."), "b": ruled_out("Memory is only touched on through rote learning, not as a main contrast."),
         "c": ruled_out("Reading and writing skills are not discussed.")},
        "People often use 'education' and 'wisdom' as if they meant the same thing, but they do not.", "education-wisdom", S1, 94, rules=["rc-r1"]),
    _rc("q-rc-remedy", "As per the author, what has contributed to the growing divide between education and wisdom in modern times?", ["Excessive reliance on social media", "Decline in the value placed on wisdom", "Emphasis on rote learning and algorithmic approaches", "Cessation of learning after formal education"], "c",
        "The passage links the widening gap to information overload, algorithm-driven thinking, and schools rewarding rote learning and exam scores.",
        {"a": ruled_out("Social media is not mentioned in this passage."),
         "b": mistake("The passage says wisdom is neglected, but it never says the value placed on wisdom has declined; it names schooling habits as the cause."),
         "d": mistake("The passage notes education ends with qualifications, but it gives that as a contrast, not as the cause of the divide.")},
        "Schools tend to reward rote learning", "education-wisdom", S1, 95, rules=["rc-r3"]),
    # ---------------- Social media and democracy (S2, Q79-Q83)
    _rc("q-rc-main", "What key democratic role of social media is highlighted in the passage?", ["Increasing entertainment content", "Eliminating printed newspapers", "Enabling wider circulation of information and ideas", "Creating labour unions"], "c",
        "The passage says democracy relies on ideas moving freely, and social media widens access by loosening the hold of gatekeepers.",
        {"a": ruled_out("Entertainment is not described as a democratic role."), "b": ruled_out("The passage compares social media with newspapers but never says they are eliminated."),
         "d": ruled_out("Labour unions are not mentioned.")},
        "these platforms widen access by loosening the hold of traditional gatekeepers", "social-media-democracy", S2, 79, rules=["rc-r1"]),
    _rc("q-rc-inference", "Why does the author describe social media as a “double-edged” force in democracy?", ["It is inexpensive to use", "It focuses mostly on images and videos", "It spreads both reliable information and false narratives", "It connects people globally"], "c",
        "Double-edged means it can help or harm: the same networks spread accurate information and falsehoods.",
        {"a": ruled_out("Cost is not discussed."), "b": ruled_out("The passage does not say social media is mostly images and videos."),
         "d": mistake("Connecting people is only one of the benefits; it does not explain a double edge, which needs both a good and a bad side.")},
        "The networks that spread accurate information also speed up falsehoods", "social-media-democracy", S2, 80, rules=["rc-r2"]),
    _rc("q-rc-detail", "According to the passage, what helps previously unheard groups gain attention on social media?", ["Newspaper editors and boards", "Strict journalistic gatekeeping", "Viral momentum along with citizen-led movements", "Government press agencies"], "c",
        "Citizen-led movements use viral momentum to bring neglected concerns into public view.",
        {"a": mistake("Editors are traditional gatekeepers whose hold social media loosens."), "b": mistake("Gatekeeping is what limits unheard groups, so it is the opposite."),
         "d": ruled_out("Government press agencies are not mentioned.")},
        "citizen-led movements can use viral momentum to bring neglected concerns into public view", "social-media-democracy", S2, 81, rules=["rc-r1"]),
    _rc("q-rc-remedy", "What remedy does the author emphasize to reduce misuse of social media in democratic systems?", ["Promoting meme-based communication", "Allowing unrestricted posting of all content", "Media awareness and transparency of algorithms", "Enforcing worldwide censorship"], "c",
        "The author calls strong oversight, public media awareness and algorithm transparency essential.",
        {"a": ruled_out("Memes are not mentioned."), "b": mistake("Unrestricted posting would add to the misuse the author warns about."),
         "d": mistake("The author asks for oversight and awareness, not censorship.")},
        "public media awareness and transparency about how algorithms rank and recommend content are essential", "social-media-democracy", S2, 82, rules=["rc-r3"]),
    _rc("q-rc-remedy", "What factor decides whether social media strengthens or weakens democracy, as per the passage?", ["The amount of political advertising", "The revenue model of platforms", "Ethical use driven by societal intent", "The influence of online celebrities"], "c",
        "The passage ends by saying the outcome depends on how responsibly citizens, institutions and platforms use it.",
        {"a": ruled_out("Political advertising is not mentioned."), "b": ruled_out("Platform revenue models are not mentioned."),
         "d": ruled_out("Online celebrities are not mentioned.")},
        "the outcome depends on how responsibly citizens, institutions and platforms use it", "social-media-democracy", S2, 83, rules=["rc-r3"]),
    # ---------------- Groupthink and conformity (S3, Q82-Q86)
    _rc("q-rc-main", "What is the main point of groupthink as presented in the passage?", ["Generating ideas through teamwork", "Prioritizing agreement over evaluation", "Relying only on specialists", "Distributing authority across units"], "b",
        "Groupthink is when a team's wish for total agreement outweighs its willingness to examine other views critically.",
        {"a": ruled_out("Generating ideas is what groupthink prevents, not what it is."), "c": ruled_out("Specialists are not mentioned."),
         "d": ruled_out("Spreading authority across units is not mentioned.")},
        "a team's wish for total agreement outweighs its willingness to examine other views critically", "groupthink", S3, 82, rules=["rc-r1"]),
    _rc("q-rc-detail", "As per the passage, which evolutionary tendency fuels social conformity?", ["Craving for control", "Urge for quick success", "Instinct for tribal belonging and safety", "Desire for comfort and luxury"], "c",
        "Conformity is linked to an evolutionary pull towards tribal belonging, when standing apart could threaten survival.",
        {"a": ruled_out("Control is not named as the evolutionary cause."), "b": ruled_out("Quick success is not named."), "d": ruled_out("Comfort and luxury are not named.")},
        "conformity is linked to an evolutionary pull towards tribal belonging", "groupthink", S3, 83, rules=["rc-r1"]),
    _rc("q-rc-detail", "Which incident is mentioned as a real-life outcome linked to groupthink?", ["A major peace treaty of the Cold War", "Challenger space shuttle disaster", "A national referendum outcome", "A stock-market technology collapse"], "b",
        "The Bay of Pigs episode and the Challenger space shuttle disaster are the cases named.",
        {"a": ruled_out("No peace treaty is named."), "c": ruled_out("No referendum is named."), "d": ruled_out("No stock-market collapse is named.")},
        "the Challenger space shuttle disaster are widely cited as classic cases", "groupthink", S3, 84, rules=["rc-r1"]),
    _rc("q-rc-inference", "How does the passage say digital platforms strengthen conformity?", ["By banning sensitive debates", "By summarizing facts through visuals", "By creating curated echo chambers", "By allowing hidden identities"], "c",
        "Algorithms build personalised bubbles that confirm what people already believe and filter out conflicting views, which are echo chambers.",
        {"a": ruled_out("Banning debates is not mentioned."), "b": ruled_out("Visual summaries are not mentioned."), "d": ruled_out("Hidden identities are not mentioned.")},
        "algorithms build personalised bubbles", "groupthink", S3, 85, rules=["rc-r2"]),
    _rc("q-rc-remedy", "What remedy does the passage recommend for groupthink and conformity?", ["Appointing more experienced seniors", "Enforcing strict compliance", "Encouraging constructive dissent", "Increasing online reach and connections"], "c",
        "The passage says the cure is to build dissent into the system and to welcome principled disagreement.",
        {"a": ruled_out("Seniority is not mentioned as a remedy."), "b": mistake("Strict compliance is conformity, the very problem."),
         "d": ruled_out("Online reach is linked to the problem, not the remedy.")},
        "The cure is to build dissent into the system", "groupthink", S3, 86, rules=["rc-r3"]),
]


def practice_items():
    return []
