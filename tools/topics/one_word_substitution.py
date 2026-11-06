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


# ---------------------------------------------------------------------------------------------------
# The 500 most repeated SSC one-word substitutions, from the ranked list in the Black Book of English
# Vocabulary (qmaths.in). The book supplies WHICH words and HOW OFTEN each has been asked (#A); every
# meaning and example below is our own wording, so none of the book's text is reproduced here.
# ---------------------------------------------------------------------------------------------------
_O2 = [
    ("bureaucracy-ows", "bureaucracy", "Government by officials working through many fixed procedures", "Every permit passes through four desks, which is bureaucracy at its slowest.", "rule"),
    ("oligarchy", "oligarchy", "Rule by a small privileged group", "The island was run as an oligarchy of six trading families.", "rule"),
    ("aristocracy", "aristocracy", "Rule by the nobility, or the nobility itself", "The old aristocracy lost its land after the reforms.", "rule"),
    ("monarchy", "monarchy", "Rule by a king or a queen", "Britain remains a monarchy with an elected parliament.", "rule"),
    ("democracy", "democracy", "Government in which the people elect their rulers", "In a democracy the losing side accepts the count.", "rule"),
    ("dictatorship", "dictatorship", "Government by a single ruler with complete power", "The dictatorship banned every newspaper in a week.", "rule"),
    ("anarchist", "anarchist", "One who believes that all government should be abolished", "The anarchist argued that the state itself was the problem.", "belief3"),
    ("red-tapism", "red tapism", "Insistence on excessive official rules and paperwork", "Red tapism delayed the hospital's licence by two years.", "office"),
    ("sinecure", "sinecure", "A post that carries pay but little or no work", "The chairmanship was a sinecure with a car and no duties.", "office"),
    ("honorarium", "honorarium", "A voluntary payment for a service for which no fee is fixed", "The guest speaker was given an honorarium of five thousand rupees.", "money3"),
    ("honorary", "honorary", "Held as an honour, without pay or the usual duties", "She was made an honorary member of the society.", "money3"),
    ("elegy", "elegy", "A poem of mourning for someone who has died", "He wrote an elegy for his brother.", "writing"),
    ("ode", "ode", "A poem addressed to a person or thing, usually in praise", "Keats wrote an ode to a nightingale.", "writing"),
    ("sonnet", "sonnet", "A poem of fourteen lines with a fixed rhyme scheme", "Each sonnet in the sequence ends with a couplet.", "writing"),
    ("ballad", "ballad", "A poem or song that tells a story in short verses", "The ballad recounts a shipwreck off the coast.", "writing"),
    ("parable", "parable", "A short story told to teach a moral or spiritual lesson", "The sermon turned on the parable of the lost sheep.", "writing"),
    ("soliloquy", "soliloquy", "A speech in which a character speaks his thoughts aloud, alone on stage", "Hamlet's soliloquy is spoken to an empty stage.", "writing"),
    ("prologue", "prologue", "An introductory section at the beginning of a play or book", "The prologue sets the quarrel in motion.", "writing"),
    ("epilogue", "epilogue", "A closing section at the end of a play or book", "An epilogue tells us what became of the family.", "writing"),
    ("epigraph", "epigraph", "An inscription cut into stone, or a quotation placed at the start of a book", "The epigraph on the gateway names the builder.", "writing"),
    ("manuscript", "manuscript", "A text written by hand, or an author's copy before it is printed", "The manuscript was corrected in pencil throughout.", "writing"),
    ("biography", "biography", "The story of a person's life written by somebody else", "The biography draws on letters nobody had read.", "writing"),
    ("bibliography", "bibliography", "A list of the books and articles used or recommended on a subject", "Add a bibliography at the end of the dissertation.", "writing"),
    ("catalogue", "catalogue", "A complete list of items arranged in order", "The library catalogue runs to four volumes.", "writing"),
    ("pseudonym", "pseudonym", "A false name used by a writer in place of his own", "She published her early novels under a pseudonym.", "writing"),
    ("plagiarism", "plagiarism", "The act of passing off another's writing or ideas as one's own", "The paper was withdrawn for plagiarism.", "writing"),
    ("lexicographer", "lexicographer", "One who compiles and edits dictionaries", "A lexicographer records how a word is used, not how it ought to be.", "job"),
    ("curator", "curator", "One in charge of a museum or a collection", "The curator rehung the whole gallery.", "job"),
    ("chauffeur", "chauffeur", "A person employed to drive somebody's car", "The chauffeur waited outside the gate.", "job"),
    ("calligraphy", "calligraphy", "The art of beautiful handwriting", "The invitation was addressed in calligraphy.", "art"),
    ("cartography", "cartography", "The art and science of drawing maps", "Cartography changed completely with satellite imaging.", "art"),
    ("archives", "archives", "A collection of historical records, or the place where they are kept", "The archives hold every file from the first survey.", "placeof"),
    ("scullery", "scullery", "A small room next to a kitchen for washing dishes", "The pots were stacked in the scullery.", "placeof"),
    ("archipelago", "archipelago", "A group of many islands, or a sea containing them", "The archipelago has over three hundred inhabited islands.", "geo"),
    ("asylum", "asylum", "Protection given by a state to a refugee from another country", "The family was granted asylum after a long hearing.", "law2"),
    ("etymology", "etymology", "The study of the origin and history of words", "Etymology shows that 'salary' comes from salt.", "study"),
    ("anthropology", "anthropology", "The study of human societies and their development", "Anthropology took her to three continents.", "study"),
    ("archaeology", "archaeology", "The study of the past through what people left behind", "Archaeology dated the mound to the Harappan period.", "study"),
    ("entomology", "entomology", "The study of insects", "Entomology was the only branch of biology that held him.", "study"),
    ("ethnology", "ethnology", "The study and comparison of different peoples and races", "Ethnology compares customs across neighbouring valleys.", "study"),
    ("ornithology", "ornithology", "The study of birds", "Ornithology is well served by amateur observers.", "study"),
    ("philology", "philology", "The study of language in its written historical sources", "Philology traced the manuscript to a single scribe.", "study"),
    ("psychology-ows", "psychology", "The study of the mind and of behaviour", "Psychology explains why a crowd behaves unlike its members.", "study"),
    ("sociology", "sociology", "The study of human society and social behaviour", "Sociology looks at the group, not the individual.", "study"),
    ("zoology", "zoology", "The branch of biology that deals with animals", "Zoology and botany share the first-year syllabus.", "study"),
    ("dermatology", "dermatology", "The branch of medicine dealing with the skin", "Dermatology has its own outpatient block.", "study"),
    ("ecology", "ecology", "The study of living things in relation to their surroundings", "Ecology links the fish catch to the mangrove.", "study"),
    ("geography", "geography", "The study of the earth's surface and of its peoples and resources", "Geography covers both the river and the people on it.", "study"),
    ("physiology", "physiology", "The study of how the bodies of living things work", "Physiology explains what training does to the heart.", "study"),
    ("philosophy", "philosophy", "The study of the nature of knowledge, reality and existence", "Philosophy asks what we can claim to know.", "study"),
    ("psephology", "psephology", "The study of elections and voting patterns", "Psephology turns a swing of two per cent into forty seats.", "study"),
    ("horticulture", "horticulture", "The art and science of growing fruit, flowers and vegetables", "Horticulture pays better here than wheat.", "study"),
    ("homicide", "homicide", "The killing of one person by another", "The charge was reduced from homicide to negligence.", "killing"),
    ("infanticide", "infanticide", "The killing of an infant", "The law treats infanticide separately from murder.", "killing"),
    ("suicide", "suicide", "The act of killing oneself deliberately", "The inquest recorded the death as suicide.", "killing2"),
    ("accomplice", "accomplice", "One who helps another to commit a crime", "The driver was charged as an accomplice.", "crime"),
    ("fugitive", "fugitive", "One who is running away, especially from the law", "The fugitive was traced to a border town.", "crime"),
    ("imposter", "imposter", "One who pretends to be somebody else in order to deceive", "The imposter had forged a whole set of papers.", "crime"),
    ("intestate", "intestate", "Having died without making a will", "He died intestate and the estate went to court.", "law3"),
    ("exonerate", "exonerate", "To declare somebody free of blame", "The inquiry exonerated the two junior clerks.", "law4"),
    ("abolish", "abolish", "To do away with a law, system or practice formally", "The state moved to abolish the levy.", "law4"),
    ("blasphemy", "blasphemy", "Speech or action that insults what is held sacred", "The passage was condemned as blasphemy.", "religion"),
    ("heresy", "heresy", "A belief that goes against accepted religious teaching", "His book was burnt as heresy.", "religion"),
    ("sacrilege", "sacrilege", "The treating of a sacred thing or place with disrespect", "Carving names on the shrine was sacrilege.", "religion"),
    ("secular", "secular", "Not concerned with religion or with a religious order", "The school follows a secular calendar.", "religion2"),
    ("theist", "theist", "One who believes that God exists", "A theist and an atheist can agree on the evidence and differ on the conclusion.", "belief"),
    ("atheism", "atheism", "The belief that God does not exist", "He arrived at atheism slowly and without bitterness.", "belief4"),
    ("fatalist", "fatalist", "One who believes that all events are fixed in advance and cannot be changed", "A fatalist sees no point in planning.", "belief"),
    ("hedonist", "hedonist", "One who believes that pleasure is the highest good", "The hedonist spent his inheritance in a year.", "belief5"),
    ("stoic", "stoic", "One who bears pain and hardship without complaint", "A stoic to the end, he never mentioned the pain.", "temper"),
    ("stoicism", "stoicism", "The practice of enduring hardship without showing feeling", "He took the news with complete stoicism.", "temper2"),
    ("iconoclast", "iconoclast", "One who attacks cherished beliefs and established institutions", "The iconoclast called the whole syllabus a waste.", "attack"),
    ("bigot", "bigot", "One who holds rigid opinions and will not hear any other view", "The bigot would not sit at the same table.", "attack2"),
    ("demagogue", "demagogue", "A leader who wins support by appealing to feeling rather than reason", "The demagogue spoke of enemies and never of costs.", "leader"),
    ("feminist", "feminist", "One who supports equal rights for women", "The feminist movement reshaped the labour laws.", "equal"),
    ("philogynist", "philogynist", "One who likes and respects women", "He was a philogynist in an age that was not.", "like"),
    ("philanderer", "philanderer", "A man who flirts with many women without serious intent", "The philanderer was the subject of every rumour.", "love2"),
    ("narcissist", "narcissist", "One who admires himself excessively", "The narcissist spoke of nothing but his own record.", "self2"),
    ("recluse", "recluse", "One who lives alone and avoids other people", "The recluse had not left the house in years.", "alone"),
    ("hermit", "hermit", "One who lives alone, usually for religious reasons", "The hermit kept a cave above the river.", "alone2"),
    ("dilettante", "dilettante", "One who dabbles in an art or subject without serious study", "As a dilettante he knew every painter's name and no painter's work.", "skill2"),
    ("martyr", "martyr", "One who suffers or dies for a belief or a cause", "The street is named after a martyr of the movement.", "sacrifice2"),
    ("cannibal", "cannibal", "One who eats human flesh", "Early accounts of the islands claimed the people were cannibals.", "eating"),
    ("carnivore", "carnivore", "An animal that feeds on flesh", "The tiger is the best-known carnivore of the region.", "eating2"),
    ("fauna", "fauna", "All the animals of a particular region or period", "The fauna of the valley is listed in the appendix.", "animal2"),
    ("aquatic", "aquatic", "Growing or living in or near water", "Aquatic plants had choked the whole tank.", "animal3"),
    ("indigenous", "indigenous", "Belonging naturally to a place; native to it", "The indigenous grasses survive the dry months.", "origin"),
    ("endemic", "endemic", "Regularly found in a particular place or among a particular people", "The disease is endemic to the coastal belt.", "origin2"),
    ("emigrant", "emigrant", "One who leaves his own country to settle in another", "As an emigrant he sent money home every month.", "move"),
    ("immigrant", "immigrant", "One who comes into a country in order to settle there", "The immigrant found work on the docks.", "move2"),
    ("expatriate", "expatriate", "One who lives outside his own country", "The expatriate returned after thirty years.", "move3"),
    ("itinerant", "itinerant", "Travelling from place to place to work", "An itinerant teacher visited four villages a week.", "wander"),
    ("spinster", "spinster", "An unmarried woman, especially one past the usual age of marriage", "The will left the shop to his sister, a spinster of sixty.", "marriage3"),
    ("polyandry", "polyandry", "The custom of a woman having more than one husband at a time", "Polyandry was recorded in a few hill communities.", "marriage"),
    ("maiden", "maiden", "Being the first of its kind", "The minister made her maiden speech on Tuesday.", "first"),
    ("insomnia", "insomnia", "The condition of being unable to sleep", "Insomnia had left him grey and short-tempered.", "sleep"),
    ("amnesia", "amnesia", "Loss of memory", "After the crash he suffered amnesia for three days.", "mind"),
    ("hallucination", "hallucination", "The experience of seeing or hearing something that is not there", "The fever brought on a hallucination of voices.", "mind2"),
    ("kleptomania", "kleptomania", "An uncontrollable urge to steal", "Kleptomania is treated as an illness, not a motive.", "mania"),
    ("megalomania", "megalomania", "An obsession with one's own power and greatness", "The memoir slides from confidence into megalomania.", "mania2"),
    ("hypochondriac", "hypochondriac", "One who worries constantly and needlessly about his health", "The hypochondriac read every symptom as his own.", "health"),
    ("hydrophobia", "hydrophobia", "An extreme fear of water", "Hydrophobia kept him off the ferry.", "fear"),
    ("apathy", "apathy", "A complete lack of interest or concern", "Voter apathy emptied the booths by noon.", "feeling2"),
    ("empathy", "empathy", "The ability to understand and share another's feelings", "Good nurses are chosen for empathy as much as for marks.", "feeling3"),
    ("fidelity", "fidelity", "Faithfulness, or exactness in reproducing something", "The translation keeps a strict fidelity to the original.", "loyal"),
    ("perseverance-ows", "perseverance", "Steady persistence in a course of action in spite of difficulty", "Perseverance, not talent, got her through the third attempt.", "effort2"),
    ("indefatigable", "indefatigable", "Incapable of being tired out", "An indefatigable organiser, she worked through both nights.", "effort3"),
    ("incentive", "incentive", "Something that encourages a person to act", "The subsidy was an incentive to sow early.", "push"),
    ("fastidious", "fastidious", "Very attentive to accuracy and detail; hard to please", "A fastidious editor queried every comma.", "careful"),
    ("affable", "affable", "Pleasant, friendly and easy to talk to", "The affable clerk explained the form twice.", "warm"),
    ("cordial", "cordial", "Warm and sincere in manner", "The meeting ended on cordial terms.", "warm2"),
    ("gregarious-ows", "gregarious", "Fond of company; living in groups", "A gregarious man, he knew everybody on the street.", "social"),
    ("effeminate", "effeminate", "Having qualities regarded as characteristic of women, said of a man", "The part calls for an effeminate manner and a hard heart.", "manner"),
    ("eccentric", "eccentric", "Behaving in a way others find strange", "The eccentric old man kept forty clocks.", "manner2"),
    ("extravagant", "extravagant", "Spending much more than is necessary", "An extravagant wedding emptied the account.", "money"),
    ("gullible", "gullible", "Easily deceived because too ready to believe", "A gullible buyer signed without reading.", "belief6"),
    ("credible", "credible", "Able to be believed; convincing", "The witness gave a credible account of the night.", "truth"),
    ("incredible", "incredible", "Too strange or extreme to be believed", "His story of the escape is frankly incredible.", "truth2"),
    ("authentic", "authentic", "Genuine; of undisputed origin", "The seal proved the document authentic.", "truth3"),
    ("obsolete-ows", "obsolete", "No longer in use because something newer has replaced it", "The software is obsolete and no longer patched.", "time4"),
    ("eternal", "eternal", "Lasting for ever", "The inscription promises eternal remembrance.", "time5"),
    ("extempore", "extempore", "Spoken or done without preparation", "She spoke extempore for twenty minutes.", "prepare"),
    ("notorious", "notorious", "Well known for something bad", "The crossing is notorious for accidents.", "fame"),
    ("epitome", "epitome", "A perfect example of a quality or type", "The building is the epitome of plain good sense.", "example"),
    ("exemplary", "exemplary", "Serving as a warning, or so good as to be a model", "The court imposed an exemplary fine.", "example2"),
    ("ineffable", "ineffable", "Too great to be described in words", "The relief of the verdict was ineffable.", "describe"),
    ("obscure", "obscure", "Not clearly expressed or easily understood", "The clause is obscure even to the lawyers.", "clear"),
    ("palpable", "palpable", "So intense as to be almost touched or felt", "There was a palpable tension in the hall.", "touch"),
    ("opaque", "opaque", "Not allowing light to pass through", "The window had been painted opaque.", "light"),
    ("translucent", "translucent", "Allowing light through but not a clear view", "Translucent panels lit the corridor without a view of it.", "light2"),
    ("transparent", "transparent", "Allowing light through so that things behind can be seen clearly", "A transparent sheet protects the map.", "light3"),
    ("audible", "audible", "Loud enough to be heard", "His reply was barely audible.", "cannot2"),
    ("edible", "edible", "Fit to be eaten", "Only two of the mushrooms are edible.", "cannot3"),
    ("brittle", "brittle", "Hard but easily broken", "Old plastic grows brittle in the sun.", "break"),
    ("neutral", "neutral", "Not supporting either side in a dispute", "The umpire must stay neutral.", "side"),
    ("alien", "alien", "Belonging to another place; strange and unfamiliar", "The custom felt alien to every visitor.", "strange"),
    ("cosmopolitan", "cosmopolitan", "Familiar with and at ease in many countries and cultures", "A cosmopolitan city keeps six kinds of restaurant on one street.", "world"),
    ("juxtapose", "juxtapose", "To place two things side by side for comparison", "The exhibition juxtaposes the two drafts.", "place3"),
    ("abdicate", "abdicate", "To give up a throne or a high office formally", "The king chose to abdicate rather than divide the country.", "give"),
    ("emissary", "emissary", "One sent on a mission as a representative", "An emissary carried the terms to the other camp.", "send"),
    ("itinerary", "itinerary", "A detailed plan of a journey", "The itinerary allows two nights in Jaipur.", "plan"),
    ("patrimony", "patrimony", "Property inherited from one's father or ancestors", "He sold the last of the patrimony to pay the fees.", "inherit"),
    ("wreath", "wreath", "Flowers and leaves arranged in a ring", "A wreath was laid at the memorial.", "object"),
]

