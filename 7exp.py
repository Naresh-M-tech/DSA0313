import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "Natural language processing is very interesting"
tokens = word_tokenize(sentence)
tagged_words = pos_tag(tokens)

print("POS Tagged Output:")
for word, tag in tagged_words:
    print(word, "->", tag)
