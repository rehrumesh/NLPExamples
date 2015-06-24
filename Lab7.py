__author__ = 'rumesh'

import nltk
from nltk.corpus import wordnet as wn


# if you get "<bound method Synset.definition of Synset....", make it a method

##print(wn.synsets('dog'))
##print(wn.synset('dog.n.01').lemma_names)
##print(wn.synset('dog.n.01').lemmas)
##print(wn.lemma('dog.n.01.domestic_dog').synset)
##
##for synset in wn.synsets('dog'):
##    print(synset, ": ", synset.lemma_names())

##print(wn.lemmas('dog'))



##print(wn.synset('dog.n.01').definition())
##print(wn.synset('dog.n.01').examples())


##for synset in wn.synsets('dog'):
##    print(synset, ": ", synset.definition())

##
##dog1 = wn.synset('dog.n.01')
##print(dog1.hypernyms())
##print(dog1.root_hypernyms())


good1 = wn.synset('good.a.01')
##print(wn.lemmas('good'))
#####good1.lemmas[0].antonyms()             #not working
##print(wn.synset('walk.v.01').entailments())


right = wn.synset('right_whale.n.01')
orca  = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
##print(right.lowest_common_hypernyms(minke))
##print(right.min_depth())
##print(wn.synset('baleen_whale.n.01').min_depth())
##print(wn.synset('entity.n.01').min_depth())

print(right.path_similarity(minke))
print(right.path_similarity(orca))

cat1 = wn.synset('cat.n.01')
pathscat=cat1.hypernym_paths()
