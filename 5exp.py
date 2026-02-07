from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["running", "jumps", "easily", "played", "playing"]

print("Word   Stem")
for word in words:
    print(word, "→", ps.stem(word))
