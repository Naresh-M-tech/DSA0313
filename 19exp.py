from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('wordnet')

sentence = "He deposited money in the bank"
words = word_tokenize(sentence)

sense = lesk(words, "bank")
print("Best Sense:", sense)
print("Definition:", sense.definition())
