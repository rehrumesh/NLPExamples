__author__ = 'rumesh'
import nltk
from nltk import FreqDist
#print (nltk.corpus.gutenberg.fileids())

file0 = nltk.corpus.gutenberg.fileids()[0]
emmatext = nltk.corpus.gutenberg.raw(file0)
emmatokens = nltk.wordpunct_tokenize(emmatext)
emmawords = [w.lower() for w in emmatokens]


shortwords = emmawords[11:111]
#print(shortwords)

shortdist = FreqDist(shortwords)
#print(shortdist.keys())

#for word in shortdist.keys():
 #   print(word, shortdist[word])


import re
pattern = re.compile('.*[^a-z].*')
nonAlphaMatch = pattern.match('asd5asd')
if nonAlphaMatch: print('matched non-alphabetical')

stopwords = ['to', 'be', 'of', 'the', 'in', 'it', 'was', 'i',
'am', 'she', 'had', 'been', 'is', 'have','could', 'not', 'her',
'he', 'do', 'and', 'would', 'such', 'a', 'his', 'must']


def alphaStopFreqDist(words, stoplist):
    asdist = FreqDist()
    pattern = re.compile('.*[^a-z].*')
    for word in words:
        if not pattern.match(word):
            if not word in stoplist:
                asdist[word] += 1

    return asdist

aa = alphaStopFreqDist(shortwords, stopwords)
##for key in list(aa.keys())[:30]:
##    print(key, aa[key])


bigasdist = alphaStopFreqDist(emmawords, stopwords)
##for key in list(bigasdist.keys())[:30]:
##    print(key, bigasdist[key])

def bigramDist(words, stoplist):
    biDist = FreqDist()
    uniDist = alphaStopFreqDist(words, stopwords)
    for i in range(1, len(words)):
        if words[i-1] in uniDist and words[i] in uniDist:
            biword = words[i-1] +' ' +words[i]
            biDist[biword] += 1
    return biDist


shortbidist = bigramDist(shortwords,stopwords)
emmabidist = bigramDist(emmawords, stopwords)
for key in list(emmabidist.keys())[:30]:
    print(key, emmabidist[key])
