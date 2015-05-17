__author__ = 'rumesh'

import nltk
from nltk.corpus import brown
# print brown.tagged_sents()[:2]

# print brown.tagged_words()[:50]

brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
# print brown_news_tagged[:50]

# print nltk.corpus.nps_chat.tagged_words()[:50]
from nltk.corpus import treebank
# print treebank.tagged_words()[:50]
# print len(treebank.tagged_words())
# print treebank.tagged_sents()[:2]
# print len(treebank.tagged_sents())

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag,word) for (word,tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:20]) for tag in cfd.conditions())

tagdict = findtags('NN', treebank.tagged_words())
for tag in sorted(tagdict):
    print tag, tagdict[tag]

