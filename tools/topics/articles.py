"""Articles: a / an / the and the places where no article belongs. Seed tier: no article question appeared in the three papers
analysed so far, so this topic is built from the rules and drilled, not from a filed question."""
from bank import mistake, ruled_out, q

TOPIC = "articles"
TIER = "seed"
PREFIX = "ar"

NODES = {
    "q-ar-ain": {"short": "a / an", "label": "a or an", "kind": "qtype", "parent": TOPIC, "order": 1,
                 "summary": "The choice follows the sound the next word starts with, not its spelling.", "links": []},
    "q-ar-the": {"short": "the", "label": "When 'the' is needed", "kind": "qtype", "parent": TOPIC, "order": 2,
                 "summary": "Superlatives, one-of-a-kind things, rivers, ranges, oceans and ordinals take 'the'.", "links": []},
    "q-ar-none": {"short": "No article", "label": "Where no article belongs", "kind": "qtype", "parent": TOPIC, "order": 3,
                  "summary": "Abstract and uncountable nouns in general, meals, languages, and most proper nouns take none.", "links": []},
}

RULES = [
    {"id": "ar-r1", "node": "q-ar-ain", "text": "Use 'an' before a vowel SOUND and 'a' before a consonant sound. Spelling does not decide it: an hour, an MLA, an honest man; a university, a one-rupee coin, a European.",
     "ok": "An hour, a university, an MP.", "bad": "A hour, an university, a MP."},
    {"id": "ar-r2", "node": "q-ar-the", "text": "'The' goes before a superlative, an ordinal, a thing there is only one of, and before rivers, seas, oceans, mountain ranges, deserts and groups of islands. Single mountains and single lakes take none.",
     "ok": "The tallest boy, the Ganga, the Himalayas, the sun.", "bad": "Tallest boy, Ganga is holy, Himalayas are high."},
    {"id": "ar-r3", "node": "q-ar-the", "text": "'The' also marks a noun already known from the situation or mentioned before, and it makes a singular noun stand for its whole class: the tiger is disappearing.",
     "ok": "I bought a book. The book was torn.", "bad": "I bought a book. A book was torn."},
    {"id": "ar-r4", "node": "q-ar-none", "text": "No article before an abstract or uncountable noun used in general (honesty, advice, information, furniture), before meals, languages, games, most diseases, and before a proper noun; add 'the' only when the noun is narrowed down.",
     "ok": "Honesty pays. He plays cricket after lunch.", "bad": "The honesty pays. He plays the cricket after the lunch."},
    {"id": "ar-r5", "node": "q-ar-none", "text": "In 'the more ... the more' and 'the + adjective' for a whole class (the poor, the blind), 'the' is required. One article serves two nouns of the same person or thing, but two are needed for two different ones.",
     "ok": "The more he earns, the less he saves. A black and a white shirt (two shirts).", "bad": "More he earns, less he saves."},
]

METHODS = {
    "q-ar-ain": {"cue": "A blank before a noun or adjective, with 'a' and 'an' among the options.",
                 "standard": "Say the next word aloud. If it begins with a vowel sound, use 'an'; otherwise 'a'.",
                 "fast": "Test the first sound, not the first letter: h in 'hour' is silent, u in 'university' sounds like 'yoo'.",
                 "eliminate": "Drop 'the' and the blank option first if the noun is being introduced for the first time.",
                 "traps": ["Words beginning with a silent h (hour, honour, heir) take 'an'.", "Words beginning with a 'yoo' or 'wun' sound (university, European, one) take 'a'.",
                           "Single letters and abbreviations go by sound: an MLA, an FIR, a UPSC notification."],
                 "rules": ["ar-r1"], "tech": ["read-whole"]},
    "q-ar-the": {"cue": "A blank before a superlative, an ordinal, a river or range, or a noun mentioned earlier.",
                 "standard": "Ask whether the noun is one of a kind, already known, or the best or first of something. If yes, use 'the'.",
                 "fast": "Superlative or ordinal in the phrase means 'the'.",
                 "eliminate": "If the noun is being met for the first time and is countable and singular, 'the' is usually wrong.",
                 "traps": ["Rivers and ranges take 'the' but single peaks and lakes do not.", "'The' before a second mention is easy to drop in a long sentence."],
                 "rules": ["ar-r2", "ar-r3"], "tech": ["read-whole"]},
    "q-ar-none": {"cue": "A blank before an abstract noun, a meal, a language or a game, with 'no article' among the options.",
                  "standard": "Ask whether the noun is being used in general. If it is, leave it bare.",
                  "fast": "Abstract noun used generally, meal, language or game: no article.",
                  "eliminate": "Cross out 'the' unless the sentence narrows the noun down with a phrase or clause.",
                  "traps": ["'Advice', 'information', 'furniture' and 'luggage' are uncountable and take no 'a'.", "'The' returns as soon as the noun is specified: the advice he gave me."],
                  "rules": ["ar-r4", "ar-r5"], "tech": ["read-whole"]},
}

REFS = []
WORDS = []
_F = "Select the most appropriate option to fill in the blank.\n"
_S = "Find the part of the sentence that contains an error:\n"
_I = "Choose the most suitable option to replace the highlighted part of the sentence:\n"


