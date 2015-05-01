import nltk
from nltk import FreqDist
print nltk.corpus.gutenberg.fileids()
file0 = nltk.corpus.gutenberg.fileids()[0]
emmatext = nltk.corpus.gutenberg.raw(file0)
emmatokens = nltk.wordpunct_tokenize(emmatext)
emmawords = [w.lower() for w in emmatokens]

shortwords = emmawords[11:111]
shortwords


shortdist = FreqDist(shortwords)
shortdist.keys()

for word in shortdist.keys():
	print word, shortdist[word]

