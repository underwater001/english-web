"""Spellings: 5 past questions (correct-spelling and misspelt-word) and two generated questions per stored word.
Every wrong option is a misspelling declared on the word, and every 'correct' option in a misspelt-word question is a stored correct spelling,
so no item can have a second right answer. Memory hints are written fresh."""
from bank import mistake, ruled_out, q, word

TOPIC = "spellings"
TIER = "full"
PREFIX = "sp"

NODES = {
    "q-spell-correct": {"short": "Correct spelling", "label": "Pick the correct spelling", "kind": "qtype", "parent": TOPIC, "order": 1,
                        "summary": "Four spellings of one word; only one is right.", "links": []},
    "q-spell-misspelt": {"short": "Misspelt word", "label": "Find the misspelt word", "kind": "qtype", "parent": TOPIC, "order": 2,
                         "summary": "Four different words; one of them is spelt wrongly.", "links": []},
    "q-spell-replace": {"short": "Fix in context", "label": "Correct a highlighted word, or say none is needed", "kind": "qtype", "parent": TOPIC, "order": 3,
                        "summary": "A sentence highlights one word; pick the spelling that should replace it, or 'No replacement required' if it is already correct.", "links": []},
}

RULES = [
    {"id": "sp-r1", "node": "q-spell-correct", "text": "A prefix joined to a root keeps every letter of both: dis + appear = disappear (one s, two p), un + necessary = unnecessary (two n). Words such as accommodate, embarrass and occurrence carry two double letters each.",
     "ok": "Unnecessary, disappear, accommodate.", "bad": "Unecessary, dissapear, accomodate."},
    {"id": "sp-r2", "node": "q-spell-correct", "text": "I before e, except after c, when the sound is 'ee': believe, achieve, receive, ceiling. Learn the exceptions: weird, seize, leisure, height, foreign, neighbour.",
     "ok": "Receive, believe, weird.", "bad": "Recieve, beleive, wierd."},
    {"id": "sp-r3", "node": "q-spell-correct", "text": "There is no dependable rule for -ance/-ence or -ant/-ent, so learn the word. Memory aids: independent, intelligence, existence, experience and conscience take e; appearance, acquaintance, maintenance, perseverance and relevant take a.",
     "ok": "Independent, maintenance, perseverance.", "bad": "Independant, maintenence, perseverence."},
    {"id": "sp-r4", "node": "q-spell-correct", "text": "Words from a base keep the base's letters: sacrilege gives sacrilegious (the i is added after leg-i, not dropped), religion gives religious. But mischievous has no i after v: it has three syllables, mis-chiv-ous.",
     "ok": "Sacrilegious, religious, mischievous.", "bad": "Sacrilegous, religous, mischievious."},
    {"id": "sp-r5", "node": "q-spell-correct", "text": "Only one English word ends in -sede: supersede. Exceed, proceed and succeed end in -ceed; every other word of this family ends in -cede (precede, recede, concede, secede).",
     "ok": "Supersede, succeed, precede.", "bad": "Supercede, suceed."},
    {"id": "sp-r6", "node": "q-spell-correct", "text": "Say the word slowly, one syllable at a time, and write every syllable you say: Feb-ru-ar-y, lib-rar-y, gov-ern-ment, en-vi-ron-ment, Wed-nes-day, par-lia-ment, knowl-edge.",
     "ok": "February, library, government, Wednesday.", "bad": "Febuary, libary, goverment, Wensday."},
    {"id": "sp-r7", "node": "q-spell-misspelt", "text": "In a find-the-misspelt-word question, read each option letter by letter against the rules; the odd one out is usually wrong because of a double letter, an ie/ei swap, an a/e vowel, or a missing or extra syllable.",
     "ok": "Check doubles, then ie/ei, then vowels.", "bad": "Choosing the longest word without checking."},
    {"id": "sp-r8", "node": "q-spell-replace", "text": "First decide whether the highlighted word is already spelt correctly; if it is, the answer is 'No replacement required', not the closest-looking candidate. Only when it is genuinely wrong does one of the other options give its correct spelling.",
     "ok": "The sentence already reads 'conscientious', spelt correctly: No replacement required.", "bad": "Replacing an already-correct word with a near-miss spelling out of habit."},
]

