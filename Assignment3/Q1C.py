#!/usr/bin/python

__author__ = 'rumesh'
#python version 3.4

import nltk
from nltk import load_parser

grammar = load_parser('file:Q1C.fcfg')
sentence = "the boy slept the cat".split()

trees = grammar.parse(sentence)

treeslist = list(trees)
if(len(treeslist) == 0):
	print("invalid sentence")
else:
	for tree in treeslist:
		print(tree)
		tree.draw()

# sample valid texts
# the girl with long hair slept
# the fierce dog saw a cat
# the three tall black dogs barked
# 
# sample invalid texts
# the boy slept the cat
# a cat chased
