__author__ = 'rumesh'

#1. Chunk Parsing for Base Noun Phrases using Regular Expressions

import nltk

fileid = nltk.corpus.treebank_chunk.fileids()[0]
##for senttree in nltk.corpus.treebank_chunk.chunked_sents(fileid):
##    for t in senttree.subtrees():
##        print(t)
##    print()

##s0 = nltk.corpus.treebank_chunk.chunked_sents(fileid)[0]
##s0.draw()


cp = nltk.RegexpParser("NP: {<DT>?<JJ>*<NN>}")
tagged_tokens = [("the", "DT"), ("little", "JJ"), ("yellow",
"JJ"),("dog", "NN"),("barked", "VBD"), ("at", "IN"), ("the", "DT"),
("cat", "NN")]

senttree = cp.parse(tagged_tokens)
##print(senttree)
##senttree.draw()

NPgrammar1 = r"""
NP: {<DT|PP\$>?<JJ>*<NN>} # determiner/possessive, adjectives and nouns
"""


cp1 = nltk.RegexpParser(NPgrammar1)
chunkscore = nltk.chunk.ChunkScore()

##for fileid in nltk.corpus.treebank_chunk.fileids()[:5]:
##    for chunk_struct in nltk.corpus.treebank_chunk.chunked_sents(fileid):
##        test_sent = cp1.parse(chunk_struct.flatten())
##        chunkscore.score(chunk_struct, test_sent)

##print(chunkscore)

##missed = chunkscore.missed()
##print(len(missed))
##for m in missed[:20]:
##    print(m)

from random import shuffle
##shuffle(missed)
##for m in missed[:20]:
##    print(m)


incorrect = chunkscore.incorrect()
shuffle(incorrect)
##for m in incorrect[:20]:
##    print(m)


NPgrammar2 = r"""
NP: {<DT|PP\$>?<JJ>*<NN|NNS>} # determiner/possessive, adjectives and nouns
{<NNP>+} # sequences of proper nouns
"""

cp2 = nltk.RegexpParser(NPgrammar2)
##chunkscore2 = nltk.chunk.ChunkScore()
##for fileid in nltk.corpus.treebank_chunk.fileids()[:5]:
##    for chunk_struct in nltk.corpus.treebank_chunk.chunked_sents(fileid):
##        test_sent = cp2.parse(chunk_struct.flatten())
##        chunkscore2.score(chunk_struct, test_sent)

##print(chunkscore2)

##NPgrammar3 = r"""
##NP: {<RB|DT|PP\$|PRP\$>?<JJ.*>*<VBN|VBG|NNP|CD>*<NN|NNS>+}
##{<DT>?<CD>+}
##{<DT>?<NNP>+}
##{<DT>+}
##{<WP>+}
##{<PRP>+}
##{<EX>+}
##{<WDT>+}
##"""


NPgrammar3 = r"""
NP:
{<DT>?<JJ|JJR|VBN|VBG>*<CD><JJ|JJR|VBN|VBG>*<NNS|NN>+}
{<DT>?<JJS><NNS|NN>?}
{<DT>?<PRP|NN|NNS><POS><NN|NNP|NNS>*}
{<DT>?<NNP>+<POS><NN|NNP|NNS>*}
{<DT|PRP\$>?<RB>?<JJ|JJR|VBN|VBG>*<NN|NNP|NNS>+}
{<WP|WDT|PRP|EX>}
{<DT><JJ>*<CD>}
{<\$>?<CD>+}
"""
cp3 = nltk.RegexpParser(NPgrammar3)
chunkscore3 = nltk.chunk.ChunkScore()
##for fileid in nltk.corpus.treebank_chunk.fileids()[:5]:
##    for chunk_struct in nltk.corpus.treebank_chunk.chunked_sents(fileid):
##        test_sent = cp3.parse(chunk_struct.flatten())
##        chunkscore3.score(chunk_struct, test_sent)nltk.parse_dependency_grammarnltk.parse_dependency_grammar

nltk.parse_dependency_grammar#print(chunkscore3)

# 2. Techniques for Chunking using the Annotated Data for Training: N-gram chunker

##from nltk.corpus import conll2000
##conll2000.chunked_sents('train.txt')
##
##chunk_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(chtree)]
##for chtree in conll2000.chunked_sents('train.txt')]
##
##print(chunk_data[0])
##
##unigram_chunker = nltk.UnigramTagger(chunk_data)
##print(unigram_chunker.evaluate(chunk_data))
##
##bigram_chunker = nltk.BigramTagger(chunk_data, backoff=unigram_chunker)
##print(bigram_chunker.evaluate(chunk_data))

# 3. Dependency Grammar Parser in NLTK

groucho_dep_grammar = nltk.parse_dependency_grammar("""
'shot' -> 'I' | 'elephant' | 'in'
'elephant' -> 'an' | 'in'
'in' -> 'pajamas'
'pajamas' -> 'my'
""")

##
##print (groucho_dep_grammar)