METHODS = {
    "q-spell-correct": {"cue": "'Spot / identify the correct spelling', often of a long technical term named by a short description.",
                        "standard": "Say the word in syllables; test each option's doubles, ie/ei and vowels against the rules; keep the one that survives.",
                        "fast": "The four options usually differ in one spot. Find that spot and decide only that letter.",
                        "eliminate": "Cross out options that break a known pattern (extra or missing double, ei after a consonant) before comparing the rest.",
                        "traps": ["Options that differ only by one doubled letter.", "Long technical words whose root you can split (psycho + pharmaco + logy).", "British and American forms: choose the one the paper uses."],
                        "rules": ["sp-r1", "sp-r2", "sp-r3", "sp-r6"], "tech": ["read-whole"]},
    "q-spell-misspelt": {"cue": "'Identify the misspelt word' over four words, three of them correct.",
                         "standard": "Check each of the four words one by one against the rules; mark the one that breaks a pattern.",
                         "fast": "Skim for the usual slips: single letter where two belong (privilege has one l), a missing i (sacrilegious), ie/ei swapped.",
                         "eliminate": "Words you know cold go out first; spend your time on the unfamiliar one.",
                         "traps": ["Unusual but correct words (vicereine, defenestrate) look wrong and tempt you.", "The misspelt word is often the common-looking one."],
                         "rules": ["sp-r4", "sp-r5", "sp-r7"], "tech": ["read-whole"]},
    "q-spell-replace": {"cue": "A full sentence with one word highlighted, and a fourth option 'No replacement required'.",
                        "standard": "Spell the highlighted word out correctly in your head first, then compare it against the sentence's own spelling before looking at the options.",
                        "fast": "If the sentence's own spelling already matches what you know to be correct, stop and pick 'No replacement required'; do not second-guess a correct spelling.",
                        "eliminate": "Drop every option that is a near-miss misspelling of the target word; what remains is either the one correct spelling or 'No replacement required'.",
                        "traps": ["Assuming an error exists just because the question offers correction options.", "Picking a plausible-looking near-miss instead of checking letter by letter."],
                        "rules": ["sp-r8"], "tech": ["read-whole"]},
}

REFS = []

