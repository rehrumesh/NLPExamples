__author__ = 'rumesh'
import nltk
from nltk import *
file0 = nltk.corpus.gutenberg.fileids()[0]
emmatext = nltk.corpus.gutenberg.raw(file0)

# print type(emmatext)
# print len(emmatext)
shorttext = emmatext[:150]

# for char in shorttext[:10]:
#     print char
#
#
# string1 = "Monty Python"
# string2 = "Holy grail"
# print string1+string2
# print string1 + " and the " + string2

newemmatext = emmatext.replace('\n',' ')
shorttext = newemmatext[:150]
# print shorttext


# Regular expressions for tokenizing text
import re
pword = re.compile('\w+')
# print re.findall(pword, shorttext)

specialtext = "U.S.A. poster-print costs $12.40, with 10% off."
# print re.findall(pword, specialtext)

ptoken = re.compile('(\w+(-\w+)*)')
# print re.findall(ptoken, specialtext)

pabbrev = re.compile('(([A-Z]\.)+)')
# print re.findall(pabbrev, specialtext)
ptoken = re.compile('(\w+(-\w+)*|(A-Z]\.)+)')
#print re.findall(ptoken, specialtext)

ptoken = re.compile('(([A-Z]\.)+|\w+(-\w+)*)')
#print re.findall(ptoken, specialtext)

ptoken = re.compile(r'(([A-Z]\.)+|\w+(-\w+)*|\$?\d+(\.\d+)?)')
#print re.findall(ptoken, specialtext)

ptoken = re.compile(r'''([A-Z]\.)+  # abbreviationss, e.g. U.S.A
    | \w+(-\w+)*                    # words with internal hyphens
    | \$?d+(\.\d+)?                 # currency like $12.40
    ''', re.X)                      # verbose flag

# print re.findall(ptoken, specialtext)

# Regular Expression Tokenizer using NLTK Tokenizer

pattern = r''' (?x)                 # set flag to allow verbose regexps
    ([A-Z]\.)+                      #abbreviations e.g. U.S.A
    | \w+(-\w+)*                    #words with internal hyphens
    | \$?\d+(\.\d+)?%?              #currency and percentages $12.40, 50%
    | \.\.\.                        #ellipsis
    | [][.,;"'?():-_']              #seperate special character tokens
    '''

# print nltk.regexp_tokenize(shorttext, pattern)
# print nltk.regexp_tokenize(specialtext, pattern)

tweetPattern = r''' (?x)            # set flag to allow verbose regexps
    (https?://|www)\S+              # simple URLs
    | (:-\)|;-\))                   # small list of emoticons
    | &(amp|lt|gt|quot);            # XML or HTML entity
    | \#\w+                         # hashtags
    | @\w+                          # mentions
    | \d+:\d+                       # timelike pattern
    | \d+\.\d+                      # number with decimal
    | (\d+,)+?\d{3}(?=([^,]|$))     # number with a comma
    | ([A-Z]\.)+                    # simple abbreviations
    | (--+)                         # multiple dashes
    | \w+(-\w+)*                    # words with internal hyphens or apostrophes
    | ['\".?!,:;]+                  # special characters
    '''

tweet1 = "@natalieohayre I agree #hc09 needs reform- but not by crooked politicians who r clueless about healthcare! #tcot #fishy NO GOV'T TAKEOVER!"
tweet2 = "To Sen. Roland Burris: Affordable, quality health insurance can't wait http://bit.ly/j63je #hc09 #IL #60660"
tweet3 = "RT @karoli: RT @Seriou: .@whitehouse I will stand w/ Obama on #healthcare, I trust him. #p2 #tlot"

print nltk.regexp_tokenize(tweet1, tweetPattern)
print nltk.regexp_tokenize(tweet2, tweetPattern)
print nltk.regexp_tokenize(tweet3, tweetPattern)
