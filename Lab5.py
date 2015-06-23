__author__ = 'rumesh'
import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park"
P -> "in" | "on" | "by" | "with"
""")

rd_parser = nltk.RecursiveDescentParser(grammar)

senttext = "Mary saw Bob"
sentlist = senttext.split()
treelist = rd_parser.parse(sentlist)
# for tree in treelist:
#     print tree
#
# sent2list = "John saw the man in the park with a telescope".split()
# for tree in rd_parser.parse(sent2list):
#     print tree


groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked" | "shot"
NP -> "John" | "Mary" | "Bob" | "I" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park" | "elephant" | "pajamas"
P -> "in" | "on" | "by" | "with"
""")

sr_parse = nltk.ShiftReduceParser(groucho_grammar)
sent3 = "Mary saw a dog".split()
print sr_parse.parse(sent3)