# (id, correct spelling, three misspellings, memory hint, rule, rare, own example sentence)
_S = [
    ("reconnaissance", "reconnaissance", ["reconnassance", "reconaissance", "reconnaisance"], "Two n and two s: re-con-nais-sance.", "sp-r1", True, "The scouts carried out a reconnaissance of the enemy camp."),
    ("facsimile", "facsimile", ["facsmile", "facsimily", "facsimele"], "Say every syllable: fac-sim-i-le. No double letters.", "sp-r6", True, "The museum displayed a facsimile of the original manuscript."),
    ("supplication", "supplication", ["supplecation", "suplication", "supplicasion"], "Two p: sup-pli-ca-tion, from 'supplicate'.", "sp-r1", True, "He fell to his knees in supplication before the king."),
    ("conscientious", "conscientious", ["consciencious", "conscientous", "conscienscious"], "Say every syllable: con-sci-en-tious, from 'conscience'.", "sp-r6", True, "A conscientious worker checks every report before submitting it."),
    ("indispensable", "indispensable", ["indispensible", "indispensibel", "indispensanble"], "Ends in -able, not -ible: in-dis-pens-a-ble.", "sp-r6", True, "Clean water is indispensable for good health."),
    ("entrepreneur", "entrepreneur", ["entreprenuer", "entrepeneur", "enterpreneur"], "Say every syllable: en-tre-pre-neur, borrowed whole from French.", "sp-r6", True, "The young entrepreneur started three companies before turning thirty."),
    ("euphemism-spell", "euphemism", ["euphamism", "eupheism", "euphemisim"], "Say every syllable: eu-phe-mism.", "sp-r6", True, "'Passed away' is a common euphemism for 'died'."),
    ("fractious", "fractious", ["fracteous", "fractous", "fractiuos"], "Say every syllable: frac-tious, from the same root as 'fraction'.", "sp-r6", True, "The fractious toddler refused to nap."),
    ("willful", "willful", ["wilfull", "willfull", "wifull"], "The American spelling doubles the l in 'will': will-ful. ('Wilful', with one l, is the British spelling and is also accepted.)", "sp-r6", True, "His willful disregard for the rules angered the committee."),
    ("anathema", "anathema", ["anathima", "anethema", "anathama"], "Say every syllable: a-nath-e-ma, from the Greek for a thing cursed or detested.", "sp-r6", True, "His behaviour was an anathema to the entire community."),
    ("negligence", "negligence", ["negligance", "negligense", "neglegence"], "Ends in -ence, not -ance, and keeps 'negli-' in the first syllable.", "sp-r3", True, "The inspector's report blamed the fire on negligence."),
    ("inconsistencies", "inconsistencies", ["inconsistancies", "inconsistencys", "inconsistenceis"], "Ends in -encies, not -ancies: the base word is 'consistency', spelt with an e.", "sp-r3", True, "The lawyer quickly spotted several inconsistencies in the testimony."),
    ("accommodate", "accommodate", ["acommodate", "accomodate", "acomodate"], "Two c and two m: ac-com-mo-date.", "sp-r1", False, "The hotel can accommodate two hundred guests."),
    ("achievement", "achievement", ["acheivement", "achievment", "achivement"], "i before e, then keep the e before ment.", "sp-r2", False, "Passing the exam was her proudest achievement."),
    ("acknowledge", "acknowledge", ["acknowlege", "aknowledge", "acknowledege"], "ac + knowledge: keep the d.", "sp-r6", False, "He did not acknowledge the mistake."),
    ("acquaintance", "acquaintance", ["acquaintence", "aquaintance", "acqaintance"], "Begins ac-qu; ends -ance.", "sp-r3", False, "She is only an acquaintance, not a friend."),
    ("address", "address", ["adress", "addres", "addresse"], "Two d, two s.", "sp-r1", False, "Write your address in capital letters."),
    ("aggressive", "aggressive", ["agressive", "aggresive", "agresive"], "Two g and two s.", "sp-r1", False, "The aggressive dog barked at everyone."),
    ("apparatus", "apparatus", ["aparatus", "apparatas", "apparetus"], "Two p, then -atus.", "sp-r1", False, "The lab apparatus was checked before the experiment."),
    ("appearance", "appearance", ["apperance", "appearence", "apearance"], "Keep appear whole, then add -ance.", "sp-r3", False, "His sudden appearance surprised everyone."),
    ("argument", "argument", ["arguement", "arguemnt", "argumant"], "Argue loses its e before -ment.", "sp-r6", False, "Their argument lasted an hour."),
    ("auxiliary", "auxiliary", ["auxilary", "auxillary", "auxiliery"], "aux-il-i-ary: four syllables, one l.", "sp-r6", True, "'Is' is an auxiliary verb in this sentence."),
    ("beautiful", "beautiful", ["beutiful", "beautifull", "beatiful"], "beau-ti-ful: the suffix has one l.", "sp-r6", False, "What a beautiful morning!"),
    ("beginning", "beginning", ["begining", "beggining", "beginnning"], "Double the n before -ing.", "sp-r1", False, "The beginning of the film was slow."),
    ("believe", "believe", ["beleive", "belive", "beleve"], "i before e after l.", "sp-r2", False, "I believe you will pass."),
    ("bureaucracy", "bureaucracy", ["beurocracy", "bureaucrasy", "buraucracy"], "bureau + cracy: eau is kept.", "sp-r6", True, "Too much bureaucracy slows every approval."),
    ("calendar", "calendar", ["calender", "calandar", "calander"], "Ends -ar, like 'sugar' and 'collar'.", "sp-r6", False, "Mark the date on the calendar."),
    ("category", "category", ["catagory", "categorry", "cateogry"], "cat-e-gory: an e after the t.", "sp-r6", False, "Each item belongs in a different category."),
    ("cemetery", "cemetery", ["cemetary", "cematery", "semetery"], "Three e's and no a: cem-e-ter-y.", "sp-r6", False, "The cemetery lies beyond the old church."),
    ("changeable", "changeable", ["changable", "changeble", "chaneable"], "Keep the e after g so g stays soft.", "sp-r6", False, "The weather here is changeable."),
    ("colleague", "colleague", ["collegue", "colleage", "coleague"], "Two l, then -eague.", "sp-r1", False, "My colleague covered my shift."),
    ("committee", "committee", ["comittee", "commitee", "committe"], "Double m, double t, double e.", "sp-r1", False, "The committee met on Monday."),
    ("conscience", "conscience", ["concience", "consience", "conscence"], "Contains the word 'science'.", "sp-r3", True, "A guilty conscience kept him awake."),
    ("conscious", "conscious", ["concious", "consious", "conscius"], "Contains 'science' too: con-sci-ous.", "sp-r3", False, "He was conscious of the noise."),
    ("criticism", "criticism", ["critisism", "criticizm", "critcism"], "critic + ism: keep the c.", "sp-r6", False, "She took the criticism well."),
    ("definitely", "definitely", ["definately", "definitly", "defenitely"], "Contains 'finite': de-finite-ly.", "sp-r6", False, "I will definitely attend."),
    ("desperate", "desperate", ["desparate", "desperete", "despirate"], "Contains 'sper' as in 'spare'.", "sp-r6", False, "They made a desperate attempt to escape."),
    ("dilemma", "dilemma", ["dilemna", "dillema", "dilema"], "One l, double m.", "sp-r1", False, "He faced a dilemma between two jobs."),
    ("disappear", "disappear", ["dissapear", "disapear", "dissappear"], "dis + appear: one s, two p.", "sp-r1", False, "The stain will disappear after one wash."),
    ("disappoint", "disappoint", ["dissapoint", "disapoint", "dissappoint"], "dis + appoint: one s, two p.", "sp-r1", False, "I do not want to disappoint my parents."),
    ("embarrass", "embarrass", ["embarass", "embarras", "embarrase"], "Double r and double s.", "sp-r1", False, "Please do not embarrass me in front of guests."),
    ("environment", "environment", ["enviroment", "environmant", "envirnoment"], "Say the n in 'environ' and again in 'ment'.", "sp-r6", False, "Plastic harms the environment."),
    ("exaggerate", "exaggerate", ["exagerate", "exaggarate", "exagerrate"], "ex + agg: double g.", "sp-r1", False, "Do not exaggerate the problem."),
    ("excellent", "excellent", ["excelent", "exellent", "excellant"], "Double l and ends -ent.", "sp-r3", False, "She gave an excellent speech."),
    ("existence", "existence", ["existance", "existense", "exsistence"], "Ends -ence; contains 'exist'.", "sp-r3", False, "The existence of the document was never proved."),
    ("experience", "experience", ["experiance", "expirience", "experence"], "Ends -ience.", "sp-r3", False, "He has ten years of experience."),
    ("familiar", "familiar", ["familier", "familar", "familliar"], "Contains 'liar' at the end: famil-iar.", "sp-r6", False, "The song sounded familiar."),
    ("february", "February", ["Febuary", "Febraury", "Feburary"], "Feb-ru-ar-y: pronounce the first r.", "sp-r6", False, "February is the shortest month."),
    ("fluorescent", "fluorescent", ["flourescent", "florescent", "fluoresent"], "fluor + escent.", "sp-r6", True, "A fluorescent tube lit the corridor."),
    ("foreign", "foreign", ["foriegn", "foreing", "forein"], "An exception to i before e.", "sp-r2", False, "She speaks three foreign languages."),
    ("forty", "forty", ["fourty", "fotry", "fortey"], "Four loses its u in forty.", "sp-r6", False, "Forty students passed."),
    ("government", "government", ["goverment", "govenment", "governmant"], "Say govern + ment; the n stays.", "sp-r6", False, "The government announced a new scheme."),
    ("grammar", "grammar", ["grammer", "gramar", "gramma"], "Ends -ar, with double m.", "sp-r1", False, "Good grammar improves your writing."),
    ("guarantee", "guarantee", ["garantee", "guarentee", "gaurantee"], "gu + ar + ant + ee.", "sp-r6", False, "The shop gave a one-year guarantee."),
    ("harass", "harass", ["harrass", "haras", "harasss"], "One r, double s.", "sp-r1", False, "It is a crime to harass a neighbour."),
    ("height", "height", ["heigth", "hieght", "heighth"], "Ends -ght; an exception to i before e.", "sp-r2", False, "Measure the height of the wall."),
    ("humorous", "humorous", ["humourous", "humorus", "humerous"], "humor + ous: the u of 'humour' drops.", "sp-r6", False, "He told a humorous story."),
    ("hygiene", "hygiene", ["hygeine", "hygene", "hiegene"], "Starts hy-gi-: g-i-e-n-e.", "sp-r2", False, "Hand hygiene prevents disease."),
    ("immediately", "immediately", ["imediately", "immediatly", "immedietely"], "Double m, then -ately.", "sp-r1", False, "Call me immediately."),
    ("independent", "independent", ["independant", "independen", "indipendent"], "Ends -ent, like 'dependent'.", "sp-r3", False, "An independent judge heard the case."),
    ("intelligence", "intelligence", ["inteligence", "intelligance", "intellegence"], "Double l; ends -gence.", "sp-r3", False, "Intelligence alone does not win exams."),
    ("interrupt", "interrupt", ["interupt", "interrup", "intrerupt"], "Double r.", "sp-r1", False, "Please do not interrupt the speaker."),
    ("knowledge", "knowledge", ["knowlege", "knowladge", "knoledge"], "know + ledge: keep the d.", "sp-r6", False, "Knowledge grows by reading."),
    ("laboratory", "laboratory", ["labratory", "laboritory", "labaratory"], "lab-or-a-to-ry: five syllables.", "sp-r6", False, "The laboratory was closed on Sunday."),
    ("leisure", "leisure", ["liesure", "leisur", "lesure"], "An exception: ei.", "sp-r2", False, "She reads in her leisure hours."),
    ("library", "library", ["libary", "liberry", "librery"], "Lib-rar-y: pronounce both r's.", "sp-r6", False, "The library opens at nine."),
    ("lieutenant", "lieutenant", ["leutenant", "lieutenent", "liutenant"], "lieu + tenant.", "sp-r6", True, "The lieutenant gave the order."),
    ("maintenance", "maintenance", ["maintainance", "maintenence", "maintanance"], "Not the same as 'maintain': it becomes -tenance.", "sp-r3", False, "Maintenance of the road is overdue."),
    ("miniature", "miniature", ["miniture", "minature", "minyature"], "Contains 'mini' and 'ature'.", "sp-r6", False, "He built a miniature of the fort."),
    ("miscellaneous", "miscellaneous", ["miscelaneous", "miscellanous", "miscellaneus"], "mis + cell + aneous: double l.", "sp-r4", True, "Miscellaneous expenses were small."),
    ("mischievous", "mischievous", ["mischievious", "mischivous", "mischevious"], "Three syllables: mis-chiv-ous; no extra i.", "sp-r4", True, "The mischievous child hid the keys."),
    ("necessary", "necessary", ["neccessary", "necesary", "necessery"], "One c, two s: 'a collar has one c, two s'.", "sp-r1", False, "It is necessary to carry a ticket."),
    ("noticeable", "noticeable", ["noticable", "noticeble", "notisable"], "Keep the e so c stays soft.", "sp-r6", False, "The change is noticeable."),
    ("occasion", "occasion", ["ocassion", "occassion", "occasoin"], "Double c, single s.", "sp-r1", False, "It was a happy occasion."),
    ("occurrence", "occurrence", ["occurence", "ocurrence", "occurance"], "Double c, double r.", "sp-r1", False, "A power cut is a daily occurrence here."),
    ("omission", "omission", ["ommission", "omision", "omisson"], "One m, double s.", "sp-r1", False, "The omission was noticed at once."),
    ("parallel", "parallel", ["paralel", "parallell", "parrallel"], "Double l in the middle, single at the end.", "sp-r1", False, "The two roads run parallel."),
    ("parliament", "parliament", ["parliment", "parlament", "parliamant"], "Par-lia-ment: say the 'ia'.", "sp-r6", False, "Parliament passed the bill."),
    ("perseverance", "perseverance", ["perseverence", "perserverance", "persaverance"], "From persevere, but ends -ance.", "sp-r3", False, "Perseverance brings results."),
    ("personnel", "personnel", ["personel", "personell", "personnal"], "Double n, single l.", "sp-r1", False, "All personnel must wear a badge."),
    ("phenomenon", "phenomenon", ["phenomenom", "phenomenan", "phenominon"], "Ends -non, like 'canon'.", "sp-r6", True, "Lightning is a natural phenomenon."),
    ("playwright", "playwright", ["playright", "playrite", "playwrite"], "A wright is a maker, as in 'shipwright'.", "sp-r6", True, "The playwright took a bow."),
    ("possession", "possession", ["posession", "possesion", "possestion"], "Double s twice.", "sp-r1", False, "Drugs in possession is a crime."),
    ("privilege", "privilege", ["privillage", "privelege", "priviledge"], "One l, and ends -ege.", "sp-r4", True, "It is a privilege to meet you."),
    ("pronunciation", "pronunciation", ["pronounciation", "pronuncation", "pronunciaton"], "Pronounce drops the o: pronunciation.", "sp-r6", False, "Your pronunciation is clear."),
    ("psychology", "psychology", ["psycology", "phsychology", "sychology"], "psych + ology: keep the h.", "sp-r6", False, "She studies psychology."),
    ("questionnaire", "questionnaire", ["questionaire", "questionnare", "quesionnaire"], "Double n.", "sp-r1", False, "Please fill in the questionnaire."),
    ("receive", "receive", ["recieve", "receve", "recive"], "After c, e comes before i.", "sp-r2", False, "You will receive a letter."),
    ("recommend", "recommend", ["reccomend", "recomend", "recomment"], "One c, double m.", "sp-r1", False, "I recommend this book."),
    ("referred", "referred", ["refered", "reffered", "referd"], "Double the final r before -ed.", "sp-r1", False, "The case was referred to the court."),
    ("relevant", "relevant", ["relevent", "revelant", "relavant"], "rel + evant.", "sp-r3", False, "Keep only the relevant facts."),
    ("religious", "religious", ["religous", "religeous", "relegious"], "religion + ous: keep the i.", "sp-r4", False, "It is a religious festival."),
    ("restaurant", "restaurant", ["restaraunt", "resturant", "restuarant"], "rest + au + rant.", "sp-r6", False, "We ate at a small restaurant."),
    ("rhythm", "rhythm", ["rythm", "rhythem", "rhythym"], "rhy + thm: no vowel but y.", "sp-r6", True, "The drummer kept a steady rhythm."),
    ("sacrilegious", "sacrilegious", ["sacrilegous", "sacreligious", "sacrilegeous"], "sacrilege + ious: leg-i-ous.", "sp-r4", True, "Burning the book was a sacrilegious act."),
    ("schedule", "schedule", ["shedule", "schedual", "scedule"], "Starts sch-.", "sp-r6", False, "The schedule changed again."),
    ("scissors", "scissors", ["scissers", "sissors", "scisors"], "sc + iss + ors.", "sp-r6", False, "Pass me the scissors."),
    ("separate", "separate", ["seperate", "separete", "seprate"], "sep-a-rate: 'a rat' in the middle.", "sp-r6", False, "Keep the files separate."),
    ("sergeant", "sergeant", ["sergant", "sargeant", "sergent"], "ser + geant.", "sp-r6", True, "The sergeant led the squad."),
    ("sincerely", "sincerely", ["sincerly", "sinceraly", "sincearly"], "sincere + ly: keep the e.", "sp-r6", False, "I sincerely thank you."),
    ("succeed", "succeed", ["suceed", "succede", "succed"], "Ends -ceed, with double c.", "sp-r5", False, "Hard work helps you succeed."),
    ("successful", "successful", ["succesful", "sucessful", "successfull"], "Double c, double s, one l at the end.", "sp-r1", False, "The launch was successful."),
    ("supersede", "supersede", ["supercede", "superceed", "supersead"], "The only word ending -sede.", "sp-r5", True, "The new rule will supersede the old one."),
    ("surprise", "surprise", ["suprise", "surprize", "surprice"], "sur + prise: keep the r.", "sp-r6", False, "The gift was a surprise."),
    ("temperature", "temperature", ["temprature", "tempreture", "temperture"], "tem-per-a-ture: four syllables.", "sp-r6", False, "The temperature fell at night."),
    ("tomorrow", "tomorrow", ["tommorow", "tomorow", "tommorrow"], "One m, double r.", "sp-r1", False, "I will see you tomorrow."),
    ("tournament", "tournament", ["tourment", "tornament", "tournement"], "tour + na + ment.", "sp-r6", False, "The tournament starts on Friday."),
    ("tyranny", "tyranny", ["tyrrany", "tyrany", "tyranney"], "One r, double n.", "sp-r1", True, "The people rose against tyranny."),
    ("unnecessary", "unnecessary", ["unecessary", "unneccessary", "unnecesary"], "un + necessary: two n.", "sp-r1", False, "Avoid unnecessary delays."),
    ("until", "until", ["untill", "untl", "untel"], "One l, unlike 'till'.", "sp-r6", False, "Wait until I return."),
    ("vacuum", "vacuum", ["vaccum", "vacum", "vaccuum"], "One c, double u.", "sp-r1", False, "Space is nearly a vacuum."),
    ("vengeance", "vengeance", ["vengence", "vengance", "vengeanse"], "Keep the e after g: venge-ance.", "sp-r3", True, "He swore vengeance on the thieves."),
    ("weird", "weird", ["wierd", "weired", "wirde"], "An exception to i before e.", "sp-r2", False, "A weird noise came from the attic."),
    ("wednesday", "Wednesday", ["Wensday", "Wendsday", "Wednessday"], "Wed-nes-day: say it in full.", "sp-r6", False, "The test is on Wednesday."),
    ("withhold", "withhold", ["withold", "withhould", "wihhold"], "with + hold: two h.", "sp-r1", False, "Do not withhold information."),
    # words that appeared in the 12 Sep 2025 papers
    ("vicereine", "vicereine", ["vicerine", "vicereen", "vicerein"], "Viceroy's female counterpart: vice + reine.", "sp-r6", True, "The vicereine hosted a dinner at the palace."),
    ("floccinaucinihilipilification", "floccinaucinihilipilification", ["floccinaucinihilipilifcation", "flocinaucinihilipilification", "floccinaucinihilipification"],
     "Four Latin words (flocci, nauci, nihili, pili) plus -fication; made famous as one of the longest words.", "sp-r6", True, "He was guilty of floccinaucinihilipilification, calling the offer worthless."),
    ("defenestrate", "defenestrate", ["defenistrate", "defenestrait", "deffenestrate"], "de + fenestra (window): to throw out of a window.", "sp-r6", True, "The rebels threatened to defenestrate the envoy."),
    ("ventriculoatrial", "ventriculoatrial", ["ventriculoartial", "ventriculoatriall", "ventriculoateriel"], "ventricle + atrial: ventriculo + atrial.", "sp-r6", True, "A ventriculoatrial shunt drains fluid from the brain."),
    ("psychopharmacology", "psychopharmacology", ["psychopharmacolgy", "psychopharmocology", "psychopharmecology"], "psycho + pharmaco + logy.", "sp-r6", True, "Psychopharmacology studies how drugs affect the mind."),
    ("trisomy", "trisomy", ["trissomie", "trissomy", "trisomie"], "tri (three) + somy (body): one s, ends -y.", "sp-r6", True, "Trisomy means three copies of a chromosome."),
]

