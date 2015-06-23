#!/usr/bin/python

__author__ = 'rumesh'
#python version 3.4

import nltk
from nltk import load_parser

chart = load_parser('file:Q2C.fcfg')

sentence = "මම ලස්සන කුරුල්ලෙක් දැක්කෙමි".split()
trees = chart.parse(sentence)

treeslist = list(trees)
if(len(treeslist) == 0):
	print("invalid sentence")
else:
	for tree in treeslist:
		print(tree)
		tree.draw()

# sample texts
# නිමේෂා කවියක් ලිව්වාය
# මම ලස්සන කුරුල්ලෙක් දැක්කෙමි
# අපි ලස්සන නිසදැස් ලිව්වෙමු
# ඇය අර කොල දැක්කාය
# මම ලිව්වෙමි
# අපි ලිව්වෙමු

# some unsupported texts
# මම ලිව්වෙමු
# නිමේෂා කවියක් ලිව්වෝය
# අර උස ළමයා කවි ලිව්වෝය
