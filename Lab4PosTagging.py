__author__ = 'rumesh'

import nltk
from nltk.corpus import treebank

treebank_tagged = treebank.tagged_sents()
treebank_text = treebank.words()
# print len(treebank_text)
# print treebank_text[:50]

default_tagger = nltk.DefaultTagger("NN")
# print default_tagger.tag(treebank_text[:50])
# print default_tagger.evaluate(treebank_tagged)

unigram_tagger = nltk.UnigramTagger(treebank_tagged)
# print unigram_tagger.tag(treebank_text[:50])

size = int(len(treebank_tagged) * 0.9)
treebank_train = treebank_tagged[:size]
treebank_test = treebank_tagged[size:]
unigram_tagger = nltk.UnigramTagger(treebank_train)
# print unigram_tagger.evaluate(treebank_test)

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(treebank_train, backoff=t0)
t2 = nltk.BigramTagger(treebank_train, backoff=t1)
print t2.evaluate(treebank_test)

text = "Three Calgarians have found a rather unusual way of leaving snow and ice behind. They set off this week on foot and by camels on a grueling trek across the burning Arabian desert."
tokens = nltk.wordpunct_tokenize(text)
taggedtext = t2.tag(tokens)
print taggedtext

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag,word) for (word,tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:20]) for tag in cfd.conditions())
    # if python  3.x use the below line as in python 3 cfd.keys() will returns an iteratable but not indexable object. 
    # return dict((tag, list(cfd[tag].keys())[:20]) for tag in cfd.conditions())

tagdictNN = findtags('NN', taggedtext)
for tag in sorted(tagdictNN):
    print tag, tagdictNN[tag]