WORDS = [word(i, c, "spelling", f"The correct spelling is '{c}'.", ex=e, misspell=m, note=h) for i, c, m, h, r, ra, e in _S]
_D = {i: dict(c=c, m=m, h=h, r=r, ra=ra) for i, c, m, h, r, ra, e in _S}
_ids = [i for i, *_ in _S]
S1, S2, S3 = "2025-09-12-S1", "2025-09-12-S2", "2025-09-12-S3"


def _opts(letters_key, key_text, wrongs):
    pos = "abcd".index(letters_key)
    o = wrongs[:]; o.insert(pos, key_text)
    return o


def _gen():
    items, n = [], 0
    for k, wid in enumerate(_ids, 1):
        d = _D[wid]
        n += 1
        kp = "abcd"[k % 4]
        opts = _opts(kp, d["c"], d["m"])
        wrong = {l: mistake(f"'{o}' is a common misspelling. {d['h']}") for l, o in zip("abcd", opts) if l != kp}
        items.append(q("q-spell-correct", "spelling", f"Select the correct spelling.", opts, kp,
                       f"The correct spelling is '{d['c']}'. {d['h']}", wrong, lex=("spell", wid), uid=f"sp-g{n:03d}", rules=[d["r"]], rare=d["ra"]))
    for k, wid in enumerate(_ids, 1):
        d = _D[wid]
        n += 1
        kp = "abcd"[(k + 1) % 4]
        bad = d["m"][k % 3]
        others = []
        j = (k * 5) % len(_ids)
        while len(others) < 3:
            c = _ids[j % len(_ids)]
            if c != wid and _D[c]["c"] not in others:
                others.append(_D[c]["c"])
            j += 7
        opts = _opts(kp, bad, others)
        wrong = {l: ruled_out(f"'{o}' is spelt correctly.") for l, o in zip("abcd", opts) if l != kp}
        items.append(q("q-spell-misspelt", "spelling", "Identify the misspelt word.", opts, kp,
                       f"'{bad}' is wrong; the correct spelling is '{d['c']}'. {d['h']}", wrong, lex=("misspelt", wid), uid=f"sp-g{n:03d}",
                       rules=[d["r"], "sp-r7"], rare=d["ra"]))
    return items


