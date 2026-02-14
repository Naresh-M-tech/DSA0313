from nltk.corpus import wordnet as wn
import nltk

nltk.download('wordnet')

word = "bank"
synsets = wn.synsets(word)

for syn in synsets[:3]:
    print("Synset:", syn.name())
    print("Definition:", syn.definition())
    print("Examples:", syn.examples())
    print()