def practice_items():
    return [
        q("q-ar-ain", "fill", _F + "The meeting lasted ___ hour and a half.", ["a", "an", "the", "No article"], "b",
          "'Hour' begins with a vowel sound because the h is silent, so it takes 'an'.",
          {"a": mistake("'A hour' goes by the letter h instead of the sound; the h in 'hour' is not pronounced."),
           "c": ruled_out("'The hour' would point to one particular hour already known, which the sentence does not."),
           "d": ruled_out("A singular countable noun being introduced needs an article.")}, rules=["ar-r1"], uid="ar-p01", tech=["read-whole"]),
        q("q-ar-ain", "fill", _F + "She has joined ___ university in Pune.", ["an", "a", "the", "No article"], "b",
          "'University' begins with a 'yoo' sound, which is a consonant sound, so it takes 'a'.",
          {"a": mistake("'An university' goes by the vowel letter u; the word is pronounced 'yoo-niversity'."),
           "c": ruled_out("'The university' would mean a particular one already known to the listener."),
           "d": ruled_out("A singular countable noun needs an article here.")}, rules=["ar-r1"], uid="ar-p02", tech=["read-whole"]),
        q("q-ar-ain", "fill", _F + "He filed ___ FIR at the police station.", ["a", "an", "the", "No article"], "b",
          "The abbreviation FIR is read as 'ef-eye-ar', which begins with a vowel sound, so it takes 'an'.",
          {"a": mistake("'A FIR' goes by the letter F; read aloud, the letter begins with the vowel sound 'ef'."),
           "c": ruled_out("'The FIR' would refer to one already mentioned; here it is being filed for the first time."),
           "d": ruled_out("A singular countable noun needs an article here.")}, rules=["ar-r1"], uid="ar-p03", tech=["read-whole"]),
        q("q-ar-the", "fill", _F + "He is ___ tallest boy in the class.", ["a", "an", "the", "No article"], "c",
          "A superlative singles out one person, so it takes 'the'.",
          {"a": ruled_out("'A tallest' is impossible: a superlative cannot be one of several."),
           "b": ruled_out("'An tallest' is wrong in both the article and the sound."),
           "d": mistake("Leaving out the article before a superlative is a common slip; English requires 'the'.")}, rules=["ar-r2"], uid="ar-p04", tech=["read-whole"]),
        q("q-ar-the", "fill", _F + "___ Ganga rises in the Himalayas.", ["A", "An", "The", "No article"], "c",
          "Rivers take 'the', as do mountain ranges, seas and oceans.",
          {"a": ruled_out("'A Ganga' would make the river one of several of that name."),
           "b": ruled_out("'An Ganga' is wrong in both the article and the sound."),
           "d": mistake("Dropping the article before a river name is common in speech, but a river takes 'the'.")}, rules=["ar-r2"], uid="ar-p05", tech=["read-whole"]),
        q("q-ar-the", "spot-error", _S + "I bought a dictionary yesterday / but dictionary was missing / twenty pages / in the middle.",
          ["I bought a dictionary yesterday", "but dictionary was missing", "twenty pages", "in the middle"], "b",
          "At the second mention the noun is already known, so it needs 'the dictionary'.",
          {"a": ruled_out("'A dictionary' is right for the first mention of a countable noun."),
           "c": ruled_out("'Twenty pages' is a plural count and needs no article."),
           "d": ruled_out("'In the middle' is a fixed phrase and is correct.")}, rules=["ar-r3"], uid="ar-p06", tech=["read-whole"]),
        q("q-ar-none", "fill", _F + "___ honesty is the best policy in the long run.", ["A", "An", "The", "No article"], "d",
          "An abstract noun used in general takes no article.",
          {"a": ruled_out("'A honesty' is impossible: honesty is uncountable."),
           "b": ruled_out("'An honesty' is impossible for the same reason."),
           "c": mistake("'The honesty' would point to one particular person's honesty, which the sentence does not do.")}, rules=["ar-r4"], uid="ar-p07", tech=["read-whole"]),
        q("q-ar-none", "spot-error", _S + "He gave me / a very useful advice / about the examination / last evening.",
          ["He gave me", "a very useful advice", "about the examination", "last evening"], "b",
          "'Advice' is uncountable, so it cannot take 'a'; it should be 'very useful advice' or 'a very useful piece of advice'.",
          {"a": ruled_out("'He gave me' is a correct main clause."),
           "c": ruled_out("'About the examination' points to a known examination and is correct."),
           "d": ruled_out("'Last evening' is a correct phrase of time.")}, rules=["ar-r4"], uid="ar-p08", tech=["read-whole"]),
        q("q-ar-none", "improve", _I + "[[The more you read the more]] you understand.",
          ["The more you read, the more", "More you read, more", "The more you read, more", "More you read, the more"], "a",
          "Both halves of the 'the more ... the more' pattern keep 'the'.",
          {"b": mistake("Dropping both articles is the commonest form of this error; the pattern needs 'the' twice."),
           "c": ruled_out("The second half has lost its 'the'."),
           "d": ruled_out("The first half has lost its 'the'.")}, rules=["ar-r5"], uid="ar-p09", tech=["read-whole"]),
        q("q-ar-none", "fill", _F + "We had ___ lunch at a small place near the office.", ["a", "the", "No article", "an"], "c",
          "Names of meals take no article when they mean the meal in general.",
          {"a": mistake("'A lunch' is used only when the meal is described as an event, as in 'a lunch in his honour'."),
           "b": mistake("'The lunch' would point to one particular meal already known."),
           "d": ruled_out("'An lunch' is wrong in both the article and the sound.")}, rules=["ar-r4"], uid="ar-p10", tech=["read-whole"]),
    ]


PYQS = []
