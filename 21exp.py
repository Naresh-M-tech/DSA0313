import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

sentence = "The intelligent student solved the problem"
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = RegexpParser(grammar)
tree = chunk_parser.parse(tagged)

print("Noun Phrases:")
for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        print(" ".join(word for word, tag in subtree.leaves()))