def _pc(qno, paper, wid, options, key, why, trick=""):
    d = _D[wid]
    wrong = {l: mistake(f"'{o}' is a common misspelling. {d['h']}") for l, o in zip("abcd", options) if l != key}
    return q("q-spell-correct", "spelling", PYQ_TEXT[(paper, qno)], options, key, why, wrong, lex=("spell", wid), paper=paper, qno=qno,
             rules=[d["r"]], rare=True, trick=trick)


def _pm(qno, paper, wid, options, key, why, trick=""):
    wrong = {l: ruled_out(f"'{o}' is spelt correctly.") for l, o in zip("abcd", options) if l != key}
    return q("q-spell-misspelt", "spelling", "Identify the misspelt word.", options, key, why, wrong, lex=("misspelt", wid), paper=paper, qno=qno,
             rules=[_D[wid]["r"], "sp-r7"], rare=True, trick=trick)


PYQ_TEXT = {
    (S1, 87): "Spot the correct spelling of a CSF-shunt procedure.",
    (S2, 89): "Spot the correct spelling of a drug-effect psychology field.",
    (S3, 95): "Identify the correct spelling of the term for chromosomal 'three copies'.",
    ("2026-10-07", 87): "Choose the correctly spelt word.",
    ("2026-10-08", 96): "Choose the correctly spelt word from the given options.",
}

