#!/usr/bin/python

__author__ = 'rumesh'
#python version 3.4

import nltk

grammar = nltk.data.load('Q2B.cfg')
rd_parser = nltk.RecursiveDescentParser(grammar)

sentenceText = "අම්මා පොත දැක්කා".split()
trees = rd_parser.parse(sentenceText)

for tree in trees:
    print(tree)
    tree.draw()

# sample texts
# රුමේෂ් තේ හැදුවා
# නිමේෂා ඉගැන්නුවා
# අම්මා පොත දැක්කා
# පුසා දිව්වා
# රුමේෂ් පොත ලිව්වා
# කැත පුසා ඇවිද්දා
# අර මහත ළමයා අකුරු ලිව්වා
