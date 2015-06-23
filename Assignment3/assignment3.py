__author__ = 'rumesh'

import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> D N
VP -> V | V NP | V NP PP
PP -> P NP
V -> "saw" | "chased" | "slept" | "barked"
D -> "a" | "the"
N -> "boy" | "girl" | "dog" | "cat" | "garden"
P -> "with" | "into" | "from" | "at"
""")

rd_parser = nltk.RecursiveDescentParser(grammar)

# sentlist = "the boy chased a dog".split()
sentlist = "the fierce dog saw a cat".split()
treelist = rd_parser.parse(sentlist)
for tree in treelist:
    print tree