PYQS = [
    _pc(87, S1, "ventriculoatrial", ["Ventriculoatrial", "Ventriculoartial", "Ventriculoatriall", "Ventriculoateriel"], "a",
        "The word joins ventriculo (of the ventricle) and atrial (of the atrium), so it is ventriculo + atrial.", trick="Split it: ventriculo + atrial."),
    _pm(89, S1, "sacrilegious", ["Vicereine", "floccinaucinihilipilification", "Defenestrate", "Sacrilegous"], "d",
        "Sacrilegious comes from sacrilege plus -ious, so it carries the extra i before the ending; 'sacrilegous' drops it.", trick="Sacrilege + ious: leg-i-ous."),
    _pc(89, S2, "psychopharmacology", ["Psychopharmacolgy", "Psychopharmacology", "Psychopharmocology", "Psychopharmecology"], "b",
        "The word is psycho + pharmaco + logy, and pharmaco keeps its 'ac' (as in pharmacy).", trick="Pharmacy gives pharmaco-."),
    _pm(96, S2, "privilege", ["Perseverance", "Supersede", "Privillage", "Mischievous"], "c",
        "Privilege has one l and ends -ege; 'privillage' doubles the l and changes the ending.", trick="Privilege: one l, ends -ege."),
    _pc(95, S3, "trisomy", ["Trissomie", "Trissomy", "Trisomy", "Trisomie"], "c",
        "Trisomy is tri (three) + somy (body): one s, and it ends in -y like 'monosomy'.", trick="Tri + somy."),
    _pm(81, "2026-10-07", "reconnaissance", ["Conscientious", "Indispensable", "Reconnassance", "Entrepreneur"], "c",
        "'Reconnassance' drops a letter; the correct spelling is 'reconnaissance', with two n and two s.", trick="Re-con-nais-sance: two n, two s."),
    _pc(87, "2026-10-07", "facsimile", ["Facsimile", "Facsmile", "Facsimily", "Facsimele"], "a",
        "'Facsimile' is said in four even syllables, fac-sim-i-le, with no double letters.", trick="Fac + sim + i + le, said whole."),
    _pm(93, "2026-10-07", "supplication", ["Euphemism", "Fractious", "Willful", "Supplecation"], "d",
        "'Supplecation' is wrong; the correct spelling is 'supplication', with two p, from 'supplicate'.", trick="Sup-pli-ca-tion: two p."),
    q("q-spell-replace", "spelling",
      "Select the option with the correct spelling that can replace the highlighted word in the given sentence. If the spelling in the given sentence is already correct, choose Option \"No replacement required\".\n"
      "His actions were considered an anathima to the entire community, leading to his exile.",
      ["anethema", "anathama", "anathema", "No replacement required"], "c",
      "The sentence's own spelling 'anathima' is wrong; the correct spelling is 'anathema', said a-nath-e-ma.",
      {"a": ruled_out("'Anethema' wrongly spells the third syllable with an e instead of a."),
       "b": ruled_out("'Anathama' wrongly spells the last syllable with an a instead of e."),
       "d": mistake("This says no replacement is needed, but the sentence's own spelling, 'anathima', is not a correct spelling of 'anathema'.")},
      rules=["sp-r8"], paper="2026-10-08", qno=87, rare=True),
    _pc(96, "2026-10-08", "playwright", ["Playright", "Playrite", "Playwrite", "Playwright"], "d",
        "The ending is '-wright' (one who makes something, as in 'wheelwright'), not '-write' or '-right'; 'playwright' is spelt with 'wright'.",
        trick="Play + wright, as in wheelwright: one who makes plays."),
]


