"""Conditional sentences. Seed tier: no conditional question appeared in the three papers analysed so far, but
Plinth to Paramount gives the pattern a chapter of its own and SSC papers test it as a fill-in or a spot-the-error."""
from bank import mistake, ruled_out, q

TOPIC = "conditionals"
TIER = "seed"
PREFIX = "cd"

NODES = {
    "q-cd-type": {"short": "Which type", "label": "The tense pair in an if-sentence", "kind": "qtype", "parent": TOPIC, "order": 1,
                  "summary": "Each kind of condition fixes both halves: real, likely, unlikely or impossible.", "links": []},
    "q-cd-wish": {"short": "Wish / as if", "label": "Wish, as if, if only", "kind": "qtype", "parent": TOPIC, "order": 2,
                  "summary": "These take the past form for the present and 'were' for every subject.", "links": []},
    "q-cd-unless": {"short": "Unless", "label": "Unless, in case, provided", "kind": "qtype", "parent": TOPIC, "order": 3,
                    "summary": "'Unless' already means 'if not', so a second negative is wrong.", "links": []},
}

RULES = [
    {"id": "cd-r1", "node": "q-cd-type", "text": "A general truth takes the present in both halves: If you heat ice, it melts. A likely future takes the present in the if-half and will in the other: If it rains, we will stop. Never put 'will' in the if-half.",
     "ok": "If it rains tomorrow, we will cancel the match.", "bad": "If it will rain tomorrow, we will cancel the match."},
    {"id": "cd-r2", "node": "q-cd-type", "text": "For something unlikely or imaginary now, use the past in the if-half and would + base verb in the other: If I had a car, I would drive. 'Were' is used for every subject: If I were you.",
     "ok": "If I were the minister, I would publish the file.", "bad": "If I was the minister, I will publish the file."},
    {"id": "cd-r3", "node": "q-cd-type", "text": "For something that did not happen, use the past perfect in the if-half and would have + past participle in the other: If I had known, I would have come. Never 'would have' in the if-half.",
     "ok": "If he had left earlier, he would have caught the train.", "bad": "If he would have left earlier, he would have caught the train."},
    {"id": "cd-r4", "node": "q-cd-wish", "text": "After wish, if only and as if, the verb steps one tense back: a present wish takes the past, a past regret takes the past perfect, and 'were' is used for every subject.",
     "ok": "I wish I were taller. He talks as if he were the owner.", "bad": "I wish I am taller. He talks as if he is the owner."},
    {"id": "cd-r5", "node": "q-cd-unless", "text": "'Unless' means 'if not', so the clause after it stays positive. 'Lest' is followed by should, and 'in case' and 'provided' take the present.",
     "ok": "You will fail unless you work. Take an umbrella in case it rains.", "bad": "You will fail unless you do not work."},
]

METHODS = {
    "q-cd-type": {"cue": "An if-clause with a blank in one of the two halves.",
                  "standard": "Read the half that is complete, name the type from it, then fill the other half with the form that type requires.",
                  "fast": "Past in the if-half means 'would' in the other; past perfect means 'would have'.",
                  "eliminate": "Cross out any option that puts 'will' or 'would have' inside the if-half.",
                  "traps": ["'If I will' and 'if he would have', which are never right.", "'Was' instead of 'were' in an imaginary condition.",
                            "A mixed sentence where the two halves belong to different types."],
                  "rules": ["cd-r1", "cd-r2", "cd-r3"], "tech": ["eliminate-pair", "read-whole"]},
    "q-cd-wish": {"cue": "wish, if only or as if, followed by a blank.",
                  "standard": "Step the verb one tense back from the time meant, and use 'were' for every subject.",
                  "fast": "A wish about now takes the past; a wish about the past takes 'had'.",
                  "eliminate": "Drop the present forms: after 'wish' they are always wrong.",
                  "traps": ["'I wish I am' and 'as if he is'.", "'Was' where 'were' is required."],
                  "rules": ["cd-r4"], "tech": ["back-substitute"]},
    "q-cd-unless": {"cue": "unless, lest, in case or provided in the sentence.",
                    "standard": "Replace 'unless' with 'if not' in your head and see whether the sentence still makes sense.",
                    "fast": "No second 'not' after 'unless'; 'should' after 'lest'.",
                    "eliminate": "Remove options that double the negative.",
                    "traps": ["A negative verb after 'unless'.", "'Lest ... not', which repeats the negative already in 'lest'."],
                    "rules": ["cd-r5"], "tech": ["read-whole"]},
}

REFS = []
WORDS = []
_F = "Select the most appropriate option to fill in the blank.\n"
_S = "Find the part of the sentence that contains an error:\n"


