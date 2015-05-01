import nltk
from nltk import FreqDist

file0 = nltk.corpus.gutenberg.fileids()[0]
emmatext = nltk.corpus.gutenberg.raw(file0)
emmatokens = nltk.wordpunct_tokenize(emmatext)
emmawords = [w.lower() for w in emmatokens]

porter = nltk.PorterStemmer()
ancaster = nltk.LancasterStemmer()
emmaregstem = [porter.stem(t) for t in emmatokens]

emmaregstem[1:100]

def stem(word):
    for suffix in ['ing','ly','ed','ious','ies','ive','es','s']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

stemmedword = stem('friends')
print(stemmedword)

wnl = nltk.WordNetLemmatizer()
emmalemma = [wnl.lemmatize(t) for t in emmawords]
print(emmalemma[1:100])

