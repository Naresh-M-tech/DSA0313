import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize

# Download resources (run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

sentence = "The children are playing games"

tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)

lemmatizer = WordNetLemmatizer()

print("Word   POS   Lemma")
for word, tag in pos_tags:
    lemma = lemmatizer.lemmatize(word)
    print(word, tag, lemma)