# word id -> (times asked, rank out of 500) in that list
_FREQ = {"abdicate": (4, 139), "abolish": (5, 81), "accomplice": (5, 82), "acrophobia": (3, 219), "affable": (4, 140), "agnostic": (3, 224),
          "alien": (7, 39), "altruist": (9, 17), "amateur": (7, 40), "ambidextrous": (4, 141), "amnesia": (7, 41), "amnesty": (6, 60),
          "anarchist": (4, 143), "anarchy": (7, 42), "anonymous": (3, 231), "anthropology": (7, 43), "apathy": (4, 144), "apiary": (5, 84),
          "aquarium": (5, 85), "aquatic": (6, 61), "archaeology": (6, 62), "archipelago": (4, 145), "archives": (7, 44), "aristocracy": (9, 18),
          "ascetic": (8, 25), "asylum": (4, 146), "atheism": (5, 86), "atheist": (9, 19), "audible": (4, 147), "authentic": (4, 148),
          "autobiography": (4, 149), "autocracy": (5, 87), "aviary": (5, 88), "ballad": (5, 89), "bibliography": (5, 90), "bibliophile": (3, 244),
          "bigamy": (2, 480), "bigot": (5, 91), "bilingual": (2, 481), "biography": (6, 63), "blasphemy": (4, 150), "brittle": (5, 93),
          "bureaucracy-ows": (10, 5), "calligraphy": (9, 20), "cannibal": (10, 6), "carnivore": (4, 151), "carnivorous": (8, 26), "cartography": (8,
          27), "catalogue": (4, 152), "celibate": (2, 500), "chauffeur": (5, 94), "connoisseur": (9, 21), "cordial": (4, 155), "cosmopolitan": (5,
          95), "credible": (7, 45), "credulous": (4, 156), "curator": (4, 157), "cynic": (6, 64), "demagogue": (4, 158), "democracy": (5, 96),
          "dermatology": (4, 159), "dictatorship": (5, 97), "dilettante": (4, 160), "eccentric": (5, 98), "ecology": (4, 161), "edible": (4, 162),
          "effeminate": (7, 46), "egoist": (10, 8), "elegy": (10, 9), "emigrant": (6, 65), "emissary": (4, 163), "empathy": (4, 164), "endemic": (4,
          165), "entomology": (5, 99), "epicure": (5, 100), "epigraph": (4, 167), "epilogue": (10, 10), "epitaph": (10, 11), "epitome": (4, 168),
          "eternal": (4, 169), "ethnology": (5, 101), "etymology": (8, 28), "exemplary": (4, 170), "exonerate": (5, 102), "expatriate": (4, 171),
          "extempore": (6, 66), "extravagant": (5, 103), "fanatic": (6, 67), "fastidious": (10, 12), "fatalist": (9, 22), "fauna": (5, 104),
          "feminist": (7, 47), "fidelity": (4, 172), "fratricide": (5, 105), "fugitive": (4, 173), "genocide": (7, 48), "geography": (4, 174),
          "glutton": (5, 106), "gregarious-ows": (4, 175), "gullible": (7, 49), "hallucination": (4, 176), "hedonist": (4, 177), "herbivorous": (4,
          178), "heresy": (4, 179), "hermit": (6, 68), "homicide": (8, 29), "honorarium": (7, 50), "honorary": (4, 180), "horticulture": (4, 181),
          "hydrophobia": (4, 182), "hypochondriac": (5, 107), "hypocrite": (5, 108), "iconoclast": (8, 30), "illegible": (8, 31), "immigrant": (5,
          109), "imposter": (7, 51), "impregnable": (3, 300), "inaudible": (5, 110), "incentive": (4, 183), "incorrigible": (8, 32),
          "incredible": (5, 111), "indefatigable": (5, 112), "indelible": (3, 302), "indigenous": (5, 113), "ineffable": (5, 114), "inevitable": (10,
          13), "infallible": (14, 1), "infanticide": (4, 184), "insolvent": (7, 52), "insomnia": (8, 33), "interregnum": (3, 308), "intestate": (5,
          115), "invincible": (9, 23), "itinerant": (4, 185), "itinerary": (7, 53), "juxtapose": (4, 186), "kleptomania": (6, 69),
          "lexicographer": (5, 116), "maiden": (4, 187), "manuscript": (5, 117), "martyr": (5, 118), "matricide": (5, 119), "megalomania": (4, 189),
          "mercenary": (9, 24), "misanthrope": (12, 4), "misogynist": (14, 2), "monarchy": (7, 54), "mortuary": (5, 120), "mystic": (3, 325),
          "narcissist": (5, 121), "neutral": (4, 191), "notorious": (6, 70), "novice": (4, 192), "numismatist": (6, 71), "obituary": (7, 55),
          "obscure": (4, 193), "obsolete-ows": (8, 35), "ode": (6, 72), "oligarchy": (10, 14), "omnipotent": (3, 330), "omnipresent": (3, 331),
          "omniscient": (4, 194), "omnivorous": (5, 122), "opaque": (5, 123), "optimist": (10, 15), "ornithology": (7, 56), "orphan": (3, 338),
          "pacifist": (5, 124), "palpable": (4, 195), "panacea": (10, 16), "parable": (5, 125), "patricide": (8, 36), "patrimony": (4, 197),
          "pedant": (6, 73), "perseverance-ows": (4, 198), "pessimist": (4, 199), "philanderer": (4, 200), "philanthropist": (13, 3),
          "philatelist": (8, 37), "philistine": (5, 126), "philogynist": (4, 201), "philology": (6, 74), "philosophy": (4, 202), "physiology": (4,
          203), "plagiarism": (5, 127), "plagiarist": (3, 348), "plutocracy": (7, 57), "polyandry": (4, 204), "polygamy": (5, 128), "polyglot": (7,
          58), "prologue": (4, 205), "psephology": (4, 206), "pseudonym": (4, 207), "psychology-ows": (5, 129), "recluse": (5, 130),
          "red-tapism": (6, 75), "regicide": (5, 131), "sacrilege": (6, 77), "sanatorium": (5, 132), "sceptic": (3, 369), "scullery": (4, 208),
          "secular": (5, 133), "sinecure": (7, 59), "sociology": (4, 209), "soliloquy": (5, 134), "sonnet": (6, 78), "spinster": (4, 210),
          "stoic": (8, 38), "stoicism": (4, 211), "suicide": (5, 135), "sycophant": (3, 383), "theist": (4, 212), "theocracy": (6, 79),
          "translucent": (5, 136), "transparent": (5, 137), "versatile": (4, 214), "veteran": (3, 405), "wreath": (5, 138), "xenophobia": (6, 80),
          "zoology": (4, 215)}

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

