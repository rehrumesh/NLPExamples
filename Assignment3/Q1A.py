#!/usr/bin/python

__author__ = 'rumesh'
#python version 3.4

import nltk

grammar = nltk.data.load('file:Q1A.cfg')

parser = nltk.RecursiveDescentParser(grammar)

sentence = "the boy chased a dog"
sent = sentence.split()
trees = parser.parse(sent)

print("Sentence: "+ sentence)
print("Parse tree(s) for the above sentence")
for tree in trees:
	print(tree)
	tree.draw()

