"""Sentence & para jumbles: 6 past questions and 3 original practice items. Answers rest on the cited rules (opener, connectors, process order);
nothing here is machine-checked beyond the shape of the options."""
from bank import mistake, ruled_out, q

TOPIC = "para-jumbles"
TIER = "quiz"
PREFIX = "pj"

NODES = {
    "q-pj-para": {"short": "Paragraph", "label": "Arrange sentences into a paragraph", "kind": "qtype", "parent": TOPIC, "order": 1,
                  "summary": "Four sentences with connectors (However, This, Consequently, In addition): find the opener, then follow the links.", "links": []},
    "q-pj-process": {"short": "Process order", "label": "Arrange steps of a process", "kind": "qtype", "parent": TOPIC, "order": 2,
                     "summary": "Short passive steps (gathered, examined, designed, applied): put them in the order a real process runs.", "links": []},
}

RULES = [
    {"id": "pj-r1", "node": "q-pj-para", "text": "The opener states the topic on its own. A sentence that begins with a pronoun (It, This, These), or with Consequently, However, In addition or Often, cannot start the paragraph.",
     "ok": "'Communication is a multifaceted process ...' can open.", "bad": "'Consequently, effective communication ...' cannot open."},
    {"id": "pj-r2", "node": "q-pj-para", "text": "Follow the links: 'this transition' refers back to the change just described; 'in addition' adds to a point already made; 'consequently' follows a cause. A pointer word must come after the sentence it points to.",
     "ok": "One approach is moving to renewables. This transition lowers emissions.", "bad": "This transition lowers emissions. One approach is moving to renewables."},
    {"id": "pj-r3", "node": "q-pj-process", "text": "Order a process by what has to happen before what: gather data, then examine or monitor it, then classify it, then plan the action, then apply the findings. A step cannot use something that is made later.",
     "ok": "Information gathered -> feedback examined -> campaign designed -> findings applied.", "bad": "Campaign designed -> feedback examined (nothing to base it on)."},
]

METHODS = {
    "q-pj-para": {"cue": "'Rearrange the following sentences to form a coherent paragraph' with four numbered sentences and options such as 2, 1, 3, 4.",
                  "standard": "Pick the sentence that could stand first. Then place each pointer word after what it refers to. Check the resulting order reads smoothly.",
                  "fast": "Look at the options: if only one starts with the opener you found, test it first.",
                  "eliminate": "Discard options that begin with a sentence starting 'It', 'This', 'Consequently', 'Often'.",
                  "traps": ["Starting with a detail instead of the general statement.", "Placing 'This ...' before the sentence it refers to.", "A key whose last two sentences could swap; use the options to decide."],
                  "rules": ["pj-r1", "pj-r2"], "tech": ["first-sentence", "connectors", "pair-up"]},
    "q-pj-process": {"cue": "Four short passive sentences about data, a team, a campaign or findings.",
                     "standard": "Put the steps in the order a real process runs: gather, examine, decide, apply.",
                     "fast": "Find the first step (data gathered) and the last (findings applied or strategy made).",
                     "eliminate": "Drop options in which a step uses something not yet made.",
                     "traps": ["Two middle steps can look swappable; ask which depends on the other.", "Starting with the planning step."],
                     "rules": ["pj-r3"], "tech": ["first-sentence", "pair-up"]},
}

REFS = []
S1, S2, S3 = "2025-09-12-S1", "2025-09-12-S2", "2025-09-12-S3"
_R1 = "Rearrange the following sentences in correct order to make a logical passage:\n"
_R2 = "Rearrange the following sentences to form a coherent paragraph:\n"

