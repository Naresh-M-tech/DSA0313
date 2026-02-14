import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | N [0.4]
VP -> V NP [1.0]
Det -> 'the' [1.0]
N -> 'cat' [0.5] | 'dog' [0.5]
V -> 'chased' [1.0]
""")

parser = ViterbiParser(grammar)
sentence = "the cat chased the dog".split()

for tree in parser.parse(sentence):
    print(tree)
