__author__ = "Rumesh"

def gender_features(word):
    return {'last_letter': word[-1]}

#print(gender_features('shrek'))

import nltk
from nltk.corpus import names
#print(names.words('male.txt')[:20])


namesgender = ([(name, 'male') for name in names.words('male.txt')]
               + [(name,'female') for name in names.words('female.txt')])

##print(namesgender[:20])
##print(namesgender[7924:])

import random
random.shuffle(namesgender)
##print(namesgender[:20])


featuresets = [(gender_features(n),g) for (n,g) in namesgender]
##print(featuresets[:20])

train_set, test_set = featuresets[500:],featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

##print(nltk.classify.accuracy(classifier, test_set))
##
##print(classifier.classify(gender_features('Neo')))
##print(classifier.classify(gender_features('Trinity')))
##
##print(classifier.show_most_informative_features(20))

def gender_features2(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    return features


features = gender_features2('Shrek')
#print(features)

featuresets2 = [(gender_features2(n), g) for (n,g) in namesgender]
##for (n,g) in namesgender[:5]:
##    print(n, gender_features2(n), ' \n')


train_set, test_set = featuresets2[500:], featuresets2[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))


train_names = namesgender[1500:]
devtest_names = namesgender[500:1500]
test_names = namesgender[:500]

train_set = [(gender_features(n), g) for (n,g) in train_names]
devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
test_set = [(gender_features(n), g) for (n,g) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, devtest_set))


def geterrors(devtest):
    errors = []
    for (name,tag) in devtest:
        guess = classifier.classify(gender_features(name))
        if guess != tag:
            errors.append((tag,guess,name))
    return errors

errors = geterrors(devtest_names)


def printerrors(errors):
    for (tag,guess,name) in sorted(errors):
        print('correct=%-8s guess=%-8s name=%-30s' % (tag,guess,name))

printerrors(errors)

