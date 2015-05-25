__author__ = 'rumesh'
#python version 3.4

import nltk

grammar = nltk.data.load('file:Q1B.cfg')

parser = nltk.RecursiveDescentParser(grammar)

sentence = "the three tall black dogs barked"
sent = sentence.split()
trees = parser.parse(sent)

print("Sentence: "+ sentence)
print("Parse tree(s) for the above sentence")
for tree in trees:
	print(tree)
	tree.draw()
	
# sample texts
# the girl with long hair slept
# the fierce dog saw a cat
# the three tall black dogs barked
# 