PYQS = [
    q("q-pj-process", "rearrange", _R1 + "1. A communication strategy was developed using outreach insights.\n2. Demographic data was monitored through campaign dashboards.\n3. User engagement was gathered from multiple platforms.\n4. Analysts classified users according to age and behaviour.",
      ["3-2-4-1", "2-3-1-4", "3-1-4-2", "4-1-2-3"], "a",
      "The data is gathered first (3), then monitored (2), then classified (4), and the strategy (1) is built from those insights.",
      {"b": ruled_out("This starts with monitoring (2) before any engagement data has been gathered (3)."),
       "c": mistake("This puts the strategy (1) before the users have been classified (4) and monitored (2), but the strategy uses outreach insights."),
       "d": ruled_out("This starts with classifying users (4) before data has been collected.")},
      rules=["pj-r3"], paper=S1, qno=80, tech=["first-sentence", "pair-up"], trick="Gather, monitor, classify, then plan.",
      caution="The two middle steps (monitor, classify) could be argued either way; the key follows a data pipeline (gather, monitor, classify, plan)."),
    q("q-pj-para", "rearrange", _R2 + "1. It is a process that involves systematic and objective examination of a subject to uncover new facts or verify existing ones.\n2. Research serves as a fundamental pillar of academic and scientific advancement.\n3. This may be either theoretical, intended to broaden knowledge, or applied, designed to address a practical problem.\n4. The results of this investigation are then recorded and peer-reviewed to ensure validity and credibility.",
      ["2, 1, 3, 4", "1, 2, 4, 3", "4, 3, 2, 1", "3, 4, 1, 2"], "a",
      "Sentence 2 names the topic, so it opens. Sentence 1 ('It is a process ...') defines it, 3 ('This may be ...') divides it into types, and 4 reports the results.",
      {"b": ruled_out("This opens with 'It is a process', where 'It' has no referent yet."),
       "c": ruled_out("This opens with the results of an investigation that has not yet been introduced."),
       "d": ruled_out("This opens with 'This may be either ...', where 'This' has nothing to point to.")},
      rules=["pj-r1", "pj-r2"], paper=S1, qno=81, tech=["first-sentence", "connectors"], trick="2 names the topic; 1 starts with 'It'."),
    q("q-pj-para", "rearrange", _R2 + "1. Consequently, effective communication depends on more than merely the words we speak.\n2. Non-verbal signals, such as tone, facial expressions, and gestures, may communicate more than the spoken message itself.\n3. Communication is a multifaceted process that involves sharing information, ideas, and emotions between people.\n4. Often, it is these subtle cues that reveal how a message is truly meant or received.",
      ["3, 2, 1, 4", "2, 4, 1, 3", "1, 4, 3, 2", "3, 4, 2, 1"], "a",
      "3 defines communication and opens. 2 introduces non-verbal signals, 1 ('Consequently ...') draws the conclusion, and 4 adds how subtle cues show the true meaning.",
      {"b": ruled_out("This opens with a detail (2) and ends with the general definition (3)."),
       "c": ruled_out("This opens with 'Consequently', which needs an earlier cause."),
       "d": mistake("This puts 4 ('these subtle cues') before 2 introduces non-verbal signals, so 'these' has nothing to refer to.")},
      rules=["pj-r1", "pj-r2"], paper=S2, qno=93, tech=["first-sentence", "connectors"], trick="3 is the only sentence that can stand first."),
    q("q-pj-para", "rearrange", _R2 + "1. One effective approach is to broaden energy options by moving away from fossil fuels towards renewables such as solar, wind, and geothermal energy.\n2. To reduce the severe impacts of climate change, nations must sharply cut dependence on high-carbon energy generation.\n3. This transition not only lowers greenhouse gas output but also improves air quality and opens up new economic possibilities.\n4. In addition, measures that encourage energy efficiency in buildings and transport can further reduce total energy use.",
      ["2, 1, 3, 4", "1, 2, 4, 3", "3, 1, 4, 2", "2, 3, 1, 4"], "a",
      "2 states the problem, 1 gives one approach, 3 ('This transition') comments on that approach, and 4 ('In addition') adds another measure.",
      {"b": ruled_out("This opens with 'One effective approach', which needs a problem stated first."),
       "c": ruled_out("This opens with 'This transition', which has nothing to point to."),
       "d": mistake("This puts 3 ('This transition') before 1, where the transition is first described.")},
      rules=["pj-r1", "pj-r2"], paper=S2, qno=100, tech=["first-sentence", "connectors"], trick="2 -> 1 -> 3 -> 4."),
    q("q-pj-process", "rearrange", _R1 + "1. The team examined the feedback results.\n2. The findings were applied to enhance the customer journey.\n3. A focused promotional campaign was designed.\n4. The information was gathered through multiple sources.",
      ["1-4-3-2", "3-1-2-4", "4-3-1-2", "4-1-3-2"], "d",
      "The information is gathered first (4), the team examines it (1), a campaign is designed (3), and the findings are applied (2).",
      {"a": ruled_out("This examines results (1) before the information is gathered (4)."),
       "b": ruled_out("This designs a campaign (3) before anything has been gathered or examined."),
       "c": mistake("This designs the campaign (3) before the team has examined the feedback (1).")},
      rules=["pj-r3"], paper=S3, qno=79, tech=["first-sentence", "pair-up"], trick="Gather, examine, design, apply.",
      caution="The final two steps (campaign designed, findings applied) are loosely ordered in the passage; the key follows the options on offer."),
    q("q-pj-para", "rearrange", _R2 + "1. These influences include how much sunlight is received, the make-up of the atmosphere, and the Earth’s orbital path.\n2. Long-term shifts in Earth’s climate are shaped by an intricate mix of natural and human-driven influences.\n3. The most prominent human-driven influence is the release of greenhouse gases from industrial processes.\n4. Together, these components control the planet’s overall energy balance and, as a result, its average temperature.",
      ["2, 1, 3, 4", "1, 2, 3, 4", "3, 4, 1, 2", "4, 2, 3, 1"], "a",
      "2 states the topic. 1 ('These influences') lists the natural influences, 3 adds the human-driven one, and 4 ('Together, these components') sums up.",
      {"b": ruled_out("This opens with 'These influences', which has nothing to refer to."),
       "c": ruled_out("This opens with a detail (3) and then a summary (4) before the topic has been stated."),
       "d": ruled_out("This opens with 'Together, these components', which has nothing to refer to.")},
      rules=["pj-r1", "pj-r2"], paper=S3, qno=91, tech=["first-sentence", "connectors"], trick="Only one option starts with 2.",
      caution="Sentence 4 ('these components') reads best after 1 and 3 together; 2, 1, 3, 4 is the only offered order that opens with the topic sentence."),
]