# Confusable sets among the harvested words. These are what the exam actually tests, so each is allowed in as a
# distractor. A look-alike (shared opening or shared classical ending) is noted as one; anything else is
# named as the trap it is, so the note never claims a resemblance that is not there.
# Pairs that could be argued as near-equivalents are never put side by side as key and wrong option, and a confusable listed above is the only
# way a same-group word is allowed as a distractor.
_NEVER = {frozenset(p) for p in [("hypocrite", "sycophant"), ("pedant", "hypocrite"), ("sceptic", "cynic"), ("destitute", "insolvent"), ("optimist", "altruist"),
                                  ("illegible", "inaudible"), ("lethargy", "desuetude"), ("miser", "egoist"), ("ascetic", "pacifist"), ("novice", "amateur"),
                                  ("amateur", "novice"), ("incorrigible", "indelible"), ("sceptic", "agnostic"), ("agnostic", "mystic"), ("ascetic", "mystic")]}

_ALL = _O + _O2


def _note(i):
    """What the Black Book's ranking says about this word, where it lists it."""
    if i not in _FREQ: return None
    f, n = _FREQ[i]
    return f"Asked {f} time{'' if f == 1 else 's'} in the SSC papers counted by the Black Book list (rank {n} of 500)."


_CONF.update({
    "epilogue": ["prologue", "epigraph"], "prologue": ["epilogue", "epigraph"], "epigraph": ["epitaph", "epilogue"], "epitaph": ["epigraph", "obituary"],
    "elegy": ["ode", "sonnet"], "ode": ["elegy", "ballad"], "sonnet": ["ballad", "ode"], "ballad": ["sonnet", "elegy"],
    "biography": ["autobiography", "bibliography"], "bibliography": ["biography", "catalogue"], "autobiography": ["biography", "obituary"],
    "emigrant": ["immigrant", "expatriate"], "immigrant": ["emigrant", "expatriate"], "expatriate": ["emigrant", "immigrant"],
    "translucent": ["transparent", "opaque"], "transparent": ["translucent", "opaque"], "opaque": ["translucent", "transparent"],
    "oligarchy": ["aristocracy", "autocracy"], "aristocracy": ["oligarchy", "plutocracy"], "monarchy": ["oligarchy", "autocracy"],
    "democracy": ["dictatorship", "monarchy"], "dictatorship": ["autocracy", "democracy"], "bureaucracy-ows": ["red-tapism", "aristocracy"],
    "red-tapism": ["bureaucracy-ows", "sinecure"], "sinecure": ["honorarium", "red-tapism"],
    "autocracy": ["oligarchy", "monarchy"], "plutocracy": ["aristocracy", "oligarchy"], "theocracy": ["autocracy", "monarchy"],
    "anarchy": ["anarchist", "oligarchy"], "anarchist": ["anarchy", "atheism"],
    "theist": ["atheist", "fatalist"], "atheism": ["atheist", "agnostic"], "fatalist": ["theist", "hedonist"],
    "atheist": ["atheism", "theist"], "agnostic": ["atheism", "sceptic"],
    "homicide": ["infanticide", "patricide"], "infanticide": ["homicide", "matricide"], "suicide": ["homicide", "genocide"],
    "patricide": ["matricide", "homicide"], "genocide": ["homicide", "regicide"],
    "insomnia": ["insomniac", "amnesia"], "insomniac": ["insomnia", "somnambulist"], "amnesia": ["insomnia", "hallucination"],
    "kleptomania": ["megalomania", "hallucination"], "megalomania": ["kleptomania", "narcissist"],
    "credible": ["incredible", "authentic"], "incredible": ["credible", "ineffable"], "authentic": ["credible", "indigenous"],
    "audible": ["edible", "inaudible"], "edible": ["audible", "palpable"], "inaudible": ["audible", "illegible"],
    "apathy": ["empathy", "stoicism"], "empathy": ["apathy", "fidelity"],
    "recluse": ["misanthrope", "ascetic"], "hermit": ["ascetic", "misanthrope"],
    "stoic": ["stoicism", "ascetic"], "stoicism": ["stoic", "apathy"],
    "itinerant": ["itinerary", "nomad"], "itinerary": ["itinerant", "catalogue"],
    "honorary": ["honorarium", "sinecure"], "honorarium": ["honorary", "sinecure"],
    "cannibal": ["carnivore", "carnivorous"], "carnivore": ["carnivorous", "cannibal"], "carnivorous": ["carnivore", "herbivorous"],
    "fauna": ["aquatic", "amphibian"], "aquatic": ["amphibian", "fauna"], "amphibian": ["aquatic", "fauna"],
    "entomology": ["etymology", "ethnology"], "etymology": ["entomology", "philology"], "ethnology": ["entomology", "anthropology"],
    "anthropology": ["ethnology", "archaeology"], "archaeology": ["anthropology", "ethnology"], "philology": ["etymology", "psephology"],
    "sociology": ["anthropology", "psephology"], "psephology": ["sociology", "philology"], "zoology": ["entomology", "ecology"],
    "ecology": ["zoology", "ethnology"], "physiology": ["psychology-ows", "ecology"], "psychology-ows": ["physiology", "philosophy"],
    "philosophy": ["psychology-ows", "philology"], "dermatology": ["physiology", "ecology"],
    "calligraphy": ["cartography", "geography"], "cartography": ["calligraphy", "geography"], "geography": ["cartography", "geology"] if False else ["cartography", "calligraphy"],
    "plagiarism": ["plagiarist", "pseudonym"], "plagiarist": ["plagiarism", "imposter"],
    "philanderer": ["philogynist", "misogynist"], "philogynist": ["philanderer", "misogynist"], "misogynist": ["philogynist", "misanthrope"],
    "philanthropist": ["philogynist", "misanthrope"],
    "narcissist": ["egoist", "hedonist"], "egoist": ["narcissist", "altruist"], "hedonist": ["epicure", "fatalist"], "epicure": ["hedonist", "glutton"],
    "indigenous": ["endemic", "alien"], "endemic": ["indigenous", "epidemic"] if False else ["indigenous", "alien"], "alien": ["indigenous", "expatriate"],
    "obsolete-ows": ["eternal", "ephemeral"] if False else ["eternal", "obscure"], "eternal": ["obsolete-ows", "ineffable"],
    "exemplary": ["epitome", "eternal"], "epitome": ["exemplary", "authentic"],
    "demagogue": ["iconoclast", "fanatic"], "iconoclast": ["demagogue", "bigot"], "bigot": ["iconoclast", "fanatic"], "fanatic": ["bigot", "demagogue"],
    "abdicate": ["abolish", "exonerate"], "abolish": ["abdicate", "exonerate"], "exonerate": ["abolish", "amnesty"], "amnesty": ["exonerate", "asylum"],
    "asylum": ["amnesty", "archives"], "archives": ["catalogue", "asylum"], "scullery": ["granary", "apiary"],
    "lexicographer": ["curator", "philologist"] if False else ["curator", "cartography"], "curator": ["lexicographer", "chauffeur"],
    "manuscript": ["catalogue", "bibliography"], "catalogue": ["bibliography", "manuscript"], "pseudonym": ["anonymous", "plagiarism"],
    "anonymous": ["pseudonym", "unanimous"], "unanimous": ["anonymous", "neutral"],
    "perseverance-ows": ["indefatigable", "stoicism"], "indefatigable": ["perseverance-ows", "invincible"],
    "hypochondriac": ["hallucination", "insomniac"], "hallucination": ["amnesia", "hypochondriac"],
    "blasphemy": ["sacrilege", "heresy"], "heresy": ["blasphemy", "sacrilege"], "sacrilege": ["blasphemy", "heresy"], "secular": ["ascetic", "mystic"],
    "intestate": ["patrimony", "exonerate"], "patrimony": ["intestate", "legacy"] if False else ["intestate", "amnesty"],
    "fugitive": ["imposter", "accomplice"], "imposter": ["fugitive", "plagiarist"], "accomplice": ["fugitive", "imposter"],
    "effeminate": ["eccentric", "feminist"], "eccentric": ["effeminate", "philistine"], "feminist": ["philogynist", "effeminate"],
    "affable": ["cordial", "gregarious-ows"] if False else ["cordial", "amiable"] if False else ["gregarious-ows", "cordial"],
    "cordial": ["affable", "gregarious-ows"], "gregarious-ows": ["affable", "cordial"],
    "extravagant": ["spendthrift", "miser"], "spendthrift": ["extravagant", "miser"], "miser": ["spendthrift", "extravagant"],
    "notorious": ["eminent", "obscure"] if False else ["obscure", "eccentric"], "obscure": ["notorious", "ineffable"],
    "neutral": ["pacifist", "unanimous"], "pacifist": ["neutral", "altruist"],
    "cosmopolitan": ["polyglot", "bilingual"], "polyglot": ["cosmopolitan", "bilingual"], "bilingual": ["polyglot", "cosmopolitan"],
    "hydrophobia": ["claustrophobia", "acrophobia"], "claustrophobia": ["agoraphobia", "hydrophobia"],
    "polyandry": ["polygamy", "monogamy"], "polygamy": ["polyandry", "bigamy"], "monogamy": ["polyandry", "bigamy"],
    "spinster": ["celibate", "recluse"], "celibate": ["spinster", "ascetic"],
    "ineffable": ["incredible", "palpable"], "palpable": ["audible", "ineffable"],
    "martyr": ["fanatic", "pacifist"], "brittle": ["opaque", "palpable"], "juxtapose": ["abdicate", "abolish"],
    "maiden": ["novelty", "unprecedented"], "fidelity": ["empathy", "perseverance-ows"], "incentive": ["panacea", "amnesty"],
    "archipelago": ["aviary", "granary"], "emissary": ["imposter", "mercenary"], "mercenary": ["emissary", "sycophant"],
    "wreath": ["epitaph", "epigraph"], "dilettante": ["amateur", "connoisseur"], "amateur": ["dilettante", "novice"],
    "gullible": ["credulous", "sceptic"] if False else ["sceptic", "cynic"], "credulous": ["sceptic", "gullible"] if False else ["sceptic", "cynic"],
    "chauffeur": ["curator", "mercenary"], "horticulture": ["ecology", "zoology"], "extempore": ["impromptu"] if False else ["soliloquy", "extravagant"],
    "soliloquy": ["parable", "extempore"], "parable": ["ballad", "soliloquy"], "atheism-x": [],
})
# Pairs that are too close to set against each other: one could be argued as the answer too.
_NEVER |= {frozenset(p) for p in [("obscure", "opaque"), ("recluse", "hermit"), ("affable", "cordial"), ("gullible", "credulous"),
                                   ("blasphemy", "sacrilege"), ("heresy", "blasphemy"), ("abolish", "abdicate"), ("stoicism", "apathy"),
                                   ("eternal", "ineffable"), ("notorious", "obscure"), ("amnesty", "exonerate"), ("carnivore", "carnivorous"),
                                   ("perseverance-ows", "indefatigable"), ("aquatic", "amphibian"), ("fatalist", "theist")]}