def _rep(uid, sentence, options, key, why, wrong, rare=False):
    return q("q-spell-replace", "spelling",
             "Select the option with the correct spelling that can replace the highlighted word in the given sentence. If the spelling in the given sentence is already correct, choose Option \"No replacement required\".\n" + sentence,
             options, key, why, wrong, rules=["sp-r8"], uid=uid, rare=rare)


def practice_items():
    return _gen() + [
        _rep("sp-pr01", "Her conscientious attention to detail impressed the auditors.",
             ["Consciencious", "Conscientous", "Conscienscious", "No replacement required"], "d",
             "The highlighted word 'conscientious' is already spelt correctly, so the answer is 'No replacement required'; the other three options are common misspellings of it.",
             {"a": ruled_out("'Consciencious' is a misspelling of the already-correct word 'conscientious'."),
              "b": mistake("A test-taker might read 'conscientious' as needing fewer syllables and pick this near-miss, but the sentence's own spelling is already correct."),
              "c": ruled_out("'Conscienscious' adds an extra syllable; the sentence's own spelling is already correct.")}),
        _rep("sp-pr02", "The committee issued a stern reprimand to the officer for his negligance.",
             ["Negligence", "Negligense", "Neglegence", "No replacement required"], "a",
             "The sentence's own spelling 'negligance' is wrong; the correct spelling is 'negligence', ending in -ence.",
             {"b": ruled_out("'Negligense' wrongly spells the ending with an s instead of a c."),
              "c": ruled_out("'Neglegence' wrongly spells the first syllable 'negli-' as 'negle-'."),
              "d": mistake("This says no replacement is needed, but the sentence's own spelling, 'negligance', is not a correct spelling of 'negligence'.")}),
        _rep("sp-pr03", "His testimony contained several inconsistancies that the lawyer quickly noticed.",
             ["Inconsistencies", "Inconsistencys", "Inconsistenceis", "No replacement required"], "a",
             "The sentence's own spelling 'inconsistancies' is wrong; the correct spelling is 'inconsistencies', keeping the base word 'consistency' spelt with an e.",
             {"b": ruled_out("'Inconsistencys' wrongly pluralises with -ys instead of changing y to i before -es."),
              "c": ruled_out("'Inconsistenceis' misorders the letters at the ending."),
              "d": mistake("This says no replacement is needed, but the sentence's own spelling, 'inconsistancies', is not a correct spelling.")}, rare=True),
    ]