def _base():
    return [
        q("q-pj-process", "rearrange", _R1 + "1. The seeds were sown in early June.\n2. The farmer ploughed the field after the first rains.\n3. By October the crop was ready to be harvested.\n4. Green shoots appeared within two weeks.",
          ["2-1-4-3", "1-2-4-3", "2-4-1-3", "3-4-1-2"], "a",
          "Ploughing comes first (2), then sowing (1), then shoots (4), then the harvest (3).",
          {"b": ruled_out("Sowing (1) is placed before the field is ploughed (2)."), "c": ruled_out("Shoots (4) appear before the seeds are sown (1)."), "d": ruled_out("Harvest (3) is placed first.")},
          rules=["pj-r3"], uid="pj-p01"),
        q("q-pj-para", "rearrange", _R2 + "1. Therefore, schools should teach students how to judge sources.\n2. The internet gives every student instant access to information.\n3. However, not everything online is accurate.\n4. Fake claims often look as convincing as real ones.",
          ["2-3-4-1", "3-2-4-1", "2-4-3-1", "1-2-3-4"], "a",
          "2 states the topic, 3 ('However') adds the problem, 4 gives the reason it matters, and 1 ('Therefore') concludes.",
          {"b": ruled_out("This opens with 'However', which needs a point to contrast with."), "c": mistake("4 ('Fake claims') comes before 3 states that online content may be inaccurate."),
           "d": ruled_out("This opens with 'Therefore', which needs a cause.")}, rules=["pj-r1", "pj-r2"], uid="pj-p02"),
        q("q-pj-para", "rearrange", _R2 + "1. Soon the whole village joined the clean-up.\n2. A small group of students began collecting litter from the river bank.\n3. Within a month the river looked clear again.\n4. Their effort drew the attention of their neighbours.",
          ["2-4-1-3", "2-1-4-3", "4-2-1-3", "2-4-3-1"], "a",
          "2 starts the story, 4 ('Their effort') follows, 1 ('Soon the whole village') grows, and 3 gives the result.",
          {"b": mistake("1 (the whole village joining) comes before the neighbours notice (4)."), "c": ruled_out("This opens with 'Their effort', which has nothing to refer to."), "d": ruled_out("The result (3) is placed before the village joins (1).")},
          rules=["pj-r1", "pj-r2"], uid="pj-p03", rare=True),
    ]