WORDS = [word(i, w, "ows", m, ex=e, note=_note(i)) for i, w, m, e, g in _ALL]
_W = {i: w for i, w, m, e, g in _ALL}
_M = {i: m for i, w, m, e, g in _ALL}
_GR = {i: g for i, w, m, e, g in _ALL}
_HI = {i for i in _FREQ if _FREQ[i][0] >= 7}        # the heaviest repeaters earn a rule citation of their own
_RARE = {"desuetude", "interregnum", "sycophant", "polymath", "numismatist", "philistine", "pedant", "plutocracy", "theocracy", "nostalgia", "regicide",
         "credulous", "epicure", "connoisseur", "sanatorium", "apiary", "amnesty", "mystic", "ascetic", "insatiable", "indelible"}
_STEM = "Select the word that can be used as a substitute for the given group of words.\n"
_ids = [i for i, *_ in _ALL]


_ROOTS = ("logy", "graphy", "cracy", "cide", "phobia", "gamy", "mania", "nomy", "archy", "ism", "ist", "ible", "able", "ate")


def _alike(a, b):
    """True when two words would be confused by eye: a shared opening or a shared classical ending."""
    x, y = _W[a].lower(), _W[b].lower()
    if x[:4] == y[:4]: return True
    return any(x.endswith(r) and y.endswith(r) for r in _ROOTS)


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
                wrong[ltr] = mistake(f"'{_W[oid]}' looks like the right word but means {_lc(_M[oid])}." if _alike(wid, oid)
                                     else f"'{_W[oid]}' is the trap set beside it here: it means {_lc(_M[oid])}.")
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
