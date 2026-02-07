words = ["time", "flies", "like", "arrow"]

pos_probabilities = {
    "time": {"NN": 0.7, "VB": 0.3},
    "flies": {"VB": 0.6, "NNS": 0.4},
    "like": {"IN": 0.5, "VB": 0.5},
    "arrow": {"NN": 0.9, "VB": 0.1}
}

print("Stochastic POS Tagging Output:")
for word in words:
    tag = max(pos_probabilities[word],
              key=pos_probabilities[word].get)
    print(word, "->", tag)