_EXTRA = [
    q("q-pj-para", "rearrange", _R2 + "1. The habit spread quickly once tea became cheap enough for a daily cup.\n2. Tea reached Britain as a luxury that only the rich could afford.\n3. By the end of the century it had become the drink of the whole country.\n4. Falling prices, in turn, depended on new plantations in India and Ceylon.",
      ["2, 1, 4, 3", "1, 2, 3, 4", "4, 2, 1, 3", "3, 2, 4, 1"], "a",
      "2 introduces tea as a luxury, 1 says the habit spread when it grew cheap, 4 explains what made it cheap, and 3 states the result.",
      {"b": ruled_out("This opens with 'The habit', which has no habit before it to refer to."),
       "c": mistake("'Falling prices, in turn' answers a point already made, so it cannot open the paragraph."),
       "d": ruled_out("This opens with the final result and then explains the beginning.")},
      rules=["pj-r1", "pj-r2"], uid="pj-p04", tech=["first-sentence", "connectors"]),
    q("q-pj-para", "rearrange", _R2 + "1. However, a single reading tells us very little about a patient's usual pressure.\n2. Blood pressure is measured in almost every clinic, often within a minute of the patient sitting down.\n3. For this reason, doctors now prefer several readings taken at home over one taken in the clinic.\n4. It rises with anxiety, with a brisk walk to the door and even with a full bladder.",
      ["2, 1, 4, 3", "2, 4, 1, 3", "1, 4, 2, 3", "4, 1, 2, 3"], "a",
      "2 states the practice, 1 ('However') raises the doubt, 4 gives the reasons the single reading misleads, and 3 ('For this reason') draws the conclusion.",
      {"b": mistake("Putting 4 before 1 gives the reasons before the doubt they support, so 'However' loses the point it contrasts with."),
       "c": ruled_out("This opens with 'However', which needs an earlier statement."),
       "d": ruled_out("This opens with 'It rises', where 'It' has nothing to refer to.")},
      rules=["pj-r1", "pj-r2"], uid="pj-p05", tech=["first-sentence", "connectors"]),
    q("q-pj-para", "rearrange", _R2 + "1. Such a lamp paid for itself within a year and then went on saving.\n2. The early models were dim, slow to brighten and unpleasant to read by.\n3. Compact fluorescent lamps were sold in the 1990s as the answer to the household electricity bill.\n4. Later versions fixed all three faults while keeping the saving.",
      ["3, 2, 4, 1", "2, 3, 1, 4", "3, 1, 2, 4", "1, 3, 2, 4"], "a",
      "3 introduces the lamps, 2 lists the early faults, 4 says later versions fixed those three faults, and 1 states what such a lamp then achieved.",
      {"b": ruled_out("This opens with 'The early models', which needs the product to be named first."),
       "c": mistake("'Such a lamp' in 1 can only follow the sentence that describes the improved lamp, so it cannot come before 2 and 4."),
       "d": ruled_out("This opens with 'Such a lamp', which has nothing to refer to.")},
      rules=["pj-r1", "pj-r2"], uid="pj-p06", tech=["first-sentence", "connectors"], rare=True),
    q("q-pj-process", "rearrange", _R1 + "1. The shortlisted applications were verified against the records.\n2. Advertisements were published in three newspapers.\n3. Appointment letters were issued to the selected candidates.\n4. The applications received were screened against the minimum qualifications.",
      ["2-4-1-3", "4-2-1-3", "2-1-4-3", "1-2-4-3"], "a",
      "The post is advertised (2), the applications are screened (4), the shortlist is verified (1), and letters are issued (3).",
      {"b": ruled_out("Applications are screened before they have been invited by an advertisement."),
       "c": mistake("Verification of the shortlist (1) is placed before the screening (4) that produces the shortlist."),
       "d": ruled_out("This opens with the verification of a shortlist that does not yet exist.")},
      rules=["pj-r3"], uid="pj-p07", tech=["first-sentence", "pair-up"]),
    q("q-pj-process", "rearrange", _R1 + "1. The samples were tested in the district laboratory.\n2. Notices were served on the two dairies whose milk had failed.\n3. Inspectors collected milk samples from eleven shops.\n4. The results were entered in the inspection register.",
      ["3-1-4-2", "1-3-4-2", "3-4-1-2", "2-3-1-4"], "a",
      "Samples are collected (3), tested (1), the results recorded (4), and notices served on the dairies that failed (2).",
      {"b": ruled_out("Samples cannot be tested before they are collected."),
       "c": mistake("Results are entered in the register (4) before the testing (1) that produces them."),
       "d": ruled_out("Notices are served before any sample has been collected or tested.")},
      rules=["pj-r3"], uid="pj-p08", tech=["first-sentence", "pair-up"]),
    q("q-pj-para", "rearrange", _R2 + "1. They settled instead on a rule of thumb: plant where the shade will fall on a wall by noon.\n2. The committee wanted a formula for deciding where to plant street trees.\n3. None of the formulas it examined survived contact with the city's narrow lanes.\n4. Two summers later, the rule had produced more usable shade than any formula would have.",
      ["2, 3, 1, 4", "2, 1, 3, 4", "3, 2, 1, 4", "1, 2, 3, 4"], "a",
      "2 states the aim, 3 reports that the formulas failed, 1 ('They settled instead') gives what was adopted, and 4 reports the outcome.",
      {"b": mistake("'They settled instead' in 1 must follow the failure in 3, not come before it."),
       "c": ruled_out("This opens with 'None of the formulas it examined', where 'it' has no antecedent."),
       "d": ruled_out("This opens with 'They settled instead', which needs an earlier attempt to replace.")},
      rules=["pj-r1", "pj-r2"], uid="pj-p09", tech=["first-sentence", "connectors"]),
    q("q-pj-para", "rearrange", _R2 + "1. In addition, a bus that is predictable is worth more to a passenger than one that is merely frequent.\n2. Most cities measure their bus service by the number of buses they run.\n3. A better measure is the share of passengers who reach their stop within a minute of the published time.\n4. That number says nothing about whether the buses arrive when they are expected.",
      ["2, 4, 3, 1", "2, 3, 4, 1", "4, 2, 3, 1", "1, 2, 4, 3"], "a",
      "2 states the usual measure, 4 ('That number') criticises it, 3 offers a better one, and 1 ('In addition') adds a supporting point.",
      {"b": mistake("3 offers the better measure before 4 has explained what is wrong with the old one, so 'That number' has nothing to point back to."),
       "c": ruled_out("This opens with 'That number', which has no number before it."),
       "d": ruled_out("This opens with 'In addition', which needs an earlier point to add to.")},
      rules=["pj-r1", "pj-r2"], uid="pj-p10", tech=["first-sentence", "connectors"]),
]


def practice_items():
    return _base() + _EXTRA