def practice_items():
    return [
        q("q-cd-type", "fill", _F + "If it ___ tomorrow, the match will be called off.", ["will rain", "rains", "rained", "would rain"], "b",
          "A likely future takes the present tense in the if-half and 'will' in the other half.",
          {"a": mistake("'If it will rain' puts 'will' inside the if-half, which English never does."),
           "c": mistake("The past 'rained' would make the condition imaginary, but the other half has 'will', not 'would'."),
           "d": ruled_out("'Would rain' belongs to an imaginary condition and clashes with 'will be called off'.")},
          rules=["cd-r1"], uid="cd-p01", tech=["eliminate-pair"]),
        q("q-cd-type", "fill", _F + "If I ___ you, I would accept the transfer.", ["was", "were", "am", "will be"], "b",
          "An imaginary condition uses 'were' for every subject, and the other half has 'would'.",
          {"a": mistake("'If I was you' is common in speech, but the imaginary condition takes 'were'."),
           "c": ruled_out("The present 'am' cannot go with 'would accept'."),
           "d": ruled_out("'Will be' puts a future form inside the if-half.")},
          rules=["cd-r2"], uid="cd-p02", tech=["eliminate-pair"]),
        q("q-cd-type", "fill", _F + "If she had revised the chapter, she ___ the question.", ["would answer", "will answer", "would have answered", "had answered"], "c",
          "The if-half is in the past perfect, so the other half takes 'would have' plus the past participle.",
          {"a": mistake("'Would answer' belongs with a simple past in the if-half, not a past perfect."),
           "b": ruled_out("'Will answer' cannot follow a past perfect condition."),
           "d": ruled_out("Repeating 'had answered' leaves the sentence without a result clause.")},
          rules=["cd-r3"], uid="cd-p03", tech=["eliminate-pair"]),
        q("q-cd-type", "spot-error", _S + "If he would have informed us / about the change in time, / we could have arranged / another vehicle.",
          ["If he would have informed us", "about the change in time,", "we could have arranged", "another vehicle"], "a",
          "The if-half of an impossible condition takes the past perfect: 'If he had informed us'. 'Would have' never goes inside the if-clause.",
          {"b": ruled_out("'About the change in time' is a correct prepositional phrase."),
           "c": ruled_out("'We could have arranged' is a correct result clause for this type."),
           "d": ruled_out("'Another vehicle' is the object and holds no error.")},
          rules=["cd-r3"], uid="cd-p04", tech=["read-whole"]),
        q("q-cd-wish", "fill", _F + "I wish I ___ how to swim.", ["know", "knew", "have known", "will know"], "b",
          "A wish about the present steps the verb back to the past.",
          {"a": mistake("'Wish I know' keeps the present tense, which 'wish' does not allow."),
           "c": ruled_out("'Have known' is the present perfect and does not follow 'wish' here."),
           "d": ruled_out("'Will know' puts a future form after 'wish'.")},
          rules=["cd-r4"], uid="cd-p05", tech=["back-substitute"]),
        q("q-cd-wish", "fill", _F + "He behaves as if he ___ the owner of the shop.", ["is", "was", "were", "will be"], "c",
          "After 'as if' the verb steps back and takes 'were' for every subject.",
          {"a": mistake("'As if he is' keeps the present, which the pattern does not allow."),
           "b": mistake("'Was' is heard in speech, but 'as if' takes 'were' whatever the subject."),
           "d": ruled_out("'Will be' puts a future form after 'as if'.")},
          rules=["cd-r4"], uid="cd-p06", tech=["back-substitute"], rare=True),
        q("q-cd-wish", "fill", _F + "If only she ___ told us earlier, we could have helped.", ["has", "had", "would have", "have"], "b",
          "'If only' about the past takes the past perfect: 'if only she had told us'.",
          {"a": ruled_out("'Has told' is the present perfect and clashes with 'could have helped'."),
           "c": mistake("'Would have told' in the if-half is the same error as 'if he would have'."),
           "d": ruled_out("'Have told' does not agree with the singular 'she'.")},
          rules=["cd-r4", "cd-r3"], uid="cd-p07", tech=["back-substitute"]),
        q("q-cd-unless", "fill", _F + "You will not be allowed in ___ you carry the pass.", ["unless", "until", "if not", "lest"], "a",
          "'Unless' means 'if not', which is exactly what the sentence needs before a positive verb.",
          {"b": mistake("'Until' is about time, not about a condition."),
           "c": mistake("'If not you carry' is not the English word order; 'if you do not carry' would be, but that is not the option."),
           "d": ruled_out("'Lest' is followed by 'should' and expresses a precaution.")},
          rules=["cd-r5"], uid="cd-p08", tech=["read-whole"]),
        q("q-cd-unless", "spot-error", _S + "The guard warned us / that we would be fined / unless we did not move / the car at once.",
          ["The guard warned us", "that we would be fined", "unless we did not move", "the car at once"], "c",
          "'Unless' already carries the negative, so 'unless we did not move' says the opposite of what is meant; it should be 'unless we moved'.",
          {"a": ruled_out("'The guard warned us' is a correct main clause."),
           "b": ruled_out("'That we would be fined' is correct reported speech after a past verb."),
           "d": ruled_out("'The car at once' is the object with a phrase of time.")},
          rules=["cd-r5"], uid="cd-p09", tech=["read-whole"]),
        q("q-cd-type", "fill", _F + "If you heat water to a hundred degrees, it ___.", ["will boil", "boils", "boiled", "would boil"], "b",
          "A general truth takes the present tense in both halves.",
          {"a": mistake("'Will boil' turns a standing fact into a single future event; a general truth takes the present."),
           "c": ruled_out("The past 'boiled' does not state a general truth."),
           "d": ruled_out("'Would boil' belongs to an imaginary condition.")},
          rules=["cd-r1"], uid="cd-p10", tech=["eliminate-pair"]),
    ]


PYQS = []
